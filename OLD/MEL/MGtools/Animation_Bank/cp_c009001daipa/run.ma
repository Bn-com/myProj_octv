//Maya ASCII 2011 scene
//Name: run.ma
//Last modified: Wed, Jul 11, 2012 08:53:38 AM
//Codeset: 936
requires maya "2011";
requires "stereoCamera" "10.0";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2011";
fileInfo "version" "2011 Hotfix 2 x64";
fileInfo "cutIdentifier" "201006030309-775258";
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
	setAttr ".ns" -type "string" "cp_c009001daipa";
	setAttr ".range" -type "string" "\"1:60\"";
	setAttr ".num" 15;
	setAttr ".nts" -type "string" "cp_c009001daipa:waist_Ctrl; cp_c009001daipa:root_waist_ikCtrl; cp_c009001daipa:RtLeg_Leg_IK; cp_c009001daipa:LfLeg_Leg_IK; cp_c009001daipa:LfArm_Wrist_FK; cp_c009001daipa:LfArm_Elbow_FK; cp_c009001daipa:LfArm_UpArm_FK; cp_c009001daipa:Lf_shoulder; cp_c009001daipa:Rt_shoulder; cp_c009001daipa:RtArm_UpArm_FK; cp_c009001daipa:RtArm_Elbow_FK; cp_c009001daipa:RtArm_Wrist_FK; cp_c009001daipa:head_ctrl; cp_c009001daipa:waist_FK1_ctrl; cp_c009001daipa:waist_FK2_ctrl; ";
createNode transform -n "cp_c009001daipa:waist_Ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ikfk_switch" -ln "ikfk_switch" -min 1000 -max -1 -at "enum";
	addAttr -ci true -sn "second_vis" -ln "second_vis" -min 1000 -max -1 -at "enum";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr -k on ".ikfk_switch";
	setAttr -k on ".second_vis";
	setAttr ".ObjName" -type "string" "cp_c009001daipa:waist_Ctrl";
createNode locator -n "cp_c009001daipa:waist_Ctrl_outPutAnimBank_1Shape" -p "cp_c009001daipa:waist_Ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "cp_c009001daipa:root_waist_ikCtrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "cp_c009001daipa:root_waist_ikCtrl";
createNode locator -n "cp_c009001daipa:root_waist_ikCtrl_outPutAnimBank_1Shape" -p
		 "cp_c009001daipa:root_waist_ikCtrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "raiseBall" -ln "raiseBall" -at "float";
	addAttr -ci true -sn "raiseToeTip" -ln "raiseToeTip" -at "float";
	addAttr -ci true -sn "side" -ln "side" -at "float";
	addAttr -ci true -sn "swivel" -ln "swivel" -at "float";
	addAttr -ci true -sn "roll" -ln "roll" -at "float";
	addAttr -ci true -sn "raiseToe" -ln "raiseToe" -at "float";
	addAttr -ci true -sn "swivelToe" -ln "swivelToe" -at "float";
	addAttr -ci true -sn "twistToe" -ln "twistToe" -at "double";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr -k on ".raiseBall";
	setAttr -k on ".raiseToeTip";
	setAttr -k on ".side";
	setAttr -k on ".swivel";
	setAttr -k on ".roll";
	setAttr -k on ".raiseToe";
	setAttr -k on ".swivelToe";
	setAttr -k on ".twistToe";
	setAttr ".ObjName" -type "string" "cp_c009001daipa:RtLeg_Leg_IK";
createNode locator -n "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1Shape" -p "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "raiseBall" -ln "raiseBall" -at "float";
	addAttr -ci true -sn "raiseToeTip" -ln "raiseToeTip" -at "float";
	addAttr -ci true -sn "side" -ln "side" -at "float";
	addAttr -ci true -sn "swivel" -ln "swivel" -at "float";
	addAttr -ci true -sn "roll" -ln "roll" -at "float";
	addAttr -ci true -sn "raiseToe" -ln "raiseToe" -at "float";
	addAttr -ci true -sn "swivelToe" -ln "swivelToe" -at "float";
	addAttr -ci true -sn "twistToe" -ln "twistToe" -at "double";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr -k on ".raiseBall";
	setAttr -k on ".raiseToeTip";
	setAttr -k on ".side";
	setAttr -k on ".swivel";
	setAttr -k on ".roll";
	setAttr -k on ".raiseToe";
	setAttr -k on ".swivelToe";
	setAttr -k on ".twistToe";
	setAttr ".ObjName" -type "string" "cp_c009001daipa:LfLeg_Leg_IK";
createNode locator -n "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1Shape" -p "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "cp_c009001daipa:LfArm_Wrist_FK_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "cp_c009001daipa:LfArm_Wrist_FK";
createNode locator -n "cp_c009001daipa:LfArm_Wrist_FK_outPutAnimBank_1Shape" -p "cp_c009001daipa:LfArm_Wrist_FK_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "cp_c009001daipa:LfArm_Elbow_FK_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "cp_c009001daipa:LfArm_Elbow_FK";
createNode locator -n "cp_c009001daipa:LfArm_Elbow_FK_outPutAnimBank_1Shape" -p "cp_c009001daipa:LfArm_Elbow_FK_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "cp_c009001daipa:LfArm_UpArm_FK_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "twistPlacement" -ln "twistPlacement" -min 1000 -max -1 -at "enum";
	addAttr -ci true -sn "addTwist" -ln "addTwist" -at "float";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr -k on ".twistPlacement";
	setAttr -k on ".addTwist";
	setAttr ".ObjName" -type "string" "cp_c009001daipa:LfArm_UpArm_FK";
createNode locator -n "cp_c009001daipa:LfArm_UpArm_FK_outPutAnimBank_1Shape" -p "cp_c009001daipa:LfArm_UpArm_FK_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "cp_c009001daipa:Lf_shoulder_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "Arm_follow" -ln "Arm_follow" -min 1000 -max -1 -at "enum";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr -k on ".Arm_follow";
	setAttr ".ObjName" -type "string" "cp_c009001daipa:Lf_shoulder";
createNode locator -n "cp_c009001daipa:Lf_shoulder_outPutAnimBank_1Shape" -p "cp_c009001daipa:Lf_shoulder_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "cp_c009001daipa:Rt_shoulder_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "Arm_follow" -ln "Arm_follow" -min 1000 -max -1 -at "enum";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr -k on ".Arm_follow";
	setAttr ".ObjName" -type "string" "cp_c009001daipa:Rt_shoulder";
createNode locator -n "cp_c009001daipa:Rt_shoulder_outPutAnimBank_1Shape" -p "cp_c009001daipa:Rt_shoulder_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "cp_c009001daipa:RtArm_UpArm_FK_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "twistPlacement" -ln "twistPlacement" -min 1000 -max -1 -at "enum";
	addAttr -ci true -sn "addTwist" -ln "addTwist" -at "float";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr -k on ".twistPlacement";
	setAttr -k on ".addTwist";
	setAttr ".ObjName" -type "string" "cp_c009001daipa:RtArm_UpArm_FK";
createNode locator -n "cp_c009001daipa:RtArm_UpArm_FK_outPutAnimBank_1Shape" -p "cp_c009001daipa:RtArm_UpArm_FK_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "cp_c009001daipa:RtArm_Elbow_FK_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "cp_c009001daipa:RtArm_Elbow_FK";
createNode locator -n "cp_c009001daipa:RtArm_Elbow_FK_outPutAnimBank_1Shape" -p "cp_c009001daipa:RtArm_Elbow_FK_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "cp_c009001daipa:RtArm_Wrist_FK_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "cp_c009001daipa:RtArm_Wrist_FK";
createNode locator -n "cp_c009001daipa:RtArm_Wrist_FK_outPutAnimBank_1Shape" -p "cp_c009001daipa:RtArm_Wrist_FK_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "cp_c009001daipa:head_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "rotation" -ln "rotation" -min 1000 -max -1 -at "enum";
	addAttr -ci true -sn "DYNHatPrimaryCtrl" -ln "DYNHatPrimaryCtrl" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "DYNHatStartFrame" -ln "DYNHatStartFrame" -at "double";
	addAttr -ci true -sn "DYNEaringPrimaryCtrl" -ln "DYNEaringPrimaryCtrl" -min 0 -max 
		1 -at "bool";
	addAttr -ci true -sn "DYNEaringStartFrame" -ln "DYNEaringStartFrame" -at "double";
	addAttr -ci true -sn "DYNNecklacePrimaryCtrl" -ln "DYNNecklacePrimaryCtrl" -min 
		0 -max 1 -at "bool";
	addAttr -ci true -sn "DYNNecklaceStartFrame" -ln "DYNNecklaceStartFrame" -at "double";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr -k on ".rotation";
	setAttr -k on ".DYNHatPrimaryCtrl";
	setAttr -k on ".DYNHatStartFrame";
	setAttr -k on ".DYNEaringPrimaryCtrl";
	setAttr -k on ".DYNEaringStartFrame";
	setAttr -k on ".DYNNecklacePrimaryCtrl";
	setAttr -k on ".DYNNecklaceStartFrame";
	setAttr ".ObjName" -type "string" "cp_c009001daipa:head_ctrl";
createNode locator -n "cp_c009001daipa:head_ctrl_outPutAnimBank_1Shape" -p "cp_c009001daipa:head_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "cp_c009001daipa:waist_FK1_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "cp_c009001daipa:waist_FK1_ctrl";
createNode locator -n "cp_c009001daipa:waist_FK1_ctrl_outPutAnimBank_1Shape" -p "cp_c009001daipa:waist_FK1_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "cp_c009001daipa:waist_FK2_ctrl_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "cp_c009001daipa:waist_FK2_ctrl";
createNode locator -n "cp_c009001daipa:waist_FK2_ctrl_outPutAnimBank_1Shape" -p "cp_c009001daipa:waist_FK2_ctrl_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "cp_c009001daipa:waist_Ctrl_outPutAnimBank_2" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ikfk_switch" -ln "ikfk_switch" -min 1000 -max -1 -at "enum";
	addAttr -ci true -sn "second_vis" -ln "second_vis" -min 1000 -max -1 -at "enum";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr -k on ".ikfk_switch";
	setAttr -k on ".second_vis";
	setAttr ".ObjName" -type "string" "cp_c009001daipa:waist_Ctrl";
createNode locator -n "cp_c009001daipa:waist_Ctrl_outPutAnimBank_2Shape" -p "cp_c009001daipa:waist_Ctrl_outPutAnimBank_2";
	setAttr -k off ".v";
createNode transform -n "cp_c009001daipa:root_waist_ikCtrl_outPutAnimBank_2" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "cp_c009001daipa:root_waist_ikCtrl";
createNode locator -n "cp_c009001daipa:root_waist_ikCtrl_outPutAnimBank_2Shape" -p
		 "cp_c009001daipa:root_waist_ikCtrl_outPutAnimBank_2";
	setAttr -k off ".v";
createNode transform -n "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_2" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "raiseBall" -ln "raiseBall" -at "float";
	addAttr -ci true -sn "raiseToeTip" -ln "raiseToeTip" -at "float";
	addAttr -ci true -sn "side" -ln "side" -at "float";
	addAttr -ci true -sn "swivel" -ln "swivel" -at "float";
	addAttr -ci true -sn "roll" -ln "roll" -at "float";
	addAttr -ci true -sn "raiseToe" -ln "raiseToe" -at "float";
	addAttr -ci true -sn "swivelToe" -ln "swivelToe" -at "float";
	addAttr -ci true -sn "twistToe" -ln "twistToe" -at "double";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr -k on ".raiseBall";
	setAttr -k on ".raiseToeTip";
	setAttr -k on ".side";
	setAttr -k on ".swivel";
	setAttr -k on ".roll";
	setAttr -k on ".raiseToe";
	setAttr -k on ".swivelToe";
	setAttr -k on ".twistToe";
	setAttr ".ObjName" -type "string" "cp_c009001daipa:RtLeg_Leg_IK";
createNode locator -n "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_2Shape" -p "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_2";
	setAttr -k off ".v";
createNode transform -n "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_2" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "raiseBall" -ln "raiseBall" -at "float";
	addAttr -ci true -sn "raiseToeTip" -ln "raiseToeTip" -at "float";
	addAttr -ci true -sn "side" -ln "side" -at "float";
	addAttr -ci true -sn "swivel" -ln "swivel" -at "float";
	addAttr -ci true -sn "roll" -ln "roll" -at "float";
	addAttr -ci true -sn "raiseToe" -ln "raiseToe" -at "float";
	addAttr -ci true -sn "swivelToe" -ln "swivelToe" -at "float";
	addAttr -ci true -sn "twistToe" -ln "twistToe" -at "double";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr -k on ".raiseBall";
	setAttr -k on ".raiseToeTip";
	setAttr -k on ".side";
	setAttr -k on ".swivel";
	setAttr -k on ".roll";
	setAttr -k on ".raiseToe";
	setAttr -k on ".swivelToe";
	setAttr -k on ".twistToe";
	setAttr ".ObjName" -type "string" "cp_c009001daipa:LfLeg_Leg_IK";
createNode locator -n "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_2Shape" -p "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_2";
	setAttr -k off ".v";
createNode transform -n "cp_c009001daipa:LfArm_Wrist_FK_outPutAnimBank_2" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "cp_c009001daipa:LfArm_Wrist_FK";
createNode locator -n "cp_c009001daipa:LfArm_Wrist_FK_outPutAnimBank_2Shape" -p "cp_c009001daipa:LfArm_Wrist_FK_outPutAnimBank_2";
	setAttr -k off ".v";
createNode transform -n "cp_c009001daipa:LfArm_Elbow_FK_outPutAnimBank_2" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "cp_c009001daipa:LfArm_Elbow_FK";
createNode locator -n "cp_c009001daipa:LfArm_Elbow_FK_outPutAnimBank_2Shape" -p "cp_c009001daipa:LfArm_Elbow_FK_outPutAnimBank_2";
	setAttr -k off ".v";
createNode transform -n "cp_c009001daipa:LfArm_UpArm_FK_outPutAnimBank_2" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "twistPlacement" -ln "twistPlacement" -min 1000 -max -1 -at "enum";
	addAttr -ci true -sn "addTwist" -ln "addTwist" -at "float";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr -k on ".twistPlacement";
	setAttr -k on ".addTwist";
	setAttr ".ObjName" -type "string" "cp_c009001daipa:LfArm_UpArm_FK";
createNode locator -n "cp_c009001daipa:LfArm_UpArm_FK_outPutAnimBank_2Shape" -p "cp_c009001daipa:LfArm_UpArm_FK_outPutAnimBank_2";
	setAttr -k off ".v";
createNode transform -n "cp_c009001daipa:Lf_shoulder_outPutAnimBank_2" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "Arm_follow" -ln "Arm_follow" -min 1000 -max -1 -at "enum";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr -k on ".Arm_follow";
	setAttr ".ObjName" -type "string" "cp_c009001daipa:Lf_shoulder";
createNode locator -n "cp_c009001daipa:Lf_shoulder_outPutAnimBank_2Shape" -p "cp_c009001daipa:Lf_shoulder_outPutAnimBank_2";
	setAttr -k off ".v";
createNode transform -n "cp_c009001daipa:Rt_shoulder_outPutAnimBank_2" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "Arm_follow" -ln "Arm_follow" -min 1000 -max -1 -at "enum";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr -k on ".Arm_follow";
	setAttr ".ObjName" -type "string" "cp_c009001daipa:Rt_shoulder";
createNode locator -n "cp_c009001daipa:Rt_shoulder_outPutAnimBank_2Shape" -p "cp_c009001daipa:Rt_shoulder_outPutAnimBank_2";
	setAttr -k off ".v";
createNode transform -n "cp_c009001daipa:RtArm_UpArm_FK_outPutAnimBank_2" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "twistPlacement" -ln "twistPlacement" -min 1000 -max -1 -at "enum";
	addAttr -ci true -sn "addTwist" -ln "addTwist" -at "float";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr -k on ".twistPlacement";
	setAttr -k on ".addTwist";
	setAttr ".ObjName" -type "string" "cp_c009001daipa:RtArm_UpArm_FK";
createNode locator -n "cp_c009001daipa:RtArm_UpArm_FK_outPutAnimBank_2Shape" -p "cp_c009001daipa:RtArm_UpArm_FK_outPutAnimBank_2";
	setAttr -k off ".v";
createNode transform -n "cp_c009001daipa:RtArm_Elbow_FK_outPutAnimBank_2" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "cp_c009001daipa:RtArm_Elbow_FK";
createNode locator -n "cp_c009001daipa:RtArm_Elbow_FK_outPutAnimBank_2Shape" -p "cp_c009001daipa:RtArm_Elbow_FK_outPutAnimBank_2";
	setAttr -k off ".v";
createNode transform -n "cp_c009001daipa:RtArm_Wrist_FK_outPutAnimBank_2" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "cp_c009001daipa:RtArm_Wrist_FK";
createNode locator -n "cp_c009001daipa:RtArm_Wrist_FK_outPutAnimBank_2Shape" -p "cp_c009001daipa:RtArm_Wrist_FK_outPutAnimBank_2";
	setAttr -k off ".v";
createNode transform -n "cp_c009001daipa:head_ctrl_outPutAnimBank_2" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "rotation" -ln "rotation" -min 1000 -max -1 -at "enum";
	addAttr -ci true -sn "DYNHatPrimaryCtrl" -ln "DYNHatPrimaryCtrl" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "DYNHatStartFrame" -ln "DYNHatStartFrame" -at "double";
	addAttr -ci true -sn "DYNEaringPrimaryCtrl" -ln "DYNEaringPrimaryCtrl" -min 0 -max 
		1 -at "bool";
	addAttr -ci true -sn "DYNEaringStartFrame" -ln "DYNEaringStartFrame" -at "double";
	addAttr -ci true -sn "DYNNecklacePrimaryCtrl" -ln "DYNNecklacePrimaryCtrl" -min 
		0 -max 1 -at "bool";
	addAttr -ci true -sn "DYNNecklaceStartFrame" -ln "DYNNecklaceStartFrame" -at "double";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr -k on ".rotation";
	setAttr -k on ".DYNHatPrimaryCtrl";
	setAttr -k on ".DYNHatStartFrame";
	setAttr -k on ".DYNEaringPrimaryCtrl";
	setAttr -k on ".DYNEaringStartFrame";
	setAttr -k on ".DYNNecklacePrimaryCtrl";
	setAttr -k on ".DYNNecklaceStartFrame";
	setAttr ".ObjName" -type "string" "cp_c009001daipa:head_ctrl";
createNode locator -n "cp_c009001daipa:head_ctrl_outPutAnimBank_2Shape" -p "cp_c009001daipa:head_ctrl_outPutAnimBank_2";
	setAttr -k off ".v";
createNode transform -n "cp_c009001daipa:waist_FK1_ctrl_outPutAnimBank_2" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "cp_c009001daipa:waist_FK1_ctrl";
createNode locator -n "cp_c009001daipa:waist_FK1_ctrl_outPutAnimBank_2Shape" -p "cp_c009001daipa:waist_FK1_ctrl_outPutAnimBank_2";
	setAttr -k off ".v";
createNode transform -n "cp_c009001daipa:waist_FK2_ctrl_outPutAnimBank_2" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "cp_c009001daipa:waist_FK2_ctrl";
createNode locator -n "cp_c009001daipa:waist_FK2_ctrl_outPutAnimBank_2Shape" -p "cp_c009001daipa:waist_FK2_ctrl_outPutAnimBank_2";
	setAttr -k off ".v";
createNode animCurveTL -n "cp_c009001daipa:waist_Ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0.38462733391759213 6 -0.4 7 -0.39825846980397417 
		12 0.4 13 0.38462733391759213;
	setAttr -s 5 ".kix[0:4]"  0.041666671633720398 0.85264283418655396 
		0.68966537714004517 0.76178967952728271 0.041666671633720398;
	setAttr -s 5 ".kiy[0:4]"  -0.086720980703830719 -0.52249425649642944 
		0.72412824630737305 0.64782446622848511 -0.086720980703830719;
	setAttr -s 5 ".kox[0:4]"  0.43307393789291382 0.85264295339584351 
		0.68966537714004517 0.76178967952728271 0.43307393789291382;
	setAttr -s 5 ".koy[0:4]"  -0.90135836601257324 -0.52249401807785034 
		0.72412824630737305 0.64782440662384033 -0.90135836601257324;
createNode animCurveTL -n "cp_c009001daipa:waist_Ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 11 ".ktv[0:10]"  1 -0.8033230891458587 2 -0.73444302121663796 
		4 0.19897493080965684 5 0.19254931498214672 6 -0.28794141487989716 7 -0.8033230891458587 
		8 -0.73444302121663796 10 0.19897493080965684 11 0.19273094214668635 12 -0.30030235670670391 
		13 -0.8033230891458587;
	setAttr -s 11 ".kix[0:10]"  0.65546047687530518 0.13482001423835754 
		0.57466703653335571 0.24188598990440369 0.070173755288124084 0.65761339664459229 
		0.13617889583110809 0.55314421653747559 0.49805524945259094 0.067307420074939728 
		0.65975040197372437;
	setAttr -s 11 ".kiy[0:10]"  -0.75522953271865845 0.99087017774581909 
		0.81838732957839966 -0.97030472755432129 -0.99753481149673462 -0.75335556268692017 
		0.99068427085876465 0.83308553695678711 -0.8671453595161438 -0.99773234128952026 
		-0.75148481130599976;
	setAttr -s 11 ".kox[0:10]"  0.65546047687530518 0.13481996953487396 
		0.57466703653335571 0.24188593029975891 0.070173755288124084 0.65761339664459229 
		0.13617891073226929 0.55314415693283081 0.49805521965026855 0.067307405173778534 
		0.65975040197372437;
	setAttr -s 11 ".koy[0:10]"  -0.75522953271865845 0.99087011814117432 
		0.81838732957839966 -0.97030472755432129 -0.99753481149673462 -0.75335562229156494 
		0.99068427085876465 0.83308553695678711 -0.8671453595161438 -0.99773228168487549 
		-0.75148481130599976;
createNode animCurveTL -n "cp_c009001daipa:waist_Ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 0 7 8.0953576081999667 10 11.992588544451927 
		13 16.761371939379117;
	setAttr -s 4 ".kit[0:3]"  9 10 10 9;
	setAttr -s 4 ".kot[0:3]"  9 10 10 9;
createNode animCurveTA -n "cp_c009001daipa:waist_Ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 16.509832958918931 4 14.431316417628221 
		7 16.509832958918931 10 14.431316417628221 13 16.509832958918931;
	setAttr -s 5 ".kit[1:4]"  10 3 10 3;
	setAttr -s 5 ".kot[1:4]"  10 3 10 3;
createNode animCurveTA -n "cp_c009001daipa:waist_Ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 4.8148149472695785 3 10 7 -4.8148137551766554 
		9 -10 13 4.814816934090949;
	setAttr -s 5 ".kit[0:4]"  1 3 10 3 1;
	setAttr -s 5 ".kot[0:4]"  1 3 10 3 1;
	setAttr -s 5 ".kix[0:4]"  0.50659406185150146 1 0.58226674795150757 
		1 0.57297205924987793;
	setAttr -s 5 ".kiy[0:4]"  0.86218476295471191 0 -0.81299775838851929 
		0 0.81957495212554932;
	setAttr -s 5 ".kox[0:4]"  0.58355569839477539 1 0.58226674795150757 
		1 0.57297194004058838;
	setAttr -s 5 ".koy[0:4]"  0.81207311153411865 0 -0.81299775838851929 
		0 0.81957501173019409;
createNode animCurveTA -n "cp_c009001daipa:waist_Ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 5 7 -5 13 5;
createNode animCurveTU -n "cp_c009001daipa:waist_Ctrl_outPutAnimBank_1_ikfk_switch";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 2 5 2 7 2 9 2 13 2;
	setAttr -s 5 ".kot[0:4]"  5 5 5 5 5;
createNode animCurveTU -n "cp_c009001daipa:waist_Ctrl_outPutAnimBank_1_second_vis";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 5 0 7 0 9 0 13 0;
	setAttr -s 5 ".kot[0:4]"  5 5 5 5 5;
createNode animCurveTL -n "cp_c009001daipa:root_waist_ikCtrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTL -n "cp_c009001daipa:root_waist_ikCtrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTL -n "cp_c009001daipa:root_waist_ikCtrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTA -n "cp_c009001daipa:root_waist_ikCtrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTA -n "cp_c009001daipa:root_waist_ikCtrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 0 4 2 10 -2 13 0.06423037296393555;
	setAttr -s 4 ".kit[0:3]"  1 3 3 1;
	setAttr -s 4 ".kot[0:3]"  1 3 3 1;
	setAttr -s 4 ".kix[0:3]"  0.95656079053878784 1 1 0.9552081823348999;
	setAttr -s 4 ".kiy[0:3]"  0.29153302311897278 0 0 0.29593482613563538;
	setAttr -s 4 ".kox[0:3]"  0.95656079053878784 1 1 0.9552081823348999;
	setAttr -s 4 ".koy[0:3]"  0.291532963514328 0 0 0.29593485593795776;
createNode animCurveTA -n "cp_c009001daipa:root_waist_ikCtrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 3.0000000000000004 7 -3.0000000000000004 
		13 3.0000000000000004;
createNode animCurveTL -n "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 0.45910039198848906 6 0.45545569501248773 
		7 0.45545569501248773 8 0.45545569501248773 10 0.45545569501248773 13 0.45910039198848906;
	setAttr -s 6 ".kit[0:5]"  3 10 10 10 10 3;
	setAttr -s 6 ".kot[0:5]"  3 10 10 10 10 3;
createNode animCurveTL -n "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 13 ".ktv[0:12]"  1 2.0964702848911632 2 1.0806296514920453 
		3 0.6428663434319154 4 1.106190712862251 5 1.0989394466396112 6 0.12037026288760333 
		7 0 8 0 9 -0.031258909670084767 10 0.4463800103914255 11 1.8140373532012719 12 2.5612793467033597 
		13 2.0964702848911632;
	setAttr -s 13 ".kit[0:12]"  1 10 1 10 10 1 10 10 
		10 1 10 10 1;
	setAttr -s 13 ".kot[0:12]"  1 10 1 10 10 1 10 10 
		10 1 10 10 1;
	setAttr -s 13 ".kix[0:12]"  0.038139384239912033 0.057234793901443481 
		0.95817941427230835 1 1 0.17913900315761566 1 1 1 0.12319459021091461 0.039372429251670837 
		0.28299397230148315 0.029119981452822685;
	setAttr -s 13 ".kiy[0:12]"  -0.99927246570587158 -0.99836075305938721 
		0.28616812825202942 0 0 -0.98382377624511719 0 0 0 0.99238258600234985 0.99922460317611694 
		0.95912164449691772 -0.9995759129524231;
	setAttr -s 13 ".kox[0:12]"  0.039582237601280212 0.057234793901443481 
		0.95817917585372925 1 1 0.17913895845413208 1 1 1 0.12319457530975342 0.039372429251670837 
		0.28299397230148315 0.029119983315467834;
	setAttr -s 13 ".koy[0:12]"  -0.99921631813049316 -0.99836075305938721 
		0.28616902232170105 0 0 -0.98382377624511719 0 0 0 0.99238252639770508 0.99922460317611694 
		0.95912164449691772 -0.9995759129524231;
createNode animCurveTL -n "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 13 ".ktv[0:12]"  1 -5.816889968164686 2 -2.8387141270168765 
		3 1.9712145111043302 4 4.9505542371176627 5 7.0036268682164922 6 7.3163765687481206 
		7 7.3163765687481206 8 7.3163765687481206 9 7.3703364105519507 10 6.9126809219840908 
		11 6.8753053497519918 12 9.014804800398343 13 10.944481971214429;
	setAttr -s 13 ".kit[0:12]"  1 10 10 1 10 10 3 10 
		10 3 10 10 1;
	setAttr -s 13 ".kot[0:12]"  1 10 10 1 10 10 3 10 
		10 3 10 10 1;
	setAttr -s 13 ".kix[0:12]"  0.016631057485938072 0.010699465870857239 
		0.010697868652641773 0.017037270590662956 0.035202000290155411 1 1 1 0.20216375589370728 
		1 1 0.020474873483181 0.013523144647479057;
	setAttr -s 13 ".kiy[0:12]"  0.99986165761947632 0.99994277954101563 
		0.99994277954101563 0.9998549222946167 0.99938023090362549 0 0 0 -0.97935175895690918 
		0 0 0.99979037046432495 0.99990856647491455;
	setAttr -s 13 ".kox[0:12]"  0.016248956322669983 0.010699465870857239 
		0.010697868652641773 0.017037270590662956 0.035202000290155411 1 1 1 0.20216375589370728 
		1 1 0.020474873483181 0.013523140922188759;
	setAttr -s 13 ".koy[0:12]"  0.99986797571182251 0.99994277954101563 
		0.99994277954101563 0.99985486268997192 0.99938023090362549 0 0 0 -0.97935175895690918 
		0 0 0.99979037046432495 0.99990856647491455;
createNode animCurveTA -n "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  1 0 3 0 4 0 6 0 7 0 8 0 10 0 13 0;
	setAttr -s 8 ".kit[0:7]"  3 10 10 10 10 10 10 3;
	setAttr -s 8 ".kot[0:7]"  3 10 10 10 10 10 10 3;
createNode animCurveTA -n "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 -4.1085025456484328 3 -7.2814440433212981 
		4 -12.538426630754913 6 -7.2814440433212981 7 -7.2814440433212981 8 -7.2814440433212981 
		10 -8.5036012940625252 11 -6.1475156220904781 13 -4.1085025456484328;
	setAttr -s 9 ".kit[0:8]"  3 10 10 10 10 10 10 1 
		3;
	setAttr -s 9 ".kot[0:8]"  3 10 10 10 10 10 10 1 
		3;
	setAttr -s 9 ".kix[7:8]"  0.69050306081771851 1;
	setAttr -s 9 ".kiy[7:8]"  0.72332954406738281 0;
	setAttr -s 9 ".kox[7:8]"  0.69050312042236328 1;
	setAttr -s 9 ".koy[7:8]"  0.72332948446273804 0;
createNode animCurveTA -n "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 -9.1368053204204909 2 -7.9818965593802469 
		3 -4.2775507787446205 6 0 7 0 8 0 10 -3.6664718602184161 11 -6.3793410450000128 13 
		-9.1368053204204909;
	setAttr -s 9 ".kit[0:8]"  3 1 1 10 10 10 1 1 
		3;
	setAttr -s 9 ".kot[0:8]"  3 1 1 10 10 10 1 1 
		3;
	setAttr -s 9 ".kix[1:8]"  0.71138191223144531 0.62563824653625488 
		1 1 1 0.61713892221450806 0.65805685520172119 1;
	setAttr -s 9 ".kiy[1:8]"  0.70280569791793823 0.7801133394241333 
		0 0 0 -0.78685426712036133 -0.7529681921005249 0;
	setAttr -s 9 ".kox[1:8]"  0.71138197183609009 0.62563818693161011 
		1 1 1 0.61713898181915283 0.65805685520172119 1;
	setAttr -s 9 ".koy[1:8]"  0.70280569791793823 0.7801133394241333 
		0 0 0 -0.78685414791107178 -0.75296831130981445 0;
createNode animCurveTU -n "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1_raiseBall";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  1 0 3 0 6 0 7 0 8 3.4000000953674316 9 
		0 10 0 13 0;
createNode animCurveTU -n "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1_raiseToeTip";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  1 111.59999847412109 2 92.116668701171875 
		3 45.701667785644531 4 17.349994659423828 5 -15.108477592468262 6 -1.7999999523162842 
		7 0 8 0 9 18.400001525878906 10 54.600006103515625 12 113.34999847412109 13 111.59999847412109;
	setAttr -s 12 ".kit[0:11]"  1 10 10 1 10 10 10 10 
		10 10 1 1;
	setAttr -s 12 ".kot[0:11]"  1 10 10 1 10 10 10 10 
		10 10 1 1;
	setAttr -s 12 ".kix[0:11]"  0.0054314816370606422 0.0012645731912925839 
		0.0011145778698846698 0.0028716560918837786 0.0043515702709555626 0.0055155833251774311 
		1 1 0.0015262492233887315 0.0013164812698960304 0.008700639009475708 0.0068298066034913063;
	setAttr -s 12 ".kiy[0:11]"  -0.99998527765274048 -0.99999922513961792 
		-0.99999940395355225 -0.99999594688415527 -0.99999058246612549 0.99998486042022705 
		0 0 0.99999886751174927 0.99999910593032837 0.99996215105056763 -0.99997669458389282;
	setAttr -s 12 ".kox[0:11]"  0.0054314807057380676 0.0012645731912925839 
		0.0011145778698846698 0.0028716556262224913 0.0043515702709555626 0.0055155833251774311 
		1 1 0.0015262492233887315 0.0013164812698960304 0.008700639009475708 0.0068298056721687317;
	setAttr -s 12 ".koy[0:11]"  -0.99998527765274048 -0.99999922513961792 
		-0.99999940395355225 -0.9999958872795105 -0.99999058246612549 0.99998486042022705 
		0 0 0.99999886751174927 0.99999910593032837 0.9999622106552124 -0.99997669458389282;
createNode animCurveTU -n "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1_side";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  1 0 3 0 6 0 7 0 8 0 10 0 13 0;
createNode animCurveTU -n "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1_swivel";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  1 0 3 0 6 0 7 0 8 0 10 0 13 0;
createNode animCurveTU -n "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1_roll";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  1 0 3 0 6 0 7 0 8 0 10 0 13 0;
createNode animCurveTU -n "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1_raiseToe";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  1 -25.299999237060547 3 0 5 20.5 6 9.793655475729814 
		7 0 8 0 10 0 13 -25.299999237060547;
	setAttr -s 8 ".kit[0:7]"  3 10 10 1 10 10 10 3;
	setAttr -s 8 ".kot[0:7]"  3 10 10 1 10 10 10 3;
	setAttr -s 8 ".kix[3:7]"  0.0035323176998645067 1 1 1 1;
	setAttr -s 8 ".kiy[3:7]"  -0.99999374151229858 0 0 0 0;
	setAttr -s 8 ".kox[3:7]"  0.003532318165525794 1 1 1 1;
	setAttr -s 8 ".koy[3:7]"  -0.99999380111694336 0 0 0 0;
createNode animCurveTU -n "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1_swivelToe";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  1 0 3 0 6 0 7 0 8 0 10 0 13 0;
createNode animCurveTU -n "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1_twistToe";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  1 0 3 0 6 0 7 0 8 0 10 0 13 0;
createNode animCurveTL -n "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -0.64825357777019976 3 -0.64825357777019976 
		4 -0.64825357777019976 12 -0.64825357777019976 13 -0.64825357777019976;
createNode animCurveTL -n "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  1 -1.4571677198205177e-016 3 -1.4571677198205177e-016 
		4 0.61189607404510404 5 1.9591470569443796 6 2.7412092650079107 7 1.7060575786909919 
		8 0.52335942154551962 9 0.63161249160636268 10 1.0421314568109357 11 1.0270479018523921 
		12 -1.4571677198205177e-016 13 -1.4571677198205177e-016;
	setAttr -s 12 ".kit[7:11]"  1 10 1 1 3;
	setAttr -s 12 ".kot[7:11]"  1 10 1 1 3;
	setAttr -s 12 ".kix[7:11]"  0.3626444935798645 1 0.68407732248306274 
		0.27588382363319397 1;
	setAttr -s 12 ".kiy[7:11]"  0.93192762136459351 0 -0.72940957546234131 
		-0.96119099855422974 0;
	setAttr -s 12 ".kox[7:11]"  0.3626444935798645 1 0.68407726287841797 
		0.27588361501693726 1;
	setAttr -s 12 ".koy[7:11]"  0.93192756175994873 0 -0.72940963506698608 
		-0.96119105815887451 0;
createNode animCurveTL -n "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  1 -1.2 3 -1.2 4 -1.4006171048126714 5 -1.2889092911197986 
		6 0.028191899823270875 7 2.3061607549622964 8 5.3975588305646447 9 9.5777952758995006 
		10 13.245140894674345 11 15.401285978332968 12 15.561371939379114 13 15.561371939379114;
	setAttr -s 12 ".kit[2:11]"  1 1 10 10 10 10 1 1 
		10 10;
	setAttr -s 12 ".kot[2:11]"  1 1 10 10 10 10 1 1 
		10 10;
	setAttr -s 12 ".kix[2:11]"  0.75002944469451904 0.044274482876062393 
		0.023173665627837181 0.015518274158239365 0.011459304019808769 0.010618381202220917 
		0.015192680992186069 0.067967407405376434 1 1;
	setAttr -s 12 ".kiy[2:11]"  -0.66140449047088623 0.99901938438415527 
		0.99973142147064209 0.99987959861755371 0.99993431568145752 0.99994361400604248 0.99988466501235962 
		0.99768757820129395 0 0;
	setAttr -s 12 ".kox[2:11]"  0.75002944469451904 0.044274482876062393 
		0.023173665627837181 0.015518274158239365 0.011459304019808769 0.010618381202220917 
		0.015192685648798943 0.067967399954795837 1 1;
	setAttr -s 12 ".koy[2:11]"  -0.66140449047088623 0.99901944398880005 
		0.99973142147064209 0.99987959861755371 0.99993431568145752 0.99994361400604248 0.99988460540771484 
		0.99768757820129395 0 0;
createNode animCurveTA -n "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 3 0 4 0 12 0 13 0;
createNode animCurveTA -n "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  1 7.5861487364620919 3 7.5861487364620919 
		4 6.4326160035022681 6 2.5605759366068148 8 5.1174285731688292 12 7.5861487364620919 
		13 7.5861487364620919;
	setAttr -s 7 ".kit[2:6]"  1 1 1 10 10;
	setAttr -s 7 ".kot[2:6]"  1 1 1 10 10;
	setAttr -s 7 ".kix[2:6]"  0.84169971942901611 0.91898429393768311 
		0.92329508066177368 1 1;
	setAttr -s 7 ".kiy[2:6]"  -0.53994596004486084 -0.39429429173469543 
		0.3840915858745575 0 0;
	setAttr -s 7 ".kox[2:6]"  0.84169965982437134 0.91898429393768311 
		0.92329508066177368 1 1;
	setAttr -s 7 ".koy[2:6]"  -0.53994601964950562 -0.39429429173469543 
		0.38409152626991272 0 0;
createNode animCurveTA -n "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 0 3 0 4 2.3070654659196532 8 8.1464053987921634 
		12 0 13 0;
	setAttr -s 6 ".kit[2:5]"  1 10 10 10;
	setAttr -s 6 ".kot[2:5]"  1 10 10 10;
	setAttr -s 6 ".kix[2:5]"  0.75554925203323364 0.9927828311920166 
		1 1;
	setAttr -s 6 ".kiy[2:5]"  0.65509188175201416 -0.119925856590271 
		0 0;
	setAttr -s 6 ".kox[2:5]"  0.75554925203323364 0.9927828311920166 
		1 1;
	setAttr -s 6 ".koy[2:5]"  0.65509182214736938 -0.119925856590271 
		0 0;
createNode animCurveTU -n "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1_raiseBall";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 0 2 13.90000057220459 3 0 4 0 12 0 13 
		0;
	setAttr -s 6 ".kit[0:5]"  3 10 1 10 10 10;
	setAttr -s 6 ".kot[0:5]"  3 10 1 10 10 10;
	setAttr -s 6 ".kix[2:5]"  0.0037791812792420387 1 1 1;
	setAttr -s 6 ".kiy[2:5]"  -0.99999284744262695 0 0 0;
	setAttr -s 6 ".kox[2:5]"  0.0037791822105646133 1 1 1;
	setAttr -s 6 ".koy[2:5]"  -0.99999290704727173 0 0 0;
createNode animCurveTU -n "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1_raiseToeTip";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  1 0 2 0 3 33.199996948242187 4 61.100002288818359 
		6 116.45370483398437 7 103 8 73.318558540585229 9 38.05952488167938 10 12.946810051143977 
		11 -11.022356986999512 12 0 13 0;
	setAttr -s 12 ".kit[5:11]"  1 10 1 1 10 10 10;
	setAttr -s 12 ".kot[5:11]"  1 10 1 1 10 10 10;
	setAttr -s 12 ".kix[5:11]"  0.0015439761336892843 0.0012832256034016609 
		0.0013952433364465833 0.0021525342017412186 0.0064364587888121605 1 1;
	setAttr -s 12 ".kiy[5:11]"  -0.99999880790710449 -0.99999922513961792 
		-0.99999904632568359 -0.99999767541885376 -0.99997925758361816 0 0;
	setAttr -s 12 ".kox[5:11]"  0.0015439760172739625 0.0012832256034016609 
		0.0013952433364465833 0.0021525337360799313 0.0064364587888121605 1 1;
	setAttr -s 12 ".koy[5:11]"  -0.99999880790710449 -0.99999922513961792 
		-0.99999904632568359 -0.99999767541885376 -0.99997925758361816 0 0;
createNode animCurveTU -n "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1_side";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 3 0 4 0 12 0 13 0;
createNode animCurveTU -n "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1_swivel";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 3 0 4 0 12 0 13 0;
createNode animCurveTU -n "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1_roll";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 3 0 4 0 12 0 13 0;
createNode animCurveTU -n "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1_raiseToe";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  1 0 3 0 4 0 5 -7.9999995231628418 8 -25.854808807373047 
		11 24.774473190307617 12 0 13 0;
	setAttr -s 8 ".kit[0:7]"  3 10 10 1 10 10 1 3;
	setAttr -s 8 ".kot[0:7]"  3 10 10 1 10 10 1 3;
	setAttr -s 8 ".kix[3:7]"  0.0043848925270140171 0.0076276659965515137 
		0.0064461198635399342 0.0019693728536367416 1;
	setAttr -s 8 ".kiy[3:7]"  -0.99999040365219116 0.99997091293334961 
		0.99997925758361816 -0.99999809265136719 0;
	setAttr -s 8 ".kox[3:7]"  0.0043848920613527298 0.0076276659965515137 
		0.0064461198635399342 0.0019693728536367416 1;
	setAttr -s 8 ".koy[3:7]"  -0.99999040365219116 0.99997091293334961 
		0.99997925758361816 -0.99999809265136719 0;
createNode animCurveTU -n "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1_swivelToe";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 3 0 4 0 12 0 13 0;
createNode animCurveTU -n "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1_twistToe";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 3 0 4 0 12 0 13 0;
createNode animCurveTA -n "cp_c009001daipa:LfArm_Wrist_FK_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 14.797168765717032 4 22.262865141960368 
		13 14.797168765717032;
	setAttr -s 3 ".kit[1:2]"  3 1;
	setAttr -s 3 ".kot[1:2]"  3 1;
	setAttr -s 3 ".kix[2]"  0.99999397993087769;
	setAttr -s 3 ".kiy[2]"  0.0034730467014014721;
	setAttr -s 3 ".kox[2]"  0.99999397993087769;
	setAttr -s 3 ".koy[2]"  0.003473060904070735;
createNode animCurveTA -n "cp_c009001daipa:LfArm_Wrist_FK_outPutAnimBank_1_rotateY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 3.9716138967504131 4 -1.028386103249588 
		7 -6.0283861032495887 13 3.9716138967504131;
	setAttr -s 4 ".kit[0:3]"  9 1 1 1;
	setAttr -s 4 ".kot[0:3]"  9 1 1 1;
	setAttr -s 4 ".kix[1:3]"  0.75361311435699463 0.99188739061355591 
		0.97196114063262939;
	setAttr -s 4 ".kiy[1:3]"  -0.65731823444366455 -0.12711995840072632 
		0.2351418137550354;
	setAttr -s 4 ".kox[1:3]"  0.75361299514770508 0.99188739061355591 
		0.97196108102798462;
	setAttr -s 4 ".koy[1:3]"  -0.65731847286224365 -0.12711991369724274 
		0.23514185845851898;
createNode animCurveTA -n "cp_c009001daipa:LfArm_Wrist_FK_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 24.224637499946031 4 32.076610819193775 
		10 17.460173126713627 13 24.222133153761842;
	setAttr -s 4 ".kix[0:3]"  0.5897795557975769 0.96637123823165894 
		0.99927067756652832 0.59333348274230957;
	setAttr -s 4 ".kiy[0:3]"  0.80756425857543945 0.25715106725692749 
		-0.038185302168130875 0.80495679378509521;
	setAttr -s 4 ".kox[0:3]"  0.59876221418380737 0.96637123823165894 
		0.99927067756652832 0.58385241031646729;
	setAttr -s 4 ".koy[0:3]"  0.80092686414718628 0.25715115666389465 
		-0.038185283541679382 0.81185990571975708;
createNode animCurveTA -n "cp_c009001daipa:LfArm_Elbow_FK_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 2 0 13 0;
	setAttr -s 3 ".kit[1:2]"  9 10;
	setAttr -s 3 ".kot[1:2]"  9 10;
createNode animCurveTA -n "cp_c009001daipa:LfArm_Elbow_FK_outPutAnimBank_1_rotateY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -26.024979506583499 3 -34.13370373675432 
		7 -47.74778769826441 12 -25.686427562727307 13 -26.056677894362455;
	setAttr -s 5 ".kit[2:4]"  9 1 1;
	setAttr -s 5 ".kot[2:4]"  9 1 1;
	setAttr -s 5 ".kix[0:4]"  0.69405531883239746 0.40192535519599915 
		0.93065738677978516 0.82519161701202393 0.75087141990661621;
	setAttr -s 5 ".kiy[0:4]"  -0.71992170810699463 -0.91567248106002808 
		0.36589175462722778 0.5648530125617981 -0.66044843196868896;
	setAttr -s 5 ".kox[0:4]"  0.69405519962310791 0.40192538499832153 
		0.93065738677978516 0.82519161701202393 0.75087147951126099;
	setAttr -s 5 ".koy[0:4]"  -0.71992182731628418 -0.9156724214553833 
		0.36589175462722778 0.56485295295715332 -0.66044837236404419;
createNode animCurveTA -n "cp_c009001daipa:LfArm_Elbow_FK_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 2 0 13 0;
	setAttr -s 3 ".kit[1:2]"  9 10;
	setAttr -s 3 ".kot[1:2]"  9 10;
createNode animCurveTA -n "cp_c009001daipa:LfArm_UpArm_FK_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 -19.988588480493895 4 -16.049855334054886 
		10 -22.753707455441077 13 -19.988588480493895;
	setAttr -s 4 ".kit[0:3]"  1 10 10 1;
	setAttr -s 4 ".kot[0:3]"  1 10 10 1;
	setAttr -s 4 ".kix[0:3]"  0.74927842617034912 0.99182033538818359 
		1 0.81639307737350464;
	setAttr -s 4 ".kiy[0:3]"  0.66225522756576538 -0.12764179706573486 
		0 0.57749664783477783;
	setAttr -s 4 ".kox[0:3]"  0.74927842617034912 0.99182033538818359 
		1 0.81639307737350464;
	setAttr -s 4 ".koy[0:3]"  0.66225516796112061 -0.12764179706573486 
		0 0.57749664783477783;
createNode animCurveTA -n "cp_c009001daipa:LfArm_UpArm_FK_outPutAnimBank_1_rotateY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 10.013115204228884 4 -5.1473506268854585 
		10 19.442361127792367 13 10.013115204228884;
	setAttr -s 4 ".kit[2:3]"  10 1;
	setAttr -s 4 ".kot[2:3]"  10 1;
	setAttr -s 4 ".kix[0:3]"  0.42321768403053284 0.88057076930999756 
		0.81707650423049927 0.45123010873794556;
	setAttr -s 4 ".kiy[0:3]"  -0.90602803230285645 -0.47391468286514282 
		0.57652926445007324 -0.89240765571594238;
	setAttr -s 4 ".kox[0:3]"  0.42957112193107605 0.88057076930999756 
		0.81707650423049927 0.45122948288917542;
	setAttr -s 4 ".koy[0:3]"  -0.90303307771682739 -0.47391471266746521 
		0.57652926445007324 -0.89240801334381104;
createNode animCurveTA -n "cp_c009001daipa:LfArm_UpArm_FK_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -53.869185624778481 4 -56.862220751904125 
		7 -71.240229843408173 10 -57.200733755765846 13 -53.869185624778481;
	setAttr -s 5 ".kit[2:4]"  10 1 1;
	setAttr -s 5 ".kot[2:4]"  10 1 1;
	setAttr -s 5 ".kix[0:4]"  0.99951934814453125 0.77740973234176636 
		0.99972087144851685 0.64281618595123291 0.99765431880950928;
	setAttr -s 5 ".kiy[0:4]"  0.031002424657344818 -0.62899458408355713 
		-0.023626072332262993 0.76602041721343994 0.068453334271907806;
	setAttr -s 5 ".kox[0:4]"  0.99951928853988647 0.77740973234176636 
		0.99972087144851685 0.64281630516052246 0.99765431880950928;
	setAttr -s 5 ".koy[0:4]"  0.031002113595604897 -0.62899458408355713 
		-0.023626072332262993 0.76602041721343994 0.068453341722488403;
createNode animCurveTU -n "cp_c009001daipa:LfArm_UpArm_FK_outPutAnimBank_1_twistPlacement";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "cp_c009001daipa:LfArm_UpArm_FK_outPutAnimBank_1_addTwist";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTL -n "cp_c009001daipa:Lf_shoulder_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTL -n "cp_c009001daipa:Lf_shoulder_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTL -n "cp_c009001daipa:Lf_shoulder_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTA -n "cp_c009001daipa:Lf_shoulder_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTA -n "cp_c009001daipa:Lf_shoulder_outPutAnimBank_1_rotateY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 0 4 -5 10 5 13 0;
	setAttr -s 4 ".kit[2:3]"  10 1;
	setAttr -s 4 ".kot[2:3]"  10 1;
	setAttr -s 4 ".kix[0:3]"  0.76377081871032715 0.99303281307220459 
		0.97397536039352417 0.78570222854614258;
	setAttr -s 4 ".kiy[0:3]"  -0.64548748731613159 -0.11783847212791443 
		0.22665435075759888 -0.61860501766204834;
	setAttr -s 4 ".kox[0:3]"  0.77449214458465576 0.99303281307220459 
		0.97397536039352417 0.78570222854614258;
	setAttr -s 4 ".koy[0:3]"  -0.63258349895477295 -0.11783847212791443 
		0.22665435075759888 -0.61860489845275879;
createNode animCurveTA -n "cp_c009001daipa:Lf_shoulder_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 4 1.8628399622523 7 0 10 1.8628399622523 
		13 0;
createNode animCurveTU -n "cp_c009001daipa:Lf_shoulder_outPutAnimBank_1_Arm_follow";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 1 13 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTL -n "cp_c009001daipa:Rt_shoulder_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTL -n "cp_c009001daipa:Rt_shoulder_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTL -n "cp_c009001daipa:Rt_shoulder_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTA -n "cp_c009001daipa:Rt_shoulder_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTA -n "cp_c009001daipa:Rt_shoulder_outPutAnimBank_1_rotateY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 0 4 5 10 -5 13 0;
	setAttr -s 4 ".kit[1:3]"  10 1 1;
	setAttr -s 4 ".kot[1:3]"  10 1 1;
	setAttr -s 4 ".kix[0:3]"  0.77958911657333374 0.97397536039352417 
		0.98687386512756348 0.6244845986366272;
	setAttr -s 4 ".kiy[0:3]"  0.62629145383834839 -0.22665435075759888 
		0.16149283945560455 0.7810370922088623;
	setAttr -s 4 ".kox[0:3]"  0.77958899736404419 0.97397536039352417 
		0.98687386512756348 0.62448465824127197;
	setAttr -s 4 ".koy[0:3]"  0.62629151344299316 -0.22665435075759888 
		0.16149280965328217 0.7810370922088623;
createNode animCurveTA -n "cp_c009001daipa:Rt_shoulder_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 4 1.8485055404455606 7 0.023961398508284226 
		10 1.8196984057014751 13 0;
	setAttr -s 5 ".kit[1:4]"  10 10 3 3;
	setAttr -s 5 ".kot[1:4]"  10 10 3 3;
createNode animCurveTU -n "cp_c009001daipa:Rt_shoulder_outPutAnimBank_1_Arm_follow";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 1 13 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTA -n "cp_c009001daipa:RtArm_UpArm_FK_outPutAnimBank_1_rotateX";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 -31.646137377657983 4 -35.468052440851658 
		10 -28.065287816939335 13 -31.646137377657983;
	setAttr -s 4 ".kix[0:3]"  0.77920526266098022 0.97461789846420288 
		0.94954514503479004 0.74302530288696289;
	setAttr -s 4 ".kiy[0:3]"  -0.62676888704299927 -0.22387520968914032 
		0.31363052129745483 -0.66926336288452148;
	setAttr -s 4 ".kox[0:3]"  0.77920502424240112 0.97461783885955811 
		0.94954508543014526 0.74302548170089722;
	setAttr -s 4 ".koy[0:3]"  -0.62676912546157837 -0.22387534379959106 
		0.31363049149513245 -0.66926312446594238;
createNode animCurveTA -n "cp_c009001daipa:RtArm_UpArm_FK_outPutAnimBank_1_rotateY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 5.985507743982466 4 18.098034603373826 
		10 -5.4354198603960047 13 5.985507743982466;
	setAttr -s 4 ".kix[0:3]"  0.40008857846260071 0.9353712797164917 
		0.84123861789703369 0.42549920082092285;
	setAttr -s 4 ".kiy[0:3]"  0.91647648811340332 0.35366731882095337 
		-0.54066401720046997 0.90495890378952026;
	setAttr -s 4 ".kox[0:3]"  0.40164998173713684 0.93537133932113647 
		0.84123861789703369 0.42549893260002136;
	setAttr -s 4 ".koy[0:3]"  0.91579329967498779 0.35366731882095337 
		-0.54066401720046997 0.90495896339416504;
createNode animCurveTA -n "cp_c009001daipa:RtArm_UpArm_FK_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -65.159245171386701 4 -58.691786705981819 
		7 -51.581333423920661 10 -57.222519309316041 13 -65.159245171386701;
	setAttr -s 5 ".kit[0:4]"  3 1 10 1 3;
	setAttr -s 5 ".kot[0:4]"  3 1 10 1 3;
	setAttr -s 5 ".kix[1:4]"  0.69187968969345093 0.99478036165237427 
		0.64576601982116699 1;
	setAttr -s 5 ".kiy[1:4]"  0.72201281785964966 0.10203882306814194 
		-0.76353543996810913 0;
	setAttr -s 5 ".kox[1:4]"  0.69188016653060913 0.99478036165237427 
		0.64576560258865356 1;
	setAttr -s 5 ".koy[1:4]"  0.72201246023178101 0.10203882306814194 
		-0.76353573799133301 0;
createNode animCurveTU -n "cp_c009001daipa:RtArm_UpArm_FK_outPutAnimBank_1_twistPlacement";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "cp_c009001daipa:RtArm_UpArm_FK_outPutAnimBank_1_addTwist";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTA -n "cp_c009001daipa:RtArm_Elbow_FK_outPutAnimBank_1_rotateX";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTA -n "cp_c009001daipa:RtArm_Elbow_FK_outPutAnimBank_1_rotateY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -47.536723060478025 3 -33.466921654544279 
		6 -15.484945842943411 12 -49.372595280063031 13 -47.383980848790131;
	setAttr -s 5 ".kix[0:4]"  0.34380638599395752 0.35439109802246094 
		0.68512362241744995 0.76602709293365479 0.4094398021697998;
	setAttr -s 5 ".kiy[0:4]"  0.93904060125350952 0.93509739637374878 
		0.72842687368392944 -0.64280831813812256 0.91233718395233154;
	setAttr -s 5 ".kox[0:4]"  0.39062744379043579 0.35439091920852661 
		0.68512356281280518 0.76602709293365479 0.40943968296051025;
	setAttr -s 5 ".koy[0:4]"  0.92054885625839233 0.93509739637374878 
		0.72842693328857422 -0.64280831813812256 0.91233724355697632;
createNode animCurveTA -n "cp_c009001daipa:RtArm_Elbow_FK_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTA -n "cp_c009001daipa:RtArm_Wrist_FK_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 14.51890899817904 4 5.0504693988903639 
		13 14.51890899817904;
	setAttr -s 3 ".kit[1:2]"  3 1;
	setAttr -s 3 ".kot[1:2]"  3 1;
	setAttr -s 3 ".kix[2]"  0.999961256980896;
	setAttr -s 3 ".kiy[2]"  0.0088017862290143967;
	setAttr -s 3 ".kox[2]"  0.999961256980896;
	setAttr -s 3 ".koy[2]"  0.0088017936795949936;
createNode animCurveTA -n "cp_c009001daipa:RtArm_Wrist_FK_outPutAnimBank_1_rotateY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 -2.9721843450343037 4 2.0278156549656914 
		7 7.0278156549657043 13 -2.9721843450343037;
	setAttr -s 4 ".kit[0:3]"  9 1 1 1;
	setAttr -s 4 ".kot[0:3]"  9 1 1 1;
	setAttr -s 4 ".kix[1:3]"  0.76722383499145508 0.9829515814781189 
		0.97101795673370361;
	setAttr -s 4 ".kiy[1:3]"  0.64137947559356689 0.18386499583721161 
		-0.23900669813156128;
	setAttr -s 4 ".kox[1:3]"  0.76722347736358643 0.98295152187347412 
		0.97101795673370361;
	setAttr -s 4 ".koy[1:3]"  0.64137989282608032 0.1838650107383728 
		-0.23900677263736725;
createNode animCurveTA -n "cp_c009001daipa:RtArm_Wrist_FK_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 20.851178877994386 4 14.335498087068405 
		10 27.366859668920366 13 20.851177712900007;
	setAttr -s 4 ".kit[1:3]"  3 1 1;
	setAttr -s 4 ".kot[1:3]"  3 1 1;
	setAttr -s 4 ".kix[0:3]"  0.59777969121932983 1 0.99907636642456055 
		0.59996879100799561;
	setAttr -s 4 ".kiy[0:3]"  -0.80166041851043701 0 -0.042970295995473862 
		-0.80002343654632568;
	setAttr -s 4 ".kox[0:3]"  0.59777969121932983 1 0.99907636642456055 
		0.59996873140335083;
	setAttr -s 4 ".koy[0:3]"  -0.80166041851043701 0 -0.042970333248376846 
		-0.80002343654632568;
createNode animCurveTL -n "cp_c009001daipa:head_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTL -n "cp_c009001daipa:head_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTL -n "cp_c009001daipa:head_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTA -n "cp_c009001daipa:head_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 -22.351089509800399 3 -21.781918900636349 
		6 -22.550299236747527 9 -21.781918900636349 12 -22.550299236747527 13 -22.351089357136924;
	setAttr -s 6 ".kit[0:5]"  1 3 10 3 10 1;
	setAttr -s 6 ".kot[0:5]"  1 3 10 3 10 1;
	setAttr -s 6 ".kix[0:5]"  0.99026590585708618 1 1 1 1 0.98698645830154419;
	setAttr -s 6 ".kiy[0:5]"  0.13918851315975189 0 0 0 0 0.16080355644226074;
	setAttr -s 6 ".kox[0:5]"  0.99016344547271729 1 1 1 1 0.98698645830154419;
	setAttr -s 6 ".koy[0:5]"  0.13991591334342957 0 0 0 0 0.16080355644226074;
createNode animCurveTA -n "cp_c009001daipa:head_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 -0.035170272995649579 3 2.4537186869431302 
		9 -7.1462818323369932 13 -0.035169319321342152;
	setAttr -s 4 ".kit[0:3]"  1 3 3 1;
	setAttr -s 4 ".kot[0:3]"  1 3 3 1;
	setAttr -s 4 ".kix[0:3]"  0.75802755355834961 1 1 0.75736725330352783;
	setAttr -s 4 ".kiy[0:3]"  0.65222251415252686 0 0 0.65298920869827271;
	setAttr -s 4 ".kox[0:3]"  0.75937545299530029 1 1 0.75736725330352783;
	setAttr -s 4 ".koy[0:3]"  0.65065276622772217 0 0 0.65298914909362793;
createNode animCurveTA -n "cp_c009001daipa:head_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 4.1892859118943679 2 4.9849122289175316 
		8 -5.7560430508951397 13 4.1892871567484828;
	setAttr -s 4 ".kit[0:3]"  1 3 3 1;
	setAttr -s 4 ".kot[0:3]"  1 3 3 1;
	setAttr -s 4 ".kix[0:3]"  0.82229119539260864 1 1 0.84461331367492676;
	setAttr -s 4 ".kiy[0:3]"  0.56906700134277344 0 0 0.5353769063949585;
	setAttr -s 4 ".kox[0:3]"  0.82938104867935181 1 1 0.85648256540298462;
	setAttr -s 4 ".koy[0:3]"  0.55868339538574219 0 0 0.51617586612701416;
createNode animCurveTU -n "cp_c009001daipa:head_ctrl_outPutAnimBank_1_rotation";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "cp_c009001daipa:head_ctrl_outPutAnimBank_1_DYNHatPrimaryCtrl";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "cp_c009001daipa:head_ctrl_outPutAnimBank_1_DYNHatStartFrame";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 20000 13 20000;
createNode animCurveTU -n "cp_c009001daipa:head_ctrl_outPutAnimBank_1_DYNEaringPrimaryCtrl";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "cp_c009001daipa:head_ctrl_outPutAnimBank_1_DYNEaringStartFrame";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 20000 13 20000;
createNode animCurveTU -n "cp_c009001daipa:head_ctrl_outPutAnimBank_1_DYNNecklacePrimaryCtrl";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "cp_c009001daipa:head_ctrl_outPutAnimBank_1_DYNNecklaceStartFrame";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 20000 13 20000;
createNode animCurveTL -n "cp_c009001daipa:waist_FK1_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTL -n "cp_c009001daipa:waist_FK1_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTL -n "cp_c009001daipa:waist_FK1_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTA -n "cp_c009001daipa:waist_FK1_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 3.4893063859434941 2 4.0896733631007338 
		5 1.7739721654942386 8 4.0896733631007338 11 1.7739721654942386 13 3.4893071220851239;
	setAttr -s 6 ".kit[0:5]"  1 3 10 3 10 1;
	setAttr -s 6 ".kot[0:5]"  1 3 10 3 10 1;
	setAttr -s 6 ".kix[0:5]"  0.92557621002197266 1 1 1 1 0.91188681125640869;
	setAttr -s 6 ".kiy[0:5]"  0.3785613477230072 0 0 0 0 0.41044190526008606;
	setAttr -s 6 ".kox[0:5]"  0.93183261156082153 1 1 1 1 0.91188675165176392;
	setAttr -s 6 ".koy[0:5]"  0.36288848519325256 0 0 0 0 0.41044196486473083;
createNode animCurveTA -n "cp_c009001daipa:waist_FK1_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 -3.8518519578156658 3 -8 9 8 13 -3.8518535472727589;
	setAttr -s 4 ".kit[0:3]"  10 3 3 10;
	setAttr -s 4 ".kot[0:3]"  10 3 3 10;
createNode animCurveTA -n "cp_c009001daipa:waist_FK1_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 -4 7 4 13 -4;
createNode animCurveTL -n "cp_c009001daipa:waist_FK2_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTL -n "cp_c009001daipa:waist_FK2_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0.083049101730515898 4 -0.080630906223113349 
		7 0.083049101730515898 10 -0.080630906223113349 13 0.083049101730515898;
createNode animCurveTL -n "cp_c009001daipa:waist_FK2_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTA -n "cp_c009001daipa:waist_FK2_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 2.3743391733240444 3 4.0896733631007338 
		6 1.7739721654942386 9 4.0896733631007338 12 1.7739721654942386 13 2.3743396334125935;
	setAttr -s 6 ".kit[0:5]"  1 3 10 3 10 1;
	setAttr -s 6 ".kot[0:5]"  1 3 10 3 10 1;
	setAttr -s 6 ".kix[0:5]"  0.91620248556137085 1 1 1 1 0.89028549194335938;
	setAttr -s 6 ".kiy[0:5]"  0.40071564912796021 0 0 0 0 0.45540288090705872;
	setAttr -s 6 ".kox[0:5]"  0.92113959789276123 1 1 1 1 0.89028549194335938;
	setAttr -s 6 ".koy[0:5]"  0.38923248648643494 0 0 0 0 0.45540294051170349;
createNode animCurveTA -n "cp_c009001daipa:waist_FK2_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 -3.8518519578156658 3 -8 9 8 13 -3.8518535472727589;
	setAttr -s 4 ".kit[0:3]"  1 3 3 1;
	setAttr -s 4 ".kot[0:3]"  1 3 3 1;
	setAttr -s 4 ".kix[0:3]"  0.54701197147369385 1 1 0.57063096761703491;
	setAttr -s 4 ".kiy[0:3]"  -0.83712470531463623 0 0 -0.82120662927627563;
	setAttr -s 4 ".kox[0:3]"  0.57355445623397827 1 1 0.57063102722167969;
	setAttr -s 4 ".koy[0:3]"  -0.81916743516921997 0 0 -0.82120656967163086;
createNode animCurveTA -n "cp_c009001daipa:waist_FK2_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 -3.4074074074074092 2 -4 8 4 13 -3.4074083345905732;
	setAttr -s 4 ".kit[0:3]"  1 3 3 1;
	setAttr -s 4 ".kot[0:3]"  1 3 3 1;
	setAttr -s 4 ".kix[0:3]"  0.90796411037445068 1 1 0.90403735637664795;
	setAttr -s 4 ".kiy[0:3]"  -0.41904795169830322 0 0 -0.42745357751846313;
	setAttr -s 4 ".kox[0:3]"  0.91031014919281006 1 1 0.90403735637664795;
	setAttr -s 4 ".koy[0:3]"  -0.41392683982849121 0 0 -0.42745351791381836;
createNode animCurveTL -n "cp_c009001daipa:waist_Ctrl_outPutAnimBank_2_translateX";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0.38462733391759213 6 -0.4 7 -0.39825846980397417 
		12 0.4 13 0.38462733391759213;
	setAttr -s 5 ".kix[0:4]"  0.041666671633720398 0.85264283418655396 
		0.68966537714004517 0.76178967952728271 0.041666671633720398;
	setAttr -s 5 ".kiy[0:4]"  -0.086720980703830719 -0.52249425649642944 
		0.72412824630737305 0.64782446622848511 -0.086720980703830719;
	setAttr -s 5 ".kox[0:4]"  0.43307393789291382 0.85264295339584351 
		0.68966537714004517 0.76178967952728271 0.43307393789291382;
	setAttr -s 5 ".koy[0:4]"  -0.90135836601257324 -0.52249401807785034 
		0.72412824630737305 0.64782440662384033 -0.90135836601257324;
createNode animCurveTL -n "cp_c009001daipa:waist_Ctrl_outPutAnimBank_2_translateY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 11 ".ktv[0:10]"  1 -0.8033230891458587 2 -0.73444302121663796 
		4 0.19897493080965684 5 0.19254931498214672 6 -0.28794141487989716 7 -0.8033230891458587 
		8 -0.73444302121663796 10 0.19897493080965684 11 0.19273094214668635 12 -0.30030235670670391 
		13 -0.8033230891458587;
	setAttr -s 11 ".kix[0:10]"  0.65546047687530518 0.13482001423835754 
		0.57466703653335571 0.24188598990440369 0.070173755288124084 0.65761339664459229 
		0.13617889583110809 0.55314421653747559 0.49805524945259094 0.067307420074939728 
		0.65975040197372437;
	setAttr -s 11 ".kiy[0:10]"  -0.75522953271865845 0.99087017774581909 
		0.81838732957839966 -0.97030472755432129 -0.99753481149673462 -0.75335556268692017 
		0.99068427085876465 0.83308553695678711 -0.8671453595161438 -0.99773234128952026 
		-0.75148481130599976;
	setAttr -s 11 ".kox[0:10]"  0.65546047687530518 0.13481996953487396 
		0.57466703653335571 0.24188593029975891 0.070173755288124084 0.65761339664459229 
		0.13617891073226929 0.55314415693283081 0.49805521965026855 0.067307405173778534 
		0.65975040197372437;
	setAttr -s 11 ".koy[0:10]"  -0.75522953271865845 0.99087011814117432 
		0.81838732957839966 -0.97030472755432129 -0.99753481149673462 -0.75335562229156494 
		0.99068427085876465 0.83308553695678711 -0.8671453595161438 -0.99773228168487549 
		-0.75148481130599976;
createNode animCurveTL -n "cp_c009001daipa:waist_Ctrl_outPutAnimBank_2_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 0 7 8.0953576081999667 10 11.992588544451927 
		13 16.761371939379117;
	setAttr -s 4 ".kit[0:3]"  9 10 10 9;
	setAttr -s 4 ".kot[0:3]"  9 10 10 9;
createNode animCurveTA -n "cp_c009001daipa:waist_Ctrl_outPutAnimBank_2_rotateX";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 16.509832958918931 4 14.431316417628221 
		7 16.509832958918931 10 14.431316417628221 13 16.509832958918931;
	setAttr -s 5 ".kit[1:4]"  10 3 10 3;
	setAttr -s 5 ".kot[1:4]"  10 3 10 3;
createNode animCurveTA -n "cp_c009001daipa:waist_Ctrl_outPutAnimBank_2_rotateY";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 4.8148149472695785 3 10 7 -4.8148137551766554 
		9 -10 13 4.814816934090949;
	setAttr -s 5 ".kit[0:4]"  1 3 10 3 1;
	setAttr -s 5 ".kot[0:4]"  1 3 10 3 1;
	setAttr -s 5 ".kix[0:4]"  0.50659406185150146 1 0.58226674795150757 
		1 0.57297205924987793;
	setAttr -s 5 ".kiy[0:4]"  0.86218476295471191 0 -0.81299775838851929 
		0 0.81957495212554932;
	setAttr -s 5 ".kox[0:4]"  0.58355569839477539 1 0.58226674795150757 
		1 0.57297194004058838;
	setAttr -s 5 ".koy[0:4]"  0.81207311153411865 0 -0.81299775838851929 
		0 0.81957501173019409;
createNode animCurveTA -n "cp_c009001daipa:waist_Ctrl_outPutAnimBank_2_rotateZ";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 5 7 -5 13 5;
createNode animCurveTU -n "cp_c009001daipa:waist_Ctrl_outPutAnimBank_2_ikfk_switch";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 2 5 2 7 2 9 2 13 2;
	setAttr -s 5 ".kot[0:4]"  5 5 5 5 5;
createNode animCurveTU -n "cp_c009001daipa:waist_Ctrl_outPutAnimBank_2_second_vis";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 5 0 7 0 9 0 13 0;
	setAttr -s 5 ".kot[0:4]"  5 5 5 5 5;
createNode animCurveTL -n "cp_c009001daipa:root_waist_ikCtrl_outPutAnimBank_2_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTL -n "cp_c009001daipa:root_waist_ikCtrl_outPutAnimBank_2_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTL -n "cp_c009001daipa:root_waist_ikCtrl_outPutAnimBank_2_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTA -n "cp_c009001daipa:root_waist_ikCtrl_outPutAnimBank_2_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTA -n "cp_c009001daipa:root_waist_ikCtrl_outPutAnimBank_2_rotateY";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 0 4 2 10 -2 13 0.06423037296393555;
	setAttr -s 4 ".kit[0:3]"  1 3 3 1;
	setAttr -s 4 ".kot[0:3]"  1 3 3 1;
	setAttr -s 4 ".kix[0:3]"  0.95656079053878784 1 1 0.9552081823348999;
	setAttr -s 4 ".kiy[0:3]"  0.29153302311897278 0 0 0.29593482613563538;
	setAttr -s 4 ".kox[0:3]"  0.95656079053878784 1 1 0.9552081823348999;
	setAttr -s 4 ".koy[0:3]"  0.291532963514328 0 0 0.29593485593795776;
createNode animCurveTA -n "cp_c009001daipa:root_waist_ikCtrl_outPutAnimBank_2_rotateZ";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 3.0000000000000004 7 -3.0000000000000004 
		13 3.0000000000000004;
createNode animCurveTL -n "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_2_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 0.45910039198848906 6 0.45545569501248773 
		7 0.45545569501248773 8 0.45545569501248773 10 0.45545569501248773 13 0.45910039198848906;
	setAttr -s 6 ".kit[0:5]"  3 10 10 10 10 3;
	setAttr -s 6 ".kot[0:5]"  3 10 10 10 10 3;
createNode animCurveTL -n "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_2_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 13 ".ktv[0:12]"  1 2.0964702848911632 2 1.0806296514920453 
		3 0.6428663434319154 4 1.106190712862251 5 1.0989394466396112 6 0.12037026288760333 
		7 0 8 0 9 -0.031258909670084767 10 0.4463800103914255 11 1.8140373532012719 12 2.5612793467033597 
		13 2.0964702848911632;
	setAttr -s 13 ".kit[0:12]"  1 10 1 10 10 1 10 10 
		10 1 10 10 1;
	setAttr -s 13 ".kot[0:12]"  1 10 1 10 10 1 10 10 
		10 1 10 10 1;
	setAttr -s 13 ".kix[0:12]"  0.038139384239912033 0.057234793901443481 
		0.95817941427230835 1 1 0.17913900315761566 1 1 1 0.12319459021091461 0.039372429251670837 
		0.28299397230148315 0.029119981452822685;
	setAttr -s 13 ".kiy[0:12]"  -0.99927246570587158 -0.99836075305938721 
		0.28616812825202942 0 0 -0.98382377624511719 0 0 0 0.99238258600234985 0.99922460317611694 
		0.95912164449691772 -0.9995759129524231;
	setAttr -s 13 ".kox[0:12]"  0.039582237601280212 0.057234793901443481 
		0.95817917585372925 1 1 0.17913895845413208 1 1 1 0.12319457530975342 0.039372429251670837 
		0.28299397230148315 0.029119983315467834;
	setAttr -s 13 ".koy[0:12]"  -0.99921631813049316 -0.99836075305938721 
		0.28616902232170105 0 0 -0.98382377624511719 0 0 0 0.99238252639770508 0.99922460317611694 
		0.95912164449691772 -0.9995759129524231;
createNode animCurveTL -n "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_2_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 13 ".ktv[0:12]"  1 -5.816889968164686 2 -2.8387141270168765 
		3 1.9712145111043302 4 4.9505542371176627 5 7.0036268682164922 6 7.3163765687481206 
		7 7.3163765687481206 8 7.3163765687481206 9 7.3703364105519507 10 6.9126809219840908 
		11 6.8753053497519918 12 9.014804800398343 13 10.944481971214429;
	setAttr -s 13 ".kit[0:12]"  1 10 10 1 10 10 3 10 
		10 3 10 10 1;
	setAttr -s 13 ".kot[0:12]"  1 10 10 1 10 10 3 10 
		10 3 10 10 1;
	setAttr -s 13 ".kix[0:12]"  0.016631057485938072 0.010699465870857239 
		0.010697868652641773 0.017037270590662956 0.035202000290155411 1 1 1 0.20216375589370728 
		1 1 0.020474873483181 0.013523144647479057;
	setAttr -s 13 ".kiy[0:12]"  0.99986165761947632 0.99994277954101563 
		0.99994277954101563 0.9998549222946167 0.99938023090362549 0 0 0 -0.97935175895690918 
		0 0 0.99979037046432495 0.99990856647491455;
	setAttr -s 13 ".kox[0:12]"  0.016248956322669983 0.010699465870857239 
		0.010697868652641773 0.017037270590662956 0.035202000290155411 1 1 1 0.20216375589370728 
		1 1 0.020474873483181 0.013523140922188759;
	setAttr -s 13 ".koy[0:12]"  0.99986797571182251 0.99994277954101563 
		0.99994277954101563 0.99985486268997192 0.99938023090362549 0 0 0 -0.97935175895690918 
		0 0 0.99979037046432495 0.99990856647491455;
createNode animCurveTA -n "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_2_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  1 0 3 0 4 0 6 0 7 0 8 0 10 0 13 0;
	setAttr -s 8 ".kit[0:7]"  3 10 10 10 10 10 10 3;
	setAttr -s 8 ".kot[0:7]"  3 10 10 10 10 10 10 3;
createNode animCurveTA -n "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_2_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 -4.1085025456484328 3 -7.2814440433212981 
		4 -12.538426630754913 6 -7.2814440433212981 7 -7.2814440433212981 8 -7.2814440433212981 
		10 -8.5036012940625252 11 -6.1475156220904781 13 -4.1085025456484328;
	setAttr -s 9 ".kit[0:8]"  3 10 10 10 10 10 10 1 
		3;
	setAttr -s 9 ".kot[0:8]"  3 10 10 10 10 10 10 1 
		3;
	setAttr -s 9 ".kix[7:8]"  0.69050306081771851 1;
	setAttr -s 9 ".kiy[7:8]"  0.72332954406738281 0;
	setAttr -s 9 ".kox[7:8]"  0.69050312042236328 1;
	setAttr -s 9 ".koy[7:8]"  0.72332948446273804 0;
createNode animCurveTA -n "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_2_rotateZ";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 -9.1368053204204909 2 -7.9818965593802469 
		3 -4.2775507787446205 6 0 7 0 8 0 10 -3.6664718602184161 11 -6.3793410450000128 13 
		-9.1368053204204909;
	setAttr -s 9 ".kit[0:8]"  3 1 1 10 10 10 1 1 
		3;
	setAttr -s 9 ".kot[0:8]"  3 1 1 10 10 10 1 1 
		3;
	setAttr -s 9 ".kix[1:8]"  0.71138191223144531 0.62563824653625488 
		1 1 1 0.61713892221450806 0.65805685520172119 1;
	setAttr -s 9 ".kiy[1:8]"  0.70280569791793823 0.7801133394241333 
		0 0 0 -0.78685426712036133 -0.7529681921005249 0;
	setAttr -s 9 ".kox[1:8]"  0.71138197183609009 0.62563818693161011 
		1 1 1 0.61713898181915283 0.65805685520172119 1;
	setAttr -s 9 ".koy[1:8]"  0.70280569791793823 0.7801133394241333 
		0 0 0 -0.78685414791107178 -0.75296831130981445 0;
createNode animCurveTU -n "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_2_raiseBall";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  1 0 3 0 6 0 7 0 8 3.4000000953674316 9 
		0 10 0 13 0;
createNode animCurveTU -n "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_2_raiseToeTip";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  1 111.59999847412109 2 92.116668701171875 
		3 45.701667785644531 4 17.349994659423828 5 -15.108477592468262 6 -1.7999999523162842 
		7 0 8 0 9 18.400001525878906 10 54.600006103515625 12 113.34999847412109 13 111.59999847412109;
	setAttr -s 12 ".kit[0:11]"  1 10 10 1 10 10 10 10 
		10 10 1 1;
	setAttr -s 12 ".kot[0:11]"  1 10 10 1 10 10 10 10 
		10 10 1 1;
	setAttr -s 12 ".kix[0:11]"  0.0054314816370606422 0.0012645731912925839 
		0.0011145778698846698 0.0028716560918837786 0.0043515702709555626 0.0055155833251774311 
		1 1 0.0015262492233887315 0.0013164812698960304 0.008700639009475708 0.0068298066034913063;
	setAttr -s 12 ".kiy[0:11]"  -0.99998527765274048 -0.99999922513961792 
		-0.99999940395355225 -0.99999594688415527 -0.99999058246612549 0.99998486042022705 
		0 0 0.99999886751174927 0.99999910593032837 0.99996215105056763 -0.99997669458389282;
	setAttr -s 12 ".kox[0:11]"  0.0054314807057380676 0.0012645731912925839 
		0.0011145778698846698 0.0028716556262224913 0.0043515702709555626 0.0055155833251774311 
		1 1 0.0015262492233887315 0.0013164812698960304 0.008700639009475708 0.0068298056721687317;
	setAttr -s 12 ".koy[0:11]"  -0.99998527765274048 -0.99999922513961792 
		-0.99999940395355225 -0.9999958872795105 -0.99999058246612549 0.99998486042022705 
		0 0 0.99999886751174927 0.99999910593032837 0.9999622106552124 -0.99997669458389282;
createNode animCurveTU -n "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_2_side";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  1 0 3 0 6 0 7 0 8 0 10 0 13 0;
createNode animCurveTU -n "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_2_swivel";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  1 0 3 0 6 0 7 0 8 0 10 0 13 0;
createNode animCurveTU -n "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_2_roll";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  1 0 3 0 6 0 7 0 8 0 10 0 13 0;
createNode animCurveTU -n "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_2_raiseToe";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  1 -25.299999237060547 3 0 5 20.5 6 9.793655475729814 
		7 0 8 0 10 0 13 -25.299999237060547;
	setAttr -s 8 ".kit[0:7]"  3 10 10 1 10 10 10 3;
	setAttr -s 8 ".kot[0:7]"  3 10 10 1 10 10 10 3;
	setAttr -s 8 ".kix[3:7]"  0.0035323176998645067 1 1 1 1;
	setAttr -s 8 ".kiy[3:7]"  -0.99999374151229858 0 0 0 0;
	setAttr -s 8 ".kox[3:7]"  0.003532318165525794 1 1 1 1;
	setAttr -s 8 ".koy[3:7]"  -0.99999380111694336 0 0 0 0;
createNode animCurveTU -n "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_2_swivelToe";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  1 0 3 0 6 0 7 0 8 0 10 0 13 0;
createNode animCurveTU -n "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_2_twistToe";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  1 0 3 0 6 0 7 0 8 0 10 0 13 0;
createNode animCurveTL -n "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_2_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -0.64825357777019976 3 -0.64825357777019976 
		4 -0.64825357777019976 12 -0.64825357777019976 13 -0.64825357777019976;
createNode animCurveTL -n "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_2_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  1 -1.4571677198205177e-016 3 -1.4571677198205177e-016 
		4 0.61189607404510404 5 1.9591470569443796 6 2.7412092650079107 7 1.7060575786909919 
		8 0.52335942154551962 9 0.63161249160636268 10 1.0421314568109357 11 1.0270479018523921 
		12 -1.4571677198205177e-016 13 -1.4571677198205177e-016;
	setAttr -s 12 ".kit[7:11]"  1 10 1 1 3;
	setAttr -s 12 ".kot[7:11]"  1 10 1 1 3;
	setAttr -s 12 ".kix[7:11]"  0.3626444935798645 1 0.68407732248306274 
		0.27588382363319397 1;
	setAttr -s 12 ".kiy[7:11]"  0.93192762136459351 0 -0.72940957546234131 
		-0.96119099855422974 0;
	setAttr -s 12 ".kox[7:11]"  0.3626444935798645 1 0.68407726287841797 
		0.27588361501693726 1;
	setAttr -s 12 ".koy[7:11]"  0.93192756175994873 0 -0.72940963506698608 
		-0.96119105815887451 0;
createNode animCurveTL -n "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_2_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  1 -1.2 3 -1.2 4 -1.4006171048126714 5 -1.2889092911197986 
		6 0.028191899823270875 7 2.3061607549622964 8 5.3975588305646447 9 9.5777952758995006 
		10 13.245140894674345 11 15.401285978332968 12 15.561371939379114 13 15.561371939379114;
	setAttr -s 12 ".kit[2:11]"  1 1 10 10 10 10 1 1 
		10 10;
	setAttr -s 12 ".kot[2:11]"  1 1 10 10 10 10 1 1 
		10 10;
	setAttr -s 12 ".kix[2:11]"  0.75002944469451904 0.044274482876062393 
		0.023173665627837181 0.015518274158239365 0.011459304019808769 0.010618381202220917 
		0.015192680992186069 0.067967407405376434 1 1;
	setAttr -s 12 ".kiy[2:11]"  -0.66140449047088623 0.99901938438415527 
		0.99973142147064209 0.99987959861755371 0.99993431568145752 0.99994361400604248 0.99988466501235962 
		0.99768757820129395 0 0;
	setAttr -s 12 ".kox[2:11]"  0.75002944469451904 0.044274482876062393 
		0.023173665627837181 0.015518274158239365 0.011459304019808769 0.010618381202220917 
		0.015192685648798943 0.067967399954795837 1 1;
	setAttr -s 12 ".koy[2:11]"  -0.66140449047088623 0.99901944398880005 
		0.99973142147064209 0.99987959861755371 0.99993431568145752 0.99994361400604248 0.99988460540771484 
		0.99768757820129395 0 0;
createNode animCurveTA -n "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_2_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 3 0 4 0 12 0 13 0;
createNode animCurveTA -n "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_2_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  1 7.5861487364620919 3 7.5861487364620919 
		4 6.4326160035022681 6 2.5605759366068148 8 5.1174285731688292 12 7.5861487364620919 
		13 7.5861487364620919;
	setAttr -s 7 ".kit[2:6]"  1 1 1 10 10;
	setAttr -s 7 ".kot[2:6]"  1 1 1 10 10;
	setAttr -s 7 ".kix[2:6]"  0.84169971942901611 0.91898429393768311 
		0.92329508066177368 1 1;
	setAttr -s 7 ".kiy[2:6]"  -0.53994596004486084 -0.39429429173469543 
		0.3840915858745575 0 0;
	setAttr -s 7 ".kox[2:6]"  0.84169965982437134 0.91898429393768311 
		0.92329508066177368 1 1;
	setAttr -s 7 ".koy[2:6]"  -0.53994601964950562 -0.39429429173469543 
		0.38409152626991272 0 0;
createNode animCurveTA -n "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_2_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 0 3 0 4 2.3070654659196532 8 8.1464053987921634 
		12 0 13 0;
	setAttr -s 6 ".kit[2:5]"  1 10 10 10;
	setAttr -s 6 ".kot[2:5]"  1 10 10 10;
	setAttr -s 6 ".kix[2:5]"  0.75554925203323364 0.9927828311920166 
		1 1;
	setAttr -s 6 ".kiy[2:5]"  0.65509188175201416 -0.119925856590271 
		0 0;
	setAttr -s 6 ".kox[2:5]"  0.75554925203323364 0.9927828311920166 
		1 1;
	setAttr -s 6 ".koy[2:5]"  0.65509182214736938 -0.119925856590271 
		0 0;
createNode animCurveTU -n "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_2_raiseBall";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 0 2 13.90000057220459 3 0 4 0 12 0 13 
		0;
	setAttr -s 6 ".kit[0:5]"  3 10 1 10 10 10;
	setAttr -s 6 ".kot[0:5]"  3 10 1 10 10 10;
	setAttr -s 6 ".kix[2:5]"  0.0037791812792420387 1 1 1;
	setAttr -s 6 ".kiy[2:5]"  -0.99999284744262695 0 0 0;
	setAttr -s 6 ".kox[2:5]"  0.0037791822105646133 1 1 1;
	setAttr -s 6 ".koy[2:5]"  -0.99999290704727173 0 0 0;
createNode animCurveTU -n "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_2_raiseToeTip";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  1 0 2 0 3 33.199996948242187 4 61.100002288818359 
		6 116.45370483398437 7 103 8 73.318558540585229 9 38.05952488167938 10 12.946810051143977 
		11 -11.022356986999512 12 0 13 0;
	setAttr -s 12 ".kit[5:11]"  1 10 1 1 10 10 10;
	setAttr -s 12 ".kot[5:11]"  1 10 1 1 10 10 10;
	setAttr -s 12 ".kix[5:11]"  0.0015439761336892843 0.0012832256034016609 
		0.0013952433364465833 0.0021525342017412186 0.0064364587888121605 1 1;
	setAttr -s 12 ".kiy[5:11]"  -0.99999880790710449 -0.99999922513961792 
		-0.99999904632568359 -0.99999767541885376 -0.99997925758361816 0 0;
	setAttr -s 12 ".kox[5:11]"  0.0015439760172739625 0.0012832256034016609 
		0.0013952433364465833 0.0021525337360799313 0.0064364587888121605 1 1;
	setAttr -s 12 ".koy[5:11]"  -0.99999880790710449 -0.99999922513961792 
		-0.99999904632568359 -0.99999767541885376 -0.99997925758361816 0 0;
createNode animCurveTU -n "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_2_side";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 3 0 4 0 12 0 13 0;
createNode animCurveTU -n "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_2_swivel";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 3 0 4 0 12 0 13 0;
createNode animCurveTU -n "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_2_roll";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 3 0 4 0 12 0 13 0;
createNode animCurveTU -n "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_2_raiseToe";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  1 0 3 0 4 0 5 -7.9999995231628418 8 -25.854808807373047 
		11 24.774473190307617 12 0 13 0;
	setAttr -s 8 ".kit[0:7]"  3 10 10 1 10 10 1 3;
	setAttr -s 8 ".kot[0:7]"  3 10 10 1 10 10 1 3;
	setAttr -s 8 ".kix[3:7]"  0.0043848925270140171 0.0076276659965515137 
		0.0064461198635399342 0.0019693728536367416 1;
	setAttr -s 8 ".kiy[3:7]"  -0.99999040365219116 0.99997091293334961 
		0.99997925758361816 -0.99999809265136719 0;
	setAttr -s 8 ".kox[3:7]"  0.0043848920613527298 0.0076276659965515137 
		0.0064461198635399342 0.0019693728536367416 1;
	setAttr -s 8 ".koy[3:7]"  -0.99999040365219116 0.99997091293334961 
		0.99997925758361816 -0.99999809265136719 0;
createNode animCurveTU -n "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_2_swivelToe";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 3 0 4 0 12 0 13 0;
createNode animCurveTU -n "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_2_twistToe";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 3 0 4 0 12 0 13 0;
createNode animCurveTA -n "cp_c009001daipa:LfArm_Wrist_FK_outPutAnimBank_2_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 14.797168765717032 4 22.262865141960368 
		13 14.797168765717032;
	setAttr -s 3 ".kit[1:2]"  3 1;
	setAttr -s 3 ".kot[1:2]"  3 1;
	setAttr -s 3 ".kix[2]"  0.99999397993087769;
	setAttr -s 3 ".kiy[2]"  0.0034730467014014721;
	setAttr -s 3 ".kox[2]"  0.99999397993087769;
	setAttr -s 3 ".koy[2]"  0.003473060904070735;
createNode animCurveTA -n "cp_c009001daipa:LfArm_Wrist_FK_outPutAnimBank_2_rotateY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 3.9716138967504131 4 -1.028386103249588 
		7 -6.0283861032495887 13 3.9716138967504131;
	setAttr -s 4 ".kit[0:3]"  9 1 1 1;
	setAttr -s 4 ".kot[0:3]"  9 1 1 1;
	setAttr -s 4 ".kix[1:3]"  0.75361311435699463 0.99188739061355591 
		0.97196114063262939;
	setAttr -s 4 ".kiy[1:3]"  -0.65731823444366455 -0.12711995840072632 
		0.2351418137550354;
	setAttr -s 4 ".kox[1:3]"  0.75361299514770508 0.99188739061355591 
		0.97196108102798462;
	setAttr -s 4 ".koy[1:3]"  -0.65731847286224365 -0.12711991369724274 
		0.23514185845851898;
createNode animCurveTA -n "cp_c009001daipa:LfArm_Wrist_FK_outPutAnimBank_2_rotateZ";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 24.224637499946031 4 32.076610819193775 
		10 17.460173126713627 13 24.222133153761842;
	setAttr -s 4 ".kix[0:3]"  0.5897795557975769 0.96637123823165894 
		0.99927067756652832 0.59333348274230957;
	setAttr -s 4 ".kiy[0:3]"  0.80756425857543945 0.25715106725692749 
		-0.038185302168130875 0.80495679378509521;
	setAttr -s 4 ".kox[0:3]"  0.59876221418380737 0.96637123823165894 
		0.99927067756652832 0.58385241031646729;
	setAttr -s 4 ".koy[0:3]"  0.80092686414718628 0.25715115666389465 
		-0.038185283541679382 0.81185990571975708;
createNode animCurveTA -n "cp_c009001daipa:LfArm_Elbow_FK_outPutAnimBank_2_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 2 0 13 0;
	setAttr -s 3 ".kit[1:2]"  9 10;
	setAttr -s 3 ".kot[1:2]"  9 10;
createNode animCurveTA -n "cp_c009001daipa:LfArm_Elbow_FK_outPutAnimBank_2_rotateY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -26.024979506583499 3 -34.13370373675432 
		7 -47.74778769826441 12 -25.686427562727307 13 -26.056677894362455;
	setAttr -s 5 ".kit[2:4]"  9 1 1;
	setAttr -s 5 ".kot[2:4]"  9 1 1;
	setAttr -s 5 ".kix[0:4]"  0.69405531883239746 0.40192535519599915 
		0.93065738677978516 0.82519161701202393 0.75087141990661621;
	setAttr -s 5 ".kiy[0:4]"  -0.71992170810699463 -0.91567248106002808 
		0.36589175462722778 0.5648530125617981 -0.66044843196868896;
	setAttr -s 5 ".kox[0:4]"  0.69405519962310791 0.40192538499832153 
		0.93065738677978516 0.82519161701202393 0.75087147951126099;
	setAttr -s 5 ".koy[0:4]"  -0.71992182731628418 -0.9156724214553833 
		0.36589175462722778 0.56485295295715332 -0.66044837236404419;
createNode animCurveTA -n "cp_c009001daipa:LfArm_Elbow_FK_outPutAnimBank_2_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 2 0 13 0;
	setAttr -s 3 ".kit[1:2]"  9 10;
	setAttr -s 3 ".kot[1:2]"  9 10;
createNode animCurveTA -n "cp_c009001daipa:LfArm_UpArm_FK_outPutAnimBank_2_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 -19.988588480493895 4 -16.049855334054886 
		10 -22.753707455441077 13 -19.988588480493895;
	setAttr -s 4 ".kit[0:3]"  1 10 10 1;
	setAttr -s 4 ".kot[0:3]"  1 10 10 1;
	setAttr -s 4 ".kix[0:3]"  0.74927842617034912 0.99182033538818359 
		1 0.81639307737350464;
	setAttr -s 4 ".kiy[0:3]"  0.66225522756576538 -0.12764179706573486 
		0 0.57749664783477783;
	setAttr -s 4 ".kox[0:3]"  0.74927842617034912 0.99182033538818359 
		1 0.81639307737350464;
	setAttr -s 4 ".koy[0:3]"  0.66225516796112061 -0.12764179706573486 
		0 0.57749664783477783;
createNode animCurveTA -n "cp_c009001daipa:LfArm_UpArm_FK_outPutAnimBank_2_rotateY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 10.013115204228884 4 -5.1473506268854585 
		10 19.442361127792367 13 10.013115204228884;
	setAttr -s 4 ".kit[2:3]"  10 1;
	setAttr -s 4 ".kot[2:3]"  10 1;
	setAttr -s 4 ".kix[0:3]"  0.42321768403053284 0.88057076930999756 
		0.81707650423049927 0.45123010873794556;
	setAttr -s 4 ".kiy[0:3]"  -0.90602803230285645 -0.47391468286514282 
		0.57652926445007324 -0.89240765571594238;
	setAttr -s 4 ".kox[0:3]"  0.42957112193107605 0.88057076930999756 
		0.81707650423049927 0.45122948288917542;
	setAttr -s 4 ".koy[0:3]"  -0.90303307771682739 -0.47391471266746521 
		0.57652926445007324 -0.89240801334381104;
createNode animCurveTA -n "cp_c009001daipa:LfArm_UpArm_FK_outPutAnimBank_2_rotateZ";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -53.869185624778481 4 -56.862220751904125 
		7 -71.240229843408173 10 -57.200733755765846 13 -53.869185624778481;
	setAttr -s 5 ".kit[2:4]"  10 1 1;
	setAttr -s 5 ".kot[2:4]"  10 1 1;
	setAttr -s 5 ".kix[0:4]"  0.99951934814453125 0.77740973234176636 
		0.99972087144851685 0.64281618595123291 0.99765431880950928;
	setAttr -s 5 ".kiy[0:4]"  0.031002424657344818 -0.62899458408355713 
		-0.023626072332262993 0.76602041721343994 0.068453334271907806;
	setAttr -s 5 ".kox[0:4]"  0.99951928853988647 0.77740973234176636 
		0.99972087144851685 0.64281630516052246 0.99765431880950928;
	setAttr -s 5 ".koy[0:4]"  0.031002113595604897 -0.62899458408355713 
		-0.023626072332262993 0.76602041721343994 0.068453341722488403;
createNode animCurveTU -n "cp_c009001daipa:LfArm_UpArm_FK_outPutAnimBank_2_twistPlacement";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "cp_c009001daipa:LfArm_UpArm_FK_outPutAnimBank_2_addTwist";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTL -n "cp_c009001daipa:Lf_shoulder_outPutAnimBank_2_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTL -n "cp_c009001daipa:Lf_shoulder_outPutAnimBank_2_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTL -n "cp_c009001daipa:Lf_shoulder_outPutAnimBank_2_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTA -n "cp_c009001daipa:Lf_shoulder_outPutAnimBank_2_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTA -n "cp_c009001daipa:Lf_shoulder_outPutAnimBank_2_rotateY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 0 4 -5 10 5 13 0;
	setAttr -s 4 ".kit[2:3]"  10 1;
	setAttr -s 4 ".kot[2:3]"  10 1;
	setAttr -s 4 ".kix[0:3]"  0.76377081871032715 0.99303281307220459 
		0.97397536039352417 0.78570222854614258;
	setAttr -s 4 ".kiy[0:3]"  -0.64548748731613159 -0.11783847212791443 
		0.22665435075759888 -0.61860501766204834;
	setAttr -s 4 ".kox[0:3]"  0.77449214458465576 0.99303281307220459 
		0.97397536039352417 0.78570222854614258;
	setAttr -s 4 ".koy[0:3]"  -0.63258349895477295 -0.11783847212791443 
		0.22665435075759888 -0.61860489845275879;
createNode animCurveTA -n "cp_c009001daipa:Lf_shoulder_outPutAnimBank_2_rotateZ";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 4 1.8628399622523 7 0 10 1.8628399622523 
		13 0;
createNode animCurveTU -n "cp_c009001daipa:Lf_shoulder_outPutAnimBank_2_Arm_follow";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 1 13 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTL -n "cp_c009001daipa:Rt_shoulder_outPutAnimBank_2_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTL -n "cp_c009001daipa:Rt_shoulder_outPutAnimBank_2_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTL -n "cp_c009001daipa:Rt_shoulder_outPutAnimBank_2_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTA -n "cp_c009001daipa:Rt_shoulder_outPutAnimBank_2_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTA -n "cp_c009001daipa:Rt_shoulder_outPutAnimBank_2_rotateY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 0 4 5 10 -5 13 0;
	setAttr -s 4 ".kit[1:3]"  10 1 1;
	setAttr -s 4 ".kot[1:3]"  10 1 1;
	setAttr -s 4 ".kix[0:3]"  0.77958911657333374 0.97397536039352417 
		0.98687386512756348 0.6244845986366272;
	setAttr -s 4 ".kiy[0:3]"  0.62629145383834839 -0.22665435075759888 
		0.16149283945560455 0.7810370922088623;
	setAttr -s 4 ".kox[0:3]"  0.77958899736404419 0.97397536039352417 
		0.98687386512756348 0.62448465824127197;
	setAttr -s 4 ".koy[0:3]"  0.62629151344299316 -0.22665435075759888 
		0.16149280965328217 0.7810370922088623;
createNode animCurveTA -n "cp_c009001daipa:Rt_shoulder_outPutAnimBank_2_rotateZ";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 4 1.8485055404455606 7 0.023961398508284226 
		10 1.8196984057014751 13 0;
	setAttr -s 5 ".kit[1:4]"  10 10 3 3;
	setAttr -s 5 ".kot[1:4]"  10 10 3 3;
createNode animCurveTU -n "cp_c009001daipa:Rt_shoulder_outPutAnimBank_2_Arm_follow";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 1 13 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTA -n "cp_c009001daipa:RtArm_UpArm_FK_outPutAnimBank_2_rotateX";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 -31.646137377657983 4 -35.468052440851658 
		10 -28.065287816939335 13 -31.646137377657983;
	setAttr -s 4 ".kix[0:3]"  0.77920526266098022 0.97461789846420288 
		0.94954514503479004 0.74302530288696289;
	setAttr -s 4 ".kiy[0:3]"  -0.62676888704299927 -0.22387520968914032 
		0.31363052129745483 -0.66926336288452148;
	setAttr -s 4 ".kox[0:3]"  0.77920502424240112 0.97461783885955811 
		0.94954508543014526 0.74302548170089722;
	setAttr -s 4 ".koy[0:3]"  -0.62676912546157837 -0.22387534379959106 
		0.31363049149513245 -0.66926312446594238;
createNode animCurveTA -n "cp_c009001daipa:RtArm_UpArm_FK_outPutAnimBank_2_rotateY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 5.985507743982466 4 18.098034603373826 
		10 -5.4354198603960047 13 5.985507743982466;
	setAttr -s 4 ".kix[0:3]"  0.40008857846260071 0.9353712797164917 
		0.84123861789703369 0.42549920082092285;
	setAttr -s 4 ".kiy[0:3]"  0.91647648811340332 0.35366731882095337 
		-0.54066401720046997 0.90495890378952026;
	setAttr -s 4 ".kox[0:3]"  0.40164998173713684 0.93537133932113647 
		0.84123861789703369 0.42549893260002136;
	setAttr -s 4 ".koy[0:3]"  0.91579329967498779 0.35366731882095337 
		-0.54066401720046997 0.90495896339416504;
createNode animCurveTA -n "cp_c009001daipa:RtArm_UpArm_FK_outPutAnimBank_2_rotateZ";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -65.159245171386701 4 -58.691786705981819 
		7 -51.581333423920661 10 -57.222519309316041 13 -65.159245171386701;
	setAttr -s 5 ".kit[0:4]"  3 1 10 1 3;
	setAttr -s 5 ".kot[0:4]"  3 1 10 1 3;
	setAttr -s 5 ".kix[1:4]"  0.69187968969345093 0.99478036165237427 
		0.64576601982116699 1;
	setAttr -s 5 ".kiy[1:4]"  0.72201281785964966 0.10203882306814194 
		-0.76353543996810913 0;
	setAttr -s 5 ".kox[1:4]"  0.69188016653060913 0.99478036165237427 
		0.64576560258865356 1;
	setAttr -s 5 ".koy[1:4]"  0.72201246023178101 0.10203882306814194 
		-0.76353573799133301 0;
createNode animCurveTU -n "cp_c009001daipa:RtArm_UpArm_FK_outPutAnimBank_2_twistPlacement";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "cp_c009001daipa:RtArm_UpArm_FK_outPutAnimBank_2_addTwist";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTA -n "cp_c009001daipa:RtArm_Elbow_FK_outPutAnimBank_2_rotateX";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTA -n "cp_c009001daipa:RtArm_Elbow_FK_outPutAnimBank_2_rotateY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -47.536723060478025 3 -33.466921654544279 
		6 -15.484945842943411 12 -49.372595280063031 13 -47.383980848790131;
	setAttr -s 5 ".kix[0:4]"  0.34380638599395752 0.35439109802246094 
		0.68512362241744995 0.76602709293365479 0.4094398021697998;
	setAttr -s 5 ".kiy[0:4]"  0.93904060125350952 0.93509739637374878 
		0.72842687368392944 -0.64280831813812256 0.91233718395233154;
	setAttr -s 5 ".kox[0:4]"  0.39062744379043579 0.35439091920852661 
		0.68512356281280518 0.76602709293365479 0.40943968296051025;
	setAttr -s 5 ".koy[0:4]"  0.92054885625839233 0.93509739637374878 
		0.72842693328857422 -0.64280831813812256 0.91233724355697632;
createNode animCurveTA -n "cp_c009001daipa:RtArm_Elbow_FK_outPutAnimBank_2_rotateZ";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTA -n "cp_c009001daipa:RtArm_Wrist_FK_outPutAnimBank_2_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 14.51890899817904 4 5.0504693988903639 
		13 14.51890899817904;
	setAttr -s 3 ".kit[1:2]"  3 1;
	setAttr -s 3 ".kot[1:2]"  3 1;
	setAttr -s 3 ".kix[2]"  0.999961256980896;
	setAttr -s 3 ".kiy[2]"  0.0088017862290143967;
	setAttr -s 3 ".kox[2]"  0.999961256980896;
	setAttr -s 3 ".koy[2]"  0.0088017936795949936;
createNode animCurveTA -n "cp_c009001daipa:RtArm_Wrist_FK_outPutAnimBank_2_rotateY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 -2.9721843450343037 4 2.0278156549656914 
		7 7.0278156549657043 13 -2.9721843450343037;
	setAttr -s 4 ".kit[0:3]"  9 1 1 1;
	setAttr -s 4 ".kot[0:3]"  9 1 1 1;
	setAttr -s 4 ".kix[1:3]"  0.76722383499145508 0.9829515814781189 
		0.97101795673370361;
	setAttr -s 4 ".kiy[1:3]"  0.64137947559356689 0.18386499583721161 
		-0.23900669813156128;
	setAttr -s 4 ".kox[1:3]"  0.76722347736358643 0.98295152187347412 
		0.97101795673370361;
	setAttr -s 4 ".koy[1:3]"  0.64137989282608032 0.1838650107383728 
		-0.23900677263736725;
createNode animCurveTA -n "cp_c009001daipa:RtArm_Wrist_FK_outPutAnimBank_2_rotateZ";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 20.851178877994386 4 14.335498087068405 
		10 27.366859668920366 13 20.851177712900007;
	setAttr -s 4 ".kit[1:3]"  3 1 1;
	setAttr -s 4 ".kot[1:3]"  3 1 1;
	setAttr -s 4 ".kix[0:3]"  0.59777969121932983 1 0.99907636642456055 
		0.59996879100799561;
	setAttr -s 4 ".kiy[0:3]"  -0.80166041851043701 0 -0.042970295995473862 
		-0.80002343654632568;
	setAttr -s 4 ".kox[0:3]"  0.59777969121932983 1 0.99907636642456055 
		0.59996873140335083;
	setAttr -s 4 ".koy[0:3]"  -0.80166041851043701 0 -0.042970333248376846 
		-0.80002343654632568;
createNode animCurveTL -n "cp_c009001daipa:head_ctrl_outPutAnimBank_2_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTL -n "cp_c009001daipa:head_ctrl_outPutAnimBank_2_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTL -n "cp_c009001daipa:head_ctrl_outPutAnimBank_2_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTA -n "cp_c009001daipa:head_ctrl_outPutAnimBank_2_rotateX";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 -22.351089509800399 3 -21.781918900636349 
		6 -22.550299236747527 9 -21.781918900636349 12 -22.550299236747527 13 -22.351089357136924;
	setAttr -s 6 ".kit[0:5]"  1 3 10 3 10 1;
	setAttr -s 6 ".kot[0:5]"  1 3 10 3 10 1;
	setAttr -s 6 ".kix[0:5]"  0.99026590585708618 1 1 1 1 0.98698645830154419;
	setAttr -s 6 ".kiy[0:5]"  0.13918851315975189 0 0 0 0 0.16080355644226074;
	setAttr -s 6 ".kox[0:5]"  0.99016344547271729 1 1 1 1 0.98698645830154419;
	setAttr -s 6 ".koy[0:5]"  0.13991591334342957 0 0 0 0 0.16080355644226074;
createNode animCurveTA -n "cp_c009001daipa:head_ctrl_outPutAnimBank_2_rotateY";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 -0.035170272995649579 3 2.4537186869431302 
		9 -7.1462818323369932 13 -0.035169319321342152;
	setAttr -s 4 ".kit[0:3]"  1 3 3 1;
	setAttr -s 4 ".kot[0:3]"  1 3 3 1;
	setAttr -s 4 ".kix[0:3]"  0.75802755355834961 1 1 0.75736725330352783;
	setAttr -s 4 ".kiy[0:3]"  0.65222251415252686 0 0 0.65298920869827271;
	setAttr -s 4 ".kox[0:3]"  0.75937545299530029 1 1 0.75736725330352783;
	setAttr -s 4 ".koy[0:3]"  0.65065276622772217 0 0 0.65298914909362793;
createNode animCurveTA -n "cp_c009001daipa:head_ctrl_outPutAnimBank_2_rotateZ";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 4.1892859118943679 2 4.9849122289175316 
		8 -5.7560430508951397 13 4.1892871567484828;
	setAttr -s 4 ".kit[0:3]"  1 3 3 1;
	setAttr -s 4 ".kot[0:3]"  1 3 3 1;
	setAttr -s 4 ".kix[0:3]"  0.82229119539260864 1 1 0.84461331367492676;
	setAttr -s 4 ".kiy[0:3]"  0.56906700134277344 0 0 0.5353769063949585;
	setAttr -s 4 ".kox[0:3]"  0.82938104867935181 1 1 0.85648256540298462;
	setAttr -s 4 ".koy[0:3]"  0.55868339538574219 0 0 0.51617586612701416;
createNode animCurveTU -n "cp_c009001daipa:head_ctrl_outPutAnimBank_2_rotation";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "cp_c009001daipa:head_ctrl_outPutAnimBank_2_DYNHatPrimaryCtrl";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "cp_c009001daipa:head_ctrl_outPutAnimBank_2_DYNHatStartFrame";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 20000 13 20000;
createNode animCurveTU -n "cp_c009001daipa:head_ctrl_outPutAnimBank_2_DYNEaringPrimaryCtrl";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "cp_c009001daipa:head_ctrl_outPutAnimBank_2_DYNEaringStartFrame";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 20000 13 20000;
createNode animCurveTU -n "cp_c009001daipa:head_ctrl_outPutAnimBank_2_DYNNecklacePrimaryCtrl";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "cp_c009001daipa:head_ctrl_outPutAnimBank_2_DYNNecklaceStartFrame";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 20000 13 20000;
createNode animCurveTL -n "cp_c009001daipa:waist_FK1_ctrl_outPutAnimBank_2_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTL -n "cp_c009001daipa:waist_FK1_ctrl_outPutAnimBank_2_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTL -n "cp_c009001daipa:waist_FK1_ctrl_outPutAnimBank_2_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTA -n "cp_c009001daipa:waist_FK1_ctrl_outPutAnimBank_2_rotateX";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 3.4893063859434941 2 4.0896733631007338 
		5 1.7739721654942386 8 4.0896733631007338 11 1.7739721654942386 13 3.4893071220851239;
	setAttr -s 6 ".kit[0:5]"  1 3 10 3 10 1;
	setAttr -s 6 ".kot[0:5]"  1 3 10 3 10 1;
	setAttr -s 6 ".kix[0:5]"  0.92557621002197266 1 1 1 1 0.91188681125640869;
	setAttr -s 6 ".kiy[0:5]"  0.3785613477230072 0 0 0 0 0.41044190526008606;
	setAttr -s 6 ".kox[0:5]"  0.93183261156082153 1 1 1 1 0.91188675165176392;
	setAttr -s 6 ".koy[0:5]"  0.36288848519325256 0 0 0 0 0.41044196486473083;
createNode animCurveTA -n "cp_c009001daipa:waist_FK1_ctrl_outPutAnimBank_2_rotateY";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 -3.8518519578156658 3 -8 9 8 13 -3.8518535472727589;
	setAttr -s 4 ".kit[0:3]"  10 3 3 10;
	setAttr -s 4 ".kot[0:3]"  10 3 3 10;
createNode animCurveTA -n "cp_c009001daipa:waist_FK1_ctrl_outPutAnimBank_2_rotateZ";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 -4 7 4 13 -4;
createNode animCurveTL -n "cp_c009001daipa:waist_FK2_ctrl_outPutAnimBank_2_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTL -n "cp_c009001daipa:waist_FK2_ctrl_outPutAnimBank_2_translateY";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0.083049101730515898 4 -0.080630906223113349 
		7 0.083049101730515898 10 -0.080630906223113349 13 0.083049101730515898;
createNode animCurveTL -n "cp_c009001daipa:waist_FK2_ctrl_outPutAnimBank_2_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTA -n "cp_c009001daipa:waist_FK2_ctrl_outPutAnimBank_2_rotateX";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 2.3743391733240444 3 4.0896733631007338 
		6 1.7739721654942386 9 4.0896733631007338 12 1.7739721654942386 13 2.3743396334125935;
	setAttr -s 6 ".kit[0:5]"  1 3 10 3 10 1;
	setAttr -s 6 ".kot[0:5]"  1 3 10 3 10 1;
	setAttr -s 6 ".kix[0:5]"  0.91620248556137085 1 1 1 1 0.89028549194335938;
	setAttr -s 6 ".kiy[0:5]"  0.40071564912796021 0 0 0 0 0.45540288090705872;
	setAttr -s 6 ".kox[0:5]"  0.92113959789276123 1 1 1 1 0.89028549194335938;
	setAttr -s 6 ".koy[0:5]"  0.38923248648643494 0 0 0 0 0.45540294051170349;
createNode animCurveTA -n "cp_c009001daipa:waist_FK2_ctrl_outPutAnimBank_2_rotateY";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 -3.8518519578156658 3 -8 9 8 13 -3.8518535472727589;
	setAttr -s 4 ".kit[0:3]"  1 3 3 1;
	setAttr -s 4 ".kot[0:3]"  1 3 3 1;
	setAttr -s 4 ".kix[0:3]"  0.54701197147369385 1 1 0.57063096761703491;
	setAttr -s 4 ".kiy[0:3]"  -0.83712470531463623 0 0 -0.82120662927627563;
	setAttr -s 4 ".kox[0:3]"  0.57355445623397827 1 1 0.57063102722167969;
	setAttr -s 4 ".koy[0:3]"  -0.81916743516921997 0 0 -0.82120656967163086;
createNode animCurveTA -n "cp_c009001daipa:waist_FK2_ctrl_outPutAnimBank_2_rotateZ";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 -3.4074074074074092 2 -4 8 4 13 -3.4074083345905732;
	setAttr -s 4 ".kit[0:3]"  1 3 3 1;
	setAttr -s 4 ".kot[0:3]"  1 3 3 1;
	setAttr -s 4 ".kix[0:3]"  0.90796411037445068 1 1 0.90403735637664795;
	setAttr -s 4 ".kiy[0:3]"  -0.41904795169830322 0 0 -0.42745357751846313;
	setAttr -s 4 ".kox[0:3]"  0.91031014919281006 1 1 0.90403735637664795;
	setAttr -s 4 ".koy[0:3]"  -0.41392683982849121 0 0 -0.42745351791381836;
select -ne :time1;
	setAttr ".o" 1;
	setAttr ".unw" 1;
select -ne :renderPartition;
	setAttr -s 50 ".st";
select -ne :initialShadingGroup;
	setAttr -s 23 ".dsm";
	setAttr ".ro" yes;
	setAttr -s 141 ".gn";
select -ne :initialParticleSE;
	setAttr ".ro" yes;
select -ne :defaultShaderList1;
	setAttr -s 50 ".s";
select -ne :defaultTextureList1;
	setAttr -s 49 ".tx";
select -ne :postProcessList1;
	setAttr -s 2 ".p";
select -ne :defaultRenderUtilityList1;
	setAttr -s 53 ".u";
select -ne :renderGlobalsList1;
select -ne :defaultRenderGlobals;
	setAttr ".pram" -type "string" "";
select -ne :defaultResolution;
	setAttr ".w" 1280;
	setAttr ".h" 720;
	setAttr ".pa" 1;
	setAttr ".dar" 1.7777777910232544;
	setAttr ".ldar" yes;
select -ne :hardwareRenderGlobals;
	setAttr ".ctrs" 256;
	setAttr ".btrs" 512;
select -ne :defaultHardwareRenderGlobals;
	setAttr ".fn" -type "string" "im";
	setAttr ".res" -type "string" "ntsc_4d 646 485 1.333";
select -ne :ikSystem;
	setAttr -s 3 ".sol";
connectAttr "cp_c009001daipa:waist_Ctrl_outPutAnimBank_1_translateX.o" "cp_c009001daipa:waist_Ctrl_outPutAnimBank_1.tx"
		;
connectAttr "cp_c009001daipa:waist_Ctrl_outPutAnimBank_1_translateY.o" "cp_c009001daipa:waist_Ctrl_outPutAnimBank_1.ty"
		;
connectAttr "cp_c009001daipa:waist_Ctrl_outPutAnimBank_1_translateZ.o" "cp_c009001daipa:waist_Ctrl_outPutAnimBank_1.tz"
		;
connectAttr "cp_c009001daipa:waist_Ctrl_outPutAnimBank_1_rotateX.o" "cp_c009001daipa:waist_Ctrl_outPutAnimBank_1.rx"
		;
connectAttr "cp_c009001daipa:waist_Ctrl_outPutAnimBank_1_rotateY.o" "cp_c009001daipa:waist_Ctrl_outPutAnimBank_1.ry"
		;
connectAttr "cp_c009001daipa:waist_Ctrl_outPutAnimBank_1_rotateZ.o" "cp_c009001daipa:waist_Ctrl_outPutAnimBank_1.rz"
		;
connectAttr "cp_c009001daipa:waist_Ctrl_outPutAnimBank_1_ikfk_switch.o" "cp_c009001daipa:waist_Ctrl_outPutAnimBank_1.ikfk_switch"
		;
connectAttr "cp_c009001daipa:waist_Ctrl_outPutAnimBank_1_second_vis.o" "cp_c009001daipa:waist_Ctrl_outPutAnimBank_1.second_vis"
		;
connectAttr "cp_c009001daipa:root_waist_ikCtrl_outPutAnimBank_1_translateX.o" "cp_c009001daipa:root_waist_ikCtrl_outPutAnimBank_1.tx"
		;
connectAttr "cp_c009001daipa:root_waist_ikCtrl_outPutAnimBank_1_translateY.o" "cp_c009001daipa:root_waist_ikCtrl_outPutAnimBank_1.ty"
		;
connectAttr "cp_c009001daipa:root_waist_ikCtrl_outPutAnimBank_1_translateZ.o" "cp_c009001daipa:root_waist_ikCtrl_outPutAnimBank_1.tz"
		;
connectAttr "cp_c009001daipa:root_waist_ikCtrl_outPutAnimBank_1_rotateX.o" "cp_c009001daipa:root_waist_ikCtrl_outPutAnimBank_1.rx"
		;
connectAttr "cp_c009001daipa:root_waist_ikCtrl_outPutAnimBank_1_rotateY.o" "cp_c009001daipa:root_waist_ikCtrl_outPutAnimBank_1.ry"
		;
connectAttr "cp_c009001daipa:root_waist_ikCtrl_outPutAnimBank_1_rotateZ.o" "cp_c009001daipa:root_waist_ikCtrl_outPutAnimBank_1.rz"
		;
connectAttr "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1_translateX.o" "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1.tx"
		;
connectAttr "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1_translateY.o" "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1.ty"
		;
connectAttr "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1_translateZ.o" "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1.tz"
		;
connectAttr "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1_rotateX.o" "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1.rx"
		;
connectAttr "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1_rotateY.o" "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1.ry"
		;
connectAttr "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1_rotateZ.o" "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1.rz"
		;
connectAttr "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1_raiseBall.o" "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1.raiseBall"
		;
connectAttr "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1_raiseToeTip.o" "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1.raiseToeTip"
		;
connectAttr "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1_side.o" "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1.side"
		;
connectAttr "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1_swivel.o" "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1.swivel"
		;
connectAttr "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1_roll.o" "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1.roll"
		;
connectAttr "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1_raiseToe.o" "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1.raiseToe"
		;
connectAttr "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1_swivelToe.o" "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1.swivelToe"
		;
connectAttr "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1_twistToe.o" "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1.twistToe"
		;
connectAttr "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1_translateX.o" "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1.tx"
		;
connectAttr "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1_translateY.o" "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1.ty"
		;
connectAttr "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1_translateZ.o" "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1.tz"
		;
connectAttr "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1_rotateX.o" "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1.rx"
		;
connectAttr "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1_rotateY.o" "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1.ry"
		;
connectAttr "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1_rotateZ.o" "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1.rz"
		;
connectAttr "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1_raiseBall.o" "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1.raiseBall"
		;
connectAttr "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1_raiseToeTip.o" "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1.raiseToeTip"
		;
connectAttr "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1_side.o" "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1.side"
		;
connectAttr "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1_swivel.o" "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1.swivel"
		;
connectAttr "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1_roll.o" "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1.roll"
		;
connectAttr "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1_raiseToe.o" "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1.raiseToe"
		;
connectAttr "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1_swivelToe.o" "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1.swivelToe"
		;
connectAttr "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1_twistToe.o" "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1.twistToe"
		;
connectAttr "cp_c009001daipa:LfArm_Wrist_FK_outPutAnimBank_1_rotateX.o" "cp_c009001daipa:LfArm_Wrist_FK_outPutAnimBank_1.rx"
		;
connectAttr "cp_c009001daipa:LfArm_Wrist_FK_outPutAnimBank_1_rotateY.o" "cp_c009001daipa:LfArm_Wrist_FK_outPutAnimBank_1.ry"
		;
connectAttr "cp_c009001daipa:LfArm_Wrist_FK_outPutAnimBank_1_rotateZ.o" "cp_c009001daipa:LfArm_Wrist_FK_outPutAnimBank_1.rz"
		;
connectAttr "cp_c009001daipa:LfArm_Elbow_FK_outPutAnimBank_1_rotateX.o" "cp_c009001daipa:LfArm_Elbow_FK_outPutAnimBank_1.rx"
		;
connectAttr "cp_c009001daipa:LfArm_Elbow_FK_outPutAnimBank_1_rotateY.o" "cp_c009001daipa:LfArm_Elbow_FK_outPutAnimBank_1.ry"
		;
connectAttr "cp_c009001daipa:LfArm_Elbow_FK_outPutAnimBank_1_rotateZ.o" "cp_c009001daipa:LfArm_Elbow_FK_outPutAnimBank_1.rz"
		;
connectAttr "cp_c009001daipa:LfArm_UpArm_FK_outPutAnimBank_1_rotateX.o" "cp_c009001daipa:LfArm_UpArm_FK_outPutAnimBank_1.rx"
		;
connectAttr "cp_c009001daipa:LfArm_UpArm_FK_outPutAnimBank_1_rotateY.o" "cp_c009001daipa:LfArm_UpArm_FK_outPutAnimBank_1.ry"
		;
connectAttr "cp_c009001daipa:LfArm_UpArm_FK_outPutAnimBank_1_rotateZ.o" "cp_c009001daipa:LfArm_UpArm_FK_outPutAnimBank_1.rz"
		;
connectAttr "cp_c009001daipa:LfArm_UpArm_FK_outPutAnimBank_1_twistPlacement.o" "cp_c009001daipa:LfArm_UpArm_FK_outPutAnimBank_1.twistPlacement"
		;
connectAttr "cp_c009001daipa:LfArm_UpArm_FK_outPutAnimBank_1_addTwist.o" "cp_c009001daipa:LfArm_UpArm_FK_outPutAnimBank_1.addTwist"
		;
connectAttr "cp_c009001daipa:Lf_shoulder_outPutAnimBank_1_translateX.o" "cp_c009001daipa:Lf_shoulder_outPutAnimBank_1.tx"
		;
connectAttr "cp_c009001daipa:Lf_shoulder_outPutAnimBank_1_translateY.o" "cp_c009001daipa:Lf_shoulder_outPutAnimBank_1.ty"
		;
connectAttr "cp_c009001daipa:Lf_shoulder_outPutAnimBank_1_translateZ.o" "cp_c009001daipa:Lf_shoulder_outPutAnimBank_1.tz"
		;
connectAttr "cp_c009001daipa:Lf_shoulder_outPutAnimBank_1_rotateX.o" "cp_c009001daipa:Lf_shoulder_outPutAnimBank_1.rx"
		;
connectAttr "cp_c009001daipa:Lf_shoulder_outPutAnimBank_1_rotateY.o" "cp_c009001daipa:Lf_shoulder_outPutAnimBank_1.ry"
		;
connectAttr "cp_c009001daipa:Lf_shoulder_outPutAnimBank_1_rotateZ.o" "cp_c009001daipa:Lf_shoulder_outPutAnimBank_1.rz"
		;
connectAttr "cp_c009001daipa:Lf_shoulder_outPutAnimBank_1_Arm_follow.o" "cp_c009001daipa:Lf_shoulder_outPutAnimBank_1.Arm_follow"
		;
connectAttr "cp_c009001daipa:Rt_shoulder_outPutAnimBank_1_translateX.o" "cp_c009001daipa:Rt_shoulder_outPutAnimBank_1.tx"
		;
connectAttr "cp_c009001daipa:Rt_shoulder_outPutAnimBank_1_translateY.o" "cp_c009001daipa:Rt_shoulder_outPutAnimBank_1.ty"
		;
connectAttr "cp_c009001daipa:Rt_shoulder_outPutAnimBank_1_translateZ.o" "cp_c009001daipa:Rt_shoulder_outPutAnimBank_1.tz"
		;
connectAttr "cp_c009001daipa:Rt_shoulder_outPutAnimBank_1_rotateX.o" "cp_c009001daipa:Rt_shoulder_outPutAnimBank_1.rx"
		;
connectAttr "cp_c009001daipa:Rt_shoulder_outPutAnimBank_1_rotateY.o" "cp_c009001daipa:Rt_shoulder_outPutAnimBank_1.ry"
		;
connectAttr "cp_c009001daipa:Rt_shoulder_outPutAnimBank_1_rotateZ.o" "cp_c009001daipa:Rt_shoulder_outPutAnimBank_1.rz"
		;
connectAttr "cp_c009001daipa:Rt_shoulder_outPutAnimBank_1_Arm_follow.o" "cp_c009001daipa:Rt_shoulder_outPutAnimBank_1.Arm_follow"
		;
connectAttr "cp_c009001daipa:RtArm_UpArm_FK_outPutAnimBank_1_rotateX.o" "cp_c009001daipa:RtArm_UpArm_FK_outPutAnimBank_1.rx"
		;
connectAttr "cp_c009001daipa:RtArm_UpArm_FK_outPutAnimBank_1_rotateY.o" "cp_c009001daipa:RtArm_UpArm_FK_outPutAnimBank_1.ry"
		;
connectAttr "cp_c009001daipa:RtArm_UpArm_FK_outPutAnimBank_1_rotateZ.o" "cp_c009001daipa:RtArm_UpArm_FK_outPutAnimBank_1.rz"
		;
connectAttr "cp_c009001daipa:RtArm_UpArm_FK_outPutAnimBank_1_twistPlacement.o" "cp_c009001daipa:RtArm_UpArm_FK_outPutAnimBank_1.twistPlacement"
		;
connectAttr "cp_c009001daipa:RtArm_UpArm_FK_outPutAnimBank_1_addTwist.o" "cp_c009001daipa:RtArm_UpArm_FK_outPutAnimBank_1.addTwist"
		;
connectAttr "cp_c009001daipa:RtArm_Elbow_FK_outPutAnimBank_1_rotateX.o" "cp_c009001daipa:RtArm_Elbow_FK_outPutAnimBank_1.rx"
		;
connectAttr "cp_c009001daipa:RtArm_Elbow_FK_outPutAnimBank_1_rotateY.o" "cp_c009001daipa:RtArm_Elbow_FK_outPutAnimBank_1.ry"
		;
connectAttr "cp_c009001daipa:RtArm_Elbow_FK_outPutAnimBank_1_rotateZ.o" "cp_c009001daipa:RtArm_Elbow_FK_outPutAnimBank_1.rz"
		;
connectAttr "cp_c009001daipa:RtArm_Wrist_FK_outPutAnimBank_1_rotateX.o" "cp_c009001daipa:RtArm_Wrist_FK_outPutAnimBank_1.rx"
		;
connectAttr "cp_c009001daipa:RtArm_Wrist_FK_outPutAnimBank_1_rotateY.o" "cp_c009001daipa:RtArm_Wrist_FK_outPutAnimBank_1.ry"
		;
connectAttr "cp_c009001daipa:RtArm_Wrist_FK_outPutAnimBank_1_rotateZ.o" "cp_c009001daipa:RtArm_Wrist_FK_outPutAnimBank_1.rz"
		;
connectAttr "cp_c009001daipa:head_ctrl_outPutAnimBank_1_translateX.o" "cp_c009001daipa:head_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "cp_c009001daipa:head_ctrl_outPutAnimBank_1_translateY.o" "cp_c009001daipa:head_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "cp_c009001daipa:head_ctrl_outPutAnimBank_1_translateZ.o" "cp_c009001daipa:head_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "cp_c009001daipa:head_ctrl_outPutAnimBank_1_rotateX.o" "cp_c009001daipa:head_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "cp_c009001daipa:head_ctrl_outPutAnimBank_1_rotateY.o" "cp_c009001daipa:head_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "cp_c009001daipa:head_ctrl_outPutAnimBank_1_rotateZ.o" "cp_c009001daipa:head_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "cp_c009001daipa:head_ctrl_outPutAnimBank_1_rotation.o" "cp_c009001daipa:head_ctrl_outPutAnimBank_1.rotation"
		;
connectAttr "cp_c009001daipa:head_ctrl_outPutAnimBank_1_DYNHatPrimaryCtrl.o" "cp_c009001daipa:head_ctrl_outPutAnimBank_1.DYNHatPrimaryCtrl"
		;
connectAttr "cp_c009001daipa:head_ctrl_outPutAnimBank_1_DYNHatStartFrame.o" "cp_c009001daipa:head_ctrl_outPutAnimBank_1.DYNHatStartFrame"
		;
connectAttr "cp_c009001daipa:head_ctrl_outPutAnimBank_1_DYNEaringPrimaryCtrl.o" "cp_c009001daipa:head_ctrl_outPutAnimBank_1.DYNEaringPrimaryCtrl"
		;
connectAttr "cp_c009001daipa:head_ctrl_outPutAnimBank_1_DYNEaringStartFrame.o" "cp_c009001daipa:head_ctrl_outPutAnimBank_1.DYNEaringStartFrame"
		;
connectAttr "cp_c009001daipa:head_ctrl_outPutAnimBank_1_DYNNecklacePrimaryCtrl.o" "cp_c009001daipa:head_ctrl_outPutAnimBank_1.DYNNecklacePrimaryCtrl"
		;
connectAttr "cp_c009001daipa:head_ctrl_outPutAnimBank_1_DYNNecklaceStartFrame.o" "cp_c009001daipa:head_ctrl_outPutAnimBank_1.DYNNecklaceStartFrame"
		;
connectAttr "cp_c009001daipa:waist_FK1_ctrl_outPutAnimBank_1_translateX.o" "cp_c009001daipa:waist_FK1_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "cp_c009001daipa:waist_FK1_ctrl_outPutAnimBank_1_translateY.o" "cp_c009001daipa:waist_FK1_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "cp_c009001daipa:waist_FK1_ctrl_outPutAnimBank_1_translateZ.o" "cp_c009001daipa:waist_FK1_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "cp_c009001daipa:waist_FK1_ctrl_outPutAnimBank_1_rotateX.o" "cp_c009001daipa:waist_FK1_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "cp_c009001daipa:waist_FK1_ctrl_outPutAnimBank_1_rotateY.o" "cp_c009001daipa:waist_FK1_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "cp_c009001daipa:waist_FK1_ctrl_outPutAnimBank_1_rotateZ.o" "cp_c009001daipa:waist_FK1_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "cp_c009001daipa:waist_FK2_ctrl_outPutAnimBank_1_translateX.o" "cp_c009001daipa:waist_FK2_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "cp_c009001daipa:waist_FK2_ctrl_outPutAnimBank_1_translateY.o" "cp_c009001daipa:waist_FK2_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "cp_c009001daipa:waist_FK2_ctrl_outPutAnimBank_1_translateZ.o" "cp_c009001daipa:waist_FK2_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "cp_c009001daipa:waist_FK2_ctrl_outPutAnimBank_1_rotateX.o" "cp_c009001daipa:waist_FK2_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "cp_c009001daipa:waist_FK2_ctrl_outPutAnimBank_1_rotateY.o" "cp_c009001daipa:waist_FK2_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "cp_c009001daipa:waist_FK2_ctrl_outPutAnimBank_1_rotateZ.o" "cp_c009001daipa:waist_FK2_ctrl_outPutAnimBank_1.rz"
		;
connectAttr "cp_c009001daipa:waist_Ctrl_outPutAnimBank_2_translateX.o" "cp_c009001daipa:waist_Ctrl_outPutAnimBank_2.tx"
		;
connectAttr "cp_c009001daipa:waist_Ctrl_outPutAnimBank_2_translateY.o" "cp_c009001daipa:waist_Ctrl_outPutAnimBank_2.ty"
		;
connectAttr "cp_c009001daipa:waist_Ctrl_outPutAnimBank_2_translateZ.o" "cp_c009001daipa:waist_Ctrl_outPutAnimBank_2.tz"
		;
connectAttr "cp_c009001daipa:waist_Ctrl_outPutAnimBank_2_rotateX.o" "cp_c009001daipa:waist_Ctrl_outPutAnimBank_2.rx"
		;
connectAttr "cp_c009001daipa:waist_Ctrl_outPutAnimBank_2_rotateY.o" "cp_c009001daipa:waist_Ctrl_outPutAnimBank_2.ry"
		;
connectAttr "cp_c009001daipa:waist_Ctrl_outPutAnimBank_2_rotateZ.o" "cp_c009001daipa:waist_Ctrl_outPutAnimBank_2.rz"
		;
connectAttr "cp_c009001daipa:waist_Ctrl_outPutAnimBank_2_ikfk_switch.o" "cp_c009001daipa:waist_Ctrl_outPutAnimBank_2.ikfk_switch"
		;
connectAttr "cp_c009001daipa:waist_Ctrl_outPutAnimBank_2_second_vis.o" "cp_c009001daipa:waist_Ctrl_outPutAnimBank_2.second_vis"
		;
connectAttr "cp_c009001daipa:root_waist_ikCtrl_outPutAnimBank_2_translateX.o" "cp_c009001daipa:root_waist_ikCtrl_outPutAnimBank_2.tx"
		;
connectAttr "cp_c009001daipa:root_waist_ikCtrl_outPutAnimBank_2_translateY.o" "cp_c009001daipa:root_waist_ikCtrl_outPutAnimBank_2.ty"
		;
connectAttr "cp_c009001daipa:root_waist_ikCtrl_outPutAnimBank_2_translateZ.o" "cp_c009001daipa:root_waist_ikCtrl_outPutAnimBank_2.tz"
		;
connectAttr "cp_c009001daipa:root_waist_ikCtrl_outPutAnimBank_2_rotateX.o" "cp_c009001daipa:root_waist_ikCtrl_outPutAnimBank_2.rx"
		;
connectAttr "cp_c009001daipa:root_waist_ikCtrl_outPutAnimBank_2_rotateY.o" "cp_c009001daipa:root_waist_ikCtrl_outPutAnimBank_2.ry"
		;
connectAttr "cp_c009001daipa:root_waist_ikCtrl_outPutAnimBank_2_rotateZ.o" "cp_c009001daipa:root_waist_ikCtrl_outPutAnimBank_2.rz"
		;
connectAttr "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_2_translateX.o" "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_2.tx"
		;
connectAttr "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_2_translateY.o" "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_2.ty"
		;
connectAttr "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_2_translateZ.o" "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_2.tz"
		;
connectAttr "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_2_rotateX.o" "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_2.rx"
		;
connectAttr "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_2_rotateY.o" "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_2.ry"
		;
connectAttr "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_2_rotateZ.o" "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_2.rz"
		;
connectAttr "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_2_raiseBall.o" "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_2.raiseBall"
		;
connectAttr "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_2_raiseToeTip.o" "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_2.raiseToeTip"
		;
connectAttr "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_2_side.o" "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_2.side"
		;
connectAttr "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_2_swivel.o" "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_2.swivel"
		;
connectAttr "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_2_roll.o" "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_2.roll"
		;
connectAttr "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_2_raiseToe.o" "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_2.raiseToe"
		;
connectAttr "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_2_swivelToe.o" "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_2.swivelToe"
		;
connectAttr "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_2_twistToe.o" "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_2.twistToe"
		;
connectAttr "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_2_translateX.o" "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_2.tx"
		;
connectAttr "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_2_translateY.o" "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_2.ty"
		;
connectAttr "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_2_translateZ.o" "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_2.tz"
		;
connectAttr "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_2_rotateX.o" "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_2.rx"
		;
connectAttr "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_2_rotateY.o" "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_2.ry"
		;
connectAttr "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_2_rotateZ.o" "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_2.rz"
		;
connectAttr "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_2_raiseBall.o" "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_2.raiseBall"
		;
connectAttr "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_2_raiseToeTip.o" "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_2.raiseToeTip"
		;
connectAttr "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_2_side.o" "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_2.side"
		;
connectAttr "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_2_swivel.o" "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_2.swivel"
		;
connectAttr "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_2_roll.o" "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_2.roll"
		;
connectAttr "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_2_raiseToe.o" "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_2.raiseToe"
		;
connectAttr "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_2_swivelToe.o" "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_2.swivelToe"
		;
connectAttr "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_2_twistToe.o" "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_2.twistToe"
		;
connectAttr "cp_c009001daipa:LfArm_Wrist_FK_outPutAnimBank_2_rotateX.o" "cp_c009001daipa:LfArm_Wrist_FK_outPutAnimBank_2.rx"
		;
connectAttr "cp_c009001daipa:LfArm_Wrist_FK_outPutAnimBank_2_rotateY.o" "cp_c009001daipa:LfArm_Wrist_FK_outPutAnimBank_2.ry"
		;
connectAttr "cp_c009001daipa:LfArm_Wrist_FK_outPutAnimBank_2_rotateZ.o" "cp_c009001daipa:LfArm_Wrist_FK_outPutAnimBank_2.rz"
		;
connectAttr "cp_c009001daipa:LfArm_Elbow_FK_outPutAnimBank_2_rotateX.o" "cp_c009001daipa:LfArm_Elbow_FK_outPutAnimBank_2.rx"
		;
connectAttr "cp_c009001daipa:LfArm_Elbow_FK_outPutAnimBank_2_rotateY.o" "cp_c009001daipa:LfArm_Elbow_FK_outPutAnimBank_2.ry"
		;
connectAttr "cp_c009001daipa:LfArm_Elbow_FK_outPutAnimBank_2_rotateZ.o" "cp_c009001daipa:LfArm_Elbow_FK_outPutAnimBank_2.rz"
		;
connectAttr "cp_c009001daipa:LfArm_UpArm_FK_outPutAnimBank_2_rotateX.o" "cp_c009001daipa:LfArm_UpArm_FK_outPutAnimBank_2.rx"
		;
connectAttr "cp_c009001daipa:LfArm_UpArm_FK_outPutAnimBank_2_rotateY.o" "cp_c009001daipa:LfArm_UpArm_FK_outPutAnimBank_2.ry"
		;
connectAttr "cp_c009001daipa:LfArm_UpArm_FK_outPutAnimBank_2_rotateZ.o" "cp_c009001daipa:LfArm_UpArm_FK_outPutAnimBank_2.rz"
		;
connectAttr "cp_c009001daipa:LfArm_UpArm_FK_outPutAnimBank_2_twistPlacement.o" "cp_c009001daipa:LfArm_UpArm_FK_outPutAnimBank_2.twistPlacement"
		;
connectAttr "cp_c009001daipa:LfArm_UpArm_FK_outPutAnimBank_2_addTwist.o" "cp_c009001daipa:LfArm_UpArm_FK_outPutAnimBank_2.addTwist"
		;
connectAttr "cp_c009001daipa:Lf_shoulder_outPutAnimBank_2_translateX.o" "cp_c009001daipa:Lf_shoulder_outPutAnimBank_2.tx"
		;
connectAttr "cp_c009001daipa:Lf_shoulder_outPutAnimBank_2_translateY.o" "cp_c009001daipa:Lf_shoulder_outPutAnimBank_2.ty"
		;
connectAttr "cp_c009001daipa:Lf_shoulder_outPutAnimBank_2_translateZ.o" "cp_c009001daipa:Lf_shoulder_outPutAnimBank_2.tz"
		;
connectAttr "cp_c009001daipa:Lf_shoulder_outPutAnimBank_2_rotateX.o" "cp_c009001daipa:Lf_shoulder_outPutAnimBank_2.rx"
		;
connectAttr "cp_c009001daipa:Lf_shoulder_outPutAnimBank_2_rotateY.o" "cp_c009001daipa:Lf_shoulder_outPutAnimBank_2.ry"
		;
connectAttr "cp_c009001daipa:Lf_shoulder_outPutAnimBank_2_rotateZ.o" "cp_c009001daipa:Lf_shoulder_outPutAnimBank_2.rz"
		;
connectAttr "cp_c009001daipa:Lf_shoulder_outPutAnimBank_2_Arm_follow.o" "cp_c009001daipa:Lf_shoulder_outPutAnimBank_2.Arm_follow"
		;
connectAttr "cp_c009001daipa:Rt_shoulder_outPutAnimBank_2_translateX.o" "cp_c009001daipa:Rt_shoulder_outPutAnimBank_2.tx"
		;
connectAttr "cp_c009001daipa:Rt_shoulder_outPutAnimBank_2_translateY.o" "cp_c009001daipa:Rt_shoulder_outPutAnimBank_2.ty"
		;
connectAttr "cp_c009001daipa:Rt_shoulder_outPutAnimBank_2_translateZ.o" "cp_c009001daipa:Rt_shoulder_outPutAnimBank_2.tz"
		;
connectAttr "cp_c009001daipa:Rt_shoulder_outPutAnimBank_2_rotateX.o" "cp_c009001daipa:Rt_shoulder_outPutAnimBank_2.rx"
		;
connectAttr "cp_c009001daipa:Rt_shoulder_outPutAnimBank_2_rotateY.o" "cp_c009001daipa:Rt_shoulder_outPutAnimBank_2.ry"
		;
connectAttr "cp_c009001daipa:Rt_shoulder_outPutAnimBank_2_rotateZ.o" "cp_c009001daipa:Rt_shoulder_outPutAnimBank_2.rz"
		;
connectAttr "cp_c009001daipa:Rt_shoulder_outPutAnimBank_2_Arm_follow.o" "cp_c009001daipa:Rt_shoulder_outPutAnimBank_2.Arm_follow"
		;
connectAttr "cp_c009001daipa:RtArm_UpArm_FK_outPutAnimBank_2_rotateX.o" "cp_c009001daipa:RtArm_UpArm_FK_outPutAnimBank_2.rx"
		;
connectAttr "cp_c009001daipa:RtArm_UpArm_FK_outPutAnimBank_2_rotateY.o" "cp_c009001daipa:RtArm_UpArm_FK_outPutAnimBank_2.ry"
		;
connectAttr "cp_c009001daipa:RtArm_UpArm_FK_outPutAnimBank_2_rotateZ.o" "cp_c009001daipa:RtArm_UpArm_FK_outPutAnimBank_2.rz"
		;
connectAttr "cp_c009001daipa:RtArm_UpArm_FK_outPutAnimBank_2_twistPlacement.o" "cp_c009001daipa:RtArm_UpArm_FK_outPutAnimBank_2.twistPlacement"
		;
connectAttr "cp_c009001daipa:RtArm_UpArm_FK_outPutAnimBank_2_addTwist.o" "cp_c009001daipa:RtArm_UpArm_FK_outPutAnimBank_2.addTwist"
		;
connectAttr "cp_c009001daipa:RtArm_Elbow_FK_outPutAnimBank_2_rotateX.o" "cp_c009001daipa:RtArm_Elbow_FK_outPutAnimBank_2.rx"
		;
connectAttr "cp_c009001daipa:RtArm_Elbow_FK_outPutAnimBank_2_rotateY.o" "cp_c009001daipa:RtArm_Elbow_FK_outPutAnimBank_2.ry"
		;
connectAttr "cp_c009001daipa:RtArm_Elbow_FK_outPutAnimBank_2_rotateZ.o" "cp_c009001daipa:RtArm_Elbow_FK_outPutAnimBank_2.rz"
		;
connectAttr "cp_c009001daipa:RtArm_Wrist_FK_outPutAnimBank_2_rotateX.o" "cp_c009001daipa:RtArm_Wrist_FK_outPutAnimBank_2.rx"
		;
connectAttr "cp_c009001daipa:RtArm_Wrist_FK_outPutAnimBank_2_rotateY.o" "cp_c009001daipa:RtArm_Wrist_FK_outPutAnimBank_2.ry"
		;
connectAttr "cp_c009001daipa:RtArm_Wrist_FK_outPutAnimBank_2_rotateZ.o" "cp_c009001daipa:RtArm_Wrist_FK_outPutAnimBank_2.rz"
		;
connectAttr "cp_c009001daipa:head_ctrl_outPutAnimBank_2_translateX.o" "cp_c009001daipa:head_ctrl_outPutAnimBank_2.tx"
		;
connectAttr "cp_c009001daipa:head_ctrl_outPutAnimBank_2_translateY.o" "cp_c009001daipa:head_ctrl_outPutAnimBank_2.ty"
		;
connectAttr "cp_c009001daipa:head_ctrl_outPutAnimBank_2_translateZ.o" "cp_c009001daipa:head_ctrl_outPutAnimBank_2.tz"
		;
connectAttr "cp_c009001daipa:head_ctrl_outPutAnimBank_2_rotateX.o" "cp_c009001daipa:head_ctrl_outPutAnimBank_2.rx"
		;
connectAttr "cp_c009001daipa:head_ctrl_outPutAnimBank_2_rotateY.o" "cp_c009001daipa:head_ctrl_outPutAnimBank_2.ry"
		;
connectAttr "cp_c009001daipa:head_ctrl_outPutAnimBank_2_rotateZ.o" "cp_c009001daipa:head_ctrl_outPutAnimBank_2.rz"
		;
connectAttr "cp_c009001daipa:head_ctrl_outPutAnimBank_2_rotation.o" "cp_c009001daipa:head_ctrl_outPutAnimBank_2.rotation"
		;
connectAttr "cp_c009001daipa:head_ctrl_outPutAnimBank_2_DYNHatPrimaryCtrl.o" "cp_c009001daipa:head_ctrl_outPutAnimBank_2.DYNHatPrimaryCtrl"
		;
connectAttr "cp_c009001daipa:head_ctrl_outPutAnimBank_2_DYNHatStartFrame.o" "cp_c009001daipa:head_ctrl_outPutAnimBank_2.DYNHatStartFrame"
		;
connectAttr "cp_c009001daipa:head_ctrl_outPutAnimBank_2_DYNEaringPrimaryCtrl.o" "cp_c009001daipa:head_ctrl_outPutAnimBank_2.DYNEaringPrimaryCtrl"
		;
connectAttr "cp_c009001daipa:head_ctrl_outPutAnimBank_2_DYNEaringStartFrame.o" "cp_c009001daipa:head_ctrl_outPutAnimBank_2.DYNEaringStartFrame"
		;
connectAttr "cp_c009001daipa:head_ctrl_outPutAnimBank_2_DYNNecklacePrimaryCtrl.o" "cp_c009001daipa:head_ctrl_outPutAnimBank_2.DYNNecklacePrimaryCtrl"
		;
connectAttr "cp_c009001daipa:head_ctrl_outPutAnimBank_2_DYNNecklaceStartFrame.o" "cp_c009001daipa:head_ctrl_outPutAnimBank_2.DYNNecklaceStartFrame"
		;
connectAttr "cp_c009001daipa:waist_FK1_ctrl_outPutAnimBank_2_translateX.o" "cp_c009001daipa:waist_FK1_ctrl_outPutAnimBank_2.tx"
		;
connectAttr "cp_c009001daipa:waist_FK1_ctrl_outPutAnimBank_2_translateY.o" "cp_c009001daipa:waist_FK1_ctrl_outPutAnimBank_2.ty"
		;
connectAttr "cp_c009001daipa:waist_FK1_ctrl_outPutAnimBank_2_translateZ.o" "cp_c009001daipa:waist_FK1_ctrl_outPutAnimBank_2.tz"
		;
connectAttr "cp_c009001daipa:waist_FK1_ctrl_outPutAnimBank_2_rotateX.o" "cp_c009001daipa:waist_FK1_ctrl_outPutAnimBank_2.rx"
		;
connectAttr "cp_c009001daipa:waist_FK1_ctrl_outPutAnimBank_2_rotateY.o" "cp_c009001daipa:waist_FK1_ctrl_outPutAnimBank_2.ry"
		;
connectAttr "cp_c009001daipa:waist_FK1_ctrl_outPutAnimBank_2_rotateZ.o" "cp_c009001daipa:waist_FK1_ctrl_outPutAnimBank_2.rz"
		;
connectAttr "cp_c009001daipa:waist_FK2_ctrl_outPutAnimBank_2_translateX.o" "cp_c009001daipa:waist_FK2_ctrl_outPutAnimBank_2.tx"
		;
connectAttr "cp_c009001daipa:waist_FK2_ctrl_outPutAnimBank_2_translateY.o" "cp_c009001daipa:waist_FK2_ctrl_outPutAnimBank_2.ty"
		;
connectAttr "cp_c009001daipa:waist_FK2_ctrl_outPutAnimBank_2_translateZ.o" "cp_c009001daipa:waist_FK2_ctrl_outPutAnimBank_2.tz"
		;
connectAttr "cp_c009001daipa:waist_FK2_ctrl_outPutAnimBank_2_rotateX.o" "cp_c009001daipa:waist_FK2_ctrl_outPutAnimBank_2.rx"
		;
connectAttr "cp_c009001daipa:waist_FK2_ctrl_outPutAnimBank_2_rotateY.o" "cp_c009001daipa:waist_FK2_ctrl_outPutAnimBank_2.ry"
		;
connectAttr "cp_c009001daipa:waist_FK2_ctrl_outPutAnimBank_2_rotateZ.o" "cp_c009001daipa:waist_FK2_ctrl_outPutAnimBank_2.rz"
		;
// End of run.ma

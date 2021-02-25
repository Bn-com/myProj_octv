//Maya ASCII 2011 scene
//Name: walk.ma
//Last modified: Wed, Jul 11, 2012 06:07:43 PM
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
	setAttr ".range" -type "string" "\"1:24\"";
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
createNode animCurveTL -n "cp_c009001daipa:waist_Ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -0.079643020923661975 7 -0.5 16 0.5 22 
		0.026567299999999999 23 -0.079642913670439047;
	setAttr -s 5 ".kix[0:4]"  0.38422796130180359 0.99519520998001099 
		0.90902000665664673 0.36719605326652527 0.38422796130180359;
	setAttr -s 5 ".kiy[0:4]"  -0.92323827743530273 -0.097910940647125244 
		0.41675248742103577 -0.93014365434646606 -0.92323827743530273;
	setAttr -s 5 ".kox[0:4]"  0.38422790169715881 0.99519520998001099 
		0.90902000665664673 0.36719602346420288 0.38422790169715881;
	setAttr -s 5 ".koy[0:4]"  -0.92323827743530273 -0.097910940647125244 
		0.41675248742103577 -0.93014359474182129 -0.92323827743530273;
createNode animCurveTL -n "cp_c009001daipa:waist_Ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  1 -0.60973023241773916 2 -0.71826431547538439 
		4 -0.67825442645867018 8 -0.17277928429978459 10 -0.28835515713747528 13 -0.65607710435817246 
		15 -0.73474652729428502 19 -0.17107928429978461 21 -0.26948915713747529 23 -0.6367819965625382;
	setAttr -s 10 ".kit[0:9]"  10 1 1 1 1 1 1 1 
		1 10;
	setAttr -s 10 ".kot[0:9]"  10 1 1 1 1 1 1 1 
		1 10;
	setAttr -s 10 ".kix[1:9]"  0.72843718528747559 0.58654028177261353 
		0.76288056373596191 0.28568559885025024 0.50349533557891846 0.99944669008255005 0.76740062236785889 
		0.27599507570266724 0.22126172482967377;
	setAttr -s 10 ".kiy[1:9]"  -0.6851125955581665 0.80992013216018677 
		0.64653944969177246 -0.95832341909408569 -0.86399787664413452 0.033263154327869415 
		0.64116799831390381 -0.96115905046463013 -0.97521448135375977;
	setAttr -s 10 ".kox[1:9]"  0.72843718528747559 0.58654028177261353 
		0.76288056373596191 0.28568559885025024 0.50349539518356323 0.99944663047790527 0.76740062236785889 
		0.27599504590034485 0.22126172482967377;
	setAttr -s 10 ".koy[1:9]"  -0.6851125955581665 0.80992007255554199 
		0.64653944969177246 -0.95832341909408569 -0.8639979362487793 0.033263511955738068 
		0.64116799831390381 -0.96115905046463013 -0.97521448135375977;
createNode animCurveTL -n "cp_c009001daipa:waist_Ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 4 1.651973 7 3.267846 13 6.541053 23 
		12.347789;
	setAttr -s 5 ".kit[0:4]"  9 10 10 10 9;
	setAttr -s 5 ".kot[0:4]"  9 10 10 10 9;
createNode animCurveTA -n "cp_c009001daipa:waist_Ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 2.8417302530177566 4 4.6142592530177575 
		10 0.93513625301775716 15 4.6190252530177576 20 0.90935925301775689 23 2.8417302530177566;
	setAttr -s 6 ".kit[0:5]"  1 1 10 10 10 1;
	setAttr -s 6 ".kot[0:5]"  1 1 10 10 10 1;
	setAttr -s 6 ".kix[0:5]"  0.95670974254608154 0.99999892711639404 
		1 0.99999940395355225 1 0.95670974254608154;
	setAttr -s 6 ".kiy[0:5]"  0.29104393720626831 0.0014812014997005463 
		0.00018148886738345027 -0.0010797437280416489 0 0.29104393720626831;
	setAttr -s 6 ".kox[0:5]"  0.95670974254608154 0.99999892711639404 
		1 0.99999940395355225 1 0.95670974254608154;
	setAttr -s 6 ".koy[0:5]"  0.29104393720626831 0.0014812016161158681 
		0.00018148886738345027 -0.0010797437280416489 0 0.29104393720626831;
createNode animCurveTA -n "cp_c009001daipa:waist_Ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 10.734034714807244 3 13 14 -13 23 10.734035383554975;
	setAttr -s 4 ".kit[1:3]"  3 10 1;
	setAttr -s 4 ".kot[1:3]"  3 10 1;
	setAttr -s 4 ".kix[0:3]"  0.75764936208724976 1 0.99887567758560181 
		0.75764936208724976;
	setAttr -s 4 ".kiy[0:3]"  0.65266180038452148 0 -0.047404896467924118 
		0.65266180038452148;
	setAttr -s 4 ".kox[0:3]"  0.75764948129653931 1 0.99887567758560181 
		0.75764948129653931;
	setAttr -s 4 ".koy[0:3]"  0.65266174077987671 0 -0.047404896467924118 
		0.65266174077987671;
createNode animCurveTA -n "cp_c009001daipa:waist_Ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 0 8 -3.0000000000000004 18 3.0000000000000004 
		23 0;
	setAttr -s 4 ".kix[0:3]"  0.96733903884887695 0.99987155199050903 
		0.99943083524703979 0.96733903884887695;
	setAttr -s 4 ".kiy[0:3]"  -0.25348609685897827 -0.016030380502343178 
		0.033735502511262894 -0.25348609685897827;
	setAttr -s 4 ".kox[0:3]"  0.96733903884887695 0.99987155199050903 
		0.99943083524703979 0.96733903884887695;
	setAttr -s 4 ".koy[0:3]"  -0.25348612666130066 -0.016030382364988327 
		0.033735498785972595 -0.25348612666130066;
createNode animCurveTU -n "cp_c009001daipa:waist_Ctrl_outPutAnimBank_1_ikfk_switch";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 2 23 2;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "cp_c009001daipa:waist_Ctrl_outPutAnimBank_1_second_vis";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 23 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTL -n "cp_c009001daipa:root_waist_ikCtrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 23 0;
createNode animCurveTL -n "cp_c009001daipa:root_waist_ikCtrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 23 0;
createNode animCurveTL -n "cp_c009001daipa:root_waist_ikCtrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 23 0;
createNode animCurveTA -n "cp_c009001daipa:root_waist_ikCtrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 23 0;
createNode animCurveTA -n "cp_c009001daipa:root_waist_ikCtrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 23 0;
createNode animCurveTA -n "cp_c009001daipa:root_waist_ikCtrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 0 7 -1 18 1 23 0;
	setAttr -s 4 ".kit[0:3]"  1 10 10 1;
	setAttr -s 4 ".kot[0:3]"  1 10 10 1;
	setAttr -s 4 ".kix[0:3]"  0.99367189407348633 1 1 0.99367189407348633;
	setAttr -s 4 ".kiy[0:3]"  -0.11232155561447144 0 0 -0.11232155561447144;
	setAttr -s 4 ".kox[0:3]"  0.99367189407348633 1 1 0.99367189407348633;
	setAttr -s 4 ".koy[0:3]"  -0.11232158541679382 0 0 -0.11232158541679382;
createNode animCurveTL -n "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  1 0.48557675101895215 4 0.48557675101895215 
		8 0.48557675101895215 11 0.48557675101895215 12 0.48557675101895215 14 0.48557675101895215 
		19 0.28574674383641641 23 0.48557675101895215;
createNode animCurveTL -n "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  1 0 4 0 8 0 11 0 12 0 14 0 20 0.56088404384824841 
		23 0;
createNode animCurveTL -n "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 3.339684 4 3.339684 8 3.339684 11 3.339684 
		12 3.339684 14 3.339684 19 8.810313 22 14.699775 23 15.68798;
	setAttr -s 9 ".kit[6:8]"  1 10 10;
	setAttr -s 9 ".kot[6:8]"  1 10 10;
	setAttr -s 9 ".kix[6:8]"  0.022926764562726021 0.024225905537605286 
		0.042126521468162537;
	setAttr -s 9 ".kiy[6:8]"  0.9997372031211853 0.99970650672912598 
		0.99911224842071533;
	setAttr -s 9 ".kox[6:8]"  0.022926764562726021 0.024225905537605286 
		0.042126525193452835;
	setAttr -s 9 ".koy[6:8]"  0.9997372031211853 0.99970650672912598 
		0.99911230802536011;
createNode animCurveTA -n "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  1 -22.001692 2 -3.866869 3 0 4 0 8 0 11 
		0 12 0 14 0 17 -3.6282069999999997 19 -8.175254 22 -16.16596 23 -22.001692;
	setAttr -s 12 ".kit[0:11]"  3 10 10 10 10 10 10 10 
		10 10 1 3;
	setAttr -s 12 ".kot[0:11]"  3 10 10 10 10 10 10 10 
		10 10 1 3;
	setAttr -s 12 ".kix[10:11]"  0.5546233057975769 1;
	setAttr -s 12 ".kiy[10:11]"  -0.83210152387619019 0;
	setAttr -s 12 ".kox[10:11]"  0.5546233057975769 1;
	setAttr -s 12 ".koy[10:11]"  -0.83210152387619019 0;
createNode animCurveTA -n "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  1 -13.202438093683588 4 -13.202438093683588 
		8 -13.202438093683588 11 -13.202438093683588 12 -13.202438093683588 14 -13.202438093683588 
		17 -13.202757093683582 19 -18.561208063969335 22 -14.462678803750688 23 -13.202438093683588;
	setAttr -s 10 ".kit[6:9]"  3 10 1 10;
	setAttr -s 10 ".kot[6:9]"  3 10 1 10;
	setAttr -s 10 ".kix[8:9]"  0.82496386766433716 1;
	setAttr -s 10 ".kiy[8:9]"  0.56518560647964478 0;
	setAttr -s 10 ".kox[8:9]"  0.82496386766433716 1;
	setAttr -s 10 ".koy[8:9]"  0.565185546875 0;
createNode animCurveTA -n "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  1 0 4 0 8 0 11 0 12 0 14 0 17 -12.239307938142622 
		19 -13.367417214105007 22 0.10408410605046087 23 0;
	setAttr -s 10 ".kit[6:9]"  1 1 10 10;
	setAttr -s 10 ".kot[6:9]"  1 1 10 10;
	setAttr -s 10 ".kix[6:9]"  0.76446741819381714 0.98204386234283447 
		1 1;
	setAttr -s 10 ".kiy[6:9]"  -0.64466243982315063 0.18865299224853516 
		0 0;
	setAttr -s 10 ".kox[6:9]"  0.76446729898452759 0.98204386234283447 
		1 1;
	setAttr -s 10 ".koy[6:9]"  -0.64466249942779541 0.18865302205085754 
		0 0;
createNode animCurveTU -n "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1_raiseBall";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 8 0 11 8 12 13.40000057220459 13 
		25.028045654296875 14 27.999998 19 2.072397 23 0;
	setAttr -s 9 ".kit[6:8]"  1 1 10;
	setAttr -s 9 ".kot[6:8]"  1 1 10;
	setAttr -s 9 ".kix[6:8]"  0.62563484907150269 0.022875932976603508 
		0.080163337290287018;
	setAttr -s 9 ".kiy[6:8]"  -0.78011602163314819 -0.99973833560943604 
		-0.99678176641464233;
	setAttr -s 9 ".kox[6:8]"  0.62563550472259521 0.02287592925131321 
		0.080163337290287018;
	setAttr -s 9 ".koy[6:8]"  -0.78011548519134521 -0.99973833560943604 
		-0.99678176641464233;
createNode animCurveTU -n "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1_raiseToeTip";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 11 ".ktv[0:10]"  1 0 4 0 8 0 11 0 12 0 13 0 14 11 17 57.285331726074219 
		19 50.715934753417969 22 1.389858 23 0;
	setAttr -s 11 ".kit[8:10]"  1 1 10;
	setAttr -s 11 ".kot[8:10]"  1 1 10;
	setAttr -s 11 ".kix[8:10]"  0.0040360554121434689 0.013891059905290604 
		0.029965590685606003;
	setAttr -s 11 ".kiy[8:10]"  -0.99999183416366577 -0.99990350008010864 
		-0.99955093860626221;
	setAttr -s 11 ".kox[8:10]"  0.0040360554121434689 0.013891059905290604 
		0.029965590685606003;
	setAttr -s 11 ".koy[8:10]"  -0.99999183416366577 -0.99990350008010864 
		-0.99955093860626221;
createNode animCurveTU -n "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1_side";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  1 0 4 0 8 0 11 0 12 0 14 0 23 0;
createNode animCurveTU -n "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1_swivel";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  1 0 4 0 8 0 11 0 12 0 14 0 23 0;
createNode animCurveTU -n "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1_roll";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  1 0 4 0 8 0 11 0 12 0 14 0 23 0;
createNode animCurveTU -n "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1_raiseToe";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  1 15 2 13.7 3 0 4 0 8 0 11 0 12 0 14 0 
		19 -28.912756 23 15;
	setAttr -s 10 ".kit[0:9]"  3 1 10 10 10 10 10 10 
		10 3;
	setAttr -s 10 ".kot[0:9]"  3 1 10 10 10 10 10 10 
		10 3;
	setAttr -s 10 ".kix[1:9]"  0.011604362167418003 1 1 1 1 1 1 0.024992192164063454 
		1;
	setAttr -s 10 ".kiy[1:9]"  -0.99993270635604858 0 0 0 0 0 0 0.99968767166137695 
		0;
	setAttr -s 10 ".kox[1:9]"  0.011604362167418003 1 1 1 1 1 1 0.024992192164063454 
		1;
	setAttr -s 10 ".koy[1:9]"  -0.99993270635604858 0 0 0 0 0 0 0.99968767166137695 
		0;
createNode animCurveTU -n "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1_swivelToe";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  1 0 4 0 8 0 11 0 12 0 14 0 23 0;
createNode animCurveTU -n "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1_twistToe";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  1 0 4 0 8 0 11 0 12 0 14 0 23 0;
createNode animCurveTL -n "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 -0.48552378289463705 7 -0.27147710164300476 
		12 -0.48552378289463705 15 -0.48552378289463705 17 -0.48552378289463705 23 -0.48552378289463705;
	setAttr -s 6 ".kit[0:5]"  3 1 10 10 10 3;
	setAttr -s 6 ".kot[0:5]"  3 1 10 10 10 3;
	setAttr -s 6 ".kix[1:5]"  0.99871760606765747 1 1 1 1;
	setAttr -s 6 ".kiy[1:5]"  0.050627030432224274 0 0 0 0;
	setAttr -s 6 ".kox[1:5]"  0.99871766567230225 1 1 1 1;
	setAttr -s 6 ".koy[1:5]"  0.050626780837774277 0 0 0 0;
createNode animCurveTL -n "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 0 8 0.56088404384824875 12 0.11541657219982014 
		15 0 17 0 23 0;
	setAttr -s 6 ".kit[0:5]"  3 10 10 10 10 3;
	setAttr -s 6 ".kot[0:5]"  3 10 10 10 10 3;
createNode animCurveTL -n "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1_translateZ";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 -2.672081 8 2.848988 13 9.676681 15 9.676187 
		17 9.676187 23 9.676187;
	setAttr -s 6 ".kit[1:5]"  1 3 10 10 3;
	setAttr -s 6 ".kot[1:5]"  1 3 10 10 3;
	setAttr -s 6 ".kix[1:5]"  0.026596721261739731 1 1 1 1;
	setAttr -s 6 ".kiy[1:5]"  0.99964624643325806 0 0 0 0;
	setAttr -s 6 ".kox[1:5]"  0.026596706360578537 1 1 1 1;
	setAttr -s 6 ".koy[1:5]"  0.99964624643325806 0 0 0 0;
createNode animCurveTA -n "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1_rotateX";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  1 0 5 -0.055362500000000002 8 -2.585784 
		10 -10.571032 11 -18.704659 12 -22.451058 13 -15.607944999999999 15 0 17 0 23 0;
	setAttr -s 10 ".kit[0:9]"  3 10 1 10 1 1 1 10 
		10 3;
	setAttr -s 10 ".kot[0:9]"  3 10 1 10 1 1 1 10 
		10 3;
	setAttr -s 10 ".kix[2:9]"  0.74641215801239014 0.40604510903358459 
		0.30934566259384155 0.87809574604034424 0.21461530029773712 1 1 1;
	setAttr -s 10 ".kiy[2:9]"  -0.66548395156860352 -0.91385304927825928 
		-0.95094972848892212 -0.47848492860794067 0.97669863700866699 0 0 0;
	setAttr -s 10 ".kox[2:9]"  0.74641215801239014 0.40604510903358459 
		0.30934566259384155 0.87809574604034424 0.21461530029773712 1 1 1;
	setAttr -s 10 ".koy[2:9]"  -0.66548395156860352 -0.91385304927825928 
		-0.95094972848892212 -0.47848504781723022 0.97669863700866699 0 0 0;
createNode animCurveTA -n "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  1 9.8511458277978043 5 7.7666968022120795 
		8 6.2446004241854043 12 9.8511458277978043 15 9.8511458277978043 17 9.8511458277978043 
		23 9.8511458277978043;
	setAttr -s 7 ".kit[0:6]"  3 1 10 10 10 10 3;
	setAttr -s 7 ".kot[0:6]"  3 1 10 10 10 10 3;
	setAttr -s 7 ".kix[1:6]"  0.97341722249984741 1 1 1 1 1;
	setAttr -s 7 ".kiy[1:6]"  -0.22903923690319061 0 0 0 0 0;
	setAttr -s 7 ".kox[1:6]"  0.97341722249984741 1 1 1 1 1;
	setAttr -s 7 ".koy[1:6]"  -0.22903910279273987 0 0 0 0 0;
createNode animCurveTA -n "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  1 0 5 11.547488160942589 8 6.7239315074784445 
		12 0 15 0 17 0 23 0;
	setAttr -s 7 ".kit[0:6]"  3 10 1 10 10 10 3;
	setAttr -s 7 ".kot[0:6]"  3 10 1 10 10 10 3;
	setAttr -s 7 ".kix[2:6]"  0.70139890909194946 1 1 1 1;
	setAttr -s 7 ".kiy[2:6]"  -0.71276891231536865 0 0 0 0;
	setAttr -s 7 ".kox[2:6]"  0.70139890909194946 1 1 1 1;
	setAttr -s 7 ".koy[2:6]"  -0.71276891231536865 0 0 0 0;
createNode animCurveTU -n "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1_raiseBall";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  1 20.171655654907227 3 25.158077 8 5.910229 
		12 0 15 0 17 0 20 0 23 20.171655654907227;
	setAttr -s 8 ".kit[0:7]"  1 1 10 10 10 10 10 1;
	setAttr -s 8 ".kot[0:7]"  1 1 10 10 10 10 10 1;
	setAttr -s 8 ".kix[0:7]"  0.0070589794777333736 0.14981265366077423 
		0.01490409392863512 1 1 1 1 0.0070589794777333736;
	setAttr -s 8 ".kiy[0:7]"  0.99997508525848389 -0.98871439695358276 
		-0.99988889694213867 0 0 0 0 0.99997508525848389;
	setAttr -s 8 ".kox[0:7]"  0.007058984600007534 0.14981266856193542 
		0.01490409392863512 1 1 1 1 0.007058984600007534;
	setAttr -s 8 ".koy[0:7]"  0.99997508525848389 -0.98871439695358276 
		-0.99988889694213867 0 0 0 0 0.99997508525848389;
createNode animCurveTU -n "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1_raiseToeTip";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 11 ".ktv[0:10]"  1 0 3 20.73341 5 56.331230163574219 8 31.303431 
		10 13.200937 11 1.349935 12 -1.232849 13 -0.434091 15 0 17 0 23 0;
	setAttr -s 11 ".kit[0:10]"  3 10 10 1 10 1 10 10 
		10 10 3;
	setAttr -s 11 ".kot[0:10]"  3 10 10 1 10 1 10 10 
		10 10 3;
	setAttr -s 11 ".kix[3:10]"  0.0047238529659807682 0.0041730990633368492 
		0.0064224051311612129 0.046659957617521286 0.10087399184703827 1 1 1;
	setAttr -s 11 ".kiy[3:10]"  -0.999988853931427 -0.99999129772186279 
		-0.99997943639755249 -0.99891084432601929 0.9948992133140564 0 0 0;
	setAttr -s 11 ".kox[3:10]"  0.0047238534316420555 0.0041730990633368492 
		0.0064224051311612129 0.046659957617521286 0.10087399184703827 1 1 1;
	setAttr -s 11 ".koy[3:10]"  -0.999988853931427 -0.99999129772186279 
		-0.99997943639755249 -0.99891084432601929 0.9948992133140564 0 0 0;
createNode animCurveTU -n "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1_side";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 12 0 15 0 17 0 23 0;
	setAttr -s 5 ".kit[0:4]"  3 10 10 10 3;
	setAttr -s 5 ".kot[0:4]"  3 10 10 10 3;
createNode animCurveTU -n "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1_swivel";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 12 0 15 0 17 0 23 0;
	setAttr -s 5 ".kit[0:4]"  3 10 10 10 3;
	setAttr -s 5 ".kot[0:4]"  3 10 10 10 3;
createNode animCurveTU -n "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1_roll";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 12 0 15 0 17 0 23 0;
	setAttr -s 5 ".kit[0:4]"  3 10 10 10 3;
	setAttr -s 5 ".kot[0:4]"  3 10 10 10 3;
createNode animCurveTU -n "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1_raiseToe";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  1 0 8 -29.299999 12 13.1 13 13.420826 14 
		13.918753 15 0 17 0 23 0;
	setAttr -s 8 ".kit[0:7]"  3 10 1 10 1 10 10 3;
	setAttr -s 8 ".kot[0:7]"  3 10 1 10 1 10 10 3;
	setAttr -s 8 ".kix[2:7]"  0.25997960567474365 0.10125764459371567 
		0.21226368844509125 1 1 1;
	setAttr -s 8 ".kiy[2:7]"  0.96561414003372192 0.99486023187637329 
		0.97721242904663086 0 0 0;
	setAttr -s 8 ".kox[2:7]"  0.259979248046875 0.10125764459371567 0.21226321160793304 
		1 1 1;
	setAttr -s 8 ".koy[2:7]"  0.96561425924301147 0.99486023187637329 
		0.97721254825592041 0 0 0;
createNode animCurveTU -n "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1_swivelToe";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 12 0 15 0 17 0 23 0;
	setAttr -s 5 ".kit[0:4]"  3 10 10 10 3;
	setAttr -s 5 ".kot[0:4]"  3 10 10 10 3;
createNode animCurveTU -n "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1_twistToe";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 12 0 15 0 17 0 23 0;
	setAttr -s 5 ".kit[0:4]"  3 10 10 10 3;
	setAttr -s 5 ".kot[0:4]"  3 10 10 10 3;
createNode animCurveTA -n "cp_c009001daipa:LfArm_Wrist_FK_outPutAnimBank_1_rotateX";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 -0.92079113933703249 5 -7.3094415504118002 
		15 17.3324960641853 23 -0.92078975216160608;
	setAttr -s 4 ".kit[1:3]"  3 1 1;
	setAttr -s 4 ".kot[1:3]"  3 1 1;
	setAttr -s 4 ".kix[0:3]"  0.60986709594726563 1 0.99929314851760864 
		0.60986709594726563;
	setAttr -s 4 ".kiy[0:3]"  -0.79250365495681763 0 0.037593409419059753 
		-0.79250365495681763;
	setAttr -s 4 ".kox[0:3]"  0.66350191831588745 1 0.99929314851760864 
		0.66350191831588745;
	setAttr -s 4 ".koy[0:3]"  -0.74817466735839844 0 0.037593424320220947 
		-0.74817466735839844;
createNode animCurveTA -n "cp_c009001daipa:LfArm_Wrist_FK_outPutAnimBank_1_rotateY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 14.717676576835791 5 -2.6624366980571104 
		11 -23.331545644384516 15 -3.0371743606059498 21 19.654613704588368 23 14.717676576835791;
	setAttr -s 6 ".kit[2:5]"  9 1 1 1;
	setAttr -s 6 ".kot[2:5]"  9 1 1 1;
	setAttr -s 6 ".kix[0:5]"  0.50247031450271606 0.43186810612678528 
		0.99987685680389404 0.36785998940467834 0.99345356225967407 0.50247031450271606;
	setAttr -s 6 ".kiy[0:5]"  -0.86459445953369141 -0.90193676948547363 
		-0.015695041045546532 0.92988121509552002 0.11423678696155548 -0.86459445953369141;
	setAttr -s 6 ".kox[0:5]"  0.49900636076927185 0.4318680465221405 
		0.99987685680389404 0.36785989999771118 0.99345356225967407 0.49900636076927185;
	setAttr -s 6 ".koy[0:5]"  -0.86659830808639526 -0.90193682909011841 
		-0.015695041045546532 0.92988121509552002 0.11423677206039429 -0.86659830808639526;
createNode animCurveTA -n "cp_c009001daipa:LfArm_Wrist_FK_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 38 5 27.579259724523922 10 -5.3017017040695373 
		20 33.778102374596784 23 38;
	setAttr -s 5 ".kit[2:4]"  10 1 1;
	setAttr -s 5 ".kot[2:4]"  10 1 1;
	setAttr -s 5 ".kix[0:4]"  0.98928338289260864 0.43114262819290161 
		0.98534595966339111 0.50402373075485229 0.98928338289260864;
	setAttr -s 5 ".kiy[0:4]"  0.14600802958011627 -0.90228378772735596 
		0.17056767642498016 0.8636898398399353 0.14600802958011627;
	setAttr -s 5 ".kox[0:4]"  0.99990832805633545 0.43114224076271057 
		0.98534595966339111 0.50402367115020752 0.99990832805633545;
	setAttr -s 5 ".koy[0:4]"  0.01354288961738348 -0.90228396654129028 
		0.17056767642498016 0.8636898398399353 0.01354288961738348;
createNode animCurveTA -n "cp_c009001daipa:LfArm_Elbow_FK_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 4 0 23 0;
	setAttr -s 3 ".kit[1:2]"  9 10;
	setAttr -s 3 ".kot[1:2]"  9 10;
createNode animCurveTA -n "cp_c009001daipa:LfArm_Elbow_FK_outPutAnimBank_1_rotateY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -13.875502113311716 3 -22.358031329651769 
		8 -32.845966631140506 19 -2.9263056797088511 23 -13.968764144598222;
	setAttr -s 5 ".kix[0:4]"  0.43511378765106201 0.56645762920379639 
		0.99975240230560303 0.94766449928283691 0.43511378765106201;
	setAttr -s 5 ".kiy[0:4]"  -0.90037548542022705 -0.82409089803695679 
		-0.022252952679991722 0.31926801800727844 -0.90037548542022705;
	setAttr -s 5 ".kox[0:4]"  0.43880540132522583 0.56645762920379639 
		0.99975240230560303 0.94766449928283691 0.43880540132522583;
	setAttr -s 5 ".koy[0:4]"  -0.89858216047286987 -0.82409089803695679 
		-0.022252937778830528 0.31926801800727844 -0.89858216047286987;
createNode animCurveTA -n "cp_c009001daipa:LfArm_Elbow_FK_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 4 0 23 0;
	setAttr -s 3 ".kit[1:2]"  9 10;
	setAttr -s 3 ".kot[1:2]"  9 10;
createNode animCurveTA -n "cp_c009001daipa:LfArm_UpArm_FK_outPutAnimBank_1_rotateX";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -12.846065129088899 2 -10.572667439064411 
		7 -5.3312992075786454 15 -29.155682380028882 23 -12.845624612359032;
	setAttr -s 5 ".kit[3:4]"  3 1;
	setAttr -s 5 ".kot[3:4]"  3 1;
	setAttr -s 5 ".kix[0:4]"  0.71406358480453491 0.79255038499832153 
		0.98823416233062744 1 0.71406358480453491;
	setAttr -s 5 ".kiy[0:4]"  0.70008087158203125 0.60980653762817383 
		-0.15294873714447021 0 0.70008087158203125;
	setAttr -s 5 ".kox[0:4]"  0.71784746646881104 0.79255062341690063 
		0.98823410272598267 1 0.71784746646881104;
	setAttr -s 5 ".koy[0:4]"  0.69620043039321899 0.60980618000030518 
		-0.15294870734214783 0 0.69620043039321899;
createNode animCurveTA -n "cp_c009001daipa:LfArm_UpArm_FK_outPutAnimBank_1_rotateY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 -9 2 -10.736503210550811 12 16.617172864984042 
		23 -9;
	setAttr -s 4 ".kix[0:3]"  0.75260955095291138 0.89134019613265991 
		0.77314662933349609 0.75260955095291138;
	setAttr -s 4 ".kiy[0:3]"  -0.65846711397171021 -0.45333504676818848 
		0.63422733545303345 -0.65846711397171021;
	setAttr -s 4 ".kox[0:3]"  0.75260943174362183 0.89134019613265991 
		0.77314662933349609 0.75260943174362183;
	setAttr -s 4 ".koy[0:3]"  -0.65846723318099976 -0.45333504676818848 
		0.63422727584838867 -0.65846723318099976;
createNode animCurveTA -n "cp_c009001daipa:LfArm_UpArm_FK_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 -50.577213447931705 2 -49.371244871952463 
		7 -61.840383619705221 13 -49.69143687695091 19 -61.011878279758122 23 -50.577214682471336;
	setAttr -s 6 ".kit[0:5]"  1 3 10 3 10 1;
	setAttr -s 6 ".kot[0:5]"  1 3 10 3 10 1;
	setAttr -s 6 ".kix[0:5]"  0.73245513439178467 1 0.99992573261260986 
		1 0.99931240081787109 0.73245513439178467;
	setAttr -s 6 ".kiy[0:5]"  0.68081521987915039 0 -0.012191977351903915 
		0 -0.037077866494655609 0.68081521987915039;
	setAttr -s 6 ".kox[0:5]"  0.74511373043060303 1 0.99992573261260986 
		1 0.99931240081787109 0.74511373043060303;
	setAttr -s 6 ".koy[0:5]"  0.66693747043609619 0 -0.012191977351903915 
		0 -0.037077866494655609 0.66693747043609619;
createNode animCurveTU -n "cp_c009001daipa:LfArm_UpArm_FK_outPutAnimBank_1_twistPlacement";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 23 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "cp_c009001daipa:LfArm_UpArm_FK_outPutAnimBank_1_addTwist";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0.37907823920249939 2 0.37907824663027245 
		23 0.37907823920249939;
	setAttr -s 3 ".kit[1:2]"  3 10;
	setAttr -s 3 ".kot[1:2]"  3 10;
createNode animCurveTL -n "cp_c009001daipa:Lf_shoulder_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 4 0 23 0;
	setAttr -s 3 ".kit[1:2]"  3 10;
	setAttr -s 3 ".kot[1:2]"  3 10;
createNode animCurveTL -n "cp_c009001daipa:Lf_shoulder_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 4 0 23 0;
	setAttr -s 3 ".kit[1:2]"  3 10;
	setAttr -s 3 ".kot[1:2]"  3 10;
createNode animCurveTL -n "cp_c009001daipa:Lf_shoulder_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 4 0 23 0;
	setAttr -s 3 ".kit[1:2]"  3 10;
	setAttr -s 3 ".kot[1:2]"  3 10;
createNode animCurveTA -n "cp_c009001daipa:Lf_shoulder_outPutAnimBank_1_rotateX";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 0.64759533115873091 4 0.98891577448112422 
		15 -0.88062116889334618 23 0.64759511908499223;
	setAttr -s 4 ".kit[0:3]"  1 3 3 1;
	setAttr -s 4 ".kot[0:3]"  1 3 3 1;
	setAttr -s 4 ".kix[0:3]"  0.99766504764556885 1 1 0.99766504764556885;
	setAttr -s 4 ".kiy[0:3]"  0.068296760320663452 0 0 0.068296760320663452;
	setAttr -s 4 ".kox[0:3]"  0.99768775701522827 1 1 0.99768775701522827;
	setAttr -s 4 ".koy[0:3]"  0.067964173853397369 0 0 0.067964173853397369;
createNode animCurveTA -n "cp_c009001daipa:Lf_shoulder_outPutAnimBank_1_rotateY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -5.1444302117345737 4 -6.406971086021481 
		12 9.6753065910106564 15 10.761939887198317 23 -5.1444302117345737;
	setAttr -s 5 ".kit[1:4]"  3 1 3 1;
	setAttr -s 5 ".kot[1:4]"  3 1 3 1;
	setAttr -s 5 ".kix[0:4]"  0.95771276950836182 1 0.95450109243392944 
		1 0.95771276950836182;
	setAttr -s 5 ".kiy[0:4]"  -0.2877260148525238 0 0.29820749163627625 
		0 -0.2877260148525238;
	setAttr -s 5 ".kox[0:4]"  0.95771276950836182 1 0.95450109243392944 
		1 0.95771276950836182;
	setAttr -s 5 ".koy[0:4]"  -0.28772604465484619 0 0.29820749163627625 
		0 -0.28772604465484619;
createNode animCurveTA -n "cp_c009001daipa:Lf_shoulder_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 -3.5503006237104544 4 -2.458828550557334 
		15 -8.4372204205511494 23 -3.5503013018783403;
	setAttr -s 4 ".kit[0:3]"  1 3 3 1;
	setAttr -s 4 ".kot[0:3]"  1 3 3 1;
	setAttr -s 4 ".kix[0:3]"  0.96777749061584473 1 1 0.96777749061584473;
	setAttr -s 4 ".kiy[0:3]"  0.25180721282958984 0 0 0.25180721282958984;
	setAttr -s 4 ".kox[0:3]"  0.96926134824752808 1 1 0.96926134824752808;
	setAttr -s 4 ".koy[0:3]"  0.24603345990180969 0 0 0.24603345990180969;
createNode animCurveTU -n "cp_c009001daipa:Lf_shoulder_outPutAnimBank_1_Arm_follow";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 1 4 1 23 1;
	setAttr -s 3 ".kit[0:2]"  9 3 9;
	setAttr -s 3 ".kot[0:2]"  5 3 5;
createNode animCurveTL -n "cp_c009001daipa:Rt_shoulder_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 4 0 23 0;
	setAttr -s 3 ".kit[1:2]"  3 10;
	setAttr -s 3 ".kot[1:2]"  3 10;
createNode animCurveTL -n "cp_c009001daipa:Rt_shoulder_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 4 0 23 0;
	setAttr -s 3 ".kit[1:2]"  3 10;
	setAttr -s 3 ".kot[1:2]"  3 10;
createNode animCurveTL -n "cp_c009001daipa:Rt_shoulder_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 4 0 23 0;
	setAttr -s 3 ".kit[1:2]"  3 10;
	setAttr -s 3 ".kot[1:2]"  3 10;
createNode animCurveTA -n "cp_c009001daipa:Rt_shoulder_outPutAnimBank_1_rotateX";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 0.30690755306150913 4 -0.096912439440895823 
		16 1.7726245043826832 23 0.30690784370130497;
	setAttr -s 4 ".kit[0:3]"  1 3 3 1;
	setAttr -s 4 ".kot[0:3]"  1 3 3 1;
	setAttr -s 4 ".kix[0:3]"  0.99489808082580566 1 1 0.99489808082580566;
	setAttr -s 4 ".kiy[0:3]"  -0.10088565945625305 0 0 -0.10088565945625305;
	setAttr -s 4 ".kox[0:3]"  0.9951784610748291 1 1 0.9951784610748291;
	setAttr -s 4 ".koy[0:3]"  -0.098081134259700775 0 0 -0.098081134259700775;
createNode animCurveTA -n "cp_c009001daipa:Rt_shoulder_outPutAnimBank_1_rotateY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 7.1145013512591584 4 10.965634048743475 
		16 -7.2057982577637167 23 7.1144985767140305;
	setAttr -s 4 ".kit[1:3]"  3 1 1;
	setAttr -s 4 ".kot[1:3]"  3 1 1;
	setAttr -s 4 ".kix[0:3]"  0.7150198221206665 1 0.99879515171051025 
		0.7150198221206665;
	setAttr -s 4 ".kiy[0:3]"  0.6991041898727417 0 0.049073848873376846 
		0.6991041898727417;
	setAttr -s 4 ".kox[0:3]"  0.73949736356735229 1 0.99879515171051025 
		0.73949736356735229;
	setAttr -s 4 ".koy[0:3]"  0.67315948009490967 0 0.049073848873376846 
		0.67315948009490967;
createNode animCurveTA -n "cp_c009001daipa:Rt_shoulder_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 -6.7701863668456106 4 -8.0615190512276058 
		16 -2.0831271809820073 23 -6.7701854374397508;
	setAttr -s 4 ".kit[0:3]"  1 3 3 1;
	setAttr -s 4 ".kot[0:3]"  1 3 3 1;
	setAttr -s 4 ".kix[0:3]"  0.93772238492965698 1 1 0.93772238492965698;
	setAttr -s 4 ".kiy[0:3]"  -0.34738561511039734 0 0 -0.34738561511039734;
	setAttr -s 4 ".kox[0:3]"  0.96264553070068359 1 1 0.96264553070068359;
	setAttr -s 4 ".koy[0:3]"  -0.27076491713523865 0 0 -0.27076491713523865;
createNode animCurveTU -n "cp_c009001daipa:Rt_shoulder_outPutAnimBank_1_Arm_follow";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 1 4 1 23 1;
	setAttr -s 3 ".kit[0:2]"  9 3 9;
	setAttr -s 3 ".kot[0:2]"  5 3 5;
createNode animCurveTA -n "cp_c009001daipa:RtArm_UpArm_FK_outPutAnimBank_1_rotateX";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 -35.002995067975007 2 -36.469593677620558 
		17 -19.240479788514151 23 -34.960538248819056;
	setAttr -s 4 ".kit[2:3]"  10 1;
	setAttr -s 4 ".kot[2:3]"  10 1;
	setAttr -s 4 ".kix[0:3]"  0.70497757196426392 0.95990484952926636 
		0.99954730272293091 0.70497757196426392;
	setAttr -s 4 ".kiy[0:3]"  -0.70922970771789551 -0.28032615780830383 
		0.030086930841207504 -0.70922970771789551;
	setAttr -s 4 ".kox[0:3]"  0.77352124452590942 0.95990484952926636 
		0.99954730272293091 0.77352124452590942;
	setAttr -s 4 ".koy[0:3]"  -0.6337704062461853 -0.28032615780830383 
		0.030086930841207504 -0.6337704062461853;
createNode animCurveTA -n "cp_c009001daipa:RtArm_UpArm_FK_outPutAnimBank_1_rotateY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 13.026213193669717 2 15.035888394951099 
		13 -10.873276026448849 23 12.984387580362917;
	setAttr -s 4 ".kix[0:3]"  0.6403508186340332 0.879966139793396 0.95030617713928223 
		0.6403508186340332;
	setAttr -s 4 ".kiy[0:3]"  0.76808261871337891 0.47503650188446045 
		-0.3113168478012085 0.76808261871337891;
	setAttr -s 4 ".kox[0:3]"  0.69497382640838623 0.879966139793396 0.95030617713928223 
		0.69497382640838623;
	setAttr -s 4 ".koy[0:3]"  0.71903502941131592 0.47503647208213806 
		-0.3113168478012085 0.71903502941131592;
createNode animCurveTA -n "cp_c009001daipa:RtArm_UpArm_FK_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  1 -53.197689005570339 3 -50.265618507646558 
		5 -53.992734328833578 9 -61.808612951136674 14 -50.144324338047113 19 -61.549363316036057 
		23 -53.197689078861643;
	setAttr -s 7 ".kit[1:6]"  3 1 10 3 1 1;
	setAttr -s 7 ".kot[1:6]"  3 1 10 3 1 1;
	setAttr -s 7 ".kix[0:6]"  0.71059113740921021 1 0.62364238500595093 
		0.98433518409729004 1 0.9999803900718689 0.71059113740921021;
	setAttr -s 7 ".kiy[0:6]"  0.70360511541366577 0 -0.78170979022979736 
		0.17630736529827118 0 -0.0062723085284233093 0.70360511541366577;
	setAttr -s 7 ".kox[0:6]"  0.71367794275283813 1 0.62364238500595093 
		0.98433518409729004 1 0.9999803900718689 0.71367794275283813;
	setAttr -s 7 ".koy[0:6]"  0.70047402381896973 0 -0.78170979022979736 
		0.17630736529827118 0 -0.0062723043374717236 0.70047402381896973;
createNode animCurveTU -n "cp_c009001daipa:RtArm_UpArm_FK_outPutAnimBank_1_twistPlacement";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 23 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "cp_c009001daipa:RtArm_UpArm_FK_outPutAnimBank_1_addTwist";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0.37907823920249939 2 0.37907824663027245 
		23 0.37907823920249939;
	setAttr -s 3 ".kit[1:2]"  3 10;
	setAttr -s 3 ".kot[1:2]"  3 10;
createNode animCurveTA -n "cp_c009001daipa:RtArm_Elbow_FK_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 3 0 23 0;
	setAttr -s 3 ".kit[1:2]"  9 10;
	setAttr -s 3 ".kot[1:2]"  9 10;
createNode animCurveTA -n "cp_c009001daipa:RtArm_Elbow_FK_outPutAnimBank_1_rotateY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -28.457369472580822 3 -19.744150798613504 
		8 -7.390625499344857 19 -39.076732813772239 23 -28.489499679340629;
	setAttr -s 5 ".kix[0:4]"  0.45339810848236084 0.48945513367652893 
		0.99971264600753784 0.9971928596496582 0.45339810848236084;
	setAttr -s 5 ".kiy[0:4]"  0.89130806922912598 0.87202852964401245 
		-0.023970937356352806 0.074877262115478516 0.89130806922912598;
	setAttr -s 5 ".kox[0:4]"  0.45339816808700562 0.48945513367652893 
		0.99971264600753784 0.9971928596496582 0.45339816808700562;
	setAttr -s 5 ".koy[0:4]"  0.89130812883377075 0.87202852964401245 
		-0.023970918729901314 0.074877262115478516 0.89130812883377075;
createNode animCurveTA -n "cp_c009001daipa:RtArm_Elbow_FK_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 3 0 23 0;
	setAttr -s 3 ".kit[1:2]"  9 10;
	setAttr -s 3 ".kot[1:2]"  9 10;
createNode animCurveTA -n "cp_c009001daipa:RtArm_Wrist_FK_outPutAnimBank_1_rotateX";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 17.773783423003792 5 27.434186164795623 
		15 -0.3315685968585636 21 11.11022480771498 23 17.77378140515761;
	setAttr -s 5 ".kit[1:4]"  3 1 1 1;
	setAttr -s 5 ".kot[1:4]"  3 1 1 1;
	setAttr -s 5 ".kix[0:4]"  0.60162222385406494 1 0.99847382307052612 
		0.66213870048522949 0.60162222385406494;
	setAttr -s 5 ".kiy[0:4]"  0.79878073930740356 0 -0.055227048695087433 
		0.74938130378723145 0.79878073930740356;
	setAttr -s 5 ".kox[0:4]"  0.60432124137878418 1 0.99847382307052612 
		0.66213858127593994 0.60432124137878418;
	setAttr -s 5 ".koy[0:4]"  0.7967408299446106 0 -0.055227078497409821 
		0.749381422996521 0.7967408299446106;
createNode animCurveTA -n "cp_c009001daipa:RtArm_Wrist_FK_outPutAnimBank_1_rotateY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 -14.734994246473969 5 5.4693924426320848 
		11 28.997245562836873 15 4.6099121887426868 21 -17.910780462932873 23 -14.636227378828398;
	setAttr -s 6 ".kix[0:5]"  0.65555518865585327 0.34895718097686768 
		0.99994945526123047 0.43573787808418274 0.99985378980636597 0.65555518865585327;
	setAttr -s 6 ".kiy[0:5]"  0.75514727830886841 0.93713867664337158 
		0.010059810243546963 -0.90007364749908447 -0.01710035465657711 0.75514727830886841;
	setAttr -s 6 ".kox[0:5]"  0.65180414915084839 0.34895721077919006 
		0.99994939565658569 0.4357377290725708 0.99985378980636597 0.65180414915084839;
	setAttr -s 6 ".koy[0:5]"  0.75838726758956909 0.93713867664337158 
		0.010059773921966553 -0.90007370710372925 -0.01710033044219017 0.75838726758956909;
createNode animCurveTA -n "cp_c009001daipa:RtArm_Wrist_FK_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 13.490491248201586 5 37.348296452005719 
		15 13.890225312839945 21 2.7944513982284227 23 13.490486926114103;
	setAttr -s 5 ".kit[1:4]"  3 1 1 1;
	setAttr -s 5 ".kot[1:4]"  3 1 1 1;
	setAttr -s 5 ".kix[0:4]"  0.28809458017349243 1 0.66067904233932495 
		0.76163041591644287 0.28809458017349243;
	setAttr -s 5 ".kiy[0:4]"  0.95760190486907959 0 -0.75066858530044556 
		0.64801168441772461 0.95760190486907959;
	setAttr -s 5 ".kox[0:4]"  0.29774573445320129 1 0.66067898273468018 
		0.76163065433502197 0.29774573445320129;
	setAttr -s 5 ".koy[0:4]"  0.95464521646499634 0 -0.75066858530044556 
		0.64801138639450073 0.95464521646499634;
createNode animCurveTL -n "cp_c009001daipa:head_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 23 0;
createNode animCurveTL -n "cp_c009001daipa:head_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 23 0;
createNode animCurveTL -n "cp_c009001daipa:head_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 23 0;
createNode animCurveTA -n "cp_c009001daipa:head_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  1 -8.5639945767167021 3 -9.2858277154284501 
		6 -8.2604965074831309 9 -7.23516529953781 15 -9.2858277154284501 20 -7.23516529953781 
		23 -8.5639947140043322;
	setAttr -s 7 ".kit[1:6]"  10 1 1 10 10 1;
	setAttr -s 7 ".kot[1:6]"  10 1 1 10 10 1;
	setAttr -s 7 ".kix[0:6]"  0.97081649303436279 1 0.97202432155609131 
		0.99999529123306274 1 1 0.97081649303436279;
	setAttr -s 7 ".kiy[0:6]"  -0.23982354998588562 0 0.23487995564937592 
		0.0030929623171687126 0 0 -0.23982354998588562;
	setAttr -s 7 ".kox[0:6]"  0.97272306680679321 1 0.97202432155609131 
		0.99999529123306274 1 1 0.97272306680679321;
	setAttr -s 7 ".koy[0:6]"  -0.23196941614151001 0 0.23487992584705353 
		0.0030929623171687126 0 0 -0.23196941614151001;
createNode animCurveTA -n "cp_c009001daipa:head_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 23 0;
createNode animCurveTA -n "cp_c009001daipa:head_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 23 0;
createNode animCurveTU -n "cp_c009001daipa:head_ctrl_outPutAnimBank_1_rotation";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 23 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "cp_c009001daipa:head_ctrl_outPutAnimBank_1_DYNHatPrimaryCtrl";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 23 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "cp_c009001daipa:head_ctrl_outPutAnimBank_1_DYNHatStartFrame";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 20000 23 20000;
createNode animCurveTU -n "cp_c009001daipa:head_ctrl_outPutAnimBank_1_DYNEaringPrimaryCtrl";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 23 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "cp_c009001daipa:head_ctrl_outPutAnimBank_1_DYNEaringStartFrame";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 20000 23 20000;
createNode animCurveTU -n "cp_c009001daipa:head_ctrl_outPutAnimBank_1_DYNNecklacePrimaryCtrl";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 23 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "cp_c009001daipa:head_ctrl_outPutAnimBank_1_DYNNecklaceStartFrame";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 20000 23 20000;
createNode animCurveTL -n "cp_c009001daipa:waist_FK1_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 23 0;
createNode animCurveTL -n "cp_c009001daipa:waist_FK1_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 23 0;
createNode animCurveTL -n "cp_c009001daipa:waist_FK1_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 23 0;
createNode animCurveTA -n "cp_c009001daipa:waist_FK1_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 2.2035491635882365 5 3.7237573434890785 
		11 1.7561033219000162 16 3.7177381598120594 21 1.8331709648076104 23 2.2165588498676514;
	setAttr -s 6 ".kit[0:5]"  1 10 10 10 10 1;
	setAttr -s 6 ".kot[0:5]"  1 10 10 10 10 1;
	setAttr -s 6 ".kix[0:5]"  0.98718953132629395 1 1 1 1 0.98718953132629395;
	setAttr -s 6 ".kiy[0:5]"  0.15955217182636261 0 0 0 0 0.15955217182636261;
	setAttr -s 6 ".kox[0:5]"  0.98714834451675415 1 1 1 1 0.98714834451675415;
	setAttr -s 6 ".koy[0:5]"  0.15980653464794159 0 0 0 0 0.15980653464794159;
createNode animCurveTA -n "cp_c009001daipa:waist_FK1_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 -6.6739293610200408 2 -7 13 7 23 -6.6739290481169373;
	setAttr -s 4 ".kit[2:3]"  3 1;
	setAttr -s 4 ".kot[2:3]"  3 1;
	setAttr -s 4 ".kix[0:3]"  0.96760588884353638 0.99999290704727173 
		1 0.96760588884353638;
	setAttr -s 4 ".kiy[0:3]"  -0.25246554613113403 -0.0037679334636777639 
		0 -0.25246554613113403;
	setAttr -s 4 ".kox[0:3]"  0.96903795003890991 0.99999290704727173 
		1 0.96903795003890991;
	setAttr -s 4 ".koy[0:3]"  -0.24691210687160492 -0.0037679402157664299 
		0 -0.24691210687160492;
createNode animCurveTA -n "cp_c009001daipa:waist_FK1_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -1.9072479049893101 8 4 13 0 19 -4 23 
		-1.907248584331759;
	setAttr -s 5 ".kix[0:4]"  0.92735576629638672 0.99808681011199951 
		0.91020387411117554 0.99898260831832886 0.92735576629638672;
	setAttr -s 5 ".kiy[0:4]"  0.37418088316917419 0.061827823519706726 
		-0.41416060924530029 -0.045096486806869507 0.37418088316917419;
	setAttr -s 5 ".kox[0:4]"  0.92822778224945068 0.99808681011199951 
		0.91020375490188599 0.99898260831832886 0.92822778224945068;
	setAttr -s 5 ".koy[0:4]"  0.37201228737831116 0.061827916651964188 
		-0.41416075825691223 -0.045096512883901596 0.37201228737831116;
createNode animCurveTL -n "cp_c009001daipa:waist_FK2_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 23 0;
createNode animCurveTL -n "cp_c009001daipa:waist_FK2_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  1 0.043404702372173171 3 0.0021721399999999999 
		6 -0.055536200000000001 11 0.0598804 16 -0.055536200000000001 21 0.0598804 23 0.043385019254089295;
	setAttr -s 7 ".kit[3:6]"  10 1 1 1;
	setAttr -s 7 ".kot[3:6]"  10 1 1 1;
	setAttr -s 7 ".kix[0:6]"  0.9361993670463562 0.85773569345474243 
		0.98762989044189453 1 0.99944800138473511 0.99998652935028076 0.9361993670463562;
	setAttr -s 7 ".kiy[0:6]"  -0.35146942734718323 -0.514090895652771 
		-0.15680313110351563 0 -0.03322131559252739 -0.0051932758651673794 -0.35146942734718323;
	setAttr -s 7 ".kox[0:6]"  0.9361993670463562 0.85773569345474243 
		0.98762989044189453 1 0.99944800138473511 0.99998652935028076 0.9361993670463562;
	setAttr -s 7 ".koy[0:6]"  -0.35146945714950562 -0.514090895652771 
		-0.15680313110351563 0 -0.033221356570720673 -0.0051933177746832371 -0.35146945714950562;
createNode animCurveTL -n "cp_c009001daipa:waist_FK2_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 23 0;
createNode animCurveTA -n "cp_c009001daipa:waist_FK2_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  1 1.9424278186005464 3 2.6315036881988583 
		6 3.7237573434890785 12 1.7561033219000162 17 3.7177381598120594 22 1.8331709648076104 
		23 1.9398285980641921;
	setAttr -s 7 ".kit[0:6]"  1 1 10 10 10 10 1;
	setAttr -s 7 ".kot[0:6]"  1 1 10 10 10 10 1;
	setAttr -s 7 ".kix[0:6]"  0.99665540456771851 0.98345595598220825 
		1 1 1 1 0.99665540456771851;
	setAttr -s 7 ".kiy[0:6]"  0.08172009140253067 0.18114733695983887 
		0 0 0 0 0.08172009140253067;
	setAttr -s 7 ".kox[0:6]"  0.99679166078567505 0.98345595598220825 
		1 1 1 1 0.99679166078567505;
	setAttr -s 7 ".koy[0:6]"  0.080040037631988525 0.18114733695983887 
		0 0 0 0 0.080040037631988525;
createNode animCurveTA -n "cp_c009001daipa:waist_FK2_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 -5.7798648464346654 3 -7 14 7 23 -5.779865206529597;
	setAttr -s 4 ".kit[0:3]"  1 3 3 1;
	setAttr -s 4 ".kot[0:3]"  1 3 3 1;
	setAttr -s 4 ".kix[0:3]"  0.8567085862159729 1 1 0.8567085862159729;
	setAttr -s 4 ".kiy[0:3]"  -0.51580077409744263 0 0 -0.51580077409744263;
	setAttr -s 4 ".kox[0:3]"  0.89867526292800903 1 1 0.89867526292800903;
	setAttr -s 4 ".koy[0:3]"  -0.43861457705497742 0 0 -0.43861457705497742;
createNode animCurveTA -n "cp_c009001daipa:waist_FK2_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -2.6153618344731004 10 3.0000000000000004 
		15 0 21 -3.0000000000000004 23 -2.6153621696489879;
	setAttr -s 5 ".kix[0:4]"  0.97923535108566284 0.99896699190139771 
		0.93786263465881348 0.99945086240768433 0.97923535108566284;
	setAttr -s 5 ".kiy[0:4]"  0.20272690057754517 0.04544280469417572 
		-0.34700679779052734 -0.033135175704956055 0.20272690057754517;
	setAttr -s 5 ".kox[0:4]"  0.98433923721313477 0.99896699190139771 
		0.93786263465881348 0.99945086240768433 0.98433923721313477;
	setAttr -s 5 ".koy[0:4]"  0.17628449201583862 0.045442864298820496 
		-0.34700676798820496 -0.033135175704956055 0.17628449201583862;
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
// End of walk.ma

//Maya ASCII 2011 scene
//Name: slow_walk.ma
//Last modified: Wed, Jul 11, 2012 05:25:46 PM
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
	setAttr ".range" -type "string" "\"1:26\"";
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
	setAttr -s 5 ".ktv[0:4]"  1 -0.079643020923661975 7 -0.5 18 0.5 24 
		0.026567299999999999 25 -0.079642913670439047;
	setAttr -s 5 ".kix[0:4]"  0.41213956475257874 0.99592840671539307 
		0.92138731479644775 0.39431634545326233 0.41213956475257874;
	setAttr -s 5 ".kiy[0:4]"  -0.9111207127571106 -0.090148366987705231 
		0.38864564895629883 -0.91897481679916382 -0.9111207127571106;
	setAttr -s 5 ".kox[0:4]"  0.41213950514793396 0.99592840671539307 
		0.92138731479644775 0.39431631565093994 0.41213950514793396;
	setAttr -s 5 ".koy[0:4]"  -0.91112083196640015 -0.090148366987705231 
		0.38864564895629883 -0.91897475719451904 -0.91112083196640015;
createNode animCurveTL -n "cp_c009001daipa:waist_Ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 -0.31202659813530664 2 -0.36974631556631876 
		8 -0.1220963973710264 10 -0.14202479737800766 13 -0.31202659813530664 15 -0.36974631556631876 
		20 -0.12217568167081094 22 -0.12315879737800767 25 -0.31202659813530664;
	setAttr -s 9 ".kit[0:8]"  10 1 1 1 1 1 1 1 
		10;
	setAttr -s 9 ".kot[0:8]"  10 1 1 1 1 1 1 1 
		10;
	setAttr -s 9 ".kix[1:8]"  0.68700754642486572 0.80702835321426392 
		0.63704812526702881 0.56854242086410522 0.99953156709671021 0.75224018096923828 0.62345206737518311 
		0.55190956592559814;
	setAttr -s 9 ".kiy[1:8]"  -0.72665035724639893 0.59051269292831421 
		-0.77082407474517822 -0.82265394926071167 0.030606040731072426 0.65888893604278564 
		-0.78186166286468506 -0.833903968334198;
	setAttr -s 9 ".kox[1:8]"  0.68700748682022095 0.80702841281890869 
		0.63704800605773926 0.56854248046875 0.99953156709671021 0.75224030017852783 0.62345194816589355 
		0.55190956592559814;
	setAttr -s 9 ".koy[1:8]"  -0.7266504168510437 0.59051269292831421 
		-0.770824134349823 -0.82265388965606689 0.030606374144554138 0.65888893604278564 
		-0.78186172246932983 -0.833903968334198;
createNode animCurveTL -n "cp_c009001daipa:waist_Ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 4 1.0876816160553302 8 2.5533932101673966 
		14 4.9294259109611378 25 9.7;
	setAttr -s 5 ".kit[0:4]"  9 10 10 10 9;
	setAttr -s 5 ".kot[0:4]"  9 10 10 10 9;
createNode animCurveTA -n "cp_c009001daipa:waist_Ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 2.8417302530177566 4 4.6142592530177575 
		10 0.93513625301775716 16 4.6190252530177576 22 0.90935925301775689 25 2.8417302530177566;
	setAttr -s 6 ".kit[0:5]"  1 1 10 10 10 1;
	setAttr -s 6 ".kot[0:5]"  1 1 10 10 10 1;
	setAttr -s 6 ".kix[0:5]"  0.96299189329147339 0.99999910593032837 
		1 0.99999964237213135 1 0.96299189329147339;
	setAttr -s 6 ".kiy[0:5]"  0.26953041553497314 0.001362765091471374 
		0.00016636478540021926 -0.00089978671167045832 0 0.26953041553497314;
	setAttr -s 6 ".kox[0:5]"  0.96299189329147339 0.99999910593032837 
		1 0.99999964237213135 1 0.96299189329147339;
	setAttr -s 6 ".koy[0:5]"  0.26953041553497314 0.0013627652078866959 
		0.00016636478540021926 -0.00089978671167045832 0 0.26953041553497314;
createNode animCurveTA -n "cp_c009001daipa:waist_Ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 10 3 13 15 -13 25 10;
	setAttr -s 4 ".kit[1:3]"  3 10 1;
	setAttr -s 4 ".kot[1:3]"  3 10 1;
	setAttr -s 4 ".kix[0:3]"  0.72608834505081177 1 0.99837273359298706 
		0.68838953971862793;
	setAttr -s 4 ".kiy[0:3]"  0.68760150671005249 0 -0.057026918977499008 
		0.72534126043319702;
	setAttr -s 4 ".kox[0:3]"  0.72608834505081177 1 0.99837273359298706 
		0.68838953971862793;
	setAttr -s 4 ".koy[0:3]"  0.68760150671005249 0 -0.057026918977499008 
		0.72534120082855225;
createNode animCurveTA -n "cp_c009001daipa:waist_Ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 0 7 -3.0000000000000004 19 3.0000000000000004 
		25 0;
	setAttr -s 4 ".kix[0:3]"  0.97214591503143311 0.99989116191864014 
		0.99951815605163574 0.97214591503143311;
	setAttr -s 4 ".kiy[0:3]"  -0.23437631130218506 -0.014748883433640003 
		0.031040731817483902 -0.23437631130218506;
	setAttr -s 4 ".kox[0:3]"  0.97214591503143311 0.99989116191864014 
		0.99951815605163574 0.97214591503143311;
	setAttr -s 4 ".koy[0:3]"  -0.23437632620334625 -0.014748885296285152 
		0.031040728092193604 -0.23437632620334625;
createNode animCurveTU -n "cp_c009001daipa:waist_Ctrl_outPutAnimBank_1_ikfk_switch";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 2 25 2;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "cp_c009001daipa:waist_Ctrl_outPutAnimBank_1_second_vis";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 25 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTL -n "cp_c009001daipa:root_waist_ikCtrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 25 0;
createNode animCurveTL -n "cp_c009001daipa:root_waist_ikCtrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 25 0;
createNode animCurveTL -n "cp_c009001daipa:root_waist_ikCtrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 25 0;
createNode animCurveTA -n "cp_c009001daipa:root_waist_ikCtrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 25 0;
createNode animCurveTA -n "cp_c009001daipa:root_waist_ikCtrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 25 0;
createNode animCurveTA -n "cp_c009001daipa:root_waist_ikCtrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 0 8 -1 19 1 25 0;
	setAttr -s 4 ".kit[0:3]"  1 10 10 1;
	setAttr -s 4 ".kot[0:3]"  1 10 10 1;
	setAttr -s 4 ".kix[0:3]"  0.99463564157485962 1 1 0.99463564157485962;
	setAttr -s 4 ".kiy[0:3]"  -0.10344059020280838 0 0 -0.10344059020280838;
	setAttr -s 4 ".kox[0:3]"  0.99463564157485962 1 1 0.99463564157485962;
	setAttr -s 4 ".koy[0:3]"  -0.10344060510396957 0 0 -0.10344060510396957;
createNode animCurveTL -n "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  1 0.58497606426910376 4 0.58497606426910376 
		9 0.58497606426910376 12 0.58497606426910376 13 0.58497606426910376 15 0.58497606426910376 
		21 0.38514605708656802 25 0.58497606426910376;
createNode animCurveTL -n "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 4 0 9 0 12 0 13 0 15 0 18 0.029068238847461764 
		22 0.015257172243328149 25 0;
	setAttr -s 9 ".kit[7:8]"  1 3;
	setAttr -s 9 ".kot[7:8]"  1 3;
	setAttr -s 9 ".kix[7:8]"  0.99047559499740601 1;
	setAttr -s 9 ".kiy[7:8]"  -0.13768830895423889 0;
	setAttr -s 9 ".kox[7:8]"  0.99047559499740601 1;
	setAttr -s 9 ".koy[7:8]"  -0.13768832385540009 0;
createNode animCurveTL -n "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 2.6 4 2.6 9 2.6 12 2.6 13 2.6 15 2.6 
		21 7.1677636699646925 24 11.853460916380671 25 12.3;
	setAttr -s 9 ".kit[6:8]"  1 10 3;
	setAttr -s 9 ".kot[6:8]"  1 10 3;
	setAttr -s 9 ".kix[6:8]"  0.024918118491768837 0.032457355409860611 
		1;
	setAttr -s 9 ".kiy[6:8]"  0.99968951940536499 0.99947309494018555 
		0;
	setAttr -s 9 ".kox[6:8]"  0.024918118491768837 0.032457355409860611 
		1;
	setAttr -s 9 ".koy[6:8]"  0.99968951940536499 0.99947309494018555 
		0;
createNode animCurveTA -n "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  1 -14 2 -3.866869 3 0 4 0 9 0 12 0 13 0 
		15 0 18 -3.6282069999999997 21 -8.175254 24 -16.16596 25 -14;
	setAttr -s 12 ".kit[0:11]"  1 10 10 10 10 10 10 10 
		10 10 3 1;
	setAttr -s 12 ".kot[0:11]"  1 10 10 10 10 10 10 10 
		10 10 3 1;
	setAttr -s 12 ".kix[0:11]"  0.37493893504142761 0.32279026508331299 
		1 1 1 1 1 1 0.8685004711151123 0.75246471166610718 1 0.58766114711761475;
	setAttr -s 12 ".kiy[0:11]"  0.92704951763153076 0.94647049903869629 
		0 0 0 0 0 0 -0.49568828940391541 -0.65863257646560669 0 0.80910718441009521;
	setAttr -s 12 ".kox[0:11]"  0.37493896484375 0.32279026508331299 1 
		1 1 1 1 1 0.8685004711151123 0.75246471166610718 1 0.58766120672225952;
	setAttr -s 12 ".koy[0:11]"  0.92704951763153076 0.94647049903869629 
		0 0 0 0 0 0 -0.49568828940391541 -0.65863257646560669 0 0.80910718441009521;
createNode animCurveTA -n "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  1 -13.202438093683588 4 -13.202438093683588 
		9 -13.202438093683588 12 -13.202438093683588 13 -13.202438093683588 15 -13.202438093683588 
		18 -13.202757093683582 21 -14.485172618263691 24 -13.523866922993044 25 -13.202438093683588;
	setAttr -s 10 ".kit[6:9]"  3 10 1 10;
	setAttr -s 10 ".kot[6:9]"  3 10 1 10;
	setAttr -s 10 ".kix[8:9]"  0.97224467992782593 1;
	setAttr -s 10 ".kiy[8:9]"  0.23396638035774231 0;
	setAttr -s 10 ".kox[8:9]"  0.97224479913711548 1;
	setAttr -s 10 ".koy[8:9]"  0.23396624624729156 0;
createNode animCurveTA -n "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  1 0 4 0 9 0 12 0 13 0 15 0 18 -12.169139417238513 
		21 -8.4216626048604777 24 0.10408410605046087 25 0;
	setAttr -s 10 ".kit[6:9]"  1 1 10 10;
	setAttr -s 10 ".kot[6:9]"  1 1 10 10;
	setAttr -s 10 ".kix[6:9]"  0.79008817672729492 0.48227104544639587 
		1 1;
	setAttr -s 10 ".kiy[6:9]"  -0.61299329996109009 0.8760221004486084 
		0 0;
	setAttr -s 10 ".kox[6:9]"  0.79008805751800537 0.48227110505104065 
		1 1;
	setAttr -s 10 ".koy[6:9]"  -0.61299341917037964 0.87602204084396362 
		0 0;
createNode animCurveTU -n "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1_raiseBall";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  1 0 4 0 9 0 11 2.137037992477417 12 8 13 
		14.135995190303404 14 25.028045654296875 15 27.999998 21 2.072397 25 0;
	setAttr -s 10 ".kit[7:9]"  1 1 10;
	setAttr -s 10 ".kot[7:9]"  1 1 10;
	setAttr -s 10 ".kix[7:9]"  0.65708410739898682 0.024862876161932945 
		0.080163337290287018;
	setAttr -s 10 ".kiy[7:9]"  -0.75381720066070557 -0.99969089031219482 
		-0.99678176641464233;
	setAttr -s 10 ".kox[7:9]"  0.65708482265472412 0.024862872436642647 
		0.080163337290287018;
	setAttr -s 10 ".koy[7:9]"  -0.75381666421890259 -0.99969089031219482 
		-0.99678176641464233;
createNode animCurveTU -n "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1_raiseToeTip";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  1 0 4 0 9 0 12 0 13 0 14 0 15 11 18 57.285331726074219 
		21 22.720683761674707 22 8.6745119094848633 24 1.389858 25 0;
	setAttr -s 12 ".kit[8:11]"  1 10 1 10;
	setAttr -s 12 ".kot[8:11]"  1 10 1 10;
	setAttr -s 12 ".kix[8:11]"  0.0026313571725040674 0.0058599631302058697 
		0.015098054893314838 0.029965590685606003;
	setAttr -s 12 ".kiy[8:11]"  -0.99999654293060303 -0.99998283386230469 
		-0.99988609552383423 -0.99955093860626221;
	setAttr -s 12 ".kox[8:11]"  0.0026313567068427801 0.0058599631302058697 
		0.015098054893314838 0.029965590685606003;
	setAttr -s 12 ".koy[8:11]"  -0.99999654293060303 -0.99998283386230469 
		-0.99988609552383423 -0.99955093860626221;
createNode animCurveTU -n "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1_side";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  1 0 4 0 9 0 12 0 13 0 15 0 25 0;
createNode animCurveTU -n "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1_swivel";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  1 0 4 0 9 0 12 0 13 0 15 0 25 0;
createNode animCurveTU -n "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1_roll";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  1 0 4 0 9 0 12 0 13 0 15 0 25 0;
createNode animCurveTU -n "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1_raiseToe";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  1 15 2 13.7 3 0 4 0 9 0 12 0 13 0 15 0 
		21 -28.912756 25 15;
	setAttr -s 10 ".kit[0:9]"  3 1 10 10 10 10 10 10 
		10 3;
	setAttr -s 10 ".kot[0:9]"  3 1 10 10 10 10 10 10 
		10 3;
	setAttr -s 10 ".kix[1:9]"  0.012612732127308846 1 1 1 1 1 1 0.027767064049839973 
		1;
	setAttr -s 10 ".kiy[1:9]"  -0.9999205470085144 0 0 0 0 0 0 0.999614417552948 
		0;
	setAttr -s 10 ".kox[1:9]"  0.012612732127308846 1 1 1 1 1 1 0.027767064049839973 
		1;
	setAttr -s 10 ".koy[1:9]"  -0.9999205470085144 0 0 0 0 0 0 0.999614417552948 
		0;
createNode animCurveTU -n "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1_swivelToe";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  1 0 4 0 9 0 12 0 13 0 15 0 25 0;
createNode animCurveTU -n "cp_c009001daipa:RtLeg_Leg_IK_outPutAnimBank_1_twistToe";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  1 0 4 0 9 0 12 0 13 0 15 0 25 0;
createNode animCurveTL -n "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 -0.60480295879481916 8 -0.39075627754318687 
		13 -0.60480295879481916 16 -0.60480295879481916 18 -0.60480295879481916 25 -0.60480295879481916;
	setAttr -s 6 ".kit[0:5]"  3 1 10 10 10 3;
	setAttr -s 6 ".kot[0:5]"  3 1 10 10 10 3;
	setAttr -s 6 ".kix[1:5]"  0.99891418218612671 1 1 1 1;
	setAttr -s 6 ".kiy[1:5]"  0.046588070690631866 0 0 0 0;
	setAttr -s 6 ".kox[1:5]"  0.99891418218612671 1 1 1 1;
	setAttr -s 6 ".koy[1:5]"  0.046587835997343063 0 0 0 0;
createNode animCurveTL -n "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 0 9 0.29534422254613379 13 0.077228574213538501 
		16 0 18 0 25 0;
	setAttr -s 6 ".kit[0:5]"  3 10 10 10 10 3;
	setAttr -s 6 ".kot[0:5]"  3 10 10 10 10 3;
createNode animCurveTL -n "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1_translateZ";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 -2.1301800401197473 9 1.6638899302027919 
		14 7.5698199598802525 16 7.5698199598802525 18 7.5698199598802525 25 7.5698199598802525;
	setAttr -s 6 ".kit[1:5]"  1 3 10 10 3;
	setAttr -s 6 ".kot[1:5]"  1 3 10 10 3;
	setAttr -s 6 ".kix[1:5]"  0.028906360268592834 1 1 1 1;
	setAttr -s 6 ".kiy[1:5]"  0.99958211183547974 0 0 0 0;
	setAttr -s 6 ".kox[1:5]"  0.028906345367431641 1 1 1 1;
	setAttr -s 6 ".koy[1:5]"  0.99958211183547974 0 0 0 0;
createNode animCurveTA -n "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1_rotateX";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  1 0 5 -0.055362500000000002 9 -2.585784 
		11 -8.5470468002282445 12 -11.630788791838333 13 -14.148888423608492 14 -11.007978636882383 
		16 0 18 0 25 0;
	setAttr -s 10 ".kit[0:9]"  3 1 1 10 1 1 1 10 
		10 3;
	setAttr -s 10 ".kot[0:9]"  3 1 1 10 1 1 1 10 
		10 3;
	setAttr -s 10 ".kix[1:9]"  0.99991661310195923 0.77315908670425415 
		0.62077456712722778 0.33335012197494507 0.99468314647674561 0.36832395195960999 1 
		1 1;
	setAttr -s 10 ".kiy[1:9]"  -0.012916495092213154 -0.63421213626861572 
		-0.78398913145065308 -0.94280308485031128 0.10298321396112442 0.92969751358032227 
		0 0 0;
	setAttr -s 10 ".kox[1:9]"  0.99991661310195923 0.77315908670425415 
		0.62077456712722778 0.33335012197494507 0.99468314647674561 0.36832395195960999 1 
		1 1;
	setAttr -s 10 ".koy[1:9]"  -0.012916496023535728 -0.63421213626861572 
		-0.78398913145065308 -0.94280308485031128 0.10298307240009308 0.92969751358032227 
		0 0 0;
createNode animCurveTA -n "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  1 9.8511458277978043 5 7.7666968022120795 
		9 6.2446004241854043 13 9.8511458277978043 16 9.8511458277978043 18 9.8511458277978043 
		25 9.8511458277978043;
	setAttr -s 7 ".kit[0:6]"  3 1 10 10 10 10 3;
	setAttr -s 7 ".kot[0:6]"  3 1 10 10 10 10 3;
	setAttr -s 7 ".kix[1:6]"  0.97736090421676636 1 1 1 1 1;
	setAttr -s 7 ".kiy[1:6]"  -0.21157903969287872 0 0 0 0 0;
	setAttr -s 7 ".kox[1:6]"  0.97736090421676636 1 1 1 1 1;
	setAttr -s 7 ".koy[1:6]"  -0.21157892048358917 0 0 0 0 0;
createNode animCurveTA -n "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  1 0 5 11.547488160942589 9 6.7239315074784445 
		13 0 16 0 18 0 25 0;
	setAttr -s 7 ".kit[0:6]"  3 10 1 10 10 10 3;
	setAttr -s 7 ".kot[0:6]"  3 10 1 10 10 10 3;
	setAttr -s 7 ".kix[2:6]"  0.73046433925628662 1 1 1 1;
	setAttr -s 7 ".kiy[2:6]"  -0.68295091390609741 0 0 0 0;
	setAttr -s 7 ".kox[2:6]"  0.73046433925628662 1 1 1 1;
	setAttr -s 7 ".koy[2:6]"  -0.68295091390609741 0 0 0 0;
createNode animCurveTU -n "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1_raiseBall";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  1 20.171655654907227 3 25.158077 9 5.910229 
		13 0 16 0 18 0 22 0 25 20.171655654907227;
	setAttr -s 8 ".kit[0:7]"  1 1 10 10 10 10 10 1;
	setAttr -s 8 ".kot[0:7]"  1 1 10 10 10 10 10 1;
	setAttr -s 8 ".kix[0:7]"  0.0076724337413907051 0.16250231862068176 
		0.016559673473238945 1 1 1 1 0.0076724337413907051;
	setAttr -s 8 ".kiy[0:7]"  0.99997055530548096 -0.98670822381973267 
		-0.99986284971237183 0 0 0 0 0.99997055530548096;
	setAttr -s 8 ".kox[0:7]"  0.0076724393293261528 0.16250233352184296 
		0.016559673473238945 1 1 1 1 0.0076724393293261528;
	setAttr -s 8 ".koy[0:7]"  0.99997055530548096 -0.98670822381973267 
		-0.99986284971237183 0 0 0 0 0.99997055530548096;
createNode animCurveTU -n "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1_raiseToeTip";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 11 ".ktv[0:10]"  1 0 3 20.73341 5 56.331230163574219 9 31.303431 
		11 13.200937 12 1.349935 13 -1.2328490018844604 14 -0.434091 16 0 18 0 25 0;
	setAttr -s 11 ".kit[0:10]"  3 10 10 1 10 1 10 10 
		10 10 3;
	setAttr -s 11 ".kot[0:10]"  3 10 10 1 10 1 10 10 
		10 10 3;
	setAttr -s 11 ".kix[3:10]"  0.0051343878731131554 0.0041730990633368492 
		0.0069805430248379707 0.046659942716360092 0.10087399184703827 1 1 1;
	setAttr -s 11 ".kiy[3:10]"  -0.99998682737350464 -0.99999129772186279 
		-0.99997562170028687 -0.99891084432601929 0.9948992133140564 0 0 0;
	setAttr -s 11 ".kox[3:10]"  0.0051343883387744427 0.0041730990633368492 
		0.0069805430248379707 0.046659942716360092 0.10087399184703827 1 1 1;
	setAttr -s 11 ".koy[3:10]"  -0.99998682737350464 -0.99999129772186279 
		-0.99997562170028687 -0.99891084432601929 0.9948992133140564 0 0 0;
createNode animCurveTU -n "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1_side";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 13 0 16 0 18 0 25 0;
	setAttr -s 5 ".kit[0:4]"  3 10 10 10 3;
	setAttr -s 5 ".kot[0:4]"  3 10 10 10 3;
createNode animCurveTU -n "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1_swivel";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 13 0 16 0 18 0 25 0;
	setAttr -s 5 ".kit[0:4]"  3 10 10 10 3;
	setAttr -s 5 ".kot[0:4]"  3 10 10 10 3;
createNode animCurveTU -n "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1_roll";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 13 0 16 0 18 0 25 0;
	setAttr -s 5 ".kit[0:4]"  3 10 10 10 3;
	setAttr -s 5 ".kot[0:4]"  3 10 10 10 3;
createNode animCurveTU -n "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1_raiseToe";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  1 0 9 -29.299999 13 13.1 14 13.420826 15 
		13.918753 16 0 18 0 25 0;
	setAttr -s 8 ".kit[0:7]"  3 10 1 10 1 10 10 3;
	setAttr -s 8 ".kot[0:7]"  3 10 1 10 1 10 10 3;
	setAttr -s 8 ".kix[2:7]"  0.28085789084434509 0.10125764459371567 
		0.22977440059185028 1 1 1;
	setAttr -s 8 ".kiy[2:7]"  0.95974934101104736 0.99486023187637329 
		0.97324395179748535 0 0 0;
	setAttr -s 8 ".kox[2:7]"  0.28085753321647644 0.10125764459371567 
		0.2297738790512085 1 1 1;
	setAttr -s 8 ".koy[2:7]"  0.95974946022033691 0.99486023187637329 
		0.9732440710067749 0 0 0;
createNode animCurveTU -n "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1_swivelToe";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 13 0 16 0 18 0 25 0;
	setAttr -s 5 ".kit[0:4]"  3 10 10 10 3;
	setAttr -s 5 ".kot[0:4]"  3 10 10 10 3;
createNode animCurveTU -n "cp_c009001daipa:LfLeg_Leg_IK_outPutAnimBank_1_twistToe";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 13 0 16 0 18 0 25 0;
	setAttr -s 5 ".kit[0:4]"  3 10 10 10 3;
	setAttr -s 5 ".kot[0:4]"  3 10 10 10 3;
createNode animCurveTA -n "cp_c009001daipa:LfArm_Wrist_FK_outPutAnimBank_1_rotateX";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 -0.92079113933703249 5 -7.3094415504118002 
		16 17.3324960641853 25 -0.92078975216160608;
	setAttr -s 4 ".kit[1:3]"  3 1 1;
	setAttr -s 4 ".kot[1:3]"  3 1 1;
	setAttr -s 4 ".kix[0:3]"  0.64158296585083008 1 0.99940156936645508 
		0.64158296585083008;
	setAttr -s 4 ".kiy[0:3]"  -0.76705366373062134 0 0.034591197967529297 
		-0.76705366373062134;
	setAttr -s 4 ".kox[0:3]"  0.69399195909500122 1 0.99940156936645508 
		0.69399195909500122;
	setAttr -s 4 ".koy[0:3]"  -0.71998274326324463 0 0.034591212868690491 
		-0.71998274326324463;
createNode animCurveTA -n "cp_c009001daipa:LfArm_Wrist_FK_outPutAnimBank_1_rotateY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 14.717676576835791 5 -2.6624366980571104 
		12 -23.331545644384516 16 -3.0371743606059498 23 19.654613704588368 25 14.717676576835791;
	setAttr -s 6 ".kit[2:5]"  9 1 1 1;
	setAttr -s 6 ".kot[2:5]"  9 1 1 1;
	setAttr -s 6 ".kix[0:5]"  0.53404879570007324 0.46165788173675537 
		0.99989819526672363 0.3950122594833374 0.99445033073425293 0.53404879570007324;
	setAttr -s 6 ".kiy[0:5]"  -0.84545361995697021 -0.8870580792427063 
		-0.014268523082137108 0.91867589950561523 0.1052078977227211 -0.84545361995697021;
	setAttr -s 6 ".kox[0:5]"  0.53052675724029541 0.46165776252746582 
		0.99989819526672363 0.39501217007637024 0.99445033073425293 0.53052675724029541;
	setAttr -s 6 ".koy[0:5]"  -0.8476681113243103 -0.88705801963806152 
		-0.014268523082137108 0.91867589950561523 0.10520788282155991 -0.8476681113243103;
createNode animCurveTA -n "cp_c009001daipa:LfArm_Wrist_FK_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 38 5 27.579259724523922 11 -5.3017017040695373 
		22 33.778102374596784 25 38;
	setAttr -s 5 ".kit[2:4]"  10 1 1;
	setAttr -s 5 ".kot[2:4]"  10 1 1;
	setAttr -s 5 ".kix[0:4]"  0.99090629816055298 0.46090766787528992 
		0.98853558301925659 0.53562718629837036 0.99090629816055298;
	setAttr -s 5 ".kiy[0:4]"  0.13455362617969513 -0.8874480128288269 
		0.15098805725574493 0.84445452690124512 0.13455362617969513;
	setAttr -s 5 ".kox[0:4]"  0.99992239475250244 0.46090728044509888 
		0.98853558301925659 0.53562712669372559 0.99992239475250244;
	setAttr -s 5 ".koy[0:4]"  0.012460178695619106 -0.88744831085205078 
		0.15098805725574493 0.84445458650588989 0.012460178695619106;
createNode animCurveTA -n "cp_c009001daipa:LfArm_Elbow_FK_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 4 0 25 0;
	setAttr -s 3 ".kit[1:2]"  9 10;
	setAttr -s 3 ".kot[1:2]"  9 10;
createNode animCurveTA -n "cp_c009001daipa:LfArm_Elbow_FK_outPutAnimBank_1_rotateY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -14 3 -22.358031329651769 9 -32.845966631140506 
		21 -2.9263056797088511 25 -14;
	setAttr -s 5 ".kix[0:4]"  0.46501266956329346 0.59851807355880737 
		0.99979043006896973 0.95516777038574219 0.46501266956329346;
	setAttr -s 5 ".kiy[0:4]"  -0.88530397415161133 -0.80110925436019897 
		-0.0204743891954422 0.29606515169143677 -0.88530397415161133;
	setAttr -s 5 ".kox[0:4]"  0.46882537007331848 0.59851807355880737 
		0.99979043006896973 0.95516777038574219 0.46882537007331848;
	setAttr -s 5 ".koy[0:4]"  -0.88329088687896729 -0.80110925436019897 
		-0.020474376156926155 0.29606515169143677 -0.88329088687896729;
createNode animCurveTA -n "cp_c009001daipa:LfArm_Elbow_FK_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 4 0 25 0;
	setAttr -s 3 ".kit[1:2]"  9 10;
	setAttr -s 3 ".kot[1:2]"  9 10;
createNode animCurveTA -n "cp_c009001daipa:LfArm_UpArm_FK_outPutAnimBank_1_rotateX";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -12.846065129088899 2 -10.572667439064411 
		8 -5.3312992075786454 17 -29.155682380028882 25 -12.845624612359032;
	setAttr -s 5 ".kit[3:4]"  3 1;
	setAttr -s 5 ".kot[3:4]"  3 1;
	setAttr -s 5 ".kix[0:4]"  0.74254631996154785 0.81619119644165039 
		0.9900134801864624 1 0.74254631996154785;
	setAttr -s 5 ".kiy[0:4]"  0.66979467868804932 0.57778185606002808 
		-0.14097234606742859 0 0.66979467868804932;
	setAttr -s 5 ".kox[0:4]"  0.74614560604095459 0.81619149446487427 
		0.9900134801864624 1 0.74614560604095459;
	setAttr -s 5 ".koy[0:4]"  0.66578274965286255 0.5777815580368042 
		-0.1409723311662674 0 0.66578274965286255;
createNode animCurveTA -n "cp_c009001daipa:LfArm_UpArm_FK_outPutAnimBank_1_rotateY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 -5.1052987726970791 2 -6.1472007867700258 
		14 10.265006240684231 25 -5.1052987726970791;
	setAttr -s 4 ".kix[0:3]"  0.90047627687454224 0.96277397871017456 
		0.91095209121704102 0.90047627687454224;
	setAttr -s 4 ".kiy[0:3]"  -0.43490520119667053 -0.27030757069587708 
		0.41251218318939209 -0.43490520119667053;
	setAttr -s 4 ".kox[0:3]"  0.90047609806060791 0.96277397871017456 
		0.91095209121704102 0.90047609806060791;
	setAttr -s 4 ".koy[0:3]"  -0.43490549921989441 -0.27030757069587708 
		0.41251218318939209 -0.43490549921989441;
createNode animCurveTA -n "cp_c009001daipa:LfArm_UpArm_FK_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 -52.064001185994144 2 -51.219823180427724 
		8 -59.948220328472622 15 -51.443957584558802 21 -59.368266588873936 25 -52.064002050171894;
	setAttr -s 6 ".kit[0:5]"  1 3 10 3 10 1;
	setAttr -s 6 ".kot[0:5]"  1 3 10 3 10 1;
	setAttr -s 6 ".kix[0:5]"  0.85801386833190918 1 0.99997389316558838 
		1 0.99966287612915039 0.85801386833190918;
	setAttr -s 6 ".kiy[0:5]"  0.51362651586532593 0 -0.0072217495180666447 
		0 -0.025963608175516129 0.51362651586532593;
	setAttr -s 6 ".kox[0:5]"  0.8663601279258728 1 0.99997389316558838 
		1 0.99966287612915039 0.8663601279258728;
	setAttr -s 6 ".koy[0:5]"  0.49941983819007874 0 -0.0072217495180666447 
		0 -0.025963608175516129 0.49941983819007874;
createNode animCurveTU -n "cp_c009001daipa:LfArm_UpArm_FK_outPutAnimBank_1_twistPlacement";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 25 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "cp_c009001daipa:LfArm_UpArm_FK_outPutAnimBank_1_addTwist";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0.37907823920249939 2 0.37907824663027245 
		25 0.37907823920249939;
	setAttr -s 3 ".kit[1:2]"  3 10;
	setAttr -s 3 ".kot[1:2]"  3 10;
createNode animCurveTL -n "cp_c009001daipa:Lf_shoulder_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 4 0 25 0;
	setAttr -s 3 ".kit[1:2]"  3 10;
	setAttr -s 3 ".kot[1:2]"  3 10;
createNode animCurveTL -n "cp_c009001daipa:Lf_shoulder_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 4 0 25 0;
	setAttr -s 3 ".kit[1:2]"  3 10;
	setAttr -s 3 ".kot[1:2]"  3 10;
createNode animCurveTL -n "cp_c009001daipa:Lf_shoulder_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 4 0 25 0;
	setAttr -s 3 ".kit[1:2]"  3 10;
	setAttr -s 3 ".kot[1:2]"  3 10;
createNode animCurveTA -n "cp_c009001daipa:Lf_shoulder_outPutAnimBank_1_rotateX";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 0.64759533115873091 4 0.98891577448112422 
		16 -0.88062116889334618 25 0.64759511908499223;
	setAttr -s 4 ".kit[0:3]"  1 3 3 1;
	setAttr -s 4 ".kot[0:3]"  1 3 3 1;
	setAttr -s 4 ".kix[0:3]"  0.99802243709564209 1 1 0.99802243709564209;
	setAttr -s 4 ".kiy[0:3]"  0.062858276069164276 0 0 0.062858276069164276;
	setAttr -s 4 ".kox[0:3]"  0.99804174900054932 1 1 0.99804174900054932;
	setAttr -s 4 ".koy[0:3]"  0.062551960349082947 0 0 0.062551960349082947;
createNode animCurveTA -n "cp_c009001daipa:Lf_shoulder_outPutAnimBank_1_rotateY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -5.1444302117345737 4 -6.406971086021481 
		13 9.6753065910106564 16 10.761939887198317 25 -5.1444302117345737;
	setAttr -s 5 ".kit[1:4]"  3 1 3 1;
	setAttr -s 5 ".kot[1:4]"  3 1 3 1;
	setAttr -s 5 ".kix[0:4]"  0.96385759115219116 1 0.96108430624008179 
		1 0.96385759115219116;
	setAttr -s 5 ".kiy[0:4]"  -0.26641800999641418 0 0.27625519037246704 
		0 -0.26641800999641418;
	setAttr -s 5 ".kox[0:4]"  0.96385759115219116 1 0.96108430624008179 
		1 0.96385759115219116;
	setAttr -s 5 ".koy[0:4]"  -0.26641803979873657 0 0.27625519037246704 
		0 -0.26641803979873657;
createNode animCurveTA -n "cp_c009001daipa:Lf_shoulder_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 -3.5503006237104544 4 -2.458828550557334 
		16 -8.4372204205511494 25 -3.5503013018783403;
	setAttr -s 4 ".kit[0:3]"  1 3 3 1;
	setAttr -s 4 ".kot[0:3]"  1 3 3 1;
	setAttr -s 4 ".kix[0:3]"  0.9725225567817688 1 1 0.9725225567817688;
	setAttr -s 4 ".kiy[0:3]"  0.2328086793422699 0 0 0.2328086793422699;
	setAttr -s 4 ".kox[0:3]"  0.97379684448242188 1 1 0.97379684448242188;
	setAttr -s 4 ".koy[0:3]"  0.22741988301277161 0 0 0.22741988301277161;
createNode animCurveTU -n "cp_c009001daipa:Lf_shoulder_outPutAnimBank_1_Arm_follow";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 1 4 1 25 1;
	setAttr -s 3 ".kit[0:2]"  9 3 9;
	setAttr -s 3 ".kot[0:2]"  5 3 5;
createNode animCurveTL -n "cp_c009001daipa:Rt_shoulder_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 4 0 25 0;
	setAttr -s 3 ".kit[1:2]"  3 10;
	setAttr -s 3 ".kot[1:2]"  3 10;
createNode animCurveTL -n "cp_c009001daipa:Rt_shoulder_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 4 0 25 0;
	setAttr -s 3 ".kit[1:2]"  3 10;
	setAttr -s 3 ".kot[1:2]"  3 10;
createNode animCurveTL -n "cp_c009001daipa:Rt_shoulder_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 4 0 25 0;
	setAttr -s 3 ".kit[1:2]"  3 10;
	setAttr -s 3 ".kot[1:2]"  3 10;
createNode animCurveTA -n "cp_c009001daipa:Rt_shoulder_outPutAnimBank_1_rotateX";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 0.30690755306150913 4 -0.096912439440895823 
		17 1.7726245043826832 25 0.30690784370130497;
	setAttr -s 4 ".kit[0:3]"  1 3 3 1;
	setAttr -s 4 ".kot[0:3]"  1 3 3 1;
	setAttr -s 4 ".kix[0:3]"  0.99567621946334839 1 1 0.99567621946334839;
	setAttr -s 4 ".kiy[0:3]"  -0.092891469597816467 0 0 -0.092891469597816467;
	setAttr -s 4 ".kox[0:3]"  0.99591422080993652 1 1 0.99591422080993652;
	setAttr -s 4 ".koy[0:3]"  -0.090305313467979431 0 0 -0.090305313467979431;
createNode animCurveTA -n "cp_c009001daipa:Rt_shoulder_outPutAnimBank_1_rotateY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 7.115 4 10.965634048743475 17 -7.2057982577637167 
		25 7.115;
	setAttr -s 4 ".kit[1:3]"  3 1 1;
	setAttr -s 4 ".kot[1:3]"  3 1 1;
	setAttr -s 4 ".kix[0:3]"  0.74345630407333374 1 0.99897986650466919 
		0.74345630407333374;
	setAttr -s 4 ".kiy[0:3]"  0.66878437995910645 0 0.045158263295888901 
		0.66878437995910645;
	setAttr -s 4 ".kox[0:3]"  0.76664555072784424 1 0.99897986650466919 
		0.76664555072784424;
	setAttr -s 4 ".koy[0:3]"  0.64207059144973755 0 0.045158263295888901 
		0.64207059144973755;
createNode animCurveTA -n "cp_c009001daipa:Rt_shoulder_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 -6.7701863668456106 4 -8.0615190512276058 
		17 -2.0831271809820073 25 -6.7701854374397508;
	setAttr -s 4 ".kit[0:3]"  1 3 3 1;
	setAttr -s 4 ".kot[0:3]"  1 3 3 1;
	setAttr -s 4 ".kix[0:3]"  0.94653159379959106 1 1 0.94653159379959106;
	setAttr -s 4 ".kiy[0:3]"  -0.3226112425327301 0 0 -0.3226112425327301;
	setAttr -s 4 ".kox[0:3]"  0.96810925006866455 1 1 0.96810925006866455;
	setAttr -s 4 ".koy[0:3]"  -0.25052854418754578 0 0 -0.25052854418754578;
createNode animCurveTU -n "cp_c009001daipa:Rt_shoulder_outPutAnimBank_1_Arm_follow";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 1 4 1 25 1;
	setAttr -s 3 ".kit[0:2]"  9 3 9;
	setAttr -s 3 ".kot[0:2]"  5 3 5;
createNode animCurveTA -n "cp_c009001daipa:RtArm_UpArm_FK_outPutAnimBank_1_rotateX";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 -35.003 2 -36.469593677620558 17 -19.240479788514151 
		25 -35.003;
	setAttr -s 4 ".kit[2:3]"  10 1;
	setAttr -s 4 ".kot[2:3]"  10 1;
	setAttr -s 4 ".kix[0:3]"  0.73388367891311646 0.96574801206588745 
		0.99964344501495361 0.73388367891311646;
	setAttr -s 4 ".kiy[0:3]"  -0.67927515506744385 -0.25948134064674377 
		0.026700273156166077 -0.67927515506744385;
	setAttr -s 4 ".kox[0:3]"  0.79853415489196777 0.96574801206588745 
		0.99964344501495361 0.79853415489196777;
	setAttr -s 4 ".koy[0:3]"  -0.60194945335388184 -0.25948134064674377 
		0.026700273156166077 -0.60194945335388184;
createNode animCurveTA -n "cp_c009001daipa:RtArm_UpArm_FK_outPutAnimBank_1_rotateY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 8.0947023389243959 2 9.3162354787649342 
		15 -6.2292644832197448 25 8.0947023389243959;
	setAttr -s 4 ".kix[0:3]"  0.8337891697883606 0.958351731300354 0.98403865098953247 
		0.8337891697883606;
	setAttr -s 4 ".kiy[0:3]"  0.55208295583724976 0.28559067845344543 
		-0.17795470356941223 0.55208295583724976;
	setAttr -s 4 ".kox[0:3]"  0.86835247278213501 0.958351731300354 0.98403865098953247 
		0.86835247278213501;
	setAttr -s 4 ".koy[0:3]"  0.49594756960868835 0.28559067845344543 
		-0.17795470356941223 0.49594756960868835;
createNode animCurveTA -n "cp_c009001daipa:RtArm_UpArm_FK_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  1 -53.759951777225282 3 -51.845884727179346 
		5 -54.454865809368755 9 -59.925980860411933 15 -51.760978808220273 21 -59.744506115329649 
		25 -53.759951777225282;
	setAttr -s 7 ".kit[1:6]"  3 1 10 3 1 1;
	setAttr -s 7 ".kot[1:6]"  3 1 10 3 1 1;
	setAttr -s 7 ".kix[0:6]"  0.84315216541290283 1 0.77810454368591309 
		0.99369353055953979 1 0.99999183416366577 0.84315216541290283;
	setAttr -s 7 ".kiy[0:6]"  0.53767502307891846 0 -0.62813478708267212 
		0.11212964355945587 0 -0.0040395902469754219 0.53767502307891846;
	setAttr -s 7 ".kox[0:6]"  0.84528505802154541 1 0.77810454368591309 
		0.99369353055953979 1 0.99999183416366577 0.84528505802154541;
	setAttr -s 7 ".koy[0:6]"  0.53431564569473267 0 -0.62813478708267212 
		0.11212964355945587 0 -0.0040395869873464108 0.53431564569473267;
createNode animCurveTU -n "cp_c009001daipa:RtArm_UpArm_FK_outPutAnimBank_1_twistPlacement";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 25 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "cp_c009001daipa:RtArm_UpArm_FK_outPutAnimBank_1_addTwist";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0.37907823920249939 2 0.37907824663027245 
		25 0.37907823920249939;
	setAttr -s 3 ".kit[1:2]"  3 10;
	setAttr -s 3 ".kot[1:2]"  3 10;
createNode animCurveTA -n "cp_c009001daipa:RtArm_Elbow_FK_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 3 0 25 0;
	setAttr -s 3 ".kit[1:2]"  9 10;
	setAttr -s 3 ".kot[1:2]"  9 10;
createNode animCurveTA -n "cp_c009001daipa:RtArm_Elbow_FK_outPutAnimBank_1_rotateY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -28 3 -19.744150798613504 9 -7.390625499344857 
		21 -39.076732813772239 25 -28;
	setAttr -s 5 ".kix[0:4]"  0.48386475443840027 0.52079898118972778 
		0.99975681304931641 0.99762219190597534 0.48386475443840027;
	setAttr -s 5 ".kiy[0:4]"  0.87514281272888184 0.85367929935455322 
		-0.022055201232433319 0.068919748067855835 0.87514281272888184;
	setAttr -s 5 ".kox[0:4]"  0.48386475443840027 0.52079898118972778 
		0.99975681304931641 0.99762219190597534 0.48386475443840027;
	setAttr -s 5 ".koy[0:4]"  0.87514275312423706 0.85367929935455322 
		-0.022055182605981827 0.068919748067855835 0.87514275312423706;
createNode animCurveTA -n "cp_c009001daipa:RtArm_Elbow_FK_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 3 0 25 0;
	setAttr -s 3 ".kit[1:2]"  9 10;
	setAttr -s 3 ".kot[1:2]"  9 10;
createNode animCurveTA -n "cp_c009001daipa:RtArm_Wrist_FK_outPutAnimBank_1_rotateX";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 17.775 5 27.434186164795623 16 -0.3315685968585636 
		23 11.11022480771498 25 17.775;
	setAttr -s 5 ".kit[1:4]"  3 1 1 1;
	setAttr -s 5 ".kot[1:4]"  3 1 1 1;
	setAttr -s 5 ".kix[0:4]"  0.63344711065292358 1 0.99870765209197998 
		0.69267123937606812 0.63344711065292358;
	setAttr -s 5 ".kiy[0:4]"  0.77378606796264648 0 -0.05082300677895546 
		0.72125333547592163 0.77378606796264648;
	setAttr -s 5 ".kox[0:4]"  0.63611263036727905 1 0.99870765209197998 
		0.69267117977142334 0.63611263036727905;
	setAttr -s 5 ".koy[0:4]"  0.77159619331359863 0 -0.050823036581277847 
		0.72125357389450073 0.77159619331359863;
createNode animCurveTA -n "cp_c009001daipa:RtArm_Wrist_FK_outPutAnimBank_1_rotateY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 -14.600000000000001 5 5.4693924426320848 
		12 28.997245562836873 16 4.6099121887426868 23 -17.910780462932873 25 -14.600000000000001;
	setAttr -s 6 ".kix[0:5]"  0.68628448247909546 0.37516441941261292 
		0.99995720386505127 0.46565747261047363 0.99987614154815674 0.68628448247909546;
	setAttr -s 6 ".kiy[0:5]"  0.7273331880569458 0.92695826292037964 
		0.0092555014416575432 -0.88496506214141846 -0.015733366832137108 0.7273331880569458;
	setAttr -s 6 ".kox[0:5]"  0.68263936042785645 0.3751644492149353 
		0.99995720386505127 0.46565732359886169 0.99987614154815674 0.68263936042785645;
	setAttr -s 6 ".koy[0:5]"  0.73075544834136963 0.92695826292037964 
		0.009255467914044857 -0.88496512174606323 -0.015733344480395317 0.73075544834136963;
createNode animCurveTA -n "cp_c009001daipa:RtArm_Wrist_FK_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 13.5 5 37.348296452005719 16 13.890225312839945 
		23 2.7944513982284227 25 13.5;
	setAttr -s 5 ".kit[1:4]"  3 1 1 1;
	setAttr -s 5 ".kot[1:4]"  3 1 1 1;
	setAttr -s 5 ".kix[0:4]"  0.31080198287963867 1 0.69125646352767944 
		0.78743571043014526 0.31080198287963867;
	setAttr -s 5 ".kiy[0:4]"  0.95047473907470703 0 -0.72260957956314087 
		0.61639690399169922 0.95047473907470703;
	setAttr -s 5 ".kox[0:4]"  0.32105171680450439 1 0.69125640392303467 
		0.78743588924407959 0.32105171680450439;
	setAttr -s 5 ".koy[0:4]"  0.94706171751022339 0 -0.72260957956314087 
		0.61639660596847534 0.94706171751022339;
createNode animCurveTL -n "cp_c009001daipa:head_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 25 0;
createNode animCurveTL -n "cp_c009001daipa:head_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 25 0;
createNode animCurveTL -n "cp_c009001daipa:head_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 25 0;
createNode animCurveTA -n "cp_c009001daipa:head_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 -8.5639945767167021 4 -9.2858277154284501 
		10 -7.23516529953781 16 -9.2858277154284501 22 -7.23516529953781 25 -8.5639947140043322;
	setAttr -s 6 ".kit[0:5]"  1 10 1 10 10 1;
	setAttr -s 6 ".kot[0:5]"  1 10 1 10 10 1;
	setAttr -s 6 ".kix[0:5]"  0.98504745960235596 1 0.9999958872795105 
		1 1 0.97633439302444458;
	setAttr -s 6 ".kiy[0:5]"  -0.17228309810161591 0 0.0028456512372940779 
		0 0 -0.21626642346382141;
	setAttr -s 6 ".kox[0:5]"  0.98633641004562378 1 0.9999958872795105 
		1 1 0.97793269157409668;
	setAttr -s 6 ".koy[0:5]"  -0.16474390029907227 0 0.0028456512372940779 
		0 0 -0.20892024040222168;
createNode animCurveTA -n "cp_c009001daipa:head_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 25 0;
createNode animCurveTA -n "cp_c009001daipa:head_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 25 0;
createNode animCurveTU -n "cp_c009001daipa:head_ctrl_outPutAnimBank_1_rotation";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 25 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "cp_c009001daipa:head_ctrl_outPutAnimBank_1_DYNHatPrimaryCtrl";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 25 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "cp_c009001daipa:head_ctrl_outPutAnimBank_1_DYNHatStartFrame";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 20000 25 20000;
createNode animCurveTU -n "cp_c009001daipa:head_ctrl_outPutAnimBank_1_DYNEaringPrimaryCtrl";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 25 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "cp_c009001daipa:head_ctrl_outPutAnimBank_1_DYNEaringStartFrame";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 20000 25 20000;
createNode animCurveTU -n "cp_c009001daipa:head_ctrl_outPutAnimBank_1_DYNNecklacePrimaryCtrl";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 25 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "cp_c009001daipa:head_ctrl_outPutAnimBank_1_DYNNecklaceStartFrame";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 20000 25 20000;
createNode animCurveTL -n "cp_c009001daipa:waist_FK1_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 25 0;
createNode animCurveTL -n "cp_c009001daipa:waist_FK1_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 25 0;
createNode animCurveTL -n "cp_c009001daipa:waist_FK1_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 25 0;
createNode animCurveTA -n "cp_c009001daipa:waist_FK1_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 2.3848426486149901 5 3.2665633096146469 
		11 2.1253240849662816 17 3.2630721834119671 23 2.1700233136275835 25 2.3923882659438176;
	setAttr -s 6 ".kit[0:5]"  1 10 10 10 10 1;
	setAttr -s 6 ".kot[0:5]"  1 10 10 10 10 1;
	setAttr -s 6 ".kix[0:5]"  0.99630147218704224 1 1 1 1 0.99630147218704224;
	setAttr -s 6 ".kiy[0:5]"  0.085926614701747894 0 0 0 0 0.085926614701747894;
	setAttr -s 6 ".kox[0:5]"  0.99628943204879761 1 1 1 1 0.99628943204879761;
	setAttr -s 6 ".koy[0:5]"  0.086066141724586487 0 0 0 0 0.086066141724586487;
createNode animCurveTA -n "cp_c009001daipa:waist_FK1_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 -6.6739293610200408 2 -7 14 7 25 -6.6739290481169373;
	setAttr -s 4 ".kit[2:3]"  3 1;
	setAttr -s 4 ".kot[2:3]"  3 1;
	setAttr -s 4 ".kix[0:3]"  0.97237521409988403 0.99999392032623291 
		1 0.97237521409988403;
	setAttr -s 4 ".kiy[0:3]"  -0.23342336714267731 -0.0034666541032493114 
		0 -0.23342336714267731;
	setAttr -s 4 ".kox[0:3]"  0.97360503673553467 0.99999392032623291 
		1 0.97360503673553467;
	setAttr -s 4 ".koy[0:3]"  -0.22823973000049591 -0.0034666601568460464 
		0 -0.22823973000049591;
createNode animCurveTA -n "cp_c009001daipa:waist_FK1_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -1.9072479049893101 9 4 16 0 22 -3.0647734425094244 
		25 -1.907248584331759;
	setAttr -s 5 ".kix[0:4]"  0.93748623132705688 0.99837982654571533 
		0.92243051528930664 0.99913865327835083 0.93748623132705688;
	setAttr -s 5 ".kiy[0:4]"  0.34802219271659851 0.056900776922702789 
		-0.38616293668746948 -0.041497059166431427 0.34802219271659851;
	setAttr -s 5 ".kox[0:4]"  0.93824881315231323 0.99837982654571533 
		0.92243051528930664 0.99913865327835083 0.93824881315231323;
	setAttr -s 5 ".koy[0:4]"  0.34596133232116699 0.056900862604379654 
		-0.3861631453037262 -0.041497081518173218 0.34596133232116699;
createNode animCurveTL -n "cp_c009001daipa:waist_FK2_ctrl_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 25 0;
createNode animCurveTL -n "cp_c009001daipa:waist_FK2_ctrl_outPutAnimBank_1_translateY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  1 0.043404702372173171 3 0.0021721399999999999 
		6 -0.055536200000000001 12 0.0598804 17 -0.055536200000000001 23 0.0598804 25 0.043385019254089295;
	setAttr -s 7 ".kit[3:6]"  10 1 1 1;
	setAttr -s 7 ".kot[3:6]"  10 1 1 1;
	setAttr -s 7 ".kix[0:6]"  0.94520527124404907 0.87568527460098267 
		0.98949921131134033 1 0.99953269958496094 0.99998855590820313 0.94520527124404907;
	setAttr -s 7 ".kiy[0:6]"  -0.32647666335105896 -0.48288232088088989 
		-0.14453823864459991 0 -0.030567539855837822 -0.0047780326567590237 -0.32647666335105896;
	setAttr -s 7 ".kox[0:6]"  0.94520527124404907 0.87568527460098267 
		0.98949921131134033 1 0.99953269958496094 0.99998855590820313 0.94520527124404907;
	setAttr -s 7 ".koy[0:6]"  -0.32647669315338135 -0.48288232088088989 
		-0.14453823864459991 0 -0.030567578971385956 -0.0047780708409845829 -0.32647669315338135;
createNode animCurveTL -n "cp_c009001daipa:waist_FK2_ctrl_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 25 0;
createNode animCurveTA -n "cp_c009001daipa:waist_FK2_ctrl_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  1 2.2333922828376651 3 2.6330562494272707 
		6 3.2665633096146469 12 2.1253240849662816 18 3.2630721834119671 24 2.1700233136275835 
		25 2.2318847350690771;
	setAttr -s 7 ".kit[0:6]"  1 1 10 10 10 10 1;
	setAttr -s 7 ".kot[0:6]"  1 1 10 10 10 10 1;
	setAttr -s 7 ".kix[0:6]"  0.99904417991638184 0.99520421028137207 
		1 1 1 1 0.99904417991638184;
	setAttr -s 7 ".kiy[0:6]"  0.04371226578950882 0.09781917929649353 
		0 0 0 0 0.04371226578950882;
	setAttr -s 7 ".kox[0:6]"  0.99908322095870972 0.99520421028137207 
		1 1 1 1 0.99908322095870972;
	setAttr -s 7 ".koy[0:6]"  0.042809419333934784 0.09781917929649353 
		0 0 0 0 0.042809419333934784;
createNode animCurveTA -n "cp_c009001daipa:waist_FK2_ctrl_outPutAnimBank_1_rotateY";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 -5.7798648464346654 3 -7 15 7 25 -5.779865206529597;
	setAttr -s 4 ".kit[0:3]"  1 3 3 1;
	setAttr -s 4 ".kot[0:3]"  1 3 3 1;
	setAttr -s 4 ".kix[0:3]"  0.87475985288619995 1 1 0.87475985288619995;
	setAttr -s 4 ".kiy[0:3]"  -0.484556645154953 0 0 -0.484556645154953;
	setAttr -s 4 ".kox[0:3]"  0.91224825382232666 1 1 0.91224825382232666;
	setAttr -s 4 ".koy[0:3]"  -0.40963789820671082 0 0 -0.40963789820671082;
createNode animCurveTA -n "cp_c009001daipa:waist_FK2_ctrl_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -2.6153618344731004 10 3.3271305835231084 
		15 0 20 -3.6542611670462177 25 -2.6153621696489879;
	setAttr -s 5 ".kix[0:4]"  0.95930534601211548 0.99912536144256592 
		0.94665366411209106 0.99090194702148438 0.98233932256698608;
	setAttr -s 5 ".kiy[0:4]"  0.28237095475196838 0.041815835982561111 
		-0.32225281000137329 -0.13458631932735443 0.18710812926292419;
	setAttr -s 5 ".kox[0:4]"  0.96575802564620972 0.99912536144256592 
		0.94665366411209106 0.9909018874168396 0.98669582605361938;
	setAttr -s 5 ".koy[0:4]"  0.25944462418556213 0.04181588813662529 
		-0.3222527801990509 -0.13458633422851563 0.16257710754871368;
select -ne :time1;
	setAttr ".o" 49;
	setAttr ".unw" 49;
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
// End of slow_walk.ma

//Maya ASCII 2012 scene
//Name: vk_foot_walk.ma
//Last modified: Mon, Sep 03, 2012 02:15:20 PM
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
	setAttr ".num" 11;
	setAttr ".nts" -type "string" "vicky_original:l_legA_foot_IK_ctrl; vicky_original:r_legA_foot_IK_ctrl; vicky_original:r_legA_ankle_ctrl; vicky_original:l_legA_ankle_ctrl; vicky_original:l_legA_heel_IK_ctrl; vicky_original:r_legA_heel_IK_ctrl; vicky_original:r_legA_knee_IK_ctrl; vicky_original:l_legA_knee_IK_ctrl; vicky_original:m_spineA_body_ctrl; vicky_original:m_spineA_torso_ctrl; vicky_original:m_spineA_hip_ctrl; ";
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
connectAttr "vicky_original:l_legA_heel_IK_ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:l_legA_heel_IK_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:l_legA_heel_IK_ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:l_legA_heel_IK_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:l_legA_heel_IK_ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:l_legA_heel_IK_ctrl_outPutAnimBank_1.rz"
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
connectAttr "vicky_original:l_legA_knee_IK_ctrl_outPutAnimBank_1_translateX.o" "vicky_original:l_legA_knee_IK_ctrl_outPutAnimBank_1.tx"
		;
connectAttr "vicky_original:l_legA_knee_IK_ctrl_outPutAnimBank_1_translateY.o" "vicky_original:l_legA_knee_IK_ctrl_outPutAnimBank_1.ty"
		;
connectAttr "vicky_original:l_legA_knee_IK_ctrl_outPutAnimBank_1_translateZ.o" "vicky_original:l_legA_knee_IK_ctrl_outPutAnimBank_1.tz"
		;
connectAttr "vicky_original:l_legA_knee_IK_ctrl_outPutAnimBank_1_followBody_2_followFoot.o" "vicky_original:l_legA_knee_IK_ctrl_outPutAnimBank_1.followBody_2_followFoot"
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
connectAttr "vicky_original:m_spineA_torso_ctrl_outPutAnimBank_1_rotateX.o" "vicky_original:m_spineA_torso_ctrl_outPutAnimBank_1.rx"
		;
connectAttr "vicky_original:m_spineA_torso_ctrl_outPutAnimBank_1_rotateY.o" "vicky_original:m_spineA_torso_ctrl_outPutAnimBank_1.ry"
		;
connectAttr "vicky_original:m_spineA_torso_ctrl_outPutAnimBank_1_rotateZ.o" "vicky_original:m_spineA_torso_ctrl_outPutAnimBank_1.rz"
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
// End of vk_foot_walk.ma

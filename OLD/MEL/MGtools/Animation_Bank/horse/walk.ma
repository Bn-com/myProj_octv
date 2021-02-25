//Maya ASCII 2011 scene
//Name: walk.ma
//Last modified: Wed, Jul 18, 2012 09:36:37 AM
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
	setAttr ".ns" -type "string" "cc";
	setAttr ".range" -type "string" "\"1:75\"";
	setAttr ".num" 24;
	setAttr ".nts" -type "string" "cc_r_legFT01; cc_r_legBK01; cc_l_legFT01; cc_l_legBK01; cc_hipSway01; cc_midVertebraet01; cc_thoracic01; cc_r_carpalFT01; cc_r_tarsalFT01; cc_l_carpalFT01; cc_l_tarsalFT01; cc_COG01; cc_head01; cc_cervical02; cc_cervical01; cc_tail01; cc_tail02; cc_tail03; cc_cc_tail04; cc_tail05; cc_tail06; cc_r_shoulder01; cc_l_shoulder01; cc_global01; ";
createNode transform -n "cc_r_legFT01_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "fetlock_ft_curl" -ln "fetlock_ft_curl" -at "double";
	addAttr -ci true -sn "hoof_ft_curl" -ln "hoof_ft_curl" -at "double";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr -k on ".fetlock_ft_curl";
	setAttr -k on ".hoof_ft_curl";
	setAttr ".ObjName" -type "string" "cc_r_legFT01";
createNode locator -n "cc_r_legFT01_outPutAnimBank_1Shape" -p "cc_r_legFT01_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "cc_r_legBK01_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "fetlock_bk_curl" -ln "fetlock_bk_curl" -at "double";
	addAttr -ci true -sn "hoof_bk_curl" -ln "hoof_bk_curl" -at "double";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr -k on ".fetlock_bk_curl";
	setAttr -k on ".hoof_bk_curl";
	setAttr ".ObjName" -type "string" "cc_r_legBK01";
createNode locator -n "cc_r_legBK01_outPutAnimBank_1Shape" -p "cc_r_legBK01_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "cc_l_legFT01_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "fetlock_ft_curl" -ln "fetlock_ft_curl" -at "double";
	addAttr -ci true -sn "hoof_ft_curl" -ln "hoof_ft_curl" -at "double";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr -k on ".fetlock_ft_curl";
	setAttr -k on ".hoof_ft_curl";
	setAttr ".ObjName" -type "string" "cc_l_legFT01";
createNode locator -n "cc_l_legFT01_outPutAnimBank_1Shape" -p "cc_l_legFT01_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "cc_l_legBK01_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "fetlock_bk_curl" -ln "fetlock_bk_curl" -at "double";
	addAttr -ci true -sn "hoof_bk_curl" -ln "hoof_bk_curl" -at "double";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr -k on ".fetlock_bk_curl";
	setAttr -k on ".hoof_bk_curl";
	setAttr ".ObjName" -type "string" "cc_l_legBK01";
createNode locator -n "cc_l_legBK01_outPutAnimBank_1Shape" -p "cc_l_legBK01_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "cc_hipSway01_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "cc_hipSway01";
createNode locator -n "cc_hipSway01_outPutAnimBank_1Shape" -p "cc_hipSway01_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "cc_midVertebraet01_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "cc_midVertebraet01";
createNode locator -n "cc_midVertebraet01_outPutAnimBank_1Shape" -p "cc_midVertebraet01_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "cc_thoracic01_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "lock" -ln "lock" -at "double";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr -k on ".lock";
	setAttr ".ObjName" -type "string" "cc_thoracic01";
createNode locator -n "cc_thoracic01_outPutAnimBank_1Shape" -p "cc_thoracic01_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "cc_r_carpalFT01_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "cc_r_carpalFT01";
createNode locator -n "cc_r_carpalFT01_outPutAnimBank_1Shape" -p "cc_r_carpalFT01_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "cc_r_tarsalFT01_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "cc_r_tarsalFT01";
createNode locator -n "cc_r_tarsalFT01_outPutAnimBank_1Shape" -p "cc_r_tarsalFT01_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "cc_l_carpalFT01_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "cc_l_carpalFT01";
createNode locator -n "cc_l_carpalFT01_outPutAnimBank_1Shape" -p "cc_l_carpalFT01_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "cc_l_tarsalFT01_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "cc_l_tarsalFT01";
createNode locator -n "cc_l_tarsalFT01_outPutAnimBank_1Shape" -p "cc_l_tarsalFT01_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "cc_COG01_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "tr_curl" -ln "tr_curl" -at "double";
	addAttr -ci true -sn "tr_sway" -ln "tr_sway" -at "double";
	addAttr -ci true -sn "tr_turn" -ln "tr_turn" -at "double";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr -k on ".tr_curl";
	setAttr -k on ".tr_sway";
	setAttr -k on ".tr_turn";
	setAttr ".ObjName" -type "string" "cc_COG01";
createNode locator -n "cc_COG01_outPutAnimBank_1Shape" -p "cc_COG01_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "cc_head01_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ear_r_rootCurl" -ln "ear_r_rootCurl" -at "double";
	addAttr -ci true -sn "ear_r_rootTurn" -ln "ear_r_rootTurn" -at "double";
	addAttr -ci true -sn "ear_r_rootSway" -ln "ear_r_rootSway" -at "double";
	addAttr -ci true -sn "ear_r_midCurl" -ln "ear_r_midCurl" -at "double";
	addAttr -ci true -sn "ear_r_midTurn" -ln "ear_r_midTurn" -at "double";
	addAttr -ci true -sn "ear_r_midSway" -ln "ear_r_midSway" -at "double";
	addAttr -ci true -sn "ear_l_rootCurl" -ln "ear_l_rootCurl" -at "double";
	addAttr -ci true -sn "ear_l_rootTurn" -ln "ear_l_rootTurn" -at "double";
	addAttr -ci true -sn "ear_l_rootSway" -ln "ear_l_rootSway" -at "double";
	addAttr -ci true -sn "ear_l_midCurl" -ln "ear_l_midCurl" -at "double";
	addAttr -ci true -sn "ear_l_midTurn" -ln "ear_l_midTurn" -at "double";
	addAttr -ci true -sn "ear_l_midSway" -ln "ear_l_midSway" -at "double";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr -k on ".ear_r_rootCurl";
	setAttr -k on ".ear_r_rootTurn";
	setAttr -k on ".ear_r_rootSway";
	setAttr -k on ".ear_r_midCurl";
	setAttr -k on ".ear_r_midTurn";
	setAttr -k on ".ear_r_midSway";
	setAttr -k on ".ear_l_rootCurl";
	setAttr -k on ".ear_l_rootTurn";
	setAttr -k on ".ear_l_rootSway";
	setAttr -k on ".ear_l_midCurl";
	setAttr -k on ".ear_l_midTurn";
	setAttr -k on ".ear_l_midSway";
	setAttr ".ObjName" -type "string" "cc_head01";
createNode locator -n "cc_head01_outPutAnimBank_1Shape" -p "cc_head01_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "cc_cervical02_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "cc_cervical02";
createNode locator -n "cc_cervical02_outPutAnimBank_1Shape" -p "cc_cervical02_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "cc_cervical01_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "cc_cervical01";
createNode locator -n "cc_cervical01_outPutAnimBank_1Shape" -p "cc_cervical01_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "cc_tail01_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "cc_tail01";
createNode locator -n "cc_tail01_outPutAnimBank_1Shape" -p "cc_tail01_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "cc_tail02_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "cc_tail02";
createNode locator -n "cc_tail02_outPutAnimBank_1Shape" -p "cc_tail02_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "cc_tail03_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "cc_tail03";
createNode locator -n "cc_tail03_outPutAnimBank_1Shape" -p "cc_tail03_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "cc_cc_tail04_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "cc_cc_tail04";
createNode locator -n "cc_cc_tail04_outPutAnimBank_1Shape" -p "cc_cc_tail04_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "cc_tail05_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "cc_tail05";
createNode locator -n "cc_tail05_outPutAnimBank_1Shape" -p "cc_tail05_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "cc_tail06_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "cc_tail06";
createNode locator -n "cc_tail06_outPutAnimBank_1Shape" -p "cc_tail06_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "cc_r_shoulder01_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "cc_r_shoulder01";
createNode locator -n "cc_r_shoulder01_outPutAnimBank_1Shape" -p "cc_r_shoulder01_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "cc_l_shoulder01_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "cc_l_shoulder01";
createNode locator -n "cc_l_shoulder01_outPutAnimBank_1Shape" -p "cc_l_shoulder01_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "cc_global01_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "vis_head_cervix" -ln "vis_head_cervix" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "vis_upperBody" -ln "vis_upperBody" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "vis_ft_legs" -ln "vis_ft_legs" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "vis_bk_legs" -ln "vis_bk_legs" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "vis_tail" -ln "vis_tail" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k on ".vis_head_cervix";
	setAttr -k on ".vis_upperBody";
	setAttr -k on ".vis_ft_legs";
	setAttr -k on ".vis_bk_legs";
	setAttr -k on ".vis_tail";
	setAttr ".ObjName" -type "string" "cc_global01";
createNode locator -n "cc_global01_outPutAnimBank_1Shape" -p "cc_global01_outPutAnimBank_1";
	setAttr -k off ".v";
createNode animCurveTL -n "cc_r_legFT01_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 8 13 8 19 8 25 8;
createNode animCurveTL -n "cc_r_legFT01_outPutAnimBank_1_translateY";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  1 0 7 0 13 6.7726872246696033 15 6.1264465907516605 
		18 0 19 0 25 0;
	setAttr -s 7 ".kit[2:6]"  9 9 10 1 3;
	setAttr -s 7 ".kot[2:6]"  9 9 10 1 3;
	setAttr -s 7 ".kix[5:6]"  1 1;
	setAttr -s 7 ".kiy[5:6]"  0 0;
	setAttr -s 7 ".kox[5:6]"  1 1;
	setAttr -s 7 ".koy[5:6]"  0 0;
createNode animCurveTL -n "cc_r_legFT01_outPutAnimBank_1_translateZ";
	setAttr ".tan" 2;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  1 6.2825754563023199 7 -29.227782206849888 
		10 -43.527119677010091 13 -23.775390298581051 15 4.1941318516887396 17 35.392636361995486 
		19 40 25 6.2825754563023199;
	setAttr -s 8 ".kit[3:7]"  1 1 1 9 2;
	setAttr -s 8 ".kot[1:7]"  9 3 1 1 1 2 2;
	setAttr -s 8 ".kix[3:7]"  0.0048835733905434608 0.0028967331163585186 
		0.0025187286082655191 0.011450043879449368 0.0074143577367067337;
	setAttr -s 8 ".kiy[3:7]"  0.99998807907104492 0.99999576807022095 
		0.9999968409538269 -0.99993449449539185 -0.99997252225875854;
	setAttr -s 8 ".kox[3:7]"  0.0048835743218660355 0.0028967331163585186 
		0.0025187286082655191 0.0074143577367067337 1;
	setAttr -s 8 ".koy[3:7]"  0.99998807907104492 0.99999576807022095 
		0.9999968409538269 -0.99997252225875854 0;
createNode animCurveTA -n "cc_r_legFT01_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 0 13 0 19 0 25 0;
createNode animCurveTA -n "cc_r_legFT01_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 0 13 0 19 0 25 0;
createNode animCurveTA -n "cc_r_legFT01_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 0 13 0 19 0 25 0;
createNode animCurveTU -n "cc_r_legFT01_outPutAnimBank_1_fetlock_ft_curl";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  1 6.8397274158152399 4 26.512715654539122 
		7 40.38919349848787 13 0.7585424786213153 17 -8.4121278482938457 19 -9.9655658338989586 
		22 -4.7551900335022577 25 6.8397274158152399;
	setAttr -s 8 ".kit[1:7]"  10 10 1 1 1 10 9;
	setAttr -s 8 ".kot[1:7]"  10 10 1 1 1 10 9;
	setAttr -s 8 ".kix[0:7]"  0.0064886119216680527 0.0074514760635793209 
		0.014559203758835793 0.012863793410360813 0.16666656732559204 0.081086620688438416 
		0.014874614775180817 0.010779953561723232;
	setAttr -s 8 ".kiy[0:7]"  0.99997895956039429 0.99997228384017944 
		-0.99989402294158936 -0.99991726875305176 -4.3821096420288086 -0.99670714139938354 
		0.99988937377929688 0.99994182586669922;
	setAttr -s 8 ".kox[0:7]"  0.0064886114560067654 0.0074514760635793209 
		0.014559203758835793 0.01286378875374794 0.083333373069763184 0.081086546182632446 
		0.014874614775180817 0.010779953561723232;
	setAttr -s 8 ".koy[0:7]"  0.99997901916503906 0.99997228384017944 
		-0.99989402294158936 -0.99991726875305176 -2.1910562515258789 -0.99670708179473877 
		0.99988937377929688 0.99994182586669922;
createNode animCurveTU -n "cc_r_legFT01_outPutAnimBank_1_hoof_ft_curl";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  1 0 7 0 8 5 10 72.26955844364312 13 91.79862198407973 
		15 79.515291314507706 19 0 25 0;
	setAttr -s 8 ".kit[1:7]"  3 1 10 1 9 3 10;
	setAttr -s 8 ".kot[1:7]"  3 1 10 1 9 3 10;
	setAttr -s 8 ".kix[2:7]"  0.0031291225459426641 0.0024001849815249443 
		1 0.0027233422733843327 1 1;
	setAttr -s 8 ".kiy[2:7]"  0.99999511241912842 0.99999713897705078 
		0 -0.99999624490737915 0 0;
	setAttr -s 8 ".kox[2:7]"  0.0031291213817894459 0.0024001849815249443 
		1 0.0027233422733843327 1 1;
	setAttr -s 8 ".koy[2:7]"  0.99999511241912842 0.99999713897705078 
		0 -0.99999624490737915 0 0;
createNode animCurveTL -n "cc_r_legBK01_outPutAnimBank_1_translateX";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  10 2 23 2;
	setAttr -s 2 ".kit[0:1]"  10 1;
	setAttr -s 2 ".kot[1]"  10;
	setAttr -s 2 ".kix[1]"  1;
	setAttr -s 2 ".kiy[1]"  0;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "cc_r_legBK01_outPutAnimBank_1_translateY";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  2 1.6002959788509479 4 5.8924845153909882 
		7 3.9617743092692868 10 0 23 0;
	setAttr -s 5 ".kit[3:4]"  1 1;
	setAttr -s 5 ".kot[0:4]"  1 9 9 1 3;
	setAttr -s 5 ".kix[3:4]"  1 1;
	setAttr -s 5 ".kiy[3:4]"  0 0;
	setAttr -s 5 ".kox[0:4]"  0.035333696752786636 0.087880238890647888 
		0.042388789355754852 1 1;
	setAttr -s 5 ".koy[0:4]"  0.99937558174133301 0.99613106250762939 
		-0.99910116195678711 0 0;
createNode animCurveTL -n "cc_r_legBK01_outPutAnimBank_1_translateZ";
	setAttr ".tan" 2;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  2 -44.723681213940573 4 -31.047102066549193 
		10 42.083434768975231 23 -30.081800546582173;
	setAttr -s 4 ".kit[1:3]"  9 3 1;
	setAttr -s 4 ".kot[0:3]"  1 9 2 2;
	setAttr -s 4 ".kix[3]"  0.0075057107023894787;
	setAttr -s 4 ".kiy[3]"  -0.99997186660766602;
	setAttr -s 4 ".kox[0:3]"  1 0.0038399025797843933 0.0075057107023894787 
		1;
	setAttr -s 4 ".koy[0:3]"  0 0.99999260902404785 -0.99997186660766602 
		0;
createNode animCurveTA -n "cc_r_legBK01_outPutAnimBank_1_rotateX";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  10 0 23 0;
	setAttr -s 2 ".kit[0:1]"  10 1;
	setAttr -s 2 ".kot[1]"  10;
	setAttr -s 2 ".kix[1]"  1;
	setAttr -s 2 ".kiy[1]"  0;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "cc_r_legBK01_outPutAnimBank_1_rotateY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  10 0 23 0;
	setAttr -s 2 ".kit[0:1]"  10 1;
	setAttr -s 2 ".kot[1]"  10;
	setAttr -s 2 ".kix[1]"  1;
	setAttr -s 2 ".kiy[1]"  0;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "cc_r_legBK01_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  10 0 23 0;
	setAttr -s 2 ".kit[0:1]"  10 1;
	setAttr -s 2 ".kot[1]"  10;
	setAttr -s 2 ".kix[1]"  1;
	setAttr -s 2 ".kiy[1]"  0;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "cc_r_legBK01_outPutAnimBank_1_fetlock_bk_curl";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  4 -21.700000000000003 10 0 23 0;
	setAttr -s 3 ".kit[2]"  1;
	setAttr -s 3 ".kot[0:2]"  1 10 10;
	setAttr -s 3 ".kix[2]"  1;
	setAttr -s 3 ".kiy[2]"  0;
	setAttr -s 3 ".kox[0:2]"  1 1 1;
	setAttr -s 3 ".koy[0:2]"  0 0 0;
createNode animCurveTU -n "cc_r_legBK01_outPutAnimBank_1_hoof_bk_curl";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  2 63.726205422858143 4 82.322907488986786 
		7 61.947113885272813 10 0 23 0;
	setAttr -s 5 ".kit[4]"  1;
	setAttr -s 5 ".kot[0:4]"  1 10 10 10 10;
	setAttr -s 5 ".kix[4]"  1;
	setAttr -s 5 ".kiy[4]"  0;
	setAttr -s 5 ".kox[0:4]"  0.0025306770112365484 0.11630622297525406 
		0.0030368075240403414 1 1;
	setAttr -s 5 ".koy[0:4]"  0.9999968409538269 -0.99321335554122925 
		-0.99999535083770752 0 0;
createNode animCurveTL -n "cc_l_legFT01_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 -8 7 -8 13 -8 25 -8;
createNode animCurveTL -n "cc_l_legFT01_outPutAnimBank_1_translateY";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  1 6.7726872246696033 3 6.2791359887809755 
		5 1.92700380835225 7 0 13 0 19 0 25 6.7726872246696033;
	setAttr -s 7 ".kit[0:6]"  1 9 9 1 3 3 9;
	setAttr -s 7 ".kot[0:6]"  1 9 9 1 3 3 9;
	setAttr -s 7 ".kix[0:6]"  0.062088407576084137 0.034374542534351349 
		0.0265335813164711 1 1 1 0.036887839436531067;
	setAttr -s 7 ".kiy[0:6]"  0.99807065725326538 -0.999409019947052 
		-0.99964785575866699 0 0 0 0.99931943416595459;
	setAttr -s 7 ".kox[0:6]"  0.062088411301374435 0.034374542534351349 
		0.0265335813164711 1 1 1 0.036887839436531067;
	setAttr -s 7 ".koy[0:6]"  0.99807065725326538 -0.999409019947052 
		-0.99964785575866699 0 0 0 0.99931943416595459;
createNode animCurveTL -n "cc_l_legFT01_outPutAnimBank_1_translateZ";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  1 -24.106718755310137 3 2.3711622862436768 
		5 34.252775773678508 7 40 19 -27.886658718945398 22 -42.859902531733354 25 -24.106718755310137;
	setAttr -s 7 ".kit[1:6]"  10 1 9 1 2 1;
	setAttr -s 7 ".kot[1:6]"  10 1 2 2 3 1;
	setAttr -s 7 ".kix[0:6]"  0.0042217327281832695 0.002855850150808692 
		0.002458222908899188 0.0093870777636766434 0.0072622648440301418 0.0083479341119527817 
		0.0038532321341335773;
	setAttr -s 7 ".kiy[0:6]"  0.99999111890792847 0.9999958872795105 
		0.99999701976776123 -0.99995595216751099 -0.9999735951423645 -0.99996519088745117 
		0.99999254941940308;
	setAttr -s 7 ".kox[0:6]"  0.0042217322625219822 0.002855850150808692 
		0.0024582226760685444 0.0073650181293487549 0.0083479341119527817 1 0.0038532321341335773;
	setAttr -s 7 ".koy[0:6]"  0.99999111890792847 0.9999958872795105 
		0.99999701976776123 -0.99997293949127197 -0.99996519088745117 0 0.99999254941940308;
createNode animCurveTA -n "cc_l_legFT01_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 0 7 0 13 0 25 0;
createNode animCurveTA -n "cc_l_legFT01_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 0 7 0 13 0 25 0;
createNode animCurveTA -n "cc_l_legFT01_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 0 7 0 13 0 25 0;
createNode animCurveTU -n "cc_l_legFT01_outPutAnimBank_1_fetlock_ft_curl";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  1 0.80639310237617678 5 -7.8254989579151584 
		7 -9.566943709051106 10 -4.2101664884576504 13 8.3915314572992799 16 26.279281666306357 
		19 39.026193984001786 25 0.80639310237617678;
	setAttr -s 8 ".kit[2:7]"  3 1 10 9 10 9;
	setAttr -s 8 ".kot[2:7]"  3 1 10 9 10 9;
	setAttr -s 8 ".kix[0:7]"  0.012277982197701931 0.033666156232357025 
		1 0.010782231576740742 0.0081992829218506813 0.0081604188308119774 0.01471993699669838 
		0.0065409708768129349;
	setAttr -s 8 ".kiy[0:7]"  -0.99992465972900391 -0.99943315982818604 
		0 0.99994194507598877 0.9999663233757019 0.99996668100357056 -0.99989163875579834 
		-0.99997866153717041;
	setAttr -s 8 ".kox[0:7]"  0.012277981266379356 0.033666156232357025 
		1 0.010782229714095592 0.0081992829218506813 0.0081604188308119774 0.01471993699669838 
		0.0065409708768129349;
	setAttr -s 8 ".koy[0:7]"  -0.99992465972900391 -0.99943315982818604 
		0 0.99994188547134399 0.9999663233757019 0.99996668100357056 -0.99989163875579834 
		-0.99997866153717041;
createNode animCurveTU -n "cc_l_legFT01_outPutAnimBank_1_hoof_ft_curl";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  1 91.119261554279177 3 79.327465542978956 
		7 0 13 0 19 0 20 5 22 71.667959800739951 25 91.119261554279177;
	setAttr -s 8 ".kit[1:7]"  10 3 10 3 1 10 3;
	setAttr -s 8 ".kot[1:7]"  10 3 10 3 1 10 3;
	setAttr -s 8 ".kix[5:7]"  0.0028369820211082697 0.0024191185366362333 
		1;
	setAttr -s 8 ".kiy[5:7]"  0.99999600648880005 0.99999701976776123 
		0;
	setAttr -s 8 ".kox[5:7]"  0.0028369820211082697 0.0024191185366362333 
		1;
	setAttr -s 8 ".koy[5:7]"  0.99999600648880005 0.99999701976776123 
		0;
createNode animCurveTL -n "cc_l_legBK01_outPutAnimBank_1_translateX";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  11 -2 22 -2;
	setAttr -s 2 ".kit[0:1]"  10 1;
	setAttr -s 2 ".kot[1]"  10;
	setAttr -s 2 ".kix[1]"  1;
	setAttr -s 2 ".kiy[1]"  0;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTL -n "cc_l_legBK01_outPutAnimBank_1_translateY";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  11 0 14 1.6002959788509479 16 5.9875502322749501 
		19 4.0203578943831291 22 0;
	setAttr -s 5 ".kit[0:4]"  1 9 9 9 1;
	setAttr -s 5 ".kot[0:4]"  1 9 9 9 1;
	setAttr -s 5 ".kix[0:4]"  1 0.034773379564285278 0.085768744349479675 
		0.041716955602169037 1;
	setAttr -s 5 ".kiy[0:4]"  0 0.99939525127410889 0.99631506204605103 
		-0.99912941455841064 0;
	setAttr -s 5 ".kox[0:4]"  1 0.034773379564285278 0.085768744349479675 
		0.041716955602169037 1;
	setAttr -s 5 ".koy[0:4]"  0 0.99939525127410889 0.99631506204605103 
		-0.99912941455841064 0;
createNode animCurveTL -n "cc_l_legBK01_outPutAnimBank_1_translateZ";
	setAttr ".tan" 2;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  11 -29.74939508091056 14 -47.098186493698293 
		16 -31.102209095999967 22 43.145176224665207;
	setAttr -s 4 ".kit[2:3]"  9 1;
	setAttr -s 4 ".kot[0:3]"  1 3 9 3;
	setAttr -s 4 ".kix[3]"  1;
	setAttr -s 4 ".kiy[3]"  0;
	setAttr -s 4 ".kox[0:3]"  0.0073872297070920467 1 0.0036936909891664982 
		1;
	setAttr -s 4 ".koy[0:3]"  -0.99997270107269287 0 0.99999314546585083 
		0;
createNode animCurveTA -n "cc_l_legBK01_outPutAnimBank_1_rotateX";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  11 0 22 0;
	setAttr -s 2 ".kit[0:1]"  10 1;
	setAttr -s 2 ".kot[1]"  10;
	setAttr -s 2 ".kix[1]"  1;
	setAttr -s 2 ".kiy[1]"  0;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "cc_l_legBK01_outPutAnimBank_1_rotateY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  11 0 22 0;
	setAttr -s 2 ".kit[0:1]"  10 1;
	setAttr -s 2 ".kot[1]"  10;
	setAttr -s 2 ".kix[1]"  1;
	setAttr -s 2 ".kiy[1]"  0;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "cc_l_legBK01_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  11 0 22 0;
	setAttr -s 2 ".kit[0:1]"  10 1;
	setAttr -s 2 ".kot[1]"  10;
	setAttr -s 2 ".kix[1]"  1;
	setAttr -s 2 ".kiy[1]"  0;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTU -n "cc_l_legBK01_outPutAnimBank_1_fetlock_bk_curl";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  11 0 16 -21 22 0;
	setAttr -s 3 ".kit[2]"  1;
	setAttr -s 3 ".kot[0:2]"  1 10 10;
	setAttr -s 3 ".kix[2]"  0.011903918348252773;
	setAttr -s 3 ".kiy[2]"  0.99992918968200684;
	setAttr -s 3 ".kox[0:2]"  1 1 0.011903918348252773;
	setAttr -s 3 ".koy[0:2]"  0 0 0.99992918968200684;
createNode animCurveTU -n "cc_l_legBK01_outPutAnimBank_1_hoof_bk_curl";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  11 0 14 65.068568417405885 16 84.787207203710537 
		19 63.166489388949543 22 0;
	setAttr -s 5 ".kit[4]"  1;
	setAttr -s 5 ".kot[0:4]"  1 10 10 10 10;
	setAttr -s 5 ".kix[4]"  0.001978893531486392;
	setAttr -s 5 ".kiy[4]"  -0.99999803304672241;
	setAttr -s 5 ".kox[0:4]"  1 0.0024571244139224291 0.10887815803289413 
		0.0029485451523214579 0.001978893531486392;
	setAttr -s 5 ".koy[0:4]"  0 0.99999701976776123 -0.99405509233474731 
		-0.99999570846557617 -0.99999803304672241;
createNode animCurveTL -n "cc_hipSway01_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  4 0.94624107435896765 10 0.39841475325256714 
		16 -1.0561248626371453 22 -0.56303547516506391;
	setAttr -s 4 ".kit[3]"  1;
	setAttr -s 4 ".kot[0:3]"  1 10 10 1;
	setAttr -s 4 ".kix[3]"  0.19589009881019592;
	setAttr -s 4 ".kiy[3]"  0.98062586784362793;
	setAttr -s 4 ".kox[0:3]"  0.46138608455657959 0.24226589500904083 
		0.46138608455657959 0.19589009881019592;
	setAttr -s 4 ".koy[0:3]"  0.8871995210647583 -0.97020989656448364 
		-0.8871995210647583 0.98062586784362793;
createNode animCurveTL -n "cc_hipSway01_outPutAnimBank_1_translateY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  4 -1.1101368111277725 7 -1.2471027409266133 
		10 -3.1235565339049627 16 -1.0583519259623058 19 -1.2471027409266133 22 -3.1235565339049627;
	setAttr -s 6 ".kit[0:5]"  10 9 1 10 9 1;
	setAttr -s 6 ".kot[1:5]"  9 1 10 9 1;
	setAttr -s 6 ".kix[2:5]"  0.081487178802490234 0.19597005844116211 
		0.1201760545372963 0.082086116075515747;
	setAttr -s 6 ".kiy[2:5]"  -0.99667441844940186 0.98060989379882813 
		-0.99275261163711548 -0.99662530422210693;
	setAttr -s 6 ".kox[0:5]"  0.19597004354000092 0.12322061508893967 
		0.081487186253070831 0.19597005844116211 0.1201760545372963 0.082086123526096344;
	setAttr -s 6 ".koy[0:5]"  0.98060989379882813 -0.99237930774688721 
		-0.99667441844940186 0.98060989379882813 -0.99275261163711548 -0.99662530422210693;
createNode animCurveTL -n "cc_hipSway01_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  4 -0.49251101321585899 10 0 16 -0.49251101321585899 
		22 0;
	setAttr -s 4 ".kit[1:3]"  3 10 1;
	setAttr -s 4 ".kot[0:3]"  1 3 10 3;
	setAttr -s 4 ".kix[3]"  1;
	setAttr -s 4 ".kiy[3]"  0;
	setAttr -s 4 ".kox[0:3]"  1 1 1 1;
	setAttr -s 4 ".koy[0:3]"  0 0 0 0;
createNode animCurveTA -n "cc_hipSway01_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  4 -0.99361803414791949 10 -1.6772087540564644 
		16 -0.99361803414791949 22 -1.6772087540564644;
	setAttr -s 4 ".kit[1:3]"  3 10 1;
	setAttr -s 4 ".kot[0:3]"  1 3 10 3;
	setAttr -s 4 ".kix[3]"  1;
	setAttr -s 4 ".kiy[3]"  0;
	setAttr -s 4 ".kox[0:3]"  1 1 1 1;
	setAttr -s 4 ".koy[0:3]"  0 0 0 0;
createNode animCurveTA -n "cc_hipSway01_outPutAnimBank_1_rotateY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  10 3.0605354139305616 22 -3.0801409691629953;
	setAttr -s 2 ".kit[0:1]"  10 1;
	setAttr -s 2 ".kot[1]"  3;
	setAttr -s 2 ".kix[1]"  1;
	setAttr -s 2 ".kiy[1]"  0;
	setAttr -s 2 ".kox[0:1]"  1 1;
	setAttr -s 2 ".koy[0:1]"  0 0;
createNode animCurveTA -n "cc_hipSway01_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  4 4 10 0 16 -4 22 0;
	setAttr -s 4 ".kit[1:3]"  9 10 1;
	setAttr -s 4 ".kot[0:3]"  1 9 10 9;
	setAttr -s 4 ".kix[3]"  0.96315068006515503;
	setAttr -s 4 ".kiy[3]"  0.26896241307258606;
	setAttr -s 4 ".kox[0:3]"  1 0.96315068006515503 1 0.96315068006515503;
	setAttr -s 4 ".koy[0:3]"  0 -0.26896241307258606 0 0.26896241307258606;
createNode animCurveTL -n "cc_midVertebraet01_outPutAnimBank_1_translateX";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 7 0 13 0 19 0 25 0;
	setAttr -s 5 ".kit[1:4]"  10 3 10 3;
	setAttr -s 5 ".kot[1:4]"  10 3 10 3;
createNode animCurveTL -n "cc_midVertebraet01_outPutAnimBank_1_translateY";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 7 -2.4861306074271283 13 0 19 -2.5417236078018846 
		25 0;
	setAttr -s 5 ".kit[1:4]"  10 3 10 3;
	setAttr -s 5 ".kot[1:4]"  10 3 10 3;
createNode animCurveTL -n "cc_midVertebraet01_outPutAnimBank_1_translateZ";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 7 0 13 0 19 0 25 0;
	setAttr -s 5 ".kit[1:4]"  10 3 10 3;
	setAttr -s 5 ".kot[1:4]"  10 3 10 3;
createNode animCurveTA -n "cc_midVertebraet01_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  4 11.434579004306846 10 13.430946821839362 
		16 11.434579004306846 22 13.169789028426482;
	setAttr -s 4 ".kit[1:3]"  3 10 1;
	setAttr -s 4 ".kot[0:3]"  1 3 10 3;
	setAttr -s 4 ".kix[3]"  1;
	setAttr -s 4 ".kiy[3]"  0;
	setAttr -s 4 ".kox[0:3]"  1 1 1 1;
	setAttr -s 4 ".koy[0:3]"  0 0 0 0;
createNode animCurveTA -n "cc_midVertebraet01_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -5 7 -6.1467287579897535e-007 13 5 19 
		-0.41666740438888977 25 -5;
	setAttr -s 5 ".kit[0:4]"  3 10 9 10 3;
	setAttr -s 5 ".kot[0:4]"  3 10 9 10 3;
createNode animCurveTA -n "cc_midVertebraet01_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 7 0 13 0 19 0 25 0;
	setAttr -s 5 ".kit[1:4]"  10 3 10 3;
	setAttr -s 5 ".kot[1:4]"  10 3 10 3;
createNode animCurveTL -n "cc_thoracic01_outPutAnimBank_1_translateX";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -0.98945084970062469 7 -0.4414648530767154 
		13 0.99573989599926771 19 0.54190403440179669 25 -0.98945084970062469;
	setAttr -s 5 ".kit[4]"  3;
	setAttr -s 5 ".kot[4]"  3;
	setAttr -s 5 ".kix[0:4]"  0.49117833375930786 0.14078225195407867 
		0.56233423948287964 0.17411035299301147 1;
	setAttr -s 5 ".kiy[0:4]"  -0.87105906009674072 0.99004060029983521 
		0.82690995931625366 -0.98472613096237183 0;
	setAttr -s 5 ".kox[0:4]"  0.49117833375930786 0.14078222215175629 
		0.56233423948287964 0.17411027848720551 1;
	setAttr -s 5 ".koy[0:4]"  -0.87105906009674072 0.99004060029983521 
		0.82690995931625366 -0.98472625017166138 0;
createNode animCurveTL -n "cc_thoracic01_outPutAnimBank_1_translateY";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 -3.0386711198895404 4 -3.8433676180077887 
		7 -4.6028834013789153 10 -3.2696571014295319 13 -3.0386711198895404 16 -3.8528202457169436 
		19 -4.6028834013789153 22 -3.3047865371776024 25 -3.0386711198895404;
	setAttr -s 9 ".kit[1:8]"  10 3 9 3 10 3 9 3;
	setAttr -s 9 ".kot[1:8]"  10 3 9 3 10 3 9 3;
createNode animCurveTL -n "cc_thoracic01_outPutAnimBank_1_translateZ";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 7 1.0770323049456243 13 0 19 1.0770323049456243 
		25 0;
	setAttr -s 5 ".kit[1:4]"  10 3 10 3;
	setAttr -s 5 ".kot[1:4]"  10 3 10 3;
createNode animCurveTA -n "cc_thoracic01_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -1.217054033060309 7 0.57361421422993575 
		13 -1.217054033060309 19 0.57361421422993575 25 -1.217054033060309;
createNode animCurveTA -n "cc_thoracic01_outPutAnimBank_1_rotateY";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 7 -2.0180040220381543 13 0 19 2.1569449219353558 
		25 0;
	setAttr -s 5 ".kit[1:4]"  10 9 10 9;
	setAttr -s 5 ".kot[1:4]"  10 9 10 9;
createNode animCurveTA -n "cc_thoracic01_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 4 0 13 0 16 0 25 0;
	setAttr -s 5 ".kit[0:4]"  3 9 10 9 3;
	setAttr -s 5 ".kot[0:4]"  3 9 10 9 3;
createNode animCurveTU -n "cc_thoracic01_outPutAnimBank_1_lock";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 13 0 25 0;
createNode animCurveTL -n "cc_r_carpalFT01_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 8.8448402032063527 13 8.8448402032063527 
		25 8.8448402032063527;
createNode animCurveTL -n "cc_r_carpalFT01_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 13 0 25 0;
createNode animCurveTL -n "cc_r_carpalFT01_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 19.579380413640436 13 19.579380413640436 
		25 19.579380413640436;
createNode animCurveTL -n "cc_r_tarsalFT01_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 13 0 25 0;
createNode animCurveTL -n "cc_r_tarsalFT01_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 13 0 25 0;
createNode animCurveTL -n "cc_r_tarsalFT01_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 13 0 25 0;
createNode animCurveTL -n "cc_l_carpalFT01_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 -8.3170185973915078 13 -8.3170185973915078 
		25 -8.3170185973915078;
createNode animCurveTL -n "cc_l_carpalFT01_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 13 0 25 0;
createNode animCurveTL -n "cc_l_carpalFT01_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 19.579380413640436 13 19.579380413640436 
		25 19.579380413640436;
createNode animCurveTL -n "cc_l_tarsalFT01_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 13 0 25 0;
createNode animCurveTL -n "cc_l_tarsalFT01_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 13 0 25 0;
createNode animCurveTL -n "cc_l_tarsalFT01_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 13 0 25 0;
createNode animCurveTL -n "cc_COG01_outPutAnimBank_1_translateX";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 7 0 13 0 19 0 25 0;
createNode animCurveTL -n "cc_COG01_outPutAnimBank_1_translateY";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -5.3722466960352442 7 -5.3722466960352442 
		13 -5.3722466960352442 19 -5.3722466960352442 25 -5.3722466960352442;
	setAttr -s 5 ".kit[1:4]"  10 3 10 3;
	setAttr -s 5 ".kot[1:4]"  10 3 10 3;
createNode animCurveTL -n "cc_COG01_outPutAnimBank_1_translateZ";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 13 0 25 0;
createNode animCurveTA -n "cc_COG01_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -5 7 -5 13 -5 19 -5 25 -5;
createNode animCurveTA -n "cc_COG01_outPutAnimBank_1_rotateY";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 7 0 13 0 19 0 25 0;
createNode animCurveTA -n "cc_COG01_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 7 0 13 0 19 0 25 0;
createNode animCurveTU -n "cc_COG01_outPutAnimBank_1_tr_curl";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -0.81414972518439566 7 -0.00055947829732994059 
		13 -0.81414972518439566 19 -0.25302513099135671 25 -0.81414972518439566;
	setAttr -s 5 ".kit[1:4]"  10 3 10 3;
	setAttr -s 5 ".kot[1:4]"  10 3 10 3;
createNode animCurveTU -n "cc_COG01_outPutAnimBank_1_tr_sway";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 7 0 13 0 19 0 25 0;
createNode animCurveTU -n "cc_COG01_outPutAnimBank_1_tr_turn";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 7 0 13 0 19 0 25 0;
createNode animCurveTL -n "cc_head01_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 7 0 13 0 19 0 25 0;
createNode animCurveTL -n "cc_head01_outPutAnimBank_1_translateY";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -0.19426945383147207 7 1.2088014352219527 
		13 -0.19426945383147207 19 1.2088014352219527 25 -0.19426945383147207;
	setAttr -s 5 ".kit[1:4]"  10 3 10 3;
	setAttr -s 5 ".kot[1:4]"  10 3 10 3;
createNode animCurveTL -n "cc_head01_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 2.7044654209746009 7 0.11220682606280524 
		13 2.7707741332928646 19 0.11220682606280524 25 2.7044654209746009;
	setAttr -s 5 ".kit[0:4]"  3 10 10 10 3;
	setAttr -s 5 ".kot[0:4]"  3 10 10 10 3;
createNode animCurveTA -n "cc_head01_outPutAnimBank_1_rotateX";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 0.5844409412574223 4 2.2880959578607278 
		10 -1.1192140753458792 16 2.3004831463590034 22 -1.1192140753458792 25 0.5844409412574223;
	setAttr -s 6 ".kit[0:5]"  9 3 3 3 3 9;
	setAttr -s 6 ".kot[0:5]"  9 3 3 3 3 9;
createNode animCurveTA -n "cc_head01_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -0.48572742239509686 7 -0.080927392031969664 
		13 -0.48572742239509686 19 -0.080927369411997505 25 -0.48572742239509686;
	setAttr -s 5 ".kit[0:4]"  3 10 10 10 3;
	setAttr -s 5 ".kot[0:4]"  3 10 10 10 3;
createNode animCurveTA -n "cc_head01_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 7 0 13 0 19 0 25 0;
createNode animCurveTU -n "cc_head01_outPutAnimBank_1_ear_r_rootCurl";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -3.9945963533761408 7 -3.9945963533761408 
		13 -3.9945963533761408 19 -3.9945963533761408 25 -3.9945963533761408;
createNode animCurveTU -n "cc_head01_outPutAnimBank_1_ear_r_rootTurn";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 7 0 13 0 19 0 25 0;
createNode animCurveTU -n "cc_head01_outPutAnimBank_1_ear_r_rootSway";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 7 0 13 0 19 0 25 0;
createNode animCurveTU -n "cc_head01_outPutAnimBank_1_ear_r_midCurl";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -3.9945963533761408 7 -3.9945963533761408 
		13 -3.9945963533761408 19 -3.9945963533761408 25 -3.9945963533761408;
createNode animCurveTU -n "cc_head01_outPutAnimBank_1_ear_r_midTurn";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 7 0 13 0 19 0 25 0;
createNode animCurveTU -n "cc_head01_outPutAnimBank_1_ear_r_midSway";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 7 0 13 0 19 0 25 0;
createNode animCurveTU -n "cc_head01_outPutAnimBank_1_ear_l_rootCurl";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -6.6234995315938452 7 -6.6234995315938452 
		13 -6.6234995315938452 19 -6.6234995315938452 25 -6.6234995315938452;
createNode animCurveTU -n "cc_head01_outPutAnimBank_1_ear_l_rootTurn";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 7 0 13 0 19 0 25 0;
createNode animCurveTU -n "cc_head01_outPutAnimBank_1_ear_l_rootSway";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 7 0 13 0 19 0 25 0;
createNode animCurveTU -n "cc_head01_outPutAnimBank_1_ear_l_midCurl";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -6.6234995315938452 7 -6.6234995315938452 
		13 -6.6234995315938452 19 -6.6234995315938452 25 -6.6234995315938452;
createNode animCurveTU -n "cc_head01_outPutAnimBank_1_ear_l_midTurn";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 7 0 13 0 19 0 25 0;
createNode animCurveTU -n "cc_head01_outPutAnimBank_1_ear_l_midSway";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 7 0 13 0 19 0 25 0;
createNode animCurveTL -n "cc_cervical02_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 7 0 13 0 19 0 25 0;
createNode animCurveTL -n "cc_cervical02_outPutAnimBank_1_translateY";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -1.0551884603639863 7 0.082071311430694377 
		13 -1.0551884603639863 19 0.082071311430694377 25 -1.0551884603639863;
	setAttr -s 5 ".kit[1:4]"  10 3 10 3;
	setAttr -s 5 ".kot[1:4]"  10 3 10 3;
createNode animCurveTL -n "cc_cervical02_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 2.9933077137421598 7 0.11220682606280524 
		13 3.0596164260604213 19 0.11220682606280524 25 2.9933077137421598;
	setAttr -s 5 ".kit[0:4]"  3 10 10 10 3;
	setAttr -s 5 ".kot[0:4]"  3 10 10 10 3;
createNode animCurveTA -n "cc_cervical02_outPutAnimBank_1_rotateX";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 8.1386140700236087 7 7.3686350070138449 
		13 8.1386140700236087 19 7.3137294303660854 25 8.1386140700236087;
	setAttr -s 5 ".kit[2:4]"  10 10 3;
	setAttr -s 5 ".kot[2:4]"  10 10 3;
createNode animCurveTA -n "cc_cervical02_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -0.54138786416585649 7 -0.083787809165405069 
		13 -0.54138786416585649 19 -0.083787783595000664 25 -0.54138786416585649;
	setAttr -s 5 ".kit[0:4]"  3 10 10 10 3;
	setAttr -s 5 ".kot[0:4]"  3 10 10 10 3;
createNode animCurveTA -n "cc_cervical02_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 7 0 13 0 19 0 25 0;
createNode animCurveTL -n "cc_cervical01_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 7 0 13 0 19 0 25 0;
createNode animCurveTL -n "cc_cervical01_outPutAnimBank_1_translateY";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -1.0551884603639863 7 0.082071311430694377 
		13 -1.0551884603639863 19 0.082071311430694377 25 -1.0551884603639863;
	setAttr -s 5 ".kit[1:4]"  10 3 10 3;
	setAttr -s 5 ".kot[1:4]"  10 3 10 3;
createNode animCurveTL -n "cc_cervical01_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 3.1128870102628388 7 0.11220682606280524 
		13 3.0596164260604226 19 0.11220682606280524 25 3.1128870102628388;
	setAttr -s 5 ".kit[0:4]"  3 10 10 10 3;
	setAttr -s 5 ".kot[0:4]"  3 10 10 10 3;
createNode animCurveTA -n "cc_cervical01_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 1.1108709023978083 7 0.0037670928128737823 
		13 1.1108709023978083 19 0.025449863949513235 25 1.1108709023978083;
	setAttr -s 5 ".kit[0:4]"  3 10 10 10 3;
	setAttr -s 5 ".kot[0:4]"  3 10 10 10 3;
createNode animCurveTA -n "cc_cervical01_outPutAnimBank_1_rotateY";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 7 1.950244201251025 13 0 19 -1.8138169112392084 
		25 0;
	setAttr -s 5 ".kit[1:4]"  10 9 10 9;
	setAttr -s 5 ".kot[1:4]"  10 9 10 9;
createNode animCurveTA -n "cc_cervical01_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 7 0 13 0 19 0 25 0;
createNode animCurveTL -n "cc_tail01_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  4 -1.8391218562669822 10 -1.8391218562669822 
		16 -1.8391218562669822 22 -1.8391218562669822 28 -1.8391218562669822;
	setAttr -s 5 ".kit[0:4]"  3 10 10 10 3;
	setAttr -s 5 ".kot[0:4]"  3 10 10 10 3;
createNode animCurveTL -n "cc_tail01_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  4 3.1485102887614751 10 3.1485102887614751 
		16 3.1485102887614751 22 3.1485102887614751 28 3.1485102887614751;
	setAttr -s 5 ".kit[0:4]"  3 10 10 10 3;
	setAttr -s 5 ".kot[0:4]"  3 10 10 10 3;
createNode animCurveTL -n "cc_tail01_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  4 -2.5315030978858957 10 -3.3135925901095415 
		16 -2.5315030978858957 22 -3.3135925901095415 28 -2.5315030978858957;
	setAttr -s 5 ".kit[0:4]"  3 10 10 10 3;
	setAttr -s 5 ".kot[0:4]"  3 10 10 10 3;
createNode animCurveTL -n "cc_tail02_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  4 0 10 0 16 0 22 0 28 0;
	setAttr -s 5 ".kit[0:4]"  3 10 10 10 3;
	setAttr -s 5 ".kot[0:4]"  3 10 10 10 3;
createNode animCurveTL -n "cc_tail02_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  4 0 10 0 16 0 22 0 28 0;
	setAttr -s 5 ".kit[0:4]"  3 10 10 10 3;
	setAttr -s 5 ".kot[0:4]"  3 10 10 10 3;
createNode animCurveTL -n "cc_tail02_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  4 -4.8336550371564577 10 -11.56862946378207 
		16 -4.8336550371564577 22 -11.26343356763428 28 -4.8336550371564577;
	setAttr -s 5 ".kit[0:4]"  3 10 10 10 3;
	setAttr -s 5 ".kot[0:4]"  3 10 10 10 3;
createNode animCurveTL -n "cc_tail03_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  4 -0.25074067449667858 10 5.2089239285828395 
		16 -0.25074067449667858 22 -6.0704520879729422 28 -0.25074067449667858;
	setAttr -s 5 ".kit[0:4]"  9 10 10 10 9;
	setAttr -s 5 ".kot[0:4]"  9 10 10 10 9;
createNode animCurveTL -n "cc_tail03_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  4 0 10 0 16 0 22 0 28 0;
	setAttr -s 5 ".kit[0:4]"  9 10 10 10 9;
	setAttr -s 5 ".kot[0:4]"  9 10 10 10 9;
createNode animCurveTL -n "cc_tail03_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  4 -1.863951359699656 10 -12.360678087214744 
		16 -1.863951359699656 22 -11.698978996922236 28 -1.863951359699656;
	setAttr -s 5 ".kit[0:4]"  3 10 10 10 3;
	setAttr -s 5 ".kot[0:4]"  3 10 10 10 3;
createNode animCurveTL -n "cc_cc_tail04_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  4 -0.25074067449667858 10 5.2089239285828395 
		16 -0.25074067449667858 22 -6.0704520879729422 28 -0.25074067449667858;
	setAttr -s 5 ".kit[0:4]"  9 10 10 10 9;
	setAttr -s 5 ".kot[0:4]"  9 10 10 10 9;
createNode animCurveTL -n "cc_cc_tail04_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  4 0 10 0 16 0 22 0 28 0;
	setAttr -s 5 ".kit[0:4]"  9 10 10 10 9;
	setAttr -s 5 ".kot[0:4]"  9 10 10 10 9;
createNode animCurveTL -n "cc_cc_tail04_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  4 -0.34479311843182714 10 -10.471858424553243 
		16 -0.34479311843182714 22 -9.8101593342607281 28 -0.34479311843182714;
	setAttr -s 5 ".kit[0:4]"  3 10 10 10 3;
	setAttr -s 5 ".kot[0:4]"  3 10 10 10 3;
createNode animCurveTL -n "cc_tail05_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  4 -9.8445213648190713 7 0 13 11.868835351802302 
		19 0 25 -15.751230612299084 28 -9.8445213648190713;
	setAttr -s 6 ".kit[1:5]"  9 10 9 10 10;
	setAttr -s 6 ".kot[1:5]"  9 10 9 10 10;
createNode animCurveTL -n "cc_tail05_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  4 0 10 0 16 0 22 0 28 0;
	setAttr -s 5 ".kit[0:4]"  3 10 10 10 3;
	setAttr -s 5 ".kot[0:4]"  3 10 10 10 3;
createNode animCurveTL -n "cc_tail05_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  4 -9.900649120150856 10 -4.4300665042810374 
		16 -11.186763249875074 22 -5.3708445383536043 28 -9.900649120150856;
	setAttr -s 5 ".kit[0:4]"  3 10 10 10 3;
	setAttr -s 5 ".kot[0:4]"  3 10 10 10 3;
createNode animCurveTL -n "cc_tail06_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  4 -9.8445213648190713 7 0 13 11.868835351802302 
		19 0 25 -15.751230612299084 28 -9.8445213648190713;
	setAttr -s 6 ".kit[1:5]"  9 10 9 10 10;
	setAttr -s 6 ".kot[1:5]"  9 10 9 10 10;
createNode animCurveTL -n "cc_tail06_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  4 0 10 0 16 0 22 0 28 0;
	setAttr -s 5 ".kit[0:4]"  3 10 10 10 3;
	setAttr -s 5 ".kot[0:4]"  3 10 10 10 3;
createNode animCurveTL -n "cc_tail06_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  4 -10.44875057706475 10 -4.7041172327535445 
		16 -11.46081397834757 22 -5.6448952668261061 28 -10.44875057706475;
	setAttr -s 5 ".kit[0:4]"  3 10 10 10 3;
	setAttr -s 5 ".kot[0:4]"  3 10 10 10 3;
createNode animCurveTL -n "cc_r_shoulder01_outPutAnimBank_1_translateX";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 1.8939239294630301 4 3 8 0 13 0 19 0 
		25 1.8939239294630301;
	setAttr -s 6 ".kit[0:5]"  9 1 1 10 10 9;
	setAttr -s 6 ".kot[0:5]"  9 1 1 10 10 9;
	setAttr -s 6 ".kix[1:5]"  0.12500001490116119 1 1 1 0.13086585700511932;
	setAttr -s 6 ".kiy[1:5]"  0.66042482852935791 0 0 0 0.99140012264251709;
	setAttr -s 6 ".kox[1:5]"  0.1666666567325592 1 1 1 0.13086585700511932;
	setAttr -s 6 ".koy[1:5]"  0.88056647777557373 0 0 0 0.99140012264251709;
createNode animCurveTL -n "cc_r_shoulder01_outPutAnimBank_1_translateY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  1 12.616470365985618 4 14.734634080532707 
		8 -0.016084590268173882 13 -9.870534599376068 19 0 22 8.0394629457511684 25 12.616470365985618;
	setAttr -s 7 ".kit[1:6]"  3 1 10 1 1 9;
	setAttr -s 7 ".kot[1:6]"  3 1 10 1 1 9;
	setAttr -s 7 ".kix[0:6]"  0.035621229559183121 1 0.01079144049435854 
		0.99938476085662842 0.025969140231609344 0.024829288944602013 0.027300229296088219;
	setAttr -s 7 ".kiy[0:6]"  0.99936538934707642 0 -0.99994176626205444 
		0.035072058439254761 0.99966275691986084 0.99969172477722168 0.99962729215621948;
	setAttr -s 7 ".kox[0:6]"  0.035621229559183121 1 0.010791442357003689 
		0.99938476085662842 0.025969134643673897 0.024829264730215073 0.027300229296088219;
	setAttr -s 7 ".koy[0:6]"  0.99936538934707642 0 -0.99994176626205444 
		0.035072058439254761 0.99966275691986084 0.99969172477722168 0.99962729215621948;
createNode animCurveTL -n "cc_r_shoulder01_outPutAnimBank_1_translateZ";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 -3.68057898273605 4 -5.7104178077395664 
		8 -3.6652174926504641 13 0 19 0 25 -3.68057898273605;
	setAttr -s 6 ".kit[0:5]"  9 1 9 1 1 9;
	setAttr -s 6 ".kot[0:5]"  9 1 9 1 1 9;
	setAttr -s 6 ".kix[1:5]"  0.15431617200374603 0.065528303384780884 
		1 0.24999994039535522 0.067767933011054993;
	setAttr -s 6 ".kiy[1:5]"  -0.98802155256271362 0.99785071611404419 
		0 0 -0.99770110845565796;
	setAttr -s 6 ".kox[1:5]"  0.15431617200374603 0.065528303384780884 
		1 0.24999994039535522 0.067767933011054993;
	setAttr -s 6 ".koy[1:5]"  -0.98802155256271362 0.99785071611404419 
		0 0 -0.99770110845565796;
createNode animCurveTA -n "cc_r_shoulder01_outPutAnimBank_1_rotateX";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 6.0000000000000009 8 18.174953882505623 
		13 5.4579410119842136 19 -10.199694917816291 25 6.0000000000000009;
	setAttr -s 5 ".kit[2:4]"  9 3 9;
	setAttr -s 5 ".kot[2:4]"  9 3 9;
	setAttr -s 5 ".kix[0:4]"  0.70927619934082031 0.99131536483764648 
		0.67923730611801147 1 0.66240376234054565;
	setAttr -s 5 ".kiy[0:4]"  0.70493072271347046 -0.13150645792484283 
		-0.73391866683959961 0 0.74914705753326416;
	setAttr -s 5 ".kox[0:4]"  0.70927625894546509 0.99131536483764648 
		0.67923730611801147 1 0.66240376234054565;
	setAttr -s 5 ".koy[0:4]"  0.70493072271347046 -0.13150645792484283 
		-0.73391866683959961 0 0.74914705753326416;
createNode animCurveTA -n "cc_r_shoulder01_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 0 13 0 19 0 25 0;
createNode animCurveTA -n "cc_r_shoulder01_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 2.5 13 0 19 1.2500002235174446 25 2.5;
	setAttr -s 4 ".kit[0:3]"  3 10 10 3;
	setAttr -s 4 ".kot[0:3]"  3 10 10 3;
createNode animCurveTL -n "cc_l_shoulder01_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 0 7 0 13 -2.1090508177258145 16 -2.9900467289277368 
		20 0 25 0;
	setAttr -s 6 ".kit[3:5]"  3 10 10;
	setAttr -s 6 ".kot[3:5]"  3 10 10;
createNode animCurveTL -n "cc_l_shoulder01_outPutAnimBank_1_translateY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  1 -10.656831656765412 7 0 10 8.0514258918329684 
		13 12.991219407692384 16 14.773490541862945 20 0 25 -10.656831656765412;
	setAttr -s 7 ".kit[0:6]"  3 9 1 10 1 1 3;
	setAttr -s 7 ".kot[0:6]"  3 9 1 10 1 1 3;
	setAttr -s 7 ".kix[2:6]"  0.021480295807123184 0.037165265530347824 
		0.084654070436954498 0.010151281952857971 1;
	setAttr -s 7 ".kiy[2:6]"  0.99976927042007446 0.99930912256240845 
		-0.99641042947769165 -0.99994850158691406 0;
	setAttr -s 7 ".kox[2:6]"  0.021480297669768333 0.037165265530347824 
		0.084654062986373901 0.010151289403438568 1;
	setAttr -s 7 ".koy[2:6]"  0.99976927042007446 0.99930912256240845 
		-0.99641042947769165 -0.99994850158691406 0;
createNode animCurveTL -n "cc_l_shoulder01_outPutAnimBank_1_translateZ";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 0 7 0 13 -3.5684186270671163 16 -5.4847028285464505 
		20 -3.4985677952703615 25 0;
	setAttr -s 6 ".kit[0:5]"  10 1 1 1 10 3;
	setAttr -s 6 ".kot[0:5]"  10 1 1 1 10 3;
	setAttr -s 6 ".kix[1:5]"  1 0.25000002980232239 0.15300233662128448 
		0.068212717771530151 1;
	setAttr -s 6 ".kiy[1:5]"  0 -3.2493295669555664 -0.98822581768035889 
		0.99767076969146729 0;
	setAttr -s 6 ".kox[1:5]"  1 0.12500005960464478 0.15300232172012329 
		0.068212717771530151 1;
	setAttr -s 6 ".koy[1:5]"  0 -1.6246644258499146 -0.98822587728500366 
		0.99767076969146729 0;
createNode animCurveTA -n "cc_l_shoulder01_outPutAnimBank_1_rotateX";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 6.4351430841702744 7 -10.161991121137792 
		13 5.1145243115617012 20 17.994917450165833 25 6.4351430841702744;
	setAttr -s 5 ".kit[1:4]"  3 9 3 9;
	setAttr -s 5 ".kot[1:4]"  3 9 3 9;
createNode animCurveTA -n "cc_l_shoulder01_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 7 0 13 0 20 0 25 0;
createNode animCurveTA -n "cc_l_shoulder01_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 13 -2.5 25 0;
	setAttr -s 3 ".kit[1:2]"  10 3;
	setAttr -s 3 ".kot[1:2]"  10 3;
createNode animCurveTU -n "cc_global01_outPutAnimBank_1_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 1 75 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTL -n "cc_global01_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 75 0;
createNode animCurveTL -n "cc_global01_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 75 0;
createNode animCurveTL -n "cc_global01_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 75 62.799584123621557;
createNode animCurveTA -n "cc_global01_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 75 0;
createNode animCurveTA -n "cc_global01_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 75 0;
createNode animCurveTA -n "cc_global01_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 75 0;
createNode animCurveTU -n "cc_global01_outPutAnimBank_1_scaleX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0.15 75 0.15;
createNode animCurveTU -n "cc_global01_outPutAnimBank_1_scaleY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0.15 75 0.15;
createNode animCurveTU -n "cc_global01_outPutAnimBank_1_scaleZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0.15 75 0.15;
createNode animCurveTU -n "cc_global01_outPutAnimBank_1_vis_head_cervix";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 1 75 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "cc_global01_outPutAnimBank_1_vis_upperBody";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 1 75 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "cc_global01_outPutAnimBank_1_vis_ft_legs";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 1 75 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "cc_global01_outPutAnimBank_1_vis_bk_legs";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 1 75 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "cc_global01_outPutAnimBank_1_vis_tail";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 1 75 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
select -ne :time1;
	setAttr -k on ".cch";
	setAttr -k on ".nds";
	setAttr ".o" 75;
	setAttr ".unw" 75;
select -ne :renderPartition;
	setAttr -k on ".cch";
	setAttr -k on ".nds";
	setAttr -s 5 ".st";
select -ne :initialShadingGroup;
	setAttr -k on ".cch";
	setAttr -k on ".nds";
	setAttr -k on ".mwc";
	setAttr ".ro" yes;
	setAttr -av ".micc";
select -ne :initialParticleSE;
	setAttr -k on ".cch";
	setAttr -k on ".nds";
	setAttr -k on ".mwc";
	setAttr ".ro" yes;
select -ne :defaultShaderList1;
	setAttr -k on ".cch";
	setAttr -k on ".nds";
	setAttr -s 5 ".s";
select -ne :defaultTextureList1;
select -ne :lambert1;
	setAttr ".c" -type "float3" 0.697047 0.87900001 0.78471804 ;
select -ne :postProcessList1;
	setAttr -k on ".cch";
	setAttr -k on ".nds";
	setAttr -s 2 ".p";
select -ne :defaultRenderUtilityList1;
select -ne :renderGlobalsList1;
	setAttr -k on ".cch";
	setAttr -k on ".nds";
select -ne :defaultRenderGlobals;
	setAttr ".ren" -type "string" "mentalRay";
	setAttr ".pram" -type "string" "";
select -ne :defaultResolution;
	setAttr ".w" 720;
	setAttr ".h" 405;
	setAttr ".pa" 1;
	setAttr ".dar" 1.7777777910232544;
select -ne :defaultLightSet;
	setAttr -k on ".cch";
	setAttr -k on ".nds";
	setAttr -k on ".mwc";
	setAttr ".ro" yes;
select -ne :hardwareRenderGlobals;
	setAttr -k on ".cch";
	setAttr -k on ".nds";
	setAttr ".ctrs" 256;
	setAttr ".btrs" 512;
	setAttr -k on ".hwcc";
	setAttr -k on ".hwdp";
	setAttr -k on ".hwql";
select -ne :defaultHardwareRenderGlobals;
	setAttr -k on ".cch";
	setAttr -k on ".nds";
	setAttr -k on ".rp";
	setAttr -k on ".cai";
	setAttr -k on ".coi";
	setAttr -k on ".bcb";
	setAttr -k on ".bcg";
	setAttr -k on ".bcr";
	setAttr -k on ".ei";
	setAttr -k on ".ex";
	setAttr -k on ".es";
	setAttr -k on ".fii";
	setAttr -k on ".gr";
	setAttr -k on ".li";
	setAttr -k on ".ls";
	setAttr -k on ".mb";
	setAttr -k on ".ti";
	setAttr -k on ".txt";
	setAttr -k on ".mpr";
	setAttr -k on ".wzd";
	setAttr ".fn" -type "string" "im";
	setAttr -k on ".if";
	setAttr ".res" -type "string" "ntsc_4d 646 485 1.333";
	setAttr -k on ".as";
	setAttr -k on ".ds";
	setAttr -k on ".lm";
	setAttr -k on ".fir";
	setAttr -k on ".aap";
	setAttr -k on ".gh";
select -ne :characterPartition;
select -ne :ikSystem;
	setAttr -s 2 ".sol";
connectAttr "cc_r_legFT01_outPutAnimBank_1_translateX.o" "cc_r_legFT01_outPutAnimBank_1.tx"
		;
connectAttr "cc_r_legFT01_outPutAnimBank_1_translateY.o" "cc_r_legFT01_outPutAnimBank_1.ty"
		;
connectAttr "cc_r_legFT01_outPutAnimBank_1_translateZ.o" "cc_r_legFT01_outPutAnimBank_1.tz"
		;
connectAttr "cc_r_legFT01_outPutAnimBank_1_rotateX.o" "cc_r_legFT01_outPutAnimBank_1.rx"
		;
connectAttr "cc_r_legFT01_outPutAnimBank_1_rotateY.o" "cc_r_legFT01_outPutAnimBank_1.ry"
		;
connectAttr "cc_r_legFT01_outPutAnimBank_1_rotateZ.o" "cc_r_legFT01_outPutAnimBank_1.rz"
		;
connectAttr "cc_r_legFT01_outPutAnimBank_1_fetlock_ft_curl.o" "cc_r_legFT01_outPutAnimBank_1.fetlock_ft_curl"
		;
connectAttr "cc_r_legFT01_outPutAnimBank_1_hoof_ft_curl.o" "cc_r_legFT01_outPutAnimBank_1.hoof_ft_curl"
		;
connectAttr "cc_r_legBK01_outPutAnimBank_1_translateX.o" "cc_r_legBK01_outPutAnimBank_1.tx"
		;
connectAttr "cc_r_legBK01_outPutAnimBank_1_translateY.o" "cc_r_legBK01_outPutAnimBank_1.ty"
		;
connectAttr "cc_r_legBK01_outPutAnimBank_1_translateZ.o" "cc_r_legBK01_outPutAnimBank_1.tz"
		;
connectAttr "cc_r_legBK01_outPutAnimBank_1_rotateX.o" "cc_r_legBK01_outPutAnimBank_1.rx"
		;
connectAttr "cc_r_legBK01_outPutAnimBank_1_rotateY.o" "cc_r_legBK01_outPutAnimBank_1.ry"
		;
connectAttr "cc_r_legBK01_outPutAnimBank_1_rotateZ.o" "cc_r_legBK01_outPutAnimBank_1.rz"
		;
connectAttr "cc_r_legBK01_outPutAnimBank_1_fetlock_bk_curl.o" "cc_r_legBK01_outPutAnimBank_1.fetlock_bk_curl"
		;
connectAttr "cc_r_legBK01_outPutAnimBank_1_hoof_bk_curl.o" "cc_r_legBK01_outPutAnimBank_1.hoof_bk_curl"
		;
connectAttr "cc_l_legFT01_outPutAnimBank_1_translateX.o" "cc_l_legFT01_outPutAnimBank_1.tx"
		;
connectAttr "cc_l_legFT01_outPutAnimBank_1_translateY.o" "cc_l_legFT01_outPutAnimBank_1.ty"
		;
connectAttr "cc_l_legFT01_outPutAnimBank_1_translateZ.o" "cc_l_legFT01_outPutAnimBank_1.tz"
		;
connectAttr "cc_l_legFT01_outPutAnimBank_1_rotateX.o" "cc_l_legFT01_outPutAnimBank_1.rx"
		;
connectAttr "cc_l_legFT01_outPutAnimBank_1_rotateY.o" "cc_l_legFT01_outPutAnimBank_1.ry"
		;
connectAttr "cc_l_legFT01_outPutAnimBank_1_rotateZ.o" "cc_l_legFT01_outPutAnimBank_1.rz"
		;
connectAttr "cc_l_legFT01_outPutAnimBank_1_fetlock_ft_curl.o" "cc_l_legFT01_outPutAnimBank_1.fetlock_ft_curl"
		;
connectAttr "cc_l_legFT01_outPutAnimBank_1_hoof_ft_curl.o" "cc_l_legFT01_outPutAnimBank_1.hoof_ft_curl"
		;
connectAttr "cc_l_legBK01_outPutAnimBank_1_translateX.o" "cc_l_legBK01_outPutAnimBank_1.tx"
		;
connectAttr "cc_l_legBK01_outPutAnimBank_1_translateY.o" "cc_l_legBK01_outPutAnimBank_1.ty"
		;
connectAttr "cc_l_legBK01_outPutAnimBank_1_translateZ.o" "cc_l_legBK01_outPutAnimBank_1.tz"
		;
connectAttr "cc_l_legBK01_outPutAnimBank_1_rotateX.o" "cc_l_legBK01_outPutAnimBank_1.rx"
		;
connectAttr "cc_l_legBK01_outPutAnimBank_1_rotateY.o" "cc_l_legBK01_outPutAnimBank_1.ry"
		;
connectAttr "cc_l_legBK01_outPutAnimBank_1_rotateZ.o" "cc_l_legBK01_outPutAnimBank_1.rz"
		;
connectAttr "cc_l_legBK01_outPutAnimBank_1_fetlock_bk_curl.o" "cc_l_legBK01_outPutAnimBank_1.fetlock_bk_curl"
		;
connectAttr "cc_l_legBK01_outPutAnimBank_1_hoof_bk_curl.o" "cc_l_legBK01_outPutAnimBank_1.hoof_bk_curl"
		;
connectAttr "cc_hipSway01_outPutAnimBank_1_translateX.o" "cc_hipSway01_outPutAnimBank_1.tx"
		;
connectAttr "cc_hipSway01_outPutAnimBank_1_translateY.o" "cc_hipSway01_outPutAnimBank_1.ty"
		;
connectAttr "cc_hipSway01_outPutAnimBank_1_translateZ.o" "cc_hipSway01_outPutAnimBank_1.tz"
		;
connectAttr "cc_hipSway01_outPutAnimBank_1_rotateX.o" "cc_hipSway01_outPutAnimBank_1.rx"
		;
connectAttr "cc_hipSway01_outPutAnimBank_1_rotateY.o" "cc_hipSway01_outPutAnimBank_1.ry"
		;
connectAttr "cc_hipSway01_outPutAnimBank_1_rotateZ.o" "cc_hipSway01_outPutAnimBank_1.rz"
		;
connectAttr "cc_midVertebraet01_outPutAnimBank_1_translateX.o" "cc_midVertebraet01_outPutAnimBank_1.tx"
		;
connectAttr "cc_midVertebraet01_outPutAnimBank_1_translateY.o" "cc_midVertebraet01_outPutAnimBank_1.ty"
		;
connectAttr "cc_midVertebraet01_outPutAnimBank_1_translateZ.o" "cc_midVertebraet01_outPutAnimBank_1.tz"
		;
connectAttr "cc_midVertebraet01_outPutAnimBank_1_rotateX.o" "cc_midVertebraet01_outPutAnimBank_1.rx"
		;
connectAttr "cc_midVertebraet01_outPutAnimBank_1_rotateY.o" "cc_midVertebraet01_outPutAnimBank_1.ry"
		;
connectAttr "cc_midVertebraet01_outPutAnimBank_1_rotateZ.o" "cc_midVertebraet01_outPutAnimBank_1.rz"
		;
connectAttr "cc_thoracic01_outPutAnimBank_1_translateX.o" "cc_thoracic01_outPutAnimBank_1.tx"
		;
connectAttr "cc_thoracic01_outPutAnimBank_1_translateY.o" "cc_thoracic01_outPutAnimBank_1.ty"
		;
connectAttr "cc_thoracic01_outPutAnimBank_1_translateZ.o" "cc_thoracic01_outPutAnimBank_1.tz"
		;
connectAttr "cc_thoracic01_outPutAnimBank_1_rotateX.o" "cc_thoracic01_outPutAnimBank_1.rx"
		;
connectAttr "cc_thoracic01_outPutAnimBank_1_rotateY.o" "cc_thoracic01_outPutAnimBank_1.ry"
		;
connectAttr "cc_thoracic01_outPutAnimBank_1_rotateZ.o" "cc_thoracic01_outPutAnimBank_1.rz"
		;
connectAttr "cc_thoracic01_outPutAnimBank_1_lock.o" "cc_thoracic01_outPutAnimBank_1.lock"
		;
connectAttr "cc_r_carpalFT01_outPutAnimBank_1_translateX.o" "cc_r_carpalFT01_outPutAnimBank_1.tx"
		;
connectAttr "cc_r_carpalFT01_outPutAnimBank_1_translateY.o" "cc_r_carpalFT01_outPutAnimBank_1.ty"
		;
connectAttr "cc_r_carpalFT01_outPutAnimBank_1_translateZ.o" "cc_r_carpalFT01_outPutAnimBank_1.tz"
		;
connectAttr "cc_r_tarsalFT01_outPutAnimBank_1_translateX.o" "cc_r_tarsalFT01_outPutAnimBank_1.tx"
		;
connectAttr "cc_r_tarsalFT01_outPutAnimBank_1_translateY.o" "cc_r_tarsalFT01_outPutAnimBank_1.ty"
		;
connectAttr "cc_r_tarsalFT01_outPutAnimBank_1_translateZ.o" "cc_r_tarsalFT01_outPutAnimBank_1.tz"
		;
connectAttr "cc_l_carpalFT01_outPutAnimBank_1_translateX.o" "cc_l_carpalFT01_outPutAnimBank_1.tx"
		;
connectAttr "cc_l_carpalFT01_outPutAnimBank_1_translateY.o" "cc_l_carpalFT01_outPutAnimBank_1.ty"
		;
connectAttr "cc_l_carpalFT01_outPutAnimBank_1_translateZ.o" "cc_l_carpalFT01_outPutAnimBank_1.tz"
		;
connectAttr "cc_l_tarsalFT01_outPutAnimBank_1_translateX.o" "cc_l_tarsalFT01_outPutAnimBank_1.tx"
		;
connectAttr "cc_l_tarsalFT01_outPutAnimBank_1_translateY.o" "cc_l_tarsalFT01_outPutAnimBank_1.ty"
		;
connectAttr "cc_l_tarsalFT01_outPutAnimBank_1_translateZ.o" "cc_l_tarsalFT01_outPutAnimBank_1.tz"
		;
connectAttr "cc_COG01_outPutAnimBank_1_translateX.o" "cc_COG01_outPutAnimBank_1.tx"
		;
connectAttr "cc_COG01_outPutAnimBank_1_translateY.o" "cc_COG01_outPutAnimBank_1.ty"
		;
connectAttr "cc_COG01_outPutAnimBank_1_translateZ.o" "cc_COG01_outPutAnimBank_1.tz"
		;
connectAttr "cc_COG01_outPutAnimBank_1_rotateX.o" "cc_COG01_outPutAnimBank_1.rx"
		;
connectAttr "cc_COG01_outPutAnimBank_1_rotateY.o" "cc_COG01_outPutAnimBank_1.ry"
		;
connectAttr "cc_COG01_outPutAnimBank_1_rotateZ.o" "cc_COG01_outPutAnimBank_1.rz"
		;
connectAttr "cc_COG01_outPutAnimBank_1_tr_curl.o" "cc_COG01_outPutAnimBank_1.tr_curl"
		;
connectAttr "cc_COG01_outPutAnimBank_1_tr_sway.o" "cc_COG01_outPutAnimBank_1.tr_sway"
		;
connectAttr "cc_COG01_outPutAnimBank_1_tr_turn.o" "cc_COG01_outPutAnimBank_1.tr_turn"
		;
connectAttr "cc_head01_outPutAnimBank_1_translateX.o" "cc_head01_outPutAnimBank_1.tx"
		;
connectAttr "cc_head01_outPutAnimBank_1_translateY.o" "cc_head01_outPutAnimBank_1.ty"
		;
connectAttr "cc_head01_outPutAnimBank_1_translateZ.o" "cc_head01_outPutAnimBank_1.tz"
		;
connectAttr "cc_head01_outPutAnimBank_1_rotateX.o" "cc_head01_outPutAnimBank_1.rx"
		;
connectAttr "cc_head01_outPutAnimBank_1_rotateY.o" "cc_head01_outPutAnimBank_1.ry"
		;
connectAttr "cc_head01_outPutAnimBank_1_rotateZ.o" "cc_head01_outPutAnimBank_1.rz"
		;
connectAttr "cc_head01_outPutAnimBank_1_ear_r_rootCurl.o" "cc_head01_outPutAnimBank_1.ear_r_rootCurl"
		;
connectAttr "cc_head01_outPutAnimBank_1_ear_r_rootTurn.o" "cc_head01_outPutAnimBank_1.ear_r_rootTurn"
		;
connectAttr "cc_head01_outPutAnimBank_1_ear_r_rootSway.o" "cc_head01_outPutAnimBank_1.ear_r_rootSway"
		;
connectAttr "cc_head01_outPutAnimBank_1_ear_r_midCurl.o" "cc_head01_outPutAnimBank_1.ear_r_midCurl"
		;
connectAttr "cc_head01_outPutAnimBank_1_ear_r_midTurn.o" "cc_head01_outPutAnimBank_1.ear_r_midTurn"
		;
connectAttr "cc_head01_outPutAnimBank_1_ear_r_midSway.o" "cc_head01_outPutAnimBank_1.ear_r_midSway"
		;
connectAttr "cc_head01_outPutAnimBank_1_ear_l_rootCurl.o" "cc_head01_outPutAnimBank_1.ear_l_rootCurl"
		;
connectAttr "cc_head01_outPutAnimBank_1_ear_l_rootTurn.o" "cc_head01_outPutAnimBank_1.ear_l_rootTurn"
		;
connectAttr "cc_head01_outPutAnimBank_1_ear_l_rootSway.o" "cc_head01_outPutAnimBank_1.ear_l_rootSway"
		;
connectAttr "cc_head01_outPutAnimBank_1_ear_l_midCurl.o" "cc_head01_outPutAnimBank_1.ear_l_midCurl"
		;
connectAttr "cc_head01_outPutAnimBank_1_ear_l_midTurn.o" "cc_head01_outPutAnimBank_1.ear_l_midTurn"
		;
connectAttr "cc_head01_outPutAnimBank_1_ear_l_midSway.o" "cc_head01_outPutAnimBank_1.ear_l_midSway"
		;
connectAttr "cc_cervical02_outPutAnimBank_1_translateX.o" "cc_cervical02_outPutAnimBank_1.tx"
		;
connectAttr "cc_cervical02_outPutAnimBank_1_translateY.o" "cc_cervical02_outPutAnimBank_1.ty"
		;
connectAttr "cc_cervical02_outPutAnimBank_1_translateZ.o" "cc_cervical02_outPutAnimBank_1.tz"
		;
connectAttr "cc_cervical02_outPutAnimBank_1_rotateX.o" "cc_cervical02_outPutAnimBank_1.rx"
		;
connectAttr "cc_cervical02_outPutAnimBank_1_rotateY.o" "cc_cervical02_outPutAnimBank_1.ry"
		;
connectAttr "cc_cervical02_outPutAnimBank_1_rotateZ.o" "cc_cervical02_outPutAnimBank_1.rz"
		;
connectAttr "cc_cervical01_outPutAnimBank_1_translateX.o" "cc_cervical01_outPutAnimBank_1.tx"
		;
connectAttr "cc_cervical01_outPutAnimBank_1_translateY.o" "cc_cervical01_outPutAnimBank_1.ty"
		;
connectAttr "cc_cervical01_outPutAnimBank_1_translateZ.o" "cc_cervical01_outPutAnimBank_1.tz"
		;
connectAttr "cc_cervical01_outPutAnimBank_1_rotateX.o" "cc_cervical01_outPutAnimBank_1.rx"
		;
connectAttr "cc_cervical01_outPutAnimBank_1_rotateY.o" "cc_cervical01_outPutAnimBank_1.ry"
		;
connectAttr "cc_cervical01_outPutAnimBank_1_rotateZ.o" "cc_cervical01_outPutAnimBank_1.rz"
		;
connectAttr "cc_tail01_outPutAnimBank_1_translateX.o" "cc_tail01_outPutAnimBank_1.tx"
		;
connectAttr "cc_tail01_outPutAnimBank_1_translateY.o" "cc_tail01_outPutAnimBank_1.ty"
		;
connectAttr "cc_tail01_outPutAnimBank_1_translateZ.o" "cc_tail01_outPutAnimBank_1.tz"
		;
connectAttr "cc_tail02_outPutAnimBank_1_translateX.o" "cc_tail02_outPutAnimBank_1.tx"
		;
connectAttr "cc_tail02_outPutAnimBank_1_translateY.o" "cc_tail02_outPutAnimBank_1.ty"
		;
connectAttr "cc_tail02_outPutAnimBank_1_translateZ.o" "cc_tail02_outPutAnimBank_1.tz"
		;
connectAttr "cc_tail03_outPutAnimBank_1_translateX.o" "cc_tail03_outPutAnimBank_1.tx"
		;
connectAttr "cc_tail03_outPutAnimBank_1_translateY.o" "cc_tail03_outPutAnimBank_1.ty"
		;
connectAttr "cc_tail03_outPutAnimBank_1_translateZ.o" "cc_tail03_outPutAnimBank_1.tz"
		;
connectAttr "cc_cc_tail04_outPutAnimBank_1_translateX.o" "cc_cc_tail04_outPutAnimBank_1.tx"
		;
connectAttr "cc_cc_tail04_outPutAnimBank_1_translateY.o" "cc_cc_tail04_outPutAnimBank_1.ty"
		;
connectAttr "cc_cc_tail04_outPutAnimBank_1_translateZ.o" "cc_cc_tail04_outPutAnimBank_1.tz"
		;
connectAttr "cc_tail05_outPutAnimBank_1_translateX.o" "cc_tail05_outPutAnimBank_1.tx"
		;
connectAttr "cc_tail05_outPutAnimBank_1_translateY.o" "cc_tail05_outPutAnimBank_1.ty"
		;
connectAttr "cc_tail05_outPutAnimBank_1_translateZ.o" "cc_tail05_outPutAnimBank_1.tz"
		;
connectAttr "cc_tail06_outPutAnimBank_1_translateX.o" "cc_tail06_outPutAnimBank_1.tx"
		;
connectAttr "cc_tail06_outPutAnimBank_1_translateY.o" "cc_tail06_outPutAnimBank_1.ty"
		;
connectAttr "cc_tail06_outPutAnimBank_1_translateZ.o" "cc_tail06_outPutAnimBank_1.tz"
		;
connectAttr "cc_r_shoulder01_outPutAnimBank_1_translateX.o" "cc_r_shoulder01_outPutAnimBank_1.tx"
		;
connectAttr "cc_r_shoulder01_outPutAnimBank_1_translateY.o" "cc_r_shoulder01_outPutAnimBank_1.ty"
		;
connectAttr "cc_r_shoulder01_outPutAnimBank_1_translateZ.o" "cc_r_shoulder01_outPutAnimBank_1.tz"
		;
connectAttr "cc_r_shoulder01_outPutAnimBank_1_rotateX.o" "cc_r_shoulder01_outPutAnimBank_1.rx"
		;
connectAttr "cc_r_shoulder01_outPutAnimBank_1_rotateY.o" "cc_r_shoulder01_outPutAnimBank_1.ry"
		;
connectAttr "cc_r_shoulder01_outPutAnimBank_1_rotateZ.o" "cc_r_shoulder01_outPutAnimBank_1.rz"
		;
connectAttr "cc_l_shoulder01_outPutAnimBank_1_translateX.o" "cc_l_shoulder01_outPutAnimBank_1.tx"
		;
connectAttr "cc_l_shoulder01_outPutAnimBank_1_translateY.o" "cc_l_shoulder01_outPutAnimBank_1.ty"
		;
connectAttr "cc_l_shoulder01_outPutAnimBank_1_translateZ.o" "cc_l_shoulder01_outPutAnimBank_1.tz"
		;
connectAttr "cc_l_shoulder01_outPutAnimBank_1_rotateX.o" "cc_l_shoulder01_outPutAnimBank_1.rx"
		;
connectAttr "cc_l_shoulder01_outPutAnimBank_1_rotateY.o" "cc_l_shoulder01_outPutAnimBank_1.ry"
		;
connectAttr "cc_l_shoulder01_outPutAnimBank_1_rotateZ.o" "cc_l_shoulder01_outPutAnimBank_1.rz"
		;
connectAttr "cc_global01_outPutAnimBank_1_visibility.o" "cc_global01_outPutAnimBank_1.v"
		;
connectAttr "cc_global01_outPutAnimBank_1_translateX.o" "cc_global01_outPutAnimBank_1.tx"
		;
connectAttr "cc_global01_outPutAnimBank_1_translateY.o" "cc_global01_outPutAnimBank_1.ty"
		;
connectAttr "cc_global01_outPutAnimBank_1_translateZ.o" "cc_global01_outPutAnimBank_1.tz"
		;
connectAttr "cc_global01_outPutAnimBank_1_rotateX.o" "cc_global01_outPutAnimBank_1.rx"
		;
connectAttr "cc_global01_outPutAnimBank_1_rotateY.o" "cc_global01_outPutAnimBank_1.ry"
		;
connectAttr "cc_global01_outPutAnimBank_1_rotateZ.o" "cc_global01_outPutAnimBank_1.rz"
		;
connectAttr "cc_global01_outPutAnimBank_1_scaleX.o" "cc_global01_outPutAnimBank_1.sx"
		;
connectAttr "cc_global01_outPutAnimBank_1_scaleY.o" "cc_global01_outPutAnimBank_1.sy"
		;
connectAttr "cc_global01_outPutAnimBank_1_scaleZ.o" "cc_global01_outPutAnimBank_1.sz"
		;
connectAttr "cc_global01_outPutAnimBank_1_vis_head_cervix.o" "cc_global01_outPutAnimBank_1.vis_head_cervix"
		;
connectAttr "cc_global01_outPutAnimBank_1_vis_upperBody.o" "cc_global01_outPutAnimBank_1.vis_upperBody"
		;
connectAttr "cc_global01_outPutAnimBank_1_vis_ft_legs.o" "cc_global01_outPutAnimBank_1.vis_ft_legs"
		;
connectAttr "cc_global01_outPutAnimBank_1_vis_bk_legs.o" "cc_global01_outPutAnimBank_1.vis_bk_legs"
		;
connectAttr "cc_global01_outPutAnimBank_1_vis_tail.o" "cc_global01_outPutAnimBank_1.vis_tail"
		;
// End of walk.ma

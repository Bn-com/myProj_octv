//Maya ASCII 2011 scene
//Name: horse_walk.ma
//Last modified: Mon, Aug 06, 2012 09:40:24 AM
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
	setAttr ".ns" -type "string" "horse_1";
	setAttr ".range" -type "string" "\"1:26\"";
	setAttr ".num" 23;
	setAttr ".nts" -type "string" "horse_1:cc_COG01; horse_1:cc_midVertebraet01; horse_1:cc_thoracic01; horse_1:cc_hipSway01; horse_1:cc_r_shoulder01; horse_1:cc_l_shoulder01; horse_1:cc_cervical01; horse_1:cc_cervical02; horse_1:cc_head01; horse_1:cc_l_carpalFT01; horse_1:cc_r_carpalFT01; horse_1:cc_r_tarsalFT01; horse_1:cc_l_tarsalFT01; horse_1:cc_r_legFT01; horse_1:cc_l_legFT01; horse_1:cc_r_legBK01; horse_1:cc_l_legBK01; horse_1:cc_tail01; horse_1:cc_tail02; horse_1:cc_tail03; horse_1:cc_cc_tail04; horse_1:cc_tail05; horse_1:cc_tail06; ";
createNode transform -n "horse_1:cc_COG01_outPutAnimBank_1" -p "MG_outPutAnimBank";
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
	setAttr ".ObjName" -type "string" "horse_1:cc_COG01";
createNode locator -n "horse_1:cc_COG01_outPutAnimBank_1Shape" -p "horse_1:cc_COG01_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "horse_1:cc_midVertebraet01_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "horse_1:cc_midVertebraet01";
createNode locator -n "horse_1:cc_midVertebraet01_outPutAnimBank_1Shape" -p "horse_1:cc_midVertebraet01_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "horse_1:cc_thoracic01_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "lock" -ln "lock" -at "double";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr -k on ".lock";
	setAttr ".ObjName" -type "string" "horse_1:cc_thoracic01";
createNode locator -n "horse_1:cc_thoracic01_outPutAnimBank_1Shape" -p "horse_1:cc_thoracic01_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "horse_1:cc_hipSway01_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "horse_1:cc_hipSway01";
createNode locator -n "horse_1:cc_hipSway01_outPutAnimBank_1Shape" -p "horse_1:cc_hipSway01_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "horse_1:cc_r_shoulder01_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "horse_1:cc_r_shoulder01";
createNode locator -n "horse_1:cc_r_shoulder01_outPutAnimBank_1Shape" -p "horse_1:cc_r_shoulder01_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "horse_1:cc_l_shoulder01_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "horse_1:cc_l_shoulder01";
createNode locator -n "horse_1:cc_l_shoulder01_outPutAnimBank_1Shape" -p "horse_1:cc_l_shoulder01_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "horse_1:cc_cervical01_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "horse_1:cc_cervical01";
createNode locator -n "horse_1:cc_cervical01_outPutAnimBank_1Shape" -p "horse_1:cc_cervical01_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "horse_1:cc_cervical02_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "horse_1:cc_cervical02";
createNode locator -n "horse_1:cc_cervical02_outPutAnimBank_1Shape" -p "horse_1:cc_cervical02_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "horse_1:cc_head01_outPutAnimBank_1" -p "MG_outPutAnimBank";
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
	setAttr ".ObjName" -type "string" "horse_1:cc_head01";
createNode locator -n "horse_1:cc_head01_outPutAnimBank_1Shape" -p "horse_1:cc_head01_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "horse_1:cc_l_carpalFT01_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "horse_1:cc_l_carpalFT01";
createNode locator -n "horse_1:cc_l_carpalFT01_outPutAnimBank_1Shape" -p "horse_1:cc_l_carpalFT01_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "horse_1:cc_r_carpalFT01_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "horse_1:cc_r_carpalFT01";
createNode locator -n "horse_1:cc_r_carpalFT01_outPutAnimBank_1Shape" -p "horse_1:cc_r_carpalFT01_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "horse_1:cc_r_tarsalFT01_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "horse_1:cc_r_tarsalFT01";
createNode locator -n "horse_1:cc_r_tarsalFT01_outPutAnimBank_1Shape" -p "horse_1:cc_r_tarsalFT01_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "horse_1:cc_l_tarsalFT01_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "horse_1:cc_l_tarsalFT01";
createNode locator -n "horse_1:cc_l_tarsalFT01_outPutAnimBank_1Shape" -p "horse_1:cc_l_tarsalFT01_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "horse_1:cc_r_legFT01_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "fetlock_ft_curl" -ln "fetlock_ft_curl" -at "double";
	addAttr -ci true -sn "hoof_ft_curl" -ln "hoof_ft_curl" -at "double";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr -k on ".fetlock_ft_curl";
	setAttr -k on ".hoof_ft_curl";
	setAttr ".ObjName" -type "string" "horse_1:cc_r_legFT01";
createNode locator -n "horse_1:cc_r_legFT01_outPutAnimBank_1Shape" -p "horse_1:cc_r_legFT01_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "horse_1:cc_l_legFT01_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "fetlock_ft_curl" -ln "fetlock_ft_curl" -at "double";
	addAttr -ci true -sn "hoof_ft_curl" -ln "hoof_ft_curl" -at "double";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr -k on ".fetlock_ft_curl";
	setAttr -k on ".hoof_ft_curl";
	setAttr ".ObjName" -type "string" "horse_1:cc_l_legFT01";
createNode locator -n "horse_1:cc_l_legFT01_outPutAnimBank_1Shape" -p "horse_1:cc_l_legFT01_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "horse_1:cc_r_legBK01_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "fetlock_bk_curl" -ln "fetlock_bk_curl" -at "double";
	addAttr -ci true -sn "hoof_bk_curl" -ln "hoof_bk_curl" -at "double";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr -k on ".fetlock_bk_curl";
	setAttr -k on ".hoof_bk_curl";
	setAttr ".ObjName" -type "string" "horse_1:cc_r_legBK01";
createNode locator -n "horse_1:cc_r_legBK01_outPutAnimBank_1Shape" -p "horse_1:cc_r_legBK01_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "horse_1:cc_l_legBK01_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "fetlock_bk_curl" -ln "fetlock_bk_curl" -at "double";
	addAttr -ci true -sn "hoof_bk_curl" -ln "hoof_bk_curl" -at "double";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr -k on ".fetlock_bk_curl";
	setAttr -k on ".hoof_bk_curl";
	setAttr ".ObjName" -type "string" "horse_1:cc_l_legBK01";
createNode locator -n "horse_1:cc_l_legBK01_outPutAnimBank_1Shape" -p "horse_1:cc_l_legBK01_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "horse_1:cc_tail01_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "horse_1:cc_tail01";
createNode locator -n "horse_1:cc_tail01_outPutAnimBank_1Shape" -p "horse_1:cc_tail01_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "horse_1:cc_tail02_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "horse_1:cc_tail02";
createNode locator -n "horse_1:cc_tail02_outPutAnimBank_1Shape" -p "horse_1:cc_tail02_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "horse_1:cc_tail03_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "horse_1:cc_tail03";
createNode locator -n "horse_1:cc_tail03_outPutAnimBank_1Shape" -p "horse_1:cc_tail03_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "horse_1:cc_cc_tail04_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "horse_1:cc_cc_tail04";
createNode locator -n "horse_1:cc_cc_tail04_outPutAnimBank_1Shape" -p "horse_1:cc_cc_tail04_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "horse_1:cc_tail05_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "horse_1:cc_tail05";
createNode locator -n "horse_1:cc_tail05_outPutAnimBank_1Shape" -p "horse_1:cc_tail05_outPutAnimBank_1";
	setAttr -k off ".v";
createNode transform -n "horse_1:cc_tail06_outPutAnimBank_1" -p "MG_outPutAnimBank";
	addAttr -ci true -sn "ObjName" -ln "ObjName" -dt "string";
	setAttr -k off ".v";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".ObjName" -type "string" "horse_1:cc_tail06";
createNode locator -n "horse_1:cc_tail06_outPutAnimBank_1Shape" -p "horse_1:cc_tail06_outPutAnimBank_1";
	setAttr -k off ".v";
createNode animCurveTL -n "horse_1:cc_COG01_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 25 0;
createNode animCurveTL -n "horse_1:cc_COG01_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 -5.3722466960000004 25 -5.3722466960000004;
createNode animCurveTL -n "horse_1:cc_COG01_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 25 135.83875727157763;
createNode animCurveTA -n "horse_1:cc_COG01_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 -5 25 -5;
createNode animCurveTA -n "horse_1:cc_COG01_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 25 0;
createNode animCurveTA -n "horse_1:cc_COG01_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 25 0;
createNode animCurveTU -n "horse_1:cc_COG01_outPutAnimBank_1_tr_curl";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 9.1 25 9.1;
createNode animCurveTU -n "horse_1:cc_COG01_outPutAnimBank_1_tr_sway";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 25 0;
createNode animCurveTU -n "horse_1:cc_COG01_outPutAnimBank_1_tr_turn";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 -5 13 5 25 -5;
createNode animCurveTL -n "horse_1:cc_midVertebraet01_outPutAnimBank_1_translateX";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 25 0;
	setAttr -s 2 ".kit[1]"  10;
	setAttr -s 2 ".kot[1]"  10;
createNode animCurveTL -n "horse_1:cc_midVertebraet01_outPutAnimBank_1_translateY";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 7 -2.4861306070000002 13 0 19 -2.5417236079999999 
		25 0;
	setAttr -s 5 ".kit[1:4]"  10 3 10 3;
	setAttr -s 5 ".kot[1:4]"  10 3 10 3;
createNode animCurveTL -n "horse_1:cc_midVertebraet01_outPutAnimBank_1_translateZ";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 25 0;
	setAttr -s 2 ".kit[1]"  10;
	setAttr -s 2 ".kot[1]"  10;
createNode animCurveTA -n "horse_1:cc_midVertebraet01_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 12.30218402 4 11.434579 10 13.430946820000001 
		16 11.434579 22 13.16978903 25 12.30218402;
	setAttr -s 6 ".kit[0:5]"  1 10 10 10 10 1;
	setAttr -s 6 ".kot[0:5]"  1 10 10 10 10 1;
	setAttr -s 6 ".kix[0:5]"  0.98772424459457397 1 1 1 1 0.98768210411071777;
	setAttr -s 6 ".kiy[0:5]"  -0.1562076061964035 0 0 0 0 -0.15647374093532562;
	setAttr -s 6 ".kox[0:5]"  0.98772424459457397 1 1 1 1 0.98768216371536255;
	setAttr -s 6 ".koy[0:5]"  -0.15620756149291992 0 0 0 0 -0.15647368133068085;
createNode animCurveTA -n "horse_1:cc_midVertebraet01_outPutAnimBank_1_rotateY";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 -5 13 5 25 -5;
	setAttr -s 3 ".kit[1:2]"  10 3;
	setAttr -s 3 ".kot[1:2]"  10 3;
createNode animCurveTA -n "horse_1:cc_midVertebraet01_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 25 0;
	setAttr -s 2 ".kit[1]"  10;
	setAttr -s 2 ".kot[1]"  10;
createNode animCurveTL -n "horse_1:cc_thoracic01_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  1 -0.37588791162576479 4 -0.37633648264501413 
		10 0.16743048479909892 13 0.37292608193831178 16 0.37133335865383565 19 0.20173918481852945 
		25 -0.37588791162576479;
	setAttr -s 7 ".kit[0:6]"  3 10 1 10 10 1 3;
	setAttr -s 7 ".kot[0:6]"  3 10 1 10 10 1 3;
	setAttr -s 7 ".kix[2:6]"  0.37684282660484314 1 1 0.41185447573661804 
		1;
	setAttr -s 7 ".kiy[2:6]"  0.9262772798538208 0 0 -0.91124963760375977 
		0;
	setAttr -s 7 ".kox[2:6]"  0.37684282660484314 1 1 0.41185447573661804 
		1;
	setAttr -s 7 ".koy[2:6]"  0.9262772798538208 0 0 -0.91124963760375977 
		0;
createNode animCurveTL -n "horse_1:cc_thoracic01_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  1 -2.7255579528222986 7 -4.6028834009999997 
		10 -2.9565439338222985 13 -2.7255579528222986 19 -4.6028834009999997 22 -2.9916733698222986 
		25 -2.7255579528222986;
	setAttr -s 7 ".kit[0:6]"  3 10 10 10 10 10 3;
	setAttr -s 7 ".kot[0:6]"  3 10 10 10 10 10 3;
createNode animCurveTL -n "horse_1:cc_thoracic01_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 7 1.0770323049999999 13 0 19 1.0770323049999999 
		25 0;
	setAttr -s 5 ".kit[0:4]"  3 10 10 10 3;
	setAttr -s 5 ".kot[0:4]"  3 10 10 10 3;
createNode animCurveTA -n "horse_1:cc_thoracic01_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -1.2170540329999999 7 0.57361421420000003 
		13 -1.2170540329999999 19 0.57361421420000003 25 -1.2170540329999999;
	setAttr -s 5 ".kit[0:4]"  3 10 10 10 3;
	setAttr -s 5 ".kot[0:4]"  3 10 10 10 3;
createNode animCurveTA -n "horse_1:cc_thoracic01_outPutAnimBank_1_rotateY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 7 -2.018004022 13 0 19 2.1569449220000001 
		25 0;
	setAttr -s 5 ".kit[1:4]"  10 1 10 1;
	setAttr -s 5 ".kot[1:4]"  10 1 10 1;
	setAttr -s 5 ".kix[0:4]"  0.97944271564483643 1 0.97648841142654419 
		1 0.9789615273475647;
	setAttr -s 5 ".kiy[0:4]"  -0.20172275602817535 0 0.21557009220123291 
		0 -0.20404511690139771;
	setAttr -s 5 ".kox[0:4]"  0.97944271564483643 1 0.97648841142654419 
		1 0.97896146774291992;
	setAttr -s 5 ".koy[0:4]"  -0.20172260701656342 0 0.2155701071023941 
		0 -0.20404520630836487;
createNode animCurveTA -n "horse_1:cc_thoracic01_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 25 0;
	setAttr -s 2 ".kit[1]"  10;
	setAttr -s 2 ".kot[1]"  10;
createNode animCurveTU -n "horse_1:cc_thoracic01_outPutAnimBank_1_lock";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 25 0;
	setAttr -s 2 ".kit[1]"  10;
	setAttr -s 2 ".kot[1]"  10;
createNode animCurveTL -n "horse_1:cc_hipSway01_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  1 0.1118488424895359 4 0.28676362571240549 
		7 0.26198920343468107 10 0.13370882321431632 16 -0.2726686455634299 19 -0.26428245307518949 
		22 -0.13490655572427376 25 0.1118488424895359;
	setAttr -s 8 ".kit[0:7]"  1 10 1 10 10 1 10 10;
	setAttr -s 8 ".kot[0:7]"  1 10 1 10 10 1 10 10;
	setAttr -s 8 ".kix[0:7]"  0.43384093046188354 1 0.94375061988830566 
		0.57422208786010742 1 0.9651329517364502 0.55354344844818115 0.45189926028251648;
	setAttr -s 8 ".kiy[0:7]"  0.90098947286605835 0 -0.33065831661224365 
		-0.81869959831237793 0 0.26176005601882935 0.83282029628753662 0.89206904172897339;
	setAttr -s 8 ".kox[0:7]"  0.44913837313652039 1 0.94375061988830566 
		0.57422208786010742 1 0.9651329517364502 0.55354344844818115 0.45189926028251648;
	setAttr -s 8 ".koy[0:7]"  0.89346224069595337 0 -0.33065831661224365 
		-0.81869959831237793 0 0.26176029443740845 0.83282029628753662 0.89206904172897339;
createNode animCurveTL -n "horse_1:cc_hipSway01_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  1 -2.6516228590000002 4 -0.17214190844709898 
		7 -0.30910783844709888 10 -3.123556534 16 -0.12035702344709898 19 -0.30910783844709888 
		22 -3.123556534 25 -2.6516228590000002;
	setAttr -s 8 ".kit[7]"  1;
	setAttr -s 8 ".kot[7]"  1;
	setAttr -s 8 ".kix[7]"  0.11958387494087219;
	setAttr -s 8 ".kiy[7]"  0.99282413721084595;
	setAttr -s 8 ".kox[7]"  0.1195838451385498;
	setAttr -s 8 ".koy[7]"  0.99282413721084595;
createNode animCurveTL -n "horse_1:cc_hipSway01_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 -0.24625550660000001 4 -0.49251101320000001 
		10 0 16 -0.49251101320000001 22 0 25 -0.24625550660000001;
	setAttr -s 6 ".kit[0:5]"  1 10 10 10 10 1;
	setAttr -s 6 ".kot[0:5]"  1 10 10 10 10 1;
	setAttr -s 6 ".kix[0:5]"  0.29257050156593323 0.83588248491287231 
		1 1 0.83588248491287231 0.32975426316261292;
	setAttr -s 6 ".kiy[0:5]"  -0.95624399185180664 0.54890841245651245 
		0 0 0.548908531665802 -0.94406682252883911;
	setAttr -s 6 ".kox[0:5]"  0.30038049817085266 0.83588248491287231 
		1 1 0.83588248491287231 0.32975432276725769;
	setAttr -s 6 ".koy[0:5]"  -0.95381945371627808 0.54890841245651245 
		0 0 0.548908531665802 -0.94406676292419434;
createNode animCurveTA -n "horse_1:cc_hipSway01_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 -1.3354133939999999 4 -0.99361803410000005 
		10 -1.677208754 16 -0.99361803410000005 22 -1.677208754 25 -1.3354133939999999;
	setAttr -s 6 ".kit[0:5]"  1 10 10 10 10 1;
	setAttr -s 6 ".kot[0:5]"  1 10 10 10 10 1;
	setAttr -s 6 ".kix[0:5]"  0.99749487638473511 1 1 1 1 0.9962153434753418;
	setAttr -s 6 ".kiy[0:5]"  0.070739142596721649 0 0 0 0 0.086919546127319336;
	setAttr -s 6 ".kox[0:5]"  0.997763991355896 1 1 1 1 0.9962153434753418;
	setAttr -s 6 ".koy[0:5]"  0.066835857927799225 0 0 0 0 0.086919516324996948;
createNode animCurveTA -n "horse_1:cc_hipSway01_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 -2.1206602069999998 10 3.0605354139999998 
		22 -3.0801409689999999 25 -2.1206602069999998;
	setAttr -s 4 ".kit[0:3]"  1 10 10 1;
	setAttr -s 4 ".kot[0:3]"  1 10 10 1;
	setAttr -s 4 ".kix[0:3]"  0.95338696241378784 0.99981695413589478 
		1 0.97987949848175049;
	setAttr -s 4 ".kiy[0:3]"  0.30175048112869263 -0.019134894013404846 
		0 0.19958993792533875;
	setAttr -s 4 ".kox[0:3]"  0.95483779907226563 0.99981695413589478 
		1 0.97987949848175049;
	setAttr -s 4 ".koy[0:3]"  0.29712766408920288 -0.019134894013404846 
		0 0.19958995282649994;
createNode animCurveTA -n "horse_1:cc_hipSway01_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 2.5000000230000001 4 4 16 -4 25 2.5000000230000001;
	setAttr -s 4 ".kit[0:3]"  1 10 10 1;
	setAttr -s 4 ".kot[0:3]"  1 10 10 1;
	setAttr -s 4 ".kix[0:3]"  0.95449036359786987 1 0.99955266714096069 
		0.95145332813262939;
	setAttr -s 4 ".kiy[0:3]"  0.29824173450469971 0 -0.02990654855966568 
		0.30779322981834412;
	setAttr -s 4 ".kox[0:3]"  0.95541930198669434 1 0.99955266714096069 
		0.95145332813262939;
	setAttr -s 4 ".koy[0:3]"  0.29525241255760193 0 -0.02990654855966568 
		0.30779322981834412;
createNode animCurveTL -n "horse_1:cc_r_shoulder01_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 1.8939239290000001 4 3 8 0 20 0.49919280724940462 
		22 0.71022176199999998 25 1.8939239290000001;
	setAttr -s 6 ".kit[2:5]"  1 10 10 10;
	setAttr -s 6 ".kot[2:5]"  1 10 10 10;
	setAttr -s 6 ".kix[2:5]"  0.99821025133132935 0.63469845056533813 
		0.14773266017436981 0.10501690953969955;
	setAttr -s 6 ".kiy[2:5]"  -0.059802334755659103 0.77275991439819336 
		0.98902738094329834 0.99447041749954224;
	setAttr -s 6 ".kox[2:5]"  0.99821025133132935 0.63469845056533813 
		0.14773266017436981 0.10501691699028015;
	setAttr -s 6 ".koy[2:5]"  -0.059802308678627014 0.77275991439819336 
		0.98902738094329834 0.99447047710418701;
createNode animCurveTL -n "horse_1:cc_r_shoulder01_outPutAnimBank_1_translateY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  1 12.61647037 4 14.734634079999999 8 -0.016084590270000001 
		13 -9.8705345990000009 19 1.8119694086590901 20 4.4073070518412134 22 8.0394629460000004 
		25 12.61647037;
	setAttr -s 8 ".kit[3:7]"  10 1 10 10 1;
	setAttr -s 8 ".kot[3:7]"  10 1 10 10 1;
	setAttr -s 8 ".kix[0:7]"  0.031057178974151611 0.050576046109199524 
		0.013089731335639954 0.24319469928741455 0.014387242496013641 0.02006823942065239 
		0.025369973853230476 0.033612344413995743;
	setAttr -s 8 ".kiy[0:7]"  0.99951761960983276 -0.99872028827667236 
		-0.99991434812545776 0.96997749805450439 0.99989652633666992 0.99979865550994873 
		0.99967813491821289 0.99943500757217407;
	setAttr -s 8 ".kox[0:7]"  0.033920347690582275 0.050576023757457733 
		0.013089732266962528 0.24319469928741455 0.014387236908078194 0.02006823942065239 
		0.025369973853230476 0.033612344413995743;
	setAttr -s 8 ".koy[0:7]"  0.99942457675933838 -0.99872022867202759 
		-0.99991434812545776 0.96997749805450439 0.99989652633666992 0.99979865550994873 
		0.99967813491821289 0.9994349479675293;
createNode animCurveTL -n "horse_1:cc_r_shoulder01_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  1 -3.6805789830000002 4 -5.7104178079999999 
		8 -3.6652174930000001 13 0 20 -0.48256557952685486 22 -1.3802176900000001 25 -3.6805789830000002;
	setAttr -s 7 ".kit[2:6]"  1 10 10 1 10;
	setAttr -s 7 ".kot[2:6]"  1 10 10 1 10;
	setAttr -s 7 ".kix[2:6]"  0.049779150635004044 0.15519814193248749 
		0.26219123601913452 0.10431446135044098 0.054259214550256729;
	setAttr -s 7 ".kiy[2:6]"  0.99876028299331665 0.98788338899612427 
		-0.9650159478187561 -0.9945443868637085 -0.998526930809021;
	setAttr -s 7 ".kox[2:6]"  0.049779161810874939 0.15519814193248749 
		0.26219123601913452 0.10431449115276337 0.054259214550256729;
	setAttr -s 7 ".koy[2:6]"  0.99876028299331665 0.98788338899612427 
		-0.9650159478187561 -0.9945443868637085 -0.998526930809021;
createNode animCurveTA -n "horse_1:cc_r_shoulder01_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  1 6.0000000000000009 4 13.348843609999999 
		9 26.602942688952226 13 5.457941012 19 -17.261890177692027 20 -8.9624626298935954 
		22 -1.953506212444899 25 6.0000000000000009;
	setAttr -s 8 ".kit[2:7]"  3 1 1 10 9 10;
	setAttr -s 8 ".kot[2:7]"  3 1 1 10 9 10;
	setAttr -s 8 ".kix[3:7]"  0.39871734380722046 0.99363785982131958 
		0.42376276850700378 0.62363201379776001 0.66916155815124512;
	setAttr -s 8 ".kiy[3:7]"  -0.91707390546798706 0.1126224547624588 
		0.90577328205108643 0.78171807527542114 0.74311691522598267;
	setAttr -s 8 ".kox[3:7]"  0.39871746301651001 0.99363785982131958 
		0.42376276850700378 0.62363201379776001 0.66916161775588989;
	setAttr -s 8 ".koy[3:7]"  -0.91707384586334229 0.11262241750955582 
		0.90577328205108643 0.78171807527542114 0.74311697483062744;
createNode animCurveTA -n "horse_1:cc_r_shoulder01_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 25 0;
createNode animCurveTA -n "horse_1:cc_r_shoulder01_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 2.5 13 0 25 2.5;
createNode animCurveTL -n "horse_1:cc_l_shoulder01_outPutAnimBank_1_translateX";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 0 10 -0.80535467579999998 13 -2.109050818 
		16 -2.9900467289999999 20 0 25 0;
	setAttr -s 6 ".kit[0:5]"  3 10 1 1 3 10;
	setAttr -s 6 ".kot[0:5]"  3 10 1 1 3 10;
	setAttr -s 6 ".kix[2:5]"  0.084344334900379181 0.95231711864471436 
		1 1;
	setAttr -s 6 ".kiy[2:5]"  -0.99643665552139282 0.30511009693145752 
		0 0;
	setAttr -s 6 ".kox[2:5]"  0.084344357252120972 0.95231741666793823 
		1 1;
	setAttr -s 6 ".koy[2:5]"  -0.99643665552139282 0.30510914325714111 
		0 0;
createNode animCurveTL -n "horse_1:cc_l_shoulder01_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  1 -10.65683166 7 0 10 7.7539050872179818 
		13 12.693698605217982 16 14.773490539999999 20 0 25 -10.65683166;
	setAttr -s 7 ".kit[0:6]"  3 10 10 10 1 1 3;
	setAttr -s 7 ".kot[0:6]"  3 10 10 10 1 1 3;
	setAttr -s 7 ".kix[4:6]"  0.058747630566358566 0.010336404666304588 
		1;
	setAttr -s 7 ".kiy[4:6]"  -0.99827289581298828 -0.99994665384292603 
		0;
	setAttr -s 7 ".kox[4:6]"  0.058747615665197372 0.010336402803659439 
		1;
	setAttr -s 7 ".koy[4:6]"  -0.99827289581298828 -0.99994659423828125 
		0;
createNode animCurveTL -n "horse_1:cc_l_shoulder01_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 0 10 -1.3780428469999999 13 -3.5684186269999998 
		16 -5.4847028289999997 20 -3.9558001051558938 25 0;
	setAttr -s 6 ".kit[0:5]"  3 10 10 10 10 3;
	setAttr -s 6 ".kot[0:5]"  3 10 10 10 10 3;
createNode animCurveTA -n "horse_1:cc_l_shoulder01_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  1 6.4351430839999999 7 -14.84920034516734 
		8 -6.3008613947237313 10 -0.76471632854476279 13 5.9862050866332872 16 12.30578118 
		20 19.22692335540048 25 6.4351430839999999;
	setAttr -s 8 ".kit[0:7]"  1 1 10 10 10 10 1 1;
	setAttr -s 8 ".kot[0:7]"  1 1 10 10 10 10 1 1;
	setAttr -s 8 ".kix[0:7]"  0.57684236764907837 0.99990099668502808 
		0.45326530933380127 0.69680404663085938 0.73868805170059204 0.78379547595977783 0.99636995792388916 
		0.62106156349182129;
	setAttr -s 8 ".kiy[0:7]"  -0.81685554981231689 -0.014070414938032627 
		0.89137566089630127 0.71726143360137939 0.67404747009277344 0.62101906538009644 -0.085129454731941223 
		-0.78376179933547974;
	setAttr -s 8 ".kox[0:7]"  0.5900954008102417 0.99990105628967285 
		0.45326530933380127 0.69680404663085938 0.73868805170059204 0.78379547595977783 0.99636989831924438 
		0.62106162309646606;
	setAttr -s 8 ".koy[0:7]"  -0.80733358860015869 -0.014070365577936172 
		0.89137566089630127 0.71726143360137939 0.67404747009277344 0.62101906538009644 -0.085129417479038239 
		-0.78376179933547974;
createNode animCurveTA -n "horse_1:cc_l_shoulder01_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 25 0;
createNode animCurveTA -n "horse_1:cc_l_shoulder01_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 13 -2.5 25 0;
createNode animCurveTL -n "horse_1:cc_cervical01_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 7 -0.1321770990222956 13 0 19 0.11772784835310439 
		25 0;
createNode animCurveTL -n "horse_1:cc_cervical01_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 7 0.2908249988630966 13 0 19 0.24235693180230555 
		25 0;
createNode animCurveTL -n "horse_1:cc_cervical01_outPutAnimBank_1_translateZ";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 1.3855928946414202 7 -2.119381739341391 
		13 1.3855928946414202 19 -2.1606934037629371 25 1.3855928946414202;
	setAttr -s 5 ".kit[1:4]"  10 3 10 3;
	setAttr -s 5 ".kot[1:4]"  10 3 10 3;
createNode animCurveTA -n "horse_1:cc_cervical01_outPutAnimBank_1_rotateX";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 4.7494443412216123 7 -1.7147383002490002 
		13 4.7494443412216123 19 -1.7147383002490002 25 4.7494443412216123;
	setAttr -s 5 ".kit[1:4]"  10 3 10 3;
	setAttr -s 5 ".kot[1:4]"  10 3 10 3;
createNode animCurveTA -n "horse_1:cc_cervical01_outPutAnimBank_1_rotateY";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 -1 13 1 25 -1;
createNode animCurveTA -n "horse_1:cc_cervical01_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0.40813430961167352 13 -0.42215639825242796 
		25 0.40813430961167352;
createNode animCurveTL -n "horse_1:cc_cervical02_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 11 ".ktv[0:10]"  1 0.024212752614044847 6 -0.105736332716252 
		8 0 12 -0.0050818497230619725 13 0 14 0 18 0.11725736971124279 19 0 20 0 24 0.026148268359471333 
		25 0;
createNode animCurveTL -n "horse_1:cc_cervical02_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 11 ".ktv[0:10]"  1 -0.024184928298799001 6 0.31574544346624378 
		8 0 12 -0.017491033693583329 13 0 14 0 18 0.32057078756774149 19 0 20 0 24 -0.08746879763615803 
		25 0;
createNode animCurveTL -n "horse_1:cc_cervical02_outPutAnimBank_1_translateZ";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  1 0.954 2 2.103301671392432 4 1.9061777746768236 
		9 -2.9410701998938955 15 2.2835644771859855 21 -2.8434392247745532 25 0.95377708969530595;
	setAttr -s 7 ".kit[3:6]"  10 10 1 1;
	setAttr -s 7 ".kot[3:6]"  10 10 1 1;
	setAttr -s 7 ".kix[0:6]"  0.035390302538871765 0.062941893935203552 
		0.034062523394823074 0.77198332548141479 0.98146480321884155 0.96926164627075195 
		0.033013656735420227;
	setAttr -s 7 ".kiy[0:6]"  0.99937355518341064 0.99801719188690186 
		-0.99941974878311157 0.63564276695251465 0.19164273142814636 -0.24603217840194702 
		0.99945491552352905;
	setAttr -s 7 ".kox[0:6]"  0.035963311791419983 0.06572936475276947 
		0.035333059728145599 0.77198332548141479 0.98146480321884155 0.9692617654800415 0.031981226056814194;
	setAttr -s 7 ".koy[0:6]"  0.99935311079025269 0.99783754348754883 
		-0.99937558174133301 0.63564276695251465 0.19164273142814636 -0.24603196978569031 
		0.99948853254318237;
createNode animCurveTA -n "horse_1:cc_cervical02_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 -1.2875654210578464 3 -0.87026096916568552 
		9 -2.2115164397608558 15 -0.87026096916568552 21 -2.2115164397608558 25 -1.2875654210578464;
	setAttr -s 6 ".kit[0:5]"  1 10 10 10 10 1;
	setAttr -s 6 ".kot[0:5]"  1 10 10 10 10 1;
	setAttr -s 6 ".kix[0:5]"  0.99070698022842407 1 1 1 1 0.98779869079589844;
	setAttr -s 6 ".kiy[0:5]"  0.1360137015581131 0 0 0 0 0.15573602914810181;
	setAttr -s 6 ".kox[0:5]"  0.9907570481300354 1 1 1 1 0.98779869079589844;
	setAttr -s 6 ".koy[0:5]"  0.13564836978912354 0 0 0 0 0.155736044049263;
createNode animCurveTA -n "horse_1:cc_cervical02_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  1 0 8 0 13 0 14 0 19 0 20 0 25 0;
createNode animCurveTA -n "horse_1:cc_cervical02_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  1 0 8 0 13 0 14 0 19 0 20 0 25 0;
createNode animCurveTL -n "horse_1:cc_head01_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 13 0 25 0;
createNode animCurveTL -n "horse_1:cc_head01_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 13 0 25 0;
createNode animCurveTL -n "horse_1:cc_head01_outPutAnimBank_1_translateZ";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  1 -1.2274117273904137 5 0.91579839228177673 
		8 -0.48420179696472343 11 -1.8842019862112243 17 0.91579839228177673 23 -1.8842019862112243 
		25 -1.2274123196536171;
	setAttr -s 7 ".kit[3:6]"  3 10 3 1;
	setAttr -s 7 ".kot[3:6]"  3 10 3 1;
	setAttr -s 7 ".kix[0:6]"  0.068358488380908966 0.27047690749168396 
		0.063166350126266479 1 1 1 0.068727016448974609;
	setAttr -s 7 ".kiy[0:6]"  0.99766081571578979 0.96272653341293335 
		-0.99800300598144531 0 0 0 0.99763548374176025;
	setAttr -s 7 ".kox[0:6]"  0.077260740101337433 0.27047687768936157 
		0.066463947296142578 1 1 1 0.068726979196071625;
	setAttr -s 7 ".koy[0:6]"  0.99701094627380371 0.96272653341293335 
		-0.99778884649276733 0 0 0 0.99763554334640503;
createNode animCurveTA -n "horse_1:cc_head01_outPutAnimBank_1_rotateX";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  1 -0.10915567307124144 3 3.4565784164755589 
		6 6.236506638278259 12 -0.88349661021102133 18 6.1547794282437209 24 -0.67235116209480539 
		25 -0.095828583626792752;
	setAttr -s 7 ".kit[2:6]"  10 10 10 1 1;
	setAttr -s 7 ".kot[2:6]"  10 10 10 1 1;
	setAttr -s 7 ".kix[0:6]"  0.81753081083297729 0.81730085611343384 
		1 0.99999594688415527 0.99997282028198242 0.99437421560287476 0.84595358371734619;
	setAttr -s 7 ".kiy[0:6]"  0.57588487863540649 0.57621121406555176 
		0 -0.0028528061229735613 0.0073701664805412292 -0.1059243306517601 0.53325653076171875;
	setAttr -s 7 ".kox[0:6]"  0.82127153873443604 0.81730085611343384 
		1 0.99999594688415527 0.99997282028198242 0.99437421560287476 0.84595358371734619;
	setAttr -s 7 ".koy[0:6]"  0.57053756713867188 0.57621121406555176 
		0 -0.0028528061229735613 0.0073701664805412292 -0.10592431575059891 0.53325659036636353;
createNode animCurveTA -n "horse_1:cc_head01_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 13 0 25 0;
createNode animCurveTA -n "horse_1:cc_head01_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 13 0 25 0;
createNode animCurveTU -n "horse_1:cc_head01_outPutAnimBank_1_ear_r_rootCurl";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 -3.9945963533761408 13 -3.9945963533761408 
		19 -3.9945963533761408 25 -3.9945963533761408;
createNode animCurveTU -n "horse_1:cc_head01_outPutAnimBank_1_ear_r_rootTurn";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 13 0 25 0;
createNode animCurveTU -n "horse_1:cc_head01_outPutAnimBank_1_ear_r_rootSway";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 13 0 25 0;
createNode animCurveTU -n "horse_1:cc_head01_outPutAnimBank_1_ear_r_midCurl";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 -3.9945963533761408 13 -3.9945963533761408 
		19 -3.9945963533761408 25 -3.9945963533761408;
createNode animCurveTU -n "horse_1:cc_head01_outPutAnimBank_1_ear_r_midTurn";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 13 0 25 0;
createNode animCurveTU -n "horse_1:cc_head01_outPutAnimBank_1_ear_r_midSway";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 13 0 25 0;
createNode animCurveTU -n "horse_1:cc_head01_outPutAnimBank_1_ear_l_rootCurl";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 -6.6234995315938452 13 -6.6234995315938452 
		19 -6.6234995315938452 25 -6.6234995315938452;
createNode animCurveTU -n "horse_1:cc_head01_outPutAnimBank_1_ear_l_rootTurn";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 13 0 25 0;
createNode animCurveTU -n "horse_1:cc_head01_outPutAnimBank_1_ear_l_rootSway";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 13 0 25 0;
createNode animCurveTU -n "horse_1:cc_head01_outPutAnimBank_1_ear_l_midCurl";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 -6.6234995315938452 13 -6.6234995315938452 
		19 -6.6234995315938452 25 -6.6234995315938452;
createNode animCurveTU -n "horse_1:cc_head01_outPutAnimBank_1_ear_l_midTurn";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 13 0 25 0;
createNode animCurveTU -n "horse_1:cc_head01_outPutAnimBank_1_ear_l_midSway";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 13 0 25 0;
createNode animCurveTL -n "horse_1:cc_l_carpalFT01_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 25 0;
createNode animCurveTL -n "horse_1:cc_l_carpalFT01_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 25 0;
createNode animCurveTL -n "horse_1:cc_l_carpalFT01_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 23.565778 25 23.565778;
createNode animCurveTL -n "horse_1:cc_r_carpalFT01_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 25 0;
createNode animCurveTL -n "horse_1:cc_r_carpalFT01_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 25 0;
createNode animCurveTL -n "horse_1:cc_r_carpalFT01_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 23.565778 25 23.565778;
createNode animCurveTL -n "horse_1:cc_r_tarsalFT01_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 25 0;
createNode animCurveTL -n "horse_1:cc_r_tarsalFT01_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 25 0;
createNode animCurveTL -n "horse_1:cc_r_tarsalFT01_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 30.561868 25 30.561868;
createNode animCurveTL -n "horse_1:cc_l_tarsalFT01_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 25 0;
createNode animCurveTL -n "horse_1:cc_l_tarsalFT01_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 25 0;
createNode animCurveTL -n "horse_1:cc_l_tarsalFT01_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 30.561868 25 30.561868;
createNode animCurveTL -n "horse_1:cc_r_legFT01_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 7 7 7 25 7;
createNode animCurveTL -n "horse_1:cc_r_legFT01_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 7 0.15078576305329638 8 0.39531887469999999 
		10 2.8119886620000001 13 6.7726872250000003 15 6.1264465909999997 17 1.287330724 
		18 0.67862858880571286 25 0;
createNode animCurveTL -n "horse_1:cc_r_legFT01_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  1 6.282575456 4 6.283 7 6.283 8 6.283 10 
		6.283 13 45.891797020324013 15 83.563990190477313 17 118.94203157507756 18 136.93676141183701 
		19 142.122 22 142.122 25 142.122;
	setAttr -s 12 ".kit[4:11]"  3 1 10 1 10 10 10 3;
	setAttr -s 12 ".kot[4:11]"  3 1 10 1 10 10 10 3;
	setAttr -s 12 ".kix[5:11]"  0.0021012662909924984 0.002281528664752841 
		0.0028628024738281965 0.0035950366873294115 1 1 1;
	setAttr -s 12 ".kiy[5:11]"  0.99999779462814331 0.99999743700027466 
		0.99999594688415527 0.99999350309371948 0 0 0;
	setAttr -s 12 ".kox[5:11]"  0.0021012662909924984 0.002281528664752841 
		0.0028628022409975529 0.0035950366873294115 1 1 1;
	setAttr -s 12 ".koy[5:11]"  0.99999779462814331 0.99999743700027466 
		0.99999594688415527 0.99999350309371948 0 0 0;
createNode animCurveTA -n "horse_1:cc_r_legFT01_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 7 0 25 0;
createNode animCurveTA -n "horse_1:cc_r_legFT01_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 7 0 25 0;
createNode animCurveTA -n "horse_1:cc_r_legFT01_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 7 0 25 0;
createNode animCurveTU -n "horse_1:cc_r_legFT01_outPutAnimBank_1_fetlock_ft_curl";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 12 ".ktv[0:11]"  1 6.8397274159999997 4 26.512715650000001 
		7 40.389193499999998 8 35.916215649999998 10 20.85678789 13 0.75854247860000001 15 
		2.5015723599999999 17 0 18 0 19 0 22 0 25 6.8397274159999997;
	setAttr -s 12 ".kit[2:11]"  1 10 10 10 10 10 10 10 
		10 1;
	setAttr -s 12 ".kot[2:11]"  1 10 10 10 10 10 10 10 
		10 1;
	setAttr -s 12 ".kix[2:11]"  0.063668340444564819 0.0063994899392127991 
		0.0059255822561681271 0.011349357664585114 0.21460051834583282 1 1 1 1 0.009333483874797821;
	setAttr -s 12 ".kiy[2:11]"  0.99797111749649048 -0.99997949600219727 
		-0.99998247623443604 -0.9999355673789978 -0.97670191526412964 0 0 0 0 0.99995648860931396;
	setAttr -s 12 ".kox[2:11]"  0.063668318092823029 0.0063994899392127991 
		0.0059255822561681271 0.011349357664585114 0.21460051834583282 1 1 1 1 0.009333479218184948;
	setAttr -s 12 ".koy[2:11]"  0.99797111749649048 -0.99997949600219727 
		-0.99998247623443604 -0.9999355673789978 -0.97670191526412964 0 0 0 0 0.99995642900466919;
createNode animCurveTU -n "horse_1:cc_r_legFT01_outPutAnimBank_1_hoof_ft_curl";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 11 ".ktv[0:10]"  1 0 4 0 7 0 8 5 10 72.269558439999997 13 
		91.798621979999993 15 74.115291310000003 17 40 18 10 19 0 25 0;
	setAttr -s 11 ".kit[3:10]"  1 10 10 10 10 10 10 10;
	setAttr -s 11 ".kot[3:10]"  1 10 10 10 10 10 10 10;
	setAttr -s 11 ".kix[3:10]"  0.004489503800868988 0.0024001849815249443 
		0.11216074228286743 0.0032175711821764708 0.0019496092572808266 0.0020833297166973352 
		1 1;
	setAttr -s 11 ".kiy[3:10]"  0.99998998641967773 0.99999713897705078 
		0.99369001388549805 -0.99999481439590454 -0.99999809265136719 -0.99999785423278809 
		0 0;
	setAttr -s 11 ".kox[3:10]"  0.004489503800868988 0.0024001849815249443 
		0.11216074228286743 0.0032175711821764708 0.0019496092572808266 0.0020833297166973352 
		1 1;
	setAttr -s 11 ".koy[3:10]"  0.99998998641967773 0.99999713897705078 
		0.99369001388549805 -0.99999481439590454 -0.99999809265136719 -0.99999785423278809 
		0 0;
createNode animCurveTL -n "horse_1:cc_l_legFT01_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 -7 25 -7;
createNode animCurveTL -n "horse_1:cc_l_legFT01_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  1 6.7726872250000003 3 6.2791359890000003 
		5 3.6104952080080901 7 0 20 0 22 2.5397587179999999 25 6.7726872250000003;
	setAttr -s 7 ".kit[3:6]"  3 3 10 10;
	setAttr -s 7 ".kot[3:6]"  3 3 10 10;
createNode animCurveTL -n "horse_1:cc_l_legFT01_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 11 ".ktv[0:10]"  1 -24 3 11.815306053875503 5 50.418677306059976 
		6 68.24443760462718 7 73.925 10 73.925 13 73.925 16 73.925 19 73.925 20 73.925 25 
		111.839;
	setAttr -s 11 ".kit[7:10]"  3 10 10 1;
	setAttr -s 11 ".kot[7:10]"  3 10 10 1;
	setAttr -s 11 ".kix[10]"  0.0032362211495637894;
	setAttr -s 11 ".kiy[10]"  0.99999481439590454;
	setAttr -s 11 ".kox[10]"  0.0032362188212573528;
	setAttr -s 11 ".koy[10]"  0.99999481439590454;
createNode animCurveTA -n "horse_1:cc_l_legFT01_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 25 0;
createNode animCurveTA -n "horse_1:cc_l_legFT01_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 25 0;
createNode animCurveTA -n "horse_1:cc_l_legFT01_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 25 0;
createNode animCurveTU -n "horse_1:cc_l_legFT01_outPutAnimBank_1_fetlock_ft_curl";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  1 0.80639310239999995 3 0 5 0 7 0 10 7.9898335120000015 
		16 32.050505723966936 19 39.026193980000002 20 31.004311220433095 22 14.864759744562072 
		25 0.80639310239999995;
	setAttr -s 10 ".kit[0:9]"  1 10 10 10 10 1 3 10 
		10 1;
	setAttr -s 10 ".kot[0:9]"  1 10 10 10 10 1 3 10 
		10 1;
	setAttr -s 10 ".kix[0:9]"  0.030829513445496559 1 1 1 0.011699482798576355 
		0.013133186846971512 1 0.0051734643056988716 0.0068987654522061348 0.047770518809556961;
	setAttr -s 10 ".kiy[0:9]"  -0.99952471256256104 0 0 0 0.99993151426315308 
		0.99991375207901001 0 -0.99998658895492554 -0.99997621774673462 -0.99885833263397217;
	setAttr -s 10 ".kox[0:9]"  0.03495309129357338 1 1 1 0.011699482798576355 
		0.013133188709616661 1 0.0051734643056988716 0.0068987654522061348 0.047770511358976364;
	setAttr -s 10 ".koy[0:9]"  -0.99938899278640747 0 0 0 0.99993151426315308 
		0.99991375207901001 0 -0.99998658895492554 -0.99997621774673462 -0.99885839223861694;
createNode animCurveTU -n "horse_1:cc_l_legFT01_outPutAnimBank_1_hoof_ft_curl";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 11 ".ktv[0:10]"  1 91.119261550000004 3 79.327465540000006 
		5 42.6 6 20 7 0 13 0 16 0 19 0 20 5 22 71.667959800000006 25 91.119261550000004;
	setAttr -s 11 ".kit[0:10]"  3 10 10 10 10 10 10 10 
		1 10 3;
	setAttr -s 11 ".kot[0:10]"  3 10 10 10 10 10 10 10 
		1 10 3;
	setAttr -s 11 ".kix[8:10]"  0.003308100625872612 0.0024191185366362333 
		1;
	setAttr -s 11 ".kiy[8:10]"  0.99999451637268066 0.99999701976776123 
		0;
	setAttr -s 11 ".kox[8:10]"  0.0033081010915338993 0.0024191185366362333 
		1;
	setAttr -s 11 ".koy[8:10]"  0.99999451637268066 0.99999701976776123 
		0;
createNode animCurveTL -n "horse_1:cc_r_legBK01_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 2 25 2;
createNode animCurveTL -n "horse_1:cc_r_legBK01_outPutAnimBank_1_translateY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  1 0.66162804900000005 2 1.600295979 4 5.8924845149999996 
		7 3.9617743089999999 11 0 23 0 25 0.66162804900000005;
	setAttr -s 7 ".kit[2:6]"  10 1 10 10 1;
	setAttr -s 7 ".kot[2:6]"  10 1 10 10 1;
	setAttr -s 7 ".kix[0:6]"  0.065717160701751709 0.034040134400129318 
		0.087880238890647888 0.033191870898008347 1 1 0.085521973669528961;
	setAttr -s 7 ".kiy[0:6]"  0.99783825874328613 0.99942046403884888 
		0.99613106250762939 -0.99944901466369629 0 0 0.99633628129959106;
	setAttr -s 7 ".kox[0:6]"  0.063353054225444794 0.034040126949548721 
		0.087880238890647888 0.033191867172718048 1 1 0.085521973669528961;
	setAttr -s 7 ".koy[0:6]"  0.99799120426177979 0.99942046403884888 
		0.99613106250762939 -0.99944901466369629 0 0 0.99633628129959106;
createNode animCurveTL -n "horse_1:cc_r_legBK01_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 -39.843054270000003 2 -39.757884881500765 
		4 -26.081305741500763 11 95.996 23 95.996 25 95.995703001577638;
	setAttr -s 6 ".kit[1:5]"  1 10 10 10 10;
	setAttr -s 6 ".kot[1:5]"  1 10 10 10 10;
	setAttr -s 6 ".kix[1:5]"  0.020598143339157104 0.0027623414061963558 
		1 1 1;
	setAttr -s 6 ".kiy[1:5]"  0.99978786706924438 0.99999618530273438 
		0 0 0;
	setAttr -s 6 ".kox[1:5]"  0.020598134025931358 0.0027623414061963558 
		1 1 1;
	setAttr -s 6 ".koy[1:5]"  0.99978786706924438 0.99999618530273438 
		0 0 0;
createNode animCurveTA -n "horse_1:cc_r_legBK01_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 25 0;
createNode animCurveTA -n "horse_1:cc_r_legBK01_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 25 0;
createNode animCurveTA -n "horse_1:cc_r_legBK01_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 25 0;
createNode animCurveTU -n "horse_1:cc_r_legBK01_outPutAnimBank_1_fetlock_bk_curl";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  1 -10.76319988 2 -16.144799920000001 4 
		-21.7 7 -10.85000097 11 0 23 0 25 -10.76319988;
createNode animCurveTU -n "horse_1:cc_r_legBK01_outPutAnimBank_1_hoof_bk_curl";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  1 44.607464870000001 2 63.726205419999999 
		4 82.322907490000006 7 61.947113889999997 11 0 23 0 25 44.607464870000001;
	setAttr -s 7 ".kit[1:6]"  1 10 10 10 10 1;
	setAttr -s 7 ".kot[1:6]"  1 10 10 10 10 1;
	setAttr -s 7 ".kix[1:6]"  0.0030583408661186695 0.11630622297525406 
		0.0035429368726909161 1 1 0.0012734556803479791;
	setAttr -s 7 ".kiy[1:6]"  0.99999535083770752 -0.99321335554122925 
		-0.99999374151229858 0 0 0.99999922513961792;
	setAttr -s 7 ".kox[1:6]"  0.0030583399347960949 0.11630622297525406 
		0.0035429368726909161 1 1 0.0012414668453857303;
	setAttr -s 7 ".koy[1:6]"  0.99999535083770752 -0.99321335554122925 
		-0.99999374151229858 0 0 0.99999922513961792;
createNode animCurveTL -n "horse_1:cc_l_legBK01_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 -2 25 -2;
createNode animCurveTL -n "horse_1:cc_l_legBK01_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  1 0 11 0 14 1.600295979 16 5.9875502320000002 
		20 4.020357894 22 0 25 0;
	setAttr -s 7 ".kit[5:6]"  3 10;
	setAttr -s 7 ".kot[5:6]"  3 10;
createNode animCurveTL -n "horse_1:cc_l_legBK01_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 26.323352310000001 11 26.323 14 27.498780302020378 
		20 129.70535537596629 22 162.162 25 162.16210958157768;
	setAttr -s 6 ".kit[2:5]"  1 10 10 3;
	setAttr -s 6 ".kot[2:5]"  1 10 10 3;
	setAttr -s 6 ".kix[2:5]"  0.013050094246864319 0.0024753035977482796 
		1 1;
	setAttr -s 6 ".kiy[2:5]"  0.99991488456726074 0.99999696016311646 
		0 0;
	setAttr -s 6 ".kox[2:5]"  0.013050089590251446 0.0024753035977482796 
		1 1;
	setAttr -s 6 ".koy[2:5]"  0.99991488456726074 0.99999696016311646 
		0 0;
createNode animCurveTA -n "horse_1:cc_l_legBK01_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 25 0;
createNode animCurveTA -n "horse_1:cc_l_legBK01_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 25 0;
createNode animCurveTA -n "horse_1:cc_l_legBK01_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 25 0;
createNode animCurveTU -n "horse_1:cc_l_legBK01_outPutAnimBank_1_fetlock_bk_curl";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  1 0 11 0 14 -13.607994809999999 16 -21 
		20 -13.12500013 22 0 25 0;
	setAttr -s 7 ".kit[5:6]"  3 10;
	setAttr -s 7 ".kot[5:6]"  3 10;
createNode animCurveTU -n "horse_1:cc_l_legBK01_outPutAnimBank_1_hoof_bk_curl";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  1 0 11 0 14 65.068568420000005 16 84.787207199999997 
		20 36.066489390000001 22 0 25 0;
	setAttr -s 7 ".kit[5:6]"  3 10;
	setAttr -s 7 ".kot[5:6]"  3 10;
createNode animCurveTL -n "horse_1:cc_tail01_outPutAnimBank_1_translateX";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 -0.10451099272243458 2 -0.065159558996939038 
		8 -0.59640391429113104 14 -0.065159558996939038 20 -0.59640391429113104 25 -0.10451111586271955;
	setAttr -s 6 ".kit[0:5]"  1 3 3 3 3 1;
	setAttr -s 6 ".kot[0:5]"  1 3 3 3 3 1;
	setAttr -s 6 ".kix[0:5]"  0.47324028611183167 1 1 1 1 0.46088972687721252;
	setAttr -s 6 ".kiy[0:5]"  0.88093334436416626 0 0 0 0 0.88745737075805664;
	setAttr -s 6 ".kox[0:5]"  0.47324025630950928 1 1 1 1 0.46088951826095581;
	setAttr -s 6 ".koy[0:5]"  0.88093340396881104 0 0 0 0 0.88745754957199097;
createNode animCurveTL -n "horse_1:cc_tail01_outPutAnimBank_1_translateY";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 3.2431787090734909 2 3.4887912900941247 
		8 0.17302144631556793 14 3.4887912900941247 20 0.17302144631556793 25 3.2431779404915022;
	setAttr -s 6 ".kit[0:5]"  10 3 3 3 3 1;
	setAttr -s 6 ".kot[0:5]"  10 3 3 3 3 1;
	setAttr -s 6 ".kix[5]"  0.086387984454631805;
	setAttr -s 6 ".kiy[5]"  0.9962615966796875;
	setAttr -s 6 ".kox[5]"  0.086387984454631805;
	setAttr -s 6 ".koy[5]"  0.9962615966796875;
createNode animCurveTL -n "horse_1:cc_tail01_outPutAnimBank_1_translateZ";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 -0.17252660309127221 2 -0.036998097564437282 
		8 -1.8666329221767142 14 -0.036998097564437282 20 -1.8666329221767142 25 -0.1725270271931969;
	setAttr -s 6 ".kit[0:5]"  10 3 3 3 3 1;
	setAttr -s 6 ".kot[0:5]"  10 3 3 3 3 1;
	setAttr -s 6 ".kix[5]"  0.16441686451435089;
	setAttr -s 6 ".kiy[5]"  0.98639094829559326;
	setAttr -s 6 ".kox[5]"  0.16441687941551208;
	setAttr -s 6 ".koy[5]"  0.98639094829559326;
createNode animCurveTL -n "horse_1:cc_tail02_outPutAnimBank_1_translateX";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 0.010916897952015281 2 0.032579779498469914 
		8 -0.25986912137866697 14 0.032579779498469914 20 -0.25986912137866697 25 0.010916830163547386;
	setAttr -s 6 ".kit[0:5]"  1 3 3 3 3 1;
	setAttr -s 6 ".kot[0:5]"  1 3 3 3 3 1;
	setAttr -s 6 ".kix[0:5]"  0.67093491554260254 1 1 1 1 0.6966739296913147;
	setAttr -s 6 ".kiy[0:5]"  0.74151623249053955 0 0 0 0 0.71738797426223755;
	setAttr -s 6 ".kox[0:5]"  0.69174784421920776 1 1 1 1 0.6966739296913147;
	setAttr -s 6 ".koy[0:5]"  0.72213917970657349 0 0 0 0 0.71738797426223755;
createNode animCurveTL -n "horse_1:cc_tail02_outPutAnimBank_1_translateY";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 6.2413457749252217 2 6.425384720202695 
		8 3.9408589589567988 14 6.425384720202695 20 3.9408589589567988 25 6.2413451990222359;
	setAttr -s 6 ".kit[0:5]"  1 3 3 3 3 1;
	setAttr -s 6 ".kot[0:5]"  1 3 3 3 3 1;
	setAttr -s 6 ".kix[0:5]"  0.10814732313156128 1 1 1 1 0.11674821376800537;
	setAttr -s 6 ".kiy[0:5]"  0.99413490295410156 0 0 0 0 0.99316155910491943;
	setAttr -s 6 ".kox[0:5]"  0.10785516351461411 1 1 1 1 0.11674822121858597;
	setAttr -s 6 ".koy[0:5]"  0.99416661262512207 0 0 0 0 0.99316155910491943;
createNode animCurveTL -n "horse_1:cc_tail02_outPutAnimBank_1_translateZ";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 6.0360408841575817 2 6.334286227590276 
		8 2.3079740912488953 14 6.334286227590276 20 2.3079740912488953 25 6.0360399508747742;
	setAttr -s 6 ".kit[0:5]"  1 3 3 3 3 1;
	setAttr -s 6 ".kot[0:5]"  1 3 3 3 3 1;
	setAttr -s 6 ".kix[0:5]"  0.071998715400695801 1 1 1 1 0.072974495589733124;
	setAttr -s 6 ".kiy[0:5]"  0.99740475416183472 0 0 0 0 0.997333824634552;
	setAttr -s 6 ".kox[0:5]"  0.070838674902915955 1 1 1 1 0.072974510490894318;
	setAttr -s 6 ".koy[0:5]"  0.99748778343200684 0 0 0 0 0.997333824634552;
createNode animCurveTL -n "horse_1:cc_tail03_outPutAnimBank_1_translateX";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 -0.093328889128966641 4 0 10 -0.18665777825793334 
		16 0 22 -0.18665777825793334 25 -0.093328922505986303;
	setAttr -s 6 ".kit[0:5]"  1 3 3 3 3 1;
	setAttr -s 6 ".kot[0:5]"  1 3 3 3 3 1;
	setAttr -s 6 ".kix[0:5]"  0.67560309171676636 1 1 1 1 0.66204297542572021;
	setAttr -s 6 ".kiy[0:5]"  0.73726552724838257 0 0 0 0 0.74946600198745728;
	setAttr -s 6 ".kox[0:5]"  0.6879572868347168 1 1 1 1 0.66204297542572021;
	setAttr -s 6 ".koy[0:5]"  0.72575122117996216 0 0 0 0 0.7494659423828125;
createNode animCurveTL -n "horse_1:cc_tail03_outPutAnimBank_1_translateY";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 15.754221193331995 4 17.542268 10 13.96617438666399 
		16 17.542268 22 13.96617438666399 25 15.754220553876474;
	setAttr -s 6 ".kit[0:5]"  1 3 3 3 3 1;
	setAttr -s 6 ".kot[0:5]"  1 3 3 3 3 1;
	setAttr -s 6 ".kix[0:5]"  0.047362331300973892 1 1 1 1 0.042912255972623825;
	setAttr -s 6 ".kiy[0:5]"  0.9988778829574585 0 0 0 0 0.99907886981964111;
	setAttr -s 6 ".kox[0:5]"  0.045800667256116867 1 1 1 1 0.04291226714849472;
	setAttr -s 6 ".koy[0:5]"  0.99895060062408447 0 0 0 0 0.99907886981964111;
createNode animCurveTL -n "horse_1:cc_tail03_outPutAnimBank_1_translateZ";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 6.5787081529163167 3 7.2896111722864516 
		9 4.5475565989562803 15 7.2896111722864516 21 4.5475565989562803 25 6.5787075536392221;
	setAttr -s 6 ".kit[0:5]"  1 3 3 3 3 1;
	setAttr -s 6 ".kot[0:5]"  1 3 3 3 3 1;
	setAttr -s 6 ".kix[0:5]"  0.065553136169910431 1 1 1 1 0.068856194615364075;
	setAttr -s 6 ".kiy[0:5]"  0.99784910678863525 0 0 0 0 0.99762660264968872;
	setAttr -s 6 ".kox[0:5]"  0.070166260004043579 1 1 1 1 0.068856187164783478;
	setAttr -s 6 ".koy[0:5]"  0.9975353479385376 0 0 0 0 0.99762660264968872;
createNode animCurveTL -n "horse_1:cc_cc_tail04_outPutAnimBank_1_translateX";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0.0029272198474993849 4 0.29321801548623194 
		10 0.43167229678583108 22 -0.28736357579123312 25 0.0029271160313961708;
	setAttr -s 5 ".kit[2:4]"  3 3 1;
	setAttr -s 5 ".kot[2:4]"  3 3 1;
	setAttr -s 5 ".kix[0:4]"  0.26272767782211304 0.73161345720291138 
		1 1 0.26634946465492249;
	setAttr -s 5 ".kiy[0:4]"  0.96487003564834595 0.68171977996826172 
		0 0 0.96387654542922974;
	setAttr -s 5 ".kox[0:4]"  0.28257700800895691 0.73161345720291138 
		1 1 0.2663494348526001;
	setAttr -s 5 ".koy[0:4]"  0.95924460887908936 0.68171977996826172 
		0 0 0.96387654542922974;
createNode animCurveTL -n "horse_1:cc_cc_tail04_outPutAnimBank_1_translateY";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 23.427912275337807 4 24.655343153586404 
		10 22.500746969825361 16 24.655343153586404 22 22.200481397089209 25 23.427911836374214;
	setAttr -s 6 ".kit[0:5]"  1 3 3 3 3 1;
	setAttr -s 6 ".kot[0:5]"  1 3 3 3 3 1;
	setAttr -s 6 ".kix[0:5]"  0.069634325802326202 1 1 1 1 0.06672484427690506;
	setAttr -s 6 ".kiy[0:5]"  0.99757254123687744 0 0 0 0 0.99777144193649292;
	setAttr -s 6 ".kox[0:5]"  0.070662535727024078 1 1 1 1 0.066724807024002075;
	setAttr -s 6 ".koy[0:5]"  0.99750030040740967 0 0 0 0 0.99777144193649292;
createNode animCurveTL -n "horse_1:cc_cc_tail04_outPutAnimBank_1_translateZ";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 6.243265101044055 4 8.0948499277915467 
		10 4.276298355115058 16 8.0948499277915467 22 4.3916802742965633 25 6.2432644388655625;
	setAttr -s 6 ".kit[0:5]"  1 3 3 3 3 1;
	setAttr -s 6 ".kot[0:5]"  1 3 3 3 3 1;
	setAttr -s 6 ".kix[0:5]"  0.048257399350404739 1 1 1 1 0.043888192623853683;
	setAttr -s 6 ".kiy[0:5]"  0.99883490800857544 0 0 0 0 0.99903643131256104;
	setAttr -s 6 ".kox[0:5]"  0.046815570443868637 1 1 1 1 0.043888192623853683;
	setAttr -s 6 ".koy[0:5]"  0.99890357255935669 0 0 0 0 0.99903643131256104;
createNode animCurveTL -n "horse_1:cc_tail05_outPutAnimBank_1_translateX";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 0.015811142556790128 5 0.065159558996944797 
		11 -0.0014608049841614607 17 0.065159558996944797 23 -0.0014608049841614607 25 0.015811127114471857;
	setAttr -s 6 ".kit[0:5]"  1 3 3 3 3 1;
	setAttr -s 6 ".kot[0:5]"  1 3 3 3 3 1;
	setAttr -s 6 ".kix[0:5]"  0.92118877172470093 1 1 1 1 0.93431055545806885;
	setAttr -s 6 ".kiy[0:5]"  0.38911595940589905 0 0 0 0 0.35646030306816101;
	setAttr -s 6 ".kox[0:5]"  0.93967157602310181 1 1 1 1 0.93431049585342407;
	setAttr -s 6 ".koy[0:5]"  0.34207797050476074 0 0 0 0 0.3564603328704834;
createNode animCurveTL -n "horse_1:cc_tail05_outPutAnimBank_1_translateY";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 17.249838487977218 6 15.683607781836351 
		12 17.375136952030214 18 15.683607781836351 24 17.375136952030214 25 17.249838719029832;
	setAttr -s 6 ".kit[0:5]"  1 3 3 3 3 1;
	setAttr -s 6 ".kot[0:5]"  1 3 3 3 3 1;
	setAttr -s 6 ".kix[0:5]"  0.17294664680957794 1 1 1 1 0.19132237136363983;
	setAttr -s 6 ".kiy[0:5]"  -0.98493123054504395 0 0 0 0 -0.98152726888656616;
	setAttr -s 6 ".kox[0:5]"  0.17625686526298523 1 1 1 1 0.19132243096828461;
	setAttr -s 6 ".koy[0:5]"  -0.9843442440032959 0 0 0 0 -0.98152726888656616;
createNode animCurveTL -n "horse_1:cc_tail05_outPutAnimBank_1_translateZ";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 6.0466253382662787 5 3.069810061747515 
		11 7.0885107928378019 17 3.069810061747515 23 7.0885107928378019 25 6.0466262697840909;
	setAttr -s 6 ".kit[0:5]"  1 1 3 3 3 1;
	setAttr -s 6 ".kot[0:5]"  1 1 3 3 3 1;
	setAttr -s 6 ".kix[0:5]"  0.046278826892375946 0.92057532072067261 
		1 1 1 0.044895421713590622;
	setAttr -s 6 ".kiy[0:5]"  -0.99892854690551758 -0.39056527614593506 
		0 0 0 -0.99899172782897949;
	setAttr -s 6 ".kox[0:5]"  0.047734275460243225 0.92057520151138306 
		1 1 1 0.044895421713590622;
	setAttr -s 6 ".koy[0:5]"  -0.99886006116867065 -0.390565425157547 
		0 0 0 -0.99899172782897949;
createNode animCurveTL -n "horse_1:cc_tail06_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 0.31425293832637391 6 2.8731861133169314 
		9 2.3232229152178441 18 -3.8975909587200648 22 -1.8374215200414754 25 0.31425186014476991;
	setAttr -s 6 ".kit[0:5]"  1 3 10 3 10 10;
	setAttr -s 6 ".kot[0:5]"  1 3 10 3 10 10;
	setAttr -s 6 ".kix[0:5]"  0.058581028133630753 1 0.073646225035190582 
		1 0.069083727896213531 0.057996507734060287;
	setAttr -s 6 ".kiy[0:5]"  0.99828267097473145 0 -0.99728435277938843 
		0 0.99761086702346802 0.99831682443618774;
	setAttr -s 6 ".kox[0:5]"  0.059075459837913513 1 0.073646225035190582 
		1 0.069083727896213531 0.057996507734060287;
	setAttr -s 6 ".koy[0:5]"  0.99825352430343628 0 -0.99728435277938843 
		0 0.99761086702346802 0.99831682443618774;
createNode animCurveTL -n "horse_1:cc_tail06_outPutAnimBank_1_translateY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 15.718282158100571 5 16.614618648606353 
		11 15.488379 17 16.762272074276478 23 15.448139843517863 25 15.718281904790574;
	setAttr -s 6 ".kit[4:5]"  3 1;
	setAttr -s 6 ".kot[4:5]"  3 1;
	setAttr -s 6 ".kix[0:5]"  0.16463793814182281 0.49763461947441101 
		0.71580958366394043 0.97990196943283081 1 0.17920677363872528;
	setAttr -s 6 ".kiy[0:5]"  0.98635405302047729 0.86738681793212891 
		0.69829559326171875 0.1994798481464386 0 0.98381149768829346;
	setAttr -s 6 ".kox[0:5]"  0.1746535450220108 0.49763453006744385 
		0.71580946445465088 0.97990190982818604 1 0.17920677363872528;
	setAttr -s 6 ".koy[0:5]"  0.98462998867034912 0.86738681793212891 
		0.69829565286636353 0.19947986304759979 0 0.98381149768829346;
createNode animCurveTL -n "horse_1:cc_tail06_outPutAnimBank_1_translateZ";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 2.8378089597163085 6 -1.6858677479877302 
		12 3.1900261954111895 18 -1.6858677479877302 24 3.1997031181728355 25 2.8378096270556195;
	setAttr -s 6 ".kit[1:5]"  3 10 3 1 1;
	setAttr -s 6 ".kot[1:5]"  3 10 3 1 1;
	setAttr -s 6 ".kix[0:5]"  0.057297799736261368 1 1 1 0.98024404048919678 
		0.059043630957603455;
	setAttr -s 6 ".kiy[0:5]"  -0.99835711717605591 0 0 0 -0.19779181480407715 
		-0.99825543165206909;
	setAttr -s 6 ".kox[0:5]"  0.05835864320397377 1 1 1 0.98024433851242065 
		0.059043649584054947;
	setAttr -s 6 ".koy[0:5]"  -0.99829566478729248 0 0 0 -0.19779033958911896 
		-0.99825543165206909;
select -ne :time1;
	setAttr ".o" 1;
	setAttr ".unw" 1;
select -ne :renderPartition;
	setAttr -s 5 ".st";
select -ne :initialShadingGroup;
	setAttr ".ro" yes;
select -ne :initialParticleSE;
	setAttr ".ro" yes;
select -ne :defaultShaderList1;
	setAttr -s 5 ".s";
select -ne :defaultTextureList1;
select -ne :postProcessList1;
	setAttr -s 2 ".p";
select -ne :defaultRenderUtilityList1;
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
select -ne :characterPartition;
select -ne :ikSystem;
	setAttr -s 2 ".sol";
connectAttr "horse_1:cc_COG01_outPutAnimBank_1_translateX.o" "horse_1:cc_COG01_outPutAnimBank_1.tx"
		;
connectAttr "horse_1:cc_COG01_outPutAnimBank_1_translateY.o" "horse_1:cc_COG01_outPutAnimBank_1.ty"
		;
connectAttr "horse_1:cc_COG01_outPutAnimBank_1_translateZ.o" "horse_1:cc_COG01_outPutAnimBank_1.tz"
		;
connectAttr "horse_1:cc_COG01_outPutAnimBank_1_rotateX.o" "horse_1:cc_COG01_outPutAnimBank_1.rx"
		;
connectAttr "horse_1:cc_COG01_outPutAnimBank_1_rotateY.o" "horse_1:cc_COG01_outPutAnimBank_1.ry"
		;
connectAttr "horse_1:cc_COG01_outPutAnimBank_1_rotateZ.o" "horse_1:cc_COG01_outPutAnimBank_1.rz"
		;
connectAttr "horse_1:cc_COG01_outPutAnimBank_1_tr_curl.o" "horse_1:cc_COG01_outPutAnimBank_1.tr_curl"
		;
connectAttr "horse_1:cc_COG01_outPutAnimBank_1_tr_sway.o" "horse_1:cc_COG01_outPutAnimBank_1.tr_sway"
		;
connectAttr "horse_1:cc_COG01_outPutAnimBank_1_tr_turn.o" "horse_1:cc_COG01_outPutAnimBank_1.tr_turn"
		;
connectAttr "horse_1:cc_midVertebraet01_outPutAnimBank_1_translateX.o" "horse_1:cc_midVertebraet01_outPutAnimBank_1.tx"
		;
connectAttr "horse_1:cc_midVertebraet01_outPutAnimBank_1_translateY.o" "horse_1:cc_midVertebraet01_outPutAnimBank_1.ty"
		;
connectAttr "horse_1:cc_midVertebraet01_outPutAnimBank_1_translateZ.o" "horse_1:cc_midVertebraet01_outPutAnimBank_1.tz"
		;
connectAttr "horse_1:cc_midVertebraet01_outPutAnimBank_1_rotateX.o" "horse_1:cc_midVertebraet01_outPutAnimBank_1.rx"
		;
connectAttr "horse_1:cc_midVertebraet01_outPutAnimBank_1_rotateY.o" "horse_1:cc_midVertebraet01_outPutAnimBank_1.ry"
		;
connectAttr "horse_1:cc_midVertebraet01_outPutAnimBank_1_rotateZ.o" "horse_1:cc_midVertebraet01_outPutAnimBank_1.rz"
		;
connectAttr "horse_1:cc_thoracic01_outPutAnimBank_1_translateX.o" "horse_1:cc_thoracic01_outPutAnimBank_1.tx"
		;
connectAttr "horse_1:cc_thoracic01_outPutAnimBank_1_translateY.o" "horse_1:cc_thoracic01_outPutAnimBank_1.ty"
		;
connectAttr "horse_1:cc_thoracic01_outPutAnimBank_1_translateZ.o" "horse_1:cc_thoracic01_outPutAnimBank_1.tz"
		;
connectAttr "horse_1:cc_thoracic01_outPutAnimBank_1_rotateX.o" "horse_1:cc_thoracic01_outPutAnimBank_1.rx"
		;
connectAttr "horse_1:cc_thoracic01_outPutAnimBank_1_rotateY.o" "horse_1:cc_thoracic01_outPutAnimBank_1.ry"
		;
connectAttr "horse_1:cc_thoracic01_outPutAnimBank_1_rotateZ.o" "horse_1:cc_thoracic01_outPutAnimBank_1.rz"
		;
connectAttr "horse_1:cc_thoracic01_outPutAnimBank_1_lock.o" "horse_1:cc_thoracic01_outPutAnimBank_1.lock"
		;
connectAttr "horse_1:cc_hipSway01_outPutAnimBank_1_translateX.o" "horse_1:cc_hipSway01_outPutAnimBank_1.tx"
		;
connectAttr "horse_1:cc_hipSway01_outPutAnimBank_1_translateY.o" "horse_1:cc_hipSway01_outPutAnimBank_1.ty"
		;
connectAttr "horse_1:cc_hipSway01_outPutAnimBank_1_translateZ.o" "horse_1:cc_hipSway01_outPutAnimBank_1.tz"
		;
connectAttr "horse_1:cc_hipSway01_outPutAnimBank_1_rotateX.o" "horse_1:cc_hipSway01_outPutAnimBank_1.rx"
		;
connectAttr "horse_1:cc_hipSway01_outPutAnimBank_1_rotateY.o" "horse_1:cc_hipSway01_outPutAnimBank_1.ry"
		;
connectAttr "horse_1:cc_hipSway01_outPutAnimBank_1_rotateZ.o" "horse_1:cc_hipSway01_outPutAnimBank_1.rz"
		;
connectAttr "horse_1:cc_r_shoulder01_outPutAnimBank_1_translateX.o" "horse_1:cc_r_shoulder01_outPutAnimBank_1.tx"
		;
connectAttr "horse_1:cc_r_shoulder01_outPutAnimBank_1_translateY.o" "horse_1:cc_r_shoulder01_outPutAnimBank_1.ty"
		;
connectAttr "horse_1:cc_r_shoulder01_outPutAnimBank_1_translateZ.o" "horse_1:cc_r_shoulder01_outPutAnimBank_1.tz"
		;
connectAttr "horse_1:cc_r_shoulder01_outPutAnimBank_1_rotateX.o" "horse_1:cc_r_shoulder01_outPutAnimBank_1.rx"
		;
connectAttr "horse_1:cc_r_shoulder01_outPutAnimBank_1_rotateY.o" "horse_1:cc_r_shoulder01_outPutAnimBank_1.ry"
		;
connectAttr "horse_1:cc_r_shoulder01_outPutAnimBank_1_rotateZ.o" "horse_1:cc_r_shoulder01_outPutAnimBank_1.rz"
		;
connectAttr "horse_1:cc_l_shoulder01_outPutAnimBank_1_translateX.o" "horse_1:cc_l_shoulder01_outPutAnimBank_1.tx"
		;
connectAttr "horse_1:cc_l_shoulder01_outPutAnimBank_1_translateY.o" "horse_1:cc_l_shoulder01_outPutAnimBank_1.ty"
		;
connectAttr "horse_1:cc_l_shoulder01_outPutAnimBank_1_translateZ.o" "horse_1:cc_l_shoulder01_outPutAnimBank_1.tz"
		;
connectAttr "horse_1:cc_l_shoulder01_outPutAnimBank_1_rotateX.o" "horse_1:cc_l_shoulder01_outPutAnimBank_1.rx"
		;
connectAttr "horse_1:cc_l_shoulder01_outPutAnimBank_1_rotateY.o" "horse_1:cc_l_shoulder01_outPutAnimBank_1.ry"
		;
connectAttr "horse_1:cc_l_shoulder01_outPutAnimBank_1_rotateZ.o" "horse_1:cc_l_shoulder01_outPutAnimBank_1.rz"
		;
connectAttr "horse_1:cc_cervical01_outPutAnimBank_1_translateX.o" "horse_1:cc_cervical01_outPutAnimBank_1.tx"
		;
connectAttr "horse_1:cc_cervical01_outPutAnimBank_1_translateY.o" "horse_1:cc_cervical01_outPutAnimBank_1.ty"
		;
connectAttr "horse_1:cc_cervical01_outPutAnimBank_1_translateZ.o" "horse_1:cc_cervical01_outPutAnimBank_1.tz"
		;
connectAttr "horse_1:cc_cervical01_outPutAnimBank_1_rotateX.o" "horse_1:cc_cervical01_outPutAnimBank_1.rx"
		;
connectAttr "horse_1:cc_cervical01_outPutAnimBank_1_rotateY.o" "horse_1:cc_cervical01_outPutAnimBank_1.ry"
		;
connectAttr "horse_1:cc_cervical01_outPutAnimBank_1_rotateZ.o" "horse_1:cc_cervical01_outPutAnimBank_1.rz"
		;
connectAttr "horse_1:cc_cervical02_outPutAnimBank_1_translateX.o" "horse_1:cc_cervical02_outPutAnimBank_1.tx"
		;
connectAttr "horse_1:cc_cervical02_outPutAnimBank_1_translateY.o" "horse_1:cc_cervical02_outPutAnimBank_1.ty"
		;
connectAttr "horse_1:cc_cervical02_outPutAnimBank_1_translateZ.o" "horse_1:cc_cervical02_outPutAnimBank_1.tz"
		;
connectAttr "horse_1:cc_cervical02_outPutAnimBank_1_rotateX.o" "horse_1:cc_cervical02_outPutAnimBank_1.rx"
		;
connectAttr "horse_1:cc_cervical02_outPutAnimBank_1_rotateY.o" "horse_1:cc_cervical02_outPutAnimBank_1.ry"
		;
connectAttr "horse_1:cc_cervical02_outPutAnimBank_1_rotateZ.o" "horse_1:cc_cervical02_outPutAnimBank_1.rz"
		;
connectAttr "horse_1:cc_head01_outPutAnimBank_1_translateX.o" "horse_1:cc_head01_outPutAnimBank_1.tx"
		;
connectAttr "horse_1:cc_head01_outPutAnimBank_1_translateY.o" "horse_1:cc_head01_outPutAnimBank_1.ty"
		;
connectAttr "horse_1:cc_head01_outPutAnimBank_1_translateZ.o" "horse_1:cc_head01_outPutAnimBank_1.tz"
		;
connectAttr "horse_1:cc_head01_outPutAnimBank_1_rotateX.o" "horse_1:cc_head01_outPutAnimBank_1.rx"
		;
connectAttr "horse_1:cc_head01_outPutAnimBank_1_rotateY.o" "horse_1:cc_head01_outPutAnimBank_1.ry"
		;
connectAttr "horse_1:cc_head01_outPutAnimBank_1_rotateZ.o" "horse_1:cc_head01_outPutAnimBank_1.rz"
		;
connectAttr "horse_1:cc_head01_outPutAnimBank_1_ear_r_rootCurl.o" "horse_1:cc_head01_outPutAnimBank_1.ear_r_rootCurl"
		;
connectAttr "horse_1:cc_head01_outPutAnimBank_1_ear_r_rootTurn.o" "horse_1:cc_head01_outPutAnimBank_1.ear_r_rootTurn"
		;
connectAttr "horse_1:cc_head01_outPutAnimBank_1_ear_r_rootSway.o" "horse_1:cc_head01_outPutAnimBank_1.ear_r_rootSway"
		;
connectAttr "horse_1:cc_head01_outPutAnimBank_1_ear_r_midCurl.o" "horse_1:cc_head01_outPutAnimBank_1.ear_r_midCurl"
		;
connectAttr "horse_1:cc_head01_outPutAnimBank_1_ear_r_midTurn.o" "horse_1:cc_head01_outPutAnimBank_1.ear_r_midTurn"
		;
connectAttr "horse_1:cc_head01_outPutAnimBank_1_ear_r_midSway.o" "horse_1:cc_head01_outPutAnimBank_1.ear_r_midSway"
		;
connectAttr "horse_1:cc_head01_outPutAnimBank_1_ear_l_rootCurl.o" "horse_1:cc_head01_outPutAnimBank_1.ear_l_rootCurl"
		;
connectAttr "horse_1:cc_head01_outPutAnimBank_1_ear_l_rootTurn.o" "horse_1:cc_head01_outPutAnimBank_1.ear_l_rootTurn"
		;
connectAttr "horse_1:cc_head01_outPutAnimBank_1_ear_l_rootSway.o" "horse_1:cc_head01_outPutAnimBank_1.ear_l_rootSway"
		;
connectAttr "horse_1:cc_head01_outPutAnimBank_1_ear_l_midCurl.o" "horse_1:cc_head01_outPutAnimBank_1.ear_l_midCurl"
		;
connectAttr "horse_1:cc_head01_outPutAnimBank_1_ear_l_midTurn.o" "horse_1:cc_head01_outPutAnimBank_1.ear_l_midTurn"
		;
connectAttr "horse_1:cc_head01_outPutAnimBank_1_ear_l_midSway.o" "horse_1:cc_head01_outPutAnimBank_1.ear_l_midSway"
		;
connectAttr "horse_1:cc_l_carpalFT01_outPutAnimBank_1_translateX.o" "horse_1:cc_l_carpalFT01_outPutAnimBank_1.tx"
		;
connectAttr "horse_1:cc_l_carpalFT01_outPutAnimBank_1_translateY.o" "horse_1:cc_l_carpalFT01_outPutAnimBank_1.ty"
		;
connectAttr "horse_1:cc_l_carpalFT01_outPutAnimBank_1_translateZ.o" "horse_1:cc_l_carpalFT01_outPutAnimBank_1.tz"
		;
connectAttr "horse_1:cc_r_carpalFT01_outPutAnimBank_1_translateX.o" "horse_1:cc_r_carpalFT01_outPutAnimBank_1.tx"
		;
connectAttr "horse_1:cc_r_carpalFT01_outPutAnimBank_1_translateY.o" "horse_1:cc_r_carpalFT01_outPutAnimBank_1.ty"
		;
connectAttr "horse_1:cc_r_carpalFT01_outPutAnimBank_1_translateZ.o" "horse_1:cc_r_carpalFT01_outPutAnimBank_1.tz"
		;
connectAttr "horse_1:cc_r_tarsalFT01_outPutAnimBank_1_translateX.o" "horse_1:cc_r_tarsalFT01_outPutAnimBank_1.tx"
		;
connectAttr "horse_1:cc_r_tarsalFT01_outPutAnimBank_1_translateY.o" "horse_1:cc_r_tarsalFT01_outPutAnimBank_1.ty"
		;
connectAttr "horse_1:cc_r_tarsalFT01_outPutAnimBank_1_translateZ.o" "horse_1:cc_r_tarsalFT01_outPutAnimBank_1.tz"
		;
connectAttr "horse_1:cc_l_tarsalFT01_outPutAnimBank_1_translateX.o" "horse_1:cc_l_tarsalFT01_outPutAnimBank_1.tx"
		;
connectAttr "horse_1:cc_l_tarsalFT01_outPutAnimBank_1_translateY.o" "horse_1:cc_l_tarsalFT01_outPutAnimBank_1.ty"
		;
connectAttr "horse_1:cc_l_tarsalFT01_outPutAnimBank_1_translateZ.o" "horse_1:cc_l_tarsalFT01_outPutAnimBank_1.tz"
		;
connectAttr "horse_1:cc_r_legFT01_outPutAnimBank_1_translateX.o" "horse_1:cc_r_legFT01_outPutAnimBank_1.tx"
		;
connectAttr "horse_1:cc_r_legFT01_outPutAnimBank_1_translateY.o" "horse_1:cc_r_legFT01_outPutAnimBank_1.ty"
		;
connectAttr "horse_1:cc_r_legFT01_outPutAnimBank_1_translateZ.o" "horse_1:cc_r_legFT01_outPutAnimBank_1.tz"
		;
connectAttr "horse_1:cc_r_legFT01_outPutAnimBank_1_rotateX.o" "horse_1:cc_r_legFT01_outPutAnimBank_1.rx"
		;
connectAttr "horse_1:cc_r_legFT01_outPutAnimBank_1_rotateY.o" "horse_1:cc_r_legFT01_outPutAnimBank_1.ry"
		;
connectAttr "horse_1:cc_r_legFT01_outPutAnimBank_1_rotateZ.o" "horse_1:cc_r_legFT01_outPutAnimBank_1.rz"
		;
connectAttr "horse_1:cc_r_legFT01_outPutAnimBank_1_fetlock_ft_curl.o" "horse_1:cc_r_legFT01_outPutAnimBank_1.fetlock_ft_curl"
		;
connectAttr "horse_1:cc_r_legFT01_outPutAnimBank_1_hoof_ft_curl.o" "horse_1:cc_r_legFT01_outPutAnimBank_1.hoof_ft_curl"
		;
connectAttr "horse_1:cc_l_legFT01_outPutAnimBank_1_translateX.o" "horse_1:cc_l_legFT01_outPutAnimBank_1.tx"
		;
connectAttr "horse_1:cc_l_legFT01_outPutAnimBank_1_translateY.o" "horse_1:cc_l_legFT01_outPutAnimBank_1.ty"
		;
connectAttr "horse_1:cc_l_legFT01_outPutAnimBank_1_translateZ.o" "horse_1:cc_l_legFT01_outPutAnimBank_1.tz"
		;
connectAttr "horse_1:cc_l_legFT01_outPutAnimBank_1_rotateX.o" "horse_1:cc_l_legFT01_outPutAnimBank_1.rx"
		;
connectAttr "horse_1:cc_l_legFT01_outPutAnimBank_1_rotateY.o" "horse_1:cc_l_legFT01_outPutAnimBank_1.ry"
		;
connectAttr "horse_1:cc_l_legFT01_outPutAnimBank_1_rotateZ.o" "horse_1:cc_l_legFT01_outPutAnimBank_1.rz"
		;
connectAttr "horse_1:cc_l_legFT01_outPutAnimBank_1_fetlock_ft_curl.o" "horse_1:cc_l_legFT01_outPutAnimBank_1.fetlock_ft_curl"
		;
connectAttr "horse_1:cc_l_legFT01_outPutAnimBank_1_hoof_ft_curl.o" "horse_1:cc_l_legFT01_outPutAnimBank_1.hoof_ft_curl"
		;
connectAttr "horse_1:cc_r_legBK01_outPutAnimBank_1_translateX.o" "horse_1:cc_r_legBK01_outPutAnimBank_1.tx"
		;
connectAttr "horse_1:cc_r_legBK01_outPutAnimBank_1_translateY.o" "horse_1:cc_r_legBK01_outPutAnimBank_1.ty"
		;
connectAttr "horse_1:cc_r_legBK01_outPutAnimBank_1_translateZ.o" "horse_1:cc_r_legBK01_outPutAnimBank_1.tz"
		;
connectAttr "horse_1:cc_r_legBK01_outPutAnimBank_1_rotateX.o" "horse_1:cc_r_legBK01_outPutAnimBank_1.rx"
		;
connectAttr "horse_1:cc_r_legBK01_outPutAnimBank_1_rotateY.o" "horse_1:cc_r_legBK01_outPutAnimBank_1.ry"
		;
connectAttr "horse_1:cc_r_legBK01_outPutAnimBank_1_rotateZ.o" "horse_1:cc_r_legBK01_outPutAnimBank_1.rz"
		;
connectAttr "horse_1:cc_r_legBK01_outPutAnimBank_1_fetlock_bk_curl.o" "horse_1:cc_r_legBK01_outPutAnimBank_1.fetlock_bk_curl"
		;
connectAttr "horse_1:cc_r_legBK01_outPutAnimBank_1_hoof_bk_curl.o" "horse_1:cc_r_legBK01_outPutAnimBank_1.hoof_bk_curl"
		;
connectAttr "horse_1:cc_l_legBK01_outPutAnimBank_1_translateX.o" "horse_1:cc_l_legBK01_outPutAnimBank_1.tx"
		;
connectAttr "horse_1:cc_l_legBK01_outPutAnimBank_1_translateY.o" "horse_1:cc_l_legBK01_outPutAnimBank_1.ty"
		;
connectAttr "horse_1:cc_l_legBK01_outPutAnimBank_1_translateZ.o" "horse_1:cc_l_legBK01_outPutAnimBank_1.tz"
		;
connectAttr "horse_1:cc_l_legBK01_outPutAnimBank_1_rotateX.o" "horse_1:cc_l_legBK01_outPutAnimBank_1.rx"
		;
connectAttr "horse_1:cc_l_legBK01_outPutAnimBank_1_rotateY.o" "horse_1:cc_l_legBK01_outPutAnimBank_1.ry"
		;
connectAttr "horse_1:cc_l_legBK01_outPutAnimBank_1_rotateZ.o" "horse_1:cc_l_legBK01_outPutAnimBank_1.rz"
		;
connectAttr "horse_1:cc_l_legBK01_outPutAnimBank_1_fetlock_bk_curl.o" "horse_1:cc_l_legBK01_outPutAnimBank_1.fetlock_bk_curl"
		;
connectAttr "horse_1:cc_l_legBK01_outPutAnimBank_1_hoof_bk_curl.o" "horse_1:cc_l_legBK01_outPutAnimBank_1.hoof_bk_curl"
		;
connectAttr "horse_1:cc_tail01_outPutAnimBank_1_translateX.o" "horse_1:cc_tail01_outPutAnimBank_1.tx"
		;
connectAttr "horse_1:cc_tail01_outPutAnimBank_1_translateY.o" "horse_1:cc_tail01_outPutAnimBank_1.ty"
		;
connectAttr "horse_1:cc_tail01_outPutAnimBank_1_translateZ.o" "horse_1:cc_tail01_outPutAnimBank_1.tz"
		;
connectAttr "horse_1:cc_tail02_outPutAnimBank_1_translateX.o" "horse_1:cc_tail02_outPutAnimBank_1.tx"
		;
connectAttr "horse_1:cc_tail02_outPutAnimBank_1_translateY.o" "horse_1:cc_tail02_outPutAnimBank_1.ty"
		;
connectAttr "horse_1:cc_tail02_outPutAnimBank_1_translateZ.o" "horse_1:cc_tail02_outPutAnimBank_1.tz"
		;
connectAttr "horse_1:cc_tail03_outPutAnimBank_1_translateX.o" "horse_1:cc_tail03_outPutAnimBank_1.tx"
		;
connectAttr "horse_1:cc_tail03_outPutAnimBank_1_translateY.o" "horse_1:cc_tail03_outPutAnimBank_1.ty"
		;
connectAttr "horse_1:cc_tail03_outPutAnimBank_1_translateZ.o" "horse_1:cc_tail03_outPutAnimBank_1.tz"
		;
connectAttr "horse_1:cc_cc_tail04_outPutAnimBank_1_translateX.o" "horse_1:cc_cc_tail04_outPutAnimBank_1.tx"
		;
connectAttr "horse_1:cc_cc_tail04_outPutAnimBank_1_translateY.o" "horse_1:cc_cc_tail04_outPutAnimBank_1.ty"
		;
connectAttr "horse_1:cc_cc_tail04_outPutAnimBank_1_translateZ.o" "horse_1:cc_cc_tail04_outPutAnimBank_1.tz"
		;
connectAttr "horse_1:cc_tail05_outPutAnimBank_1_translateX.o" "horse_1:cc_tail05_outPutAnimBank_1.tx"
		;
connectAttr "horse_1:cc_tail05_outPutAnimBank_1_translateY.o" "horse_1:cc_tail05_outPutAnimBank_1.ty"
		;
connectAttr "horse_1:cc_tail05_outPutAnimBank_1_translateZ.o" "horse_1:cc_tail05_outPutAnimBank_1.tz"
		;
connectAttr "horse_1:cc_tail06_outPutAnimBank_1_translateX.o" "horse_1:cc_tail06_outPutAnimBank_1.tx"
		;
connectAttr "horse_1:cc_tail06_outPutAnimBank_1_translateY.o" "horse_1:cc_tail06_outPutAnimBank_1.ty"
		;
connectAttr "horse_1:cc_tail06_outPutAnimBank_1_translateZ.o" "horse_1:cc_tail06_outPutAnimBank_1.tz"
		;
// End of horse_walk.ma

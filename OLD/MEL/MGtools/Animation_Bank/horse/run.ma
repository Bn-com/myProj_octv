//Maya ASCII 2011 scene
//Name: run.ma
//Last modified: Thu, Jul 26, 2012 10:53:12 AM
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
	setAttr ".range" -type "string" "\"1:14\"";
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
	setAttr -s 3 ".ktv[0:2]"  1 0 3 0 13 0;
createNode animCurveTL -n "horse_1:cc_COG01_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 -7 4 -4.9425591983738517 7 -7 13 -7;
	setAttr -s 4 ".kit[0:3]"  3 10 10 3;
	setAttr -s 4 ".kot[0:3]"  3 10 10 3;
createNode animCurveTL -n "horse_1:cc_COG01_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 0 3 51.003059620452674 5 112.46916047637058 
		9 227.05087145720699 11 284.67393561808188 13 350.76111933894811;
	setAttr -s 6 ".kit[0:5]"  1 10 10 10 10 9;
	setAttr -s 6 ".kot[0:5]"  1 10 10 10 10 9;
	setAttr -s 6 ".kix[0:5]"  0.0014171850634738803 0.0014818860217928886 
		0.0014200673904269934 0.0014517584349960089 0.0013472330756485462 0.0012609597761183977;
	setAttr -s 6 ".kiy[0:5]"  0.99999898672103882 0.99999892711639404 
		0.99999898672103882 0.99999892711639404 0.99999910593032837 0.99999916553497314;
	setAttr -s 6 ".kox[0:5]"  0.0014171850634738803 0.0014818860217928886 
		0.0014200673904269934 0.0014517584349960089 0.0013472330756485462 0.0012609597761183977;
	setAttr -s 6 ".koy[0:5]"  0.99999898672103882 0.99999892711639404 
		0.99999898672103882 0.99999892711639404 0.99999910593032837 0.99999916553497314;
createNode animCurveTA -n "horse_1:cc_COG01_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  1 0 3 0 7 0 9 0 11 0 12 0 13 0;
	setAttr -s 7 ".kit[0:6]"  3 10 10 10 10 3 3;
	setAttr -s 7 ".kot[0:6]"  3 10 10 10 10 3 3;
createNode animCurveTA -n "horse_1:cc_COG01_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 3 0 13 0;
createNode animCurveTA -n "horse_1:cc_COG01_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 3 0 13 0;
createNode animCurveTU -n "horse_1:cc_COG01_outPutAnimBank_1_tr_curl";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 32.186462145492804 3 39.112357398349474 
		10 26.183946555416 13 32.186462145492804;
	setAttr -s 4 ".kit[1:3]"  10 9 1;
	setAttr -s 4 ".kot[1:3]"  10 9 1;
	setAttr -s 4 ".kix[0:3]"  0.014731289818882942 0.062352247536182404 
		0.060052122920751572 0.016304122284054756;
	setAttr -s 4 ".kiy[0:3]"  0.99989151954650879 -0.99805420637130737 
		-0.99819529056549072 0.99986708164215088;
	setAttr -s 4 ".kox[0:3]"  0.01473128329962492 0.062352247536182404 
		0.060052122920751572 0.016304118558764458;
	setAttr -s 4 ".koy[0:3]"  0.99989151954650879 -0.99805420637130737 
		-0.99819529056549072 0.99986714124679565;
createNode animCurveTU -n "horse_1:cc_COG01_outPutAnimBank_1_tr_sway";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 3 0 13 0;
createNode animCurveTU -n "horse_1:cc_COG01_outPutAnimBank_1_tr_turn";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 3 0 13 0;
createNode animCurveTL -n "horse_1:cc_midVertebraet01_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTL -n "horse_1:cc_midVertebraet01_outPutAnimBank_1_translateY";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0.60822483169039576 4 6.3985885848532114 
		5 6.482265216733901 6 9.7007760123611959 7 17.435089659506247 9 5.0908032020111529 
		10 1.5959905328769919 11 0.73134185921353079 13 0.60822483169039576;
	setAttr -s 9 ".kit[2:8]"  1 10 10 9 1 9 9;
	setAttr -s 9 ".kot[2:8]"  1 10 10 9 1 9 9;
	setAttr -s 9 ".kix[2:8]"  0.08528456836938858 0.0076081673614680767 
		0.027105165645480156 0.0078916177153587341 0.038244962692260742 0.12554696202278137 
		0.56053221225738525;
	setAttr -s 9 ".kiy[2:8]"  0.99635666608810425 0.99997109174728394 
		-0.99963265657424927 -0.99996888637542725 -0.99926847219467163 -0.992087721824646 
		-0.82813268899917603;
	setAttr -s 9 ".kox[2:8]"  0.08528456836938858 0.0076081673614680767 
		0.027105165645480156 0.0078916177153587341 0.038244962692260742 0.12554696202278137 
		0.56053221225738525;
	setAttr -s 9 ".koy[2:8]"  0.99635666608810425 0.99997109174728394 
		-0.99963265657424927 -0.99996888637542725 -0.99926841259002686 -0.992087721824646 
		-0.82813268899917603;
createNode animCurveTL -n "horse_1:cc_midVertebraet01_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  1 56.207852626124321 3 -30.961923929911144 
		4 -43.630995500083408 5 -30.376474533143142 6 -29.400029567361226 7 42.396244731013283 
		9 12.11433931344518 10 10.755401419140915 11 13.021392497999988 13 56.207852626124321;
	setAttr -s 10 ".kit[0:9]"  1 10 10 10 10 10 1 10 
		1 1;
	setAttr -s 10 ".kot[0:9]"  1 10 10 10 10 10 1 10 
		1 1;
	setAttr -s 10 ".kix[0:9]"  0.071461550891399384 0.0012520166346803308 
		0.14092035591602325 0.0058556739240884781 0.0011451169848442078 0.0030109919607639313 
		0.021175302565097809 0.091487325727939606 0.0083243651315569878 0.051622774451971054;
	setAttr -s 10 ".kiy[0:9]"  0.99744337797164917 -0.99999922513961792 
		0.99002093076705933 0.99998283386230469 0.99999934434890747 0.99999547004699707 -0.99977576732635498 
		0.99580627679824829 0.9999653697013855 0.99866664409637451;
	setAttr -s 10 ".kox[0:9]"  0.077012307941913605 0.0012520166346803308 
		0.14092035591602325 0.0058556739240884781 0.0011451169848442078 0.0030109919607639313 
		0.02117527462542057 0.091487325727939606 0.0083243660628795624 0.051526356488466263;
	setAttr -s 10 ".koy[0:9]"  0.99703013896942139 -0.99999922513961792 
		0.99002093076705933 0.99998283386230469 0.99999934434890747 0.99999547004699707 -0.99977576732635498 
		0.99580627679824829 0.9999653697013855 0.99867171049118042;
createNode animCurveTA -n "horse_1:cc_midVertebraet01_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  1 11.650762050679248 3 -2.1651826008936057 
		4 13.700107539240191 5 10.905824033605221 6 44.431921111377378 8 34.033836811713996 
		13 11.650762050679248;
	setAttr -s 7 ".kit[0:6]"  3 10 1 10 10 10 3;
	setAttr -s 7 ".kot[0:6]"  3 10 1 10 10 10 3;
	setAttr -s 7 ".kix[2:6]"  0.97555232048034668 1 0.29580822587013245 
		0.4541725218296051 1;
	setAttr -s 7 ".kiy[2:6]"  0.21976728737354279 0 0.95524734258651733 
		-0.89091378450393677 0;
	setAttr -s 7 ".kox[2:6]"  0.97555232048034668 1 0.29580822587013245 
		0.4541725218296051 1;
	setAttr -s 7 ".koy[2:6]"  0.2197672426700592 0 0.95524734258651733 
		-0.89091378450393677 0;
createNode animCurveTA -n "horse_1:cc_midVertebraet01_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTA -n "horse_1:cc_midVertebraet01_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTL -n "horse_1:cc_thoracic01_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 3 0 13 0;
createNode animCurveTL -n "horse_1:cc_thoracic01_outPutAnimBank_1_translateY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  1 3.8173149086498337 3 5.2907746598935201 
		5 9.9079058232088979 7 9.1429130303416457 9 6.0259022967114708 11 4.3856610804115777 
		12 4.0367368282189027 13 3.8173149086498337;
	setAttr -s 8 ".kit[4:7]"  9 1 1 1;
	setAttr -s 8 ".kot[4:7]"  9 1 1 1;
	setAttr -s 8 ".kix[0:7]"  0.16651540994644165 0.025517420843243599 
		0.016628969460725784 0.026003727689385414 0.035012755542993546 0.10708112269639969 
		0.1954985111951828 0.16974003612995148;
	setAttr -s 8 ".kiy[0:7]"  -0.9860389232635498 0.99967437982559204 
		0.99986177682876587 -0.99966192245483398 -0.99938690662384033 -0.99425035715103149 
		-0.98070400953292847 -0.9854888916015625;
	setAttr -s 8 ".kox[0:7]"  0.16651533544063568 0.025517415255308151 
		0.016628965735435486 0.026003723964095116 0.035012755542993546 0.10708111524581909 
		0.19549845159053802 0.16974006593227386;
	setAttr -s 8 ".koy[0:7]"  -0.98603886365890503 0.99967437982559204 
		0.99986177682876587 -0.99966186285018921 -0.99938690662384033 -0.99425029754638672 
		-0.98070400953292847 -0.9854888916015625;
createNode animCurveTL -n "horse_1:cc_thoracic01_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 -0.14128752265635169 3 0.20922518005706126 
		5 0.6078359436577635 7 0.77103277142761595 9 0.34752902378753103 13 -0.14128752265635169;
	setAttr -s 6 ".kit[0:5]"  3 10 10 10 1 3;
	setAttr -s 6 ".kot[0:5]"  3 10 10 10 1 3;
	setAttr -s 6 ".kix[4:5]"  0.18080513179302216 1;
	setAttr -s 6 ".kiy[4:5]"  -0.98351895809173584 0;
	setAttr -s 6 ".kox[4:5]"  0.18080513179302216 1;
	setAttr -s 6 ".koy[4:5]"  -0.98351901769638062 0;
createNode animCurveTA -n "horse_1:cc_thoracic01_outPutAnimBank_1_rotateX";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  1 6.1466502461053194 3 8.0192343936104891 
		5 3.4913855955675048 7 0.31764908047777562 9 0.47062286009140525 11 2.7325441279270875 
		12 4.3493422006922504 13 6.1466502461053194;
	setAttr -s 8 ".kix[0:7]"  0.83295750617980957 0.96050244569778442 
		0.65097731351852417 0.9876328706741333 0.97819232940673828 0.84314256906509399 0.81827414035797119 
		0.73855036497116089;
	setAttr -s 8 ".kiy[0:7]"  0.5533369779586792 -0.27827182412147522 
		-0.75909721851348877 -0.15678432583808899 0.2077011913061142 0.53769016265869141 
		0.57482826709747314 0.67419832944869995;
	setAttr -s 8 ".kox[0:7]"  0.83295744657516479 0.96050244569778442 
		0.65097725391387939 0.9876328706741333 0.97819232940673828 0.84314262866973877 0.81827425956726074 
		0.73855018615722656;
	setAttr -s 8 ".koy[0:7]"  0.55333709716796875 -0.27827176451683044 
		-0.75909727811813354 -0.1567843109369278 0.20770131051540375 0.5376899242401123 0.57482808828353882 
		0.67419856786727905;
createNode animCurveTA -n "horse_1:cc_thoracic01_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 3 0 13 0;
createNode animCurveTA -n "horse_1:cc_thoracic01_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 3 0 13 0;
createNode animCurveTU -n "horse_1:cc_thoracic01_outPutAnimBank_1_lock";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 3 0 13 0;
createNode animCurveTL -n "horse_1:cc_hipSway01_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 -0.56303547519999997 3 -0.56303547519999997 
		13 -0.56303547519999997;
	setAttr -s 3 ".kit[0:2]"  9 10 10;
	setAttr -s 3 ".kot[0:2]"  9 10 10;
createNode animCurveTL -n "horse_1:cc_hipSway01_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0.35361623611900495 3 -0.3439326406702099 
		7 -1.3407110749221234 9 -2.0563199360985274 13 0.35361623611900495;
	setAttr -s 5 ".kit[0:4]"  3 1 10 10 3;
	setAttr -s 5 ".kot[0:4]"  3 1 10 10 3;
	setAttr -s 5 ".kix[1:4]"  0.10324511677026749 0.14446353912353516 
		0.14597076177597046 1;
	setAttr -s 5 ".kiy[1:4]"  -0.99465596675872803 -0.98951011896133423 
		0.98928886651992798 0;
	setAttr -s 5 ".kox[1:4]"  0.10324511677026749 0.14446353912353516 
		0.14597076177597046 1;
	setAttr -s 5 ".koy[1:4]"  -0.99465596675872803 -0.98951011896133423 
		0.98928886651992798 0;
createNode animCurveTL -n "horse_1:cc_hipSway01_outPutAnimBank_1_translateZ";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 5.7653438600000735 3 4.8185699080628019 
		7 4.1129600287190016 9 4.599731169492399 13 5.7653438600000735;
	setAttr -s 5 ".kit[0:4]"  3 1 1 10 3;
	setAttr -s 5 ".kot[0:4]"  3 1 1 10 3;
	setAttr -s 5 ".kix[1:4]"  0.10177645832300186 0.62165439128875732 
		0.14959411323070526 1;
	setAttr -s 5 ".kiy[1:4]"  -0.99480730295181274 0.78329169750213623 
		0.98874741792678833 0;
	setAttr -s 5 ".kox[1:4]"  0.10177642852067947 0.62165439128875732 
		0.14959411323070526 1;
	setAttr -s 5 ".koy[1:4]"  -0.99480736255645752 0.78329163789749146 
		0.98874741792678833 0;
createNode animCurveTA -n "horse_1:cc_hipSway01_outPutAnimBank_1_rotateX";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 1.7268182200057263 5 -15.337788750757404 
		9 4.5179482471567622 11 6.8066947289157334 13 1.7268182200057263;
	setAttr -s 5 ".kit[2:4]"  10 9 1;
	setAttr -s 5 ".kot[2:4]"  10 9 1;
	setAttr -s 5 ".kix[0:4]"  0.52173709869384766 0.93782079219818115 
		1 0.95983999967575073 0.46763214468955994;
	setAttr -s 5 ".kiy[0:4]"  -0.85310637950897217 -0.34711986780166626 
		0 -0.28054821491241455 -0.88392317295074463;
	setAttr -s 5 ".kox[0:4]"  0.52173727750778198 0.93782079219818115 
		1 0.95983999967575073 0.46763217449188232;
	setAttr -s 5 ".koy[0:4]"  -0.85310626029968262 -0.34711983799934387 
		0 -0.28054821491241455 -0.88392317295074463;
createNode animCurveTA -n "horse_1:cc_hipSway01_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 3.08 3 3.08 13 3.08;
	setAttr -s 3 ".kit[0:2]"  9 10 10;
	setAttr -s 3 ".kot[0:2]"  9 10 10;
createNode animCurveTA -n "horse_1:cc_hipSway01_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 3 0 13 0;
	setAttr -s 3 ".kit[0:2]"  9 10 10;
	setAttr -s 3 ".kot[0:2]"  9 10 10;
createNode animCurveTL -n "horse_1:cc_r_shoulder01_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  1 0 3 0 7 -1.9622821299940798 9 2.6306877119929939 
		10 -4.5592057625919695 11 -6.0016120745094748 13 0;
	setAttr -s 7 ".kit[0:6]"  3 10 10 10 10 10 10;
	setAttr -s 7 ".kot[0:6]"  3 10 10 10 10 10 10;
createNode animCurveTL -n "horse_1:cc_r_shoulder01_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  1 0.85456109025737215 3 0.82702695282781258 
		7 0.75387297429008027 8 6.3450175613180262 9 8.4879201981874584 10 -16.081225003726836 
		11 -24.220647870615618 13 0.85456109025737215;
	setAttr -s 8 ".kit[0:7]"  9 10 10 10 10 10 10 9;
	setAttr -s 8 ".kot[0:7]"  9 10 10 10 10 10 10 9;
createNode animCurveTL -n "horse_1:cc_r_shoulder01_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  1 6.0892759240502405 3 5.8703027781840458 
		7 1.6529884583502517 8 1.1330339761315846 9 1.1225120174192216 10 11.115613639864472 
		11 4.1114753617412072 13 6.0892759240502405;
	setAttr -s 8 ".kit[0:7]"  3 10 10 10 10 10 10 3;
	setAttr -s 8 ".kot[0:7]"  3 10 10 10 10 10 10 3;
createNode animCurveTA -n "horse_1:cc_r_shoulder01_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  1 0 3 -43.816147679622318 7 -47.900584924398458 
		8 -31.808396040306061 9 -4.1673064368972383 10 2.4953399679101524 11 0.40423469201259027 
		13 0;
	setAttr -s 8 ".kit[0:7]"  1 10 10 10 10 10 1 1;
	setAttr -s 8 ".kot[0:7]"  1 10 10 10 10 10 1 1;
	setAttr -s 8 ".kix[0:7]"  0.086938060820102692 0.28649941086769104 
		0.70500308275222778 0.108531653881073 0.13785842061042786 1 0.9617459774017334 0.077448070049285889;
	setAttr -s 8 ".kiy[0:7]"  -0.99621373414993286 -0.95808041095733643 
		0.70920419692993164 0.99409306049346924 0.99045199155807495 0 -0.27394312620162964 
		-0.99699640274047852;
	setAttr -s 8 ".kox[0:7]"  0.090455465018749237 0.28649941086769104 
		0.70500308275222778 0.108531653881073 0.13785842061042786 1 0.96174591779708862 0.077448062598705292;
	setAttr -s 8 ".koy[0:7]"  -0.99590051174163818 -0.95808041095733643 
		0.70920419692993164 0.99409306049346924 0.99045199155807495 0 -0.27394306659698486 
		-0.99699640274047852;
createNode animCurveTA -n "horse_1:cc_r_shoulder01_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 0 3 0 7 -11.007355668145967 9 -7.4560846865343331 
		10 -5.143661554631251 13 0;
	setAttr -s 6 ".kit[0:5]"  3 10 10 10 10 3;
	setAttr -s 6 ".kot[0:5]"  3 10 10 10 10 3;
createNode animCurveTA -n "horse_1:cc_r_shoulder01_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 0 3 0 7 15.785256308152908 9 0.18815411965469708 
		10 -5.3591044633047282 13 0;
	setAttr -s 6 ".kit[0:5]"  3 10 10 10 10 3;
	setAttr -s 6 ".kot[0:5]"  3 10 10 10 10 3;
createNode animCurveTL -n "horse_1:cc_l_shoulder01_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -3.0927669940498013 3 -2.2791634342206217 
		7 -0.86900203116711627 12 -3.6316353069735938 13 -3.0927669940498013;
	setAttr -s 5 ".kit[0:4]"  1 10 10 10 1;
	setAttr -s 5 ".kot[0:4]"  1 10 10 10 1;
	setAttr -s 5 ".kix[0:4]"  0.099206589162349701 0.11171817779541016 
		0.26718965172767639 0.11171819269657135 0.084406346082687378;
	setAttr -s 5 ".kiy[0:4]"  0.99506682157516479 0.99373996257781982 
		-0.96364396810531616 -0.99373984336853027 0.99643141031265259;
	setAttr -s 5 ".kox[0:4]"  0.1010311171412468 0.11171817779541016 
		0.26718965172767639 0.11171819269657135 0.084406338632106781;
	setAttr -s 5 ".koy[0:4]"  0.99488329887390137 0.99373996257781982 
		-0.96364396810531616 -0.99373984336853027 0.99643141031265259;
createNode animCurveTL -n "horse_1:cc_l_shoulder01_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  1 5.439180038827212 3 9.3506174943974578 
		5 12.624963371278467 7 11.587806538863781 10 12.724825474238735 12 12.936662316797902 
		13 5.4391800388276854;
	setAttr -s 7 ".kit[0:6]"  3 10 10 10 10 10 3;
	setAttr -s 7 ".kot[0:6]"  3 10 10 10 10 10 3;
createNode animCurveTL -n "horse_1:cc_l_shoulder01_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  1 4.0762323567650087 3 1.8413304944564315 
		5 -2.0562658849298319 7 -1.7906793261645273 10 0.25898998350843311 12 1.3145036230245077 
		13 4.0762323567693191;
	setAttr -s 7 ".kit[0:6]"  3 10 10 10 10 10 3;
	setAttr -s 7 ".kot[0:6]"  3 10 10 10 10 10 3;
createNode animCurveTA -n "horse_1:cc_l_shoulder01_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 7 ".ktv[0:6]"  1 13.140874194207182 3 -22.387836651072632 
		7 -51.086739307746903 10 -33.766311288760349 11 -17.263674071076871 12 8.0921110156125824 
		13 13.140874194207182;
	setAttr -s 7 ".kit[0:6]"  3 1 10 10 10 10 1;
	setAttr -s 7 ".kot[0:6]"  3 1 10 10 10 10 1;
	setAttr -s 7 ".kix[1:6]"  0.08977825939655304 0.82658565044403076 
		0.27170947194099426 0.11333172023296356 0.15513609349727631 0.99864006042480469;
	setAttr -s 7 ".kiy[1:6]"  -0.99596184492111206 -0.56281089782714844 
		0.9623793363571167 0.99355727434158325 0.98789310455322266 0.052134864032268524;
	setAttr -s 7 ".kox[1:6]"  0.089778274297714233 0.82658565044403076 
		0.27170947194099426 0.11333172023296356 0.15513609349727631 0.99864006042480469;
	setAttr -s 7 ".koy[1:6]"  -0.99596178531646729 -0.56281089782714844 
		0.9623793363571167 0.99355727434158325 0.98789310455322266 0.052135005593299866;
createNode animCurveTA -n "horse_1:cc_l_shoulder01_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 3.7919284751143705 3 2.8628764547063161 
		7 14.228734264318668 10 9.0276147565520386 12 4.670965725540964 13 3.7919284751143705;
	setAttr -s 6 ".kit[0:5]"  3 10 10 10 10 10;
	setAttr -s 6 ".kot[0:5]"  3 10 10 10 10 10;
createNode animCurveTA -n "horse_1:cc_l_shoulder01_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 0.88454510102773087 3 -1.2820282600558333 
		7 -17.119426037646981 10 -11.969532673066617 12 -2.8406393077829386 13 0.88454510102773087;
	setAttr -s 6 ".kit[0:5]"  3 10 10 10 10 10;
	setAttr -s 6 ".kot[0:5]"  3 10 10 10 10 10;
createNode animCurveTL -n "horse_1:cc_cervical01_outPutAnimBank_1_translateX";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTL -n "horse_1:cc_cervical01_outPutAnimBank_1_translateY";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 0.7835809559948832 5 -7.1352981389302483 
		10 -0.27396655170529771 13 0.7835809559948832;
	setAttr -s 4 ".kit[1:3]"  9 1 3;
	setAttr -s 4 ".kot[1:3]"  9 1 3;
	setAttr -s 4 ".kix[2:3]"  0.59229683876037598 1;
	setAttr -s 4 ".kiy[2:3]"  0.80571985244750977 0;
	setAttr -s 4 ".kox[2:3]"  0.5922967791557312 1;
	setAttr -s 4 ".koy[2:3]"  0.80571997165679932 0;
createNode animCurveTL -n "horse_1:cc_cervical01_outPutAnimBank_1_translateZ";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 1.490873298909785 5 -4.0101756554070294 
		10 -2.61671386332609 13 1.490873298909785;
	setAttr -s 4 ".kit[0:3]"  1 9 9 1;
	setAttr -s 4 ".kot[0:3]"  1 9 9 1;
	setAttr -s 4 ".kix[0:3]"  0.078909032046794891 0.090916380286216736 
		0.060483571141958237 0.075211942195892334;
	setAttr -s 4 ".kiy[0:3]"  -0.99688184261322021 -0.99585855007171631 
		0.9981691837310791 -0.99716758728027344;
	setAttr -s 4 ".kox[0:3]"  0.078909032046794891 0.090916380286216736 
		0.060483571141958237 0.075211942195892334;
	setAttr -s 4 ".koy[0:3]"  -0.99688184261322021 -0.99585855007171631 
		0.9981691837310791 -0.99716758728027344;
createNode animCurveTA -n "horse_1:cc_cervical01_outPutAnimBank_1_rotateX";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 -10.345177511347394 5 -7.192806571548175 
		10 -0.93238738752840822 13 -10.345177511347394;
	setAttr -s 4 ".kix[0:3]"  0.92341166734695435 0.91168540716171265 
		0.99971306324005127 0.73253488540649414;
	setAttr -s 4 ".kiy[0:3]"  -0.38381105661392212 0.4108891487121582 
		0.023954538628458977 -0.68072950839996338;
	setAttr -s 4 ".kox[0:3]"  0.92341160774230957 0.91168534755706787 
		0.99971306324005127 0.73253494501113892;
	setAttr -s 4 ".koy[0:3]"  -0.38381123542785645 0.41088911890983582 
		0.023954527452588081 -0.6807294487953186;
createNode animCurveTA -n "horse_1:cc_cervical01_outPutAnimBank_1_rotateY";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTA -n "horse_1:cc_cervical01_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTL -n "horse_1:cc_cervical02_outPutAnimBank_1_translateX";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTL -n "horse_1:cc_cervical02_outPutAnimBank_1_translateY";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 10 -1.1417495490532779 13 0;
	setAttr -s 3 ".kit[1:2]"  9 3;
	setAttr -s 3 ".kot[1:2]"  9 3;
createNode animCurveTL -n "horse_1:cc_cervical02_outPutAnimBank_1_translateZ";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 1.6251217415928882 10 4.8987883369843574 
		13 1.6251217415928882;
	setAttr -s 3 ".kit[1:2]"  9 1;
	setAttr -s 3 ".kot[1:2]"  9 1;
	setAttr -s 3 ".kix[0:2]"  0.075254648923873901 1 0.061169844120740891;
	setAttr -s 3 ".kiy[0:2]"  -0.99716430902481079 0 -0.99812740087509155;
	setAttr -s 3 ".kox[0:2]"  0.075254634022712708 1 0.061169844120740891;
	setAttr -s 3 ".koy[0:2]"  -0.99716430902481079 0 -0.99812740087509155;
createNode animCurveTA -n "horse_1:cc_cervical02_outPutAnimBank_1_rotateX";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 5.1419330457586749 4 0.32479740628245701 
		10 4.3298912186663152 13 5.1419330457586749;
	setAttr -s 4 ".kit[1:3]"  10 9 1;
	setAttr -s 4 ".kot[1:3]"  10 9 1;
	setAttr -s 4 ".kix[0:3]"  0.98480033874511719 0.99928659200668335 
		0.97577673196792603 0.9833991527557373;
	setAttr -s 4 ".kiy[0:3]"  0.17369073629379272 -0.037767179310321808 
		0.21876882016658783 0.18145570158958435;
	setAttr -s 4 ".kox[0:3]"  0.98480027914047241 0.99928659200668335 
		0.97577673196792603 0.9833991527557373;
	setAttr -s 4 ".koy[0:3]"  0.17369075119495392 -0.037767179310321808 
		0.21876882016658783 0.18145570158958435;
createNode animCurveTA -n "horse_1:cc_cervical02_outPutAnimBank_1_rotateY";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTA -n "horse_1:cc_cervical02_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTL -n "horse_1:cc_head01_outPutAnimBank_1_translateX";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTL -n "horse_1:cc_head01_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0 5 -0.11786232787671386 7 -1.5720544614561263 
		10 1.2469908860607966 13 0;
	setAttr -s 5 ".kit[0:4]"  3 10 10 10 1;
	setAttr -s 5 ".kot[0:4]"  3 10 10 10 1;
	setAttr -s 5 ".kix[4]"  0.97971087694168091;
	setAttr -s 5 ".kiy[4]"  -0.20041631162166595;
	setAttr -s 5 ".kox[4]"  0.97971087694168091;
	setAttr -s 5 ".koy[4]"  -0.20041631162166595;
createNode animCurveTL -n "horse_1:cc_head01_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 0.2349340071407886 5 -5.8022930647445072 
		7 -1.7212171367728706 10 5.7704429364873597 13 0.2349340071407886;
	setAttr -s 5 ".kit[0:4]"  1 10 10 10 1;
	setAttr -s 5 ".kot[0:4]"  1 10 10 10 1;
	setAttr -s 5 ".kix[0:4]"  0.024520318955183029 0.12677088379859924 
		0.017999164760112762 0.12677089869976044 0.026194470003247261;
	setAttr -s 5 ".kiy[0:4]"  -0.99969935417175293 -0.99193203449249268 
		0.99983793497085571 0.9919319748878479 -0.99965685606002808;
	setAttr -s 5 ".kox[0:4]"  0.024520277976989746 0.12677088379859924 
		0.017999164760112762 0.12677089869976044 0.026194455102086067;
	setAttr -s 5 ".koy[0:4]"  -0.99969935417175293 -0.99193203449249268 
		0.99983793497085571 0.9919319748878479 -0.99965685606002808;
createNode animCurveTA -n "horse_1:cc_head01_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 8.5751710641313839 5 12.643523176171882 
		10 2.0952566598164544 13 8.5751710641313839;
	setAttr -s 4 ".kit[0:3]"  1 10 10 1;
	setAttr -s 4 ".kot[0:3]"  1 10 10 1;
	setAttr -s 4 ".kix[0:3]"  0.86624890565872192 0.95740658044815063 
		0.97805559635162354 0.83900970220565796;
	setAttr -s 4 ".kiy[0:3]"  0.49961274862289429 -0.28874322772026062 
		-0.20834383368492126 0.54411649703979492;
	setAttr -s 4 ".kox[0:3]"  0.8662492036819458 0.95740658044815063 
		0.97805559635162354 0.83900964260101318;
	setAttr -s 4 ".koy[0:3]"  0.4996122419834137 -0.28874322772026062 
		-0.20834383368492126 0.54411661624908447;
createNode animCurveTA -n "horse_1:cc_head01_outPutAnimBank_1_rotateY";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTA -n "horse_1:cc_head01_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTU -n "horse_1:cc_head01_outPutAnimBank_1_ear_r_rootCurl";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTU -n "horse_1:cc_head01_outPutAnimBank_1_ear_r_rootTurn";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTU -n "horse_1:cc_head01_outPutAnimBank_1_ear_r_rootSway";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTU -n "horse_1:cc_head01_outPutAnimBank_1_ear_r_midCurl";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTU -n "horse_1:cc_head01_outPutAnimBank_1_ear_r_midTurn";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTU -n "horse_1:cc_head01_outPutAnimBank_1_ear_r_midSway";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTU -n "horse_1:cc_head01_outPutAnimBank_1_ear_l_rootCurl";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTU -n "horse_1:cc_head01_outPutAnimBank_1_ear_l_rootTurn";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTU -n "horse_1:cc_head01_outPutAnimBank_1_ear_l_rootSway";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTU -n "horse_1:cc_head01_outPutAnimBank_1_ear_l_midCurl";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTU -n "horse_1:cc_head01_outPutAnimBank_1_ear_l_midTurn";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTU -n "horse_1:cc_head01_outPutAnimBank_1_ear_l_midSway";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1 0 13 0;
createNode animCurveTL -n "horse_1:cc_l_carpalFT01_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  3 -5.216937 13 -5.216937;
createNode animCurveTL -n "horse_1:cc_l_carpalFT01_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  3 40.781652766306713 7 40.781652766306713 
		13 40.781652766306713;
createNode animCurveTL -n "horse_1:cc_l_carpalFT01_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  3 79.884195613827274 7 79.884195613827274 
		13 79.884195613827274;
createNode animCurveTL -n "horse_1:cc_r_carpalFT01_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  3 2.4012283179412606 13 2.4012283179412606;
createNode animCurveTL -n "horse_1:cc_r_carpalFT01_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  3 40.781652766306713 7 40.781652766306713 
		13 40.781652766306713;
createNode animCurveTL -n "horse_1:cc_r_carpalFT01_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  3 79.884195613827274 7 79.884195613827274 
		13 79.884195613827274;
createNode animCurveTL -n "horse_1:cc_r_tarsalFT01_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 -6.103028445245898 3 -6.103028445245898 
		13 -6.103028445245898;
createNode animCurveTL -n "horse_1:cc_r_tarsalFT01_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 15.879731150667233 3 15.879731150667233 
		13 15.879731150667233;
createNode animCurveTL -n "horse_1:cc_r_tarsalFT01_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 40.228008268540492 3 40.228008268540492 
		13 40.228008268540492;
createNode animCurveTL -n "horse_1:cc_l_tarsalFT01_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 4.797206960887145 3 4.797206960887145 
		13 4.797206960887145;
createNode animCurveTL -n "horse_1:cc_l_tarsalFT01_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 12.725873401787787 3 12.725873401787787 
		13 12.725873401787787;
createNode animCurveTL -n "horse_1:cc_l_tarsalFT01_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 48.869950145959919 3 48.869950145959919 
		13 48.869950145959919;
createNode animCurveTL -n "horse_1:cc_r_legFT01_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 7 3 7 9 7 13 7;
createNode animCurveTL -n "horse_1:cc_r_legFT01_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 38.783673226687242 3 33.005701871757353 
		5 24.8200440205141 7 17.76192047638061 8 0 9 0 11 0 12 13.884654589868539 13 38.783673229999998;
	setAttr -s 9 ".kit[0:8]"  1 10 10 10 10 10 10 10 
		1;
	setAttr -s 9 ".kot[0:8]"  1 10 10 10 10 10 10 10 
		1;
	setAttr -s 9 ".kix[0:8]"  0.025501947849988937 0.011934920214116573 
		0.010932766832411289 0.005036188755184412 1 1 1 0.0021486657205969095 0.0098615502938628197;
	setAttr -s 9 ".kiy[0:8]"  0.99967473745346069 -0.99992877244949341 
		-0.99994027614593506 -0.99998730421066284 0 0 0 0.99999767541885376 0.99995136260986328;
	setAttr -s 9 ".kox[0:8]"  0.025501957163214684 0.011934920214116573 
		0.010932766832411289 0.005036188755184412 1 1 1 0.0021486657205969095 0.0098615428432822227;
	setAttr -s 9 ".koy[0:8]"  0.99967479705810547 -0.99992877244949341 
		-0.99994027614593506 -0.99998730421066284 0 0 0 0.99999767541885376 0.99995136260986328;
createNode animCurveTL -n "horse_1:cc_r_legFT01_outPutAnimBank_1_translateZ";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 11 ".ktv[0:10]"  1 -71.305505263405507 3 47.866573906852757 
		5 157.77266170038033 6 205.84514355795673 7 238.68946244866967 8 247.00538443476421 
		9 247.00588157486706 10 247.00545562930688 11 247.00545562930688 12 253.47037446155477 
		13 279.45527412464526;
	setAttr -s 11 ".kit[1:10]"  10 1 10 1 10 3 3 3 
		1 1;
	setAttr -s 11 ".kot[1:10]"  10 1 10 1 10 3 3 3 
		1 1;
	setAttr -s 11 ".kix[0:10]"  0.00098627421539276838 0.0007275534444488585 
		0.00075314007699489594 0.0010298638371750712 0.0054693864658474922 1 1 1 1 0.00248129409737885 
		0.0012207443360239267;
	setAttr -s 11 ".kiy[0:10]"  0.9999995231628418 0.9999997615814209 0.99999970197677612 
		0.9999995231628418 0.99998503923416138 0 0 0 0 0.99999696016311646 0.9999992847442627;
	setAttr -s 11 ".kox[0:10]"  0.00098418979905545712 0.0007275534444488585 
		0.00075314025161787868 0.0010298638371750712 0.0054693878628313541 1 1 1 1 0.0024812936317175627 
		0.0012207438703626394;
	setAttr -s 11 ".koy[0:10]"  0.9999995231628418 0.9999997615814209 0.9999997615814209 
		0.9999995231628418 0.99998503923416138 0 0 0 0 0.99999696016311646 0.9999992847442627;
createNode animCurveTA -n "horse_1:cc_r_legFT01_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 0 3 0 9 0 13 0;
createNode animCurveTA -n "horse_1:cc_r_legFT01_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 0 3 0 9 0 13 0;
createNode animCurveTA -n "horse_1:cc_r_legFT01_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 0 3 0 9 0 13 0;
createNode animCurveTU -n "horse_1:cc_r_legFT01_outPutAnimBank_1_fetlock_ft_curl";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 0 3 0 7 0 8 2 9 -4.6999999999999993 10 
		6.3000000000000007 11 30.300000000000004 12 0 13 0;
createNode animCurveTU -n "horse_1:cc_r_legFT01_outPutAnimBank_1_hoof_ft_curl";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  1 135.5 3 98.371180979289136 5 49.906560093529777 
		7 0.68518409256009161 8 0 9 0 10 0 11 10.100000000000001 12 103.81246980015463 13 
		135.5;
	setAttr -s 10 ".kit[0:9]"  3 10 10 1 10 10 10 10 
		10 3;
	setAttr -s 10 ".kot[0:9]"  3 10 10 1 10 10 10 10 
		10 3;
	setAttr -s 10 ".kix[3:9]"  0.035981044173240662 1 1 1 0.00080272933701053262 
		0.0006645400426350534 1;
	setAttr -s 10 ".kiy[3:9]"  -0.99935245513916016 0 0 0 0.99999970197677612 
		0.9999997615814209 0;
	setAttr -s 10 ".kox[3:9]"  0.035981003195047379 1 1 1 0.00080272933701053262 
		0.0006645400426350534 1;
	setAttr -s 10 ".koy[3:9]"  -0.99935251474380493 0 0 0 0.99999970197677612 
		0.9999997615814209 0;
createNode animCurveTL -n "horse_1:cc_l_legFT01_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 -7 3 -7 12 -7 13 -7;
createNode animCurveTL -n "horse_1:cc_l_legFT01_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  1 0 2 1.6979940216488911 3 21.182595892993724 
		5 30.911844053084806 7 31.864573595917307 9 23.996401108166673 10 14.627552443359999 
		11 0 12 0 13 0;
	setAttr -s 10 ".kit[0:9]"  3 1 10 10 10 10 10 10 
		10 10;
	setAttr -s 10 ".kot[0:9]"  3 1 10 10 10 10 10 10 
		10 10;
	setAttr -s 10 ".kix[1:9]"  0.0075596445240080357 0.0042787529528141022 
		0.015600704587996006 0.024093654006719589 0.0072516421787440777 0.0034727223683148623 
		1 1 1;
	setAttr -s 10 ".kiy[1:9]"  0.99997144937515259 0.99999088048934937 
		0.99987834692001343 -0.99970972537994385 -0.99997365474700928 -0.99999397993087769 
		0 0 0;
	setAttr -s 10 ".kox[1:9]"  0.0075596440583467484 0.0042787529528141022 
		0.015600704587996006 0.024093654006719589 0.0072516421787440777 0.0034727223683148623 
		1 1 1;
	setAttr -s 10 ".koy[1:9]"  0.99997144937515259 0.99999088048934937 
		0.99987834692001343 -0.99970972537994385 -0.99997365474700928 -0.99999397993087769 
		0 0 0;
createNode animCurveTL -n "horse_1:cc_l_legFT01_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  1 -24.596348951574328 2 -15.430634236340424 
		3 9.2929113081331316 5 100.1780293511958 7 205.89272858664037 9 292.32035235460893 
		10 321.34786244339477 11 326.10507666826038 12 326.10507666826038 13 326.10507666826038;
	setAttr -s 10 ".kit[0:9]"  3 10 10 1 10 10 1 10 
		10 3;
	setAttr -s 10 ".kot[0:9]"  3 10 10 1 10 10 1 10 
		10 3;
	setAttr -s 10 ".kix[3:9]"  0.00079865020234137774 0.00086741225095465779 
		0.0010826709913089871 0.0028820435982197523 1 1 1;
	setAttr -s 10 ".kiy[3:9]"  0.99999970197677612 0.99999958276748657 
		0.99999940395355225 0.99999582767486572 0 0 0;
	setAttr -s 10 ".kox[3:9]"  0.00079865031875669956 0.00086741225095465779 
		0.0010826709913089871 0.0028820408042520285 1 1 1;
	setAttr -s 10 ".koy[3:9]"  0.99999970197677612 0.99999958276748657 
		0.99999940395355225 0.9999958872795105 0 0 0;
createNode animCurveTA -n "horse_1:cc_l_legFT01_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 0 3 0 12 0 13 0;
createNode animCurveTA -n "horse_1:cc_l_legFT01_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 0 3 0 12 0 13 0;
createNode animCurveTA -n "horse_1:cc_l_legFT01_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 0 3 0 12 0 13 0;
createNode animCurveTU -n "horse_1:cc_l_legFT01_outPutAnimBank_1_fetlock_ft_curl";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 21.700000000000003 3 0 7 0 11 0 12 -21.900000000000002 
		13 21.7;
	setAttr -s 6 ".kit[0:5]"  3 10 10 10 10 3;
	setAttr -s 6 ".kot[0:5]"  3 10 10 10 10 3;
createNode animCurveTU -n "horse_1:cc_l_legFT01_outPutAnimBank_1_hoof_ft_curl";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  1 0 2 89.313536964278967 3 119.20000000000002 
		5 122.68346237857472 7 66.148153716215589 9 25.728933263013637 10 2.1 11 0 12 0 13 
		0;
	setAttr -s 10 ".kit[0:9]"  3 10 10 10 10 10 1 10 
		10 10;
	setAttr -s 10 ".kot[0:9]"  3 10 10 10 10 10 1 10 
		10 10;
	setAttr -s 10 ".kix[6:9]"  0.011582892388105392 1 1 1;
	setAttr -s 10 ".kiy[6:9]"  -0.99993294477462769 0 0 0;
	setAttr -s 10 ".kox[6:9]"  0.011582888662815094 1 1 1;
	setAttr -s 10 ".koy[6:9]"  -0.99993294477462769 0 0 0;
createNode animCurveTL -n "horse_1:cc_r_legBK01_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 0 3 0 7 0 13 0;
createNode animCurveTL -n "horse_1:cc_r_legBK01_outPutAnimBank_1_translateY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  1 21.538956586841362 3 10.758932887566944 
		5 0 7 0 8 0 9 11.100980177740995 10 22.397439667184791 11 25.935825530720354 12 24.786847912397366 
		13 21.538956590000002;
	setAttr -s 10 ".kit[2:9]"  10 10 1 1 1 10 10 1;
	setAttr -s 10 ".kot[2:9]"  10 10 1 1 1 10 10 1;
	setAttr -s 10 ".kix[0:9]"  0.015370613895356655 0.0056909332051873207 
		1 1 0.53532814979553223 0.0033296935725957155 0.0062166904099285603 0.034854952245950699 
		0.018949480727314949 0.010847361758351326;
	setAttr -s 10 ".kiy[0:9]"  -0.99988186359405518 -0.99998384714126587 
		0 0 0.84464424848556519 0.99999445676803589 0.99998068809509277 0.99939239025115967 
		-0.99982041120529175 -0.99994117021560669;
	setAttr -s 10 ".kox[0:9]"  0.013759595341980457 0.0056909332051873207 
		1 1 0.53531128168106079 0.0033296926412731409 0.0062166890129446983 0.034854952245950699 
		0.018949480727314949 0.010847362689673901;
	setAttr -s 10 ".koy[0:9]"  -0.99990540742874146 -0.99998384714126587 
		0 0 0.84465485811233521 0.99999445676803589 0.99998068809509277 0.99939239025115967 
		-0.99982041120529175 -0.99994117021560669;
createNode animCurveTL -n "horse_1:cc_r_legBK01_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 11 ".ktv[0:10]"  1 -6.6824534925025532 3 100.88222433073685 
		4 138.1159647992468 5 143.18786367017103 7 143.18786367017103 8 145.30346096624086 
		9 151.0679998844879 10 179.86525969882152 11 232.05844904939053 12 290.96681263683718 
		13 344.079;
	setAttr -s 11 ".kit[0:10]"  1 10 10 3 3 10 1 10 
		10 10 1;
	setAttr -s 11 ".kot[0:10]"  1 10 10 3 3 10 1 10 
		10 10 1;
	setAttr -s 11 ".kix[0:10]"  0.0006789534236304462 0.00086326873861253262 
		0.0019697886891663074 1 1 0.010574523359537125 0.0026607327163219452 0.0010289275087416172 
		0.00075006438419222832 0.00074391101952642202 0.00090181361883878708;
	setAttr -s 11 ".kiy[0:10]"  0.9999997615814209 0.99999958276748657 
		0.99999809265136719 0 0 0.99994409084320068 0.99999648332595825 0.9999995231628418 
		0.99999970197677612 0.99999970197677612 0.99999958276748657;
	setAttr -s 11 ".kox[0:10]"  0.00068014179123565555 0.00086326873861253262 
		0.0019697886891663074 1 1 0.010574523359537125 0.0026607329491525888 0.0010289275087416172 
		0.00075006438419222832 0.00074391101952642202 0.00089443125762045383;
	setAttr -s 11 ".koy[0:10]"  0.9999997615814209 0.99999958276748657 
		0.99999809265136719 0 0 0.99994409084320068 0.99999648332595825 0.9999995231628418 
		0.99999970197677612 0.99999970197677612 0.99999964237213135;
createNode animCurveTA -n "horse_1:cc_r_legBK01_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 0 3 0 7 0 13 0;
createNode animCurveTA -n "horse_1:cc_r_legBK01_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 0 3 0 7 0 13 0;
createNode animCurveTA -n "horse_1:cc_r_legBK01_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 0 3 0 7 0 13 0;
createNode animCurveTU -n "horse_1:cc_r_legBK01_outPutAnimBank_1_fetlock_bk_curl";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 0 3 0 7 0 13 0;
createNode animCurveTU -n "horse_1:cc_r_legBK01_outPutAnimBank_1_hoof_bk_curl";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 8 ".ktv[0:7]"  1 56.300000000000011 3 13.11249939668717 
		5 0 7 0 8 61.05314925758482 9 97.500000000000014 11 95.949999997850227 13 56.3;
	setAttr -s 8 ".kit[7]"  1;
	setAttr -s 8 ".kot[7]"  1;
	setAttr -s 8 ".kix[7]"  0.0022379511501640081;
	setAttr -s 8 ".kiy[7]"  -0.99999749660491943;
	setAttr -s 8 ".kox[7]"  0.0022379506845027208;
	setAttr -s 8 ".koy[7]"  -0.99999749660491943;
createNode animCurveTL -n "horse_1:cc_l_legBK01_outPutAnimBank_1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 0 3 0 8 0 13 0;
createNode animCurveTL -n "horse_1:cc_l_legBK01_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 24.399411551236732 3 21.431920785468535 
		5 14.754225240858016 7 0 8 0 10 0 11 12.885550400937392 12 20.829776856061486 13 
		24.399411548745082;
	setAttr -s 9 ".kit[0:8]"  3 10 10 10 10 10 1 10 
		3;
	setAttr -s 9 ".kot[0:8]"  3 10 10 10 10 10 1 10 
		3;
	setAttr -s 9 ".kix[6:8]"  0.0032487357966601849 0.0072374641895294189 
		1;
	setAttr -s 9 ".kiy[6:8]"  0.99999469518661499 0.9999738335609436 
		0;
	setAttr -s 9 ".kox[6:8]"  0.0032487362623214722 0.0072374641895294189 
		1;
	setAttr -s 9 ".koy[6:8]"  0.99999475479125977 0.9999738335609436 
		0;
createNode animCurveTL -n "horse_1:cc_l_legBK01_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 10 ".ktv[0:9]"  1 -60.961423534922304 2 6.451810013172361 
		3 75.506893507114114 5 183.61850821915294 7 211.80327969687244 8 211.80327969687244 
		10 211.80366004560872 11 211.11036732951055 12 237.6926666814104 13 289.8;
	setAttr -s 10 ".kit[0:9]"  1 10 10 10 3 3 10 1 
		10 1;
	setAttr -s 10 ".kot[0:9]"  1 10 10 10 3 3 10 1 
		10 1;
	setAttr -s 10 ".kix[0:9]"  0.00058521644677966833 0.00061064225155860186 
		0.0007055500173009932 0.0012228243285790086 1 1 1 0.0033908316399902105 0.0010590123711153865 
		0.0006338037783280015;
	setAttr -s 10 ".kiy[0:9]"  0.99999982118606567 0.99999982118606567 
		0.9999997615814209 0.99999922513961792 0 0 0 0.99999433755874634 0.99999940395355225 
		0.99999982118606567;
	setAttr -s 10 ".kox[0:9]"  0.00057792005827650428 0.00061064225155860186 
		0.0007055500173009932 0.0012228243285790086 1 1 1 0.0033908276818692684 0.0010590123711153865 
		0.0006338037783280015;
	setAttr -s 10 ".koy[0:9]"  0.99999988079071045 0.99999982118606567 
		0.9999997615814209 0.99999922513961792 0 0 0 0.99999427795410156 0.99999940395355225 
		0.99999982118606567;
createNode animCurveTA -n "horse_1:cc_l_legBK01_outPutAnimBank_1_rotateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 0 3 0 8 0 13 0;
createNode animCurveTA -n "horse_1:cc_l_legBK01_outPutAnimBank_1_rotateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 0 3 0 8 0 13 0;
createNode animCurveTA -n "horse_1:cc_l_legBK01_outPutAnimBank_1_rotateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 0 3 0 8 0 13 0;
createNode animCurveTU -n "horse_1:cc_l_legBK01_outPutAnimBank_1_fetlock_bk_curl";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 0 3 0 8 0 10 0 11 0 13 0;
createNode animCurveTU -n "horse_1:cc_l_legBK01_outPutAnimBank_1_hoof_bk_curl";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 9 ".ktv[0:8]"  1 102.40000000000002 3 47.619213444256104 
		5 6.3128932304025263 7 0 8 0 9 0 10 31.200000000000003 11 101.42706397521656 13 102.4;
	setAttr -s 9 ".kit[0:8]"  1 10 1 10 10 10 10 10 
		1;
	setAttr -s 9 ".kot[0:8]"  1 10 1 10 10 10 10 10 
		1;
	setAttr -s 9 ".kix[0:8]"  0.0035347521770745516 0.0017345345113426447 
		0.0050254971720278263 1 1 1 0.00082160829333588481 0.0017556158127263188 0.0026677753776311874;
	setAttr -s 9 ".kiy[0:8]"  -0.99999380111694336 -0.99999850988388062 
		-0.99998742341995239 0 0 0 0.99999970197677612 0.99999850988388062 -0.99999648332595825;
	setAttr -s 9 ".kox[0:8]"  0.0034655199851840734 0.0017345345113426447 
		0.0050254971720278263 1 1 1 0.00082160829333588481 0.0017556158127263188 0.0026677744463086128;
	setAttr -s 9 ".koy[0:8]"  -0.99999403953552246 -0.99999850988388062 
		-0.99998736381530762 0 0 0 0.99999970197677612 0.99999850988388062 -0.99999648332595825;
createNode animCurveTL -n "horse_1:cc_tail01_outPutAnimBank_1_translateX";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 7 0 13 0;
	setAttr -s 3 ".kit[1:2]"  10 3;
	setAttr -s 3 ".kot[1:2]"  10 3;
createNode animCurveTL -n "horse_1:cc_tail01_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 9.3360283893128315 4 3.7772638989299714 
		7 -0.062680527185682455 13 9.3360283893128315;
	setAttr -s 4 ".kit[0:3]"  3 10 10 3;
	setAttr -s 4 ".kot[0:3]"  3 10 10 3;
createNode animCurveTL -n "horse_1:cc_tail01_outPutAnimBank_1_translateZ";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  1 2.2635881117103165 4 -4.5718141108301795 
		7 -0.62981281051148819 13 2.2635881117103165;
	setAttr -s 4 ".kit[1:3]"  10 1 3;
	setAttr -s 4 ".kot[1:3]"  10 1 3;
	setAttr -s 4 ".kix[2:3]"  0.048025339841842651 1;
	setAttr -s 4 ".kiy[2:3]"  0.99884611368179321 0;
	setAttr -s 4 ".kox[2:3]"  0.048025336116552353 1;
	setAttr -s 4 ".koy[2:3]"  0.99884617328643799 0;
createNode animCurveTL -n "horse_1:cc_tail02_outPutAnimBank_1_translateX";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 7 0 13 0;
	setAttr -s 3 ".kit[1:2]"  10 3;
	setAttr -s 3 ".kot[1:2]"  10 3;
createNode animCurveTL -n "horse_1:cc_tail02_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 11.497204049920814 4 9.3329121780390718 
		7 5.4235911597809263 10 3.138038944238418 13 11.497204049920814;
	setAttr -s 5 ".kit[0:4]"  3 1 10 10 3;
	setAttr -s 5 ".kot[0:4]"  3 1 10 10 3;
	setAttr -s 5 ".kix[1:4]"  0.023731077089905739 0.040323123335838318 
		0.04112684354186058 1;
	setAttr -s 5 ".kiy[1:4]"  -0.99971836805343628 -0.99918669462203979 
		0.99915397167205811 0;
	setAttr -s 5 ".kox[1:4]"  0.023731080815196037 0.040323123335838318 
		0.04112684354186058 1;
	setAttr -s 5 ".koy[1:4]"  -0.99971842765808105 -0.99918669462203979 
		0.99915397167205811 0;
createNode animCurveTL -n "horse_1:cc_tail02_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -2.4888111478099701 4 -11.612903564371935 
		7 -13.246562818744332 10 0.70480158606201349 13 -2.4888111478099701;
	setAttr -s 5 ".kit[0:4]"  1 10 10 10 1;
	setAttr -s 5 ".kot[0:4]"  1 10 10 10 1;
	setAttr -s 5 ".kix[0:4]"  0.01700315810739994 0.023232782259583473 
		0.020291807129979134 0.023232785984873772 0.018993930891156197;
	setAttr -s 5 ".kiy[0:4]"  -0.99985545873641968 -0.99973005056381226 
		0.9997941255569458 0.99973005056381226 -0.99981963634490967;
	setAttr -s 5 ".kox[0:4]"  0.017003156244754791 0.023232782259583473 
		0.020291807129979134 0.023232785984873772 0.018993930891156197;
	setAttr -s 5 ".koy[0:4]"  -0.99985545873641968 -0.99973005056381226 
		0.9997941255569458 0.99973005056381226 -0.99981957674026489;
createNode animCurveTL -n "horse_1:cc_tail03_outPutAnimBank_1_translateX";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 7 0 13 0;
	setAttr -s 3 ".kit[1:2]"  10 3;
	setAttr -s 3 ".kot[1:2]"  10 3;
createNode animCurveTL -n "horse_1:cc_tail03_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 19.656976337937035 4 19.226721419624994 
		7 16.312194546339928 10 14.395389860163139 13 19.656976337937035;
	setAttr -s 5 ".kit[0:4]"  3 10 10 10 3;
	setAttr -s 5 ".kot[0:4]"  3 10 10 10 3;
createNode animCurveTL -n "horse_1:cc_tail03_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -7.2121010384883011 4 -19.977662021048722 
		7 -18.555410993219773 10 -13.223898152005228 13 -7.2121010384883011;
	setAttr -s 5 ".kit[0:4]"  3 10 10 10 3;
	setAttr -s 5 ".kot[0:4]"  3 10 10 10 3;
createNode animCurveTL -n "horse_1:cc_cc_tail04_outPutAnimBank_1_translateX";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 -2.6645352591003082e-015 7 -2.6645352591003082e-015 
		13 -2.6645352591003082e-015;
	setAttr -s 3 ".kit[1:2]"  10 3;
	setAttr -s 3 ".kot[1:2]"  10 3;
createNode animCurveTL -n "horse_1:cc_cc_tail04_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 28.371662491355877 4 28.968197186145659 
		7 27.704827661867757 10 27.396386153296451 13 28.371662491355877;
	setAttr -s 5 ".kit[0:4]"  1 10 10 10 1;
	setAttr -s 5 ".kot[0:4]"  1 10 10 10 1;
	setAttr -s 5 ".kix[0:4]"  0.024980081245303154 0.35104575753211975 
		0.15707775950431824 0.35104581713676453 0.023504434153437614;
	setAttr -s 5 ".kiy[0:4]"  -0.99968796968460083 -0.93635827302932739 
		-0.98758620023727417 0.93635827302932739 -0.99972373247146606;
	setAttr -s 5 ".kox[0:4]"  0.024980094283819199 0.35104575753211975 
		0.15707775950431824 0.35104581713676453 0.023504428565502167;
	setAttr -s 5 ".koy[0:4]"  -0.99968796968460083 -0.93635827302932739 
		-0.98758620023727417 0.93635827302932739 -0.99972373247146606;
createNode animCurveTL -n "horse_1:cc_cc_tail04_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -13.28752994772343 4 -22.174172119735939 
		7 -24.200086143166462 10 -25.421711790241549 13 -13.28752994772343;
	setAttr -s 5 ".kit[0:4]"  3 10 10 1 3;
	setAttr -s 5 ".kot[0:4]"  3 10 10 1 3;
	setAttr -s 5 ".kix[3:4]"  0.015869317576289177 1;
	setAttr -s 5 ".kiy[3:4]"  0.99987411499023438 0;
	setAttr -s 5 ".kox[3:4]"  0.015869313850998878 1;
	setAttr -s 5 ".koy[3:4]"  0.99987411499023438 0;
createNode animCurveTL -n "horse_1:cc_tail05_outPutAnimBank_1_translateX";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 7 0 13 0;
	setAttr -s 3 ".kit[1:2]"  10 3;
	setAttr -s 3 ".kot[1:2]"  10 3;
createNode animCurveTL -n "horse_1:cc_tail05_outPutAnimBank_1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 30.792450125970028 4 23.455555893584652 
		7 26.26551247861191 10 30.322705882236455 13 30.792450125970028;
	setAttr -s 5 ".kit[0:4]"  1 10 10 10 1;
	setAttr -s 5 ".kot[0:4]"  1 10 10 10 1;
	setAttr -s 5 ".kix[0:4]"  0.014853638596832752 0.055140946060419083 
		0.036381103098392487 0.055140957236289978 0.023603560402989388;
	setAttr -s 5 ".kiy[0:4]"  -0.99988967180252075 -0.99847859144210815 
		0.99933803081512451 0.99847859144210815 -0.99972140789031982;
	setAttr -s 5 ".kox[0:4]"  0.014853633008897305 0.055140946060419083 
		0.036381103098392487 0.055140957236289978 0.023603567853569984;
	setAttr -s 5 ".koy[0:4]"  -0.99988967180252075 -0.99847859144210815 
		0.99933803081512451 0.99847859144210815 -0.99972140789031982;
createNode animCurveTL -n "horse_1:cc_tail05_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -23.040376186045805 4 -19.079289273476526 
		7 -29.803470438839142 10 -33.522671002719257 13 -23.040376186045805;
	setAttr -s 5 ".kit[0:4]"  1 10 10 10 1;
	setAttr -s 5 ".kot[0:4]"  1 10 10 10 1;
	setAttr -s 5 ".kix[0:4]"  0.019188342615962029 0.036940097808837891 
		0.0173063725233078 0.036940101534128189 0.016409901902079582;
	setAttr -s 5 ".kiy[0:4]"  0.99981588125228882 -0.999317467212677 
		-0.99985021352767944 0.999317467212677 0.99986541271209717;
	setAttr -s 5 ".kox[0:4]"  0.019188325852155685 0.036940097808837891 
		0.0173063725233078 0.036940101534128189 0.016409903764724731;
	setAttr -s 5 ".koy[0:4]"  0.99981588125228882 -0.999317467212677 
		-0.99985021352767944 0.999317467212677 0.99986535310745239;
createNode animCurveTL -n "horse_1:cc_tail06_outPutAnimBank_1_translateX";
	setAttr ".tan" 3;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 0 7 0 13 0;
	setAttr -s 3 ".kit[1:2]"  10 3;
	setAttr -s 3 ".kot[1:2]"  10 3;
createNode animCurveTL -n "horse_1:cc_tail06_outPutAnimBank_1_translateY";
	setAttr ".tan" 1;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 33.252811958704228 4 22.337101448535954 
		7 15.970213049129228 10 26.584026488770554 13 33.252811958704228;
	setAttr -s 5 ".kit[0:4]"  3 1 10 1 3;
	setAttr -s 5 ".kot[0:4]"  3 1 10 1 3;
	setAttr -s 5 ".kix[1:4]"  0.011404475197196007 0.058764386922121048 
		0.014591765590012074 1;
	setAttr -s 5 ".kiy[1:4]"  -0.99993503093719482 0.9982718825340271 
		0.99989354610443115 0;
	setAttr -s 5 ".kox[1:4]"  0.011404472403228283 0.058764386922121048 
		0.014591761864721775 1;
	setAttr -s 5 ".koy[1:4]"  -0.99993497133255005 0.9982718825340271 
		0.99989354610443115 0;
createNode animCurveTL -n "horse_1:cc_tail06_outPutAnimBank_1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  1 -37.261201168130228 4 -26.550310644695596 
		7 -27.528512074112818 10 -38.080888082529945 13 -37.261201168130228;
	setAttr -s 5 ".kit[0:4]"  3 10 10 10 3;
	setAttr -s 5 ".kot[0:4]"  3 10 10 10 3;
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
// End of run.ma

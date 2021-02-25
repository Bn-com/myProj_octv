from maya.cmds import*
import maya.mel as mm
def North_FaceCtrlTools():   
    winName = "North_FaceCtrl"
    if window(winName, q = True, ex = True):
        deleteUI(winName)
    window(winName, w= 280, h= 280, title = "North_FaceCtrlTools", rtf = True)

    form = formLayout()
    tabs = tabLayout(innerMarginWidth=5, innerMarginHeight=5)
    formLayout( form, edit=True, attachForm=((tabs, 'top', 0), (tabs, 'left', 0), (tabs, 'bottom', 0), (tabs, 'right', 0)) )
    
    #---------------------------- easyAnimCurve IO -------------------------#
    child = columnLayout(adj = True)
    separator(h = 10)
    text(l = "")
    button(l = "select EyeBrow",c = "from idmt.maya.norch import North_FaceCtrlTools\nreload(North_FaceCtrlTools)\nNorth_FaceCtrlTools.North_SelectEyeBrow()")
    button(l = "Select EyeLid", c = "from idmt.maya.norch import North_FaceCtrlTools\nreload(North_FaceCtrlTools)\nNorth_FaceCtrlTools.North_SelectEyeLid()")
    button(l = "Select EyeBall", c = "from idmt.maya.norch import North_FaceCtrlTools\nreload(North_FaceCtrlTools)\nNorth_FaceCtrlTools.North_SelectEyeBall()")
    button(l = "-----EyesALL-----", c = "from idmt.maya.norch import North_FaceCtrlTools\nreload(North_FaceCtrlTools)\nNorth_FaceCtrlTools.North_SelectEyesALL()")
    separator(h = 10)
    button(l = "Select Nose", c = "from idmt.maya.norch import North_FaceCtrlTools\nreload(North_FaceCtrlTools)\nNorth_FaceCtrlTools.North_SelectNose()")
    separator(h = 10)
    button(l = "Select Teeth", c = "from idmt.maya.norch import North_FaceCtrlTools\nreload(North_FaceCtrlTools)\nNorth_FaceCtrlTools.North_SelectTeeth()")
    button(l = "Select Tongue", c = "from idmt.maya.norch import North_FaceCtrlTools\nreload(North_FaceCtrlTools)\nNorth_FaceCtrlTools.North_SelectTongue()")
    button(l = "Select Mouth", c = "from idmt.maya.norch import North_FaceCtrlTools\nreload(North_FaceCtrlTools)\nNorth_FaceCtrlTools.North_SelectMouth()")
    button(l = "Select MouthLip", c = "from idmt.maya.norch import North_FaceCtrlTools\nreload(North_FaceCtrlTools)\nNorth_FaceCtrlTools.North_SelectMouthLip()")
#    button(l = "Select -O- ", c = "HbSelectA_U_O_FV_the_eee_Mbp()")
    button(l = "-----MouthALL-----", c = "from idmt.maya.norch import North_FaceCtrlTools\nreload(North_FaceCtrlTools)\nNorth_FaceCtrlTools.North_SelectMouthALL()")
    separator(h = 10)
    separator(h = 10)
    button(l = "-----Face ALL-----", c = "from idmt.maya.norch import North_FaceCtrlTools\nreload(North_FaceCtrlTools)\nNorth_FaceCtrlTools.North_SelectFaceAll()")
    separator(h = 10)
    separator(h = 10)

    checkBox( "North_ADD",label='ADD' )



    text(l = " ")
    text(l = " ")
    text(l = " ")

    
    text(l = "CJW")

    text(l = "-----------------------")
    text(l = "GDC-IDMT 2015 (C)\n")
    setParent( '..' )
    
    tabLayout( tabs, edit=True, tabLabel=((child,"FacialRIG")))

    

    child = columnLayout(adj = True)
    separator(h = 10)
    text(l = "")
    button(l = "select Lf_hand",c = "from idmt.maya.norch import North_FaceCtrlTools\nreload(North_FaceCtrlTools)\nNorth_FaceCtrlTools.North_SelectLf_hand()")
    button(l = "Select Lf_Arm", c = "from idmt.maya.norch import North_FaceCtrlTools\nreload(North_FaceCtrlTools)\nNorth_FaceCtrlTools.North_SelectLf_Arm()")
    button(l = "-----ALL_Lf_Arm-----", c = "from idmt.maya.norch import North_FaceCtrlTools\nreload(North_FaceCtrlTools)\nNorth_FaceCtrlTools.North_SelectLf_ArmALL()")
    separator(h = 10)
    button(l = "Select Rt_hand", c = "from idmt.maya.norch import North_FaceCtrlTools\nreload(North_FaceCtrlTools)\nNorth_FaceCtrlTools.North_SelectRt_hand()")
    button(l = "Select Rt_Arm", c = "from idmt.maya.norch import North_FaceCtrlTools\nreload(North_FaceCtrlTools)\nNorth_FaceCtrlTools.North_SelectRt_Arm()")
    button(l = "-----ALL_Rt_Arm-----", c = "from idmt.maya.norch import North_FaceCtrlTools\nreload(North_FaceCtrlTools)\nNorth_FaceCtrlTools.North_SelectRt_ArmALL()")
    separator(h = 10)
#    button(l = "Select Lf_Toes", c = "HbSelectLf_Toes()")
    button(l = "Select Lf_Leg", c = "from idmt.maya.norch import North_FaceCtrlTools\nreload(North_FaceCtrlTools)\nNorth_FaceCtrlTools.North_SelectLf_Leg()")
    separator(h = 10)
#    button(l = "Select Rt_Toes", c = "HbSelectRt_Toes()")
    button(l = "Select Rt_Leg", c = "from idmt.maya.norch import North_FaceCtrlTools\nreload(North_FaceCtrlTools)\nNorth_FaceCtrlTools.North_SelectRt_Leg()")
    separator(h = 10)
    separator(h = 10)
#    button(l = "Select Hair", c = "HbSelectHair()")
    button(l = "-----ALL_Body-----", c = "from idmt.maya.norch import North_FaceCtrlTools\nreload(North_FaceCtrlTools)\nNorth_FaceCtrlTools.North_SelectALL_Body()")   
    separator(h = 10)


    checkBox( "North_ADD",label='ADD' )



    text(l = " ")
    text(l = " ")
    text(l = " ")

    
    text(l = "CJW")

    text(l = "-----------------------")
    text(l = "GDC-IDMT 2014 (C)\n")
    setParent( '..' )
    
    tabLayout( tabs, edit=True, tabLabel=((child,"BodyRIG")))


    showWindow(winName)

def North_SelectEyeBrow():
    getTheName=ls(sl=1)
    getTHeNum=getTheName[0].split(":")
    TheNameSpace=""
    if len(getTHeNum)>1:
        for i in range(len(getTHeNum)-1):
            TheNameSpace=TheNameSpace+getTHeNum[i]+":"
    if len(getTHeNum)==1:
        TheNameSpace=""
    questADD=checkBox("North_ADD",q=1,v=1)
    if questADD==0:
        select(cl=1)

    Ctrls = ["c_Lf_eyebrows_CTRL","c_Lf_eyebrows_01_CTRL","c_Lf_eyebrows_02_CTRL","c_Lf_eyebrows_03_CTRL",
"c_Rt_eyebrows_CTRL","c_Rt_eyebrows_01_CTRL","c_Rt_eyebrows_02_CTRL","c_Rt_eyebrows_03_CTRL",
"r_eyeBrow_Curl","r_eyeBrow_Surprise_Flat","r_eyeBrow_Sad","r_eyeBrow_Angry",
"r_eyeBrow_Angry","l_eyeBrow_Sad","l_eyeBrow_Surprise_Flat","l_eyeBrow_Curl",
"eyeBrow_Mid_In_Out","r_eyeBrow_Worried","l_eyeBrow_Worried","l_eyeBrow_Angry",
"eYebrw_flOat_L_ctlr","eYebrw_flOat_L1_ctlr","eYebrw_flOat_L2_ctlr","eYebrw_flOat_L3_ctlr","eYebrw_flOat_L4_ctlr",
"eYebrw_flOat_R_ctlr","eYebrw_flOat_R1_ctlr","eYebrw_flOat_R2_ctlr","eYebrw_flOat_R3_ctlr","eYebrw_flOat_R4_ctlr",
"eyebrw_mid1_ctlr","eyebrw_mid_ctlr","eyebrw_base_L_ctrl","eyebrw_base_R_ctrl",
"eyebrw_R2_ctlr",
"eyebrw_R1_ctlr",
"eyebrw_R_ctlr",
"forehead_jnt_ctlr",
"eyebrw_L_ctlr",
"eyebrw_L1_ctlr",
"eyebrw_L2_ctlr",
"R_EyeBrow_03_ctlr","R_EyeBrow_02_ctlr","R_EyeBrow_01_ctlr",
"L_EyeBrow_01_ctlr","L_EyeBrow_02_ctlr","L_EyeBrow_03_ctlr"

]

    for Ctrl in Ctrls:
        ctrl = TheNameSpace + Ctrl
        if objExists(ctrl)==True:
            select(ctrl,add=1)
    
        
def North_SelectEyeLid():
    getTheName=ls(sl=1)
    getTHeNum=getTheName[0].split(":")
    TheNameSpace=""
    if len(getTHeNum)>1:
        for i in range(len(getTHeNum)-1):
            TheNameSpace=TheNameSpace+getTHeNum[i]+":"
    if len(getTHeNum)==1:
        TheNameSpace=""
    questADD=checkBox("North_ADD",q=1,v=1)
    if questADD==0:
        select(cl=1)

    Ctrls = ["c_Rt_up_eyelids_CTRL","c_Rt_dn_eyelids_CTRL","c_Rt_eyelids_CTRL",
"c_Lf_up_eyelids_CTRL","c_Lf_dn_eyelids_CTRL","c_Lf_eyelids_CTRL",
"r_lower_eye_socket","r_eye_Sliders","l_lower_eye_socket","l_eye_Sliders",
"Eye_Lid_R_ctlr","Eye_Lld_R_ctlr","Eye_Lld_L_ctlr",
"Eye_R_Pop_ctlr","Eye_L_Pop_ctlr",
"eye_R_jnt_ctlr","eye_L_jnt_ctlr",
"eyelash_*_*_ctlr"
]    

    for Ctrl in Ctrls:
        ctrl = TheNameSpace + Ctrl
        if objExists(ctrl)==True:
            select(ctrl,add=1)


def North_SelectEyeBall():
    getTheName=ls(sl=1)
    getTHeNum=getTheName[0].split(":")
    TheNameSpace=""
    if len(getTHeNum)>1:
        for i in range(len(getTHeNum)-1):
            TheNameSpace=TheNameSpace+getTHeNum[i]+":"
    if len(getTHeNum)==1:
        TheNameSpace=""
    questADD=checkBox("North_ADD",q=1,v=1)
    if questADD==0:
        select(cl=1)

    Ctrls = ["c_eye_M","c_Lf_eye_M","c_Lf_spec_M","c_Rt_eye_M","c_Rt_spec_M",
"AimCurveEye_M","FKCurveEye_L","FKCurveEye_R"]    

    for Ctrl in Ctrls:
        ctrl = TheNameSpace + Ctrl
        if objExists(ctrl)==True:
            select(ctrl,add=1)    

    
def North_SelectEyesALL():
    getTheName=ls(sl=1)
    getTHeNum=getTheName[0].split(":")
    TheNameSpace=""
    if len(getTHeNum)>1:
        for i in range(len(getTHeNum)-1):
            TheNameSpace=TheNameSpace+getTHeNum[i]+":"
    if len(getTHeNum)==1:
        TheNameSpace=""
    questADD=checkBox("North_ADD",q=1,v=1)
    if questADD==0:
        select(cl=1)
    Ctrls = ["c_Lf_eyebrows_CTRL","c_Lf_eyebrows_01_CTRL","c_Lf_eyebrows_02_CTRL","c_Lf_eyebrows_03_CTRL",
"c_Rt_eyebrows_CTRL","c_Rt_eyebrows_01_CTRL","c_Rt_eyebrows_02_CTRL","c_Rt_eyebrows_03_CTRL",
"r_eyeBrow_Curl","r_eyeBrow_Surprise_Flat","r_eyeBrow_Sad","r_eyeBrow_Angry",
"r_eyeBrow_Angry","l_eyeBrow_Sad","l_eyeBrow_Surprise_Flat","l_eyeBrow_Curl",
"eyeBrow_Mid_In_Out","r_eyeBrow_Worried","l_eyeBrow_Worried","l_eyeBrow_Angry",
"eYebrw_flOat_L_ctlr","eYebrw_flOat_L1_ctlr","eYebrw_flOat_L2_ctlr","eYebrw_flOat_L3_ctlr","eYebrw_flOat_L4_ctlr",
"eYebrw_flOat_R_ctlr","eYebrw_flOat_R1_ctlr","eYebrw_flOat_R2_ctlr","eYebrw_flOat_R3_ctlr","eYebrw_flOat_R4_ctlr",
"eyebrw_mid1_ctlr","eyebrw_mid_ctlr","eyebrw_base_L_ctrl","eyebrw_base_R_ctrl",
"eyebrw_R2_ctlr",
"eyebrw_R1_ctlr",
"eyebrw_R_ctlr",
"forehead_jnt_ctlr",
"eyebrw_L_ctlr",
"eyebrw_L1_ctlr",
"eyebrw_L2_ctlr",
"c_Rt_up_eyelids_CTRL","c_Rt_dn_eyelids_CTRL","c_Rt_eyelids_CTRL",
"c_Lf_up_eyelids_CTRL","c_Lf_dn_eyelids_CTRL","c_Lf_eyelids_CTRL",
"r_lower_eye_socket","r_eye_Sliders","l_lower_eye_socket","l_eye_Sliders",
"Eye_Lid_R_ctlr","Eye_Lld_R_ctlr","Eye_Lld_L_ctlr",
"Eye_R_Pop_ctlr","Eye_L_Pop_ctlr",
"c_eye_M","c_Lf_eye_M","c_Lf_spec_M","c_Rt_eye_M","c_Rt_spec_M",
"AimCurveEye_M","FKCurveEye_L","FKCurveEye_R",
"R_EyeBrow_03_ctlr","R_EyeBrow_02_ctlr","R_EyeBrow_01_ctlr",
"L_EyeBrow_01_ctlr","L_EyeBrow_02_ctlr","L_EyeBrow_03_ctlr",
"eye_R_jnt_ctlr","eye_L_jnt_ctlr",
"eyelash_*_*_ctlr"
]

    for Ctrl in Ctrls:
        ctrl = TheNameSpace + Ctrl
        if objExists(ctrl)==True:
            select(ctrl,add=1)

def North_SelectNose():
    getTheName=ls(sl=1)
    getTHeNum=getTheName[0].split(":")
    TheNameSpace=""
    if len(getTHeNum)>1:
        for i in range(len(getTHeNum)-1):
            TheNameSpace=TheNameSpace+getTHeNum[i]+":"
    if len(getTHeNum)==1:
        TheNameSpace=""
    questADD=checkBox("North_ADD",q=1,v=1)
    if questADD==0:
        select(cl=1)

    Ctrls = ["c_nose_M_CTRL","c_nose_CTRL","c_Rt_nosewing_CTRL","c_Lf_nosewing_CTRL",
"Snarl","nose_flare_R_ctlr","nose_flare_L_ctlr",
"ns_r_nose_up","ns_l_nose_up",
"FKCurveuprJaw1_M","FKCurveuprJaw2_M","FKCurveuprJaw4_M",
"R_Nose_ctlr","L_Nose_ctlr",
"nose_mid_ctlr"
]    

    for Ctrl in Ctrls:
        ctrl = TheNameSpace + Ctrl
        if objExists(ctrl)==True:
            select(ctrl,add=1)      


def North_SelectTeeth():
    getTheName=ls(sl=1)
    getTHeNum=getTheName[0].split(":")
    TheNameSpace=""
    if len(getTHeNum)>1:
        for i in range(len(getTHeNum)-1):
            TheNameSpace=TheNameSpace+getTHeNum[i]+":"
    if len(getTHeNum)==1:
        TheNameSpace=""
    questADD=checkBox("North_ADD",q=1,v=1)
    if questADD==0:
        select(cl=1)

    Ctrls = ["uptooth_ctrl","lowtooth_ctrl",
"upTeeth_ctrl","lowTeeth_ctrl",
"FKCurveupper_teeth_M","FKCurvelower_teeth_M",
"upper_teeth_ctlr","lower_teeth_ctlr"
]    

    for Ctrl in Ctrls:
        ctrl = TheNameSpace + Ctrl
        if objExists(ctrl)==True:
            select(ctrl,add=1)        
  
def North_SelectTongue():
    getTheName=ls(sl=1)
    getTHeNum=getTheName[0].split(":")
    TheNameSpace=""
    if len(getTHeNum)>1:
        for i in range(len(getTHeNum)-1):
            TheNameSpace=TheNameSpace+getTHeNum[i]+":"
    if len(getTHeNum)==1:
        TheNameSpace=""
    questADD=checkBox("North_ADD",q=1,v=1)
    if questADD==0:
        select(cl=1)

    Ctrls = ["c_tongue_CTRL","c_tongue_joint1","c_tongue_joint2","c_tongue_joint3","c_tongue_joint4",
"c_tongue_joint5","c_tongue_joint6","c_tongue_joint7","c_tongue_joint8","c_tongue_joint9",           
"FKCurveTongue1_M","FKCurveTongue2_M","FKCurveTongue3_M","FKCurveTongue4_M",
"FKCurveTongue5_M","FKCurveTongue6_M","FKCurveTongue7_M","FKCurveTongue8_M",
"FKCurveTongue9_M","FKCurveTongue10_M","FKCurveTongue11_M","FKCurveTongue12_M",
"FKCurveTongue13_M"]    

    for Ctrl in Ctrls:
        ctrl = TheNameSpace + Ctrl
        if objExists(ctrl)==True:
            select(ctrl,add=1)     

def North_SelectMouth():
    getTheName=ls(sl=1)
    getTHeNum=getTheName[0].split(":")
    TheNameSpace=""
    if len(getTHeNum)>1:
        for i in range(len(getTHeNum)-1):
            TheNameSpace=TheNameSpace+getTHeNum[i]+":"
    if len(getTHeNum)==1:
        TheNameSpace=""
    questADD=checkBox("North_ADD",q=1,v=1)
    if questADD==0:
        select(cl=1)

    Ctrls = ["c_mouth_CTRL","c_jaw_dn_CTRL","c_Rt_mouthLip_CTRL","c_Lf_mouthLip_CTRL","c_dn_mouthLip_CTRL","c_up_mouthLip_CTRL",
"c_Rt_eyeStretch_CTRL","c_Lf_eyeStretch_CTRL","uptooth_ctrl","lowtooth_ctrl","upTeeth_ctrl","lowTeeth_ctrl",              
"LipRoll","mo_r_small_wide","r_puff","r_puff_02","l_puff_02","l_puff",
"mo_l_small_wide","Laugh","Up_JawDrop","Dn_JawDrop",
"smile_sad",
"r_lwr_sneer_asneer","r_upr_sneer_asneer",
"Snarl",
"l_upr_sneer_asneer","l_lwr_sneer_asneer","l_evil_happy","Ah","U",
"Sync",
"F","lwr_lip_close","r_evil_happy","maniacal_laugh","L","angry_yell",
"indifference","shocked","extrm_shocked","surprise","l_smirk","r_smirk",
"lip_Slide","lips_base_ctrl","Cheek_R_ctlr","Cheek_L_ctlr","FKCurveJaw_M",
"cheek_R_01_ctlr","cheek_L_01_ctlr","cheek_R_ctlr","cheek_L_ctlr",
"upper_lip_R_ctlr","upper_mid_lip_ctlr","upper_lip_L_ctlr",
"lower_lip_R_ctlr","lower_mid_lip_ctlr","lower_lip_L_ctlr",
"corner_lip_R_ctlr","corner_lip_R1_ctlr","upper_lip_R1_ctlr","lower_lip_R1_ctlr",
"corner_lip_L_ctlr","corner_lip_L1_ctlr","upper_lip_L1_ctlr","lower_lip_L1_ctlr",
"FKCurveJaw2_M","FKCurveJaw3_M","FKCurveJaw4_M","FKCurveJaw5_M","FKCurveJaw6_M",
"mo_r_scared","mo_r_sneer_new","mo_r_sad_02","mo_r_sad_01","mo_l_sad_02","mo_l_sad_01","mo_l_sneer_new","mo_l_scared",
"O2","O3","U2","ph_oo_new","o_small",
"mo_01_upset","mo_02_upset","very_happy","zoned_out","extreme_shock"
]    

    for Ctrl in Ctrls:
        ctrl = TheNameSpace + Ctrl
        if objExists(ctrl)==True:
            select(ctrl,add=1)     

    
def North_SelectMouthLip():
    getTheName=ls(sl=1)
    getTHeNum=getTheName[0].split(":")
    TheNameSpace=""
    if len(getTHeNum)>1:
        for i in range(len(getTHeNum)-1):
            TheNameSpace=TheNameSpace+getTHeNum[i]+":"
    if len(getTHeNum)==1:
        TheNameSpace=""
    questADD=checkBox("North_ADD",q=1,v=1)
    if questADD==0:
        select(cl=1)

    Ctrls = ["c_muothLip_01_second_CTRL","c_muothLip_02_second_CTRL","c_muothLip_03_second_CTRL","c_muothLip_04_second_CTRL",
"c_muothLip_05_second_CTRL","c_muothLip_06_second_CTRL","c_muothLip_07_second_CTRL","c_muothLip_08_second_CTRL",  
"uppEr_lip_R_ctlr","uppEr_lip_mid_ctlr","uppEr_lip_L_ctlr",        
"lOwer_lip_R_ctlr","lOwer_lip_mid_ctlr","lOwer_lip_L_ctlr",
"uppEr_lip_R1_ctlr","Corner_lip_R_ctlr","cOrner_ext_lip_R_ctlr","lOwer_lip_R1_ctlr",
"uppEr_lip_L1_ctlr","Corner_lip_L_ctlr","cOrner_ext_lip_L_ctlr","lOwer_lip_L1_ctlr",
"upper_lip_R_ctlr","upper_mid_lip_ctlr","upper_lip_L_ctlr",
"lower_lip_R_ctlr","lower_mid_lip_ctlr","lower_lip_L_ctlr",
"corner_lip_R_ctlr","corner_lip_R1_ctlr","upper_lip_R1_ctlr","lower_lip_R1_ctlr",
"corner_lip_L_ctlr","corner_lip_L1_ctlr","upper_lip_L1_ctlr","lower_lip_L1_ctlr",
"UprLip_Mian_R_1_jt_ctlr","UprLip_Mian_L_1_jt_ctlr","UprLip_Mian_R_2_jt_ctlr","UprLip_Mian_L_2_jt_ctlr","UprLip_Mian_mid_3_jt_ctlr",
"WlrLip_Mian_R_1_jt_ctlr","WlrLip_Mian_L_1_jt_ctlr","WlrLip_Mian_L_2_jt_ctlr","WlrLip_Mian_R_2_jt_ctlr","WlrLip_Mian_mid_3_jt_ctlr",
"Lip_Corner_R_ctlr","UprLip_1_R_ctlr","LwrLip_1_R_ctlr","UprLip_2_R_ctlr","LwrLip_2_R_ctlr",
"UprLip_3_R_ctlr","LwrLip_3_R_ctlr","UprLip_4_R_ctlr","LwrLip_4_R_ctlr",
"UprLip_5_R_ctlr","UprLip_6_R_ctlr","LwrLip_5_R_ctlr","LwrLip_6_R_ctlr",
"UprLip_M_ctlr","LwrLip_M_ctlr","UprLip_6_L_ctlr","LwrLip_6_L_ctlr",
"UprLip_5_L_ctlr","LwrLip_5_L_ctlr","UprLip_4_L_ctlr","LwrLip_4_L_ctlr",
"UprLip_3_L_ctlr","LwrLip_3_L_ctlr","UprLip_2_L_ctlr","LwrLip_2_L_ctlr",
"UprLip_1_L_ctlr______","LwrLip_1_L_ctlr","Lip_Corner_L_ctlr"
]    

    for Ctrl in Ctrls:
        ctrl = TheNameSpace + Ctrl
        if objExists(ctrl)==True:
            select(ctrl,add=1)       

def HbSelectA_U_O_FV_the_eee_Mbp():
    getTheName=ls(sl=1)
    getTHeNum=getTheName[0].split(":")
    TheNameSpace=""
    if len(getTHeNum)>1:
        for i in range(len(getTHeNum)-1):
            TheNameSpace=TheNameSpace+getTHeNum[i]+":"
    if len(getTHeNum)==1:
        TheNameSpace=""
    questADD=checkBox("North_ADD",q=1,v=1)
    if questADD==0:
        select(cl=1)
    try:
        select(TheNameSpace+"c_OU_CTRL",add=1)
    except:
        pass

def North_SelectMouthALL():
    getTheName=ls(sl=1)
    getTHeNum=getTheName[0].split(":")
    TheNameSpace=""
    if len(getTHeNum)>1:
        for i in range(len(getTHeNum)-1):
            TheNameSpace=TheNameSpace+getTHeNum[i]+":"
    if len(getTHeNum)==1:
        TheNameSpace=""
    questADD=checkBox("North_ADD",q=1,v=1)
    if questADD==0:
        select(cl=1)

    Ctrls = ["c_nose_M_CTRL","c_nose_CTRL","c_Rt_nosewing_CTRL","c_Lf_nosewing_CTRL",
"Snarl","nose_flare_R_ctlr","nose_flare_L_ctlr",
"uptooth_ctrl","lowtooth_ctrl",
"upTeeth_ctrl","lowTeeth_ctrl",
"FKCurveupper_teeth_M","FKCurvelower_teeth_M",
"c_tongue_CTRL","c_tongue_joint1","c_tongue_joint2","c_tongue_joint3","c_tongue_joint4",
"c_tongue_joint5","c_tongue_joint6","c_tongue_joint7","c_tongue_joint8","c_tongue_joint9",           
"FKCurveTongue1_M","FKCurveTongue2_M","FKCurveTongue3_M","FKCurveTongue4_M",
"FKCurveTongue5_M","FKCurveTongue6_M","FKCurveTongue7_M","FKCurveTongue8_M",
"FKCurveTongue9_M","FKCurveTongue10_M","FKCurveTongue11_M","FKCurveTongue12_M",
"FKCurveTongue13_M",
"c_mouth_CTRL","c_jaw_dn_CTRL","c_Rt_mouthLip_CTRL","c_Lf_mouthLip_CTRL","c_dn_mouthLip_CTRL","c_up_mouthLip_CTRL",
"c_Rt_eyeStretch_CTRL","c_Lf_eyeStretch_CTRL","uptooth_ctrl","lowtooth_ctrl","upTeeth_ctrl","lowTeeth_ctrl",              
"LipRoll","mo_r_small_wide","r_puff","r_puff_02","l_puff_02","l_puff",
"mo_l_small_wide","Laugh","Up_JawDrop","Dn_JawDrop",
"smile_sad",
"r_lwr_sneer_asneer","r_upr_sneer_asneer",
"Snarl",
"l_upr_sneer_asneer","l_lwr_sneer_asneer","l_evil_happy","Ah","U",
"Sync",
"F","lwr_lip_close","r_evil_happy","maniacal_laugh","L","angry_yell",
"indifference","shocked","extrm_shocked","surprise","l_smirk","r_smirk",
"lip_Slide","lips_base_ctrl","Cheek_R_ctlr","Cheek_L_ctlr","FKCurveJaw_M",
"cheek_R_01_ctlr","cheek_L_01_ctlr","cheek_R_ctlr","cheek_L_ctlr",
"upper_lip_R_ctlr","upper_mid_lip_ctlr","upper_lip_L_ctlr",
"lower_lip_R_ctlr","lower_mid_lip_ctlr","lower_lip_L_ctlr",
"corner_lip_R_ctlr","corner_lip_R1_ctlr","upper_lip_R1_ctlr","lower_lip_R1_ctlr",
"corner_lip_L_ctlr","corner_lip_L1_ctlr","upper_lip_L1_ctlr","lower_lip_L1_ctlr",
"c_muothLip_01_second_CTRL","c_muothLip_02_second_CTRL","c_muothLip_03_second_CTRL","c_muothLip_04_second_CTRL",
"c_muothLip_05_second_CTRL","c_muothLip_06_second_CTRL","c_muothLip_07_second_CTRL","c_muothLip_08_second_CTRL",  
"uppEr_lip_R_ctlr","uppEr_lip_mid_ctlr","uppEr_lip_L_ctlr",        
"lOwer_lip_R_ctlr","lOwer_lip_mid_ctlr","lOwer_lip_L_ctlr",
"uppEr_lip_R1_ctlr","Corner_lip_R_ctlr","cOrner_ext_lip_R_ctlr","lOwer_lip_R1_ctlr",
"uppEr_lip_L1_ctlr","Corner_lip_L_ctlr","cOrner_ext_lip_L_ctlr","lOwer_lip_L1_ctlr",
"FKCurveJaw2_M","FKCurveJaw3_M","FKCurveJaw4_M","FKCurveJaw5_M","FKCurveJaw6_M",
"mo_r_scared","mo_r_sneer_new","mo_r_sad_02","mo_r_sad_01","mo_l_sad_02","mo_l_sad_01","mo_l_sneer_new","mo_l_scared",
"O2","O3","U2","ph_oo_new","o_small",
"mo_01_upset","mo_02_upset","very_happy","zoned_out","extreme_shock",
"UprLip_Mian_R_1_jt_ctlr","UprLip_Mian_L_1_jt_ctlr","UprLip_Mian_R_2_jt_ctlr","UprLip_Mian_L_2_jt_ctlr","UprLip_Mian_mid_3_jt_ctlr",
"WlrLip_Mian_R_1_jt_ctlr","WlrLip_Mian_L_1_jt_ctlr","WlrLip_Mian_L_2_jt_ctlr","WlrLip_Mian_R_2_jt_ctlr","WlrLip_Mian_mid_3_jt_ctlr",
"Lip_Corner_R_ctlr","UprLip_1_R_ctlr","LwrLip_1_R_ctlr","UprLip_2_R_ctlr","LwrLip_2_R_ctlr",
"UprLip_3_R_ctlr","LwrLip_3_R_ctlr","UprLip_4_R_ctlr","LwrLip_4_R_ctlr",
"UprLip_5_R_ctlr","UprLip_6_R_ctlr","LwrLip_5_R_ctlr","LwrLip_6_R_ctlr",
"UprLip_M_ctlr","LwrLip_M_ctlr","UprLip_6_L_ctlr","LwrLip_6_L_ctlr",
"UprLip_5_L_ctlr","LwrLip_5_L_ctlr","UprLip_4_L_ctlr","LwrLip_4_L_ctlr",
"UprLip_3_L_ctlr","LwrLip_3_L_ctlr","UprLip_2_L_ctlr","LwrLip_2_L_ctlr",
"UprLip_1_L_ctlr______","LwrLip_1_L_ctlr","Lip_Corner_L_ctlr",
"nose_mid_ctlr",
"cheekline_R_ctlr","cheekline_L_ctlr"
]    

    for Ctrl in Ctrls:
        ctrl = TheNameSpace + Ctrl
        if objExists(ctrl)==True:
            select(ctrl,add=1)   



def North_SelectFaceAll():
    getTheName=ls(sl=1)
    getTHeNum=getTheName[0].split(":")
    TheNameSpace=""
    if len(getTHeNum)>1:
        for i in range(len(getTHeNum)-1):
            TheNameSpace=TheNameSpace+getTHeNum[i]+":"
    if len(getTHeNum)==1:
        TheNameSpace=""
    questADD=checkBox("North_ADD",q=1,v=1)
    if questADD==0:
        select(cl=1)
    Ctrls = ["c_Lf_eyebrows_CTRL","c_Lf_eyebrows_01_CTRL","c_Lf_eyebrows_02_CTRL","c_Lf_eyebrows_03_CTRL",
"c_Rt_eyebrows_CTRL","c_Rt_eyebrows_01_CTRL","c_Rt_eyebrows_02_CTRL","c_Rt_eyebrows_03_CTRL",
"r_eyeBrow_Curl","r_eyeBrow_Surprise_Flat","r_eyeBrow_Sad","r_eyeBrow_Angry",
"r_eyeBrow_Angry","l_eyeBrow_Sad","l_eyeBrow_Surprise_Flat","l_eyeBrow_Curl",
"eyeBrow_Mid_In_Out","r_eyeBrow_Worried","l_eyeBrow_Worried","l_eyeBrow_Angry",
"eYebrw_flOat_L_ctlr","eYebrw_flOat_L1_ctlr","eYebrw_flOat_L2_ctlr","eYebrw_flOat_L3_ctlr","eYebrw_flOat_L4_ctlr",
"eYebrw_flOat_R_ctlr","eYebrw_flOat_R1_ctlr","eYebrw_flOat_R2_ctlr","eYebrw_flOat_R3_ctlr","eYebrw_flOat_R4_ctlr",
"eyebrw_mid1_ctlr","eyebrw_mid_ctlr","eyebrw_base_L_ctrl","eyebrw_base_R_ctrl",
"eyebrw_R2_ctlr",
"eyebrw_R1_ctlr",
"eyebrw_R_ctlr",
"forehead_jnt_ctlr",
"eyebrw_L_ctlr",
"eyebrw_L1_ctlr",
"eyebrw_L2_ctlr",
"c_Rt_up_eyelids_CTRL","c_Rt_dn_eyelids_CTRL","c_Rt_eyelids_CTRL",
"c_Lf_up_eyelids_CTRL","c_Lf_dn_eyelids_CTRL","c_Lf_eyelids_CTRL",
"r_lower_eye_socket","r_eye_Sliders","l_lower_eye_socket","l_eye_Sliders",
"Eye_Lid_R_ctlr","Eye_Lld_R_ctlr","Eye_Lld_L_ctlr",
"Eye_R_Pop_ctlr","Eye_L_Pop_ctlr",
"c_eye_M","c_Lf_eye_M","c_Lf_spec_M","c_Rt_eye_M","c_Rt_spec_M",
"AimCurveEye_M","FKCurveEye_L","FKCurveEye_R",
"c_nose_M_CTRL","c_nose_CTRL","c_Rt_nosewing_CTRL","c_Lf_nosewing_CTRL",
"Snarl","nose_flare_R_ctlr","nose_flare_L_ctlr",
"uptooth_ctrl","lowtooth_ctrl",
"upTeeth_ctrl","lowTeeth_ctrl",
"FKCurveupper_teeth_M","FKCurvelower_teeth_M",
"c_tongue_CTRL","c_tongue_joint1","c_tongue_joint2","c_tongue_joint3","c_tongue_joint4",
"c_tongue_joint5","c_tongue_joint6","c_tongue_joint7","c_tongue_joint8","c_tongue_joint9",           
"FKCurveTongue1_M","FKCurveTongue2_M","FKCurveTongue3_M","FKCurveTongue4_M",
"FKCurveTongue5_M","FKCurveTongue6_M","FKCurveTongue7_M","FKCurveTongue8_M",
"FKCurveTongue9_M","FKCurveTongue10_M","FKCurveTongue11_M","FKCurveTongue12_M",
"FKCurveTongue13_M",
"c_mouth_CTRL","c_jaw_dn_CTRL","c_Rt_mouthLip_CTRL","c_Lf_mouthLip_CTRL","c_dn_mouthLip_CTRL","c_up_mouthLip_CTRL",
"c_Rt_eyeStretch_CTRL","c_Lf_eyeStretch_CTRL","uptooth_ctrl","lowtooth_ctrl","upTeeth_ctrl","lowTeeth_ctrl",              
"LipRoll","mo_r_small_wide","r_puff","r_puff_02","l_puff_02","l_puff",
"mo_l_small_wide","Laugh","Up_JawDrop","Dn_JawDrop",
"smile_sad",
"r_lwr_sneer_asneer","r_upr_sneer_asneer",
"Snarl",
"l_upr_sneer_asneer","l_lwr_sneer_asneer","l_evil_happy","Ah","U",
"Sync",
"F","lwr_lip_close","r_evil_happy","maniacal_laugh","L","angry_yell",
"indifference","shocked","extrm_shocked","surprise","l_smirk","r_smirk",
"lip_Slide","lips_base_ctrl","Cheek_R_ctlr","Cheek_L_ctlr","FKCurveJaw_M",
"cheek_R_01_ctlr","cheek_L_01_ctlr","cheek_R_ctlr","cheek_L_ctlr",
"upper_lip_R_ctlr","upper_mid_lip_ctlr","upper_lip_L_ctlr",
"lower_lip_R_ctlr","lower_mid_lip_ctlr","lower_lip_L_ctlr",
"corner_lip_R_ctlr","corner_lip_R1_ctlr","upper_lip_R1_ctlr","lower_lip_R1_ctlr",
"corner_lip_L_ctlr","corner_lip_L1_ctlr","upper_lip_L1_ctlr","lower_lip_L1_ctlr",
"c_muothLip_01_second_CTRL","c_muothLip_02_second_CTRL","c_muothLip_03_second_CTRL","c_muothLip_04_second_CTRL",
"c_muothLip_05_second_CTRL","c_muothLip_06_second_CTRL","c_muothLip_07_second_CTRL","c_muothLip_08_second_CTRL",  
"uppEr_lip_R_ctlr","uppEr_lip_mid_ctlr","uppEr_lip_L_ctlr",        
"lOwer_lip_R_ctlr","lOwer_lip_mid_ctlr","lOwer_lip_L_ctlr",
"uppEr_lip_R1_ctlr","Corner_lip_R_ctlr","cOrner_ext_lip_R_ctlr","lOwer_lip_R1_ctlr",
"uppEr_lip_L1_ctlr","Corner_lip_L_ctlr","cOrner_ext_lip_L_ctlr","lOwer_lip_L1_ctlr",
"R_EyeBrow_03_ctlr","R_EyeBrow_02_ctlr","R_EyeBrow_01_ctlr",
"L_EyeBrow_01_ctlr","L_EyeBrow_02_ctlr","L_EyeBrow_03_ctlr",
"ns_r_nose_up","ns_l_nose_up",
"FKCurveuprJaw1_M","FKCurveuprJaw2_M","FKCurveuprJaw4_M",
"R_Nose_ctlr","L_Nose_ctlr",
"upper_teeth_ctlr","lower_teeth_ctlr",
"FKCurveJaw2_M","FKCurveJaw3_M","FKCurveJaw4_M","FKCurveJaw5_M","FKCurveJaw6_M",
"mo_r_scared","mo_r_sneer_new","mo_r_sad_02","mo_r_sad_01","mo_l_sad_02","mo_l_sad_01","mo_l_sneer_new","mo_l_scared",
"O2","O3","U2","ph_oo_new","o_small",
"mo_01_upset","mo_02_upset","very_happy","zoned_out","extreme_shock",
"UprLip_Mian_R_1_jt_ctlr","UprLip_Mian_L_1_jt_ctlr","UprLip_Mian_R_2_jt_ctlr","UprLip_Mian_L_2_jt_ctlr","UprLip_Mian_mid_3_jt_ctlr",
"WlrLip_Mian_R_1_jt_ctlr","WlrLip_Mian_L_1_jt_ctlr","WlrLip_Mian_L_2_jt_ctlr","WlrLip_Mian_R_2_jt_ctlr","WlrLip_Mian_mid_3_jt_ctlr",
"Lip_Corner_R_ctlr","UprLip_1_R_ctlr","LwrLip_1_R_ctlr","UprLip_2_R_ctlr","LwrLip_2_R_ctlr",
"UprLip_3_R_ctlr","LwrLip_3_R_ctlr","UprLip_4_R_ctlr","LwrLip_4_R_ctlr",
"UprLip_5_R_ctlr","UprLip_6_R_ctlr","LwrLip_5_R_ctlr","LwrLip_6_R_ctlr",
"UprLip_M_ctlr","LwrLip_M_ctlr","UprLip_6_L_ctlr","LwrLip_6_L_ctlr",
"UprLip_5_L_ctlr","LwrLip_5_L_ctlr","UprLip_4_L_ctlr","LwrLip_4_L_ctlr",
"UprLip_3_L_ctlr","LwrLip_3_L_ctlr","UprLip_2_L_ctlr","LwrLip_2_L_ctlr",
"UprLip_1_L_ctlr______","LwrLip_1_L_ctlr","Lip_Corner_L_ctlr",
"Jaw_sqst_ctrl","Snout_sqst_ctrl","UP_Jaw_sqst_ctrl","Head_sqst_ctrl","Face_sqst_ctrl",
"eye_R_jnt_ctlr","eye_L_jnt_ctlr",
"eyelash_*_*_ctlr",
"nose_mid_ctlr",
"cheekline_R_ctlr","cheekline_L_ctlr"
]

    for Ctrl in Ctrls:
        ctrl = TheNameSpace + Ctrl
        if objExists(ctrl)==True:
            select(ctrl,add=1)


def North_SelectLf_hand():
    getTheName=ls(sl=1)
    getTHeNum=getTheName[0].split(":")
    TheNameSpace=""
    if len(getTHeNum)>1:
        for i in range(len(getTHeNum)-1):
            TheNameSpace=TheNameSpace+getTHeNum[i]+":"
    if len(getTHeNum)==1:
        TheNameSpace=""
    questADD=checkBox("North_ADD",q=1,v=1)
    if questADD==0:
        select(cl=1)

    Ctrls = ["Lf_thumb1","Lf_thumb2","Lf_thumb3","Lf_index1","Lf_index2","Lf_index3","Lf_mid1","Lf_mid2","Lf_mid3",
"Lf_ring1","Lf_ring2","Lf_ring3","Lf_pinky1","Lf_pinky2","Lf_pinky3",
"l_thumb_finger_control",
"l_index_finger_control",
"l_mid_finger_control",
"l_ring_finger_control",
"l_pinkie_finger_control",
"l_hand_control"]    

    for Ctrl in Ctrls:
        ctrl = TheNameSpace + Ctrl
        if objExists(ctrl)==True:
            select(ctrl,add=1)      

def North_SelectLf_Arm():
    getTheName=ls(sl=1)
    getTHeNum=getTheName[0].split(":")
    TheNameSpace=""
    if len(getTHeNum)>1:
        for i in range(len(getTHeNum)-1):
            TheNameSpace=TheNameSpace+getTHeNum[i]+":"
    if len(getTHeNum)==1:
        TheNameSpace=""
    questADD=checkBox("North_ADD",q=1,v=1)
    if questADD==0:
        select(cl=1)

    Ctrls = ["Lf_shoulder","LfArm_UpArm_FK","LfArm_Elbow_FK","LfArm_Wrist_FK","LfArm_Pole_ctrl","LfArm_Wrist_IK",
"FKCurveWrist_L","MSC_ElbowDisplacer_Start_L","FKCurveElbow_L","FKCurveElbowDisplacer_L",
"MSC_ShoulderDisplacer_Start_L",
"FKCurveShoulder_L",
"FKCurveScapula_L",
"FKIK_Switch_Arm_L",
"IKPoleVectorCurveArm_L",
"IKCurveArm_L"]    

    for Ctrl in Ctrls:
        ctrl = TheNameSpace + Ctrl
        if objExists(ctrl)==True:
            select(ctrl,add=1)     

def North_SelectLf_ArmALL():
    getTheName=ls(sl=1)
    getTHeNum=getTheName[0].split(":")
    TheNameSpace=""
    if len(getTHeNum)>1:
        for i in range(len(getTHeNum)-1):
            TheNameSpace=TheNameSpace+getTHeNum[i]+":"
    if len(getTHeNum)==1:
        TheNameSpace=""
    questADD=checkBox("North_ADD",q=1,v=1)
    if questADD==0:
        select(cl=1)
    Ctrls = ["Lf_thumb1","Lf_thumb2","Lf_thumb3","Lf_index1","Lf_index2","Lf_index3","Lf_mid1","Lf_mid2","Lf_mid3",
"Lf_ring1","Lf_ring2","Lf_ring3","Lf_pinky1","Lf_pinky2","Lf_pinky3",
"l_thumb_finger_control",
"l_index_finger_control",
"l_mid_finger_control",
"l_ring_finger_control",
"l_pinkie_finger_control",
"l_hand_control",
"Lf_shoulder","LfArm_UpArm_FK","LfArm_Elbow_FK","LfArm_Wrist_FK","LfArm_Pole_ctrl","LfArm_Wrist_IK",
"FKCurveWrist_L","MSC_ElbowDisplacer_Start_L","FKCurveElbow_L","FKCurveElbowDisplacer_L",
"MSC_ShoulderDisplacer_Start_L",
"FKCurveShoulder_L",
"FKCurveScapula_L",
"FKIK_Switch_Arm_L",
"IKPoleVectorCurveArm_L",
"IKCurveArm_L"]    

    for Ctrl in Ctrls:
        ctrl = TheNameSpace + Ctrl
        if objExists(ctrl)==True:
            select(ctrl,add=1)  

def North_SelectRt_hand():
    getTheName=ls(sl=1)
    getTHeNum=getTheName[0].split(":")
    TheNameSpace=""
    if len(getTHeNum)>1:
        for i in range(len(getTHeNum)-1):
            TheNameSpace=TheNameSpace+getTHeNum[i]+":"
    if len(getTHeNum)==1:
        TheNameSpace=""
    questADD=checkBox("North_ADD",q=1,v=1)
    if questADD==0:
        select(cl=1)

    Ctrls = ["Rt_thumb1","Rt_thumb2","Rt_thumb3","Rt_index1","Rt_index2","Rt_index3","Rt_mid1","Rt_mid2","Rt_mid3",
"Rt_ring1","Rt_ring2","Rt_ring3","Rt_pinky1","Rt_pinky2","Rt_pinky3",
"r_thumb_finger_control",
"r_index_finger_control",
"r_mid_finger_control",
"r_ring_finger_control",
"r_pinkie_finger_control",
"r_hand_control"]    

    for Ctrl in Ctrls:
        ctrl = TheNameSpace + Ctrl
        if objExists(ctrl)==True:
            select(ctrl,add=1)       
    
def North_SelectRt_Arm():
    getTheName=ls(sl=1)
    getTHeNum=getTheName[0].split(":")
    TheNameSpace=""
    if len(getTHeNum)>1:
        for i in range(len(getTHeNum)-1):
            TheNameSpace=TheNameSpace+getTHeNum[i]+":"
    if len(getTHeNum)==1:
        TheNameSpace=""
    questADD=checkBox("North_ADD",q=1,v=1)
    if questADD==0:
        select(cl=1)

    Ctrls = ["Rt_shoulder","RtArm_UpArm_FK","RtArm_Elbow_FK","RtArm_Wrist_FK","RtArm_Pole_ctrl","RtArm_Wrist_IK",
"FKCurveWrist_R","MSC_ElbowDisplacer_Start_R","FKCurveElbow_R","FKCurveElbowDisplacer_R",
"MSC_ShoulderDisplacer_Start_R",
"FKCurveShoulder_R",
"FKCurveScapula_R",
"FKIK_Switch_Arm_R",
"IKPoleVectorCurveArm_R",
"IKCurveArm_R"]    

    for Ctrl in Ctrls:
        ctrl = TheNameSpace + Ctrl
        if objExists(ctrl)==True:
            select(ctrl,add=1)     

def North_SelectRt_ArmALL():
    getTheName=ls(sl=1)
    getTHeNum=getTheName[0].split(":")
    TheNameSpace=""
    if len(getTHeNum)>1:
        for i in range(len(getTHeNum)-1):
            TheNameSpace=TheNameSpace+getTHeNum[i]+":"
    if len(getTHeNum)==1:
        TheNameSpace=""
    questADD=checkBox("North_ADD",q=1,v=1)
    if questADD==0:
        select(cl=1)
    Ctrls = ["Rt_thumb1","Rt_thumb2","Rt_thumb3","Rt_index1","Rt_index2","Rt_index3","Rt_mid1","Rt_mid2","Rt_mid3",
"Rt_ring1","Rt_ring2","Rt_ring3","Rt_pinky1","Rt_pinky2","Rt_pinky3",
"r_thumb_finger_control",
"r_index_finger_control",
"r_mid_finger_control",
"r_ring_finger_control",
"r_pinkie_finger_control",
"r_hand_control",
"Rt_shoulder","RtArm_UpArm_FK","RtArm_Elbow_FK","RtArm_Wrist_FK","RtArm_Pole_ctrl","RtArm_Wrist_IK",
"FKCurveWrist_R","MSC_ElbowDisplacer_Start_R","FKCurveElbow_R","FKCurveElbowDisplacer_R",
"MSC_ShoulderDisplacer_Start_R",
"FKCurveShoulder_R",
"FKCurveScapula_R",
"FKIK_Switch_Arm_R",
"IKPoleVectorCurveArm_R",
"IKCurveArm_R"]    

    for Ctrl in Ctrls:
        ctrl = TheNameSpace + Ctrl
        if objExists(ctrl)==True:
            select(ctrl,add=1)  
            
def HbSelectLf_Toes():
    getTheName=ls(sl=1)
    getTHeNum=getTheName[0].split(":")
    TheNameSpace=""
    if len(getTHeNum)>1:
        for i in range(len(getTHeNum)-1):
            TheNameSpace=TheNameSpace+getTHeNum[i]+":"
    if len(getTHeNum)==1:
        TheNameSpace=""
    questADD=checkBox("North_ADD",q=1,v=1)
    if questADD==0:
        select(cl=1)
    try:
        select(TheNameSpace+"Lf_Toe_thumb1",add=1)
        select(TheNameSpace+"Lf_Toe_thumb2",add=1)
        select(TheNameSpace+"Lf_Toe_thumb3",add=1)
        select(TheNameSpace+"Lf_Toe_index1",add=1)
        select(TheNameSpace+"Lf_Toe_index2",add=1)
        select(TheNameSpace+"Lf_Toe_index3",add=1)
        select(TheNameSpace+"Lf_Toe_mid1",add=1)
        select(TheNameSpace+"Lf_Toe_mid2",add=1)
        select(TheNameSpace+"Lf_Toe_mid3",add=1)
        select(TheNameSpace+"Lf_Toe_ring1",add=1)
        select(TheNameSpace+"Lf_Toe_ring2",add=1)
        select(TheNameSpace+"Lf_Toe_ring3",add=1)
        select(TheNameSpace+"Lf_Toe_pinky1",add=1)
        select(TheNameSpace+"Lf_Toe_pinky2",add=1)
        select(TheNameSpace+"Lf_Toe_pinky3",add=1)
        select(TheNameSpace+"LfLeg_Switch",add=1)

    except:
        pass

def North_SelectLf_Leg():
    getTheName=ls(sl=1)
    getTHeNum=getTheName[0].split(":")
    TheNameSpace=""
    if len(getTHeNum)>1:
        for i in range(len(getTHeNum)-1):
            TheNameSpace=TheNameSpace+getTHeNum[i]+":"
    if len(getTHeNum)==1:
        TheNameSpace=""
    questADD=checkBox("North_ADD",q=1,v=1)
    if questADD==0:
        select(cl=1)

    Ctrls = ["Lf_hip_ctrl","LfLeg_Leg_FK","LfLeg_Knee_FK","LfLeg_Ankle_FK","LfLeg_Pole_ctrl","LfLeg_Leg_IK","l_leg_ctrl","l_leg7_ctrl",
"IKCurveLeg_L","FKCurveMiddleToe1_L","FKIK_Switch_Leg_L","IKPoleVectorCurveLeg_L",
"MSC_KneeDisplacer_Start_L",
"FKCurveKneeDisplacer_L",
"MSC_HipDisplacer_Start_L",
"FKCurveAnkle_L",
"FKCurveKnee_L",
"FKCurveHip_L",
"l_leg_index_finger_control","l_leg_mid_finger_control","l_leg_ring_finger_control","l_leg_pinkie_finger_control","l_leg_control"
]    

    for Ctrl in Ctrls:
        ctrl = TheNameSpace + Ctrl
        if objExists(ctrl)==True:
            select(ctrl,add=1)     



def HbSelectRt_Toes():
    getTheName=ls(sl=1)
    getTHeNum=getTheName[0].split(":")
    TheNameSpace=""
    if len(getTHeNum)>1:
        for i in range(len(getTHeNum)-1):
            TheNameSpace=TheNameSpace+getTHeNum[i]+":"
    if len(getTHeNum)==1:
        TheNameSpace=""
    questADD=checkBox("North_ADD",q=1,v=1)
    if questADD==0:
        select(cl=1)
    try:
        select(TheNameSpace+"Rt_Toe_thumb1",add=1)
        select(TheNameSpace+"Rt_Toe_thumb2",add=1)
        select(TheNameSpace+"Rt_Toe_thumb3",add=1)
        select(TheNameSpace+"Rt_Toe_index1",add=1)
        select(TheNameSpace+"Rt_Toe_index2",add=1)
        select(TheNameSpace+"Rt_Toe_index3",add=1)
        select(TheNameSpace+"Rt_Toe_mid1",add=1)
        select(TheNameSpace+"Rt_Toe_mid2",add=1)
        select(TheNameSpace+"Rt_Toe_mid3",add=1)
        select(TheNameSpace+"Rt_Toe_ring1",add=1)
        select(TheNameSpace+"Rt_Toe_ring2",add=1)
        select(TheNameSpace+"Rt_Toe_ring3",add=1)
        select(TheNameSpace+"Rt_Toe_pinky1",add=1)
        select(TheNameSpace+"Rt_Toe_pinky2",add=1)
        select(TheNameSpace+"Rt_Toe_pinky3",add=1)
        select(TheNameSpace+"RtLeg_Switch",add=1)

    except:
        pass

def North_SelectRt_Leg():
    getTheName=ls(sl=1)
    getTHeNum=getTheName[0].split(":")
    TheNameSpace=""
    if len(getTHeNum)>1:
        for i in range(len(getTHeNum)-1):
            TheNameSpace=TheNameSpace+getTHeNum[i]+":"
    if len(getTHeNum)==1:
        TheNameSpace=""
    questADD=checkBox("North_ADD",q=1,v=1)
    if questADD==0:
        select(cl=1)

    Ctrls = ["Rt_hip_ctrl","RtLeg_Leg_FK","RtLeg_Knee_FK","RtLeg_Ankle_FK","RtLeg_Pole_ctrl","RtLeg_Leg_IK","r_leg_ctrl","r_leg7_ctrl",
"IKCurveLeg_R","FKCurveMiddleToe1_R","FKIK_Switch_Leg_R","IKPoleVectorCurveLeg_R",
"MSC_KneeDisplacer_Start_R",
"FKCurveKneeDisplacer_R",
"MSC_HipDisplacer_Start_R",
"FKCurveAnkle_R",
"FKCurveKnee_R",
"FKCurveHip_R",
"r_leg_index_finger_control","r_leg_mid_finger_control","r_leg_ring_finger_control","r_leg_pinkie_finger_control","r_leg_control"
]    

    for Ctrl in Ctrls:
        ctrl = TheNameSpace + Ctrl
        if objExists(ctrl)==True:
            select(ctrl,add=1)  


def North_SelectALL_Body():
    getTheName=ls(sl=1)
    getTHeNum=getTheName[0].split(":")
    TheNameSpace=""
    if len(getTHeNum)>1:
        for i in range(len(getTHeNum)-1):
            TheNameSpace=TheNameSpace+getTHeNum[i]+":"
    if len(getTHeNum)==1:
        TheNameSpace=""
    questADD=checkBox("North_ADD",q=1,v=1)
    if questADD==0:
        select(cl=1)

    Ctrls = ["Lf_thumb1","Lf_thumb2","Lf_thumb3","Lf_index1","Lf_index2","Lf_index3","Lf_mid1","Lf_mid2","Lf_mid3",
"Lf_ring1","Lf_ring2","Lf_ring3","Lf_pinky1","Lf_pinky2","Lf_pinky3",
"l_thumb_finger_control",
"l_index_finger_control",
"l_mid_finger_control",
"l_ring_finger_control",
"l_pinkie_finger_control",
"l_hand_control",
"Lf_shoulder","LfArm_UpArm_FK","LfArm_Elbow_FK","LfArm_Wrist_FK","LfArm_Pole_ctrl","LfArm_Wrist_IK",
"FKCurveWrist_L","MSC_ElbowDisplacer_Start_L","FKCurveElbow_L","FKCurveElbowDisplacer_L",
"MSC_ShoulderDisplacer_Start_L",
"FKCurveShoulder_L",
"FKCurveScapula_L",
"FKIK_Switch_Arm_L",
"IKPoleVectorCurveArm_L",
"IKCurveArm_L",
"Rt_thumb1","Rt_thumb2","Rt_thumb3","Rt_index1","Rt_index2","Rt_index3","Rt_mid1","Rt_mid2","Rt_mid3",
"Rt_ring1","Rt_ring2","Rt_ring3","Rt_pinky1","Rt_pinky2","Rt_pinky3",
"r_thumb_finger_control",
"r_index_finger_control",
"r_mid_finger_control",
"r_ring_finger_control",
"r_pinkie_finger_control",
"r_hand_control",
"Rt_shoulder","RtArm_UpArm_FK","RtArm_Elbow_FK","RtArm_Wrist_FK","RtArm_Pole_ctrl","RtArm_Wrist_IK",
"FKCurveWrist_R","MSC_ElbowDisplacer_Start_R","FKCurveElbow_R","FKCurveElbowDisplacer_R",
"MSC_ShoulderDisplacer_Start_R",
"FKCurveShoulder_R",
"FKCurveScapula_R",
"FKIK_Switch_Arm_R",
"IKPoleVectorCurveArm_R",
"IKCurveArm_R",
"Lf_hip_ctrl","LfLeg_Leg_FK","LfLeg_Knee_FK","LfLeg_Ankle_FK","LfLeg_Pole_ctrl","LfLeg_Leg_IK","l_leg_ctrl","l_leg7_ctrl",
"IKCurveLeg_L","FKCurveMiddleToe1_L","FKIK_Switch_Leg_L","IKPoleVectorCurveLeg_L",
"MSC_KneeDisplacer_Start_L",
"FKCurveKneeDisplacer_L",
"MSC_HipDisplacer_Start_L",
"FKCurveAnkle_L",
"FKCurveKnee_L",
"FKCurveHip_L",
"Rt_hip_ctrl","RtLeg_Leg_FK","RtLeg_Knee_FK","RtLeg_Ankle_FK","RtLeg_Pole_ctrl","RtLeg_Leg_IK","r_leg_ctrl","r_leg7_ctrl",
"IKCurveLeg_R","FKCurveMiddleToe1_R","FKIK_Switch_Leg_R","IKPoleVectorCurveLeg_R",
"MSC_KneeDisplacer_Start_R",
"FKCurveKneeDisplacer_R",
"MSC_HipDisplacer_Start_R",
"FKCurveAnkle_R",
"FKCurveKnee_R",
"FKCurveHip_R",
"RootCurveRoot_M","IKCurveSpine0_M","belly_cloth_jnt_base_ctlr","IKCurveSpine2_M","IKCurveSpine_mid_M","IKCurveSpine5_M",
"FKCurveExtraHead_M","IKCurveSpineNeck0_M","IKCurveSpineNeck2_M","IKCurveSpineNeck5_M",
"l_leg_index_finger_control","l_leg_mid_finger_control","l_leg_ring_finger_control","l_leg_pinkie_finger_control","l_leg_control",
"r_leg_index_finger_control","r_leg_mid_finger_control","r_leg_ring_finger_control","r_leg_pinkie_finger_control","r_leg_control",
"FKCurveleg_aim_L","FKCurveleg_aim_R","L_hip_Flt_end_ctlr","R_hip_Flt_end_ctlr",
"FKCurveTail_03_M","FKCurveTail_04_M","FKCurveTail_05_M","FKCurveTail_Base_M",
"Tummay_flt_end_ctlr","chest_flt_end_ctlr"
]    

    for Ctrl in Ctrls:
        ctrl = TheNameSpace + Ctrl
        if objExists(ctrl)==True:
            select(ctrl,add=1) 


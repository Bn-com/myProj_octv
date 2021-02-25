from maya.cmds import*
import maya.mel as mm
def HbSelectFaceCtrl():
    
    winName = "ZWDFaceCtrl"
    if window(winName, q = True, ex = True):
        deleteUI(winName)
    window(winName, w= 280, h= 280, title = "ZWDFaceCtrlTools", rtf = True)

    form = formLayout()
    tabs = tabLayout(innerMarginWidth=5, innerMarginHeight=5)
    formLayout( form, edit=True, attachForm=((tabs, 'top', 0), (tabs, 'left', 0), (tabs, 'bottom', 0), (tabs, 'right', 0)) )
    
    #---------------------------- easyAnimCurve IO -------------------------#
    child = columnLayout(adj = True)
    separator(h = 10)
    text(l = "")
    button(l = "select EyeBrow",c = "HbSelectEyeBrow()")
    button(l = "Select EyeLid", c = "HbSelectEyeLid()")
    button(l = "Select EyeBall", c = "HbSelectEyeBall()")
    separator(h = 10)
    button(l = "Select Nose", c = "HbSelectNose()")
    separator(h = 10)
    button(l = "Select Teeth", c = "HbSelectTeeth()")
    button(l = "Select Tongue", c = "HbSelectTongue()")
    button(l = "Select Mouth", c = "HbSelectMouth()")
    button(l = "Select MouthLip", c = "HbSelectMouthLip()")
    button(l = "Select A_U_O_FV_the_eee_Mbp...", c = "HbSelectA_U_O_FV_the_eee_Mbp()")
    button(l = "Select -----MouthALL-----", c = "HbSelectMouthALL()")
    separator(h = 10)
    separator(h = 10)
    button(l = "-----Select ALL-----", c = "HbSelectAll()")
    separator(h = 10)
    separator(h = 10)

    checkBox( "HbADD",label='ADD' )



    text(l = " ")
    text(l = " ")
    text(l = " ")

    
    text(l = "CJW")

    text(l = "-----------------------")
    text(l = "GDC-IDMT 2013 (C)\n")
    setParent( '..' )
    
    tabLayout( tabs, edit=True, tabLabel=((child,"FacialRIG")))

    

    child = columnLayout(adj = True)
    separator(h = 10)
    text(l = "")
    button(l = "select Lf_hand",c = "HbSelectLf_hand()")
    button(l = "Select Lf_Arm", c = "HbSelectLf_Arm()")
    separator(h = 10)
    button(l = "Select Rt_hand", c = "HbSelectRt_hand()")
    button(l = "Select Rt_Arm", c = "HbSelectRt_Arm()")
    separator(h = 10)
    button(l = "Select Lf_Toes", c = "HbSelectLf_Toes()")
    button(l = "Select Lf_Leg", c = "HbSelectLf_Leg()")
    separator(h = 10)
    button(l = "Select Rt_Toes", c = "HbSelectRt_Toes()")
    button(l = "Select Rt_Leg", c = "HbSelectRt_Leg()")
    separator(h = 10)
    separator(h = 10)

    button(l = "Select Hair", c = "HbSelectHair()")
    separator(h = 10)
    separator(h = 10)

    checkBox( "HbADD",label='ADD' )



    text(l = " ")
    text(l = " ")
    text(l = " ")

    
    text(l = "CJW")

    text(l = "-----------------------")
    text(l = "GDC-IDMT 2013 (C)\n")
    setParent( '..' )
    
    tabLayout( tabs, edit=True, tabLabel=((child,"BodyRIG")))


    showWindow(winName)

HbSelectFaceCtrl()
def HbSelectEyeBrow():
	getTheName=ls(sl=1)
	getTHeNum=getTheName[0].split(":")
	TheNameSpace=""
	if len(getTHeNum)>1:
		for i in range(len(getTHeNum)-1):
			TheNameSpace=TheNameSpace+getTHeNum[i]+":"
	if len(getTHeNum)==1:
		TheNameSpace=""
	questADD=checkBox("HbADD",q=1,v=1)
	if questADD==0:
		select(cl=1)
	try:
		select(TheNameSpace+"c_Lf_eyebrows_CTRL",add=1)
		select(TheNameSpace+"c_Rt_eyebrows_CTRL",add=1)


	except:
		pass

def HbSelectEyeLid():
	getTheName=ls(sl=1)
	getTHeNum=getTheName[0].split(":")
	TheNameSpace=""
	if len(getTHeNum)>1:
		for i in range(len(getTHeNum)-1):
			TheNameSpace=TheNameSpace+getTHeNum[i]+":"
	if len(getTHeNum)==1:
		TheNameSpace=""
	questADD=checkBox("HbADD",q=1,v=1)
	if questADD==0:
		select(cl=1)
	try:
		select(TheNameSpace+"c_Rt_up_eyelids_CTRL",TheNameSpace+"c_Rt_dn_eyelids_CTRL",TheNameSpace+"Rt_blink_CTRL",add=1)
		select(TheNameSpace+"c_Lf_up_eyelids_CTRL",TheNameSpace+"c_Lf_dn_eyelids_CTRL",TheNameSpace+"Lf_blink_CTRL",add=1)
	except:
		pass



def HbSelectEyeBall():
	getTheName=ls(sl=1)
	getTHeNum=getTheName[0].split(":")
	TheNameSpace=""
	if len(getTHeNum)>1:
		for i in range(len(getTHeNum)-1):
			TheNameSpace=TheNameSpace+getTHeNum[i]+":"
	if len(getTHeNum)==1:
		TheNameSpace=""
	questADD=checkBox("HbADD",q=1,v=1)
	if questADD==0:
		select(cl=1)
	try:
		select(TheNameSpace+"c_eye_M",add=1)
		select(TheNameSpace+"c_Lf_eye_M",add=1)
		select(TheNameSpace+"c_Lf_spec_M",add=1)
		select(TheNameSpace+"c_Rt_eye_M",add=1)
		select(TheNameSpace+"c_Rt_spec_M",add=1)
	except:
		pass





def HbSelectNose():
	getTheName=ls(sl=1)
	getTHeNum=getTheName[0].split(":")
	TheNameSpace=""
	if len(getTHeNum)>1:
		for i in range(len(getTHeNum)-1):
			TheNameSpace=TheNameSpace+getTHeNum[i]+":"
	if len(getTHeNum)==1:
		TheNameSpace=""
	questADD=checkBox("HbADD",q=1,v=1)
	if questADD==0:
		select(cl=1)
	try:
		select(TheNameSpace+"c_jaw_up_CTRL",add=1)
	except:
		pass


def HbSelectTeeth():
	getTheName=ls(sl=1)
	getTHeNum=getTheName[0].split(":")
	TheNameSpace=""
	if len(getTHeNum)>1:
		for i in range(len(getTHeNum)-1):
			TheNameSpace=TheNameSpace+getTHeNum[i]+":"
	if len(getTHeNum)==1:
		TheNameSpace=""
	questADD=checkBox("HbADD",q=1,v=1)
	if questADD==0:
		select(cl=1)
	try:
		select(TheNameSpace+"upTeeth_ctrl",add=1)
		select(TheNameSpace+"upTeeth001_ctrl",add=1)
		select(TheNameSpace+"upTeeth002_ctrl",add=1)
		select(TheNameSpace+"upTeeth003_ctrl",add=1)
		select(TheNameSpace+"topteeth_Ctrl",add=1)

	except:
		pass

	try:
		select(TheNameSpace+"lowTeeth_ctrl",add=1)
		select(TheNameSpace+"lowTeeth001_ctrl",add=1)
		select(TheNameSpace+"lowTeeth002_ctrl",add=1)
		select(TheNameSpace+"lowTeeth003_ctrl",add=1)
		select(TheNameSpace+"dowteeth_Ctrl",add=1)

	except:
		pass



def HbSelectTongue():
	getTheName=ls(sl=1)
	getTHeNum=getTheName[0].split(":")
	TheNameSpace=""
	if len(getTHeNum)>1:
		for i in range(len(getTHeNum)-1):
			TheNameSpace=TheNameSpace+getTHeNum[i]+":"
	if len(getTHeNum)==1:
		TheNameSpace=""
	questADD=checkBox("HbADD",q=1,v=1)
	if questADD==0:
		select(cl=1)
	try:
		select(TheNameSpace+"c_tongue_CTRL",add=1)
		select(TheNameSpace+"c_tongue_joint1",add=1)
		select(TheNameSpace+"c_tongue_joint2",add=1)
		select(TheNameSpace+"c_tongue_joint3",add=1)
		select(TheNameSpace+"c_tongue_joint4",add=1)
		select(TheNameSpace+"c_tongue_joint5",add=1)
		select(TheNameSpace+"c_tongue_joint6",add=1)
		select(TheNameSpace+"c_tongue_joint7",add=1)
		select(TheNameSpace+"c_tongue_joint8",add=1)
		select(TheNameSpace+"c_tongue_joint9",add=1)

	except:
		pass



def HbSelectMouth():
	getTheName=ls(sl=1)
	getTHeNum=getTheName[0].split(":")
	TheNameSpace=""
	if len(getTHeNum)>1:
		for i in range(len(getTHeNum)-1):
			TheNameSpace=TheNameSpace+getTHeNum[i]+":"
	if len(getTHeNum)==1:
		TheNameSpace=""
	questADD=checkBox("HbADD",q=1,v=1)
	if questADD==0:
		select(cl=1)
	try:
		select(TheNameSpace+"c_jaw_dn_CTRL",add=1)
		select(TheNameSpace+"c_Rt_mouthLip_CTRL",add=1)
		select(TheNameSpace+"c_Lf_mouthLip_CTRL",add=1)
		select(TheNameSpace+"mouth_CTRL",add=1)
		select(TheNameSpace+"c_Rt_cheek_CTRL",add=1)
		select(TheNameSpace+"c_Lf_cheek_CTRL",add=1)
		select(TheNameSpace+"c_jaw_dn_translateZ_CTRL",add=1)
		
	except:
		pass


def HbSelectMouthLip():
	getTheName=ls(sl=1)
	getTHeNum=getTheName[0].split(":")
	TheNameSpace=""
	if len(getTHeNum)>1:
		for i in range(len(getTHeNum)-1):
			TheNameSpace=TheNameSpace+getTHeNum[i]+":"
	if len(getTHeNum)==1:
		TheNameSpace=""
	questADD=checkBox("HbADD",q=1,v=1)
	if questADD==0:
		select(cl=1)
	try:
		select(TheNameSpace+"c_Rt_up_mouthLip_CTRL",add=1)
		select(TheNameSpace+"c_Lf_up_mouthLip_CTRL",add=1)
		select(TheNameSpace+"c_Rt_dn_mouthLip_CTRL",add=1)
		select(TheNameSpace+"c_Lf_dn_mouthLip_CTRL",add=1)
		select(TheNameSpace+"c_Rt_up_rollLip_CTRL",add=1)
		select(TheNameSpace+"c_up_rollLip_CTRL",add=1)
		select(TheNameSpace+"c_Lf_up_rollLip_CTRL",add=1)
		select(TheNameSpace+"c_Rt_dn_rollLip_CTRL",add=1)
		select(TheNameSpace+"c_dn_rollLip_CTRL",add=1)
		select(TheNameSpace+"c_Lf_dn_rollLip_CTRL",add=1)		
	except:
		pass



def HbSelectA_U_O_FV_the_eee_Mbp():
	getTheName=ls(sl=1)
	getTHeNum=getTheName[0].split(":")
	TheNameSpace=""
	if len(getTHeNum)>1:
		for i in range(len(getTHeNum)-1):
			TheNameSpace=TheNameSpace+getTHeNum[i]+":"
	if len(getTHeNum)==1:
		TheNameSpace=""
	questADD=checkBox("HbADD",q=1,v=1)
	if questADD==0:
		select(cl=1)
	try:
		select(TheNameSpace+"c_a_CTRL",add=1)
		select(TheNameSpace+"c_uo_CTRL",add=1)

		select(TheNameSpace+"c_fv_CTRL",add=1)
		select(TheNameSpace+"c_the_CTRL",add=1)
		select(TheNameSpace+"c_eeesz_CTRL",add=1)

		select(TheNameSpace+"c_mbp_CTRL",add=1)


	except:
		pass

	try:

		select(TheNameSpace+"c_OU_CTRL",add=1)

	except:
		pass
	try:

		select(TheNameSpace+"c_SHH_CTRL",add=1)

	except:
		pass

	try:

		select(TheNameSpace+"c_kiss_CTRL",add=1)

	except:
		pass




def HbSelectMouthALL():
	getTheName=ls(sl=1)
	getTHeNum=getTheName[0].split(":")
	TheNameSpace=""
	if len(getTHeNum)>1:
		for i in range(len(getTHeNum)-1):
			TheNameSpace=TheNameSpace+getTHeNum[i]+":"
	if len(getTHeNum)==1:
		TheNameSpace=""
	questADD=checkBox("HbADD",q=1,v=1)
	if questADD==0:
		select(cl=1)
	try:
		select(TheNameSpace+"upTeeth_ctrl",add=1)
		select(TheNameSpace+"upTeeth001_ctrl",add=1)
		select(TheNameSpace+"upTeeth002_ctrl",add=1)
		select(TheNameSpace+"upTeeth003_ctrl",add=1)

		select(TheNameSpace+"lowTeeth_ctrl",add=1)
		select(TheNameSpace+"lowTeeth001_ctrl",add=1)
		select(TheNameSpace+"lowTeeth002_ctrl",add=1)
		select(TheNameSpace+"lowTeeth003_ctrl",add=1)


		select(TheNameSpace+"c_tongue_CTRL",add=1)
		select(TheNameSpace+"c_tongue_joint1",add=1)
		select(TheNameSpace+"c_tongue_joint2",add=1)
		select(TheNameSpace+"c_tongue_joint3",add=1)
		select(TheNameSpace+"c_tongue_joint4",add=1)
		select(TheNameSpace+"c_tongue_joint5",add=1)
		select(TheNameSpace+"c_tongue_joint6",add=1)
		select(TheNameSpace+"c_tongue_joint7",add=1)
		select(TheNameSpace+"c_tongue_joint8",add=1)
		select(TheNameSpace+"c_tongue_joint9",add=1)

		select(TheNameSpace+"c_jaw_dn_CTRL",add=1)
		select(TheNameSpace+"c_Rt_mouthLip_CTRL",add=1)
		select(TheNameSpace+"c_Lf_mouthLip_CTRL",add=1)
		select(TheNameSpace+"mouth_CTRL",add=1)
		select(TheNameSpace+"c_Rt_cheek_CTRL",add=1)
		select(TheNameSpace+"c_Lf_cheek_CTRL",add=1)
		select(TheNameSpace+"c_jaw_dn_translateZ_CTRL",add=1)

		select(TheNameSpace+"c_Rt_up_mouthLip_CTRL",add=1)
		select(TheNameSpace+"c_Lf_up_mouthLip_CTRL",add=1)
		select(TheNameSpace+"c_Rt_dn_mouthLip_CTRL",add=1)
		select(TheNameSpace+"c_Lf_dn_mouthLip_CTRL",add=1)
		select(TheNameSpace+"c_Rt_up_rollLip_CTRL",add=1)
		select(TheNameSpace+"c_up_rollLip_CTRL",add=1)
		select(TheNameSpace+"c_Lf_up_rollLip_CTRL",add=1)
		select(TheNameSpace+"c_Rt_dn_rollLip_CTRL",add=1)
		select(TheNameSpace+"c_dn_rollLip_CTRL",add=1)
		select(TheNameSpace+"c_Lf_dn_rollLip_CTRL",add=1)

		select(TheNameSpace+"c_a_CTRL",add=1)
		select(TheNameSpace+"c_uo_CTRL",add=1)

		select(TheNameSpace+"c_fv_CTRL",add=1)
		select(TheNameSpace+"c_the_CTRL",add=1)
		select(TheNameSpace+"c_eeesz_CTRL",add=1)

		select(TheNameSpace+"c_mbp_CTRL",add=1)
		
	except:
		pass

	try:

		select(TheNameSpace+"c_OU_CTRL",add=1)

	except:
		pass
	try:

		select(TheNameSpace+"c_SHH_CTRL",add=1)

	except:
		pass

	try:

		select(TheNameSpace+"c_kiss_CTRL",add=1)

	except:
		pass










def HbSelectAll():
	getTheName=ls(sl=1)
	getTHeNum=getTheName[0].split(":")
	TheNameSpace=""
	if len(getTHeNum)>1:
		for i in range(len(getTHeNum)-1):
			TheNameSpace=TheNameSpace+getTHeNum[i]+":"
	if len(getTHeNum)==1:
		TheNameSpace=""
	questADD=checkBox("HbADD",q=1,v=1)
	if questADD==0:
		select(cl=1)
	try:

		select(TheNameSpace+"c_Lf_eyebrows_CTRL",add=1)
		select(TheNameSpace+"c_Rt_eyebrows_CTRL",add=1)

		select(TheNameSpace+"c_Rt_up_eyelids_CTRL",TheNameSpace+"c_Rt_dn_eyelids_CTRL",TheNameSpace+"Rt_blink_CTRL",add=1)
		select(TheNameSpace+"c_Lf_up_eyelids_CTRL",TheNameSpace+"c_Lf_dn_eyelids_CTRL",TheNameSpace+"Lf_blink_CTRL",add=1)

		select(TheNameSpace+"c_eye_M",add=1)
		select(TheNameSpace+"c_Lf_eye_M",add=1)
		select(TheNameSpace+"c_Lf_spec_M",add=1)
		select(TheNameSpace+"c_Rt_eye_M",add=1)
		select(TheNameSpace+"c_Rt_spec_M",add=1)

		select(TheNameSpace+"c_jaw_up_CTRL",add=1)



		select(TheNameSpace+"upTeeth_ctrl",add=1)
		select(TheNameSpace+"upTeeth001_ctrl",add=1)
		select(TheNameSpace+"upTeeth002_ctrl",add=1)
		select(TheNameSpace+"upTeeth003_ctrl",add=1)

		select(TheNameSpace+"lowTeeth_ctrl",add=1)
		select(TheNameSpace+"lowTeeth001_ctrl",add=1)
		select(TheNameSpace+"lowTeeth002_ctrl",add=1)
		select(TheNameSpace+"lowTeeth003_ctrl",add=1)


		select(TheNameSpace+"c_tongue_CTRL",add=1)
		select(TheNameSpace+"c_tongue_joint1",add=1)
		select(TheNameSpace+"c_tongue_joint2",add=1)
		select(TheNameSpace+"c_tongue_joint3",add=1)
		select(TheNameSpace+"c_tongue_joint4",add=1)
		select(TheNameSpace+"c_tongue_joint5",add=1)
		select(TheNameSpace+"c_tongue_joint6",add=1)
		select(TheNameSpace+"c_tongue_joint7",add=1)
		select(TheNameSpace+"c_tongue_joint8",add=1)
		select(TheNameSpace+"c_tongue_joint9",add=1)

		select(TheNameSpace+"c_jaw_dn_CTRL",add=1)
		select(TheNameSpace+"c_Rt_mouthLip_CTRL",add=1)
		select(TheNameSpace+"c_Lf_mouthLip_CTRL",add=1)
		select(TheNameSpace+"mouth_CTRL",add=1)
		select(TheNameSpace+"c_Rt_cheek_CTRL",add=1)
		select(TheNameSpace+"c_Lf_cheek_CTRL",add=1)
		select(TheNameSpace+"c_jaw_dn_translateZ_CTRL",add=1)

		select(TheNameSpace+"c_Rt_up_mouthLip_CTRL",add=1)
		select(TheNameSpace+"c_Lf_up_mouthLip_CTRL",add=1)
		select(TheNameSpace+"c_Rt_dn_mouthLip_CTRL",add=1)
		select(TheNameSpace+"c_Lf_dn_mouthLip_CTRL",add=1)
		select(TheNameSpace+"c_Rt_up_rollLip_CTRL",add=1)
		select(TheNameSpace+"c_up_rollLip_CTRL",add=1)
		select(TheNameSpace+"c_Lf_up_rollLip_CTRL",add=1)
		select(TheNameSpace+"c_Rt_dn_rollLip_CTRL",add=1)
		select(TheNameSpace+"c_dn_rollLip_CTRL",add=1)
		select(TheNameSpace+"c_Lf_dn_rollLip_CTRL",add=1)

		select(TheNameSpace+"c_a_CTRL",add=1)
		select(TheNameSpace+"c_uo_CTRL",add=1)

		select(TheNameSpace+"c_fv_CTRL",add=1)
		select(TheNameSpace+"c_the_CTRL",add=1)
		select(TheNameSpace+"c_eeesz_CTRL",add=1)

		select(TheNameSpace+"c_mbp_CTRL",add=1)
		
	except:
		pass

	try:

		select(TheNameSpace+"c_OU_CTRL",add=1)

	except:
		pass
	try:

		select(TheNameSpace+"c_SHH_CTRL",add=1)

	except:
		pass

	try:

		select(TheNameSpace+"c_kiss_CTRL",add=1)

	except:
		pass


def HbSelectLf_hand():
	getTheName=ls(sl=1)
	getTHeNum=getTheName[0].split(":")
	TheNameSpace=""
	if len(getTHeNum)>1:
		for i in range(len(getTHeNum)-1):
			TheNameSpace=TheNameSpace+getTHeNum[i]+":"
	if len(getTHeNum)==1:
		TheNameSpace=""
	questADD=checkBox("HbADD",q=1,v=1)
	if questADD==0:
		select(cl=1)
	try:
		select(TheNameSpace+"Lf_thumb1",add=1)
		select(TheNameSpace+"Lf_thumb2",add=1)
		select(TheNameSpace+"Lf_thumb3",add=1)
		select(TheNameSpace+"Lf_index1",add=1)
		select(TheNameSpace+"Lf_index2",add=1)
		select(TheNameSpace+"Lf_index3",add=1)
		select(TheNameSpace+"Lf_mid1",add=1)
		select(TheNameSpace+"Lf_mid2",add=1)
		select(TheNameSpace+"Lf_mid3",add=1)
		select(TheNameSpace+"Lf_ring1",add=1)
		select(TheNameSpace+"Lf_ring2",add=1)
		select(TheNameSpace+"Lf_ring3",add=1)
		select(TheNameSpace+"Lf_pinky1",add=1)
		select(TheNameSpace+"Lf_pinky2",add=1)
		select(TheNameSpace+"Lf_pinky3",add=1)


	except:
		pass

def HbSelectLf_Arm():
	getTheName=ls(sl=1)
	getTHeNum=getTheName[0].split(":")
	TheNameSpace=""
	if len(getTHeNum)>1:
		for i in range(len(getTHeNum)-1):
			TheNameSpace=TheNameSpace+getTHeNum[i]+":"
	if len(getTHeNum)==1:
		TheNameSpace=""
	questADD=checkBox("HbADD",q=1,v=1)
	if questADD==0:
		select(cl=1)
	try:
		select(TheNameSpace+"Lf_shoulder",add=1)
		select(TheNameSpace+"LfArm_UpArm_FK",add=1)
		select(TheNameSpace+"LfArm_Elbow_FK",add=1)
		select(TheNameSpace+"LfArm_Wrist_FK",add=1)
		select(TheNameSpace+"LfArm_Pole_ctrl",add=1)
		select(TheNameSpace+"LfArm_Wrist_IK",add=1)


	except:
		pass



def HbSelectRt_hand():
	getTheName=ls(sl=1)
	getTHeNum=getTheName[0].split(":")
	TheNameSpace=""
	if len(getTHeNum)>1:
		for i in range(len(getTHeNum)-1):
			TheNameSpace=TheNameSpace+getTHeNum[i]+":"
	if len(getTHeNum)==1:
		TheNameSpace=""
	questADD=checkBox("HbADD",q=1,v=1)
	if questADD==0:
		select(cl=1)
	try:
		select(TheNameSpace+"Rt_thumb1",add=1)
		select(TheNameSpace+"Rt_thumb2",add=1)
		select(TheNameSpace+"Rt_thumb3",add=1)
		select(TheNameSpace+"Rt_index1",add=1)
		select(TheNameSpace+"Rt_index2",add=1)
		select(TheNameSpace+"Rt_index3",add=1)
		select(TheNameSpace+"Rt_mid1",add=1)
		select(TheNameSpace+"Rt_mid2",add=1)
		select(TheNameSpace+"Rt_mid3",add=1)
		select(TheNameSpace+"Rt_ring1",add=1)
		select(TheNameSpace+"Rt_ring2",add=1)
		select(TheNameSpace+"Rt_ring3",add=1)
		select(TheNameSpace+"Rt_pinky1",add=1)
		select(TheNameSpace+"Rt_pinky2",add=1)
		select(TheNameSpace+"Rt_pinky3",add=1)

	except:
		pass


def HbSelectRt_Arm():
	getTheName=ls(sl=1)
	getTHeNum=getTheName[0].split(":")
	TheNameSpace=""
	if len(getTHeNum)>1:
		for i in range(len(getTHeNum)-1):
			TheNameSpace=TheNameSpace+getTHeNum[i]+":"
	if len(getTHeNum)==1:
		TheNameSpace=""
	questADD=checkBox("HbADD",q=1,v=1)
	if questADD==0:
		select(cl=1)
	try:
		select(TheNameSpace+"Rt_shoulder",add=1)
		select(TheNameSpace+"RtArm_UpArm_FK",add=1)
		select(TheNameSpace+"RtArm_Elbow_FK",add=1)
		select(TheNameSpace+"RtArm_Wrist_FK",add=1)
		select(TheNameSpace+"RtArm_Pole_ctrl",add=1)
		select(TheNameSpace+"RtArm_Wrist_IK",add=1)


	except:
		pass


def HbSelectLf_Toes():
	getTheName=ls(sl=1)
	getTHeNum=getTheName[0].split(":")
	TheNameSpace=""
	if len(getTHeNum)>1:
		for i in range(len(getTHeNum)-1):
			TheNameSpace=TheNameSpace+getTHeNum[i]+":"
	if len(getTHeNum)==1:
		TheNameSpace=""
	questADD=checkBox("HbADD",q=1,v=1)
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

def HbSelectLf_Leg():
	getTheName=ls(sl=1)
	getTHeNum=getTheName[0].split(":")
	TheNameSpace=""
	if len(getTHeNum)>1:
		for i in range(len(getTHeNum)-1):
			TheNameSpace=TheNameSpace+getTHeNum[i]+":"
	if len(getTHeNum)==1:
		TheNameSpace=""
	questADD=checkBox("HbADD",q=1,v=1)
	if questADD==0:
		select(cl=1)
	try:
		select(TheNameSpace+"Lt_hip_ctrl",add=1)
		select(TheNameSpace+"LfLeg_Leg_FK",add=1)
		select(TheNameSpace+"LfLeg_Knee_FK",add=1)
		select(TheNameSpace+"LfLeg_Ankle_FK",add=1)
		select(TheNameSpace+"LfLeg_Pole_ctrl",add=1)
		select(TheNameSpace+"LfLeg_Leg_IK",add=1)


	except:
		pass



def HbSelectRt_Toes():
	getTheName=ls(sl=1)
	getTHeNum=getTheName[0].split(":")
	TheNameSpace=""
	if len(getTHeNum)>1:
		for i in range(len(getTHeNum)-1):
			TheNameSpace=TheNameSpace+getTHeNum[i]+":"
	if len(getTHeNum)==1:
		TheNameSpace=""
	questADD=checkBox("HbADD",q=1,v=1)
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

def HbSelectRt_Leg():
	getTheName=ls(sl=1)
	getTHeNum=getTheName[0].split(":")
	TheNameSpace=""
	if len(getTHeNum)>1:
		for i in range(len(getTHeNum)-1):
			TheNameSpace=TheNameSpace+getTHeNum[i]+":"
	if len(getTHeNum)==1:
		TheNameSpace=""
	questADD=checkBox("HbADD",q=1,v=1)
	if questADD==0:
		select(cl=1)
	try:
		select(TheNameSpace+"Rt_hip_ctrl",add=1)
		select(TheNameSpace+"RtLeg_Leg_FK",add=1)
		select(TheNameSpace+"RtLeg_Knee_FK",add=1)
		select(TheNameSpace+"RtLeg_Ankle_FK",add=1)
		select(TheNameSpace+"RtLeg_Pole_ctrl",add=1)
		select(TheNameSpace+"RtLeg_Leg_IK",add=1)


	except:
		pass




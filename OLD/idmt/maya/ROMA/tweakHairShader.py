import maya.cmds as cmd
import maya.mel as mel

def tweakShader(character = 'Timo'):
	toTweak=[]
	# search pranaHair shaders into the scene
	PranaHair=cmd.ls(type='PranaHair')
	for pr in PranaHair:
		vcrtc=cmd.getAttr(pr+'.vcrtc') # vcrtc=1 is applyed only for painteffects
		grayBias=cmd.getAttr(pr+'.grayBiasEnable')
		# check if the shader is applyed on painteffects nodes
		# check if the shader has the grayBias enable
		# and eventually collect these shaders into a list
		if vcrtc == 1 and grayBias == 1:
			toTweak.append(pr)

	for twk in toTweak:
		# tweak the attributes only for the checked shaders
		cmd.setAttr(twk+'.grayBiasEnable',0)
		specular=cmd.getAttr(twk+'.specular')
		
		# reduce the original specular value of 25%
		newSpecular=specular-(specular/4)
		
		cmd.setAttr(twk+'.specular',newSpecular)

		if character == 'Timo':
			cmd.setAttr(r'%s.diffuse' % (twk), 0.7)
			cmd.setAttr(r'%s.opacityAtTip' % (twk), 0.5)
			cmd.setAttr(r'%s.opacityAtTipUpto' % (twk), 0.5)
			cmd.setAttr(r'%s.opacityAtTipPower' % (twk), 1)
			cmd.setAttr(r'%s.specular' % (twk), 0.225)
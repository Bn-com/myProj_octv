//Maya ASCII 2014 scene
//Name: HIGH_jaw_rig.ma
//Last modified: Fri, Jul 31, 2015 03:16:53 PM
//Codeset: 936
requires maya "2014";
requires -nodeType "mentalrayFramebuffer" -nodeType "mentalrayOutputPass" -nodeType "mentalrayRenderPass"
		 -nodeType "mentalrayUserBuffer" -nodeType "mentalraySubdivApprox" -nodeType "mentalrayCurveApprox"
		 -nodeType "mentalraySurfaceApprox" -nodeType "mentalrayDisplaceApprox" -nodeType "mentalrayOptions"
		 -nodeType "mentalrayGlobals" -nodeType "mentalrayItemsList" -nodeType "mentalrayShader"
		 -nodeType "mentalrayUserData" -nodeType "mentalrayText" -nodeType "mentalrayTessellation"
		 -nodeType "mentalrayPhenomenon" -nodeType "mentalrayLightProfile" -nodeType "mentalrayVertexColors"
		 -nodeType "mentalrayIblShape" -nodeType "mapVizShape" -nodeType "mentalrayCCMeshProxy"
		 -nodeType "cylindricalLightLocator" -nodeType "discLightLocator" -nodeType "rectangularLightLocator"
		 -nodeType "sphericalLightLocator" -nodeType "hotOcean" -nodeType "nr_vectorDisplace"
		 -nodeType "abcimport" -nodeType "mia_physicalsun" -nodeType "mia_physicalsky" -nodeType "mia_material"
		 -nodeType "mia_material_x" -nodeType "mia_roundcorners" -nodeType "mia_exposure_simple"
		 -nodeType "mia_portal_light" -nodeType "mia_light_surface" -nodeType "mia_exposure_photographic"
		 -nodeType "mia_exposure_photographic_rev" -nodeType "mia_lens_bokeh" -nodeType "mia_envblur"
		 -nodeType "mia_ciesky" -nodeType "mia_photometric_light" -nodeType "mib_texture_vector"
		 -nodeType "mib_texture_remap" -nodeType "mib_texture_rotate" -nodeType "mib_bump_basis"
		 -nodeType "mib_bump_map" -nodeType "mib_passthrough_bump_map" -nodeType "mib_bump_map2"
		 -nodeType "mib_lookup_spherical" -nodeType "mib_lookup_cube1" -nodeType "mib_lookup_cube6"
		 -nodeType "mib_lookup_background" -nodeType "mib_lookup_cylindrical" -nodeType "mib_texture_lookup"
		 -nodeType "mib_texture_lookup2" -nodeType "mib_texture_filter_lookup" -nodeType "mib_texture_checkerboard"
		 -nodeType "mib_texture_polkadot" -nodeType "mib_texture_polkasphere" -nodeType "mib_texture_turbulence"
		 -nodeType "mib_texture_wave" -nodeType "mib_reflect" -nodeType "mib_refract" -nodeType "mib_transparency"
		 -nodeType "mib_continue" -nodeType "mib_opacity" -nodeType "mib_twosided" -nodeType "mib_refraction_index"
		 -nodeType "mib_dielectric" -nodeType "mib_ray_marcher" -nodeType "mib_illum_lambert"
		 -nodeType "mib_illum_phong" -nodeType "mib_illum_ward" -nodeType "mib_illum_ward_deriv"
		 -nodeType "mib_illum_blinn" -nodeType "mib_illum_cooktorr" -nodeType "mib_illum_hair"
		 -nodeType "mib_volume" -nodeType "mib_color_alpha" -nodeType "mib_color_average"
		 -nodeType "mib_color_intensity" -nodeType "mib_color_interpolate" -nodeType "mib_color_mix"
		 -nodeType "mib_color_spread" -nodeType "mib_geo_cube" -nodeType "mib_geo_torus" -nodeType "mib_geo_sphere"
		 -nodeType "mib_geo_cone" -nodeType "mib_geo_cylinder" -nodeType "mib_geo_square"
		 -nodeType "mib_geo_instance" -nodeType "mib_geo_instance_mlist" -nodeType "mib_geo_add_uv_texsurf"
		 -nodeType "mib_photon_basic" -nodeType "mib_light_infinite" -nodeType "mib_light_point"
		 -nodeType "mib_light_spot" -nodeType "mib_light_photometric" -nodeType "mib_cie_d"
		 -nodeType "mib_blackbody" -nodeType "mib_shadow_transparency" -nodeType "mib_lens_stencil"
		 -nodeType "mib_lens_clamp" -nodeType "mib_lightmap_write" -nodeType "mib_lightmap_sample"
		 -nodeType "mib_amb_occlusion" -nodeType "mib_fast_occlusion" -nodeType "mib_map_get_scalar"
		 -nodeType "mib_map_get_integer" -nodeType "mib_map_get_vector" -nodeType "mib_map_get_color"
		 -nodeType "mib_map_get_transform" -nodeType "mib_map_get_scalar_array" -nodeType "mib_map_get_integer_array"
		 -nodeType "mib_fg_occlusion" -nodeType "mib_bent_normal_env" -nodeType "mib_glossy_reflection"
		 -nodeType "mib_glossy_refraction" -nodeType "mib_illum_hair_x" -nodeType "builtin_bsdf_architectural"
		 -nodeType "builtin_bsdf_architectural_comp" -nodeType "builtin_bsdf_carpaint" -nodeType "builtin_bsdf_ashikhmin"
		 -nodeType "builtin_bsdf_lambert" -nodeType "builtin_bsdf_mirror" -nodeType "builtin_bsdf_phong"
		 -nodeType "contour_store_function" -nodeType "contour_store_function_simple" -nodeType "contour_contrast_function_levels"
		 -nodeType "contour_contrast_function_simple" -nodeType "contour_shader_simple" -nodeType "contour_shader_silhouette"
		 -nodeType "contour_shader_maxcolor" -nodeType "contour_shader_curvature" -nodeType "contour_shader_factorcolor"
		 -nodeType "contour_shader_depthfade" -nodeType "contour_shader_framefade" -nodeType "contour_shader_layerthinner"
		 -nodeType "contour_shader_widthfromcolor" -nodeType "contour_shader_widthfromlightdir"
		 -nodeType "contour_shader_widthfromlight" -nodeType "contour_shader_combi" -nodeType "contour_only"
		 -nodeType "contour_composite" -nodeType "contour_ps" -nodeType "mi_metallic_paint"
		 -nodeType "mi_metallic_paint_x" -nodeType "mi_bump_flakes" -nodeType "mi_car_paint_phen"
		 -nodeType "mi_metallic_paint_output_mixer" -nodeType "mi_car_paint_phen_x" -nodeType "physical_lens_dof"
		 -nodeType "physical_light" -nodeType "dgs_material" -nodeType "dgs_material_photon"
		 -nodeType "dielectric_material" -nodeType "dielectric_material_photon" -nodeType "oversampling_lens"
		 -nodeType "path_material" -nodeType "parti_volume" -nodeType "parti_volume_photon"
		 -nodeType "transmat" -nodeType "transmat_photon" -nodeType "mip_rayswitch" -nodeType "mip_rayswitch_advanced"
		 -nodeType "mip_rayswitch_environment" -nodeType "mip_card_opacity" -nodeType "mip_motionblur"
		 -nodeType "mip_motion_vector" -nodeType "mip_matteshadow" -nodeType "mip_cameramap"
		 -nodeType "mip_mirrorball" -nodeType "mip_grayball" -nodeType "mip_gamma_gain" -nodeType "mip_render_subset"
		 -nodeType "mip_matteshadow_mtl" -nodeType "mip_binaryproxy" -nodeType "mip_rayswitch_stage"
		 -nodeType "mip_fgshooter" -nodeType "mib_ptex_lookup" -nodeType "misss_physical"
		 -nodeType "misss_physical_phen" -nodeType "misss_fast_shader" -nodeType "misss_fast_shader_x"
		 -nodeType "misss_fast_shader2" -nodeType "misss_fast_shader2_x" -nodeType "misss_skin_specular"
		 -nodeType "misss_lightmap_write" -nodeType "misss_lambert_gamma" -nodeType "misss_call_shader"
		 -nodeType "misss_set_normal" -nodeType "misss_fast_lmap_maya" -nodeType "misss_fast_simple_maya"
		 -nodeType "misss_fast_skin_maya" -nodeType "misss_fast_skin_phen" -nodeType "misss_fast_skin_phen_d"
		 -nodeType "misss_mia_skin2_phen" -nodeType "misss_mia_skin2_phen_d" -nodeType "misss_lightmap_phen"
		 -nodeType "misss_mia_skin2_surface_phen" -nodeType "surfaceSampler" -nodeType "mib_data_bool"
		 -nodeType "mib_data_int" -nodeType "mib_data_scalar" -nodeType "mib_data_vector"
		 -nodeType "mib_data_color" -nodeType "mib_data_string" -nodeType "mib_data_texture"
		 -nodeType "mib_data_shader" -nodeType "mib_data_bool_array" -nodeType "mib_data_int_array"
		 -nodeType "mib_data_scalar_array" -nodeType "mib_data_vector_array" -nodeType "mib_data_color_array"
		 -nodeType "mib_data_string_array" -nodeType "mib_data_texture_array" -nodeType "mib_data_shader_array"
		 -nodeType "mib_data_get_bool" -nodeType "mib_data_get_int" -nodeType "mib_data_get_scalar"
		 -nodeType "mib_data_get_vector" -nodeType "mib_data_get_color" -nodeType "mib_data_get_string"
		 -nodeType "mib_data_get_texture" -nodeType "mib_data_get_shader" -nodeType "mib_data_get_shader_bool"
		 -nodeType "mib_data_get_shader_int" -nodeType "mib_data_get_shader_scalar" -nodeType "mib_data_get_shader_vector"
		 -nodeType "mib_data_get_shader_color" -nodeType "user_ibl_env" -nodeType "user_ibl_rect"
		 -nodeType "xgen_geo" -nodeType "xgen_seexpr" -nodeType "xgen_scalar_to_integer" -nodeType "xgen_integer_to_vector"
		 -nodeType "xgen_scalar_to_vector" -nodeType "xgen_boolean_to_vector" -nodeType "xgen_boolean_switch"
		 -nodeType "xgen_tube_normals" -nodeType "xgen_hair_phen" -nodeType "mia_material_x_passes"
		 -nodeType "mi_metallic_paint_x_passes" -nodeType "mi_car_paint_phen_x_passes" -nodeType "misss_fast_shader_x_passes"
		 -dataType "byteArray" "Mayatomr" "2014.0 - 3.11.1.13 ";
requires "stretchMesh2012_linux64" "1.6";
requires "RenderMan_for_Maya" "3.0.1";
requires "3delight_for_maya2012" "7.0.12";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2014";
fileInfo "version" "2014";
fileInfo "cutIdentifier" "201310090313-890429";
fileInfo "osv" "Microsoft Windows 7 Ultimate Edition, 64-bit Windows 7 Service Pack 1 (Build 7601)\n";
createNode transform -n "GRP_JAW_TEMPLATE";
	setAttr ".t" -type "double3" 0 2.9552905740525337 0 ;
createNode nurbsCurve -n "curveShape1" -p "GRP_JAW_TEMPLATE";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-6.1208811960837526 0.5146202518335512 5.8014026134310877
		6.1208811960837526 0.5146202518335512 5.8014026134310877
		6.1208811960837526 0.5146202518335512 -3.4490906409248554
		-6.1208811960837526 0.5146202518335512 -3.4490906409248554
		-6.1208811960837526 0.5146202518335512 5.8014026134310877
		;
createNode transform -n "JAW_ALL_JNT_Ctrl_GRP" -p "GRP_JAW_TEMPLATE";
createNode joint -n "up_jaw_inverse_joint" -p "JAW_ALL_JNT_Ctrl_GRP";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".t" -type "double3" 0 1.0338736248854845 0 ;
	setAttr ".r" -type "double3" 0 -89.999999999999986 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 1.2;
createNode joint -n "up_jaw_joint0" -p "up_jaw_inverse_joint";
	addAttr -ci true -sn "up_scale" -ln "up_scale" -at "double";
	addAttr -ci true -sn "dn_scale" -ln "dn_scale" -at "double";
	addAttr -ci true -sn "lf_scale" -ln "lf_scale" -at "double";
	addAttr -ci true -sn "rt_scale" -ln "rt_scale" -at "double";
	addAttr -ci true -sn "twist_scale" -ln "twist_scale" -at "double";
	addAttr -ci true -sn "up_driven" -ln "up_driven" -at "double";
	addAttr -ci true -sn "dn_driven" -ln "dn_driven" -at "double";
	addAttr -ci true -sn "lf_driven" -ln "lf_driven" -at "double";
	addAttr -ci true -sn "rt_driven" -ln "rt_driven" -at "double";
	addAttr -ci true -sn "twist_driven" -ln "twist_driven" -at "double";
	addAttr -ci true -sn "driven_envelope" -ln "driven_envelope" -min 0 -max 1 -at "double";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.65517241379310343;
	setAttr -cb on ".up_scale";
	setAttr -cb on ".dn_scale";
	setAttr -cb on ".lf_scale";
	setAttr -cb on ".rt_scale";
	setAttr -cb on ".twist_scale" 10;
	setAttr -cb on ".up_driven";
	setAttr -cb on ".dn_driven";
	setAttr -cb on ".lf_driven";
	setAttr -cb on ".rt_driven";
	setAttr -cb on ".twist_driven";
	setAttr -cb on ".driven_envelope" 1;
createNode joint -n "up_jaw_joint1" -p "up_jaw_joint0";
	setAttr ".t" -type "double3" 3.9999999999999991 0 8.8817841970012484e-016 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.65517241379310343;
createNode transform -n "up_jaw_joint1_locator1_GRP" -p "up_jaw_joint1";
	setAttr ".v" no;
	setAttr ".r" -type "double3" 0 89.999999999999986 0 ;
	setAttr ".s" -type "double3" 0.99999999999999978 1 0.99999999999999978 ;
createNode transform -n "up_jaw_joint1_locator1" -p "up_jaw_joint1_locator1_GRP";
createNode locator -n "up_jaw_joint1_locatorShape1" -p "up_jaw_joint1_locator1";
	setAttr -k off ".v";
	setAttr ".los" -type "double3" 0.2 0.2 0.2 ;
createNode transform -n "UpperTooth_Ctrl_GRP" -p "up_jaw_joint1";
	setAttr ".t" -type "double3" 0 0 -8.8817841970012484e-016 ;
	setAttr ".r" -type "double3" 0 89.999999999999986 0 ;
createNode transform -n "UpperTooth_Ctrl" -p "UpperTooth_Ctrl_GRP";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".t" -type "double3" 0 0.32072603094272267 1.1604098494159929 ;
	setAttr ".rp" -type "double3" 3.5527136788005009e-015 -0.15579652586853765 0 ;
	setAttr ".sp" -type "double3" 3.5527136788005009e-015 -0.15579652586853765 0 ;
createNode nurbsCurve -n "UpperTooth_CtrlShape" -p "UpperTooth_Ctrl";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		2 16 0 no 3
		19 0 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 16
		18
		-1.1306822720041669 -0.15455858837691183 0
		-1.1306822720041669 -0.15455858837691183 0
		-1.1306822720041669 -0.34985541985946522 0
		-0.56534113600208435 -0.44813386073335604 0
		-0.56534113600208435 -0.20726045714834163 0
		-0.56534113600208435 -0.20726045714834163 0
		-0.56534113600208435 -0.44813386073335604 0
		3.5527136788005009e-015 -0.44813386073335604 0
		3.5527136788005009e-015 -0.20726045714834163 0
		3.5527136788005009e-015 -0.20726045714834163 0
		3.5527136788005009e-015 -0.44813386073335604 0
		0.56534113600208435 -0.44813386073335604 0
		0.56534113600208435 -0.20726045714834163 0
		0.56534113600208435 -0.20726045714834163 0
		0.56534113600208435 -0.44813386073335604 0
		1.1306822720041581 -0.34985541985946522 0
		1.1306822720041581 -0.15455858837691183 0
		1.1306822720041581 -0.15455858837691183 0
		;
createNode nurbsCurve -n "UpperTooth_CtrlShape1" -p "UpperTooth_Ctrl";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		2 7 0 no 3
		10 0 0 1 2 3 4 5 6 7 7
		9
		-1.2689785075923687 0.13654080899628029 0
		-1.2689785075923687 0.13654080899628029 0
		-1.2689785075923687 -0.1792943775125857 0
		-0.63448925379618082 -0.26301304936812953 0
		3.5527136788005009e-015 -0.26301304936812953 0
		0.6344892537961897 -0.26301304936812953 0
		1.2689785075923758 -0.1792943775125857 0
		1.2689785075923758 0.13654080899628029 0
		1.2689785075923758 0.13654080899628029 0
		;
createNode nurbsCurve -n "UpperTooth_CtrlShape2" -p "UpperTooth_Ctrl";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		2 1 0 no 3
		4 0 0 1 1
		3
		-1.2689785075923687 0.13654080899628029 0
		3.5527136788005009e-015 0.085411240117682752 0
		1.2689785075923758 0.13654080899628029 0
		;
createNode joint -n "UpperTooth_Ctrl_joint1" -p "UpperTooth_Ctrl";
	setAttr ".v" no;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.5;
createNode transform -n "UpperTooth_second_Ctrl_GRP1" -p "UpperTooth_Ctrl";
	setAttr ".t" -type "double3" -8.8817841970012464e-016 -1.7763568394002505e-015 
		-4.6676336780747549 ;
	setAttr ".s" -type "double3" 0.99999999999999956 1 0.99999999999999956 ;
createNode transform -n "UpperTooth_second01_Ctrl_GRP" -p "UpperTooth_second_Ctrl_GRP1";
	setAttr ".t" -type "double3" -3.3475091250915936 0 0.47583406500714087 ;
createNode transform -n "UpperTooth_second01_Ctrl" -p "UpperTooth_second01_Ctrl_GRP";
	setAttr ".ove" yes;
	setAttr ".ovc" 15;
createNode nurbsCurve -n "UpperTooth_second01_CtrlShape" -p "UpperTooth_second01_Ctrl";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".cc" -type "nurbsCurve" 
		1 16 0 no 3
		17 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
		17
		-0.16132997132451851 0.36015578738767356 0.16132997132451862
		-0.16132997132451851 0.36015578738767356 -0.16132997132451862
		0.16132997132451851 0.36015578738767356 -0.16132997132451862
		0.16132997132451851 0.36015578738767356 0.16132997132451862
		-0.16132997132451851 0.36015578738767356 0.16132997132451862
		-0.34966010860242996 -0.46129804976527822 0.34966010860243019
		-0.34966010860242996 -0.46129804976527822 -0.34966010860243019
		-0.16132997132451851 0.36015578738767356 -0.16132997132451862
		-0.16132997132451851 0.36015578738767356 0.16132997132451862
		-0.34966010860242996 -0.46129804976527822 0.34966010860243019
		0.34966010860242996 -0.46129804976527822 0.34966010860243019
		0.16132997132451851 0.36015578738767356 0.16132997132451862
		0.16132997132451851 0.36015578738767356 -0.16132997132451862
		0.34966010860242996 -0.46129804976527822 -0.34966010860243019
		0.34966010860242996 -0.46129804976527822 0.34966010860243019
		0.34966010860242996 -0.46129804976527822 -0.34966010860243019
		-0.34966010860242996 -0.46129804976527822 -0.34966010860243019
		;
createNode joint -n "UpperTooth_second01_Ctrl_joint1" -p "UpperTooth_second01_Ctrl";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr ".uoc" yes;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 -3.3475091250915936 0 0.47583406500714087 1;
	setAttr ".radi" 0.5;
createNode transform -n "UpperTooth_second02_Ctrl_GRP1" -p "UpperTooth_second_Ctrl_GRP1";
	setAttr ".t" -type "double3" -2.5 0 2.9619478800781565 ;
createNode transform -n "UpperTooth_second02_Ctrl" -p "UpperTooth_second02_Ctrl_GRP1";
	setAttr ".ove" yes;
	setAttr ".ovc" 15;
createNode nurbsCurve -n "UpperTooth_second02_CtrlShape" -p "UpperTooth_second02_Ctrl";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".cc" -type "nurbsCurve" 
		1 16 0 no 3
		17 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
		17
		-0.16132997132451851 0.36015578738767356 0.16132997132451862
		-0.16132997132451851 0.36015578738767356 -0.16132997132451862
		0.16132997132451851 0.36015578738767356 -0.16132997132451862
		0.16132997132451851 0.36015578738767356 0.16132997132451862
		-0.16132997132451851 0.36015578738767356 0.16132997132451862
		-0.34966010860242996 -0.46129804976527822 0.34966010860243019
		-0.34966010860242996 -0.46129804976527822 -0.34966010860243019
		-0.16132997132451851 0.36015578738767356 -0.16132997132451862
		-0.16132997132451851 0.36015578738767356 0.16132997132451862
		-0.34966010860242996 -0.46129804976527822 0.34966010860243019
		0.34966010860242996 -0.46129804976527822 0.34966010860243019
		0.16132997132451851 0.36015578738767356 0.16132997132451862
		0.16132997132451851 0.36015578738767356 -0.16132997132451862
		0.34966010860242996 -0.46129804976527822 -0.34966010860243019
		0.34966010860242996 -0.46129804976527822 0.34966010860243019
		0.34966010860242996 -0.46129804976527822 -0.34966010860243019
		-0.34966010860242996 -0.46129804976527822 -0.34966010860243019
		;
createNode joint -n "UpperTooth_second02_Ctrl_joint1" -p "UpperTooth_second02_Ctrl";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 -2.5 0 2.9619478800781565 1;
	setAttr ".radi" 0.5;
createNode transform -n "UpperTooth_second03_Ctrl_GRP2" -p "UpperTooth_second_Ctrl_GRP1";
	setAttr ".t" -type "double3" 0 0 4 ;
createNode transform -n "UpperTooth_second03_Ctrl" -p "UpperTooth_second03_Ctrl_GRP2";
	setAttr ".ove" yes;
	setAttr ".ovc" 15;
createNode nurbsCurve -n "UpperTooth_second03_CtrlShape" -p "UpperTooth_second03_Ctrl";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".cc" -type "nurbsCurve" 
		1 16 0 no 3
		17 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
		17
		-0.16132997132451851 0.36015578738767356 0.16132997132451862
		-0.16132997132451851 0.36015578738767356 -0.16132997132451862
		0.16132997132451851 0.36015578738767356 -0.16132997132451862
		0.16132997132451851 0.36015578738767356 0.16132997132451862
		-0.16132997132451851 0.36015578738767356 0.16132997132451862
		-0.34966010860242996 -0.46129804976527822 0.34966010860243019
		-0.34966010860242996 -0.46129804976527822 -0.34966010860243019
		-0.16132997132451851 0.36015578738767356 -0.16132997132451862
		-0.16132997132451851 0.36015578738767356 0.16132997132451862
		-0.34966010860242996 -0.46129804976527822 0.34966010860243019
		0.34966010860242996 -0.46129804976527822 0.34966010860243019
		0.16132997132451851 0.36015578738767356 0.16132997132451862
		0.16132997132451851 0.36015578738767356 -0.16132997132451862
		0.34966010860242996 -0.46129804976527822 -0.34966010860243019
		0.34966010860242996 -0.46129804976527822 0.34966010860243019
		0.34966010860242996 -0.46129804976527822 -0.34966010860243019
		-0.34966010860242996 -0.46129804976527822 -0.34966010860243019
		;
createNode joint -n "UpperTooth_second03_Ctrl_joint1" -p "UpperTooth_second03_Ctrl";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 4 1;
	setAttr ".radi" 0.5;
createNode transform -n "UpperTooth_second04_Ctrl_GRP3" -p "UpperTooth_second_Ctrl_GRP1";
	setAttr ".t" -type "double3" 2.5 0 2.9619478800781565 ;
createNode transform -n "UpperTooth_second04_Ctrl" -p "UpperTooth_second04_Ctrl_GRP3";
	setAttr ".ove" yes;
	setAttr ".ovc" 15;
createNode nurbsCurve -n "UpperTooth_second04_CtrlShape" -p "UpperTooth_second04_Ctrl";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".cc" -type "nurbsCurve" 
		1 16 0 no 3
		17 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
		17
		-0.16132997132451851 0.36015578738767356 0.16132997132451862
		-0.16132997132451851 0.36015578738767356 -0.16132997132451862
		0.16132997132451851 0.36015578738767356 -0.16132997132451862
		0.16132997132451851 0.36015578738767356 0.16132997132451862
		-0.16132997132451851 0.36015578738767356 0.16132997132451862
		-0.34966010860242996 -0.46129804976527822 0.34966010860243019
		-0.34966010860242996 -0.46129804976527822 -0.34966010860243019
		-0.16132997132451851 0.36015578738767356 -0.16132997132451862
		-0.16132997132451851 0.36015578738767356 0.16132997132451862
		-0.34966010860242996 -0.46129804976527822 0.34966010860243019
		0.34966010860242996 -0.46129804976527822 0.34966010860243019
		0.16132997132451851 0.36015578738767356 0.16132997132451862
		0.16132997132451851 0.36015578738767356 -0.16132997132451862
		0.34966010860242996 -0.46129804976527822 -0.34966010860243019
		0.34966010860242996 -0.46129804976527822 0.34966010860243019
		0.34966010860242996 -0.46129804976527822 -0.34966010860243019
		-0.34966010860242996 -0.46129804976527822 -0.34966010860243019
		;
createNode joint -n "UpperTooth_second04_Ctrl_joint1" -p "UpperTooth_second04_Ctrl";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 2.5 0 2.9619478800781565 1;
	setAttr ".radi" 0.5;
createNode transform -n "UpperTooth_second05_Ctrl_GRP4" -p "UpperTooth_second_Ctrl_GRP1";
	setAttr ".t" -type "double3" 3.3475091250915936 0 1 ;
createNode transform -n "UpperTooth_second05_Ctrl" -p "UpperTooth_second05_Ctrl_GRP4";
	setAttr ".ove" yes;
	setAttr ".ovc" 15;
createNode nurbsCurve -n "UpperTooth_second05_CtrlShape" -p "UpperTooth_second05_Ctrl";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".cc" -type "nurbsCurve" 
		1 16 0 no 3
		17 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
		17
		-0.16132997132451851 0.36015578738767356 0.16132997132451862
		-0.16132997132451851 0.36015578738767356 -0.16132997132451862
		0.16132997132451851 0.36015578738767356 -0.16132997132451862
		0.16132997132451851 0.36015578738767356 0.16132997132451862
		-0.16132997132451851 0.36015578738767356 0.16132997132451862
		-0.34966010860242996 -0.46129804976527822 0.34966010860243019
		-0.34966010860242996 -0.46129804976527822 -0.34966010860243019
		-0.16132997132451851 0.36015578738767356 -0.16132997132451862
		-0.16132997132451851 0.36015578738767356 0.16132997132451862
		-0.34966010860242996 -0.46129804976527822 0.34966010860243019
		0.34966010860242996 -0.46129804976527822 0.34966010860243019
		0.16132997132451851 0.36015578738767356 0.16132997132451862
		0.16132997132451851 0.36015578738767356 -0.16132997132451862
		0.34966010860242996 -0.46129804976527822 -0.34966010860243019
		0.34966010860242996 -0.46129804976527822 0.34966010860243019
		0.34966010860242996 -0.46129804976527822 -0.34966010860243019
		-0.34966010860242996 -0.46129804976527822 -0.34966010860243019
		;
createNode joint -n "UpperTooth_second05_Ctrl_joint1" -p "UpperTooth_second05_Ctrl";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 3.3475091250915936 0 1 1;
	setAttr ".radi" 0.5;
createNode transform -n "low_jaw_inverse_Ctrl_GRP" -p "JAW_ALL_JNT_Ctrl_GRP";
createNode transform -n "low_jaw_inverse_Ctrl" -p "low_jaw_inverse_Ctrl_GRP";
createNode nurbsCurve -n "low_jaw_inverse_CtrlShape" -p "low_jaw_inverse_Ctrl";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr ".cc" -type "nurbsCurve" 
		1 50 0 no 3
		51 0 0.37689 0.75376699999999996 1.130657 1.5075460000000001 1.884423 2.2613129999999999
		 2.6382029999999999 3.0150800000000002 3.3919700000000002 3.768859 4.1457369999999996
		 4.5226249999999997 4.8995129999999998 5.2763910000000003 5.6532799999999996 6.0301710000000002
		 6.4070470000000004 6.7839369999999999 7.1608270000000003 7.5377039999999997 7.9145940000000001
		 8.2914840000000005 8.6683610000000009 9.0452510000000004 19.157319000000001 29.269387000000002
		 29.646277000000001 30.023154000000002 30.400044000000001 30.776934000000004 31.153811000000001
		 31.530701000000001 31.907591000000004 32.284467000000006 32.661358000000007 33.038246999999998
		 33.415125000000003 33.792013000000004 34.168901000000005 34.545779000000003 34.922668000000002
		 35.299558000000005 35.676434999999998 36.053325000000001 36.430215000000004 36.807091999999997
		 37.183981000000003 37.560871000000006 37.937747999999999 38.314638000000002
		51
		-4.2942986369092475 -1.7802411477161797e-016 0
		-4.3157398340885882 -0.15861152049166863 0
		-4.3769879606743904 -0.30647717448912926 0
		-4.4739818911021541 -0.43379343970267359 0
		-4.6012981563156963 -0.53078737013043487 0
		-4.7491638103131564 -0.59203549671623712 0
		-4.9077753308048297 -0.61347669389557891 0
		-5.0663868512964934 -0.59203549671623712 0
		-5.2142520806232922 -0.53078737013043487 0
		-5.341568770507501 -0.43379343970267348 0
		-5.4385622762645953 -0.30647717448912909 0
		-5.4998112521917291 -0.15861152049166846 0
		-5.5212469286524319 9.4413133931939223e-017 0
		-5.4998112521917291 0.15861152049166857 0
		-5.4385622762645953 0.30647717448912926 0
		-5.341568770507501 0.43379343970267359 0
		-5.2142520806232922 0.53078737013043487 0
		-5.0663868512964934 0.59203549671623712 0
		-4.9077753308048297 0.61347669389557891 0
		-4.7491638103131564 0.5920354967162369 0
		-4.6012981563156963 0.53078737013043487 0
		-4.4739818911021541 0.43379343970267348 0
		-4.3769879606743904 0.30647717448912909 0
		-4.3157398340885882 0.15861152049166843 0
		-4.2942986369092475 -1.7802411477161797e-016 0
		0 -1.1315499590342317e-015 0
		4.2942986369092475 -1.7802411477161753e-016 0
		4.3157398340885882 -0.15861152049166863 0
		4.3769879606743904 -0.30647717448912926 0
		4.4739818911021541 -0.43379343970267359 0
		4.6012981563156963 -0.53078737013043487 0
		4.7491638103131564 -0.59203549671623712 0
		4.9077753308048297 -0.61347669389557891 0
		5.0663868512964934 -0.59203549671623712 0
		5.2142520806232922 -0.53078737013043487 0
		5.341568770507501 -0.43379343970267348 0
		5.4385622762645953 -0.30647717448912909 0
		5.4998112521917291 -0.15861152049166846 0
		5.5212469286524319 9.4413133931940037e-017 0
		5.4998112521917291 0.15861152049166857 0
		5.4385622762645953 0.30647717448912926 0
		5.341568770507501 0.43379343970267359 0
		5.2142520806232922 0.53078737013043487 0
		5.0663868512964934 0.59203549671623712 0
		4.9077753308048297 0.61347669389557891 0
		4.7491638103131564 0.5920354967162369 0
		4.6012981563156963 0.53078737013043487 0
		4.4739818911021541 0.43379343970267348 0
		4.3769879606743904 0.30647717448912909 0
		4.3157398340885882 0.15861152049166843 0
		4.2942986369092475 -1.7802411477161753e-016 0
		;
createNode joint -n "low_jaw_inverse_joint0" -p "low_jaw_inverse_Ctrl";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 -89.999999999999986 0 ;
	setAttr ".radi" 1.2;
createNode joint -n "low_jaw_joint0" -p "low_jaw_inverse_joint0";
	addAttr -ci true -sn "up_scale" -ln "up_scale" -at "double";
	addAttr -ci true -sn "dn_scale" -ln "dn_scale" -at "double";
	addAttr -ci true -sn "lf_scale" -ln "lf_scale" -at "double";
	addAttr -ci true -sn "rt_scale" -ln "rt_scale" -at "double";
	addAttr -ci true -sn "twist_scale" -ln "twist_scale" -at "double";
	addAttr -ci true -sn "up_driven" -ln "up_driven" -at "double";
	addAttr -ci true -sn "dn_driven" -ln "dn_driven" -at "double";
	addAttr -ci true -sn "lf_driven" -ln "lf_driven" -at "double";
	addAttr -ci true -sn "rt_driven" -ln "rt_driven" -at "double";
	addAttr -ci true -sn "twist_driven" -ln "twist_driven" -at "double";
	addAttr -ci true -sn "driven_envelope" -ln "driven_envelope" -min 0 -max 1 -at "double";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.65517241379310343;
	setAttr -cb on ".up_scale";
	setAttr -cb on ".dn_scale" 20;
	setAttr -cb on ".lf_scale" 10;
	setAttr -cb on ".rt_scale" 10;
	setAttr -cb on ".twist_scale" 10;
	setAttr -cb on ".up_driven";
	setAttr -cb on ".dn_driven";
	setAttr -cb on ".lf_driven";
	setAttr -cb on ".rt_driven";
	setAttr -cb on ".twist_driven";
	setAttr -cb on ".driven_envelope" 1;
createNode joint -n "low_jaw_joint1" -p "low_jaw_joint0";
	setAttr ".t" -type "double3" 3.9999999999999991 0 8.8817841970012484e-016 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.65517241379310343;
createNode transform -n "low_jaw_joint1_locator1_GRP" -p "low_jaw_joint1";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 4.4408920985006262e-016 0 ;
	setAttr ".r" -type "double3" 0 89.999999999999986 0 ;
	setAttr ".s" -type "double3" 0.99999999999999978 1 0.99999999999999978 ;
createNode transform -n "low_jaw_joint1_locator1" -p "low_jaw_joint1_locator1_GRP";
createNode locator -n "low_jaw_joint1_locatorShape1" -p "low_jaw_joint1_locator1";
	setAttr -k off ".v";
	setAttr ".los" -type "double3" 0.2 0.2 0.2 ;
createNode transform -n "LowerTooth_Ctrl_GRP" -p "low_jaw_joint1";
	setAttr ".t" -type "double3" 0 4.4408920985006262e-016 0 ;
	setAttr ".r" -type "double3" 0 89.999999999999986 0 ;
	setAttr ".s" -type "double3" 0.99999999999999978 1 0.99999999999999978 ;
createNode transform -n "LowerTooth_Ctrl" -p "LowerTooth_Ctrl_GRP";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".t" -type "double3" 0 -0.30501729715100723 1.1513499477445635 ;
	setAttr ".rp" -type "double3" 2.1316282072803006e-014 0.25976856819356575 0 ;
	setAttr ".sp" -type "double3" 2.1316282072803006e-014 0.25976856819356575 0 ;
createNode nurbsCurve -n "LowerTooth_CtrlShape" -p "LowerTooth_Ctrl";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		2 16 0 no 3
		19 0 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 16
		18
		-1.1306822720041456 0.34334852807156713 0
		-1.1306822720041456 0.34334852807156713 0
		-1.1306822720041456 0.61930294451850254 0
		-0.56534113600206659 0.45914548531661414 0
		-0.56534113600206659 0.2182720817316004 0
		-0.56534113600206659 0.2182720817316004 0
		-0.56534113600206659 0.45914548531661414 0
		2.1316282072803006e-014 0.45914548531661414 0
		2.1316282072803006e-014 0.2182720817316004 0
		2.1316282072803006e-014 0.2182720817316004 0
		2.1316282072803006e-014 0.45914548531661414 0
		0.56534113600210567 0.45914548531661414 0
		0.56534113600210567 0.2182720817316004 0
		0.56534113600210567 0.2182720817316004 0
		0.56534113600210567 0.45914548531661414 0
		1.1306822720041811 0.61930294451850254 0
		1.1306822720041811 0.34334852807156713 0
		1.1306822720041811 0.34334852807156713 0
		;
createNode nurbsCurve -n "LowerTooth_CtrlShape1" -p "LowerTooth_Ctrl";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		2 7 0 no 3
		10 0 0 1 2 3 4 5 6 7 7
		9
		-1.2689785075923492 -0.013044132880099202 0
		-1.2689785075923492 -0.013044132880099202 0
		-1.2689785075923492 0.43418213315327647 0
		-0.63448925379616306 0.27402467395138808 0
		2.1316282072803006e-014 0.27402467395138808 0
		0.63448925379620746 0.27402467395138808 0
		1.2689785075923901 0.43418213315327647 0
		1.2689785075923901 -0.013044132880099202 0
		1.2689785075923901 -0.013044132880099202 0
		;
createNode nurbsCurve -n "LowerTooth_CtrlShape2" -p "LowerTooth_Ctrl";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		2 1 0 no 3
		4 0 0 1 1
		3
		-1.2689785075923492 -0.013044132880099202 0
		2.1316282072803006e-014 -0.099765808131371259 0
		1.2689785075923901 -0.013044132880099202 0
		;
createNode joint -n "LowerTooth_Ctrl_joint1" -p "LowerTooth_Ctrl";
	setAttr ".v" no;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.5;
createNode transform -n "LowerTooth_second_Ctrl_GRP" -p "LowerTooth_Ctrl";
	setAttr ".t" -type "double3" 0 0.23299730815575526 -4.6394063358182134 ;
	setAttr ".s" -type "double3" 0.99999999999999978 1 0.99999999999999978 ;
createNode transform -n "LowerTooth_second01_Ctrl_GRP" -p "LowerTooth_second_Ctrl_GRP";
	setAttr ".t" -type "double3" -3.3475091250915936 0 0.47583406500714087 ;
createNode transform -n "LowerTooth_second01_Ctrl" -p "LowerTooth_second01_Ctrl_GRP";
	setAttr ".ove" yes;
	setAttr ".ovc" 15;
createNode nurbsCurve -n "LowerTooth_second01_CtrlShape" -p "LowerTooth_second01_Ctrl";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".cc" -type "nurbsCurve" 
		1 16 0 no 3
		17 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
		17
		-0.36015578738767356 0.36015578738767356 0.36015578738767356
		-0.36015578738767356 0.36015578738767356 -0.36015578738767356
		0.36015578738767356 0.36015578738767356 -0.36015578738767356
		0.36015578738767356 0.36015578738767356 0.36015578738767356
		-0.36015578738767356 0.36015578738767356 0.36015578738767356
		-0.12507825517515772 -0.36015578738767356 0.12507825517515772
		-0.12507825517515772 -0.36015578738767356 -0.12507825517515772
		-0.36015578738767356 0.36015578738767356 -0.36015578738767356
		-0.36015578738767356 0.36015578738767356 0.36015578738767356
		-0.12507825517515772 -0.36015578738767356 0.12507825517515772
		0.12507825517515772 -0.36015578738767356 0.12507825517515772
		0.36015578738767356 0.36015578738767356 0.36015578738767356
		0.36015578738767356 0.36015578738767356 -0.36015578738767356
		0.12507825517515772 -0.36015578738767356 -0.12507825517515772
		0.12507825517515772 -0.36015578738767356 0.12507825517515772
		0.12507825517515772 -0.36015578738767356 -0.12507825517515772
		-0.12507825517515772 -0.36015578738767356 -0.12507825517515772
		;
createNode joint -n "LowerTooth_second01_Ctrl_joint1" -p "LowerTooth_second01_Ctrl";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr ".uoc" yes;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 -3.3475091250915936 0 0.47583406500714087 1;
	setAttr ".radi" 0.5;
createNode transform -n "LowerTooth_second02_Ctrl_GRP1" -p "LowerTooth_second_Ctrl_GRP";
	setAttr ".t" -type "double3" -2.5 0 2.9619478800781565 ;
createNode transform -n "LowerTooth_second02_Ctrl" -p "LowerTooth_second02_Ctrl_GRP1";
	setAttr ".ove" yes;
	setAttr ".ovc" 15;
createNode nurbsCurve -n "LowerTooth_second02_CtrlShape" -p "LowerTooth_second02_Ctrl";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".cc" -type "nurbsCurve" 
		1 16 0 no 3
		17 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
		17
		-0.36015578738767356 0.36015578738767356 0.36015578738767356
		-0.36015578738767356 0.36015578738767356 -0.36015578738767356
		0.36015578738767356 0.36015578738767356 -0.36015578738767356
		0.36015578738767356 0.36015578738767356 0.36015578738767356
		-0.36015578738767356 0.36015578738767356 0.36015578738767356
		-0.12507825517515772 -0.36015578738767356 0.12507825517515772
		-0.12507825517515772 -0.36015578738767356 -0.12507825517515772
		-0.36015578738767356 0.36015578738767356 -0.36015578738767356
		-0.36015578738767356 0.36015578738767356 0.36015578738767356
		-0.12507825517515772 -0.36015578738767356 0.12507825517515772
		0.12507825517515772 -0.36015578738767356 0.12507825517515772
		0.36015578738767356 0.36015578738767356 0.36015578738767356
		0.36015578738767356 0.36015578738767356 -0.36015578738767356
		0.12507825517515772 -0.36015578738767356 -0.12507825517515772
		0.12507825517515772 -0.36015578738767356 0.12507825517515772
		0.12507825517515772 -0.36015578738767356 -0.12507825517515772
		-0.12507825517515772 -0.36015578738767356 -0.12507825517515772
		;
createNode joint -n "LowerTooth_second02_Ctrl_joint1" -p "LowerTooth_second02_Ctrl";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 -2.5 0 2.9619478800781565 1;
	setAttr ".radi" 0.5;
createNode transform -n "LowerTooth_second03_Ctrl_GRP2" -p "LowerTooth_second_Ctrl_GRP";
	setAttr ".t" -type "double3" 0 0 4 ;
createNode transform -n "LowerTooth_second03_Ctrl" -p "LowerTooth_second03_Ctrl_GRP2";
	setAttr ".ove" yes;
	setAttr ".ovc" 15;
createNode nurbsCurve -n "LowerTooth_second03_CtrlShape" -p "LowerTooth_second03_Ctrl";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".cc" -type "nurbsCurve" 
		1 16 0 no 3
		17 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
		17
		-0.36015578738767356 0.36015578738767356 0.36015578738767356
		-0.36015578738767356 0.36015578738767356 -0.36015578738767356
		0.36015578738767356 0.36015578738767356 -0.36015578738767356
		0.36015578738767356 0.36015578738767356 0.36015578738767356
		-0.36015578738767356 0.36015578738767356 0.36015578738767356
		-0.12507825517515772 -0.36015578738767356 0.12507825517515772
		-0.12507825517515772 -0.36015578738767356 -0.12507825517515772
		-0.36015578738767356 0.36015578738767356 -0.36015578738767356
		-0.36015578738767356 0.36015578738767356 0.36015578738767356
		-0.12507825517515772 -0.36015578738767356 0.12507825517515772
		0.12507825517515772 -0.36015578738767356 0.12507825517515772
		0.36015578738767356 0.36015578738767356 0.36015578738767356
		0.36015578738767356 0.36015578738767356 -0.36015578738767356
		0.12507825517515772 -0.36015578738767356 -0.12507825517515772
		0.12507825517515772 -0.36015578738767356 0.12507825517515772
		0.12507825517515772 -0.36015578738767356 -0.12507825517515772
		-0.12507825517515772 -0.36015578738767356 -0.12507825517515772
		;
createNode joint -n "LowerTooth_second03_Ctrl_joint1" -p "LowerTooth_second03_Ctrl";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 4 1;
	setAttr ".radi" 0.5;
createNode transform -n "LowerTooth_second04_Ctrl_GRP3" -p "LowerTooth_second_Ctrl_GRP";
	setAttr ".t" -type "double3" 2.5 0 2.9619478800781565 ;
createNode transform -n "LowerTooth_second04_Ctrl" -p "LowerTooth_second04_Ctrl_GRP3";
	setAttr ".ove" yes;
	setAttr ".ovc" 15;
createNode nurbsCurve -n "LowerTooth_second04_CtrlShape" -p "LowerTooth_second04_Ctrl";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".cc" -type "nurbsCurve" 
		1 16 0 no 3
		17 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
		17
		-0.36015578738767356 0.36015578738767356 0.36015578738767356
		-0.36015578738767356 0.36015578738767356 -0.36015578738767356
		0.36015578738767356 0.36015578738767356 -0.36015578738767356
		0.36015578738767356 0.36015578738767356 0.36015578738767356
		-0.36015578738767356 0.36015578738767356 0.36015578738767356
		-0.12507825517515772 -0.36015578738767356 0.12507825517515772
		-0.12507825517515772 -0.36015578738767356 -0.12507825517515772
		-0.36015578738767356 0.36015578738767356 -0.36015578738767356
		-0.36015578738767356 0.36015578738767356 0.36015578738767356
		-0.12507825517515772 -0.36015578738767356 0.12507825517515772
		0.12507825517515772 -0.36015578738767356 0.12507825517515772
		0.36015578738767356 0.36015578738767356 0.36015578738767356
		0.36015578738767356 0.36015578738767356 -0.36015578738767356
		0.12507825517515772 -0.36015578738767356 -0.12507825517515772
		0.12507825517515772 -0.36015578738767356 0.12507825517515772
		0.12507825517515772 -0.36015578738767356 -0.12507825517515772
		-0.12507825517515772 -0.36015578738767356 -0.12507825517515772
		;
createNode joint -n "LowerTooth_second04_Ctrl_joint1" -p "LowerTooth_second04_Ctrl";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 2.5 0 2.9619478800781565 1;
	setAttr ".radi" 0.5;
createNode transform -n "LowerTooth_second05_Ctrl_GRP4" -p "LowerTooth_second_Ctrl_GRP";
	setAttr ".t" -type "double3" 3.3475091250915936 0 1 ;
createNode transform -n "LowerTooth_second05_Ctrl" -p "LowerTooth_second05_Ctrl_GRP4";
	setAttr ".ove" yes;
	setAttr ".ovc" 15;
createNode nurbsCurve -n "LowerTooth_second05_CtrlShape" -p "LowerTooth_second05_Ctrl";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".cc" -type "nurbsCurve" 
		1 16 0 no 3
		17 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
		17
		-0.36015578738767356 0.36015578738767356 0.36015578738767356
		-0.36015578738767356 0.36015578738767356 -0.36015578738767356
		0.36015578738767356 0.36015578738767356 -0.36015578738767356
		0.36015578738767356 0.36015578738767356 0.36015578738767356
		-0.36015578738767356 0.36015578738767356 0.36015578738767356
		-0.12507825517515772 -0.36015578738767356 0.12507825517515772
		-0.12507825517515772 -0.36015578738767356 -0.12507825517515772
		-0.36015578738767356 0.36015578738767356 -0.36015578738767356
		-0.36015578738767356 0.36015578738767356 0.36015578738767356
		-0.12507825517515772 -0.36015578738767356 0.12507825517515772
		0.12507825517515772 -0.36015578738767356 0.12507825517515772
		0.36015578738767356 0.36015578738767356 0.36015578738767356
		0.36015578738767356 0.36015578738767356 -0.36015578738767356
		0.12507825517515772 -0.36015578738767356 -0.12507825517515772
		0.12507825517515772 -0.36015578738767356 0.12507825517515772
		0.12507825517515772 -0.36015578738767356 -0.12507825517515772
		-0.12507825517515772 -0.36015578738767356 -0.12507825517515772
		;
createNode joint -n "LowerTooth_second05_Ctrl_joint1" -p "LowerTooth_second05_Ctrl";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 3.3475091250915936 0 1 1;
	setAttr ".radi" 0.5;
createNode transform -n "Left_jaw_joint1_GRP_GRP_GRP" -p "JAW_ALL_JNT_Ctrl_GRP";
createNode joint -n "Left_jaw_joint1" -p "Left_jaw_joint1_GRP_GRP_GRP";
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr ".t" -type "double3" 1 0.5 4 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.5;
createNode transform -n "Right_jaw_joint1_GRP_GRP_GRP" -p "JAW_ALL_JNT_Ctrl_GRP";
createNode joint -n "Right_jaw_joint1" -p "Right_jaw_joint1_GRP_GRP_GRP";
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr ".t" -type "double3" -1 0.49999999999999956 4 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.5;
createNode transform -n "middle_jaw_joint1_GRP_GRP_GRP" -p "JAW_ALL_JNT_Ctrl_GRP";
createNode joint -n "middle_jaw_joint1" -p "middle_jaw_joint1_GRP_GRP_GRP";
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr ".t" -type "double3" 0 0.5 4 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.5;
createNode transform -n "Deformer_JAW_GRP";
createNode transform -n "UpperTooth_curve" -p "Deformer_JAW_GRP";
	setAttr ".v" no;
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode nurbsCurve -n "UpperTooth_curveShape" -p "UpperTooth_curve";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".tw" yes;
	setAttr ".dcv" yes;
createNode nurbsCurve -n "UpperTooth_curveShape1Orig" -p "UpperTooth_curve";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		3 4 0 no 3
		9 0 0 0 1 2 3 4 4 4
		7
		-3.3475091250915936 0 0
		-3.3475091250915936 0 1
		-2.8240562472892567 0 3.6487549113869626
		0 0 4
		2.8240562472892567 0 3.6487549113869626
		3.3475091250915936 0 1
		3.3475091250915936 0 0
		;
	setAttr ".dcv" yes;
createNode nurbsCurve -n "UpperTooth_curveShapeOrig" -p "UpperTooth_curve";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		3 4 0 no 3
		9 0 0 0 1 2 3 4 4 4
		7
		-3.3475091250915936 0 0
		-3.3475091250915936 0 1
		-2.8240562472892567 0 3.6487549113869626
		0 0 4
		2.8240562472892567 0 3.6487549113869626
		3.3475091250915936 0 1
		3.3475091250915936 0 0
		;
	setAttr ".dcv" yes;
createNode transform -n "LowerTooth_curve" -p "Deformer_JAW_GRP";
	setAttr ".v" no;
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode nurbsCurve -n "LowerTooth_curveShape" -p "LowerTooth_curve";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".tw" yes;
	setAttr ".dcv" yes;
createNode nurbsCurve -n "LowerTooth_curveShape1Orig" -p "LowerTooth_curve";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		3 4 0 no 3
		9 0 0 0 1 2 3 4 4 4
		7
		-3.3475091250915936 0 0
		-3.3475091250915936 0 1
		-2.8240562472892567 0 3.6487549113869626
		0 0 4
		2.8240562472892567 0 3.6487549113869626
		3.3475091250915936 0 1
		3.3475091250915936 0 0
		;
	setAttr ".dcv" yes;
createNode unitConversion -n "unitConversion4";
	setAttr ".cf" 0.017453292519943295;
createNode expression -n "jaw_driven_ex";
	setAttr -k on ".nds";
	setAttr -s 22 ".in[17:21]"  10 0 30 0 30;
	setAttr -s 17 ".in";
	setAttr -s 6 ".out";
	setAttr ".ixp" -type "string" "//jaw_driven_ex\n.O[0]=(linstep(0,1,.I[0])*.I[1]\n+linstep(0,1,.I[2])*-.I[3])\n*.I[4];\n\n.O[1]=(linstep(0,1,.I[5])*.I[6]\n+linstep(0,1,.I[7])*-.I[8])\n*.I[4];\n\n.O[2]=.I[9]*.I[10]\n*.I[4];\n\n\n.O[3]=(linstep(0,1,.I[0])*.I[11]\n+linstep(0,1,.I[2])*-.I[12])\n*.I[13];\n\n.O[4]=(linstep(0,1,.I[5])*.I[14]\n+linstep(0,1,.I[7])*-.I[15])\n*.I[13];\n\n.O[5]=.I[9]*.I[16]\n*.I[13];";
createNode unitConversion -n "unitConversion5";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion6";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion1";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion2";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion3";
	setAttr ".cf" 0.017453292519943295;
createNode skinCluster -n "skinCluster2";
	setAttr -s 7 ".wl";
	setAttr -s 5 ".wl[0].w[0:4]"  0.99930996640418546 0.00056867108818160652 
		6.9214770454910962e-005 2.7749963669901311e-005 2.4397773508134796e-005;
	setAttr -s 5 ".wl[1].w[0:4]"  0.99612207642527884 0.0036043627748916967 
		0.00018417678704889701 5.1957386805389379e-005 3.7426625975261694e-005;
	setAttr -s 5 ".wl[2].w[0:4]"  0.0030830597448684386 0.9913307418101418 
		0.0050270828033038414 0.00039704265318541918 0.00016207298850051018;
	setAttr ".wl[3].w[2]"  1;
	setAttr -s 5 ".wl[4].w[0:4]"  0.00014174371867211805 0.00039581505508579751 
		0.0050115397948979042 0.98826569143084586 0.0061852100004983817;
	setAttr ".wl[5].w[4]"  1;
	setAttr -s 5 ".wl[6].w[0:4]"  0.00048618183813694822 0.00053446882138924771 
		0.0013330877556386779 0.010952697807969602 0.98669356377686557;
	setAttr -s 5 ".pm";
	setAttr ".pm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 3.3475091250915936 0 -0.47583406500714087 1;
	setAttr ".pm[1]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 2.5 0 -2.9619478800781565 1;
	setAttr ".pm[2]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 -4 1;
	setAttr ".pm[3]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 -2.5 0 -2.9619478800781565 1;
	setAttr ".pm[4]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 -3.3475091250915936 0 -1 1;
	setAttr ".gm" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr -s 5 ".ma";
	setAttr -s 5 ".dpf[0:4]"  4 4 4 4 4;
	setAttr -s 5 ".lw";
	setAttr -s 5 ".lw";
	setAttr ".mmi" yes;
	setAttr ".mi" 30;
	setAttr ".bm" 0;
	setAttr ".ucm" yes;
	setAttr -s 5 ".ifcl";
	setAttr -s 5 ".ifcl";
createNode objectSet -n "skinCluster2Set";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode dagPose -n "bindPose2";
	setAttr -s 16 ".wm";
	setAttr ".wm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".wm[1]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 -3.3475091250915936 0 0.47583406500714087 1;
	setAttr ".wm[2]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 -3.3475091250915936 0 0.47583406500714087 1;
	setAttr ".wm[4]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 -2.5 0 2.9619478800781565 1;
	setAttr ".wm[5]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 -2.5 0 2.9619478800781565 1;
	setAttr ".wm[7]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 4 1;
	setAttr ".wm[8]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 4 1;
	setAttr ".wm[10]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 2.5 0 2.9619478800781565 1;
	setAttr ".wm[11]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 2.5 0 2.9619478800781565 1;
	setAttr ".wm[13]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 3.3475091250915936 0 1 1;
	setAttr ".wm[14]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 3.3475091250915936 0 1 1;
	setAttr -s 16 ".xm";
	setAttr ".xm[0]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[1]" -type "matrix" "xform" 1 1 1 0 0 0 0 -3.3475091250915936 0
		 0.47583406500714087 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[2]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[3]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[4]" -type "matrix" "xform" 1 1 1 0 0 0 0 -2.5 0 2.9619478800781565 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[5]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[6]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[7]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 4 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[8]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[9]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[10]" -type "matrix" "xform" 1 1 1 0 0 0 0 2.5 0 2.9619478800781565 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[11]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[12]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[13]" -type "matrix" "xform" 1 1 1 0 0 0 0 3.3475091250915936 0
		 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[14]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[15]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr -s 16 ".m";
	setAttr -s 16 ".p";
	setAttr -s 16 ".g[0:15]" yes yes yes no yes yes no yes yes no yes yes 
		no yes yes no;
	setAttr ".bp" yes;
createNode groupId -n "skinCluster2GroupId";
	setAttr ".ihi" 0;
createNode groupParts -n "skinCluster2GroupParts";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode tweak -n "tweak2";
createNode objectSet -n "tweakSet2";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId4";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts4";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode skinCluster -n "skinCluster1";
	setAttr -s 7 ".wl";
	setAttr -s 5 ".wl[0].w[0:4]"  0.99930996640418546 0.00056867108818160652 
		6.9214770454910962e-005 2.7749963669901311e-005 2.4397773508134796e-005;
	setAttr -s 5 ".wl[1].w[0:4]"  0.99612207642527884 0.0036043627748916967 
		0.00018417678704889701 5.1957386805389379e-005 3.7426625975261694e-005;
	setAttr -s 5 ".wl[2].w[0:4]"  0.0030830597448684386 0.9913307418101418 
		0.0050270828033038414 0.00039704265318541918 0.00016207298850051018;
	setAttr ".wl[3].w[2]"  1;
	setAttr -s 5 ".wl[4].w[0:4]"  0.00014174371867211805 0.00039581505508579751 
		0.0050115397948979042 0.98826569143084586 0.0061852100004983817;
	setAttr ".wl[5].w[4]"  1;
	setAttr -s 5 ".wl[6].w[0:4]"  0.00048618183813694822 0.00053446882138924771 
		0.0013330877556386779 0.010952697807969602 0.98669356377686557;
	setAttr -s 5 ".pm";
	setAttr ".pm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 3.3475091250915936 0 -0.47583406500714087 1;
	setAttr ".pm[1]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 2.5 0 -2.9619478800781565 1;
	setAttr ".pm[2]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 -4 1;
	setAttr ".pm[3]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 -2.5 0 -2.9619478800781565 1;
	setAttr ".pm[4]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 -3.3475091250915936 0 -1 1;
	setAttr ".gm" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr -s 5 ".ma";
	setAttr -s 5 ".dpf[0:4]"  4 4 4 4 4;
	setAttr -s 5 ".lw";
	setAttr -s 5 ".lw";
	setAttr ".mmi" yes;
	setAttr ".mi" 30;
	setAttr ".bm" 0;
	setAttr ".ucm" yes;
	setAttr -s 5 ".ifcl";
	setAttr -s 5 ".ifcl";
createNode objectSet -n "skinCluster1Set";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode dagPose -n "bindPose1";
	setAttr -s 15 ".wm";
	setAttr ".wm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 -3.3475091250915936 0 0.47583406500714087 1;
	setAttr ".wm[1]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 -3.3475091250915936 0 0.47583406500714087 1;
	setAttr ".wm[3]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 -2.5 0 2.9619478800781565 1;
	setAttr ".wm[4]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 -2.5 0 2.9619478800781565 1;
	setAttr ".wm[6]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 4 1;
	setAttr ".wm[7]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 4 1;
	setAttr ".wm[9]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 2.5 0 2.9619478800781565 1;
	setAttr ".wm[10]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 2.5 0 2.9619478800781565 1;
	setAttr ".wm[12]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 3.3475091250915936 0 1 1;
	setAttr ".wm[13]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 3.3475091250915936 0 1 1;
	setAttr -s 15 ".xm";
	setAttr ".xm[0]" -type "matrix" "xform" 1 1 1 0 0 0 0 -3.3475091250915936 0
		 0.47583406500714087 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[1]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[2]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[3]" -type "matrix" "xform" 1 1 1 0 0 0 0 -2.5 0 2.9619478800781565 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[4]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[5]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[6]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 4 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[7]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[8]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[9]" -type "matrix" "xform" 1 1 1 0 0 0 0 2.5 0 2.9619478800781565 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[10]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[11]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[12]" -type "matrix" "xform" 1 1 1 0 0 0 0 3.3475091250915936 0
		 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[13]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[14]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr -s 15 ".m";
	setAttr -s 15 ".p";
	setAttr -s 15 ".g[0:14]" yes yes no yes yes no yes yes no yes yes no 
		yes yes no;
	setAttr ".bp" yes;
createNode groupId -n "skinCluster1GroupId";
	setAttr ".ihi" 0;
createNode groupParts -n "skinCluster1GroupParts";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode tweak -n "tweak1";
createNode objectSet -n "tweakSet1";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId2";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts2";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
select -ne :time1;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".o" 1;
	setAttr -av ".unw" 1;
	setAttr -k on ".etw";
	setAttr -k on ".tps";
	setAttr -k on ".tms";
lockNode -l 1 ;
select -ne :renderPartition;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".st";
	setAttr -cb on ".an";
	setAttr -cb on ".pt";
lockNode -l 1 ;
select -ne :initialShadingGroup;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".mwc";
	setAttr -cb on ".an";
	setAttr -cb on ".il";
	setAttr -cb on ".vo";
	setAttr -cb on ".eo";
	setAttr -cb on ".fo";
	setAttr -cb on ".epo";
	setAttr -k on ".ro" yes;
	setAttr -cb on ".mimt";
	setAttr -cb on ".miop";
	setAttr -k on ".mico";
	setAttr -cb on ".mise";
	setAttr -cb on ".mism";
	setAttr -cb on ".mice";
	setAttr -av -cb on ".micc";
	setAttr -k on ".micr";
	setAttr -k on ".micg";
	setAttr -k on ".micb";
	setAttr -cb on ".mica";
	setAttr -av -cb on ".micw";
	setAttr -cb on ".mirw";
lockNode -l 1 ;
select -ne :initialParticleSE;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".mwc";
	setAttr -cb on ".an";
	setAttr -cb on ".il";
	setAttr -cb on ".vo";
	setAttr -cb on ".eo";
	setAttr -cb on ".fo";
	setAttr -cb on ".epo";
	setAttr -k on ".ro" yes;
	setAttr -cb on ".mimt";
	setAttr -cb on ".miop";
	setAttr -k on ".mico";
	setAttr -cb on ".mise";
	setAttr -cb on ".mism";
	setAttr -cb on ".mice";
	setAttr -av -cb on ".micc";
	setAttr -k on ".micr";
	setAttr -k on ".micg";
	setAttr -k on ".micb";
	setAttr -cb on ".mica";
	setAttr -av -cb on ".micw";
	setAttr -cb on ".mirw";
lockNode -l 1 ;
select -ne :defaultShaderList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".s";
lockNode -l 1 ;
select -ne :postProcessList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".p";
lockNode -l 1 ;
select -ne :defaultRenderingList1;
select -ne :renderGlobalsList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
lockNode -l 1 ;
select -ne :defaultRenderGlobals;
	addAttr -ci true -sn "shave_old_preRenderMel" -ln "shave_old_preRenderMel" -dt "string";
	addAttr -ci true -sn "shave_old_postRenderMel" -ln "shave_old_postRenderMel" -dt "string";
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".macc";
	setAttr -k on ".macd";
	setAttr -k on ".macq";
	setAttr -k on ".mcfr";
	setAttr -cb on ".ifg";
	setAttr -k on ".clip";
	setAttr -k on ".edm";
	setAttr -k on ".edl";
	setAttr -cb on ".ren";
	setAttr -av -k on ".esr";
	setAttr -k on ".ors";
	setAttr -cb on ".sdf";
	setAttr -av -k on ".outf";
	setAttr -cb on ".imfkey";
	setAttr -k on ".gama";
	setAttr -k on ".an";
	setAttr -k on ".ar";
	setAttr -k on ".fs";
	setAttr -k on ".ef";
	setAttr -av -k on ".bfs";
	setAttr -cb on ".me";
	setAttr -cb on ".se";
	setAttr -av -k on ".be";
	setAttr -k on ".ep" 1;
	setAttr -k on ".fec";
	setAttr -av -k on ".ofc";
	setAttr -cb on ".ofe";
	setAttr -cb on ".efe";
	setAttr -cb on ".oft";
	setAttr -cb on ".umfn";
	setAttr -cb on ".ufe";
	setAttr -k on ".pff";
	setAttr -k on ".peie";
	setAttr -k on ".ifp";
	setAttr -k on ".rv";
	setAttr -k on ".comp";
	setAttr -k on ".cth";
	setAttr -k on ".soll";
	setAttr -k on ".sosl";
	setAttr -k on ".rd";
	setAttr -k on ".lp";
	setAttr -av -k on ".sp";
	setAttr -k on ".shs";
	setAttr -av -k on ".lpr";
	setAttr -cb on ".gv";
	setAttr -cb on ".sv";
	setAttr -k on ".mm";
	setAttr -k on ".npu";
	setAttr -k on ".itf";
	setAttr -k on ".shp";
	setAttr -cb on ".isp";
	setAttr -k on ".uf";
	setAttr -k on ".oi";
	setAttr -k on ".rut";
	setAttr -k on ".mot";
	setAttr -av -k on ".mb";
	setAttr -av -k on ".mbf";
	setAttr -k on ".mbso";
	setAttr -k on ".mbsc";
	setAttr -av -k on ".afp";
	setAttr -k on ".pfb";
	setAttr -k on ".pram" -type "string" "";
	setAttr -k on ".poam";
	setAttr -k on ".prlm";
	setAttr -k on ".polm";
	setAttr -cb on ".prm" -type "string" "shave_MRFrameStart;";
	setAttr -cb on ".pom" -type "string" "shave_MRFrameEnd;";
	setAttr -cb on ".pfrm";
	setAttr -cb on ".pfom";
	setAttr -av -k on ".bll";
	setAttr -av -k on ".bls";
	setAttr -av -k on ".smv";
	setAttr -k on ".ubc";
	setAttr -k on ".mbc";
	setAttr -cb on ".mbt";
	setAttr -k on ".udbx";
	setAttr -k on ".smc";
	setAttr -k on ".kmv";
	setAttr -cb on ".isl";
	setAttr -cb on ".ism";
	setAttr -cb on ".imb";
	setAttr -av -k on ".rlen";
	setAttr -av -k on ".frts";
	setAttr -k on ".tlwd";
	setAttr -k on ".tlht";
	setAttr -k on ".jfc";
	setAttr -cb on ".rsb";
	setAttr -k on ".ope";
	setAttr -k on ".oppf";
	setAttr -cb on ".hbl";
	setAttr ".shave_old_preRenderMel" -type "string" "";
	setAttr ".shave_old_postRenderMel" -type "string" "";
select -ne :defaultResolution;
	setAttr -av -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -k on ".bnm";
	setAttr -av -k on ".w" 640;
	setAttr -av -k on ".h" 480;
	setAttr -av -k on ".pa";
	setAttr -av -k on ".al";
	setAttr -av -k on ".dar" 1.3333332538604736;
	setAttr -av -k on ".ldar";
	setAttr -k on ".dpi";
	setAttr -av -k on ".off";
	setAttr -av -k on ".fld";
	setAttr -av -k on ".zsl";
	setAttr -k on ".isu";
	setAttr -k on ".pdu";
select -ne :defaultLightSet;
	setAttr -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -k on ".bnm";
	setAttr -k on ".mwc";
	setAttr -k on ".an";
	setAttr -k on ".il";
	setAttr -k on ".vo";
	setAttr -k on ".eo";
	setAttr -k on ".fo";
	setAttr -k on ".epo";
	setAttr -k on ".ro" yes;
lockNode -l 1 ;
select -ne :defaultObjectSet;
	setAttr -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -k on ".nds";
	setAttr -k on ".bnm";
	setAttr -k on ".mwc";
	setAttr -k on ".an";
	setAttr -k on ".il";
	setAttr -k on ".vo";
	setAttr -k on ".eo";
	setAttr -k on ".fo";
	setAttr -k on ".epo";
	setAttr -k on ".ro" yes;
select -ne :hardwareRenderGlobals;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k off ".ctrs" 256;
	setAttr -av -k off ".btrs" 512;
	setAttr -k off ".fbfm";
	setAttr -k off -cb on ".ehql";
	setAttr -k off -cb on ".eams";
	setAttr -k off -cb on ".eeaa";
	setAttr -k off -cb on ".engm";
	setAttr -k off -cb on ".mes";
	setAttr -k off -cb on ".emb";
	setAttr -av -k off -cb on ".mbbf";
	setAttr -k off -cb on ".mbs";
	setAttr -k off -cb on ".trm";
	setAttr -k off -cb on ".tshc";
	setAttr -k off ".enpt";
	setAttr -k off -cb on ".clmt";
	setAttr -k off -cb on ".tcov";
	setAttr -k off -cb on ".lith";
	setAttr -k off -cb on ".sobc";
	setAttr -k off -cb on ".cuth";
	setAttr -k off -cb on ".hgcd";
	setAttr -k off -cb on ".hgci";
	setAttr -k off -cb on ".mgcs";
	setAttr -k off -cb on ".twa";
	setAttr -k off -cb on ".twz";
	setAttr -k on ".hwcc";
	setAttr -k on ".hwdp";
	setAttr -k on ".hwql";
	setAttr -k on ".hwfr";
	setAttr -k on ".soll";
	setAttr -k on ".sosl";
	setAttr -k on ".bswa";
	setAttr -k on ".shml";
	setAttr -k on ".hwel";
lockNode -l 1 ;
select -ne :hardwareRenderingGlobals;
	setAttr ".vac" 2;
select -ne :defaultHardwareRenderGlobals;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -av -k on ".rp";
	setAttr -k on ".cai";
	setAttr -k on ".coi";
	setAttr -cb on ".bc";
	setAttr -av -k on ".bcr";
	setAttr -av -k on ".bcg";
	setAttr -av -k on ".bcb";
	setAttr -k on ".ei";
	setAttr -av -k on ".ex";
	setAttr -av -k on ".es";
	setAttr -av -k on ".ef";
	setAttr -av -k on ".bf";
	setAttr -k on ".fii";
	setAttr -av -k on ".sf";
	setAttr -k on ".gr";
	setAttr -k on ".li";
	setAttr -k on ".ls";
	setAttr -av -k on ".mb";
	setAttr -k on ".ti";
	setAttr -k on ".txt";
	setAttr -k on ".mpr";
	setAttr -k on ".wzd";
	setAttr -k on ".fn" -type "string" "im";
	setAttr -k on ".if";
	setAttr -k on ".res" -type "string" "ntsc_4d 646 485 1.333";
	setAttr -k on ".as";
	setAttr -k on ".ds";
	setAttr -k on ".lm";
	setAttr -av -k on ".fir";
	setAttr -k on ".aap";
	setAttr -av -k on ".gh";
	setAttr -cb on ".sd";
lockNode -l 1 ;
connectAttr "up_jaw_inverse_joint.s" "up_jaw_joint0.is";
connectAttr "unitConversion4.o" "up_jaw_joint0.rz";
connectAttr "unitConversion5.o" "up_jaw_joint0.ry";
connectAttr "unitConversion6.o" "up_jaw_joint0.rx";
connectAttr "up_jaw_joint0.s" "up_jaw_joint1.is";
connectAttr "low_jaw_inverse_joint0.s" "low_jaw_joint0.is";
connectAttr "unitConversion1.o" "low_jaw_joint0.rz";
connectAttr "unitConversion2.o" "low_jaw_joint0.ry";
connectAttr "unitConversion3.o" "low_jaw_joint0.rx";
connectAttr "low_jaw_joint0.s" "low_jaw_joint1.is";
connectAttr "skinCluster2.og[0]" "UpperTooth_curveShape.cr";
connectAttr "tweak2.pl[0].cp[0]" "UpperTooth_curveShape.twl";
connectAttr "skinCluster2GroupId.id" "UpperTooth_curveShape.iog.og[2].gid";
connectAttr "skinCluster2Set.mwc" "UpperTooth_curveShape.iog.og[2].gco";
connectAttr "groupId4.id" "UpperTooth_curveShape.iog.og[3].gid";
connectAttr "tweakSet2.mwc" "UpperTooth_curveShape.iog.og[3].gco";
connectAttr "skinCluster1.og[0]" "LowerTooth_curveShape.cr";
connectAttr "tweak1.pl[0].cp[0]" "LowerTooth_curveShape.twl";
connectAttr "skinCluster1GroupId.id" "LowerTooth_curveShape.iog.og[0].gid";
connectAttr "skinCluster1Set.mwc" "LowerTooth_curveShape.iog.og[0].gco";
connectAttr "groupId2.id" "LowerTooth_curveShape.iog.og[1].gid";
connectAttr "tweakSet1.mwc" "LowerTooth_curveShape.iog.og[1].gco";
connectAttr "jaw_driven_ex.out[3]" "unitConversion4.i";
connectAttr ":time1.o" "jaw_driven_ex.tim";
connectAttr "low_jaw_joint0.up_driven" "jaw_driven_ex.in[0]";
connectAttr "low_jaw_joint0.up_scale" "jaw_driven_ex.in[1]";
connectAttr "low_jaw_joint0.dn_driven" "jaw_driven_ex.in[2]";
connectAttr "low_jaw_joint0.dn_scale" "jaw_driven_ex.in[3]";
connectAttr "low_jaw_joint0.driven_envelope" "jaw_driven_ex.in[4]";
connectAttr "low_jaw_joint0.lf_driven" "jaw_driven_ex.in[5]";
connectAttr "low_jaw_joint0.lf_scale" "jaw_driven_ex.in[6]";
connectAttr "low_jaw_joint0.rt_driven" "jaw_driven_ex.in[7]";
connectAttr "low_jaw_joint0.rt_scale" "jaw_driven_ex.in[8]";
connectAttr "low_jaw_joint0.twist_driven" "jaw_driven_ex.in[9]";
connectAttr "low_jaw_joint0.twist_scale" "jaw_driven_ex.in[10]";
connectAttr "up_jaw_joint0.up_scale" "jaw_driven_ex.in[11]";
connectAttr "up_jaw_joint0.dn_scale" "jaw_driven_ex.in[12]";
connectAttr "up_jaw_joint0.driven_envelope" "jaw_driven_ex.in[13]";
connectAttr "up_jaw_joint0.lf_scale" "jaw_driven_ex.in[14]";
connectAttr "up_jaw_joint0.rt_scale" "jaw_driven_ex.in[15]";
connectAttr "up_jaw_joint0.twist_scale" "jaw_driven_ex.in[16]";
connectAttr "jaw_driven_ex.out[4]" "unitConversion5.i";
connectAttr "jaw_driven_ex.out[5]" "unitConversion6.i";
connectAttr "jaw_driven_ex.out[0]" "unitConversion1.i";
connectAttr "jaw_driven_ex.out[1]" "unitConversion2.i";
connectAttr "jaw_driven_ex.out[2]" "unitConversion3.i";
connectAttr "skinCluster2GroupParts.og" "skinCluster2.ip[0].ig";
connectAttr "skinCluster2GroupId.id" "skinCluster2.ip[0].gi";
connectAttr "bindPose2.msg" "skinCluster2.bp";
connectAttr "UpperTooth_second01_Ctrl_joint1.wm" "skinCluster2.ma[0]";
connectAttr "UpperTooth_second02_Ctrl_joint1.wm" "skinCluster2.ma[1]";
connectAttr "UpperTooth_second03_Ctrl_joint1.wm" "skinCluster2.ma[2]";
connectAttr "UpperTooth_second04_Ctrl_joint1.wm" "skinCluster2.ma[3]";
connectAttr "UpperTooth_second05_Ctrl_joint1.wm" "skinCluster2.ma[4]";
connectAttr "UpperTooth_second01_Ctrl_joint1.liw" "skinCluster2.lw[0]";
connectAttr "UpperTooth_second02_Ctrl_joint1.liw" "skinCluster2.lw[1]";
connectAttr "UpperTooth_second03_Ctrl_joint1.liw" "skinCluster2.lw[2]";
connectAttr "UpperTooth_second04_Ctrl_joint1.liw" "skinCluster2.lw[3]";
connectAttr "UpperTooth_second05_Ctrl_joint1.liw" "skinCluster2.lw[4]";
connectAttr "UpperTooth_second01_Ctrl_joint1.obcc" "skinCluster2.ifcl[0]";
connectAttr "UpperTooth_second02_Ctrl_joint1.obcc" "skinCluster2.ifcl[1]";
connectAttr "UpperTooth_second03_Ctrl_joint1.obcc" "skinCluster2.ifcl[2]";
connectAttr "UpperTooth_second04_Ctrl_joint1.obcc" "skinCluster2.ifcl[3]";
connectAttr "UpperTooth_second05_Ctrl_joint1.obcc" "skinCluster2.ifcl[4]";
connectAttr "skinCluster2GroupId.msg" "skinCluster2Set.gn" -na;
connectAttr "UpperTooth_curveShape.iog.og[2]" "skinCluster2Set.dsm" -na;
connectAttr "skinCluster2.msg" "skinCluster2Set.ub[0]";
connectAttr "UpperTooth_second_Ctrl_GRP1.msg" "bindPose2.m[0]";
connectAttr "UpperTooth_second01_Ctrl_GRP.msg" "bindPose2.m[1]";
connectAttr "UpperTooth_second01_Ctrl.msg" "bindPose2.m[2]";
connectAttr "UpperTooth_second01_Ctrl_joint1.msg" "bindPose2.m[3]";
connectAttr "UpperTooth_second02_Ctrl_GRP1.msg" "bindPose2.m[4]";
connectAttr "UpperTooth_second02_Ctrl.msg" "bindPose2.m[5]";
connectAttr "UpperTooth_second02_Ctrl_joint1.msg" "bindPose2.m[6]";
connectAttr "UpperTooth_second03_Ctrl_GRP2.msg" "bindPose2.m[7]";
connectAttr "UpperTooth_second03_Ctrl.msg" "bindPose2.m[8]";
connectAttr "UpperTooth_second03_Ctrl_joint1.msg" "bindPose2.m[9]";
connectAttr "UpperTooth_second04_Ctrl_GRP3.msg" "bindPose2.m[10]";
connectAttr "UpperTooth_second04_Ctrl.msg" "bindPose2.m[11]";
connectAttr "UpperTooth_second04_Ctrl_joint1.msg" "bindPose2.m[12]";
connectAttr "UpperTooth_second05_Ctrl_GRP4.msg" "bindPose2.m[13]";
connectAttr "UpperTooth_second05_Ctrl.msg" "bindPose2.m[14]";
connectAttr "UpperTooth_second05_Ctrl_joint1.msg" "bindPose2.m[15]";
connectAttr "bindPose2.w" "bindPose2.p[0]";
connectAttr "bindPose2.m[0]" "bindPose2.p[1]";
connectAttr "bindPose2.m[1]" "bindPose2.p[2]";
connectAttr "bindPose2.m[2]" "bindPose2.p[3]";
connectAttr "bindPose2.m[0]" "bindPose2.p[4]";
connectAttr "bindPose2.m[4]" "bindPose2.p[5]";
connectAttr "bindPose2.m[5]" "bindPose2.p[6]";
connectAttr "bindPose2.m[0]" "bindPose2.p[7]";
connectAttr "bindPose2.m[7]" "bindPose2.p[8]";
connectAttr "bindPose2.m[8]" "bindPose2.p[9]";
connectAttr "bindPose2.m[0]" "bindPose2.p[10]";
connectAttr "bindPose2.m[10]" "bindPose2.p[11]";
connectAttr "bindPose2.m[11]" "bindPose2.p[12]";
connectAttr "bindPose2.m[0]" "bindPose2.p[13]";
connectAttr "bindPose2.m[13]" "bindPose2.p[14]";
connectAttr "bindPose2.m[14]" "bindPose2.p[15]";
connectAttr "UpperTooth_second01_Ctrl_joint1.bps" "bindPose2.wm[3]";
connectAttr "UpperTooth_second02_Ctrl_joint1.bps" "bindPose2.wm[6]";
connectAttr "UpperTooth_second03_Ctrl_joint1.bps" "bindPose2.wm[9]";
connectAttr "UpperTooth_second04_Ctrl_joint1.bps" "bindPose2.wm[12]";
connectAttr "UpperTooth_second05_Ctrl_joint1.bps" "bindPose2.wm[15]";
connectAttr "tweak2.og[0]" "skinCluster2GroupParts.ig";
connectAttr "skinCluster2GroupId.id" "skinCluster2GroupParts.gi";
connectAttr "groupParts4.og" "tweak2.ip[0].ig";
connectAttr "groupId4.id" "tweak2.ip[0].gi";
connectAttr "groupId4.msg" "tweakSet2.gn" -na;
connectAttr "UpperTooth_curveShape.iog.og[3]" "tweakSet2.dsm" -na;
connectAttr "tweak2.msg" "tweakSet2.ub[0]";
connectAttr "UpperTooth_curveShapeOrig.ws" "groupParts4.ig";
connectAttr "groupId4.id" "groupParts4.gi";
connectAttr "skinCluster1GroupParts.og" "skinCluster1.ip[0].ig";
connectAttr "skinCluster1GroupId.id" "skinCluster1.ip[0].gi";
connectAttr "bindPose1.msg" "skinCluster1.bp";
connectAttr "LowerTooth_second01_Ctrl_joint1.wm" "skinCluster1.ma[0]";
connectAttr "LowerTooth_second02_Ctrl_joint1.wm" "skinCluster1.ma[1]";
connectAttr "LowerTooth_second03_Ctrl_joint1.wm" "skinCluster1.ma[2]";
connectAttr "LowerTooth_second04_Ctrl_joint1.wm" "skinCluster1.ma[3]";
connectAttr "LowerTooth_second05_Ctrl_joint1.wm" "skinCluster1.ma[4]";
connectAttr "LowerTooth_second01_Ctrl_joint1.liw" "skinCluster1.lw[0]";
connectAttr "LowerTooth_second02_Ctrl_joint1.liw" "skinCluster1.lw[1]";
connectAttr "LowerTooth_second03_Ctrl_joint1.liw" "skinCluster1.lw[2]";
connectAttr "LowerTooth_second04_Ctrl_joint1.liw" "skinCluster1.lw[3]";
connectAttr "LowerTooth_second05_Ctrl_joint1.liw" "skinCluster1.lw[4]";
connectAttr "LowerTooth_second01_Ctrl_joint1.obcc" "skinCluster1.ifcl[0]";
connectAttr "LowerTooth_second02_Ctrl_joint1.obcc" "skinCluster1.ifcl[1]";
connectAttr "LowerTooth_second03_Ctrl_joint1.obcc" "skinCluster1.ifcl[2]";
connectAttr "LowerTooth_second04_Ctrl_joint1.obcc" "skinCluster1.ifcl[3]";
connectAttr "LowerTooth_second05_Ctrl_joint1.obcc" "skinCluster1.ifcl[4]";
connectAttr "skinCluster1GroupId.msg" "skinCluster1Set.gn" -na;
connectAttr "LowerTooth_curveShape.iog.og[0]" "skinCluster1Set.dsm" -na;
connectAttr "skinCluster1.msg" "skinCluster1Set.ub[0]";
connectAttr "LowerTooth_second01_Ctrl_GRP.msg" "bindPose1.m[0]";
connectAttr "LowerTooth_second01_Ctrl.msg" "bindPose1.m[1]";
connectAttr "LowerTooth_second01_Ctrl_joint1.msg" "bindPose1.m[2]";
connectAttr "LowerTooth_second02_Ctrl_GRP1.msg" "bindPose1.m[3]";
connectAttr "LowerTooth_second02_Ctrl.msg" "bindPose1.m[4]";
connectAttr "LowerTooth_second02_Ctrl_joint1.msg" "bindPose1.m[5]";
connectAttr "LowerTooth_second03_Ctrl_GRP2.msg" "bindPose1.m[6]";
connectAttr "LowerTooth_second03_Ctrl.msg" "bindPose1.m[7]";
connectAttr "LowerTooth_second03_Ctrl_joint1.msg" "bindPose1.m[8]";
connectAttr "LowerTooth_second04_Ctrl_GRP3.msg" "bindPose1.m[9]";
connectAttr "LowerTooth_second04_Ctrl.msg" "bindPose1.m[10]";
connectAttr "LowerTooth_second04_Ctrl_joint1.msg" "bindPose1.m[11]";
connectAttr "LowerTooth_second05_Ctrl_GRP4.msg" "bindPose1.m[12]";
connectAttr "LowerTooth_second05_Ctrl.msg" "bindPose1.m[13]";
connectAttr "LowerTooth_second05_Ctrl_joint1.msg" "bindPose1.m[14]";
connectAttr "bindPose1.w" "bindPose1.p[0]";
connectAttr "bindPose1.m[0]" "bindPose1.p[1]";
connectAttr "bindPose1.m[1]" "bindPose1.p[2]";
connectAttr "bindPose1.w" "bindPose1.p[3]";
connectAttr "bindPose1.m[3]" "bindPose1.p[4]";
connectAttr "bindPose1.m[4]" "bindPose1.p[5]";
connectAttr "bindPose1.w" "bindPose1.p[6]";
connectAttr "bindPose1.m[6]" "bindPose1.p[7]";
connectAttr "bindPose1.m[7]" "bindPose1.p[8]";
connectAttr "bindPose1.w" "bindPose1.p[9]";
connectAttr "bindPose1.m[9]" "bindPose1.p[10]";
connectAttr "bindPose1.m[10]" "bindPose1.p[11]";
connectAttr "bindPose1.w" "bindPose1.p[12]";
connectAttr "bindPose1.m[12]" "bindPose1.p[13]";
connectAttr "bindPose1.m[13]" "bindPose1.p[14]";
connectAttr "LowerTooth_second01_Ctrl_joint1.bps" "bindPose1.wm[2]";
connectAttr "LowerTooth_second02_Ctrl_joint1.bps" "bindPose1.wm[5]";
connectAttr "LowerTooth_second03_Ctrl_joint1.bps" "bindPose1.wm[8]";
connectAttr "LowerTooth_second04_Ctrl_joint1.bps" "bindPose1.wm[11]";
connectAttr "LowerTooth_second05_Ctrl_joint1.bps" "bindPose1.wm[14]";
connectAttr "tweak1.og[0]" "skinCluster1GroupParts.ig";
connectAttr "skinCluster1GroupId.id" "skinCluster1GroupParts.gi";
connectAttr "groupParts2.og" "tweak1.ip[0].ig";
connectAttr "groupId2.id" "tweak1.ip[0].gi";
connectAttr "groupId2.msg" "tweakSet1.gn" -na;
connectAttr "LowerTooth_curveShape.iog.og[1]" "tweakSet1.dsm" -na;
connectAttr "tweak1.msg" "tweakSet1.ub[0]";
connectAttr "LowerTooth_curveShape1Orig.ws" "groupParts2.ig";
connectAttr "groupId2.id" "groupParts2.gi";
// End of HIGH_jaw_rig.ma

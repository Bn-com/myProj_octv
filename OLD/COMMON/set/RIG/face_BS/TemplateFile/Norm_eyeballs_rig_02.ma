//Maya ASCII 2014 scene
//Name: High_eyeballs_rig_02.ma
//Last modified: Thu, May 21, 2015 09:28:26 AM
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
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2014";
fileInfo "version" "2014";
fileInfo "cutIdentifier" "201310090313-890429";
fileInfo "osv" "Microsoft Windows 7 Ultimate Edition, 64-bit Windows 7 Service Pack 1 (Build 7601)\n";
createNode transform -n "GRP_EYEBALLS_TEMPLATE";
	setAttr ".t" -type "double3" 0 22.415421365825836 0 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode joint -n "Lf_eyeballs_joint0" -p "GRP_EYEBALLS_TEMPLATE";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".t" -type "double3" 6 0 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 -89.999999999999986 0 ;
	setAttr ".radi" 0.60344827586206895;
createNode joint -n "Lf_eyeballs_joint1" -p "Lf_eyeballs_joint0";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".t" -type "double3" 8 0 1.5543122344752188e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.60344827586206895;
createNode joint -n "Lf_eyeballs_highlight_joint1" -p "Lf_eyeballs_joint1";
	addAttr -ci true -sn "tx_scale" -ln "tx_scale" -at "double";
	addAttr -ci true -sn "ty_scale" -ln "ty_scale" -at "double";
	addAttr -ci true -sn "envelope" -ln "envelope" -at "double";
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr ".t" -type "double3" 0 0 1.0000000000000002 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.60344827586206895;
	setAttr -cb on ".tx_scale" 1;
	setAttr -cb on ".ty_scale" 1;
	setAttr -cb on ".envelope" 1;
createNode joint -n "Rt_eyeballs_joint0" -p "GRP_EYEBALLS_TEMPLATE";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".t" -type "double3" -6 0 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 -89.999999999999986 0 ;
	setAttr ".radi" 0.60344827586206895;
createNode joint -n "Rt_eyeballs_joint1" -p "Rt_eyeballs_joint0";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".t" -type "double3" 8 0 1.5543122344752188e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.60344827586206895;
createNode joint -n "Rt_eyeballs_highlight_joint1" -p "Rt_eyeballs_joint1";
	addAttr -ci true -sn "tx_scale" -ln "tx_scale" -at "double";
	addAttr -ci true -sn "ty_scale" -ln "ty_scale" -at "double";
	addAttr -ci true -sn "envelope" -ln "envelope" -at "double";
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr ".t" -type "double3" 8.8817841970012523e-016 0 -1 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.60344827586206895;
	setAttr -cb on ".tx_scale" 1;
	setAttr -cb on ".ty_scale" 1;
	setAttr -cb on ".envelope" 1;
createNode nurbsCurve -n "curveShape1" -p "GRP_EYEBALLS_TEMPLATE";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-8.253548055175628 0 -2.4129173038717067
		-8.253548055175628 0 11.560710784343534
		8.253548055175628 0 11.560710784343534
		8.253548055175628 0 -2.4129173038717067
		-8.253548055175628 0 -2.4129173038717067
		;
createNode transform -n "EYE_RIG" -p "GRP_EYEBALLS_TEMPLATE";
	setAttr ".t" -type "double3" 0 0 20 ;
	setAttr ".s" -type "double3" 1 0.99999999999999989 0.99999999999999989 ;
createNode transform -n "eye_GoupB" -p "EYE_RIG";
createNode transform -n "eye_GoupA" -p "eye_GoupB";
createNode transform -n "c_eye_M" -p "eye_GoupA";
	addAttr -ci true -sn "sign" -ln "sign" -dv 73 -at "long";
	addAttr -ci true -sn "follow" -ln "follow" -dv 1 -min 0 -max 1 -en "OFF:ON" -at "enum";
	addAttr -ci true -sn "in_out" -ln "in_out" -min -1 -max 1 -at "double";
	setAttr -l on -k off ".v";
	setAttr -l on ".tz";
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr ".rp" -type "double3" 0 0 -3.6112658378631225e-015 ;
	setAttr ".sp" -type "double3" 0 0 -3.6112658378631225e-015 ;
	setAttr -cb on ".follow";
	setAttr -k on ".in_out";
createNode nurbsCurve -n "c_eye_MShape" -p "c_eye_M";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		10.958403031864222 5.4455177926378759 -7.1306234359665606e-015
		-1.7174646998296069e-015 7.7011251164924825 -7.1306234359665606e-015
		-10.958403031864213 5.4455177926378759 -7.1306234359665606e-015
		-13.645443259240748 4.0168419106486942e-015 -7.1306234359665606e-015
		-10.958403031864213 -5.4455177926378751 -7.1306234359665606e-015
		-4.5360198919541622e-015 -7.7011251164924825 -7.1306234359665606e-015
		10.958403031864211 -5.4455177926378759 -7.1306234359665606e-015
		13.645443259240748 -3.5423091375266121e-015 -7.1306234359665606e-015
		10.958403031864222 5.4455177926378759 -7.1306234359665606e-015
		-1.7174646998296069e-015 7.7011251164924825 -7.1306234359665606e-015
		-10.958403031864213 5.4455177926378759 -7.1306234359665606e-015
		;
createNode transform -n "Lf_eye_M_GRP" -p "c_eye_M";
	setAttr ".t" -type "double3" 2.5 0 0 ;
	setAttr ".rp" -type "double3" 0.76756054849076027 3.3306690738754696e-016 8.8817841970012523e-016 ;
	setAttr ".sp" -type "double3" 0.76756054849076027 3.3306690738754696e-016 8.8817841970012523e-016 ;
createNode transform -n "GRP_c_Lf_eye_M_inOut" -p "Lf_eye_M_GRP";
	setAttr ".rp" -type "double3" 5.0706044437764923 7.1054273576010019e-015 3.5527136788005009e-015 ;
	setAttr ".sp" -type "double3" 5.0706044437764923 7.1054273576010019e-015 3.5527136788005009e-015 ;
createNode transform -n "c_Lf_eye_M" -p "GRP_c_Lf_eye_M_inOut";
	addAttr -ci true -sn "sign" -ln "sign" -dv 73 -at "long";
	addAttr -ci true -sn "translateWeight" -ln "translateWeight" -dv 1 -min 0 -max 1 
		-at "double";
	addAttr -ci true -sn "in_scale" -ln "in_scale" -at "double";
	addAttr -ci true -sn "out_scale" -ln "out_scale" -at "double";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 4.4408920985006262e-016 0 0 ;
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sz";
	setAttr -k off ".sy";
	setAttr ".rp" -type "double3" 5.0706044437764914 6.2172489379008766e-015 3.4962297255345149e-015 ;
	setAttr ".sp" -type "double3" 5.0706044437764914 6.2172489379008766e-015 3.4962297255345149e-015 ;
	setAttr ".mnsl" -type "double3" 0.5 -1 -1 ;
	setAttr ".mxsl" -type "double3" 1.5 1 1 ;
	setAttr ".msxe" yes;
	setAttr ".xsxe" yes;
	setAttr -k on ".translateWeight";
	setAttr -cb on ".in_scale" 5;
	setAttr -cb on ".out_scale" 5;
createNode nurbsCurve -n "c_Lf_eye_MShape" -p "c_Lf_eye_M";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		8.0626199785373629 3.7414782532514548 -9.1908239759683886e-017
		5.0706044437764923 5.291249289072204 -9.1908239759683886e-017
		2.0785889090156302 3.7414782532514566 -9.1908239759683886e-017
		0.83925549568669489 5.962630571033457e-015 -9.1908239759683886e-017
		2.0785889090156329 -3.7414782532514477 -9.1908239759683886e-017
		5.0706044437764923 -5.2912492890721916 -9.1908239759683886e-017
		8.0626199785373593 -3.741478253251449 -9.1908239759683886e-017
		9.301953391866288 2.1215047803886798e-015 -9.1908239759683886e-017
		8.0626199785373629 3.7414782532514548 -9.1908239759683886e-017
		5.0706044437764923 5.291249289072204 -9.1908239759683886e-017
		2.0785889090156302 3.7414782532514566 -9.1908239759683886e-017
		;
createNode transform -n "Lf_spec_tempMod_M_GRP" -p "c_Lf_eye_M";
	setAttr ".rp" -type "double3" 7.0788108621165975 1.4432899320127035e-015 7.0843676908287134e-015 ;
	setAttr ".sp" -type "double3" 7.0788108621165975 1.4432899320127035e-015 7.0843676908287134e-015 ;
createNode transform -n "c_Lf_spec_M" -p "Lf_spec_tempMod_M_GRP";
	addAttr -ci true -sn "sign" -ln "sign" -dv 73 -at "long";
	addAttr -ci true -sn "spec_tempMod_vis" -ln "spec_tempMod_vis" -min 0 -max 1 -en 
		"OFF:ON" -at "enum";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 0 0 7.1054273576010019e-015 ;
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 7.3009755246218644 1.8717248316724677 -2.1059666772288488e-017 ;
	setAttr ".sp" -type "double3" 7.3009755246218644 1.8717248316724677 -2.1059666772288488e-017 ;
	setAttr ".mntl" -type "double3" -5 -5 -1 ;
	setAttr ".mxtl" -type "double3" 5 5 1 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".mnsl" -type "double3" 0.5 -1 -1 ;
	setAttr ".mxsl" -type "double3" 1.5 1 1 ;
	setAttr -l on ".spec_tempMod_vis" 1;
createNode nurbsCurve -n "c_Lf_spec_MShape" -p "c_Lf_spec_M";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 16;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		7.9865598672698184 2.7290395344158247 -2.1059666772288488e-017
		7.3009755246218626 3.0841509115139822 -2.1059666772288488e-017
		6.6153911819739122 2.7290395344158251 -2.1059666772288488e-017
		6.331412849098486 1.8717248316724677 -2.1059666772288488e-017
		6.6153911819739122 1.0144101289291094 -2.1059666772288488e-017
		7.3009755246218626 0.65929875183095343 -2.1059666772288488e-017
		7.9865598672698184 1.0144101289291092 -2.1059666772288488e-017
		8.2705382001452428 1.8717248316724668 -2.1059666772288488e-017
		7.9865598672698184 2.7290395344158247 -2.1059666772288488e-017
		7.3009755246218626 3.0841509115139822 -2.1059666772288488e-017
		6.6153911819739122 2.7290395344158251 -2.1059666772288488e-017
		;
createNode nurbsCurve -n "c_Lf_spec_MShapeOrig" -p "c_Lf_spec_M";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		6.4431776765251669 2.7290395344158247 -2.1059666772288241e-017
		5.7575933338772112 3.0841509115139822 -2.1059666772288241e-017
		5.0720089912292554 2.7290395344158251 -2.1059666772288241e-017
		4.7880306583538292 1.8717248316724677 -2.1059666772288241e-017
		5.0720089912292554 1.0144101289291094 -2.1059666772288241e-017
		5.7575933338772112 0.65929875183095343 -2.1059666772288241e-017
		6.443177676525166 1.0144101289291092 -2.1059666772288241e-017
		6.7271560094005896 1.8717248316724668 -2.1059666772288241e-017
		6.4431776765251669 2.7290395344158247 -2.1059666772288241e-017
		5.7575933338772112 3.0841509115139822 -2.1059666772288241e-017
		5.0720089912292554 2.7290395344158251 -2.1059666772288241e-017
		;
createNode nurbsCurve -n "c_Lf_eye_MShapeOrig" -p "c_Lf_eye_M";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		10.070826396877466 3.7414782532514548 -9.1908239759683886e-017
		7.0788108621166002 5.291249289072204 -9.1908239759683886e-017
		4.0867953273557385 3.7414782532514566 -9.1908239759683886e-017
		2.8474619140268018 5.962630571033457e-015 -9.1908239759683886e-017
		4.0867953273557376 -3.7414782532514477 -9.1908239759683886e-017
		7.0788108621166002 -5.2912492890721916 -9.1908239759683886e-017
		10.070826396877463 -3.741478253251449 -9.1908239759683886e-017
		11.310159810206393 2.1215047803886798e-015 -9.1908239759683886e-017
		10.070826396877466 3.7414782532514548 -9.1908239759683886e-017
		7.0788108621166002 5.291249289072204 -9.1908239759683886e-017
		4.0867953273557385 3.7414782532514566 -9.1908239759683886e-017
		;
createNode transform -n "Lf_eye_M_loc_GRP" -p "c_Lf_eye_M";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 5.0706044437764914 0 0 ;
createNode transform -n "Lf_eye_M_loc" -p "Lf_eye_M_loc_GRP";
	setAttr ".t" -type "double3" 0 0 7.1054273576010019e-015 ;
createNode locator -n "Lf_eye_M_locShape" -p "Lf_eye_M_loc";
	setAttr -k off ".v";
createNode transform -n "Rt_eye_M_GRP" -p "c_eye_M";
	setAttr ".t" -type "double3" -2.5 0 0 ;
	setAttr ".rp" -type "double3" -0.76756054849076027 3.3306690738754696e-016 8.8817841970012523e-016 ;
	setAttr ".sp" -type "double3" -0.76756054849076027 3.3306690738754696e-016 8.8817841970012523e-016 ;
createNode transform -n "GRP_c_Rt_eye_M_inOut" -p "Rt_eye_M_GRP";
	setAttr ".rp" -type "double3" -4.9236625107272154 7.1054273576010019e-015 0 ;
	setAttr ".sp" -type "double3" -4.9236625107272154 7.1054273576010019e-015 0 ;
createNode transform -n "c_Rt_eye_M" -p "GRP_c_Rt_eye_M_inOut";
	addAttr -ci true -sn "sign" -ln "sign" -dv 73 -at "long";
	addAttr -ci true -sn "translateWeight" -ln "translateWeight" -dv 1 -min 0 -max 1 
		-at "double";
	addAttr -ci true -sn "in_scale" -ln "in_scale" -at "double";
	addAttr -ci true -sn "out_scale" -ln "out_scale" -at "double";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" -4.4408920985006262e-016 0 0 ;
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -4.9236625107272145 6.2172489379008766e-015 -5.4394729040623414e-017 ;
	setAttr ".sp" -type "double3" -4.9236625107272145 6.2172489379008766e-015 -5.4394729040623414e-017 ;
	setAttr ".mnsl" -type "double3" 0.5 -1 -1 ;
	setAttr ".mxsl" -type "double3" 1.5 1 1 ;
	setAttr ".msxe" yes;
	setAttr ".xsxe" yes;
	setAttr -k on ".translateWeight";
	setAttr -cb on ".in_scale" 5;
	setAttr -cb on ".out_scale" 5;
createNode nurbsCurve -n "c_Rt_eye_MShape" -p "c_Rt_eye_M";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-7.9156780454880815 3.7414782532514548 -9.1908239759683886e-017
		-4.9236625107272127 5.291249289072204 -9.1908239759683886e-017
		-1.9316469759663528 3.7414782532514566 -9.1908239759683886e-017
		-0.69231356263741972 4.6822553074852011e-015 -9.1908239759683886e-017
		-1.9316469759663573 -3.7414782532514481 -9.1908239759683886e-017
		-4.9236625107272216 -5.2912492890721916 -9.1908239759683886e-017
		-7.9156780454880851 -3.7414782532514481 -9.1908239759683886e-017
		-9.1550114588170093 3.4018800439369353e-015 -9.1908239759683886e-017
		-7.9156780454880815 3.7414782532514548 -9.1908239759683886e-017
		-4.9236625107272127 5.291249289072204 -9.1908239759683886e-017
		-1.9316469759663528 3.7414782532514566 -9.1908239759683886e-017
		;
createNode transform -n "Rt_spec_tempMod_M_GRP" -p "c_Rt_eye_M";
	setAttr ".rp" -type "double3" -7.0788108621165975 1.1657341758564144e-015 -1.6881218321562939e-017 ;
	setAttr ".sp" -type "double3" -7.0788108621165975 1.1657341758564144e-015 -1.6881218321562939e-017 ;
createNode transform -n "c_Rt_spec_M" -p "Rt_spec_tempMod_M_GRP";
	addAttr -ci true -sn "sign" -ln "sign" -dv 73 -at "long";
	addAttr -ci true -sn "spec_tempMod_vis" -ln "spec_tempMod_vis" -min 0 -max 1 -en 
		"OFF:ON" -at "enum";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -2.6932914298818491 1.8717248316724677 -1.6881218321562905e-017 ;
	setAttr ".sp" -type "double3" -2.6932914298818491 1.8717248316724677 -1.6881218321562905e-017 ;
	setAttr ".mntl" -type "double3" -5 -5 -1 ;
	setAttr ".mxtl" -type "double3" 5 5 1 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".mnsl" -type "double3" 0.5 -1 -1 ;
	setAttr ".mxsl" -type "double3" 1.5 1 1 ;
	setAttr -l on ".spec_tempMod_vis" 1;
createNode nurbsCurve -n "c_Rt_spec_MShape" -p "c_Rt_spec_M";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 16;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-3.2428489841976953 2.5589397256108835 -1.6881218321562905e-017
		-2.6932914298818469 2.8435934549449637 -1.6881218321562905e-017
		-2.1437338755660047 2.5589397256108839 -1.6881218321562905e-017
		-1.916099683263794 1.8717248316724673 -1.6881218321562905e-017
		-2.1437338755660056 1.1845099377340507 -1.6881218321562905e-017
		-2.6932914298818487 0.8998562083999716 -1.6881218321562905e-017
		-3.2428489841976953 1.1845099377340507 -1.6881218321562905e-017
		-3.4704831764999042 1.8717248316724671 -1.6881218321562905e-017
		-3.2428489841976953 2.5589397256108835 -1.6881218321562905e-017
		-2.6932914298818469 2.8435934549449637 -1.6881218321562905e-017
		-2.1437338755660047 2.5589397256108839 -1.6881218321562905e-017
		;
createNode transform -n "Rt_eye_M_loc_GRP" -p "c_Rt_eye_M";
	setAttr ".v" no;
	setAttr ".t" -type "double3" -4.9236625107272145 0 0 ;
createNode transform -n "Rt_eye_M_loc" -p "Rt_eye_M_loc_GRP";
createNode locator -n "Rt_eye_M_locShape" -p "Rt_eye_M_loc";
	setAttr -k off ".v";
createNode nurbsCurve -n "EYE_RIGShape" -p "EYE_RIG";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		17.380362137855112 10.419236283121124 0.4221903658258373
		-17.380362137855112 10.419236283121124 0.4221903658258373
		-17.380362137855112 -10.419243727652569 0.42219036582583802
		17.380362137855112 -10.419243727652569 0.42219036582583802
		17.380362137855112 10.419236283121124 0.4221903658258373
		;
createNode expression -n "c_eye_M_inout_ex";
	setAttr -k on ".nds";
	setAttr -s 5 ".in";
	setAttr -s 5 ".in";
	setAttr -s 2 ".out";
	setAttr ".ixp" -type "string" ".O[0]=linstep(0,1,.I[0])*.I[1]  +  -linstep(0,1,-.I[0])*.I[2];\n.O[1]=linstep(0,1,.I[0])*-.I[3]  +  linstep(0,1,-.I[0])*.I[4];";
select -ne :time1;
	setAttr -av -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".o" 1;
	setAttr -av ".unw" 1;
lockNode -l 1 ;
select -ne :renderPartition;
	setAttr -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".st";
	setAttr -k on ".an";
	setAttr -k on ".pt";
lockNode -l 1 ;
select -ne :initialShadingGroup;
	setAttr -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".mwc";
	setAttr -k on ".an";
	setAttr -k on ".il";
	setAttr -k on ".vo";
	setAttr -k on ".eo";
	setAttr -k on ".fo";
	setAttr -k on ".epo";
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
	setAttr -k on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".mwc";
	setAttr -k on ".an";
	setAttr -k on ".il";
	setAttr -k on ".vo";
	setAttr -k on ".eo";
	setAttr -k on ".fo";
	setAttr -k on ".epo";
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
	setAttr -k on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".s";
lockNode -l 1 ;
select -ne :postProcessList1;
	setAttr -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".p";
lockNode -l 1 ;
select -ne :defaultRenderUtilityList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 4 ".u";
select -ne :defaultRenderingList1;
select -ne :renderGlobalsList1;
	setAttr -k on ".cch";
	setAttr -k on ".ihi";
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
	setAttr -k on ".be";
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
	setAttr -k on ".afp";
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
	setAttr -k on ".rlen";
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
	setAttr -av ".w" 640;
	setAttr -av ".h" 480;
	setAttr -av ".pa";
	setAttr -av -k on ".al";
	setAttr -av ".dar" 1.3333332538604736;
	setAttr -av ".ldar";
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
	setAttr ".ro" yes;
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
connectAttr "Lf_eyeballs_joint0.s" "Lf_eyeballs_joint1.is";
connectAttr "Rt_eyeballs_joint0.s" "Rt_eyeballs_joint1.is";
connectAttr "c_eye_M_inout_ex.out[0]" "GRP_c_Lf_eye_M_inOut.tx";
connectAttr "c_Lf_eye_M.sx" "c_Lf_eye_M.sy" -l on;
connectAttr "c_eye_M_inout_ex.out[1]" "GRP_c_Rt_eye_M_inOut.tx";
connectAttr "c_Rt_eye_M.sx" "c_Rt_eye_M.sy" -l on;
connectAttr "c_eye_M.in_out" "c_eye_M_inout_ex.in[0]";
connectAttr "c_Lf_eye_M.out_scale" "c_eye_M_inout_ex.in[1]";
connectAttr "c_Lf_eye_M.in_scale" "c_eye_M_inout_ex.in[2]";
connectAttr "c_Rt_eye_M.out_scale" "c_eye_M_inout_ex.in[3]";
connectAttr "c_Rt_eye_M.in_scale" "c_eye_M_inout_ex.in[4]";
connectAttr ":time1.o" "c_eye_M_inout_ex.tim";
// End of High_eyeballs_rig_02.ma

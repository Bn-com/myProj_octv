//Maya ASCII 2014 scene
//Name: High_pannel_rig.ma
//Last modified: Fri, Jul 31, 2015 02:52:30 PM
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
createNode transform -n "GRP_PANNEL_TEMPLATE";
createNode transform -n "Facial_CTRL_FRAME_GRP" -p "GRP_PANNEL_TEMPLATE";
createNode transform -n "Facial_CTRL_FRAME" -p "Facial_CTRL_FRAME_GRP";
createNode nurbsCurve -n "Facial_CTRL_FRAMEShape" -p "Facial_CTRL_FRAME";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		6.2806011045204553 3.3608238304060429 -6.0381691390884482e-016
		1.6903859157686987 3.1736958800233603 -5.6006954323441169e-016
		-2.1310543439250504 3.3608238304060452 -6.0381691390884521e-016
		-2.6878577543559428 1.1119197891412902e-015 -2.8964668496979557e-031
		-2.1310543439250522 -3.3608238304060438 6.0381691390884492e-016
		1.6903859157686982 -3.1736958800233608 5.6006954323441169e-016
		6.2806011045204473 -3.3608238304060452 6.0381691390884511e-016
		6.8374045149513414 -1.4123886715678515e-015 1.5126910812550344e-031
		6.2806011045204553 3.3608238304060429 -6.0381691390884482e-016
		1.6903859157686987 3.1736958800233603 -5.6006954323441169e-016
		-2.1310543439250504 3.3608238304060452 -6.0381691390884521e-016
		;
createNode transform -n "head_CTRL_GRP" -p "Facial_CTRL_FRAME";
	addAttr -ci true -sn "T1" -ln "T1" -at "double";
	addAttr -ci true -sn "T2" -ln "T2" -at "double";
	addAttr -ci true -sn "T3" -ln "T3" -at "double";
	addAttr -ci true -sn "R1" -ln "R1" -at "double";
	addAttr -ci true -sn "R2" -ln "R2" -at "double";
	addAttr -ci true -sn "R3" -ln "R3" -at "double";
	addAttr -ci true -sn "S1" -ln "S1" -at "double";
	addAttr -ci true -sn "S2" -ln "S2" -at "double";
	addAttr -ci true -sn "S3" -ln "S3" -at "double";
	setAttr -k on ".T1";
	setAttr -k on ".T2";
	setAttr -k on ".T3";
	setAttr -k on ".R1";
	setAttr -k on ".R2";
	setAttr -k on ".R3";
	setAttr -k on ".S1" 1;
	setAttr -k on ".S2" 1;
	setAttr -k on ".S3" 1;
createNode transform -n "head_CTRL" -p "head_CTRL_GRP";
	setAttr ".ove" yes;
	setAttr ".ovc" 14;
	setAttr ".rp" -type "double3" 0 0 0.017959868467468498 ;
	setAttr ".sp" -type "double3" 0 0 0.017959868467468498 ;
createNode nurbsCurve -n "head_CTRLShape" -p "head_CTRL";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		1.3557764736642783 1.2945716453810445 0.017959868467468977
		-1.4414673404478315e-016 1.8365536451903806 0.017959868467468876
		-1.3557764736642766 1.2945716453810452 0.017959868467468977
		-1.316742331423342 0.017959868467468939 0.017959868467468495
		-1.1489405355672566 -1.2424797041904747 0.017959868467469078
		-3.8070794296513517e-016 -1.8487909682882508 0.017959868467469192
		1.1489405355672559 -1.2424797041904754 0.017959868467469078
		1.316742331423342 0.017959868467467683 0.017959868467468495
		1.3557764736642783 1.2945716453810445 0.017959868467468977
		-1.4414673404478315e-016 1.8365536451903806 0.017959868467468876
		-1.3557764736642766 1.2945716453810452 0.017959868467468977
		;
createNode nurbsCurve -n "head_CTRLShape1Orig" -p "head_CTRL";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.89340767431903512 4.7982373409884682e-017 -1.0720129627227344
		-1.4414673404478315e-016 6.7857323231109134e-017 -1.5160552709222552
		-0.89340767431903423 4.7982373409884713e-017 -1.0720129627227351
		-1.2634692497501834 1.9663354616187859e-032 -4.3931488880507974e-016
		-0.89340767431903445 -4.7982373409884694e-017 1.0720129627227348
		-3.8070794296513517e-016 -6.7857323231109146e-017 1.5160552709222557
		0.89340767431903367 -4.7982373409884719e-017 1.0720129627227353
		1.2634692497501834 -3.6446300679047921e-032 8.1427624343361282e-016
		0.89340767431903512 4.7982373409884682e-017 -1.0720129627227344
		-1.4414673404478315e-016 6.7857323231109134e-017 -1.5160552709222552
		-0.89340767431903423 4.7982373409884713e-017 -1.0720129627227351
		;
createNode transform -n "c_eyebrows_GRP" -p "head_CTRL";
	setAttr ".rp" -type "double3" 0 0.017959868467468446 0.017959868467468498 ;
	setAttr ".sp" -type "double3" 0 0.017959868467468446 0.017959868467468498 ;
createNode transform -n "c_Lf_eyebrows_CTRL_GRP_GRP" -p "c_eyebrows_GRP";
	setAttr ".s" -type "double3" 0.2 0.2 0.2 ;
	setAttr ".rp" -type "double3" 0.56647208816660632 1.0030343002242577 0.008979934233734185 ;
	setAttr ".sp" -type "double3" 0.56647208816660632 1.0030343002242577 0.008979934233734185 ;
createNode transform -n "c_Lf_eyebrows_CTRL_GRP" -p "c_Lf_eyebrows_CTRL_GRP_GRP";
	addAttr -ci true -sn "T1" -ln "T1" -at "double";
	addAttr -ci true -sn "T2" -ln "T2" -at "double";
	addAttr -ci true -sn "T3" -ln "T3" -at "double";
	addAttr -ci true -sn "R1" -ln "R1" -at "double";
	addAttr -ci true -sn "R2" -ln "R2" -at "double";
	addAttr -ci true -sn "R3" -ln "R3" -at "double";
	addAttr -ci true -sn "S1" -ln "S1" -at "double";
	addAttr -ci true -sn "S2" -ln "S2" -at "double";
	addAttr -ci true -sn "S3" -ln "S3" -at "double";
	setAttr ".rp" -type "double3" 0.56647208816660632 1.0030343002242577 0.008979934233734185 ;
	setAttr ".sp" -type "double3" 0.56647208816660632 1.0030343002242577 0.008979934233734185 ;
	setAttr -k on ".T1";
	setAttr -k on ".T2";
	setAttr -k on ".T3";
	setAttr -k on ".R1";
	setAttr -k on ".R2";
	setAttr -k on ".R3";
	setAttr -k on ".S1" 1;
	setAttr -k on ".S2" 1;
	setAttr -k on ".S3" 1;
createNode transform -n "c_Lf_eyebrows_CTRL" -p "c_Lf_eyebrows_CTRL_GRP";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 0.56647208816660632 1.0235651538682387 0.017959868467468276 ;
	setAttr ".sp" -type "double3" 0.56647208816660632 1.0235651538682387 0.017959868467468276 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
createNode nurbsCurve -n "c_Lf_eyebrows_CTRLShape" -p "c_Lf_eyebrows_CTRL";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		2.3095768642801699 1.5555814434593696 0.017959868467468248
		0.56647208816660533 1.9707457739164809 0.017959868467468179
		-1.1766326879469584 1.5555814434593696 0.017959868467468248
		-1.8986503268505148 0.71567101171089176 0.017959868467468332
		-1.1766326879469589 -0.12423942003758477 0.017959868467468401
		0.56647208816660533 0.42849812841674223 0.017959868467468248
		2.3095768642801673 -0.12423942003758565 0.017959868467468401
		3.0315945031837286 0.71567101171089131 0.017959868467468332
		2.3095768642801699 1.5555814434593696 0.017959868467468248
		0.56647208816660533 1.9707457739164809 0.017959868467468179
		-1.1766326879469584 1.5555814434593696 0.017959868467468248
		;
createNode transform -n "GRP_c_Lf_eyebrows_01_FRAME" -p "c_Lf_eyebrows_CTRL";
	setAttr ".t" -type "double3" -0.75961854329786394 0.90652663106144526 -0.035919736934936365 ;
	setAttr ".s" -type "double3" 0.75 0.75 0.75 ;
createNode transform -n "c_Lf_eyebrows_01_FRAME" -p "GRP_c_Lf_eyebrows_01_FRAME";
	addAttr -ci true -sn "up" -ln "up" -min 0 -at "double";
	addAttr -ci true -sn "dn" -ln "dn" -min 0 -at "double";
	addAttr -ci true -sn "lf" -ln "lf" -min 0 -at "double";
	addAttr -ci true -sn "rt" -ln "rt" -min 0 -at "double";
	addAttr -ci true -sn "lfup" -ln "lfup" -min 0 -at "double";
	addAttr -ci true -sn "rtup" -ln "rtup" -min 0 -at "double";
	addAttr -ci true -sn "lfdn" -ln "lfdn" -min 0 -at "double";
	addAttr -ci true -sn "rtdn" -ln "rtdn" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_up" -ln "fourAxis_up" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_dn" -ln "fourAxis_dn" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_lf" -ln "fourAxis_lf" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_rt" -ln "fourAxis_rt" -min 0 -at "double";
	addAttr -ci true -sn "up_Vis" -ln "up_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "dn_Vis" -ln "dn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lf_Vis" -ln "lf_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lfup_Vis" -ln "lfup_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rt_Vis" -ln "rt_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rtup_Vis" -ln "rtup_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lfdn_Vis" -ln "lfdn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rtdn_Vis" -ln "rtdn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_up_Vis" -ln "fourAxis_up_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_dn_Vis" -ln "fourAxis_dn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_lf_Vis" -ln "fourAxis_lf_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_rt_Vis" -ln "fourAxis_rt_Vis" -min 0 -max 1 -at "bool";
	setAttr -k on ".up";
	setAttr -k on ".dn";
	setAttr -k on ".lf";
	setAttr -k on ".rt";
	setAttr -k on ".lfup";
	setAttr -k on ".rtup";
	setAttr -k on ".lfdn";
	setAttr -k on ".rtdn";
	setAttr -k on ".fourAxis_up";
	setAttr -k on ".fourAxis_dn";
	setAttr -k on ".fourAxis_lf";
	setAttr -k on ".fourAxis_rt";
	setAttr -cb on ".up_Vis";
	setAttr -cb on ".dn_Vis";
	setAttr -cb on ".lf_Vis";
	setAttr -cb on ".lfup_Vis";
	setAttr -cb on ".rt_Vis";
	setAttr -cb on ".rtup_Vis";
	setAttr -cb on ".lfdn_Vis";
	setAttr -cb on ".rtdn_Vis";
	setAttr -cb on ".fourAxis_up_Vis";
	setAttr -cb on ".fourAxis_dn_Vis";
	setAttr -cb on ".fourAxis_lf_Vis";
	setAttr -cb on ".fourAxis_rt_Vis";
createNode nurbsCurve -n "c_Lf_eyebrows_01_FRAMEShape" -p "c_Lf_eyebrows_01_FRAME";
	setAttr -k off ".v" no;
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode transform -n "GRP_c_Lf_eyebrows_01_CTRL" -p "c_Lf_eyebrows_01_FRAME";
createNode transform -n "c_Lf_eyebrows_01_CTRL" -p "GRP_c_Lf_eyebrows_01_CTRL";
	addAttr -ci true -sn "frameSelectAble" -ln "frameSelectAble" -min 0 -max 2 -en 
		"normal:template:reference" -at "enum";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".mntl" -type "double3" -1 -1 0 ;
	setAttr ".mxtl" -type "double3" 1 1 0 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
	setAttr ".frameSelectAble" 2;
createNode nurbsCurve -n "c_Lf_eyebrows_01_CTRLShape" -p "c_Lf_eyebrows_01_CTRL";
	setAttr -k off ".v" no;
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		1 32 0 no 3
		33 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32
		33
		-0.050000000000000003 0.050000000000000003 0
		-0.050000000000000003 0.15000000000000002 0
		-0.10000000000000001 0.15000000000000002 0
		0 0.25 0
		0.10000000000000001 0.15000000000000002 0
		0.050000000000000003 0.15000000000000002 0
		0.050000000000000003 0.050000000000000003 0
		0.20000000000000001 0.20000000000000001 0
		0.050000000000000003 0.050000000000000003 0
		0.15000000000000002 0.050000000000000003 0
		0.15000000000000002 0.10000000000000001 0
		0.25 0 0
		0.15000000000000002 -0.10000000000000001 0
		0.15000000000000002 -0.050000000000000003 0
		0.050000000000000003 -0.050000000000000003 0
		0.20000000000000001 -0.20000000000000001 0
		0.050000000000000003 -0.050000000000000003 0
		0.050000000000000003 -0.15000000000000002 0
		0.10000000000000001 -0.15000000000000002 0
		0 -0.25 0
		-0.10000000000000001 -0.15000000000000002 0
		-0.050000000000000003 -0.15000000000000002 0
		-0.050000000000000003 -0.050000000000000003 0
		-0.20000000000000001 -0.20000000000000001 0
		-0.050000000000000003 -0.050000000000000003 0
		-0.15000000000000002 -0.050000000000000003 0
		-0.15000000000000002 -0.10000000000000001 0
		-0.25 0 0
		-0.15000000000000002 0.10000000000000001 0
		-0.15000000000000002 0.050000000000000003 0
		-0.050000000000000003 0.050000000000000003 0
		-0.20000000000000001 0.20000000000000001 0
		-0.050000000000000003 0.050000000000000003 0
		;
createNode nurbsCurve -n "c_eyebrows_CTRLShape" -p "c_Lf_eyebrows_01_CTRL";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.44716383209654365 0.44716383209654292 -1.6398277419807286e-017
		-7.2147584840030067e-017 0.63238515595365707 -4.6184138029578972e-017
		-0.44716383209654315 0.4471638320965432 -1.6398277419807335e-017
		-0.63238515595365707 2.3135938565234901e-016 5.5511151231257784e-017
		-0.44716383209654331 -0.44716383209654298 1.2742057988232296e-016
		-1.9054998919238081e-016 -0.63238515595365719 1.5720644049209471e-016
		0.44716383209654287 -0.44716383209654315 1.2742057988232296e-016
		0.63238515595365707 -2.9154531239380831e-016 5.5511151231257876e-017
		0.44716383209654365 0.44716383209654292 -1.6398277419807286e-017
		-7.2147584840030067e-017 0.63238515595365707 -4.6184138029578972e-017
		-0.44716383209654315 0.4471638320965432 -1.6398277419807335e-017
		;
createNode transform -n "c_Lf_eyebrows_01_FRAME_lockzy" -p "c_Lf_eyebrows_01_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Lf_eyebrows_01_FRAME_lockzyShape" -p "c_Lf_eyebrows_01_FRAME_lockzy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 0.20000000000000001 0
		-1 -1 0
		1 -1 0
		1 0.20000000000000001 0
		-1 0.20000000000000001 0
		;
createNode transform -n "c_Lf_eyebrows_01_FRAME_lockfy" -p "c_Lf_eyebrows_01_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Lf_eyebrows_01_FRAME_lockfyShape" -p "c_Lf_eyebrows_01_FRAME_lockfy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -0.20000000000000001 0
		1 -0.20000000000000001 0
		1 1 0
		-1 1 0
		;
createNode transform -n "c_Lf_eyebrows_01_FRAME_lockzx" -p "c_Lf_eyebrows_01_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Lf_eyebrows_01_FRAME_lockzxShape" -p "c_Lf_eyebrows_01_FRAME_lockzx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		0.20000000000000001 -1 0
		0.20000000000000001 1 0
		-1 1 0
		;
createNode transform -n "c_Lf_eyebrows_01_FRAME_lockfx" -p "c_Lf_eyebrows_01_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Lf_eyebrows_01_FRAME_lockfxShape" -p "c_Lf_eyebrows_01_FRAME_lockfx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 1 0
		-0.20000000000000001 -1 0
		1 -1 0
		1 1 0
		-0.20000000000000001 1 0
		;
createNode transform -n "c_Lf_eyebrows_01_FRAME_lockzyfy" -p "c_Lf_eyebrows_01_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Lf_eyebrows_01_FRAME_lockzyfyShape" -p "c_Lf_eyebrows_01_FRAME_lockzyfy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 0.20000000000000001 0
		-1 -0.20000000000000001 0
		1 -0.20000000000000001 0
		1 0.20000000000000001 0
		-1 0.20000000000000001 0
		;
createNode transform -n "c_Lf_eyebrows_01_FRAME_lockzxfx" -p "c_Lf_eyebrows_01_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Lf_eyebrows_01_FRAME_lockzxfxShape" -p "c_Lf_eyebrows_01_FRAME_lockzxfx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 1 0
		-0.20000000000000001 -1 0
		0.20000000000000001 -1 0
		0.20000000000000001 1 0
		-0.20000000000000001 1 0
		;
createNode transform -n "c_Lf_eyebrows_01_FRAME_lockzyfyzx" -p "c_Lf_eyebrows_01_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Lf_eyebrows_01_FRAME_lockzyfyzxShape" -p "c_Lf_eyebrows_01_FRAME_lockzyfyzx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 0.20000000000000001 0
		-1 -0.20000000000000001 0
		0.20000000000000001 -0.20000000000000001 0
		0.20000000000000001 0.20000000000000001 0
		-1 0.20000000000000001 0
		;
createNode transform -n "c_Lf_eyebrows_01_FRAME_lockzyfyfx" -p "c_Lf_eyebrows_01_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Lf_eyebrows_01_FRAME_lockzyfyfxShape" -p "c_Lf_eyebrows_01_FRAME_lockzyfyfx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 0.20000000000000001 0
		-0.20000000000000001 -0.20000000000000001 0
		1 -0.20000000000000001 0
		1 0.20000000000000001 0
		-0.20000000000000001 0.20000000000000001 0
		;
createNode transform -n "c_Lf_eyebrows_01_FRAME_lockzxfxzy" -p "c_Lf_eyebrows_01_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Lf_eyebrows_01_FRAME_lockzxfxzyShape" -p "c_Lf_eyebrows_01_FRAME_lockzxfxzy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 0.20000000000000001 0
		-0.20000000000000001 -1 0
		0.20000000000000001 -1 0
		0.20000000000000001 0.20000000000000001 0
		-0.20000000000000001 0.20000000000000001 0
		;
createNode transform -n "c_Lf_eyebrows_01_FRAME_lockzxfxfy" -p "c_Lf_eyebrows_01_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Lf_eyebrows_01_FRAME_lockzxfxfyShape" -p "c_Lf_eyebrows_01_FRAME_lockzxfxfy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 1 0
		-0.20000000000000001 -0.20000000000000001 0
		0.20000000000000001 -0.20000000000000001 0
		0.20000000000000001 1 0
		-0.20000000000000001 1 0
		;
createNode transform -n "c_Lf_eyebrows_01_CTRL_up" -p "c_Lf_eyebrows_01_FRAME";
	setAttr ".t" -type "double3" 0 2.2 0 ;
createNode nurbsCurve -n "curveShape1" -p "c_Lf_eyebrows_01_CTRL_up";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_eyebrows_01_LOC_up" -p "c_Lf_eyebrows_01_CTRL_up";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_eyebrows_01_CTRL_dn" -p "c_Lf_eyebrows_01_FRAME";
	setAttr ".t" -type "double3" 0 -2.2 0 ;
createNode nurbsCurve -n "curveShape2" -p "c_Lf_eyebrows_01_CTRL_dn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_eyebrows_01_LOC_dn" -p "c_Lf_eyebrows_01_CTRL_dn";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_eyebrows_01_CTRL_lf" -p "c_Lf_eyebrows_01_FRAME";
	setAttr ".t" -type "double3" -2.2 0 0 ;
createNode nurbsCurve -n "curveShape3" -p "c_Lf_eyebrows_01_CTRL_lf";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_eyebrows_01_LOC_lf" -p "c_Lf_eyebrows_01_CTRL_lf";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_eyebrows_01_CTRL_lfup" -p "c_Lf_eyebrows_01_FRAME";
	setAttr ".t" -type "double3" -2.2 2.2 0 ;
createNode nurbsCurve -n "curveShape4" -p "c_Lf_eyebrows_01_CTRL_lfup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_eyebrows_01_LOC_lfup" -p "c_Lf_eyebrows_01_CTRL_lfup";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_eyebrows_01_CTRL_rt" -p "c_Lf_eyebrows_01_FRAME";
	setAttr ".t" -type "double3" 2.2 0 0 ;
createNode nurbsCurve -n "curveShape5" -p "c_Lf_eyebrows_01_CTRL_rt";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_eyebrows_01_LOC_rt" -p "c_Lf_eyebrows_01_CTRL_rt";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_eyebrows_01_CTRL_rtup" -p "c_Lf_eyebrows_01_FRAME";
	setAttr ".t" -type "double3" 2.2 2.2 0 ;
createNode nurbsCurve -n "curveShape6" -p "c_Lf_eyebrows_01_CTRL_rtup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_eyebrows_01_LOC_rtup" -p "c_Lf_eyebrows_01_CTRL_rtup";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_eyebrows_01_CTRL_lfdn" -p "c_Lf_eyebrows_01_FRAME";
	setAttr ".t" -type "double3" -2.2 -2.2 0 ;
createNode nurbsCurve -n "curveShape7" -p "c_Lf_eyebrows_01_CTRL_lfdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_eyebrows_01_LOC_lfdn" -p "c_Lf_eyebrows_01_CTRL_lfdn";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_eyebrows_01_CTRL_rtdn" -p "c_Lf_eyebrows_01_FRAME";
	setAttr ".t" -type "double3" 2.2 -2.2 0 ;
createNode nurbsCurve -n "curveShape8" -p "c_Lf_eyebrows_01_CTRL_rtdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_eyebrows_01_LOC_rtdn" -p "c_Lf_eyebrows_01_CTRL_rtdn";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_eyebrows_01_CTRL_fourAxisup" -p "c_Lf_eyebrows_01_FRAME";
	setAttr ".t" -type "double3" 0 4.4 0 ;
createNode nurbsCurve -n "curveShape9" -p "c_Lf_eyebrows_01_CTRL_fourAxisup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_eyebrows_01_LOC_fourAxis_up" -p "c_Lf_eyebrows_01_CTRL_fourAxisup";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_eyebrows_01_CTRL_fourAxisdn" -p "c_Lf_eyebrows_01_FRAME";
	setAttr ".t" -type "double3" 0 -4.4 0 ;
createNode nurbsCurve -n "curveShape10" -p "c_Lf_eyebrows_01_CTRL_fourAxisdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_eyebrows_01_LOC_fourAxis_dn" -p "c_Lf_eyebrows_01_CTRL_fourAxisdn";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_eyebrows_01_CTRL_fourAxislf" -p "c_Lf_eyebrows_01_FRAME";
	setAttr ".t" -type "double3" -4.4 0 0 ;
createNode nurbsCurve -n "curveShape11" -p "c_Lf_eyebrows_01_CTRL_fourAxislf";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_eyebrows_01_LOC_fourAxis_lf" -p "c_Lf_eyebrows_01_CTRL_fourAxislf";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_eyebrows_01_CTRL_fourAxisrt" -p "c_Lf_eyebrows_01_FRAME";
	setAttr ".t" -type "double3" 4.4 0 0 ;
createNode nurbsCurve -n "curveShape12" -p "c_Lf_eyebrows_01_CTRL_fourAxisrt";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_eyebrows_01_LOC_fourAxis_rt" -p "c_Lf_eyebrows_01_CTRL_fourAxisrt";
	setAttr -k off ".v" no;
createNode transform -n "GRP_c_Lf_eyebrows_02_FRAME" -p "c_Lf_eyebrows_CTRL";
	setAttr ".t" -type "double3" 0.65040064769661221 1.1030448881591202 -0.035919736934936365 ;
	setAttr ".s" -type "double3" 0.75 0.75 0.75 ;
createNode transform -n "c_Lf_eyebrows_02_FRAME" -p "GRP_c_Lf_eyebrows_02_FRAME";
	addAttr -ci true -sn "up" -ln "up" -min 0 -at "double";
	addAttr -ci true -sn "dn" -ln "dn" -min 0 -at "double";
	addAttr -ci true -sn "lf" -ln "lf" -min 0 -at "double";
	addAttr -ci true -sn "rt" -ln "rt" -min 0 -at "double";
	addAttr -ci true -sn "lfup" -ln "lfup" -min 0 -at "double";
	addAttr -ci true -sn "rtup" -ln "rtup" -min 0 -at "double";
	addAttr -ci true -sn "lfdn" -ln "lfdn" -min 0 -at "double";
	addAttr -ci true -sn "rtdn" -ln "rtdn" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_up" -ln "fourAxis_up" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_dn" -ln "fourAxis_dn" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_lf" -ln "fourAxis_lf" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_rt" -ln "fourAxis_rt" -min 0 -at "double";
	addAttr -ci true -sn "up_Vis" -ln "up_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "dn_Vis" -ln "dn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lf_Vis" -ln "lf_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lfup_Vis" -ln "lfup_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rt_Vis" -ln "rt_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rtup_Vis" -ln "rtup_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lfdn_Vis" -ln "lfdn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rtdn_Vis" -ln "rtdn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_up_Vis" -ln "fourAxis_up_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_dn_Vis" -ln "fourAxis_dn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_lf_Vis" -ln "fourAxis_lf_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_rt_Vis" -ln "fourAxis_rt_Vis" -min 0 -max 1 -at "bool";
	setAttr -k on ".up";
	setAttr -k on ".dn";
	setAttr -k on ".lf";
	setAttr -k on ".rt";
	setAttr -k on ".lfup";
	setAttr -k on ".rtup";
	setAttr -k on ".lfdn";
	setAttr -k on ".rtdn";
	setAttr -k on ".fourAxis_up";
	setAttr -k on ".fourAxis_dn";
	setAttr -k on ".fourAxis_lf";
	setAttr -k on ".fourAxis_rt";
	setAttr -cb on ".up_Vis";
	setAttr -cb on ".dn_Vis";
	setAttr -cb on ".lf_Vis";
	setAttr -cb on ".lfup_Vis";
	setAttr -cb on ".rt_Vis";
	setAttr -cb on ".rtup_Vis";
	setAttr -cb on ".lfdn_Vis";
	setAttr -cb on ".rtdn_Vis";
	setAttr -cb on ".fourAxis_up_Vis";
	setAttr -cb on ".fourAxis_dn_Vis";
	setAttr -cb on ".fourAxis_lf_Vis";
	setAttr -cb on ".fourAxis_rt_Vis";
createNode nurbsCurve -n "c_Lf_eyebrows_02_FRAMEShape" -p "c_Lf_eyebrows_02_FRAME";
	setAttr -k off ".v" no;
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode transform -n "GRP_c_Lf_eyebrows_02_CTRL" -p "c_Lf_eyebrows_02_FRAME";
createNode transform -n "c_Lf_eyebrows_02_CTRL" -p "GRP_c_Lf_eyebrows_02_CTRL";
	addAttr -ci true -sn "frameSelectAble" -ln "frameSelectAble" -min 0 -max 2 -en 
		"normal:template:reference" -at "enum";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".mntl" -type "double3" -1 -1 0 ;
	setAttr ".mxtl" -type "double3" 1 1 0 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
	setAttr ".frameSelectAble" 2;
createNode nurbsCurve -n "c_Lf_eyebrows_02_CTRLShape" -p "c_Lf_eyebrows_02_CTRL";
	setAttr -k off ".v" no;
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		1 32 0 no 3
		33 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32
		33
		-0.050000000000000003 0.050000000000000003 0
		-0.050000000000000003 0.15000000000000002 0
		-0.10000000000000001 0.15000000000000002 0
		0 0.25 0
		0.10000000000000001 0.15000000000000002 0
		0.050000000000000003 0.15000000000000002 0
		0.050000000000000003 0.050000000000000003 0
		0.20000000000000001 0.20000000000000001 0
		0.050000000000000003 0.050000000000000003 0
		0.15000000000000002 0.050000000000000003 0
		0.15000000000000002 0.10000000000000001 0
		0.25 0 0
		0.15000000000000002 -0.10000000000000001 0
		0.15000000000000002 -0.050000000000000003 0
		0.050000000000000003 -0.050000000000000003 0
		0.20000000000000001 -0.20000000000000001 0
		0.050000000000000003 -0.050000000000000003 0
		0.050000000000000003 -0.15000000000000002 0
		0.10000000000000001 -0.15000000000000002 0
		0 -0.25 0
		-0.10000000000000001 -0.15000000000000002 0
		-0.050000000000000003 -0.15000000000000002 0
		-0.050000000000000003 -0.050000000000000003 0
		-0.20000000000000001 -0.20000000000000001 0
		-0.050000000000000003 -0.050000000000000003 0
		-0.15000000000000002 -0.050000000000000003 0
		-0.15000000000000002 -0.10000000000000001 0
		-0.25 0 0
		-0.15000000000000002 0.10000000000000001 0
		-0.15000000000000002 0.050000000000000003 0
		-0.050000000000000003 0.050000000000000003 0
		-0.20000000000000001 0.20000000000000001 0
		-0.050000000000000003 0.050000000000000003 0
		;
createNode transform -n "c_Lf_eyebrows_02_FRAME_lockzy" -p "c_Lf_eyebrows_02_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Lf_eyebrows_02_FRAME_lockzyShape" -p "c_Lf_eyebrows_02_FRAME_lockzy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 0.20000000000000001 0
		-1 -1 0
		1 -1 0
		1 0.20000000000000001 0
		-1 0.20000000000000001 0
		;
createNode transform -n "c_Lf_eyebrows_02_FRAME_lockfy" -p "c_Lf_eyebrows_02_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Lf_eyebrows_02_FRAME_lockfyShape" -p "c_Lf_eyebrows_02_FRAME_lockfy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -0.20000000000000001 0
		1 -0.20000000000000001 0
		1 1 0
		-1 1 0
		;
createNode transform -n "c_Lf_eyebrows_02_FRAME_lockzx" -p "c_Lf_eyebrows_02_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Lf_eyebrows_02_FRAME_lockzxShape" -p "c_Lf_eyebrows_02_FRAME_lockzx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		0.20000000000000001 -1 0
		0.20000000000000001 1 0
		-1 1 0
		;
createNode transform -n "c_Lf_eyebrows_02_FRAME_lockfx" -p "c_Lf_eyebrows_02_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Lf_eyebrows_02_FRAME_lockfxShape" -p "c_Lf_eyebrows_02_FRAME_lockfx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 1 0
		-0.20000000000000001 -1 0
		1 -1 0
		1 1 0
		-0.20000000000000001 1 0
		;
createNode transform -n "c_Lf_eyebrows_02_FRAME_lockzyfy" -p "c_Lf_eyebrows_02_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Lf_eyebrows_02_FRAME_lockzyfyShape" -p "c_Lf_eyebrows_02_FRAME_lockzyfy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 0.20000000000000001 0
		-1 -0.20000000000000001 0
		1 -0.20000000000000001 0
		1 0.20000000000000001 0
		-1 0.20000000000000001 0
		;
createNode transform -n "c_Lf_eyebrows_02_FRAME_lockzxfx" -p "c_Lf_eyebrows_02_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Lf_eyebrows_02_FRAME_lockzxfxShape" -p "c_Lf_eyebrows_02_FRAME_lockzxfx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 1 0
		-0.20000000000000001 -1 0
		0.20000000000000001 -1 0
		0.20000000000000001 1 0
		-0.20000000000000001 1 0
		;
createNode transform -n "c_Lf_eyebrows_02_FRAME_lockzyfyzx" -p "c_Lf_eyebrows_02_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Lf_eyebrows_02_FRAME_lockzyfyzxShape" -p "c_Lf_eyebrows_02_FRAME_lockzyfyzx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 0.20000000000000001 0
		-1 -0.20000000000000001 0
		0.20000000000000001 -0.20000000000000001 0
		0.20000000000000001 0.20000000000000001 0
		-1 0.20000000000000001 0
		;
createNode transform -n "c_Lf_eyebrows_02_FRAME_lockzyfyfx" -p "c_Lf_eyebrows_02_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Lf_eyebrows_02_FRAME_lockzyfyfxShape" -p "c_Lf_eyebrows_02_FRAME_lockzyfyfx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 0.20000000000000001 0
		-0.20000000000000001 -0.20000000000000001 0
		1 -0.20000000000000001 0
		1 0.20000000000000001 0
		-0.20000000000000001 0.20000000000000001 0
		;
createNode transform -n "c_Lf_eyebrows_02_FRAME_lockzxfxzy" -p "c_Lf_eyebrows_02_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Lf_eyebrows_02_FRAME_lockzxfxzyShape" -p "c_Lf_eyebrows_02_FRAME_lockzxfxzy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 0.20000000000000001 0
		-0.20000000000000001 -1 0
		0.20000000000000001 -1 0
		0.20000000000000001 0.20000000000000001 0
		-0.20000000000000001 0.20000000000000001 0
		;
createNode transform -n "c_Lf_eyebrows_02_FRAME_lockzxfxfy" -p "c_Lf_eyebrows_02_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Lf_eyebrows_02_FRAME_lockzxfxfyShape" -p "c_Lf_eyebrows_02_FRAME_lockzxfxfy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 1 0
		-0.20000000000000001 -0.20000000000000001 0
		0.20000000000000001 -0.20000000000000001 0
		0.20000000000000001 1 0
		-0.20000000000000001 1 0
		;
createNode transform -n "c_Lf_eyebrows_02_CTRL_up" -p "c_Lf_eyebrows_02_FRAME";
	setAttr ".t" -type "double3" 0 2.2 0 ;
createNode nurbsCurve -n "curveShape13" -p "c_Lf_eyebrows_02_CTRL_up";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_eyebrows_02_LOC_up" -p "c_Lf_eyebrows_02_CTRL_up";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_eyebrows_02_CTRL_dn" -p "c_Lf_eyebrows_02_FRAME";
	setAttr ".t" -type "double3" 0 -2.2 0 ;
createNode nurbsCurve -n "curveShape14" -p "c_Lf_eyebrows_02_CTRL_dn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_eyebrows_02_LOC_dn" -p "c_Lf_eyebrows_02_CTRL_dn";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_eyebrows_02_CTRL_lf" -p "c_Lf_eyebrows_02_FRAME";
	setAttr ".t" -type "double3" -2.2 0 0 ;
createNode nurbsCurve -n "curveShape15" -p "c_Lf_eyebrows_02_CTRL_lf";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_eyebrows_02_LOC_lf" -p "c_Lf_eyebrows_02_CTRL_lf";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_eyebrows_02_CTRL_lfup" -p "c_Lf_eyebrows_02_FRAME";
	setAttr ".t" -type "double3" -2.2 2.2 0 ;
createNode nurbsCurve -n "curveShape16" -p "c_Lf_eyebrows_02_CTRL_lfup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_eyebrows_02_LOC_lfup" -p "c_Lf_eyebrows_02_CTRL_lfup";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_eyebrows_02_CTRL_rt" -p "c_Lf_eyebrows_02_FRAME";
	setAttr ".t" -type "double3" 2.2 0 0 ;
createNode nurbsCurve -n "curveShape17" -p "c_Lf_eyebrows_02_CTRL_rt";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_eyebrows_02_LOC_rt" -p "c_Lf_eyebrows_02_CTRL_rt";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_eyebrows_02_CTRL_rtup" -p "c_Lf_eyebrows_02_FRAME";
	setAttr ".t" -type "double3" 2.2 2.2 0 ;
createNode nurbsCurve -n "curveShape18" -p "c_Lf_eyebrows_02_CTRL_rtup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_eyebrows_02_LOC_rtup" -p "c_Lf_eyebrows_02_CTRL_rtup";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_eyebrows_02_CTRL_lfdn" -p "c_Lf_eyebrows_02_FRAME";
	setAttr ".t" -type "double3" -2.2 -2.2 0 ;
createNode nurbsCurve -n "curveShape19" -p "c_Lf_eyebrows_02_CTRL_lfdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_eyebrows_02_LOC_lfdn" -p "c_Lf_eyebrows_02_CTRL_lfdn";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_eyebrows_02_CTRL_rtdn" -p "c_Lf_eyebrows_02_FRAME";
	setAttr ".t" -type "double3" 2.2 -2.2 0 ;
createNode nurbsCurve -n "curveShape20" -p "c_Lf_eyebrows_02_CTRL_rtdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_eyebrows_02_LOC_rtdn" -p "c_Lf_eyebrows_02_CTRL_rtdn";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_eyebrows_02_CTRL_fourAxisup" -p "c_Lf_eyebrows_02_FRAME";
	setAttr ".t" -type "double3" 0 4.4 0 ;
createNode nurbsCurve -n "curveShape21" -p "c_Lf_eyebrows_02_CTRL_fourAxisup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_eyebrows_02_LOC_fourAxis_up" -p "c_Lf_eyebrows_02_CTRL_fourAxisup";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_eyebrows_02_CTRL_fourAxisdn" -p "c_Lf_eyebrows_02_FRAME";
	setAttr ".t" -type "double3" 0 -4.4 0 ;
createNode nurbsCurve -n "curveShape22" -p "c_Lf_eyebrows_02_CTRL_fourAxisdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_eyebrows_02_LOC_fourAxis_dn" -p "c_Lf_eyebrows_02_CTRL_fourAxisdn";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_eyebrows_02_CTRL_fourAxislf" -p "c_Lf_eyebrows_02_FRAME";
	setAttr ".t" -type "double3" -4.4 0 0 ;
createNode nurbsCurve -n "curveShape23" -p "c_Lf_eyebrows_02_CTRL_fourAxislf";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_eyebrows_02_LOC_fourAxis_lf" -p "c_Lf_eyebrows_02_CTRL_fourAxislf";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_eyebrows_02_CTRL_fourAxisrt" -p "c_Lf_eyebrows_02_FRAME";
	setAttr ".t" -type "double3" 4.4 0 0 ;
createNode nurbsCurve -n "curveShape24" -p "c_Lf_eyebrows_02_CTRL_fourAxisrt";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_eyebrows_02_LOC_fourAxis_rt" -p "c_Lf_eyebrows_02_CTRL_fourAxisrt";
	setAttr -k off ".v" no;
createNode transform -n "GRP_c_Lf_eyebrows_03_FRAME" -p "c_Lf_eyebrows_CTRL";
	setAttr ".t" -type "double3" 2.0238998834895607 0.8410926054128316 -0.035919736934936365 ;
	setAttr ".s" -type "double3" 0.75 0.75 0.75 ;
createNode transform -n "c_Lf_eyebrows_03_FRAME" -p "GRP_c_Lf_eyebrows_03_FRAME";
	addAttr -ci true -sn "up" -ln "up" -min 0 -at "double";
	addAttr -ci true -sn "dn" -ln "dn" -min 0 -at "double";
	addAttr -ci true -sn "lf" -ln "lf" -min 0 -at "double";
	addAttr -ci true -sn "rt" -ln "rt" -min 0 -at "double";
	addAttr -ci true -sn "lfup" -ln "lfup" -min 0 -at "double";
	addAttr -ci true -sn "rtup" -ln "rtup" -min 0 -at "double";
	addAttr -ci true -sn "lfdn" -ln "lfdn" -min 0 -at "double";
	addAttr -ci true -sn "rtdn" -ln "rtdn" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_up" -ln "fourAxis_up" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_dn" -ln "fourAxis_dn" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_lf" -ln "fourAxis_lf" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_rt" -ln "fourAxis_rt" -min 0 -at "double";
	addAttr -ci true -sn "up_Vis" -ln "up_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "dn_Vis" -ln "dn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lf_Vis" -ln "lf_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lfup_Vis" -ln "lfup_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rt_Vis" -ln "rt_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rtup_Vis" -ln "rtup_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lfdn_Vis" -ln "lfdn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rtdn_Vis" -ln "rtdn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_up_Vis" -ln "fourAxis_up_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_dn_Vis" -ln "fourAxis_dn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_lf_Vis" -ln "fourAxis_lf_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_rt_Vis" -ln "fourAxis_rt_Vis" -min 0 -max 1 -at "bool";
	setAttr -k on ".up";
	setAttr -k on ".dn";
	setAttr -k on ".lf";
	setAttr -k on ".rt";
	setAttr -k on ".lfup";
	setAttr -k on ".rtup";
	setAttr -k on ".lfdn";
	setAttr -k on ".rtdn";
	setAttr -k on ".fourAxis_up";
	setAttr -k on ".fourAxis_dn";
	setAttr -k on ".fourAxis_lf";
	setAttr -k on ".fourAxis_rt";
	setAttr -cb on ".up_Vis";
	setAttr -cb on ".dn_Vis";
	setAttr -cb on ".lf_Vis";
	setAttr -cb on ".lfup_Vis";
	setAttr -cb on ".rt_Vis";
	setAttr -cb on ".rtup_Vis";
	setAttr -cb on ".lfdn_Vis";
	setAttr -cb on ".rtdn_Vis";
	setAttr -cb on ".fourAxis_up_Vis";
	setAttr -cb on ".fourAxis_dn_Vis";
	setAttr -cb on ".fourAxis_lf_Vis";
	setAttr -cb on ".fourAxis_rt_Vis";
createNode nurbsCurve -n "c_Lf_eyebrows_03_FRAMEShape" -p "c_Lf_eyebrows_03_FRAME";
	setAttr -k off ".v" no;
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode transform -n "GRP_c_Lf_eyebrows_03_CTRL" -p "c_Lf_eyebrows_03_FRAME";
createNode transform -n "c_Lf_eyebrows_03_CTRL" -p "GRP_c_Lf_eyebrows_03_CTRL";
	addAttr -ci true -sn "frameSelectAble" -ln "frameSelectAble" -min 0 -max 2 -en 
		"normal:template:reference" -at "enum";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".mntl" -type "double3" -1 -1 0 ;
	setAttr ".mxtl" -type "double3" 1 1 0 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
	setAttr ".frameSelectAble" 2;
createNode nurbsCurve -n "c_Lf_eyebrows_03_CTRLShape" -p "c_Lf_eyebrows_03_CTRL";
	setAttr -k off ".v" no;
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		1 32 0 no 3
		33 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32
		33
		-0.050000000000000003 0.050000000000000003 0
		-0.050000000000000003 0.15000000000000002 0
		-0.10000000000000001 0.15000000000000002 0
		0 0.25 0
		0.10000000000000001 0.15000000000000002 0
		0.050000000000000003 0.15000000000000002 0
		0.050000000000000003 0.050000000000000003 0
		0.20000000000000001 0.20000000000000001 0
		0.050000000000000003 0.050000000000000003 0
		0.15000000000000002 0.050000000000000003 0
		0.15000000000000002 0.10000000000000001 0
		0.25 0 0
		0.15000000000000002 -0.10000000000000001 0
		0.15000000000000002 -0.050000000000000003 0
		0.050000000000000003 -0.050000000000000003 0
		0.20000000000000001 -0.20000000000000001 0
		0.050000000000000003 -0.050000000000000003 0
		0.050000000000000003 -0.15000000000000002 0
		0.10000000000000001 -0.15000000000000002 0
		0 -0.25 0
		-0.10000000000000001 -0.15000000000000002 0
		-0.050000000000000003 -0.15000000000000002 0
		-0.050000000000000003 -0.050000000000000003 0
		-0.20000000000000001 -0.20000000000000001 0
		-0.050000000000000003 -0.050000000000000003 0
		-0.15000000000000002 -0.050000000000000003 0
		-0.15000000000000002 -0.10000000000000001 0
		-0.25 0 0
		-0.15000000000000002 0.10000000000000001 0
		-0.15000000000000002 0.050000000000000003 0
		-0.050000000000000003 0.050000000000000003 0
		-0.20000000000000001 0.20000000000000001 0
		-0.050000000000000003 0.050000000000000003 0
		;
createNode transform -n "c_Lf_eyebrows_03_FRAME_lockzy" -p "c_Lf_eyebrows_03_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Lf_eyebrows_03_FRAME_lockzyShape" -p "c_Lf_eyebrows_03_FRAME_lockzy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 0.20000000000000001 0
		-1 -1 0
		1 -1 0
		1 0.20000000000000001 0
		-1 0.20000000000000001 0
		;
createNode transform -n "c_Lf_eyebrows_03_FRAME_lockfy" -p "c_Lf_eyebrows_03_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Lf_eyebrows_03_FRAME_lockfyShape" -p "c_Lf_eyebrows_03_FRAME_lockfy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -0.20000000000000001 0
		1 -0.20000000000000001 0
		1 1 0
		-1 1 0
		;
createNode transform -n "c_Lf_eyebrows_03_FRAME_lockzx" -p "c_Lf_eyebrows_03_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Lf_eyebrows_03_FRAME_lockzxShape" -p "c_Lf_eyebrows_03_FRAME_lockzx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		0.20000000000000001 -1 0
		0.20000000000000001 1 0
		-1 1 0
		;
createNode transform -n "c_Lf_eyebrows_03_FRAME_lockfx" -p "c_Lf_eyebrows_03_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Lf_eyebrows_03_FRAME_lockfxShape" -p "c_Lf_eyebrows_03_FRAME_lockfx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 1 0
		-0.20000000000000001 -1 0
		1 -1 0
		1 1 0
		-0.20000000000000001 1 0
		;
createNode transform -n "c_Lf_eyebrows_03_FRAME_lockzyfy" -p "c_Lf_eyebrows_03_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Lf_eyebrows_03_FRAME_lockzyfyShape" -p "c_Lf_eyebrows_03_FRAME_lockzyfy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 0.20000000000000001 0
		-1 -0.20000000000000001 0
		1 -0.20000000000000001 0
		1 0.20000000000000001 0
		-1 0.20000000000000001 0
		;
createNode transform -n "c_Lf_eyebrows_03_FRAME_lockzxfx" -p "c_Lf_eyebrows_03_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Lf_eyebrows_03_FRAME_lockzxfxShape" -p "c_Lf_eyebrows_03_FRAME_lockzxfx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 1 0
		-0.20000000000000001 -1 0
		0.20000000000000001 -1 0
		0.20000000000000001 1 0
		-0.20000000000000001 1 0
		;
createNode transform -n "c_Lf_eyebrows_03_FRAME_lockzyfyzx" -p "c_Lf_eyebrows_03_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Lf_eyebrows_03_FRAME_lockzyfyzxShape" -p "c_Lf_eyebrows_03_FRAME_lockzyfyzx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 0.20000000000000001 0
		-1 -0.20000000000000001 0
		0.20000000000000001 -0.20000000000000001 0
		0.20000000000000001 0.20000000000000001 0
		-1 0.20000000000000001 0
		;
createNode transform -n "c_Lf_eyebrows_03_FRAME_lockzyfyfx" -p "c_Lf_eyebrows_03_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Lf_eyebrows_03_FRAME_lockzyfyfxShape" -p "c_Lf_eyebrows_03_FRAME_lockzyfyfx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 0.20000000000000001 0
		-0.20000000000000001 -0.20000000000000001 0
		1 -0.20000000000000001 0
		1 0.20000000000000001 0
		-0.20000000000000001 0.20000000000000001 0
		;
createNode transform -n "c_Lf_eyebrows_03_FRAME_lockzxfxzy" -p "c_Lf_eyebrows_03_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Lf_eyebrows_03_FRAME_lockzxfxzyShape" -p "c_Lf_eyebrows_03_FRAME_lockzxfxzy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 0.20000000000000001 0
		-0.20000000000000001 -1 0
		0.20000000000000001 -1 0
		0.20000000000000001 0.20000000000000001 0
		-0.20000000000000001 0.20000000000000001 0
		;
createNode transform -n "c_Lf_eyebrows_03_FRAME_lockzxfxfy" -p "c_Lf_eyebrows_03_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Lf_eyebrows_03_FRAME_lockzxfxfyShape" -p "c_Lf_eyebrows_03_FRAME_lockzxfxfy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 1 0
		-0.20000000000000001 -0.20000000000000001 0
		0.20000000000000001 -0.20000000000000001 0
		0.20000000000000001 1 0
		-0.20000000000000001 1 0
		;
createNode transform -n "c_Lf_eyebrows_03_CTRL_up" -p "c_Lf_eyebrows_03_FRAME";
	setAttr ".t" -type "double3" 0 2.2 0 ;
createNode nurbsCurve -n "curveShape25" -p "c_Lf_eyebrows_03_CTRL_up";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_eyebrows_03_LOC_up" -p "c_Lf_eyebrows_03_CTRL_up";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_eyebrows_03_CTRL_dn" -p "c_Lf_eyebrows_03_FRAME";
	setAttr ".t" -type "double3" 0 -2.2 0 ;
createNode nurbsCurve -n "curveShape26" -p "c_Lf_eyebrows_03_CTRL_dn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_eyebrows_03_LOC_dn" -p "c_Lf_eyebrows_03_CTRL_dn";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_eyebrows_03_CTRL_lf" -p "c_Lf_eyebrows_03_FRAME";
	setAttr ".t" -type "double3" -2.2 0 0 ;
createNode nurbsCurve -n "curveShape27" -p "c_Lf_eyebrows_03_CTRL_lf";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_eyebrows_03_LOC_lf" -p "c_Lf_eyebrows_03_CTRL_lf";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_eyebrows_03_CTRL_lfup" -p "c_Lf_eyebrows_03_FRAME";
	setAttr ".t" -type "double3" -2.2 2.2 0 ;
createNode nurbsCurve -n "curveShape28" -p "c_Lf_eyebrows_03_CTRL_lfup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_eyebrows_03_LOC_lfup" -p "c_Lf_eyebrows_03_CTRL_lfup";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_eyebrows_03_CTRL_rt" -p "c_Lf_eyebrows_03_FRAME";
	setAttr ".t" -type "double3" 2.2 0 0 ;
createNode nurbsCurve -n "curveShape29" -p "c_Lf_eyebrows_03_CTRL_rt";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_eyebrows_03_LOC_rt" -p "c_Lf_eyebrows_03_CTRL_rt";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_eyebrows_03_CTRL_rtup" -p "c_Lf_eyebrows_03_FRAME";
	setAttr ".t" -type "double3" 2.2 2.2 0 ;
createNode nurbsCurve -n "curveShape30" -p "c_Lf_eyebrows_03_CTRL_rtup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_eyebrows_03_LOC_rtup" -p "c_Lf_eyebrows_03_CTRL_rtup";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_eyebrows_03_CTRL_lfdn" -p "c_Lf_eyebrows_03_FRAME";
	setAttr ".t" -type "double3" -2.2 -2.2 0 ;
createNode nurbsCurve -n "curveShape31" -p "c_Lf_eyebrows_03_CTRL_lfdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_eyebrows_03_LOC_lfdn" -p "c_Lf_eyebrows_03_CTRL_lfdn";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_eyebrows_03_CTRL_rtdn" -p "c_Lf_eyebrows_03_FRAME";
	setAttr ".t" -type "double3" 2.2 -2.2 0 ;
createNode nurbsCurve -n "curveShape32" -p "c_Lf_eyebrows_03_CTRL_rtdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_eyebrows_03_LOC_rtdn" -p "c_Lf_eyebrows_03_CTRL_rtdn";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_eyebrows_03_CTRL_fourAxisup" -p "c_Lf_eyebrows_03_FRAME";
	setAttr ".t" -type "double3" 0 4.4 0 ;
createNode nurbsCurve -n "curveShape33" -p "c_Lf_eyebrows_03_CTRL_fourAxisup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_eyebrows_03_LOC_fourAxis_up" -p "c_Lf_eyebrows_03_CTRL_fourAxisup";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_eyebrows_03_CTRL_fourAxisdn" -p "c_Lf_eyebrows_03_FRAME";
	setAttr ".t" -type "double3" 0 -4.4 0 ;
createNode nurbsCurve -n "curveShape34" -p "c_Lf_eyebrows_03_CTRL_fourAxisdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_eyebrows_03_LOC_fourAxis_dn" -p "c_Lf_eyebrows_03_CTRL_fourAxisdn";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_eyebrows_03_CTRL_fourAxislf" -p "c_Lf_eyebrows_03_FRAME";
	setAttr ".t" -type "double3" -4.4 0 0 ;
createNode nurbsCurve -n "curveShape35" -p "c_Lf_eyebrows_03_CTRL_fourAxislf";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_eyebrows_03_LOC_fourAxis_lf" -p "c_Lf_eyebrows_03_CTRL_fourAxislf";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_eyebrows_03_CTRL_fourAxisrt" -p "c_Lf_eyebrows_03_FRAME";
	setAttr ".t" -type "double3" 4.4 0 0 ;
createNode nurbsCurve -n "curveShape36" -p "c_Lf_eyebrows_03_CTRL_fourAxisrt";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_eyebrows_03_LOC_fourAxis_rt" -p "c_Lf_eyebrows_03_CTRL_fourAxisrt";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_eyebrows_CTRL_GRP_GRP" -p "c_eyebrows_GRP";
	setAttr ".s" -type "double3" -0.2 0.2 0.2 ;
	setAttr ".rp" -type "double3" -0.56647208816660621 1.0030343002242577 0.0089799342337341156 ;
	setAttr ".sp" -type "double3" -0.56647208816660621 1.0030343002242577 0.0089799342337341156 ;
createNode transform -n "c_Rt_eyebrows_CTRL_GRP" -p "c_Rt_eyebrows_CTRL_GRP_GRP";
	addAttr -ci true -sn "T1" -ln "T1" -at "double";
	addAttr -ci true -sn "T2" -ln "T2" -at "double";
	addAttr -ci true -sn "T3" -ln "T3" -at "double";
	addAttr -ci true -sn "R1" -ln "R1" -at "double";
	addAttr -ci true -sn "R2" -ln "R2" -at "double";
	addAttr -ci true -sn "R3" -ln "R3" -at "double";
	addAttr -ci true -sn "S1" -ln "S1" -at "double";
	addAttr -ci true -sn "S2" -ln "S2" -at "double";
	addAttr -ci true -sn "S3" -ln "S3" -at "double";
	setAttr ".rp" -type "double3" -0.56647208816660621 1.0030343002242577 0.0089799342337341156 ;
	setAttr ".sp" -type "double3" -0.56647208816660621 1.0030343002242577 0.0089799342337341156 ;
	setAttr -k on ".T1";
	setAttr -k on ".T2";
	setAttr -k on ".T3";
	setAttr -k on ".R1";
	setAttr -k on ".R2";
	setAttr -k on ".R3";
	setAttr -k on ".S1" 1;
	setAttr -k on ".S2" 1;
	setAttr -k on ".S3" 1;
createNode transform -n "c_Rt_eyebrows_CTRL" -p "c_Rt_eyebrows_CTRL_GRP";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -0.56647208816660621 1.0147499524560284 0.017959868467468276 ;
	setAttr ".sp" -type "double3" -0.56647208816660621 1.0147499524560284 0.017959868467468276 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
createNode nurbsCurve -n "c_Rt_eyebrows_CTRLShape" -p "c_Rt_eyebrows_CTRL";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-2.2522160846257946 1.5711291237949425 0.017959868467468259
		-0.56647208816660322 1.9726315390269658 0.0179598684674682
		1.1192719082925815 1.5711291237949414 0.017959868467468259
		1.8175299343150004 0.75885783219749636 0.017959868467468294
		1.1192719082925819 -0.053413459399946329 0.01795986846746836
		-0.56647208816660322 0.48113501794513835 0.017959868467468259
		-2.2522160846257901 -0.053413459399946329 0.01795986846746836
		-2.9504741106482082 0.75885783219749636 0.017959868467468294
		-2.2522160846257946 1.5711291237949425 0.017959868467468259
		-0.56647208816660322 1.9726315390269658 0.0179598684674682
		1.1192719082925815 1.5711291237949414 0.017959868467468259
		;
createNode transform -n "GRP_c_Rt_eyebrows_01_FRAME" -p "c_Rt_eyebrows_CTRL";
	setAttr ".t" -type "double3" -1.8925627196310761 0.90652663106144438 -0.035919736934936643 ;
	setAttr ".r" -type "double3" 7.9513867036587929e-017 -7.108105048507156e-015 1.0208657405589586e-014 ;
	setAttr ".s" -type "double3" 0.75 0.75 -0.75 ;
createNode transform -n "c_Rt_eyebrows_01_FRAME" -p "GRP_c_Rt_eyebrows_01_FRAME";
	addAttr -ci true -sn "up" -ln "up" -min 0 -at "double";
	addAttr -ci true -sn "dn" -ln "dn" -min 0 -at "double";
	addAttr -ci true -sn "lf" -ln "lf" -min 0 -at "double";
	addAttr -ci true -sn "rt" -ln "rt" -min 0 -at "double";
	addAttr -ci true -sn "lfup" -ln "lfup" -min 0 -at "double";
	addAttr -ci true -sn "rtup" -ln "rtup" -min 0 -at "double";
	addAttr -ci true -sn "lfdn" -ln "lfdn" -min 0 -at "double";
	addAttr -ci true -sn "rtdn" -ln "rtdn" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_up" -ln "fourAxis_up" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_dn" -ln "fourAxis_dn" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_lf" -ln "fourAxis_lf" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_rt" -ln "fourAxis_rt" -min 0 -at "double";
	addAttr -ci true -sn "up_Vis" -ln "up_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "dn_Vis" -ln "dn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lf_Vis" -ln "lf_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lfup_Vis" -ln "lfup_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rt_Vis" -ln "rt_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rtup_Vis" -ln "rtup_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lfdn_Vis" -ln "lfdn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rtdn_Vis" -ln "rtdn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_up_Vis" -ln "fourAxis_up_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_dn_Vis" -ln "fourAxis_dn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_lf_Vis" -ln "fourAxis_lf_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_rt_Vis" -ln "fourAxis_rt_Vis" -min 0 -max 1 -at "bool";
	setAttr -k on ".up";
	setAttr -k on ".dn";
	setAttr -k on ".lf";
	setAttr -k on ".rt";
	setAttr -k on ".lfup";
	setAttr -k on ".rtup";
	setAttr -k on ".lfdn";
	setAttr -k on ".rtdn";
	setAttr -k on ".fourAxis_up";
	setAttr -k on ".fourAxis_dn";
	setAttr -k on ".fourAxis_lf";
	setAttr -k on ".fourAxis_rt";
	setAttr -cb on ".up_Vis";
	setAttr -cb on ".dn_Vis";
	setAttr -cb on ".lf_Vis";
	setAttr -cb on ".lfup_Vis";
	setAttr -cb on ".rt_Vis";
	setAttr -cb on ".rtup_Vis";
	setAttr -cb on ".lfdn_Vis";
	setAttr -cb on ".rtdn_Vis";
	setAttr -cb on ".fourAxis_up_Vis";
	setAttr -cb on ".fourAxis_dn_Vis";
	setAttr -cb on ".fourAxis_lf_Vis";
	setAttr -cb on ".fourAxis_rt_Vis";
createNode nurbsCurve -n "c_Rt_eyebrows_01_FRAMEShape" -p "c_Rt_eyebrows_01_FRAME";
	setAttr -k off ".v" no;
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode transform -n "GRP_c_Rt_eyebrows_01_CTRL" -p "c_Rt_eyebrows_01_FRAME";
createNode transform -n "c_Rt_eyebrows_01_CTRL" -p "GRP_c_Rt_eyebrows_01_CTRL";
	addAttr -ci true -sn "frameSelectAble" -ln "frameSelectAble" -min 0 -max 2 -en 
		"normal:template:reference" -at "enum";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".mntl" -type "double3" -1 -1 0 ;
	setAttr ".mxtl" -type "double3" 1 1 0 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
	setAttr ".frameSelectAble" 2;
createNode nurbsCurve -n "c_Rt_eyebrows_01_CTRLShape" -p "c_Rt_eyebrows_01_CTRL";
	setAttr -k off ".v" no;
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		1 32 0 no 3
		33 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32
		33
		-0.050000000000000003 0.050000000000000003 0
		-0.050000000000000003 0.15000000000000002 0
		-0.10000000000000001 0.15000000000000002 0
		0 0.25 0
		0.10000000000000001 0.15000000000000002 0
		0.050000000000000003 0.15000000000000002 0
		0.050000000000000003 0.050000000000000003 0
		0.20000000000000001 0.20000000000000001 0
		0.050000000000000003 0.050000000000000003 0
		0.15000000000000002 0.050000000000000003 0
		0.15000000000000002 0.10000000000000001 0
		0.25 0 0
		0.15000000000000002 -0.10000000000000001 0
		0.15000000000000002 -0.050000000000000003 0
		0.050000000000000003 -0.050000000000000003 0
		0.20000000000000001 -0.20000000000000001 0
		0.050000000000000003 -0.050000000000000003 0
		0.050000000000000003 -0.15000000000000002 0
		0.10000000000000001 -0.15000000000000002 0
		0 -0.25 0
		-0.10000000000000001 -0.15000000000000002 0
		-0.050000000000000003 -0.15000000000000002 0
		-0.050000000000000003 -0.050000000000000003 0
		-0.20000000000000001 -0.20000000000000001 0
		-0.050000000000000003 -0.050000000000000003 0
		-0.15000000000000002 -0.050000000000000003 0
		-0.15000000000000002 -0.10000000000000001 0
		-0.25 0 0
		-0.15000000000000002 0.10000000000000001 0
		-0.15000000000000002 0.050000000000000003 0
		-0.050000000000000003 0.050000000000000003 0
		-0.20000000000000001 0.20000000000000001 0
		-0.050000000000000003 0.050000000000000003 0
		;
createNode transform -n "c_Rt_eyebrows_01_FRAME_lockzy" -p "c_Rt_eyebrows_01_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Rt_eyebrows_01_FRAME_lockzyShape" -p "c_Rt_eyebrows_01_FRAME_lockzy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 0.20000000000000001 0
		-1 -1 0
		1 -1 0
		1 0.20000000000000001 0
		-1 0.20000000000000001 0
		;
createNode transform -n "c_Rt_eyebrows_01_FRAME_lockfy" -p "c_Rt_eyebrows_01_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Rt_eyebrows_01_FRAME_lockfyShape" -p "c_Rt_eyebrows_01_FRAME_lockfy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -0.20000000000000001 0
		1 -0.20000000000000001 0
		1 1 0
		-1 1 0
		;
createNode transform -n "c_Rt_eyebrows_01_FRAME_lockzx" -p "c_Rt_eyebrows_01_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Rt_eyebrows_01_FRAME_lockzxShape" -p "c_Rt_eyebrows_01_FRAME_lockzx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		0.20000000000000001 -1 0
		0.20000000000000001 1 0
		-1 1 0
		;
createNode transform -n "c_Rt_eyebrows_01_FRAME_lockfx" -p "c_Rt_eyebrows_01_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Rt_eyebrows_01_FRAME_lockfxShape" -p "c_Rt_eyebrows_01_FRAME_lockfx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 1 0
		-0.20000000000000001 -1 0
		1 -1 0
		1 1 0
		-0.20000000000000001 1 0
		;
createNode transform -n "c_Rt_eyebrows_01_FRAME_lockzyfy" -p "c_Rt_eyebrows_01_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Rt_eyebrows_01_FRAME_lockzyfyShape" -p "c_Rt_eyebrows_01_FRAME_lockzyfy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 0.20000000000000001 0
		-1 -0.20000000000000001 0
		1 -0.20000000000000001 0
		1 0.20000000000000001 0
		-1 0.20000000000000001 0
		;
createNode transform -n "c_Rt_eyebrows_01_FRAME_lockzxfx" -p "c_Rt_eyebrows_01_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Rt_eyebrows_01_FRAME_lockzxfxShape" -p "c_Rt_eyebrows_01_FRAME_lockzxfx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 1 0
		-0.20000000000000001 -1 0
		0.20000000000000001 -1 0
		0.20000000000000001 1 0
		-0.20000000000000001 1 0
		;
createNode transform -n "c_Rt_eyebrows_01_FRAME_lockzyfyzx" -p "c_Rt_eyebrows_01_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Rt_eyebrows_01_FRAME_lockzyfyzxShape" -p "c_Rt_eyebrows_01_FRAME_lockzyfyzx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 0.20000000000000001 0
		-1 -0.20000000000000001 0
		0.20000000000000001 -0.20000000000000001 0
		0.20000000000000001 0.20000000000000001 0
		-1 0.20000000000000001 0
		;
createNode transform -n "c_Rt_eyebrows_01_FRAME_lockzyfyfx" -p "c_Rt_eyebrows_01_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Rt_eyebrows_01_FRAME_lockzyfyfxShape" -p "c_Rt_eyebrows_01_FRAME_lockzyfyfx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 0.20000000000000001 0
		-0.20000000000000001 -0.20000000000000001 0
		1 -0.20000000000000001 0
		1 0.20000000000000001 0
		-0.20000000000000001 0.20000000000000001 0
		;
createNode transform -n "c_Rt_eyebrows_01_FRAME_lockzxfxzy" -p "c_Rt_eyebrows_01_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Rt_eyebrows_01_FRAME_lockzxfxzyShape" -p "c_Rt_eyebrows_01_FRAME_lockzxfxzy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 0.20000000000000001 0
		-0.20000000000000001 -1 0
		0.20000000000000001 -1 0
		0.20000000000000001 0.20000000000000001 0
		-0.20000000000000001 0.20000000000000001 0
		;
createNode transform -n "c_Rt_eyebrows_01_FRAME_lockzxfxfy" -p "c_Rt_eyebrows_01_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Rt_eyebrows_01_FRAME_lockzxfxfyShape" -p "c_Rt_eyebrows_01_FRAME_lockzxfxfy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 1 0
		-0.20000000000000001 -0.20000000000000001 0
		0.20000000000000001 -0.20000000000000001 0
		0.20000000000000001 1 0
		-0.20000000000000001 1 0
		;
createNode transform -n "c_Rt_eyebrows_01_CTRL_up" -p "c_Rt_eyebrows_01_FRAME";
	setAttr ".t" -type "double3" 0 2.2 0 ;
createNode nurbsCurve -n "curveShape37" -p "c_Rt_eyebrows_01_CTRL_up";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_eyebrows_01_LOC_up" -p "c_Rt_eyebrows_01_CTRL_up";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_eyebrows_01_CTRL_dn" -p "c_Rt_eyebrows_01_FRAME";
	setAttr ".t" -type "double3" 0 -2.2 0 ;
createNode nurbsCurve -n "curveShape38" -p "c_Rt_eyebrows_01_CTRL_dn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_eyebrows_01_LOC_dn" -p "c_Rt_eyebrows_01_CTRL_dn";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_eyebrows_01_CTRL_lf" -p "c_Rt_eyebrows_01_FRAME";
	setAttr ".t" -type "double3" -2.2 0 0 ;
createNode nurbsCurve -n "curveShape39" -p "c_Rt_eyebrows_01_CTRL_lf";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_eyebrows_01_LOC_lf" -p "c_Rt_eyebrows_01_CTRL_lf";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_eyebrows_01_CTRL_lfup" -p "c_Rt_eyebrows_01_FRAME";
	setAttr ".t" -type "double3" -2.2 2.2 0 ;
createNode nurbsCurve -n "curveShape40" -p "c_Rt_eyebrows_01_CTRL_lfup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_eyebrows_01_LOC_lfup" -p "c_Rt_eyebrows_01_CTRL_lfup";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_eyebrows_01_CTRL_rt" -p "c_Rt_eyebrows_01_FRAME";
	setAttr ".t" -type "double3" 2.2 0 0 ;
createNode nurbsCurve -n "curveShape41" -p "c_Rt_eyebrows_01_CTRL_rt";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_eyebrows_01_LOC_rt" -p "c_Rt_eyebrows_01_CTRL_rt";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_eyebrows_01_CTRL_rtup" -p "c_Rt_eyebrows_01_FRAME";
	setAttr ".t" -type "double3" 2.2 2.2 0 ;
createNode nurbsCurve -n "curveShape42" -p "c_Rt_eyebrows_01_CTRL_rtup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_eyebrows_01_LOC_rtup" -p "c_Rt_eyebrows_01_CTRL_rtup";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_eyebrows_01_CTRL_lfdn" -p "c_Rt_eyebrows_01_FRAME";
	setAttr ".t" -type "double3" -2.2 -2.2 0 ;
createNode nurbsCurve -n "curveShape43" -p "c_Rt_eyebrows_01_CTRL_lfdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_eyebrows_01_LOC_lfdn" -p "c_Rt_eyebrows_01_CTRL_lfdn";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_eyebrows_01_CTRL_rtdn" -p "c_Rt_eyebrows_01_FRAME";
	setAttr ".t" -type "double3" 2.2 -2.2 0 ;
createNode nurbsCurve -n "curveShape44" -p "c_Rt_eyebrows_01_CTRL_rtdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_eyebrows_01_LOC_rtdn" -p "c_Rt_eyebrows_01_CTRL_rtdn";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_eyebrows_01_CTRL_fourAxisup" -p "c_Rt_eyebrows_01_FRAME";
	setAttr ".t" -type "double3" 0 4.4 0 ;
createNode nurbsCurve -n "curveShape45" -p "c_Rt_eyebrows_01_CTRL_fourAxisup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_eyebrows_01_LOC_fourAxis_up" -p "c_Rt_eyebrows_01_CTRL_fourAxisup";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_eyebrows_01_CTRL_fourAxisdn" -p "c_Rt_eyebrows_01_FRAME";
	setAttr ".t" -type "double3" 0 -4.4 0 ;
createNode nurbsCurve -n "curveShape46" -p "c_Rt_eyebrows_01_CTRL_fourAxisdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_eyebrows_01_LOC_fourAxis_dn" -p "c_Rt_eyebrows_01_CTRL_fourAxisdn";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_eyebrows_01_CTRL_fourAxislf" -p "c_Rt_eyebrows_01_FRAME";
	setAttr ".t" -type "double3" -4.4 0 0 ;
createNode nurbsCurve -n "curveShape47" -p "c_Rt_eyebrows_01_CTRL_fourAxislf";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_eyebrows_01_LOC_fourAxis_lf" -p "c_Rt_eyebrows_01_CTRL_fourAxislf";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_eyebrows_01_CTRL_fourAxisrt" -p "c_Rt_eyebrows_01_FRAME";
	setAttr ".t" -type "double3" 4.4 0 0 ;
createNode nurbsCurve -n "curveShape48" -p "c_Rt_eyebrows_01_CTRL_fourAxisrt";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_eyebrows_01_LOC_fourAxis_rt" -p "c_Rt_eyebrows_01_CTRL_fourAxisrt";
	setAttr -k off ".v" no;
createNode transform -n "GRP_c_Rt_eyebrows_02_FRAME" -p "c_Rt_eyebrows_CTRL";
	setAttr ".t" -type "double3" -0.48254352863659999 1.1030448881591202 -0.035919736934936469 ;
	setAttr ".r" -type "double3" 7.9513867036587929e-017 -7.108105048507156e-015 1.0208657405589586e-014 ;
	setAttr ".s" -type "double3" 0.75 0.75 -0.75 ;
createNode transform -n "c_Rt_eyebrows_02_FRAME" -p "GRP_c_Rt_eyebrows_02_FRAME";
	addAttr -ci true -sn "up" -ln "up" -min 0 -at "double";
	addAttr -ci true -sn "dn" -ln "dn" -min 0 -at "double";
	addAttr -ci true -sn "lf" -ln "lf" -min 0 -at "double";
	addAttr -ci true -sn "rt" -ln "rt" -min 0 -at "double";
	addAttr -ci true -sn "lfup" -ln "lfup" -min 0 -at "double";
	addAttr -ci true -sn "rtup" -ln "rtup" -min 0 -at "double";
	addAttr -ci true -sn "lfdn" -ln "lfdn" -min 0 -at "double";
	addAttr -ci true -sn "rtdn" -ln "rtdn" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_up" -ln "fourAxis_up" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_dn" -ln "fourAxis_dn" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_lf" -ln "fourAxis_lf" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_rt" -ln "fourAxis_rt" -min 0 -at "double";
	addAttr -ci true -sn "up_Vis" -ln "up_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "dn_Vis" -ln "dn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lf_Vis" -ln "lf_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lfup_Vis" -ln "lfup_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rt_Vis" -ln "rt_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rtup_Vis" -ln "rtup_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lfdn_Vis" -ln "lfdn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rtdn_Vis" -ln "rtdn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_up_Vis" -ln "fourAxis_up_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_dn_Vis" -ln "fourAxis_dn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_lf_Vis" -ln "fourAxis_lf_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_rt_Vis" -ln "fourAxis_rt_Vis" -min 0 -max 1 -at "bool";
	setAttr -k on ".up";
	setAttr -k on ".dn";
	setAttr -k on ".lf";
	setAttr -k on ".rt";
	setAttr -k on ".lfup";
	setAttr -k on ".rtup";
	setAttr -k on ".lfdn";
	setAttr -k on ".rtdn";
	setAttr -k on ".fourAxis_up";
	setAttr -k on ".fourAxis_dn";
	setAttr -k on ".fourAxis_lf";
	setAttr -k on ".fourAxis_rt";
	setAttr -cb on ".up_Vis";
	setAttr -cb on ".dn_Vis";
	setAttr -cb on ".lf_Vis";
	setAttr -cb on ".lfup_Vis";
	setAttr -cb on ".rt_Vis";
	setAttr -cb on ".rtup_Vis";
	setAttr -cb on ".lfdn_Vis";
	setAttr -cb on ".rtdn_Vis";
	setAttr -cb on ".fourAxis_up_Vis";
	setAttr -cb on ".fourAxis_dn_Vis";
	setAttr -cb on ".fourAxis_lf_Vis";
	setAttr -cb on ".fourAxis_rt_Vis";
createNode nurbsCurve -n "c_Rt_eyebrows_02_FRAMEShape" -p "c_Rt_eyebrows_02_FRAME";
	setAttr -k off ".v" no;
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode transform -n "GRP_c_Rt_eyebrows_02_CTRL" -p "c_Rt_eyebrows_02_FRAME";
createNode transform -n "c_Rt_eyebrows_02_CTRL" -p "GRP_c_Rt_eyebrows_02_CTRL";
	addAttr -ci true -sn "frameSelectAble" -ln "frameSelectAble" -min 0 -max 2 -en 
		"normal:template:reference" -at "enum";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".mntl" -type "double3" -1 -1 0 ;
	setAttr ".mxtl" -type "double3" 1 1 0 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
	setAttr ".frameSelectAble" 2;
createNode nurbsCurve -n "c_Rt_eyebrows_02_CTRLShape" -p "c_Rt_eyebrows_02_CTRL";
	setAttr -k off ".v" no;
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		1 32 0 no 3
		33 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32
		33
		-0.050000000000000003 0.050000000000000003 0
		-0.050000000000000003 0.15000000000000002 0
		-0.10000000000000001 0.15000000000000002 0
		0 0.25 0
		0.10000000000000001 0.15000000000000002 0
		0.050000000000000003 0.15000000000000002 0
		0.050000000000000003 0.050000000000000003 0
		0.20000000000000001 0.20000000000000001 0
		0.050000000000000003 0.050000000000000003 0
		0.15000000000000002 0.050000000000000003 0
		0.15000000000000002 0.10000000000000001 0
		0.25 0 0
		0.15000000000000002 -0.10000000000000001 0
		0.15000000000000002 -0.050000000000000003 0
		0.050000000000000003 -0.050000000000000003 0
		0.20000000000000001 -0.20000000000000001 0
		0.050000000000000003 -0.050000000000000003 0
		0.050000000000000003 -0.15000000000000002 0
		0.10000000000000001 -0.15000000000000002 0
		0 -0.25 0
		-0.10000000000000001 -0.15000000000000002 0
		-0.050000000000000003 -0.15000000000000002 0
		-0.050000000000000003 -0.050000000000000003 0
		-0.20000000000000001 -0.20000000000000001 0
		-0.050000000000000003 -0.050000000000000003 0
		-0.15000000000000002 -0.050000000000000003 0
		-0.15000000000000002 -0.10000000000000001 0
		-0.25 0 0
		-0.15000000000000002 0.10000000000000001 0
		-0.15000000000000002 0.050000000000000003 0
		-0.050000000000000003 0.050000000000000003 0
		-0.20000000000000001 0.20000000000000001 0
		-0.050000000000000003 0.050000000000000003 0
		;
createNode transform -n "c_Rt_eyebrows_02_FRAME_lockzy" -p "c_Rt_eyebrows_02_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Rt_eyebrows_02_FRAME_lockzyShape" -p "c_Rt_eyebrows_02_FRAME_lockzy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 0.20000000000000001 0
		-1 -1 0
		1 -1 0
		1 0.20000000000000001 0
		-1 0.20000000000000001 0
		;
createNode transform -n "c_Rt_eyebrows_02_FRAME_lockfy" -p "c_Rt_eyebrows_02_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Rt_eyebrows_02_FRAME_lockfyShape" -p "c_Rt_eyebrows_02_FRAME_lockfy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -0.20000000000000001 0
		1 -0.20000000000000001 0
		1 1 0
		-1 1 0
		;
createNode transform -n "c_Rt_eyebrows_02_FRAME_lockzx" -p "c_Rt_eyebrows_02_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Rt_eyebrows_02_FRAME_lockzxShape" -p "c_Rt_eyebrows_02_FRAME_lockzx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		0.20000000000000001 -1 0
		0.20000000000000001 1 0
		-1 1 0
		;
createNode transform -n "c_Rt_eyebrows_02_FRAME_lockfx" -p "c_Rt_eyebrows_02_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Rt_eyebrows_02_FRAME_lockfxShape" -p "c_Rt_eyebrows_02_FRAME_lockfx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 1 0
		-0.20000000000000001 -1 0
		1 -1 0
		1 1 0
		-0.20000000000000001 1 0
		;
createNode transform -n "c_Rt_eyebrows_02_FRAME_lockzyfy" -p "c_Rt_eyebrows_02_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Rt_eyebrows_02_FRAME_lockzyfyShape" -p "c_Rt_eyebrows_02_FRAME_lockzyfy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 0.20000000000000001 0
		-1 -0.20000000000000001 0
		1 -0.20000000000000001 0
		1 0.20000000000000001 0
		-1 0.20000000000000001 0
		;
createNode transform -n "c_Rt_eyebrows_02_FRAME_lockzxfx" -p "c_Rt_eyebrows_02_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Rt_eyebrows_02_FRAME_lockzxfxShape" -p "c_Rt_eyebrows_02_FRAME_lockzxfx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 1 0
		-0.20000000000000001 -1 0
		0.20000000000000001 -1 0
		0.20000000000000001 1 0
		-0.20000000000000001 1 0
		;
createNode transform -n "c_Rt_eyebrows_02_FRAME_lockzyfyzx" -p "c_Rt_eyebrows_02_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Rt_eyebrows_02_FRAME_lockzyfyzxShape" -p "c_Rt_eyebrows_02_FRAME_lockzyfyzx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 0.20000000000000001 0
		-1 -0.20000000000000001 0
		0.20000000000000001 -0.20000000000000001 0
		0.20000000000000001 0.20000000000000001 0
		-1 0.20000000000000001 0
		;
createNode transform -n "c_Rt_eyebrows_02_FRAME_lockzyfyfx" -p "c_Rt_eyebrows_02_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Rt_eyebrows_02_FRAME_lockzyfyfxShape" -p "c_Rt_eyebrows_02_FRAME_lockzyfyfx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 0.20000000000000001 0
		-0.20000000000000001 -0.20000000000000001 0
		1 -0.20000000000000001 0
		1 0.20000000000000001 0
		-0.20000000000000001 0.20000000000000001 0
		;
createNode transform -n "c_Rt_eyebrows_02_FRAME_lockzxfxzy" -p "c_Rt_eyebrows_02_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Rt_eyebrows_02_FRAME_lockzxfxzyShape" -p "c_Rt_eyebrows_02_FRAME_lockzxfxzy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 0.20000000000000001 0
		-0.20000000000000001 -1 0
		0.20000000000000001 -1 0
		0.20000000000000001 0.20000000000000001 0
		-0.20000000000000001 0.20000000000000001 0
		;
createNode transform -n "c_Rt_eyebrows_02_FRAME_lockzxfxfy" -p "c_Rt_eyebrows_02_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Rt_eyebrows_02_FRAME_lockzxfxfyShape" -p "c_Rt_eyebrows_02_FRAME_lockzxfxfy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 1 0
		-0.20000000000000001 -0.20000000000000001 0
		0.20000000000000001 -0.20000000000000001 0
		0.20000000000000001 1 0
		-0.20000000000000001 1 0
		;
createNode transform -n "c_Rt_eyebrows_02_CTRL_up" -p "c_Rt_eyebrows_02_FRAME";
	setAttr ".t" -type "double3" 0 2.2 0 ;
createNode nurbsCurve -n "curveShape49" -p "c_Rt_eyebrows_02_CTRL_up";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_eyebrows_02_LOC_up" -p "c_Rt_eyebrows_02_CTRL_up";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_eyebrows_02_CTRL_dn" -p "c_Rt_eyebrows_02_FRAME";
	setAttr ".t" -type "double3" 0 -2.2 0 ;
createNode nurbsCurve -n "curveShape50" -p "c_Rt_eyebrows_02_CTRL_dn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_eyebrows_02_LOC_dn" -p "c_Rt_eyebrows_02_CTRL_dn";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_eyebrows_02_CTRL_lf" -p "c_Rt_eyebrows_02_FRAME";
	setAttr ".t" -type "double3" -2.2 0 0 ;
createNode nurbsCurve -n "curveShape51" -p "c_Rt_eyebrows_02_CTRL_lf";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_eyebrows_02_LOC_lf" -p "c_Rt_eyebrows_02_CTRL_lf";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_eyebrows_02_CTRL_lfup" -p "c_Rt_eyebrows_02_FRAME";
	setAttr ".t" -type "double3" -2.2 2.2 0 ;
createNode nurbsCurve -n "curveShape52" -p "c_Rt_eyebrows_02_CTRL_lfup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_eyebrows_02_LOC_lfup" -p "c_Rt_eyebrows_02_CTRL_lfup";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_eyebrows_02_CTRL_rt" -p "c_Rt_eyebrows_02_FRAME";
	setAttr ".t" -type "double3" 2.2 0 0 ;
createNode nurbsCurve -n "curveShape53" -p "c_Rt_eyebrows_02_CTRL_rt";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_eyebrows_02_LOC_rt" -p "c_Rt_eyebrows_02_CTRL_rt";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_eyebrows_02_CTRL_rtup" -p "c_Rt_eyebrows_02_FRAME";
	setAttr ".t" -type "double3" 2.2 2.2 0 ;
createNode nurbsCurve -n "curveShape54" -p "c_Rt_eyebrows_02_CTRL_rtup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_eyebrows_02_LOC_rtup" -p "c_Rt_eyebrows_02_CTRL_rtup";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_eyebrows_02_CTRL_lfdn" -p "c_Rt_eyebrows_02_FRAME";
	setAttr ".t" -type "double3" -2.2 -2.2 0 ;
createNode nurbsCurve -n "curveShape55" -p "c_Rt_eyebrows_02_CTRL_lfdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_eyebrows_02_LOC_lfdn" -p "c_Rt_eyebrows_02_CTRL_lfdn";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_eyebrows_02_CTRL_rtdn" -p "c_Rt_eyebrows_02_FRAME";
	setAttr ".t" -type "double3" 2.2 -2.2 0 ;
createNode nurbsCurve -n "curveShape56" -p "c_Rt_eyebrows_02_CTRL_rtdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_eyebrows_02_LOC_rtdn" -p "c_Rt_eyebrows_02_CTRL_rtdn";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_eyebrows_02_CTRL_fourAxisup" -p "c_Rt_eyebrows_02_FRAME";
	setAttr ".t" -type "double3" 0 4.4 0 ;
createNode nurbsCurve -n "curveShape57" -p "c_Rt_eyebrows_02_CTRL_fourAxisup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_eyebrows_02_LOC_fourAxis_up" -p "c_Rt_eyebrows_02_CTRL_fourAxisup";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_eyebrows_02_CTRL_fourAxisdn" -p "c_Rt_eyebrows_02_FRAME";
	setAttr ".t" -type "double3" 0 -4.4 0 ;
createNode nurbsCurve -n "curveShape58" -p "c_Rt_eyebrows_02_CTRL_fourAxisdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_eyebrows_02_LOC_fourAxis_dn" -p "c_Rt_eyebrows_02_CTRL_fourAxisdn";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_eyebrows_02_CTRL_fourAxislf" -p "c_Rt_eyebrows_02_FRAME";
	setAttr ".t" -type "double3" -4.4 0 0 ;
createNode nurbsCurve -n "curveShape59" -p "c_Rt_eyebrows_02_CTRL_fourAxislf";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_eyebrows_02_LOC_fourAxis_lf" -p "c_Rt_eyebrows_02_CTRL_fourAxislf";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_eyebrows_02_CTRL_fourAxisrt" -p "c_Rt_eyebrows_02_FRAME";
	setAttr ".t" -type "double3" 4.4 0 0 ;
createNode nurbsCurve -n "curveShape60" -p "c_Rt_eyebrows_02_CTRL_fourAxisrt";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_eyebrows_02_LOC_fourAxis_rt" -p "c_Rt_eyebrows_02_CTRL_fourAxisrt";
	setAttr -k off ".v" no;
createNode transform -n "GRP_c_Rt_eyebrows_03_FRAME" -p "c_Rt_eyebrows_CTRL";
	setAttr ".t" -type "double3" 0.89095570715634853 0.8410926054128316 -0.035919736934936303 ;
	setAttr ".r" -type "double3" 7.9513867036587929e-017 -7.108105048507156e-015 1.0208657405589586e-014 ;
	setAttr ".s" -type "double3" 0.75 0.75 -0.75 ;
createNode transform -n "c_Rt_eyebrows_03_FRAME" -p "GRP_c_Rt_eyebrows_03_FRAME";
	addAttr -ci true -sn "up" -ln "up" -min 0 -at "double";
	addAttr -ci true -sn "dn" -ln "dn" -min 0 -at "double";
	addAttr -ci true -sn "lf" -ln "lf" -min 0 -at "double";
	addAttr -ci true -sn "rt" -ln "rt" -min 0 -at "double";
	addAttr -ci true -sn "lfup" -ln "lfup" -min 0 -at "double";
	addAttr -ci true -sn "rtup" -ln "rtup" -min 0 -at "double";
	addAttr -ci true -sn "lfdn" -ln "lfdn" -min 0 -at "double";
	addAttr -ci true -sn "rtdn" -ln "rtdn" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_up" -ln "fourAxis_up" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_dn" -ln "fourAxis_dn" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_lf" -ln "fourAxis_lf" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_rt" -ln "fourAxis_rt" -min 0 -at "double";
	addAttr -ci true -sn "up_Vis" -ln "up_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "dn_Vis" -ln "dn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lf_Vis" -ln "lf_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lfup_Vis" -ln "lfup_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rt_Vis" -ln "rt_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rtup_Vis" -ln "rtup_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lfdn_Vis" -ln "lfdn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rtdn_Vis" -ln "rtdn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_up_Vis" -ln "fourAxis_up_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_dn_Vis" -ln "fourAxis_dn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_lf_Vis" -ln "fourAxis_lf_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_rt_Vis" -ln "fourAxis_rt_Vis" -min 0 -max 1 -at "bool";
	setAttr -k on ".up";
	setAttr -k on ".dn";
	setAttr -k on ".lf";
	setAttr -k on ".rt";
	setAttr -k on ".lfup";
	setAttr -k on ".rtup";
	setAttr -k on ".lfdn";
	setAttr -k on ".rtdn";
	setAttr -k on ".fourAxis_up";
	setAttr -k on ".fourAxis_dn";
	setAttr -k on ".fourAxis_lf";
	setAttr -k on ".fourAxis_rt";
	setAttr -cb on ".up_Vis";
	setAttr -cb on ".dn_Vis";
	setAttr -cb on ".lf_Vis";
	setAttr -cb on ".lfup_Vis";
	setAttr -cb on ".rt_Vis";
	setAttr -cb on ".rtup_Vis";
	setAttr -cb on ".lfdn_Vis";
	setAttr -cb on ".rtdn_Vis";
	setAttr -cb on ".fourAxis_up_Vis";
	setAttr -cb on ".fourAxis_dn_Vis";
	setAttr -cb on ".fourAxis_lf_Vis";
	setAttr -cb on ".fourAxis_rt_Vis";
createNode nurbsCurve -n "c_Rt_eyebrows_03_FRAMEShape" -p "c_Rt_eyebrows_03_FRAME";
	setAttr -k off ".v" no;
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode transform -n "GRP_c_Rt_eyebrows_03_CTRL" -p "c_Rt_eyebrows_03_FRAME";
createNode transform -n "c_Rt_eyebrows_03_CTRL" -p "GRP_c_Rt_eyebrows_03_CTRL";
	addAttr -ci true -sn "frameSelectAble" -ln "frameSelectAble" -min 0 -max 2 -en 
		"normal:template:reference" -at "enum";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".mntl" -type "double3" -1 -1 0 ;
	setAttr ".mxtl" -type "double3" 1 1 0 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
	setAttr ".frameSelectAble" 2;
createNode nurbsCurve -n "c_Rt_eyebrows_03_CTRLShape" -p "c_Rt_eyebrows_03_CTRL";
	setAttr -k off ".v" no;
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		1 32 0 no 3
		33 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32
		33
		-0.050000000000000003 0.050000000000000003 0
		-0.050000000000000003 0.15000000000000002 0
		-0.10000000000000001 0.15000000000000002 0
		0 0.25 0
		0.10000000000000001 0.15000000000000002 0
		0.050000000000000003 0.15000000000000002 0
		0.050000000000000003 0.050000000000000003 0
		0.20000000000000001 0.20000000000000001 0
		0.050000000000000003 0.050000000000000003 0
		0.15000000000000002 0.050000000000000003 0
		0.15000000000000002 0.10000000000000001 0
		0.25 0 0
		0.15000000000000002 -0.10000000000000001 0
		0.15000000000000002 -0.050000000000000003 0
		0.050000000000000003 -0.050000000000000003 0
		0.20000000000000001 -0.20000000000000001 0
		0.050000000000000003 -0.050000000000000003 0
		0.050000000000000003 -0.15000000000000002 0
		0.10000000000000001 -0.15000000000000002 0
		0 -0.25 0
		-0.10000000000000001 -0.15000000000000002 0
		-0.050000000000000003 -0.15000000000000002 0
		-0.050000000000000003 -0.050000000000000003 0
		-0.20000000000000001 -0.20000000000000001 0
		-0.050000000000000003 -0.050000000000000003 0
		-0.15000000000000002 -0.050000000000000003 0
		-0.15000000000000002 -0.10000000000000001 0
		-0.25 0 0
		-0.15000000000000002 0.10000000000000001 0
		-0.15000000000000002 0.050000000000000003 0
		-0.050000000000000003 0.050000000000000003 0
		-0.20000000000000001 0.20000000000000001 0
		-0.050000000000000003 0.050000000000000003 0
		;
createNode transform -n "c_Rt_eyebrows_03_FRAME_lockzy" -p "c_Rt_eyebrows_03_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Rt_eyebrows_03_FRAME_lockzyShape" -p "c_Rt_eyebrows_03_FRAME_lockzy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 0.20000000000000001 0
		-1 -1 0
		1 -1 0
		1 0.20000000000000001 0
		-1 0.20000000000000001 0
		;
createNode transform -n "c_Rt_eyebrows_03_FRAME_lockfy" -p "c_Rt_eyebrows_03_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Rt_eyebrows_03_FRAME_lockfyShape" -p "c_Rt_eyebrows_03_FRAME_lockfy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -0.20000000000000001 0
		1 -0.20000000000000001 0
		1 1 0
		-1 1 0
		;
createNode transform -n "c_Rt_eyebrows_03_FRAME_lockzx" -p "c_Rt_eyebrows_03_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Rt_eyebrows_03_FRAME_lockzxShape" -p "c_Rt_eyebrows_03_FRAME_lockzx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		0.20000000000000001 -1 0
		0.20000000000000001 1 0
		-1 1 0
		;
createNode transform -n "c_Rt_eyebrows_03_FRAME_lockfx" -p "c_Rt_eyebrows_03_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Rt_eyebrows_03_FRAME_lockfxShape" -p "c_Rt_eyebrows_03_FRAME_lockfx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 1 0
		-0.20000000000000001 -1 0
		1 -1 0
		1 1 0
		-0.20000000000000001 1 0
		;
createNode transform -n "c_Rt_eyebrows_03_FRAME_lockzyfy" -p "c_Rt_eyebrows_03_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Rt_eyebrows_03_FRAME_lockzyfyShape" -p "c_Rt_eyebrows_03_FRAME_lockzyfy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 0.20000000000000001 0
		-1 -0.20000000000000001 0
		1 -0.20000000000000001 0
		1 0.20000000000000001 0
		-1 0.20000000000000001 0
		;
createNode transform -n "c_Rt_eyebrows_03_FRAME_lockzxfx" -p "c_Rt_eyebrows_03_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Rt_eyebrows_03_FRAME_lockzxfxShape" -p "c_Rt_eyebrows_03_FRAME_lockzxfx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 1 0
		-0.20000000000000001 -1 0
		0.20000000000000001 -1 0
		0.20000000000000001 1 0
		-0.20000000000000001 1 0
		;
createNode transform -n "c_Rt_eyebrows_03_FRAME_lockzyfyzx" -p "c_Rt_eyebrows_03_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Rt_eyebrows_03_FRAME_lockzyfyzxShape" -p "c_Rt_eyebrows_03_FRAME_lockzyfyzx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 0.20000000000000001 0
		-1 -0.20000000000000001 0
		0.20000000000000001 -0.20000000000000001 0
		0.20000000000000001 0.20000000000000001 0
		-1 0.20000000000000001 0
		;
createNode transform -n "c_Rt_eyebrows_03_FRAME_lockzyfyfx" -p "c_Rt_eyebrows_03_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Rt_eyebrows_03_FRAME_lockzyfyfxShape" -p "c_Rt_eyebrows_03_FRAME_lockzyfyfx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 0.20000000000000001 0
		-0.20000000000000001 -0.20000000000000001 0
		1 -0.20000000000000001 0
		1 0.20000000000000001 0
		-0.20000000000000001 0.20000000000000001 0
		;
createNode transform -n "c_Rt_eyebrows_03_FRAME_lockzxfxzy" -p "c_Rt_eyebrows_03_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Rt_eyebrows_03_FRAME_lockzxfxzyShape" -p "c_Rt_eyebrows_03_FRAME_lockzxfxzy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 0.20000000000000001 0
		-0.20000000000000001 -1 0
		0.20000000000000001 -1 0
		0.20000000000000001 0.20000000000000001 0
		-0.20000000000000001 0.20000000000000001 0
		;
createNode transform -n "c_Rt_eyebrows_03_FRAME_lockzxfxfy" -p "c_Rt_eyebrows_03_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Rt_eyebrows_03_FRAME_lockzxfxfyShape" -p "c_Rt_eyebrows_03_FRAME_lockzxfxfy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 1 0
		-0.20000000000000001 -0.20000000000000001 0
		0.20000000000000001 -0.20000000000000001 0
		0.20000000000000001 1 0
		-0.20000000000000001 1 0
		;
createNode transform -n "c_Rt_eyebrows_03_CTRL_up" -p "c_Rt_eyebrows_03_FRAME";
	setAttr ".t" -type "double3" 0 2.2 0 ;
createNode nurbsCurve -n "curveShape61" -p "c_Rt_eyebrows_03_CTRL_up";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_eyebrows_03_LOC_up" -p "c_Rt_eyebrows_03_CTRL_up";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_eyebrows_03_CTRL_dn" -p "c_Rt_eyebrows_03_FRAME";
	setAttr ".t" -type "double3" 0 -2.2 0 ;
createNode nurbsCurve -n "curveShape62" -p "c_Rt_eyebrows_03_CTRL_dn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_eyebrows_03_LOC_dn" -p "c_Rt_eyebrows_03_CTRL_dn";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_eyebrows_03_CTRL_lf" -p "c_Rt_eyebrows_03_FRAME";
	setAttr ".t" -type "double3" -2.2 0 0 ;
createNode nurbsCurve -n "curveShape63" -p "c_Rt_eyebrows_03_CTRL_lf";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_eyebrows_03_LOC_lf" -p "c_Rt_eyebrows_03_CTRL_lf";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_eyebrows_03_CTRL_lfup" -p "c_Rt_eyebrows_03_FRAME";
	setAttr ".t" -type "double3" -2.2 2.2 0 ;
createNode nurbsCurve -n "curveShape64" -p "c_Rt_eyebrows_03_CTRL_lfup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_eyebrows_03_LOC_lfup" -p "c_Rt_eyebrows_03_CTRL_lfup";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_eyebrows_03_CTRL_rt" -p "c_Rt_eyebrows_03_FRAME";
	setAttr ".t" -type "double3" 2.2 0 0 ;
createNode nurbsCurve -n "curveShape65" -p "c_Rt_eyebrows_03_CTRL_rt";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_eyebrows_03_LOC_rt" -p "c_Rt_eyebrows_03_CTRL_rt";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_eyebrows_03_CTRL_rtup" -p "c_Rt_eyebrows_03_FRAME";
	setAttr ".t" -type "double3" 2.2 2.2 0 ;
createNode nurbsCurve -n "curveShape66" -p "c_Rt_eyebrows_03_CTRL_rtup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_eyebrows_03_LOC_rtup" -p "c_Rt_eyebrows_03_CTRL_rtup";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_eyebrows_03_CTRL_lfdn" -p "c_Rt_eyebrows_03_FRAME";
	setAttr ".t" -type "double3" -2.2 -2.2 0 ;
createNode nurbsCurve -n "curveShape67" -p "c_Rt_eyebrows_03_CTRL_lfdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_eyebrows_03_LOC_lfdn" -p "c_Rt_eyebrows_03_CTRL_lfdn";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_eyebrows_03_CTRL_rtdn" -p "c_Rt_eyebrows_03_FRAME";
	setAttr ".t" -type "double3" 2.2 -2.2 0 ;
createNode nurbsCurve -n "curveShape68" -p "c_Rt_eyebrows_03_CTRL_rtdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_eyebrows_03_LOC_rtdn" -p "c_Rt_eyebrows_03_CTRL_rtdn";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_eyebrows_03_CTRL_fourAxisup" -p "c_Rt_eyebrows_03_FRAME";
	setAttr ".t" -type "double3" 0 4.4 0 ;
createNode nurbsCurve -n "curveShape69" -p "c_Rt_eyebrows_03_CTRL_fourAxisup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_eyebrows_03_LOC_fourAxis_up" -p "c_Rt_eyebrows_03_CTRL_fourAxisup";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_eyebrows_03_CTRL_fourAxisdn" -p "c_Rt_eyebrows_03_FRAME";
	setAttr ".t" -type "double3" 0 -4.4 0 ;
createNode nurbsCurve -n "curveShape70" -p "c_Rt_eyebrows_03_CTRL_fourAxisdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_eyebrows_03_LOC_fourAxis_dn" -p "c_Rt_eyebrows_03_CTRL_fourAxisdn";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_eyebrows_03_CTRL_fourAxislf" -p "c_Rt_eyebrows_03_FRAME";
	setAttr ".t" -type "double3" -4.4 0 0 ;
createNode nurbsCurve -n "curveShape71" -p "c_Rt_eyebrows_03_CTRL_fourAxislf";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_eyebrows_03_LOC_fourAxis_lf" -p "c_Rt_eyebrows_03_CTRL_fourAxislf";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_eyebrows_03_CTRL_fourAxisrt" -p "c_Rt_eyebrows_03_FRAME";
	setAttr ".t" -type "double3" 4.4 0 0 ;
createNode nurbsCurve -n "curveShape72" -p "c_Rt_eyebrows_03_CTRL_fourAxisrt";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_eyebrows_03_LOC_fourAxis_rt" -p "c_Rt_eyebrows_03_CTRL_fourAxisrt";
	setAttr -k off ".v" no;
createNode transform -n "c_nose_M_CTRL_GRP" -p "head_CTRL";
	addAttr -ci true -sn "T1" -ln "T1" -at "double";
	addAttr -ci true -sn "T2" -ln "T2" -at "double";
	addAttr -ci true -k true -sn "T3" -ln "T3" -at "double";
	addAttr -ci true -k true -sn "R1" -ln "R1" -at "double";
	addAttr -ci true -k true -sn "R2" -ln "R2" -at "double";
	addAttr -ci true -k true -sn "R3" -ln "R3" -at "double";
	addAttr -ci true -sn "S1" -ln "S1" -at "double";
	addAttr -ci true -sn "S2" -ln "S2" -at "double";
	addAttr -ci true -sn "S3" -ln "S3" -at "double";
	setAttr ".rp" -type "double3" 0 -0.028874163260878521 0.001441099348299309 ;
	setAttr ".sp" -type "double3" 0 -0.028874163260878521 0.001441099348299309 ;
	setAttr -k on ".T1";
	setAttr -k on ".T2";
	setAttr -k on ".S1" 1;
	setAttr -k on ".S2" 1;
	setAttr -k on ".S3" 1;
createNode transform -n "c_nose_M_CTRL" -p "c_nose_M_CTRL_GRP";
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr ".rp" -type "double3" 0 -0.12516516994152505 0.017959868467468703 ;
	setAttr ".sp" -type "double3" 0 -0.12516516994152505 0.017959868467468703 ;
createNode nurbsCurve -n "c_nose_M_CTRLShape" -p "c_nose_M_CTRL";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.29062734822418668 0.11267173806920706 0.017959868467468668
		-4.6891228131148182e-017 0.3397221900345222 0.017959868467468627
		-0.29062734822418634 0.11267173806920727 0.017959868467468668
		-0.48400929250002661 -0.29647634652645544 0.017959868467468741
		-0.29062734822418645 -0.39747051655627913 0.017959868467468745
		-1.2384507441821144e-016 -0.35784931168577205 0.017959868467468731
		0.29062734822418612 -0.39747051655627924 0.017959868467468745
		0.48400929250002661 -0.29647634652645577 0.017959868467468741
		0.29062734822418668 0.11267173806920706 0.017959868467468668
		-4.6891228131148182e-017 0.3397221900345222 0.017959868467468627
		-0.29062734822418634 0.11267173806920727 0.017959868467468668
		;
createNode transform -n "c_Lf_nosewing_CTRL_GRP" -p "c_nose_M_CTRL";
	addAttr -ci true -k true -sn "T1" -ln "T1" -at "double";
	addAttr -ci true -k true -sn "T2" -ln "T2" -at "double";
	addAttr -ci true -k true -sn "T3" -ln "T3" -at "double";
	addAttr -ci true -k true -sn "R1" -ln "R1" -at "double";
	addAttr -ci true -k true -sn "R2" -ln "R2" -at "double";
	addAttr -ci true -k true -sn "R3" -ln "R3" -at "double";
	addAttr -ci true -sn "S1" -ln "S1" -at "double";
	addAttr -ci true -sn "S2" -ln "S2" -at "double";
	addAttr -ci true -sn "S3" -ln "S3" -at "double";
	setAttr ".rp" -type "double3" 0.27062691464421684 -0.14482811692132733 0.017959868467468706 ;
	setAttr ".sp" -type "double3" 0.27062691464421684 -0.14482811692132733 0.017959868467468706 ;
	setAttr -k on ".S1" 1;
	setAttr -k on ".S2" 1;
	setAttr -k on ".S3" 1;
createNode transform -n "c_Lf_nosewing_CTRL" -p "c_Lf_nosewing_CTRL_GRP";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".rp" -type "double3" 0.27062691464421684 -0.14482811692132733 0.017959868467468706 ;
	setAttr ".sp" -type "double3" 0.2706269146442169 -0.14482811692132735 0.017959868467468706 ;
createNode nurbsCurve -n "c_Lf_nosewing_CTRLShape" -p "c_Lf_nosewing_CTRL";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.32359927886417877 -0.098656004976716005 0.017959868467468703
		0.20648845155715095 -0.018191076084209501 0.017959868467468689
		0.17464760174969132 -0.060029063534832852 0.017959868467468696
		0.18891101104759189 -0.12431628288427127 0.017959868467468703
		0.19327118249571287 -0.22838213600570945 0.01795986846746872
		0.19448084549824274 -0.27146515775844515 0.017959868467468727
		0.32359927886417861 -0.26418252442210644 0.017959868467468727
		0.36660622753874239 -0.20248396374313127 0.01795986846746872
		0.32359927886417877 -0.098656004976716005 0.017959868467468703
		0.20648845155715095 -0.018191076084209501 0.017959868467468689
		0.17464760174969132 -0.060029063534832852 0.017959868467468696
		;
createNode transform -n "c_Rt_nosewing_CTRL_GRP" -p "c_nose_M_CTRL";
	addAttr -ci true -k true -sn "T1" -ln "T1" -at "double";
	addAttr -ci true -k true -sn "T2" -ln "T2" -at "double";
	addAttr -ci true -k true -sn "T3" -ln "T3" -at "double";
	addAttr -ci true -k true -sn "R1" -ln "R1" -at "double";
	addAttr -ci true -k true -sn "R2" -ln "R2" -at "double";
	addAttr -ci true -k true -sn "R3" -ln "R3" -at "double";
	addAttr -ci true -sn "S1" -ln "S1" -at "double";
	addAttr -ci true -sn "S2" -ln "S2" -at "double";
	addAttr -ci true -sn "S3" -ln "S3" -at "double";
	setAttr ".rp" -type "double3" -0.27062691464421684 -0.14482811692132735 0.017959868467468706 ;
	setAttr ".sp" -type "double3" -0.27062691464421684 -0.14482811692132735 0.017959868467468706 ;
	setAttr -k on ".S1" 1;
	setAttr -k on ".S2" 1;
	setAttr -k on ".S3" 1;
createNode transform -n "c_Rt_nosewing_CTRL" -p "c_Rt_nosewing_CTRL_GRP";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".rp" -type "double3" -0.27062691464421684 -0.14482811692132735 0.017959868467468706 ;
	setAttr ".sp" -type "double3" -0.2706269146442169 -0.14482811692132735 0.017959868467468706 ;
createNode nurbsCurve -n "c_Rt_nosewing_CTRLShape" -p "c_Rt_nosewing_CTRL";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-0.32359927886417877 -0.098656004976716019 0.017959868467468703
		-0.20648845155715093 -0.018191076084209522 0.017959868467468689
		-0.17464760174969132 -0.06002906353483288 0.017959868467468696
		-0.18891101104759189 -0.1243162828842713 0.017959868467468703
		-0.19327118249571287 -0.22838213600570945 0.01795986846746872
		-0.19448084549824271 -0.27146515775844521 0.017959868467468727
		-0.32359927886417861 -0.26418252442210649 0.017959868467468727
		-0.36660622753874239 -0.20248396374313132 0.01795986846746872
		-0.32359927886417877 -0.098656004976716019 0.017959868467468703
		-0.20648845155715093 -0.018191076084209522 0.017959868467468689
		-0.17464760174969132 -0.06002906353483288 0.017959868467468696
		;
createNode transform -n "GRP_c_nose_FRAME" -p "c_nose_M_CTRL";
	setAttr ".t" -type "double3" 0 -0.055342470515774532 0 ;
	setAttr ".s" -type "double3" 0.23925466036442045 0.23925466036442045 0.23925466036442045 ;
createNode transform -n "c_nose_FRAME" -p "GRP_c_nose_FRAME";
	addAttr -ci true -sn "up" -ln "up" -min 0 -at "double";
	addAttr -ci true -sn "dn" -ln "dn" -min 0 -at "double";
	addAttr -ci true -sn "lf" -ln "lf" -min 0 -at "double";
	addAttr -ci true -sn "rt" -ln "rt" -min 0 -at "double";
	addAttr -ci true -sn "lfup" -ln "lfup" -min 0 -at "double";
	addAttr -ci true -sn "rtup" -ln "rtup" -min 0 -at "double";
	addAttr -ci true -sn "lfdn" -ln "lfdn" -min 0 -at "double";
	addAttr -ci true -sn "rtdn" -ln "rtdn" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_up" -ln "fourAxis_up" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_dn" -ln "fourAxis_dn" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_lf" -ln "fourAxis_lf" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_rt" -ln "fourAxis_rt" -min 0 -at "double";
	addAttr -ci true -sn "up_Vis" -ln "up_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "dn_Vis" -ln "dn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lf_Vis" -ln "lf_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lfup_Vis" -ln "lfup_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rt_Vis" -ln "rt_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rtup_Vis" -ln "rtup_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lfdn_Vis" -ln "lfdn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rtdn_Vis" -ln "rtdn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_up_Vis" -ln "fourAxis_up_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_dn_Vis" -ln "fourAxis_dn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_lf_Vis" -ln "fourAxis_lf_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_rt_Vis" -ln "fourAxis_rt_Vis" -min 0 -max 1 -at "bool";
	setAttr -k on ".up";
	setAttr -k on ".dn";
	setAttr -k on ".lf";
	setAttr -k on ".rt";
	setAttr -k on ".lfup";
	setAttr -k on ".rtup";
	setAttr -k on ".lfdn";
	setAttr -k on ".rtdn";
	setAttr -k on ".fourAxis_up";
	setAttr -k on ".fourAxis_dn";
	setAttr -k on ".fourAxis_lf";
	setAttr -k on ".fourAxis_rt";
	setAttr -cb on ".up_Vis";
	setAttr -cb on ".dn_Vis";
	setAttr -cb on ".lf_Vis";
	setAttr -cb on ".lfup_Vis";
	setAttr -cb on ".rt_Vis";
	setAttr -cb on ".rtup_Vis";
	setAttr -cb on ".lfdn_Vis";
	setAttr -cb on ".rtdn_Vis";
	setAttr -cb on ".fourAxis_up_Vis";
	setAttr -cb on ".fourAxis_dn_Vis";
	setAttr -cb on ".fourAxis_lf_Vis";
	setAttr -cb on ".fourAxis_rt_Vis";
createNode nurbsCurve -n "c_nose_FRAMEShape" -p "c_nose_FRAME";
	setAttr -k off ".v" no;
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode transform -n "GRP_c_nose_CTRL" -p "c_nose_FRAME";
	addAttr -ci true -sn "T1" -ln "T1" -at "double";
	addAttr -ci true -sn "T2" -ln "T2" -at "double";
	addAttr -ci true -sn "T3" -ln "T3" -at "double";
	addAttr -ci true -sn "R1" -ln "R1" -at "double";
	addAttr -ci true -sn "R2" -ln "R2" -at "double";
	addAttr -ci true -sn "R3" -ln "R3" -at "double";
	addAttr -ci true -sn "S1" -ln "S1" -at "double";
	addAttr -ci true -sn "S2" -ln "S2" -at "double";
	addAttr -ci true -sn "S3" -ln "S3" -at "double";
	setAttr -k on ".T1";
	setAttr -k on ".T2";
	setAttr -k on ".T3";
	setAttr -k on ".R1";
	setAttr -k on ".R2";
	setAttr -k on ".R3";
	setAttr -k on ".S1" 1;
	setAttr -k on ".S2" 1;
	setAttr -k on ".S3" 1;
createNode transform -n "c_nose_CTRL" -p "GRP_c_nose_CTRL";
	addAttr -ci true -sn "frameSelectAble" -ln "frameSelectAble" -min 0 -max 2 -en 
		"normal:template:reference" -at "enum";
	setAttr ".mntl" -type "double3" -1 -1 0 ;
	setAttr ".mxtl" -type "double3" 1 1 0 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
	setAttr ".frameSelectAble" 2;
createNode nurbsCurve -n "c_nose_CTRLShape" -p "c_nose_CTRL";
	setAttr -k off ".v" no;
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		1 32 0 no 3
		33 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32
		33
		-0.050000000000000003 0.050000000000000003 0
		-0.050000000000000003 0.15000000000000002 0
		-0.10000000000000001 0.15000000000000002 0
		0 0.25 0
		0.10000000000000001 0.15000000000000002 0
		0.050000000000000003 0.15000000000000002 0
		0.050000000000000003 0.050000000000000003 0
		0.20000000000000001 0.20000000000000001 0
		0.050000000000000003 0.050000000000000003 0
		0.15000000000000002 0.050000000000000003 0
		0.15000000000000002 0.10000000000000001 0
		0.25 0 0
		0.15000000000000002 -0.10000000000000001 0
		0.15000000000000002 -0.050000000000000003 0
		0.050000000000000003 -0.050000000000000003 0
		0.20000000000000001 -0.20000000000000001 0
		0.050000000000000003 -0.050000000000000003 0
		0.050000000000000003 -0.15000000000000002 0
		0.10000000000000001 -0.15000000000000002 0
		0 -0.25 0
		-0.10000000000000001 -0.15000000000000002 0
		-0.050000000000000003 -0.15000000000000002 0
		-0.050000000000000003 -0.050000000000000003 0
		-0.20000000000000001 -0.20000000000000001 0
		-0.050000000000000003 -0.050000000000000003 0
		-0.15000000000000002 -0.050000000000000003 0
		-0.15000000000000002 -0.10000000000000001 0
		-0.25 0 0
		-0.15000000000000002 0.10000000000000001 0
		-0.15000000000000002 0.050000000000000003 0
		-0.050000000000000003 0.050000000000000003 0
		-0.20000000000000001 0.20000000000000001 0
		-0.050000000000000003 0.050000000000000003 0
		;
createNode nurbsCurve -n "c_nose_CTRL_Shape" -p "c_nose_CTRL";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 24;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.55994815214896687 0.25614707919128571 0.037527505355205971
		7.771658485634142e-016 1.2341558252088312 -0.060310679083480506
		-0.55994815214896643 0.25614707919128604 0.037527505355205971
		-0.5848332646916915 -0.14986124528487324 0.037527505355205944
		-0.73299009201642862 -0.67873842776343496 0.037527505355205944
		-6.3445537365991924e-017 -0.72788695885914212 0.037527505355205812
		0.73299009201642829 -0.67873842776343496 0.037527505355205944
		0.5848332646916915 -0.14986124528487405 0.037527505355205944
		0.55994815214896687 0.25614707919128571 0.037527505355205971
		7.771658485634142e-016 1.2341558252088312 -0.060310679083480506
		-0.55994815214896643 0.25614707919128604 0.037527505355205971
		;
createNode transform -n "c_nose_FRAME_lockzy" -p "c_nose_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_nose_FRAME_lockzyShape" -p "c_nose_FRAME_lockzy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 0.20000000000000001 0
		-1 -1 0
		1 -1 0
		1 0.20000000000000001 0
		-1 0.20000000000000001 0
		;
createNode transform -n "c_nose_FRAME_lockfy" -p "c_nose_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_nose_FRAME_lockfyShape" -p "c_nose_FRAME_lockfy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -0.20000000000000001 0
		1 -0.20000000000000001 0
		1 1 0
		-1 1 0
		;
createNode transform -n "c_nose_FRAME_lockzx" -p "c_nose_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_nose_FRAME_lockzxShape" -p "c_nose_FRAME_lockzx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		0.20000000000000001 -1 0
		0.20000000000000001 1 0
		-1 1 0
		;
createNode transform -n "c_nose_FRAME_lockfx" -p "c_nose_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_nose_FRAME_lockfxShape" -p "c_nose_FRAME_lockfx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 1 0
		-0.20000000000000001 -1 0
		1 -1 0
		1 1 0
		-0.20000000000000001 1 0
		;
createNode transform -n "c_nose_FRAME_lockzyfy" -p "c_nose_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_nose_FRAME_lockzyfyShape" -p "c_nose_FRAME_lockzyfy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 0.20000000000000001 0
		-1 -0.20000000000000001 0
		1 -0.20000000000000001 0
		1 0.20000000000000001 0
		-1 0.20000000000000001 0
		;
createNode transform -n "c_nose_FRAME_lockzxfx" -p "c_nose_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_nose_FRAME_lockzxfxShape" -p "c_nose_FRAME_lockzxfx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 1 0
		-0.20000000000000001 -1 0
		0.20000000000000001 -1 0
		0.20000000000000001 1 0
		-0.20000000000000001 1 0
		;
createNode transform -n "c_nose_FRAME_lockzyfyzx" -p "c_nose_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_nose_FRAME_lockzyfyzxShape" -p "c_nose_FRAME_lockzyfyzx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 0.20000000000000001 0
		-1 -0.20000000000000001 0
		0.20000000000000001 -0.20000000000000001 0
		0.20000000000000001 0.20000000000000001 0
		-1 0.20000000000000001 0
		;
createNode transform -n "c_nose_FRAME_lockzyfyfx" -p "c_nose_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_nose_FRAME_lockzyfyfxShape" -p "c_nose_FRAME_lockzyfyfx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 0.20000000000000001 0
		-0.20000000000000001 -0.20000000000000001 0
		1 -0.20000000000000001 0
		1 0.20000000000000001 0
		-0.20000000000000001 0.20000000000000001 0
		;
createNode transform -n "c_nose_FRAME_lockzxfxzy" -p "c_nose_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_nose_FRAME_lockzxfxzyShape" -p "c_nose_FRAME_lockzxfxzy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 0.20000000000000001 0
		-0.20000000000000001 -1 0
		0.20000000000000001 -1 0
		0.20000000000000001 0.20000000000000001 0
		-0.20000000000000001 0.20000000000000001 0
		;
createNode transform -n "c_nose_FRAME_lockzxfxfy" -p "c_nose_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_nose_FRAME_lockzxfxfyShape" -p "c_nose_FRAME_lockzxfxfy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 1 0
		-0.20000000000000001 -0.20000000000000001 0
		0.20000000000000001 -0.20000000000000001 0
		0.20000000000000001 1 0
		-0.20000000000000001 1 0
		;
createNode transform -n "c_nose_CTRL_up" -p "c_nose_FRAME";
	setAttr ".t" -type "double3" 0 2.2 0 ;
createNode nurbsCurve -n "curveShape529" -p "c_nose_CTRL_up";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_nose_LOC_up" -p "c_nose_CTRL_up";
	setAttr -k off ".v" no;
createNode transform -n "c_nose_CTRL_dn" -p "c_nose_FRAME";
	setAttr ".t" -type "double3" 0 -2.2 0 ;
createNode nurbsCurve -n "curveShape530" -p "c_nose_CTRL_dn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_nose_LOC_dn" -p "c_nose_CTRL_dn";
	setAttr -k off ".v" no;
createNode transform -n "c_nose_CTRL_lf" -p "c_nose_FRAME";
	setAttr ".t" -type "double3" -2.2 0 0 ;
createNode nurbsCurve -n "curveShape531" -p "c_nose_CTRL_lf";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_nose_LOC_lf" -p "c_nose_CTRL_lf";
	setAttr -k off ".v" no;
createNode transform -n "c_nose_CTRL_lfup" -p "c_nose_FRAME";
	setAttr ".t" -type "double3" -2.2 2.2 0 ;
createNode nurbsCurve -n "curveShape532" -p "c_nose_CTRL_lfup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_nose_LOC_lfup" -p "c_nose_CTRL_lfup";
	setAttr -k off ".v" no;
createNode transform -n "c_nose_CTRL_rt" -p "c_nose_FRAME";
	setAttr ".t" -type "double3" 2.2 0 0 ;
createNode nurbsCurve -n "curveShape533" -p "c_nose_CTRL_rt";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_nose_LOC_rt" -p "c_nose_CTRL_rt";
	setAttr -k off ".v" no;
createNode transform -n "c_nose_CTRL_rtup" -p "c_nose_FRAME";
	setAttr ".t" -type "double3" 2.2 2.2 0 ;
createNode nurbsCurve -n "curveShape534" -p "c_nose_CTRL_rtup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_nose_LOC_rtup" -p "c_nose_CTRL_rtup";
	setAttr -k off ".v" no;
createNode transform -n "c_nose_CTRL_lfdn" -p "c_nose_FRAME";
	setAttr ".t" -type "double3" -2.2 -2.2 0 ;
createNode nurbsCurve -n "curveShape535" -p "c_nose_CTRL_lfdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_nose_LOC_lfdn" -p "c_nose_CTRL_lfdn";
	setAttr -k off ".v" no;
createNode transform -n "c_nose_CTRL_rtdn" -p "c_nose_FRAME";
	setAttr ".t" -type "double3" 2.2 -2.2 0 ;
createNode nurbsCurve -n "curveShape536" -p "c_nose_CTRL_rtdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_nose_LOC_rtdn" -p "c_nose_CTRL_rtdn";
	setAttr -k off ".v" no;
createNode transform -n "c_nose_CTRL_fourAxisup" -p "c_nose_FRAME";
	setAttr ".t" -type "double3" 0 4.4 0 ;
createNode nurbsCurve -n "curveShape537" -p "c_nose_CTRL_fourAxisup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_nose_LOC_fourAxis_up" -p "c_nose_CTRL_fourAxisup";
	setAttr -k off ".v" no;
createNode transform -n "c_nose_CTRL_fourAxisdn" -p "c_nose_FRAME";
	setAttr ".t" -type "double3" 0 -4.4 0 ;
createNode nurbsCurve -n "curveShape538" -p "c_nose_CTRL_fourAxisdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_nose_LOC_fourAxis_dn" -p "c_nose_CTRL_fourAxisdn";
	setAttr -k off ".v" no;
createNode transform -n "c_nose_CTRL_fourAxislf" -p "c_nose_FRAME";
	setAttr ".t" -type "double3" -4.4 0 0 ;
createNode nurbsCurve -n "curveShape539" -p "c_nose_CTRL_fourAxislf";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_nose_LOC_fourAxis_lf" -p "c_nose_CTRL_fourAxislf";
	setAttr -k off ".v" no;
createNode transform -n "c_nose_CTRL_fourAxisrt" -p "c_nose_FRAME";
	setAttr ".t" -type "double3" 4.4 0 0 ;
createNode nurbsCurve -n "curveShape540" -p "c_nose_CTRL_fourAxisrt";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_nose_LOC_fourAxis_rt" -p "c_nose_CTRL_fourAxisrt";
	setAttr -k off ".v" no;
createNode transform -n "GRP_c_Lf_cheek_FRAME" -p "head_CTRL";
	setAttr ".t" -type "double3" 0.93258728545787273 -0.30649805431506916 2.3997675305669668e-016 ;
	setAttr ".s" -type "double3" 0.25 0.25 0.25 ;
createNode transform -n "c_Lf_cheek_FRAME" -p "GRP_c_Lf_cheek_FRAME";
	addAttr -ci true -sn "up" -ln "up" -min 0 -at "double";
	addAttr -ci true -sn "dn" -ln "dn" -min 0 -at "double";
	addAttr -ci true -sn "lf" -ln "lf" -min 0 -at "double";
	addAttr -ci true -sn "rt" -ln "rt" -min 0 -at "double";
	addAttr -ci true -sn "lfup" -ln "lfup" -min 0 -at "double";
	addAttr -ci true -sn "rtup" -ln "rtup" -min 0 -at "double";
	addAttr -ci true -sn "lfdn" -ln "lfdn" -min 0 -at "double";
	addAttr -ci true -sn "rtdn" -ln "rtdn" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_up" -ln "fourAxis_up" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_dn" -ln "fourAxis_dn" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_lf" -ln "fourAxis_lf" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_rt" -ln "fourAxis_rt" -min 0 -at "double";
	addAttr -ci true -sn "up_Vis" -ln "up_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "dn_Vis" -ln "dn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lf_Vis" -ln "lf_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lfup_Vis" -ln "lfup_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rt_Vis" -ln "rt_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rtup_Vis" -ln "rtup_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lfdn_Vis" -ln "lfdn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rtdn_Vis" -ln "rtdn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_up_Vis" -ln "fourAxis_up_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_dn_Vis" -ln "fourAxis_dn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_lf_Vis" -ln "fourAxis_lf_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_rt_Vis" -ln "fourAxis_rt_Vis" -min 0 -max 1 -at "bool";
	setAttr -k on ".up";
	setAttr -k on ".dn";
	setAttr -k on ".lf";
	setAttr -k on ".rt";
	setAttr -k on ".lfup";
	setAttr -k on ".rtup";
	setAttr -k on ".lfdn";
	setAttr -k on ".rtdn";
	setAttr -k on ".fourAxis_up";
	setAttr -k on ".fourAxis_dn";
	setAttr -k on ".fourAxis_lf";
	setAttr -k on ".fourAxis_rt";
	setAttr -cb on ".up_Vis";
	setAttr -cb on ".dn_Vis";
	setAttr -cb on ".lf_Vis";
	setAttr -cb on ".lfup_Vis";
	setAttr -cb on ".rt_Vis";
	setAttr -cb on ".rtup_Vis";
	setAttr -cb on ".lfdn_Vis";
	setAttr -cb on ".rtdn_Vis";
	setAttr -cb on ".fourAxis_up_Vis";
	setAttr -cb on ".fourAxis_dn_Vis";
	setAttr -cb on ".fourAxis_lf_Vis";
	setAttr -cb on ".fourAxis_rt_Vis";
createNode nurbsCurve -n "c_Lf_cheek_FRAMEShape" -p "c_Lf_cheek_FRAME";
	setAttr -k off ".v" no;
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode transform -n "GRP_c_Lf_cheek_CTRL" -p "c_Lf_cheek_FRAME";
	addAttr -ci true -k true -sn "T1" -ln "T1" -at "double";
	addAttr -ci true -k true -sn "T2" -ln "T2" -at "double";
	addAttr -ci true -k true -sn "T3" -ln "T3" -at "double";
	addAttr -ci true -k true -sn "R1" -ln "R1" -at "double";
	addAttr -ci true -k true -sn "R2" -ln "R2" -at "double";
	addAttr -ci true -k true -sn "R3" -ln "R3" -at "double";
	addAttr -ci true -sn "S1" -ln "S1" -at "double";
	addAttr -ci true -sn "S2" -ln "S2" -at "double";
	addAttr -ci true -sn "S3" -ln "S3" -at "double";
	setAttr -k on ".S1" 1;
	setAttr -k on ".S2" 1;
	setAttr -k on ".S3" 1;
createNode transform -n "c_Lf_cheek_CTRL" -p "GRP_c_Lf_cheek_CTRL";
	addAttr -ci true -sn "frameSelectAble" -ln "frameSelectAble" -min 0 -max 2 -en 
		"normal:template:reference" -at "enum";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".mntl" -type "double3" -1 -1 0 ;
	setAttr ".mxtl" -type "double3" 1 1 0 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
	setAttr ".frameSelectAble" 2;
createNode nurbsCurve -n "c_Lf_cheek_CTRLShape" -p "c_Lf_cheek_CTRL";
	setAttr -k off ".v" no;
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		1 32 0 no 3
		33 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32
		33
		-0.050000000000000003 0.050000000000000003 0
		-0.050000000000000003 0.15000000000000002 0
		-0.10000000000000001 0.15000000000000002 0
		0 0.25 0
		0.10000000000000001 0.15000000000000002 0
		0.050000000000000003 0.15000000000000002 0
		0.050000000000000003 0.050000000000000003 0
		0.20000000000000001 0.20000000000000001 0
		0.050000000000000003 0.050000000000000003 0
		0.15000000000000002 0.050000000000000003 0
		0.15000000000000002 0.10000000000000001 0
		0.25 0 0
		0.15000000000000002 -0.10000000000000001 0
		0.15000000000000002 -0.050000000000000003 0
		0.050000000000000003 -0.050000000000000003 0
		0.20000000000000001 -0.20000000000000001 0
		0.050000000000000003 -0.050000000000000003 0
		0.050000000000000003 -0.15000000000000002 0
		0.10000000000000001 -0.15000000000000002 0
		0 -0.25 0
		-0.10000000000000001 -0.15000000000000002 0
		-0.050000000000000003 -0.15000000000000002 0
		-0.050000000000000003 -0.050000000000000003 0
		-0.20000000000000001 -0.20000000000000001 0
		-0.050000000000000003 -0.050000000000000003 0
		-0.15000000000000002 -0.050000000000000003 0
		-0.15000000000000002 -0.10000000000000001 0
		-0.25 0 0
		-0.15000000000000002 0.10000000000000001 0
		-0.15000000000000002 0.050000000000000003 0
		-0.050000000000000003 0.050000000000000003 0
		-0.20000000000000001 0.20000000000000001 0
		-0.050000000000000003 0.050000000000000003 0
		;
createNode nurbsCurve -n "c_eyeStretch_CTRLShape" -p "c_Lf_cheek_CTRL";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.74451401525385352 0.82640218109965946 -1.0513648591768327e-016
		-0.0050372851181066979 1.1687091724858449 -1.4649719089436598e-016
		-0.52703170880766381 0.82640218109966035 -1.0513648591768327e-016
		-0.54116960830062866 5.3339199690283546e-016 5.1587273534703039e-018
		-0.52703170880766381 -0.82640218109966024 1.0166703896572956e-016
		-0.13607543482114393 -1.1687091724858454 1.4302774394241202e-016
		0.66963507256640542 -0.82640218109966046 1.0166703896572956e-016
		0.99616838124092622 -5.6956013580869987e-016 5.1587273534703039e-018
		0.74451401525385352 0.82640218109965946 -1.0513648591768327e-016
		-0.0050372851181066979 1.1687091724858449 -1.4649719089436598e-016
		-0.52703170880766381 0.82640218109966035 -1.0513648591768327e-016
		;
createNode transform -n "c_Lf_cheek_FRAME_lockzy" -p "c_Lf_cheek_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Lf_cheek_FRAME_lockzyShape" -p "c_Lf_cheek_FRAME_lockzy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 0.20000000000000001 0
		-1 -1 0
		1 -1 0
		1 0.20000000000000001 0
		-1 0.20000000000000001 0
		;
createNode transform -n "c_Lf_cheek_FRAME_lockfy" -p "c_Lf_cheek_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Lf_cheek_FRAME_lockfyShape" -p "c_Lf_cheek_FRAME_lockfy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -0.20000000000000001 0
		1 -0.20000000000000001 0
		1 1 0
		-1 1 0
		;
createNode transform -n "c_Lf_cheek_FRAME_lockzx" -p "c_Lf_cheek_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Lf_cheek_FRAME_lockzxShape" -p "c_Lf_cheek_FRAME_lockzx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		0.20000000000000001 -1 0
		0.20000000000000001 1 0
		-1 1 0
		;
createNode transform -n "c_Lf_cheek_FRAME_lockfx" -p "c_Lf_cheek_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Lf_cheek_FRAME_lockfxShape" -p "c_Lf_cheek_FRAME_lockfx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 1 0
		-0.20000000000000001 -1 0
		1 -1 0
		1 1 0
		-0.20000000000000001 1 0
		;
createNode transform -n "c_Lf_cheek_FRAME_lockzyfy" -p "c_Lf_cheek_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Lf_cheek_FRAME_lockzyfyShape" -p "c_Lf_cheek_FRAME_lockzyfy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 0.20000000000000001 0
		-1 -0.20000000000000001 0
		1 -0.20000000000000001 0
		1 0.20000000000000001 0
		-1 0.20000000000000001 0
		;
createNode transform -n "c_Lf_cheek_FRAME_lockzxfx" -p "c_Lf_cheek_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Lf_cheek_FRAME_lockzxfxShape" -p "c_Lf_cheek_FRAME_lockzxfx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 1 0
		-0.20000000000000001 -1 0
		0.20000000000000001 -1 0
		0.20000000000000001 1 0
		-0.20000000000000001 1 0
		;
createNode transform -n "c_Lf_cheek_FRAME_lockzyfyzx" -p "c_Lf_cheek_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Lf_cheek_FRAME_lockzyfyzxShape" -p "c_Lf_cheek_FRAME_lockzyfyzx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 0.20000000000000001 0
		-1 -0.20000000000000001 0
		0.20000000000000001 -0.20000000000000001 0
		0.20000000000000001 0.20000000000000001 0
		-1 0.20000000000000001 0
		;
createNode transform -n "c_Lf_cheek_FRAME_lockzyfyfx" -p "c_Lf_cheek_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Lf_cheek_FRAME_lockzyfyfxShape" -p "c_Lf_cheek_FRAME_lockzyfyfx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 0.20000000000000001 0
		-0.20000000000000001 -0.20000000000000001 0
		1 -0.20000000000000001 0
		1 0.20000000000000001 0
		-0.20000000000000001 0.20000000000000001 0
		;
createNode transform -n "c_Lf_cheek_FRAME_lockzxfxzy" -p "c_Lf_cheek_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Lf_cheek_FRAME_lockzxfxzyShape" -p "c_Lf_cheek_FRAME_lockzxfxzy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 0.20000000000000001 0
		-0.20000000000000001 -1 0
		0.20000000000000001 -1 0
		0.20000000000000001 0.20000000000000001 0
		-0.20000000000000001 0.20000000000000001 0
		;
createNode transform -n "c_Lf_cheek_FRAME_lockzxfxfy" -p "c_Lf_cheek_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Lf_cheek_FRAME_lockzxfxfyShape" -p "c_Lf_cheek_FRAME_lockzxfxfy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 1 0
		-0.20000000000000001 -0.20000000000000001 0
		0.20000000000000001 -0.20000000000000001 0
		0.20000000000000001 1 0
		-0.20000000000000001 1 0
		;
createNode transform -n "c_Lf_cheek_CTRL_up" -p "c_Lf_cheek_FRAME";
	setAttr ".t" -type "double3" 0 2.2 0 ;
createNode nurbsCurve -n "curveShape481" -p "c_Lf_cheek_CTRL_up";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_cheek_LOC_up" -p "c_Lf_cheek_CTRL_up";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_cheek_CTRL_dn" -p "c_Lf_cheek_FRAME";
	setAttr ".t" -type "double3" 0 -2.2 0 ;
createNode nurbsCurve -n "curveShape482" -p "c_Lf_cheek_CTRL_dn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_cheek_LOC_dn" -p "c_Lf_cheek_CTRL_dn";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_cheek_CTRL_lf" -p "c_Lf_cheek_FRAME";
	setAttr ".t" -type "double3" -2.2 0 0 ;
createNode nurbsCurve -n "curveShape483" -p "c_Lf_cheek_CTRL_lf";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_cheek_LOC_lf" -p "c_Lf_cheek_CTRL_lf";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_cheek_CTRL_lfup" -p "c_Lf_cheek_FRAME";
	setAttr ".t" -type "double3" -2.2 2.2 0 ;
createNode nurbsCurve -n "curveShape484" -p "c_Lf_cheek_CTRL_lfup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_cheek_LOC_lfup" -p "c_Lf_cheek_CTRL_lfup";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_cheek_CTRL_rt" -p "c_Lf_cheek_FRAME";
	setAttr ".t" -type "double3" 2.2 0 0 ;
createNode nurbsCurve -n "curveShape485" -p "c_Lf_cheek_CTRL_rt";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_cheek_LOC_rt" -p "c_Lf_cheek_CTRL_rt";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_cheek_CTRL_rtup" -p "c_Lf_cheek_FRAME";
	setAttr ".t" -type "double3" 2.2 2.2 0 ;
createNode nurbsCurve -n "curveShape486" -p "c_Lf_cheek_CTRL_rtup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_cheek_LOC_rtup" -p "c_Lf_cheek_CTRL_rtup";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_cheek_CTRL_lfdn" -p "c_Lf_cheek_FRAME";
	setAttr ".t" -type "double3" -2.2 -2.2 0 ;
createNode nurbsCurve -n "curveShape487" -p "c_Lf_cheek_CTRL_lfdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_cheek_LOC_lfdn" -p "c_Lf_cheek_CTRL_lfdn";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_cheek_CTRL_rtdn" -p "c_Lf_cheek_FRAME";
	setAttr ".t" -type "double3" 2.2 -2.2 0 ;
createNode nurbsCurve -n "curveShape488" -p "c_Lf_cheek_CTRL_rtdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_cheek_LOC_rtdn" -p "c_Lf_cheek_CTRL_rtdn";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_cheek_CTRL_fourAxisup" -p "c_Lf_cheek_FRAME";
	setAttr ".t" -type "double3" 0 4.4 0 ;
createNode nurbsCurve -n "curveShape489" -p "c_Lf_cheek_CTRL_fourAxisup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_cheek_LOC_fourAxis_up" -p "c_Lf_cheek_CTRL_fourAxisup";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_cheek_CTRL_fourAxisdn" -p "c_Lf_cheek_FRAME";
	setAttr ".t" -type "double3" 0 -4.4 0 ;
createNode nurbsCurve -n "curveShape490" -p "c_Lf_cheek_CTRL_fourAxisdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_cheek_LOC_fourAxis_dn" -p "c_Lf_cheek_CTRL_fourAxisdn";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_cheek_CTRL_fourAxislf" -p "c_Lf_cheek_FRAME";
	setAttr ".t" -type "double3" -4.4 0 0 ;
createNode nurbsCurve -n "curveShape491" -p "c_Lf_cheek_CTRL_fourAxislf";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_cheek_LOC_fourAxis_lf" -p "c_Lf_cheek_CTRL_fourAxislf";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_cheek_CTRL_fourAxisrt" -p "c_Lf_cheek_FRAME";
	setAttr ".t" -type "double3" 4.4 0 0 ;
createNode nurbsCurve -n "curveShape492" -p "c_Lf_cheek_CTRL_fourAxisrt";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_cheek_LOC_fourAxis_rt" -p "c_Lf_cheek_CTRL_fourAxisrt";
	setAttr -k off ".v" no;
createNode transform -n "GRP_c_Rt_cheek_FRAME" -p "head_CTRL";
	setAttr ".t" -type "double3" -0.93258728545787273 -0.30649805431506916 -1.2576774965054683e-016 ;
	setAttr ".r" -type "double3" 0 -180 0 ;
	setAttr ".s" -type "double3" 0.25 0.25 0.25 ;
createNode transform -n "c_Rt_cheek_FRAME" -p "GRP_c_Rt_cheek_FRAME";
	addAttr -ci true -sn "up" -ln "up" -min 0 -at "double";
	addAttr -ci true -sn "dn" -ln "dn" -min 0 -at "double";
	addAttr -ci true -sn "lf" -ln "lf" -min 0 -at "double";
	addAttr -ci true -sn "rt" -ln "rt" -min 0 -at "double";
	addAttr -ci true -sn "lfup" -ln "lfup" -min 0 -at "double";
	addAttr -ci true -sn "rtup" -ln "rtup" -min 0 -at "double";
	addAttr -ci true -sn "lfdn" -ln "lfdn" -min 0 -at "double";
	addAttr -ci true -sn "rtdn" -ln "rtdn" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_up" -ln "fourAxis_up" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_dn" -ln "fourAxis_dn" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_lf" -ln "fourAxis_lf" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_rt" -ln "fourAxis_rt" -min 0 -at "double";
	addAttr -ci true -sn "up_Vis" -ln "up_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "dn_Vis" -ln "dn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lf_Vis" -ln "lf_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lfup_Vis" -ln "lfup_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rt_Vis" -ln "rt_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rtup_Vis" -ln "rtup_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lfdn_Vis" -ln "lfdn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rtdn_Vis" -ln "rtdn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_up_Vis" -ln "fourAxis_up_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_dn_Vis" -ln "fourAxis_dn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_lf_Vis" -ln "fourAxis_lf_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_rt_Vis" -ln "fourAxis_rt_Vis" -min 0 -max 1 -at "bool";
	setAttr -k on ".up";
	setAttr -k on ".dn";
	setAttr -k on ".lf";
	setAttr -k on ".rt";
	setAttr -k on ".lfup";
	setAttr -k on ".rtup";
	setAttr -k on ".lfdn";
	setAttr -k on ".rtdn";
	setAttr -k on ".fourAxis_up";
	setAttr -k on ".fourAxis_dn";
	setAttr -k on ".fourAxis_lf";
	setAttr -k on ".fourAxis_rt";
	setAttr -cb on ".up_Vis";
	setAttr -cb on ".dn_Vis";
	setAttr -cb on ".lf_Vis";
	setAttr -cb on ".lfup_Vis";
	setAttr -cb on ".rt_Vis";
	setAttr -cb on ".rtup_Vis";
	setAttr -cb on ".lfdn_Vis";
	setAttr -cb on ".rtdn_Vis";
	setAttr -cb on ".fourAxis_up_Vis";
	setAttr -cb on ".fourAxis_dn_Vis";
	setAttr -cb on ".fourAxis_lf_Vis";
	setAttr -cb on ".fourAxis_rt_Vis";
createNode nurbsCurve -n "c_Rt_cheek_FRAMEShape" -p "c_Rt_cheek_FRAME";
	setAttr -k off ".v" no;
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode transform -n "GRP_c_Rt_cheek_CTRL" -p "c_Rt_cheek_FRAME";
	addAttr -ci true -k true -sn "T1" -ln "T1" -at "double";
	addAttr -ci true -k true -sn "T2" -ln "T2" -at "double";
	addAttr -ci true -k true -sn "T3" -ln "T3" -at "double";
	addAttr -ci true -k true -sn "R1" -ln "R1" -at "double";
	addAttr -ci true -k true -sn "R2" -ln "R2" -at "double";
	addAttr -ci true -k true -sn "R3" -ln "R3" -at "double";
	addAttr -ci true -sn "S1" -ln "S1" -at "double";
	addAttr -ci true -sn "S2" -ln "S2" -at "double";
	addAttr -ci true -sn "S3" -ln "S3" -at "double";
	setAttr -k on ".S1" 1;
	setAttr -k on ".S2" 1;
	setAttr -k on ".S3" 1;
createNode transform -n "c_Rt_cheek_CTRL" -p "GRP_c_Rt_cheek_CTRL";
	addAttr -ci true -sn "frameSelectAble" -ln "frameSelectAble" -min 0 -max 2 -en 
		"normal:template:reference" -at "enum";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".mntl" -type "double3" -1 -1 0 ;
	setAttr ".mxtl" -type "double3" 1 1 0 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
	setAttr ".frameSelectAble" 2;
createNode nurbsCurve -n "c_Rt_cheek_CTRLShape" -p "c_Rt_cheek_CTRL";
	setAttr -k off ".v" no;
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		1 32 0 no 3
		33 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32
		33
		-0.050000000000000003 0.050000000000000003 0
		-0.050000000000000003 0.15000000000000002 0
		-0.10000000000000001 0.15000000000000002 0
		0 0.25 0
		0.10000000000000001 0.15000000000000002 0
		0.050000000000000003 0.15000000000000002 0
		0.050000000000000003 0.050000000000000003 0
		0.20000000000000001 0.20000000000000001 0
		0.050000000000000003 0.050000000000000003 0
		0.15000000000000002 0.050000000000000003 0
		0.15000000000000002 0.10000000000000001 0
		0.25 0 0
		0.15000000000000002 -0.10000000000000001 0
		0.15000000000000002 -0.050000000000000003 0
		0.050000000000000003 -0.050000000000000003 0
		0.20000000000000001 -0.20000000000000001 0
		0.050000000000000003 -0.050000000000000003 0
		0.050000000000000003 -0.15000000000000002 0
		0.10000000000000001 -0.15000000000000002 0
		0 -0.25 0
		-0.10000000000000001 -0.15000000000000002 0
		-0.050000000000000003 -0.15000000000000002 0
		-0.050000000000000003 -0.050000000000000003 0
		-0.20000000000000001 -0.20000000000000001 0
		-0.050000000000000003 -0.050000000000000003 0
		-0.15000000000000002 -0.050000000000000003 0
		-0.15000000000000002 -0.10000000000000001 0
		-0.25 0 0
		-0.15000000000000002 0.10000000000000001 0
		-0.15000000000000002 0.050000000000000003 0
		-0.050000000000000003 0.050000000000000003 0
		-0.20000000000000001 0.20000000000000001 0
		-0.050000000000000003 0.050000000000000003 0
		;
createNode transform -n "c_Rt_cheek_FRAME_lockzy" -p "c_Rt_cheek_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Rt_cheek_FRAME_lockzyShape" -p "c_Rt_cheek_FRAME_lockzy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 0.20000000000000001 0
		-1 -1 0
		1 -1 0
		1 0.20000000000000001 0
		-1 0.20000000000000001 0
		;
createNode transform -n "c_Rt_cheek_FRAME_lockfy" -p "c_Rt_cheek_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Rt_cheek_FRAME_lockfyShape" -p "c_Rt_cheek_FRAME_lockfy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -0.20000000000000001 0
		1 -0.20000000000000001 0
		1 1 0
		-1 1 0
		;
createNode transform -n "c_Rt_cheek_FRAME_lockzx" -p "c_Rt_cheek_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Rt_cheek_FRAME_lockzxShape" -p "c_Rt_cheek_FRAME_lockzx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		0.20000000000000001 -1 0
		0.20000000000000001 1 0
		-1 1 0
		;
createNode transform -n "c_Rt_cheek_FRAME_lockfx" -p "c_Rt_cheek_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Rt_cheek_FRAME_lockfxShape" -p "c_Rt_cheek_FRAME_lockfx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 1 0
		-0.20000000000000001 -1 0
		1 -1 0
		1 1 0
		-0.20000000000000001 1 0
		;
createNode transform -n "c_Rt_cheek_FRAME_lockzyfy" -p "c_Rt_cheek_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Rt_cheek_FRAME_lockzyfyShape" -p "c_Rt_cheek_FRAME_lockzyfy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 0.20000000000000001 0
		-1 -0.20000000000000001 0
		1 -0.20000000000000001 0
		1 0.20000000000000001 0
		-1 0.20000000000000001 0
		;
createNode transform -n "c_Rt_cheek_FRAME_lockzxfx" -p "c_Rt_cheek_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Rt_cheek_FRAME_lockzxfxShape" -p "c_Rt_cheek_FRAME_lockzxfx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 1 0
		-0.20000000000000001 -1 0
		0.20000000000000001 -1 0
		0.20000000000000001 1 0
		-0.20000000000000001 1 0
		;
createNode transform -n "c_Rt_cheek_FRAME_lockzyfyzx" -p "c_Rt_cheek_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Rt_cheek_FRAME_lockzyfyzxShape" -p "c_Rt_cheek_FRAME_lockzyfyzx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 0.20000000000000001 0
		-1 -0.20000000000000001 0
		0.20000000000000001 -0.20000000000000001 0
		0.20000000000000001 0.20000000000000001 0
		-1 0.20000000000000001 0
		;
createNode transform -n "c_Rt_cheek_FRAME_lockzyfyfx" -p "c_Rt_cheek_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Rt_cheek_FRAME_lockzyfyfxShape" -p "c_Rt_cheek_FRAME_lockzyfyfx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 0.20000000000000001 0
		-0.20000000000000001 -0.20000000000000001 0
		1 -0.20000000000000001 0
		1 0.20000000000000001 0
		-0.20000000000000001 0.20000000000000001 0
		;
createNode transform -n "c_Rt_cheek_FRAME_lockzxfxzy" -p "c_Rt_cheek_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Rt_cheek_FRAME_lockzxfxzyShape" -p "c_Rt_cheek_FRAME_lockzxfxzy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 0.20000000000000001 0
		-0.20000000000000001 -1 0
		0.20000000000000001 -1 0
		0.20000000000000001 0.20000000000000001 0
		-0.20000000000000001 0.20000000000000001 0
		;
createNode transform -n "c_Rt_cheek_FRAME_lockzxfxfy" -p "c_Rt_cheek_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Rt_cheek_FRAME_lockzxfxfyShape" -p "c_Rt_cheek_FRAME_lockzxfxfy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 1 0
		-0.20000000000000001 -0.20000000000000001 0
		0.20000000000000001 -0.20000000000000001 0
		0.20000000000000001 1 0
		-0.20000000000000001 1 0
		;
createNode transform -n "c_Rt_cheek_CTRL_up" -p "c_Rt_cheek_FRAME";
	setAttr ".t" -type "double3" 0 2.2 0 ;
createNode nurbsCurve -n "curveShape493" -p "c_Rt_cheek_CTRL_up";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_cheek_LOC_up" -p "c_Rt_cheek_CTRL_up";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_cheek_CTRL_dn" -p "c_Rt_cheek_FRAME";
	setAttr ".t" -type "double3" 0 -2.2 0 ;
createNode nurbsCurve -n "curveShape494" -p "c_Rt_cheek_CTRL_dn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_cheek_LOC_dn" -p "c_Rt_cheek_CTRL_dn";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_cheek_CTRL_lf" -p "c_Rt_cheek_FRAME";
	setAttr ".t" -type "double3" -2.2 0 0 ;
createNode nurbsCurve -n "curveShape495" -p "c_Rt_cheek_CTRL_lf";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_cheek_LOC_lf" -p "c_Rt_cheek_CTRL_lf";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_cheek_CTRL_lfup" -p "c_Rt_cheek_FRAME";
	setAttr ".t" -type "double3" -2.2 2.2 0 ;
createNode nurbsCurve -n "curveShape496" -p "c_Rt_cheek_CTRL_lfup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_cheek_LOC_lfup" -p "c_Rt_cheek_CTRL_lfup";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_cheek_CTRL_rt" -p "c_Rt_cheek_FRAME";
	setAttr ".t" -type "double3" 2.2 0 0 ;
createNode nurbsCurve -n "curveShape497" -p "c_Rt_cheek_CTRL_rt";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_cheek_LOC_rt" -p "c_Rt_cheek_CTRL_rt";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_cheek_CTRL_rtup" -p "c_Rt_cheek_FRAME";
	setAttr ".t" -type "double3" 2.2 2.2 0 ;
createNode nurbsCurve -n "curveShape498" -p "c_Rt_cheek_CTRL_rtup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_cheek_LOC_rtup" -p "c_Rt_cheek_CTRL_rtup";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_cheek_CTRL_lfdn" -p "c_Rt_cheek_FRAME";
	setAttr ".t" -type "double3" -2.2 -2.2 0 ;
createNode nurbsCurve -n "curveShape499" -p "c_Rt_cheek_CTRL_lfdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_cheek_LOC_lfdn" -p "c_Rt_cheek_CTRL_lfdn";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_cheek_CTRL_rtdn" -p "c_Rt_cheek_FRAME";
	setAttr ".t" -type "double3" 2.2 -2.2 0 ;
createNode nurbsCurve -n "curveShape500" -p "c_Rt_cheek_CTRL_rtdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_cheek_LOC_rtdn" -p "c_Rt_cheek_CTRL_rtdn";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_cheek_CTRL_fourAxisup" -p "c_Rt_cheek_FRAME";
	setAttr ".t" -type "double3" 0 4.4 0 ;
createNode nurbsCurve -n "curveShape501" -p "c_Rt_cheek_CTRL_fourAxisup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_cheek_LOC_fourAxis_up" -p "c_Rt_cheek_CTRL_fourAxisup";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_cheek_CTRL_fourAxisdn" -p "c_Rt_cheek_FRAME";
	setAttr ".t" -type "double3" 0 -4.4 0 ;
createNode nurbsCurve -n "curveShape502" -p "c_Rt_cheek_CTRL_fourAxisdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_cheek_LOC_fourAxis_dn" -p "c_Rt_cheek_CTRL_fourAxisdn";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_cheek_CTRL_fourAxislf" -p "c_Rt_cheek_FRAME";
	setAttr ".t" -type "double3" -4.4 0 0 ;
createNode nurbsCurve -n "curveShape503" -p "c_Rt_cheek_CTRL_fourAxislf";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_cheek_LOC_fourAxis_lf" -p "c_Rt_cheek_CTRL_fourAxislf";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_cheek_CTRL_fourAxisrt" -p "c_Rt_cheek_FRAME";
	setAttr ".t" -type "double3" 4.4 0 0 ;
createNode nurbsCurve -n "curveShape504" -p "c_Rt_cheek_CTRL_fourAxisrt";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_cheek_LOC_fourAxis_rt" -p "c_Rt_cheek_CTRL_fourAxisrt";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_eyelids_CTRL_GRP" -p "head_CTRL";
	addAttr -ci true -k true -sn "T1" -ln "T1" -at "double";
	addAttr -ci true -k true -sn "T2" -ln "T2" -at "double";
	addAttr -ci true -k true -sn "T3" -ln "T3" -at "double";
	addAttr -ci true -k true -sn "R1" -ln "R1" -at "double";
	addAttr -ci true -k true -sn "R2" -ln "R2" -at "double";
	addAttr -ci true -k true -sn "R3" -ln "R3" -at "double";
	addAttr -ci true -sn "S1" -ln "S1" -at "double";
	addAttr -ci true -sn "S2" -ln "S2" -at "double";
	addAttr -ci true -sn "S3" -ln "S3" -at "double";
	setAttr ".rp" -type "double3" 0.57197200339923482 0.43332811444394093 0.0089799342337342804 ;
	setAttr ".sp" -type "double3" 0.57197200339923482 0.43332811444394093 0.0089799342337342804 ;
	setAttr -k on ".S1" 1;
	setAttr -k on ".S2" 1;
	setAttr -k on ".S3" 1;
createNode transform -n "c_Lf_eyelids_CTRL" -p "c_Lf_eyelids_CTRL_GRP";
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr ".rp" -type "double3" 0.57197200339923482 0.43332811444394098 0.017959868467468398 ;
	setAttr ".sp" -type "double3" 0.57197200339923482 0.43332811444394098 0.017959868467468398 ;
createNode nurbsCurve -n "c_Lf_eyelids_CTRLShape" -p "c_Lf_eyelids_CTRL";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.90137056676753879 0.68586817917106391 0.017959868467468363
		0.57197200339923482 0.79047369902361775 0.017959868467468349
		0.24257344003093118 0.68586817917106413 0.017959868467468363
		0.10613208765756638 0.43332811444394109 0.017959868467468398
		0.24257344003093112 0.180788049716818 0.017959868467468436
		0.57197200339923471 0.076182529864264104 0.01795986846746845
		0.90137056676753824 0.18078804971681789 0.017959868467468436
		1.0378119191409032 0.43332811444394082 0.017959868467468398
		0.90137056676753879 0.68586817917106391 0.017959868467468363
		0.57197200339923482 0.79047369902361775 0.017959868467468349
		0.24257344003093118 0.68586817917106413 0.017959868467468363
		;
createNode transform -n "GRP_c_Lf_up_eyelids_FRAME" -p "c_Lf_eyelids_CTRL";
	setAttr ".t" -type "double3" 0.59485344757778891 0.57375519613646297 1.4569707410758149e-016 ;
	setAttr ".s" -type "double3" 0.15 0.15 0.15 ;
createNode transform -n "c_Lf_up_eyelids_FRAME" -p "GRP_c_Lf_up_eyelids_FRAME";
	addAttr -ci true -sn "up" -ln "up" -min 0 -at "double";
	addAttr -ci true -sn "dn" -ln "dn" -min 0 -at "double";
	addAttr -ci true -sn "lf" -ln "lf" -min 0 -at "double";
	addAttr -ci true -sn "rt" -ln "rt" -min 0 -at "double";
	addAttr -ci true -sn "lfup" -ln "lfup" -min 0 -at "double";
	addAttr -ci true -sn "rtup" -ln "rtup" -min 0 -at "double";
	addAttr -ci true -sn "lfdn" -ln "lfdn" -min 0 -at "double";
	addAttr -ci true -sn "rtdn" -ln "rtdn" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_up" -ln "fourAxis_up" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_dn" -ln "fourAxis_dn" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_lf" -ln "fourAxis_lf" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_rt" -ln "fourAxis_rt" -min 0 -at "double";
	addAttr -ci true -sn "up_Vis" -ln "up_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "dn_Vis" -ln "dn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lf_Vis" -ln "lf_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lfup_Vis" -ln "lfup_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rt_Vis" -ln "rt_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rtup_Vis" -ln "rtup_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lfdn_Vis" -ln "lfdn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rtdn_Vis" -ln "rtdn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_up_Vis" -ln "fourAxis_up_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_dn_Vis" -ln "fourAxis_dn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_lf_Vis" -ln "fourAxis_lf_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_rt_Vis" -ln "fourAxis_rt_Vis" -min 0 -max 1 -at "bool";
	setAttr -k on ".up";
	setAttr -k on ".dn";
	setAttr -k on ".lf";
	setAttr -k on ".rt";
	setAttr -k on ".lfup";
	setAttr -k on ".rtup";
	setAttr -k on ".lfdn";
	setAttr -k on ".rtdn";
	setAttr -k on ".fourAxis_up";
	setAttr -k on ".fourAxis_dn";
	setAttr -k on ".fourAxis_lf";
	setAttr -k on ".fourAxis_rt";
	setAttr -cb on ".up_Vis";
	setAttr -cb on ".dn_Vis";
	setAttr -cb on ".lf_Vis";
	setAttr -cb on ".lfup_Vis";
	setAttr -cb on ".rt_Vis";
	setAttr -cb on ".rtup_Vis";
	setAttr -cb on ".lfdn_Vis";
	setAttr -cb on ".rtdn_Vis";
	setAttr -cb on ".fourAxis_up_Vis";
	setAttr -cb on ".fourAxis_dn_Vis";
	setAttr -cb on ".fourAxis_lf_Vis";
	setAttr -cb on ".fourAxis_rt_Vis";
createNode nurbsCurve -n "c_Lf_up_eyelids_FRAMEShape" -p "c_Lf_up_eyelids_FRAME";
	setAttr -k off ".v" no;
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode transform -n "GRP_c_Lf_up_eyelids_CTRL" -p "c_Lf_up_eyelids_FRAME";
createNode transform -n "c_Lf_up_eyelids_CTRL" -p "GRP_c_Lf_up_eyelids_CTRL";
	addAttr -ci true -sn "frameSelectAble" -ln "frameSelectAble" -min 0 -max 2 -en 
		"normal:template:reference" -at "enum";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".mntl" -type "double3" -1 -1 0 ;
	setAttr ".mxtl" -type "double3" 1 1 0 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
	setAttr ".frameSelectAble" 2;
createNode nurbsCurve -n "c_Lf_up_eyelids_CTRLShape" -p "c_Lf_up_eyelids_CTRL";
	setAttr -k off ".v" no;
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		1 32 0 no 3
		33 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32
		33
		-0.050000000000000003 0.050000000000000003 0
		-0.050000000000000003 0.15000000000000002 0
		-0.10000000000000001 0.15000000000000002 0
		0 0.25 0
		0.10000000000000001 0.15000000000000002 0
		0.050000000000000003 0.15000000000000002 0
		0.050000000000000003 0.050000000000000003 0
		0.20000000000000001 0.20000000000000001 0
		0.050000000000000003 0.050000000000000003 0
		0.15000000000000002 0.050000000000000003 0
		0.15000000000000002 0.10000000000000001 0
		0.25 0 0
		0.15000000000000002 -0.10000000000000001 0
		0.15000000000000002 -0.050000000000000003 0
		0.050000000000000003 -0.050000000000000003 0
		0.20000000000000001 -0.20000000000000001 0
		0.050000000000000003 -0.050000000000000003 0
		0.050000000000000003 -0.15000000000000002 0
		0.10000000000000001 -0.15000000000000002 0
		0 -0.25 0
		-0.10000000000000001 -0.15000000000000002 0
		-0.050000000000000003 -0.15000000000000002 0
		-0.050000000000000003 -0.050000000000000003 0
		-0.20000000000000001 -0.20000000000000001 0
		-0.050000000000000003 -0.050000000000000003 0
		-0.15000000000000002 -0.050000000000000003 0
		-0.15000000000000002 -0.10000000000000001 0
		-0.25 0 0
		-0.15000000000000002 0.10000000000000001 0
		-0.15000000000000002 0.050000000000000003 0
		-0.050000000000000003 0.050000000000000003 0
		-0.20000000000000001 0.20000000000000001 0
		-0.050000000000000003 0.050000000000000003 0
		;
createNode nurbsCurve -n "c_up_eyelids_CTRLShape" -p "c_Lf_up_eyelids_CTRL";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-1.1805284788122838 0.28088342970082619 -2.8119034862619438e-017
		5.9987274373588188e-016 0.53769956303961686 -5.0334505056319287e-017
		1.1805284788122818 0.28088342970082508 -2.8119034862619438e-017
		1.7353936476310003 -0.48086452706465671 6.0742845912180087e-017
		1.3585413972457063 -0.49010148636113088 -2.8119034862619438e-017
		1.3107677899342808e-015 -0.46428063594092522 -5.0334505056319287e-017
		-1.3585413972457059 -0.49010148636113054 -2.8119034862619438e-017
		-1.7353936476310019 -0.48086452706465804 6.0742845912180087e-017
		-1.1805284788122838 0.28088342970082619 -2.8119034862619438e-017
		5.9987274373588188e-016 0.53769956303961686 -5.0334505056319287e-017
		1.1805284788122818 0.28088342970082508 -2.8119034862619438e-017
		;
createNode transform -n "c_Lf_up_eyelids_FRAME_lockzy" -p "c_Lf_up_eyelids_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Lf_up_eyelids_FRAME_lockzyShape" -p "c_Lf_up_eyelids_FRAME_lockzy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 0.20000000000000001 0
		-1 -1 0
		1 -1 0
		1 0.20000000000000001 0
		-1 0.20000000000000001 0
		;
createNode transform -n "c_Lf_up_eyelids_FRAME_lockfy" -p "c_Lf_up_eyelids_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Lf_up_eyelids_FRAME_lockfyShape" -p "c_Lf_up_eyelids_FRAME_lockfy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -0.20000000000000001 0
		1 -0.20000000000000001 0
		1 1 0
		-1 1 0
		;
createNode transform -n "c_Lf_up_eyelids_FRAME_lockzx" -p "c_Lf_up_eyelids_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Lf_up_eyelids_FRAME_lockzxShape" -p "c_Lf_up_eyelids_FRAME_lockzx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		0.20000000000000001 -1 0
		0.20000000000000001 1 0
		-1 1 0
		;
createNode transform -n "c_Lf_up_eyelids_FRAME_lockfx" -p "c_Lf_up_eyelids_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Lf_up_eyelids_FRAME_lockfxShape" -p "c_Lf_up_eyelids_FRAME_lockfx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 1 0
		-0.20000000000000001 -1 0
		1 -1 0
		1 1 0
		-0.20000000000000001 1 0
		;
createNode transform -n "c_Lf_up_eyelids_FRAME_lockzyfy" -p "c_Lf_up_eyelids_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Lf_up_eyelids_FRAME_lockzyfyShape" -p "c_Lf_up_eyelids_FRAME_lockzyfy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 0.20000000000000001 0
		-1 -0.20000000000000001 0
		1 -0.20000000000000001 0
		1 0.20000000000000001 0
		-1 0.20000000000000001 0
		;
createNode transform -n "c_Lf_up_eyelids_FRAME_lockzxfx" -p "c_Lf_up_eyelids_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Lf_up_eyelids_FRAME_lockzxfxShape" -p "c_Lf_up_eyelids_FRAME_lockzxfx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 1 0
		-0.20000000000000001 -1 0
		0.20000000000000001 -1 0
		0.20000000000000001 1 0
		-0.20000000000000001 1 0
		;
createNode transform -n "c_Lf_up_eyelids_FRAME_lockzyfyzx" -p "c_Lf_up_eyelids_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Lf_up_eyelids_FRAME_lockzyfyzxShape" -p "c_Lf_up_eyelids_FRAME_lockzyfyzx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 0.20000000000000001 0
		-1 -0.20000000000000001 0
		0.20000000000000001 -0.20000000000000001 0
		0.20000000000000001 0.20000000000000001 0
		-1 0.20000000000000001 0
		;
createNode transform -n "c_Lf_up_eyelids_FRAME_lockzyfyfx" -p "c_Lf_up_eyelids_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Lf_up_eyelids_FRAME_lockzyfyfxShape" -p "c_Lf_up_eyelids_FRAME_lockzyfyfx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 0.20000000000000001 0
		-0.20000000000000001 -0.20000000000000001 0
		1 -0.20000000000000001 0
		1 0.20000000000000001 0
		-0.20000000000000001 0.20000000000000001 0
		;
createNode transform -n "c_Lf_up_eyelids_FRAME_lockzxfxzy" -p "c_Lf_up_eyelids_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Lf_up_eyelids_FRAME_lockzxfxzyShape" -p "c_Lf_up_eyelids_FRAME_lockzxfxzy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 0.20000000000000001 0
		-0.20000000000000001 -1 0
		0.20000000000000001 -1 0
		0.20000000000000001 0.20000000000000001 0
		-0.20000000000000001 0.20000000000000001 0
		;
createNode transform -n "c_Lf_up_eyelids_FRAME_lockzxfxfy" -p "c_Lf_up_eyelids_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Lf_up_eyelids_FRAME_lockzxfxfyShape" -p "c_Lf_up_eyelids_FRAME_lockzxfxfy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 1 0
		-0.20000000000000001 -0.20000000000000001 0
		0.20000000000000001 -0.20000000000000001 0
		0.20000000000000001 1 0
		-0.20000000000000001 1 0
		;
createNode transform -n "c_Lf_up_eyelids_CTRL_up" -p "c_Lf_up_eyelids_FRAME";
	setAttr ".t" -type "double3" 0 2.2 0 ;
createNode nurbsCurve -n "curveShape73" -p "c_Lf_up_eyelids_CTRL_up";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_up_eyelids_LOC_up" -p "c_Lf_up_eyelids_CTRL_up";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_up_eyelids_CTRL_dn" -p "c_Lf_up_eyelids_FRAME";
	setAttr ".t" -type "double3" 0 -2.2 0 ;
createNode nurbsCurve -n "curveShape74" -p "c_Lf_up_eyelids_CTRL_dn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_up_eyelids_LOC_dn" -p "c_Lf_up_eyelids_CTRL_dn";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_up_eyelids_CTRL_lf" -p "c_Lf_up_eyelids_FRAME";
	setAttr ".t" -type "double3" -2.2 0 0 ;
createNode nurbsCurve -n "curveShape75" -p "c_Lf_up_eyelids_CTRL_lf";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_up_eyelids_LOC_lf" -p "c_Lf_up_eyelids_CTRL_lf";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_up_eyelids_CTRL_lfup" -p "c_Lf_up_eyelids_FRAME";
	setAttr ".t" -type "double3" -2.2 2.2 0 ;
createNode nurbsCurve -n "curveShape76" -p "c_Lf_up_eyelids_CTRL_lfup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_up_eyelids_LOC_lfup" -p "c_Lf_up_eyelids_CTRL_lfup";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_up_eyelids_CTRL_rt" -p "c_Lf_up_eyelids_FRAME";
	setAttr ".t" -type "double3" 2.2 0 0 ;
createNode nurbsCurve -n "curveShape77" -p "c_Lf_up_eyelids_CTRL_rt";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_up_eyelids_LOC_rt" -p "c_Lf_up_eyelids_CTRL_rt";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_up_eyelids_CTRL_rtup" -p "c_Lf_up_eyelids_FRAME";
	setAttr ".t" -type "double3" 2.2 2.2 0 ;
createNode nurbsCurve -n "curveShape78" -p "c_Lf_up_eyelids_CTRL_rtup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_up_eyelids_LOC_rtup" -p "c_Lf_up_eyelids_CTRL_rtup";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_up_eyelids_CTRL_lfdn" -p "c_Lf_up_eyelids_FRAME";
	setAttr ".t" -type "double3" -2.2 -2.2 0 ;
createNode nurbsCurve -n "curveShape79" -p "c_Lf_up_eyelids_CTRL_lfdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_up_eyelids_LOC_lfdn" -p "c_Lf_up_eyelids_CTRL_lfdn";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_up_eyelids_CTRL_rtdn" -p "c_Lf_up_eyelids_FRAME";
	setAttr ".t" -type "double3" 2.2 -2.2 0 ;
createNode nurbsCurve -n "curveShape80" -p "c_Lf_up_eyelids_CTRL_rtdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_up_eyelids_LOC_rtdn" -p "c_Lf_up_eyelids_CTRL_rtdn";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_up_eyelids_CTRL_fourAxisup" -p "c_Lf_up_eyelids_FRAME";
	setAttr ".t" -type "double3" 0 4.4 0 ;
createNode nurbsCurve -n "curveShape81" -p "c_Lf_up_eyelids_CTRL_fourAxisup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_up_eyelids_LOC_fourAxis_up" -p "c_Lf_up_eyelids_CTRL_fourAxisup";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_up_eyelids_CTRL_fourAxisdn" -p "c_Lf_up_eyelids_FRAME";
	setAttr ".t" -type "double3" 0 -4.4 0 ;
createNode nurbsCurve -n "curveShape82" -p "c_Lf_up_eyelids_CTRL_fourAxisdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_up_eyelids_LOC_fourAxis_dn" -p "c_Lf_up_eyelids_CTRL_fourAxisdn";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_up_eyelids_CTRL_fourAxislf" -p "c_Lf_up_eyelids_FRAME";
	setAttr ".t" -type "double3" -4.4 0 0 ;
createNode nurbsCurve -n "curveShape83" -p "c_Lf_up_eyelids_CTRL_fourAxislf";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_up_eyelids_LOC_fourAxis_lf" -p "c_Lf_up_eyelids_CTRL_fourAxislf";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_up_eyelids_CTRL_fourAxisrt" -p "c_Lf_up_eyelids_FRAME";
	setAttr ".t" -type "double3" 4.4 0 0 ;
createNode nurbsCurve -n "curveShape84" -p "c_Lf_up_eyelids_CTRL_fourAxisrt";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_up_eyelids_LOC_fourAxis_rt" -p "c_Lf_up_eyelids_CTRL_fourAxisrt";
	setAttr -k off ".v" no;
createNode transform -n "GRP_c_Lf_dn_eyelids_FRAME" -p "c_Lf_eyelids_CTRL";
	setAttr ".t" -type "double3" 0.59568934560581388 0.27868064396936604 1.4590181007646836e-016 ;
	setAttr ".s" -type "double3" 0.15 0.15 0.15 ;
createNode transform -n "c_Lf_dn_eyelids_FRAME" -p "GRP_c_Lf_dn_eyelids_FRAME";
	addAttr -ci true -sn "up" -ln "up" -min 0 -at "double";
	addAttr -ci true -sn "dn" -ln "dn" -min 0 -at "double";
	addAttr -ci true -sn "lf" -ln "lf" -min 0 -at "double";
	addAttr -ci true -sn "rt" -ln "rt" -min 0 -at "double";
	addAttr -ci true -sn "lfup" -ln "lfup" -min 0 -at "double";
	addAttr -ci true -sn "rtup" -ln "rtup" -min 0 -at "double";
	addAttr -ci true -sn "lfdn" -ln "lfdn" -min 0 -at "double";
	addAttr -ci true -sn "rtdn" -ln "rtdn" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_up" -ln "fourAxis_up" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_dn" -ln "fourAxis_dn" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_lf" -ln "fourAxis_lf" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_rt" -ln "fourAxis_rt" -min 0 -at "double";
	addAttr -ci true -sn "up_Vis" -ln "up_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "dn_Vis" -ln "dn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lf_Vis" -ln "lf_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lfup_Vis" -ln "lfup_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rt_Vis" -ln "rt_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rtup_Vis" -ln "rtup_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lfdn_Vis" -ln "lfdn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rtdn_Vis" -ln "rtdn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_up_Vis" -ln "fourAxis_up_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_dn_Vis" -ln "fourAxis_dn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_lf_Vis" -ln "fourAxis_lf_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_rt_Vis" -ln "fourAxis_rt_Vis" -min 0 -max 1 -at "bool";
	setAttr -k on ".up";
	setAttr -k on ".dn";
	setAttr -k on ".lf";
	setAttr -k on ".rt";
	setAttr -k on ".lfup";
	setAttr -k on ".rtup";
	setAttr -k on ".lfdn";
	setAttr -k on ".rtdn";
	setAttr -k on ".fourAxis_up";
	setAttr -k on ".fourAxis_dn";
	setAttr -k on ".fourAxis_lf";
	setAttr -k on ".fourAxis_rt";
	setAttr -cb on ".up_Vis";
	setAttr -cb on ".dn_Vis";
	setAttr -cb on ".lf_Vis";
	setAttr -cb on ".lfup_Vis";
	setAttr -cb on ".rt_Vis";
	setAttr -cb on ".rtup_Vis";
	setAttr -cb on ".lfdn_Vis";
	setAttr -cb on ".rtdn_Vis";
	setAttr -cb on ".fourAxis_up_Vis";
	setAttr -cb on ".fourAxis_dn_Vis";
	setAttr -cb on ".fourAxis_lf_Vis";
	setAttr -cb on ".fourAxis_rt_Vis";
createNode nurbsCurve -n "c_Lf_dn_eyelids_FRAMEShape" -p "c_Lf_dn_eyelids_FRAME";
	setAttr -k off ".v" no;
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode transform -n "GRP_c_Lf_dn_eyelids_CTRL" -p "c_Lf_dn_eyelids_FRAME";
createNode transform -n "c_Lf_dn_eyelids_CTRL" -p "GRP_c_Lf_dn_eyelids_CTRL";
	addAttr -ci true -sn "frameSelectAble" -ln "frameSelectAble" -min 0 -max 2 -en 
		"normal:template:reference" -at "enum";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".mntl" -type "double3" -1 -1 0 ;
	setAttr ".mxtl" -type "double3" 1 1 0 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
	setAttr ".frameSelectAble" 2;
createNode nurbsCurve -n "c_Lf_dn_eyelids_CTRLShape" -p "c_Lf_dn_eyelids_CTRL";
	setAttr -k off ".v" no;
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		1 32 0 no 3
		33 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32
		33
		-0.050000000000000003 0.050000000000000003 0
		-0.050000000000000003 0.15000000000000002 0
		-0.10000000000000001 0.15000000000000002 0
		0 0.25 0
		0.10000000000000001 0.15000000000000002 0
		0.050000000000000003 0.15000000000000002 0
		0.050000000000000003 0.050000000000000003 0
		0.20000000000000001 0.20000000000000001 0
		0.050000000000000003 0.050000000000000003 0
		0.15000000000000002 0.050000000000000003 0
		0.15000000000000002 0.10000000000000001 0
		0.25 0 0
		0.15000000000000002 -0.10000000000000001 0
		0.15000000000000002 -0.050000000000000003 0
		0.050000000000000003 -0.050000000000000003 0
		0.20000000000000001 -0.20000000000000001 0
		0.050000000000000003 -0.050000000000000003 0
		0.050000000000000003 -0.15000000000000002 0
		0.10000000000000001 -0.15000000000000002 0
		0 -0.25 0
		-0.10000000000000001 -0.15000000000000002 0
		-0.050000000000000003 -0.15000000000000002 0
		-0.050000000000000003 -0.050000000000000003 0
		-0.20000000000000001 -0.20000000000000001 0
		-0.050000000000000003 -0.050000000000000003 0
		-0.15000000000000002 -0.050000000000000003 0
		-0.15000000000000002 -0.10000000000000001 0
		-0.25 0 0
		-0.15000000000000002 0.10000000000000001 0
		-0.15000000000000002 0.050000000000000003 0
		-0.050000000000000003 0.050000000000000003 0
		-0.20000000000000001 0.20000000000000001 0
		-0.050000000000000003 0.050000000000000003 0
		;
createNode nurbsCurve -n "c_dn_eyelids_CTRLShape" -p "c_Lf_dn_eyelids_CTRL";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-1.2390997585947046 -0.28532736599049813 1.4368477171183337e-016
		1.9157969561577778e-016 -0.57035700346218554 2.3947461951972243e-016
		1.2390997585947028 -0.28532736599049857 1.4368477171183337e-016
		1.8214942616291434 0.56010528319295472 -1.1973730975986122e-016
		1.4259446913654181 0.57035700346218543 -2.155271575677502e-016
		9.5789847807888972e-016 0.54169950621385821 -2.3947461951972243e-016
		-1.4259446913654161 0.57035700346218554 -2.155271575677502e-016
		-1.8214942616291434 0.56010528319295583 -1.1973730975986122e-016
		-1.2390997585947046 -0.28532736599049813 1.4368477171183337e-016
		1.9157969561577778e-016 -0.57035700346218554 2.3947461951972243e-016
		1.2390997585947028 -0.28532736599049857 1.4368477171183337e-016
		;
createNode transform -n "c_Lf_dn_eyelids_FRAME_lockzy" -p "c_Lf_dn_eyelids_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Lf_dn_eyelids_FRAME_lockzyShape" -p "c_Lf_dn_eyelids_FRAME_lockzy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 0.20000000000000001 0
		-1 -1 0
		1 -1 0
		1 0.20000000000000001 0
		-1 0.20000000000000001 0
		;
createNode transform -n "c_Lf_dn_eyelids_FRAME_lockfy" -p "c_Lf_dn_eyelids_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Lf_dn_eyelids_FRAME_lockfyShape" -p "c_Lf_dn_eyelids_FRAME_lockfy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -0.20000000000000001 0
		1 -0.20000000000000001 0
		1 1 0
		-1 1 0
		;
createNode transform -n "c_Lf_dn_eyelids_FRAME_lockzx" -p "c_Lf_dn_eyelids_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Lf_dn_eyelids_FRAME_lockzxShape" -p "c_Lf_dn_eyelids_FRAME_lockzx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		0.20000000000000001 -1 0
		0.20000000000000001 1 0
		-1 1 0
		;
createNode transform -n "c_Lf_dn_eyelids_FRAME_lockfx" -p "c_Lf_dn_eyelids_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Lf_dn_eyelids_FRAME_lockfxShape" -p "c_Lf_dn_eyelids_FRAME_lockfx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 1 0
		-0.20000000000000001 -1 0
		1 -1 0
		1 1 0
		-0.20000000000000001 1 0
		;
createNode transform -n "c_Lf_dn_eyelids_FRAME_lockzyfy" -p "c_Lf_dn_eyelids_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Lf_dn_eyelids_FRAME_lockzyfyShape" -p "c_Lf_dn_eyelids_FRAME_lockzyfy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 0.20000000000000001 0
		-1 -0.20000000000000001 0
		1 -0.20000000000000001 0
		1 0.20000000000000001 0
		-1 0.20000000000000001 0
		;
createNode transform -n "c_Lf_dn_eyelids_FRAME_lockzxfx" -p "c_Lf_dn_eyelids_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Lf_dn_eyelids_FRAME_lockzxfxShape" -p "c_Lf_dn_eyelids_FRAME_lockzxfx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 1 0
		-0.20000000000000001 -1 0
		0.20000000000000001 -1 0
		0.20000000000000001 1 0
		-0.20000000000000001 1 0
		;
createNode transform -n "c_Lf_dn_eyelids_FRAME_lockzyfyzx" -p "c_Lf_dn_eyelids_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Lf_dn_eyelids_FRAME_lockzyfyzxShape" -p "c_Lf_dn_eyelids_FRAME_lockzyfyzx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 0.20000000000000001 0
		-1 -0.20000000000000001 0
		0.20000000000000001 -0.20000000000000001 0
		0.20000000000000001 0.20000000000000001 0
		-1 0.20000000000000001 0
		;
createNode transform -n "c_Lf_dn_eyelids_FRAME_lockzyfyfx" -p "c_Lf_dn_eyelids_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Lf_dn_eyelids_FRAME_lockzyfyfxShape" -p "c_Lf_dn_eyelids_FRAME_lockzyfyfx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 0.20000000000000001 0
		-0.20000000000000001 -0.20000000000000001 0
		1 -0.20000000000000001 0
		1 0.20000000000000001 0
		-0.20000000000000001 0.20000000000000001 0
		;
createNode transform -n "c_Lf_dn_eyelids_FRAME_lockzxfxzy" -p "c_Lf_dn_eyelids_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Lf_dn_eyelids_FRAME_lockzxfxzyShape" -p "c_Lf_dn_eyelids_FRAME_lockzxfxzy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 0.20000000000000001 0
		-0.20000000000000001 -1 0
		0.20000000000000001 -1 0
		0.20000000000000001 0.20000000000000001 0
		-0.20000000000000001 0.20000000000000001 0
		;
createNode transform -n "c_Lf_dn_eyelids_FRAME_lockzxfxfy" -p "c_Lf_dn_eyelids_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Lf_dn_eyelids_FRAME_lockzxfxfyShape" -p "c_Lf_dn_eyelids_FRAME_lockzxfxfy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 1 0
		-0.20000000000000001 -0.20000000000000001 0
		0.20000000000000001 -0.20000000000000001 0
		0.20000000000000001 1 0
		-0.20000000000000001 1 0
		;
createNode transform -n "c_Lf_dn_eyelids_CTRL_up" -p "c_Lf_dn_eyelids_FRAME";
	setAttr ".t" -type "double3" 0 2.2 0 ;
createNode nurbsCurve -n "curveShape97" -p "c_Lf_dn_eyelids_CTRL_up";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_dn_eyelids_LOC_up" -p "c_Lf_dn_eyelids_CTRL_up";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_dn_eyelids_CTRL_dn" -p "c_Lf_dn_eyelids_FRAME";
	setAttr ".t" -type "double3" 0 -2.2 0 ;
createNode nurbsCurve -n "curveShape98" -p "c_Lf_dn_eyelids_CTRL_dn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_dn_eyelids_LOC_dn" -p "c_Lf_dn_eyelids_CTRL_dn";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_dn_eyelids_CTRL_lf" -p "c_Lf_dn_eyelids_FRAME";
	setAttr ".t" -type "double3" -2.2 0 0 ;
createNode nurbsCurve -n "curveShape99" -p "c_Lf_dn_eyelids_CTRL_lf";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_dn_eyelids_LOC_lf" -p "c_Lf_dn_eyelids_CTRL_lf";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_dn_eyelids_CTRL_lfup" -p "c_Lf_dn_eyelids_FRAME";
	setAttr ".t" -type "double3" -2.2 2.2 0 ;
createNode nurbsCurve -n "curveShape100" -p "c_Lf_dn_eyelids_CTRL_lfup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_dn_eyelids_LOC_lfup" -p "c_Lf_dn_eyelids_CTRL_lfup";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_dn_eyelids_CTRL_rt" -p "c_Lf_dn_eyelids_FRAME";
	setAttr ".t" -type "double3" 2.2 0 0 ;
createNode nurbsCurve -n "curveShape101" -p "c_Lf_dn_eyelids_CTRL_rt";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_dn_eyelids_LOC_rt" -p "c_Lf_dn_eyelids_CTRL_rt";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_dn_eyelids_CTRL_rtup" -p "c_Lf_dn_eyelids_FRAME";
	setAttr ".t" -type "double3" 2.2 2.2 0 ;
createNode nurbsCurve -n "curveShape102" -p "c_Lf_dn_eyelids_CTRL_rtup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_dn_eyelids_LOC_rtup" -p "c_Lf_dn_eyelids_CTRL_rtup";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_dn_eyelids_CTRL_lfdn" -p "c_Lf_dn_eyelids_FRAME";
	setAttr ".t" -type "double3" -2.2 -2.2 0 ;
createNode nurbsCurve -n "curveShape103" -p "c_Lf_dn_eyelids_CTRL_lfdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_dn_eyelids_LOC_lfdn" -p "c_Lf_dn_eyelids_CTRL_lfdn";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_dn_eyelids_CTRL_rtdn" -p "c_Lf_dn_eyelids_FRAME";
	setAttr ".t" -type "double3" 2.2 -2.2 0 ;
createNode nurbsCurve -n "curveShape104" -p "c_Lf_dn_eyelids_CTRL_rtdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_dn_eyelids_LOC_rtdn" -p "c_Lf_dn_eyelids_CTRL_rtdn";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_dn_eyelids_CTRL_fourAxisup" -p "c_Lf_dn_eyelids_FRAME";
	setAttr ".t" -type "double3" 0 4.4 0 ;
createNode nurbsCurve -n "curveShape105" -p "c_Lf_dn_eyelids_CTRL_fourAxisup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_dn_eyelids_LOC_fourAxis_up" -p "c_Lf_dn_eyelids_CTRL_fourAxisup";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_dn_eyelids_CTRL_fourAxisdn" -p "c_Lf_dn_eyelids_FRAME";
	setAttr ".t" -type "double3" 0 -4.4 0 ;
createNode nurbsCurve -n "curveShape106" -p "c_Lf_dn_eyelids_CTRL_fourAxisdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_dn_eyelids_LOC_fourAxis_dn" -p "c_Lf_dn_eyelids_CTRL_fourAxisdn";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_dn_eyelids_CTRL_fourAxislf" -p "c_Lf_dn_eyelids_FRAME";
	setAttr ".t" -type "double3" -4.4 0 0 ;
createNode nurbsCurve -n "curveShape107" -p "c_Lf_dn_eyelids_CTRL_fourAxislf";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_dn_eyelids_LOC_fourAxis_lf" -p "c_Lf_dn_eyelids_CTRL_fourAxislf";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_dn_eyelids_CTRL_fourAxisrt" -p "c_Lf_dn_eyelids_FRAME";
	setAttr ".t" -type "double3" 4.4 0 0 ;
createNode nurbsCurve -n "curveShape108" -p "c_Lf_dn_eyelids_CTRL_fourAxisrt";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_dn_eyelids_LOC_fourAxis_rt" -p "c_Lf_dn_eyelids_CTRL_fourAxisrt";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_eyelids_CTRL_GRP" -p "head_CTRL";
	addAttr -ci true -k true -sn "T1" -ln "T1" -at "double";
	addAttr -ci true -k true -sn "T2" -ln "T2" -at "double";
	addAttr -ci true -k true -sn "T3" -ln "T3" -at "double";
	addAttr -ci true -k true -sn "R1" -ln "R1" -at "double";
	addAttr -ci true -k true -sn "R2" -ln "R2" -at "double";
	addAttr -ci true -k true -sn "R3" -ln "R3" -at "double";
	addAttr -ci true -sn "S1" -ln "S1" -at "double";
	addAttr -ci true -sn "S2" -ln "S2" -at "double";
	addAttr -ci true -sn "S3" -ln "S3" -at "double";
	setAttr ".rp" -type "double3" -0.57197200339923482 0.43332811444394109 0.0089799342337341537 ;
	setAttr ".sp" -type "double3" -0.57197200339923482 0.43332811444394109 0.0089799342337341537 ;
	setAttr -k on ".S1" 1;
	setAttr -k on ".S2" 1;
	setAttr -k on ".S3" 1;
createNode transform -n "c_Rt_eyelids_CTRL" -p "c_Rt_eyelids_CTRL_GRP";
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr ".rp" -type "double3" -0.57197200339923482 0.43332811444394104 0.017959868467468398 ;
	setAttr ".sp" -type "double3" -0.57197200339923482 0.43332811444394104 0.017959868467468398 ;
createNode nurbsCurve -n "c_Rt_eyelids_CTRLShape" -p "c_Rt_eyelids_CTRL";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-0.90137056676753857 0.68586817917106402 0.017959868467468363
		-0.57197200339923471 0.79047369902361797 0.017959868467468349
		-0.24257344003093112 0.68586817917106413 0.017959868467468363
		-0.10613208765756632 0.43332811444394115 0.017959868467468398
		-0.24257344003093109 0.18078804971681808 0.017959868467468436
		-0.57197200339923471 0.076182529864264215 0.01795986846746845
		-0.90137056676753824 0.18078804971681806 0.017959868467468436
		-1.0378119191409032 0.43332811444394098 0.017959868467468398
		-0.90137056676753857 0.68586817917106402 0.017959868467468363
		-0.57197200339923471 0.79047369902361797 0.017959868467468349
		-0.24257344003093112 0.68586817917106413 0.017959868467468363
		;
createNode transform -n "GRP_c_Rt_up_eyelids_FRAME" -p "c_Rt_eyelids_CTRL";
	setAttr ".t" -type "double3" -0.59485344757778891 0.57375519613646297 -7.2848537053790746e-017 ;
	setAttr ".r" -type "double3" 0 -180 0 ;
	setAttr ".s" -type "double3" 0.15 0.15 0.15 ;
createNode transform -n "c_Rt_up_eyelids_FRAME" -p "GRP_c_Rt_up_eyelids_FRAME";
	addAttr -ci true -sn "up" -ln "up" -min 0 -at "double";
	addAttr -ci true -sn "dn" -ln "dn" -min 0 -at "double";
	addAttr -ci true -sn "lf" -ln "lf" -min 0 -at "double";
	addAttr -ci true -sn "rt" -ln "rt" -min 0 -at "double";
	addAttr -ci true -sn "lfup" -ln "lfup" -min 0 -at "double";
	addAttr -ci true -sn "rtup" -ln "rtup" -min 0 -at "double";
	addAttr -ci true -sn "lfdn" -ln "lfdn" -min 0 -at "double";
	addAttr -ci true -sn "rtdn" -ln "rtdn" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_up" -ln "fourAxis_up" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_dn" -ln "fourAxis_dn" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_lf" -ln "fourAxis_lf" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_rt" -ln "fourAxis_rt" -min 0 -at "double";
	addAttr -ci true -sn "up_Vis" -ln "up_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "dn_Vis" -ln "dn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lf_Vis" -ln "lf_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lfup_Vis" -ln "lfup_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rt_Vis" -ln "rt_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rtup_Vis" -ln "rtup_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lfdn_Vis" -ln "lfdn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rtdn_Vis" -ln "rtdn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_up_Vis" -ln "fourAxis_up_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_dn_Vis" -ln "fourAxis_dn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_lf_Vis" -ln "fourAxis_lf_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_rt_Vis" -ln "fourAxis_rt_Vis" -min 0 -max 1 -at "bool";
	setAttr -k on ".up";
	setAttr -k on ".dn";
	setAttr -k on ".lf";
	setAttr -k on ".rt";
	setAttr -k on ".lfup";
	setAttr -k on ".rtup";
	setAttr -k on ".lfdn";
	setAttr -k on ".rtdn";
	setAttr -k on ".fourAxis_up";
	setAttr -k on ".fourAxis_dn";
	setAttr -k on ".fourAxis_lf";
	setAttr -k on ".fourAxis_rt";
	setAttr -cb on ".up_Vis";
	setAttr -cb on ".dn_Vis";
	setAttr -cb on ".lf_Vis";
	setAttr -cb on ".lfup_Vis";
	setAttr -cb on ".rt_Vis";
	setAttr -cb on ".rtup_Vis";
	setAttr -cb on ".lfdn_Vis";
	setAttr -cb on ".rtdn_Vis";
	setAttr -cb on ".fourAxis_up_Vis";
	setAttr -cb on ".fourAxis_dn_Vis";
	setAttr -cb on ".fourAxis_lf_Vis";
	setAttr -cb on ".fourAxis_rt_Vis";
createNode nurbsCurve -n "c_Rt_up_eyelids_FRAMEShape" -p "c_Rt_up_eyelids_FRAME";
	setAttr -k off ".v" no;
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode transform -n "GRP_c_Rt_up_eyelids_CTRL" -p "c_Rt_up_eyelids_FRAME";
createNode transform -n "c_Rt_up_eyelids_CTRL" -p "GRP_c_Rt_up_eyelids_CTRL";
	addAttr -ci true -sn "frameSelectAble" -ln "frameSelectAble" -min 0 -max 2 -en 
		"normal:template:reference" -at "enum";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".mntl" -type "double3" -1 -1 0 ;
	setAttr ".mxtl" -type "double3" 1 1 0 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
	setAttr ".frameSelectAble" 2;
createNode nurbsCurve -n "c_Rt_up_eyelids_CTRLShape" -p "c_Rt_up_eyelids_CTRL";
	setAttr -k off ".v" no;
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		1 32 0 no 3
		33 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32
		33
		-0.050000000000000003 0.050000000000000003 0
		-0.050000000000000003 0.15000000000000002 0
		-0.10000000000000001 0.15000000000000002 0
		0 0.25 0
		0.10000000000000001 0.15000000000000002 0
		0.050000000000000003 0.15000000000000002 0
		0.050000000000000003 0.050000000000000003 0
		0.20000000000000001 0.20000000000000001 0
		0.050000000000000003 0.050000000000000003 0
		0.15000000000000002 0.050000000000000003 0
		0.15000000000000002 0.10000000000000001 0
		0.25 0 0
		0.15000000000000002 -0.10000000000000001 0
		0.15000000000000002 -0.050000000000000003 0
		0.050000000000000003 -0.050000000000000003 0
		0.20000000000000001 -0.20000000000000001 0
		0.050000000000000003 -0.050000000000000003 0
		0.050000000000000003 -0.15000000000000002 0
		0.10000000000000001 -0.15000000000000002 0
		0 -0.25 0
		-0.10000000000000001 -0.15000000000000002 0
		-0.050000000000000003 -0.15000000000000002 0
		-0.050000000000000003 -0.050000000000000003 0
		-0.20000000000000001 -0.20000000000000001 0
		-0.050000000000000003 -0.050000000000000003 0
		-0.15000000000000002 -0.050000000000000003 0
		-0.15000000000000002 -0.10000000000000001 0
		-0.25 0 0
		-0.15000000000000002 0.10000000000000001 0
		-0.15000000000000002 0.050000000000000003 0
		-0.050000000000000003 0.050000000000000003 0
		-0.20000000000000001 0.20000000000000001 0
		-0.050000000000000003 0.050000000000000003 0
		;
createNode transform -n "c_Rt_up_eyelids_FRAME_lockzy" -p "c_Rt_up_eyelids_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Rt_up_eyelids_FRAME_lockzyShape" -p "c_Rt_up_eyelids_FRAME_lockzy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 0.20000000000000001 0
		-1 -1 0
		1 -1 0
		1 0.20000000000000001 0
		-1 0.20000000000000001 0
		;
createNode transform -n "c_Rt_up_eyelids_FRAME_lockfy" -p "c_Rt_up_eyelids_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Rt_up_eyelids_FRAME_lockfyShape" -p "c_Rt_up_eyelids_FRAME_lockfy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -0.20000000000000001 0
		1 -0.20000000000000001 0
		1 1 0
		-1 1 0
		;
createNode transform -n "c_Rt_up_eyelids_FRAME_lockzx" -p "c_Rt_up_eyelids_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Rt_up_eyelids_FRAME_lockzxShape" -p "c_Rt_up_eyelids_FRAME_lockzx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		0.20000000000000001 -1 0
		0.20000000000000001 1 0
		-1 1 0
		;
createNode transform -n "c_Rt_up_eyelids_FRAME_lockfx" -p "c_Rt_up_eyelids_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Rt_up_eyelids_FRAME_lockfxShape" -p "c_Rt_up_eyelids_FRAME_lockfx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 1 0
		-0.20000000000000001 -1 0
		1 -1 0
		1 1 0
		-0.20000000000000001 1 0
		;
createNode transform -n "c_Rt_up_eyelids_FRAME_lockzyfy" -p "c_Rt_up_eyelids_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Rt_up_eyelids_FRAME_lockzyfyShape" -p "c_Rt_up_eyelids_FRAME_lockzyfy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 0.20000000000000001 0
		-1 -0.20000000000000001 0
		1 -0.20000000000000001 0
		1 0.20000000000000001 0
		-1 0.20000000000000001 0
		;
createNode transform -n "c_Rt_up_eyelids_FRAME_lockzxfx" -p "c_Rt_up_eyelids_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Rt_up_eyelids_FRAME_lockzxfxShape" -p "c_Rt_up_eyelids_FRAME_lockzxfx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 1 0
		-0.20000000000000001 -1 0
		0.20000000000000001 -1 0
		0.20000000000000001 1 0
		-0.20000000000000001 1 0
		;
createNode transform -n "c_Rt_up_eyelids_FRAME_lockzyfyzx" -p "c_Rt_up_eyelids_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Rt_up_eyelids_FRAME_lockzyfyzxShape" -p "c_Rt_up_eyelids_FRAME_lockzyfyzx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 0.20000000000000001 0
		-1 -0.20000000000000001 0
		0.20000000000000001 -0.20000000000000001 0
		0.20000000000000001 0.20000000000000001 0
		-1 0.20000000000000001 0
		;
createNode transform -n "c_Rt_up_eyelids_FRAME_lockzyfyfx" -p "c_Rt_up_eyelids_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Rt_up_eyelids_FRAME_lockzyfyfxShape" -p "c_Rt_up_eyelids_FRAME_lockzyfyfx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 0.20000000000000001 0
		-0.20000000000000001 -0.20000000000000001 0
		1 -0.20000000000000001 0
		1 0.20000000000000001 0
		-0.20000000000000001 0.20000000000000001 0
		;
createNode transform -n "c_Rt_up_eyelids_FRAME_lockzxfxzy" -p "c_Rt_up_eyelids_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Rt_up_eyelids_FRAME_lockzxfxzyShape" -p "c_Rt_up_eyelids_FRAME_lockzxfxzy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 0.20000000000000001 0
		-0.20000000000000001 -1 0
		0.20000000000000001 -1 0
		0.20000000000000001 0.20000000000000001 0
		-0.20000000000000001 0.20000000000000001 0
		;
createNode transform -n "c_Rt_up_eyelids_FRAME_lockzxfxfy" -p "c_Rt_up_eyelids_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Rt_up_eyelids_FRAME_lockzxfxfyShape" -p "c_Rt_up_eyelids_FRAME_lockzxfxfy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 1 0
		-0.20000000000000001 -0.20000000000000001 0
		0.20000000000000001 -0.20000000000000001 0
		0.20000000000000001 1 0
		-0.20000000000000001 1 0
		;
createNode transform -n "c_Rt_up_eyelids_CTRL_up" -p "c_Rt_up_eyelids_FRAME";
	setAttr ".t" -type "double3" 0 2.2 0 ;
createNode nurbsCurve -n "curveShape85" -p "c_Rt_up_eyelids_CTRL_up";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_up_eyelids_LOC_up" -p "c_Rt_up_eyelids_CTRL_up";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_up_eyelids_CTRL_dn" -p "c_Rt_up_eyelids_FRAME";
	setAttr ".t" -type "double3" 0 -2.2 0 ;
createNode nurbsCurve -n "curveShape86" -p "c_Rt_up_eyelids_CTRL_dn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_up_eyelids_LOC_dn" -p "c_Rt_up_eyelids_CTRL_dn";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_up_eyelids_CTRL_lf" -p "c_Rt_up_eyelids_FRAME";
	setAttr ".t" -type "double3" -2.2 0 0 ;
createNode nurbsCurve -n "curveShape87" -p "c_Rt_up_eyelids_CTRL_lf";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_up_eyelids_LOC_lf" -p "c_Rt_up_eyelids_CTRL_lf";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_up_eyelids_CTRL_lfup" -p "c_Rt_up_eyelids_FRAME";
	setAttr ".t" -type "double3" -2.2 2.2 0 ;
createNode nurbsCurve -n "curveShape88" -p "c_Rt_up_eyelids_CTRL_lfup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_up_eyelids_LOC_lfup" -p "c_Rt_up_eyelids_CTRL_lfup";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_up_eyelids_CTRL_rt" -p "c_Rt_up_eyelids_FRAME";
	setAttr ".t" -type "double3" 2.2 0 0 ;
createNode nurbsCurve -n "curveShape89" -p "c_Rt_up_eyelids_CTRL_rt";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_up_eyelids_LOC_rt" -p "c_Rt_up_eyelids_CTRL_rt";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_up_eyelids_CTRL_rtup" -p "c_Rt_up_eyelids_FRAME";
	setAttr ".t" -type "double3" 2.2 2.2 0 ;
createNode nurbsCurve -n "curveShape90" -p "c_Rt_up_eyelids_CTRL_rtup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_up_eyelids_LOC_rtup" -p "c_Rt_up_eyelids_CTRL_rtup";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_up_eyelids_CTRL_lfdn" -p "c_Rt_up_eyelids_FRAME";
	setAttr ".t" -type "double3" -2.2 -2.2 0 ;
createNode nurbsCurve -n "curveShape91" -p "c_Rt_up_eyelids_CTRL_lfdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_up_eyelids_LOC_lfdn" -p "c_Rt_up_eyelids_CTRL_lfdn";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_up_eyelids_CTRL_rtdn" -p "c_Rt_up_eyelids_FRAME";
	setAttr ".t" -type "double3" 2.2 -2.2 0 ;
createNode nurbsCurve -n "curveShape92" -p "c_Rt_up_eyelids_CTRL_rtdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_up_eyelids_LOC_rtdn" -p "c_Rt_up_eyelids_CTRL_rtdn";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_up_eyelids_CTRL_fourAxisup" -p "c_Rt_up_eyelids_FRAME";
	setAttr ".t" -type "double3" 0 4.4 0 ;
createNode nurbsCurve -n "curveShape93" -p "c_Rt_up_eyelids_CTRL_fourAxisup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_up_eyelids_LOC_fourAxis_up" -p "c_Rt_up_eyelids_CTRL_fourAxisup";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_up_eyelids_CTRL_fourAxisdn" -p "c_Rt_up_eyelids_FRAME";
	setAttr ".t" -type "double3" 0 -4.4 0 ;
createNode nurbsCurve -n "curveShape94" -p "c_Rt_up_eyelids_CTRL_fourAxisdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_up_eyelids_LOC_fourAxis_dn" -p "c_Rt_up_eyelids_CTRL_fourAxisdn";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_up_eyelids_CTRL_fourAxislf" -p "c_Rt_up_eyelids_FRAME";
	setAttr ".t" -type "double3" -4.4 0 0 ;
createNode nurbsCurve -n "curveShape95" -p "c_Rt_up_eyelids_CTRL_fourAxislf";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_up_eyelids_LOC_fourAxis_lf" -p "c_Rt_up_eyelids_CTRL_fourAxislf";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_up_eyelids_CTRL_fourAxisrt" -p "c_Rt_up_eyelids_FRAME";
	setAttr ".t" -type "double3" 4.4 0 0 ;
createNode nurbsCurve -n "curveShape96" -p "c_Rt_up_eyelids_CTRL_fourAxisrt";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_up_eyelids_LOC_fourAxis_rt" -p "c_Rt_up_eyelids_CTRL_fourAxisrt";
	setAttr -k off ".v" no;
createNode transform -n "GRP_c_Rt_dn_eyelids_FRAME" -p "c_Rt_eyelids_CTRL";
	setAttr ".t" -type "double3" -0.59568934560581388 0.27868064396936604 -7.2950905038234194e-017 ;
	setAttr ".r" -type "double3" 0 -180 0 ;
	setAttr ".s" -type "double3" 0.15 0.15 0.15 ;
createNode transform -n "c_Rt_dn_eyelids_FRAME" -p "GRP_c_Rt_dn_eyelids_FRAME";
	addAttr -ci true -sn "up" -ln "up" -min 0 -at "double";
	addAttr -ci true -sn "dn" -ln "dn" -min 0 -at "double";
	addAttr -ci true -sn "lf" -ln "lf" -min 0 -at "double";
	addAttr -ci true -sn "rt" -ln "rt" -min 0 -at "double";
	addAttr -ci true -sn "lfup" -ln "lfup" -min 0 -at "double";
	addAttr -ci true -sn "rtup" -ln "rtup" -min 0 -at "double";
	addAttr -ci true -sn "lfdn" -ln "lfdn" -min 0 -at "double";
	addAttr -ci true -sn "rtdn" -ln "rtdn" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_up" -ln "fourAxis_up" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_dn" -ln "fourAxis_dn" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_lf" -ln "fourAxis_lf" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_rt" -ln "fourAxis_rt" -min 0 -at "double";
	addAttr -ci true -sn "up_Vis" -ln "up_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "dn_Vis" -ln "dn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lf_Vis" -ln "lf_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lfup_Vis" -ln "lfup_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rt_Vis" -ln "rt_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rtup_Vis" -ln "rtup_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lfdn_Vis" -ln "lfdn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rtdn_Vis" -ln "rtdn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_up_Vis" -ln "fourAxis_up_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_dn_Vis" -ln "fourAxis_dn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_lf_Vis" -ln "fourAxis_lf_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_rt_Vis" -ln "fourAxis_rt_Vis" -min 0 -max 1 -at "bool";
	setAttr -k on ".up";
	setAttr -k on ".dn";
	setAttr -k on ".lf";
	setAttr -k on ".rt";
	setAttr -k on ".lfup";
	setAttr -k on ".rtup";
	setAttr -k on ".lfdn";
	setAttr -k on ".rtdn";
	setAttr -k on ".fourAxis_up";
	setAttr -k on ".fourAxis_dn";
	setAttr -k on ".fourAxis_lf";
	setAttr -k on ".fourAxis_rt";
	setAttr -cb on ".up_Vis";
	setAttr -cb on ".dn_Vis";
	setAttr -cb on ".lf_Vis";
	setAttr -cb on ".lfup_Vis";
	setAttr -cb on ".rt_Vis";
	setAttr -cb on ".rtup_Vis";
	setAttr -cb on ".lfdn_Vis";
	setAttr -cb on ".rtdn_Vis";
	setAttr -cb on ".fourAxis_up_Vis";
	setAttr -cb on ".fourAxis_dn_Vis";
	setAttr -cb on ".fourAxis_lf_Vis";
	setAttr -cb on ".fourAxis_rt_Vis";
createNode nurbsCurve -n "c_Rt_dn_eyelids_FRAMEShape" -p "c_Rt_dn_eyelids_FRAME";
	setAttr -k off ".v" no;
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode transform -n "GRP_c_Rt_dn_eyelids_CTRL" -p "c_Rt_dn_eyelids_FRAME";
createNode transform -n "c_Rt_dn_eyelids_CTRL" -p "GRP_c_Rt_dn_eyelids_CTRL";
	addAttr -ci true -sn "frameSelectAble" -ln "frameSelectAble" -min 0 -max 2 -en 
		"normal:template:reference" -at "enum";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".mntl" -type "double3" -1 -1 0 ;
	setAttr ".mxtl" -type "double3" 1 1 0 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
	setAttr ".frameSelectAble" 2;
createNode nurbsCurve -n "c_Rt_dn_eyelids_CTRLShape" -p "c_Rt_dn_eyelids_CTRL";
	setAttr -k off ".v" no;
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		1 32 0 no 3
		33 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32
		33
		-0.050000000000000003 0.050000000000000003 0
		-0.050000000000000003 0.15000000000000002 0
		-0.10000000000000001 0.15000000000000002 0
		0 0.25 0
		0.10000000000000001 0.15000000000000002 0
		0.050000000000000003 0.15000000000000002 0
		0.050000000000000003 0.050000000000000003 0
		0.20000000000000001 0.20000000000000001 0
		0.050000000000000003 0.050000000000000003 0
		0.15000000000000002 0.050000000000000003 0
		0.15000000000000002 0.10000000000000001 0
		0.25 0 0
		0.15000000000000002 -0.10000000000000001 0
		0.15000000000000002 -0.050000000000000003 0
		0.050000000000000003 -0.050000000000000003 0
		0.20000000000000001 -0.20000000000000001 0
		0.050000000000000003 -0.050000000000000003 0
		0.050000000000000003 -0.15000000000000002 0
		0.10000000000000001 -0.15000000000000002 0
		0 -0.25 0
		-0.10000000000000001 -0.15000000000000002 0
		-0.050000000000000003 -0.15000000000000002 0
		-0.050000000000000003 -0.050000000000000003 0
		-0.20000000000000001 -0.20000000000000001 0
		-0.050000000000000003 -0.050000000000000003 0
		-0.15000000000000002 -0.050000000000000003 0
		-0.15000000000000002 -0.10000000000000001 0
		-0.25 0 0
		-0.15000000000000002 0.10000000000000001 0
		-0.15000000000000002 0.050000000000000003 0
		-0.050000000000000003 0.050000000000000003 0
		-0.20000000000000001 0.20000000000000001 0
		-0.050000000000000003 0.050000000000000003 0
		;
createNode transform -n "c_Rt_dn_eyelids_FRAME_lockzy" -p "c_Rt_dn_eyelids_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Rt_dn_eyelids_FRAME_lockzyShape" -p "c_Rt_dn_eyelids_FRAME_lockzy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 0.20000000000000001 0
		-1 -1 0
		1 -1 0
		1 0.20000000000000001 0
		-1 0.20000000000000001 0
		;
createNode transform -n "c_Rt_dn_eyelids_FRAME_lockfy" -p "c_Rt_dn_eyelids_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Rt_dn_eyelids_FRAME_lockfyShape" -p "c_Rt_dn_eyelids_FRAME_lockfy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -0.20000000000000001 0
		1 -0.20000000000000001 0
		1 1 0
		-1 1 0
		;
createNode transform -n "c_Rt_dn_eyelids_FRAME_lockzx" -p "c_Rt_dn_eyelids_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Rt_dn_eyelids_FRAME_lockzxShape" -p "c_Rt_dn_eyelids_FRAME_lockzx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		0.20000000000000001 -1 0
		0.20000000000000001 1 0
		-1 1 0
		;
createNode transform -n "c_Rt_dn_eyelids_FRAME_lockfx" -p "c_Rt_dn_eyelids_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Rt_dn_eyelids_FRAME_lockfxShape" -p "c_Rt_dn_eyelids_FRAME_lockfx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 1 0
		-0.20000000000000001 -1 0
		1 -1 0
		1 1 0
		-0.20000000000000001 1 0
		;
createNode transform -n "c_Rt_dn_eyelids_FRAME_lockzyfy" -p "c_Rt_dn_eyelids_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Rt_dn_eyelids_FRAME_lockzyfyShape" -p "c_Rt_dn_eyelids_FRAME_lockzyfy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 0.20000000000000001 0
		-1 -0.20000000000000001 0
		1 -0.20000000000000001 0
		1 0.20000000000000001 0
		-1 0.20000000000000001 0
		;
createNode transform -n "c_Rt_dn_eyelids_FRAME_lockzxfx" -p "c_Rt_dn_eyelids_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Rt_dn_eyelids_FRAME_lockzxfxShape" -p "c_Rt_dn_eyelids_FRAME_lockzxfx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 1 0
		-0.20000000000000001 -1 0
		0.20000000000000001 -1 0
		0.20000000000000001 1 0
		-0.20000000000000001 1 0
		;
createNode transform -n "c_Rt_dn_eyelids_FRAME_lockzyfyzx" -p "c_Rt_dn_eyelids_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Rt_dn_eyelids_FRAME_lockzyfyzxShape" -p "c_Rt_dn_eyelids_FRAME_lockzyfyzx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 0.20000000000000001 0
		-1 -0.20000000000000001 0
		0.20000000000000001 -0.20000000000000001 0
		0.20000000000000001 0.20000000000000001 0
		-1 0.20000000000000001 0
		;
createNode transform -n "c_Rt_dn_eyelids_FRAME_lockzyfyfx" -p "c_Rt_dn_eyelids_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Rt_dn_eyelids_FRAME_lockzyfyfxShape" -p "c_Rt_dn_eyelids_FRAME_lockzyfyfx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 0.20000000000000001 0
		-0.20000000000000001 -0.20000000000000001 0
		1 -0.20000000000000001 0
		1 0.20000000000000001 0
		-0.20000000000000001 0.20000000000000001 0
		;
createNode transform -n "c_Rt_dn_eyelids_FRAME_lockzxfxzy" -p "c_Rt_dn_eyelids_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Rt_dn_eyelids_FRAME_lockzxfxzyShape" -p "c_Rt_dn_eyelids_FRAME_lockzxfxzy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 0.20000000000000001 0
		-0.20000000000000001 -1 0
		0.20000000000000001 -1 0
		0.20000000000000001 0.20000000000000001 0
		-0.20000000000000001 0.20000000000000001 0
		;
createNode transform -n "c_Rt_dn_eyelids_FRAME_lockzxfxfy" -p "c_Rt_dn_eyelids_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Rt_dn_eyelids_FRAME_lockzxfxfyShape" -p "c_Rt_dn_eyelids_FRAME_lockzxfxfy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 1 0
		-0.20000000000000001 -0.20000000000000001 0
		0.20000000000000001 -0.20000000000000001 0
		0.20000000000000001 1 0
		-0.20000000000000001 1 0
		;
createNode transform -n "c_Rt_dn_eyelids_CTRL_up" -p "c_Rt_dn_eyelids_FRAME";
	setAttr ".t" -type "double3" 0 2.2 0 ;
createNode nurbsCurve -n "curveShape109" -p "c_Rt_dn_eyelids_CTRL_up";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_dn_eyelids_LOC_up" -p "c_Rt_dn_eyelids_CTRL_up";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_dn_eyelids_CTRL_dn" -p "c_Rt_dn_eyelids_FRAME";
	setAttr ".t" -type "double3" 0 -2.2 0 ;
createNode nurbsCurve -n "curveShape110" -p "c_Rt_dn_eyelids_CTRL_dn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_dn_eyelids_LOC_dn" -p "c_Rt_dn_eyelids_CTRL_dn";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_dn_eyelids_CTRL_lf" -p "c_Rt_dn_eyelids_FRAME";
	setAttr ".t" -type "double3" -2.2 0 0 ;
createNode nurbsCurve -n "curveShape111" -p "c_Rt_dn_eyelids_CTRL_lf";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_dn_eyelids_LOC_lf" -p "c_Rt_dn_eyelids_CTRL_lf";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_dn_eyelids_CTRL_lfup" -p "c_Rt_dn_eyelids_FRAME";
	setAttr ".t" -type "double3" -2.2 2.2 0 ;
createNode nurbsCurve -n "curveShape112" -p "c_Rt_dn_eyelids_CTRL_lfup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_dn_eyelids_LOC_lfup" -p "c_Rt_dn_eyelids_CTRL_lfup";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_dn_eyelids_CTRL_rt" -p "c_Rt_dn_eyelids_FRAME";
	setAttr ".t" -type "double3" 2.2 0 0 ;
createNode nurbsCurve -n "curveShape113" -p "c_Rt_dn_eyelids_CTRL_rt";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_dn_eyelids_LOC_rt" -p "c_Rt_dn_eyelids_CTRL_rt";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_dn_eyelids_CTRL_rtup" -p "c_Rt_dn_eyelids_FRAME";
	setAttr ".t" -type "double3" 2.2 2.2 0 ;
createNode nurbsCurve -n "curveShape114" -p "c_Rt_dn_eyelids_CTRL_rtup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_dn_eyelids_LOC_rtup" -p "c_Rt_dn_eyelids_CTRL_rtup";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_dn_eyelids_CTRL_lfdn" -p "c_Rt_dn_eyelids_FRAME";
	setAttr ".t" -type "double3" -2.2 -2.2 0 ;
createNode nurbsCurve -n "curveShape115" -p "c_Rt_dn_eyelids_CTRL_lfdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_dn_eyelids_LOC_lfdn" -p "c_Rt_dn_eyelids_CTRL_lfdn";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_dn_eyelids_CTRL_rtdn" -p "c_Rt_dn_eyelids_FRAME";
	setAttr ".t" -type "double3" 2.2 -2.2 0 ;
createNode nurbsCurve -n "curveShape116" -p "c_Rt_dn_eyelids_CTRL_rtdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_dn_eyelids_LOC_rtdn" -p "c_Rt_dn_eyelids_CTRL_rtdn";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_dn_eyelids_CTRL_fourAxisup" -p "c_Rt_dn_eyelids_FRAME";
	setAttr ".t" -type "double3" 0 4.4 0 ;
createNode nurbsCurve -n "curveShape117" -p "c_Rt_dn_eyelids_CTRL_fourAxisup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_dn_eyelids_LOC_fourAxis_up" -p "c_Rt_dn_eyelids_CTRL_fourAxisup";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_dn_eyelids_CTRL_fourAxisdn" -p "c_Rt_dn_eyelids_FRAME";
	setAttr ".t" -type "double3" 0 -4.4 0 ;
createNode nurbsCurve -n "curveShape118" -p "c_Rt_dn_eyelids_CTRL_fourAxisdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_dn_eyelids_LOC_fourAxis_dn" -p "c_Rt_dn_eyelids_CTRL_fourAxisdn";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_dn_eyelids_CTRL_fourAxislf" -p "c_Rt_dn_eyelids_FRAME";
	setAttr ".t" -type "double3" -4.4 0 0 ;
createNode nurbsCurve -n "curveShape119" -p "c_Rt_dn_eyelids_CTRL_fourAxislf";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_dn_eyelids_LOC_fourAxis_lf" -p "c_Rt_dn_eyelids_CTRL_fourAxislf";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_dn_eyelids_CTRL_fourAxisrt" -p "c_Rt_dn_eyelids_FRAME";
	setAttr ".t" -type "double3" 4.4 0 0 ;
createNode nurbsCurve -n "curveShape120" -p "c_Rt_dn_eyelids_CTRL_fourAxisrt";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_dn_eyelids_LOC_fourAxis_rt" -p "c_Rt_dn_eyelids_CTRL_fourAxisrt";
	setAttr -k off ".v" no;
createNode transform -n "c_head_top_CTRL_GRP" -p "head_CTRL";
	addAttr -ci true -k true -sn "T1" -ln "T1" -at "double";
	addAttr -ci true -k true -sn "T2" -ln "T2" -at "double";
	addAttr -ci true -k true -sn "T3" -ln "T3" -at "double";
	addAttr -ci true -k true -sn "R1" -ln "R1" -at "double";
	addAttr -ci true -k true -sn "R2" -ln "R2" -at "double";
	addAttr -ci true -k true -sn "R3" -ln "R3" -at "double";
	addAttr -ci true -sn "S1" -ln "S1" -at "double";
	addAttr -ci true -sn "S2" -ln "S2" -at "double";
	addAttr -ci true -sn "S3" -ln "S3" -at "double";
	setAttr ".rp" -type "double3" 0 1.9431389628644593 0.017959868467468082 ;
	setAttr ".sp" -type "double3" 0 1.9431389628644593 0.017959868467468082 ;
	setAttr -k on ".S1" 1;
	setAttr -k on ".S2" 1;
	setAttr -k on ".S3" 1;
createNode transform -n "c_head_top_CTRL" -p "c_head_top_CTRL_GRP";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 0 1.9195916094266003 0.017959868467468072 ;
	setAttr ".sp" -type "double3" 0 1.9195916094266021 0.017959868467468072 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
createNode nurbsCurve -n "c_head_top_CTRLShape" -p "c_head_top_CTRL";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.80035796967966721 2.066391723503215 0.017959868467468089
		-1.2913364269449901e-016 2.3202314277630629 0.017959868467468051
		-0.80035796967966644 2.0663917235032154 0.017959868467468089
		-1.1318770954743789 1.5660464979658557 0.017959868467468151
		-0.80035796967966666 1.6847846073748258 0.017959868467468075
		-3.4105665871377893e-016 1.9022229337682388 0.017959868467468009
		0.80035796967966599 1.6847846073748258 0.017959868467468075
		1.1318770954743789 1.5660464979658557 0.017959868467468151
		0.80035796967966721 2.066391723503215 0.017959868467468089
		-1.2913364269449901e-016 2.3202314277630629 0.017959868467468051
		-0.80035796967966644 2.0663917235032154 0.017959868467468089
		;
createNode transform -n "c_head_bottom_CTRL_GRP" -p "head_CTRL";
	addAttr -ci true -k true -sn "T1" -ln "T1" -at "double";
	addAttr -ci true -k true -sn "T2" -ln "T2" -at "double";
	addAttr -ci true -k true -sn "T3" -ln "T3" -at "double";
	addAttr -ci true -k true -sn "R1" -ln "R1" -at "double";
	addAttr -ci true -k true -sn "R2" -ln "R2" -at "double";
	addAttr -ci true -k true -sn "R3" -ln "R3" -at "double";
	addAttr -ci true -sn "S1" -ln "S1" -at "double";
	addAttr -ci true -sn "S2" -ln "S2" -at "double";
	addAttr -ci true -sn "S3" -ln "S3" -at "double";
	setAttr ".rp" -type "double3" 0 -1.8428001309486892 0.017959868467468929 ;
	setAttr ".sp" -type "double3" 0 -1.8428001309486892 0.017959868467468929 ;
	setAttr -k on ".S1" 1;
	setAttr -k on ".S2" 1;
	setAttr -k on ".S3" 1;
createNode transform -n "c_head_bottom_CTRL" -p "c_head_bottom_CTRL_GRP";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 0 -1.8838647742525503 0.017959868467468918 ;
	setAttr ".sp" -type "double3" 0 -1.8838647742525487 0.017959868467468918 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
createNode nurbsCurve -n "c_head_bottom_CTRLShape" -p "c_head_bottom_CTRL";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.64852112862328959 -1.9289469763090203 0.017959868467468967
		-1.0463554918681113e-016 -2.1374695908963579 0.017959868467469029
		-0.64852112862328892 -1.9289469763090203 0.017959868467468967
		-0.91714737558456172 -1.5481306710010205 0.017959868467468842
		-0.64852112862328914 -1.6456708926826935 0.017959868467468824
		-2.7635440342035124e-016 -1.8695968658070921 0.017959868467468859
		0.64852112862328859 -1.6456708926826935 0.017959868467468824
		0.91714737558456172 -1.5481306710010205 0.017959868467468842
		0.64852112862328959 -1.9289469763090203 0.017959868467468967
		-1.0463554918681113e-016 -2.1374695908963579 0.017959868467469029
		-0.64852112862328892 -1.9289469763090203 0.017959868467468967
		;
createNode transform -n "c_Lf_ear_CTRL_GRP" -p "head_CTRL";
	addAttr -ci true -k true -sn "T1" -ln "T1" -at "double";
	addAttr -ci true -k true -sn "T2" -ln "T2" -at "double";
	addAttr -ci true -k true -sn "T3" -ln "T3" -at "double";
	addAttr -ci true -k true -sn "R1" -ln "R1" -at "double";
	addAttr -ci true -k true -sn "R2" -ln "R2" -at "double";
	addAttr -ci true -k true -sn "R3" -ln "R3" -at "double";
	addAttr -ci true -sn "S1" -ln "S1" -at "double";
	addAttr -ci true -sn "S2" -ln "S2" -at "double";
	addAttr -ci true -sn "S3" -ln "S3" -at "double";
	setAttr ".rp" -type "double3" 1.3621751717825445 -0.01195900539510035 0.017959868467468533 ;
	setAttr ".sp" -type "double3" 1.3621751717825445 -0.01195900539510035 0.017959868467468533 ;
	setAttr -k on ".S1" 1;
	setAttr -k on ".S2" 1;
	setAttr -k on ".S3" 1;
createNode transform -n "c_Lf_ear_CTRL" -p "c_Lf_ear_CTRL_GRP";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".rp" -type "double3" 1.3621751717825445 -0.01195900539510035 0.017959868467468533 ;
	setAttr ".sp" -type "double3" 1.3621751717825445 -0.01195900539510035 0.017959868467468533 ;
createNode nurbsCurve -n "c_Lf_ear_CTRLShape" -p "c_Lf_ear_CTRL";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		1.8801578750117995 0.38392297822554866 0.017959868467468439
		1.4778780569584615 0.40384780238955958 0.017959868467468439
		1.3748938444008607 0.25772145598404134 0.017959868467468467
		1.3578166281719859 -0.10775009501476329 0.01795986846746853
		1.3234627211603525 -0.47227469855814197 0.017959868467468592
		1.2955130648653099 -0.62251374125574943 0.01795986846746862
		1.6680531949284454 -0.49116194244076233 0.017959868467468599
		1.9062436424360565 -0.13780976165892544 0.017959868467468536
		1.8801578750117995 0.38392297822554866 0.017959868467468439
		1.4778780569584615 0.40384780238955958 0.017959868467468439
		1.3748938444008607 0.25772145598404134 0.017959868467468467
		;
createNode transform -n "c_Rt_ear_CTRL_GRP_GRP" -p "head_CTRL";
	setAttr ".r" -type "double3" 180 0 0 ;
	setAttr ".rp" -type "double3" -1.3619233749248725 -0.0075651078952623345 0.017959868467468533 ;
	setAttr ".sp" -type "double3" -1.3619233749248725 -0.0075651078952623345 0.017959868467468533 ;
createNode transform -n "c_Rt_ear_CTRL_GRP" -p "c_Rt_ear_CTRL_GRP_GRP";
	addAttr -ci true -k true -sn "T1" -ln "T1" -at "double";
	addAttr -ci true -k true -sn "T2" -ln "T2" -at "double";
	addAttr -ci true -k true -sn "T3" -ln "T3" -at "double";
	addAttr -ci true -k true -sn "R1" -ln "R1" -at "double";
	addAttr -ci true -k true -sn "R2" -ln "R2" -at "double";
	addAttr -ci true -k true -sn "R3" -ln "R3" -at "double";
	addAttr -ci true -sn "S1" -ln "S1" -at "double";
	addAttr -ci true -sn "S2" -ln "S2" -at "double";
	addAttr -ci true -sn "S3" -ln "S3" -at "double";
	setAttr ".rp" -type "double3" -1.3619233749248725 -0.0075651078952623345 0.017959868467468533 ;
	setAttr ".rpt" -type "double3" 0 0.015130215790524672 -0.035919736934937066 ;
	setAttr ".sp" -type "double3" -1.3619233749248725 -0.0075651078952623345 0.017959868467468533 ;
	setAttr -k on ".S1" 1;
	setAttr -k on ".S2" 1;
	setAttr -k on ".S3" 1;
createNode transform -n "c_Rt_ear_CTRL" -p "c_Rt_ear_CTRL_GRP";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".rp" -type "double3" -1.3619233749248725 -0.0075651078952623345 0.017959868467468533 ;
	setAttr ".rpt" -type "double3" 0 0.015130215790524666 -0.035919736934937066 ;
	setAttr ".sp" -type "double3" -1.3619233749248725 -0.0075651078952623345 0.017959868467468533 ;
createNode nurbsCurve -n "c_Rt_ear_CTRLShape" -p "c_Rt_ear_CTRL";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-1.8801578750117995 -0.39905378762382543 0.01886595738737866
		-1.4778780569584615 -0.41897860184840674 0.018885859213048622
		-1.3748938444008607 -0.27285232833750928 0.018739901534928129
		-1.3578166281719859 0.092619040347081502 0.018374851834343106
		-1.3234627211603525 0.45714346204862738 0.018010747988186783
		-1.2955130648653099 0.60738242980001111 0.017860682360908601
		-1.6680531949284454 0.47603069650941188 0.017991882545157406
		-1.9062436424360565 0.12267869199608337 0.018344826864470209
		-1.8801578750117995 -0.39905378762382543 0.01886595738737866
		-1.4778780569584615 -0.41897860184840674 0.018885859213048622
		-1.3748938444008607 -0.27285232833750928 0.018739901534928129
		;
createNode transform -n "c_mouth_CTRL_GRP" -p "head_CTRL";
	addAttr -ci true -k true -sn "T1" -ln "T1" -at "double";
	addAttr -ci true -k true -sn "T2" -ln "T2" -at "double";
	addAttr -ci true -k true -sn "T3" -ln "T3" -at "double";
	addAttr -ci true -k true -sn "R1" -ln "R1" -at "double";
	addAttr -ci true -k true -sn "R2" -ln "R2" -at "double";
	addAttr -ci true -k true -sn "R3" -ln "R3" -at "double";
	addAttr -ci true -sn "S1" -ln "S1" -at "double";
	addAttr -ci true -sn "S2" -ln "S2" -at "double";
	addAttr -ci true -sn "S3" -ln "S3" -at "double";
	setAttr ".rp" -type "double3" 0 -1.0192970667831824 0.0089799342337343845 ;
	setAttr ".sp" -type "double3" 0 -1.0192970667831824 0.0089799342337343845 ;
	setAttr -k on ".S1" 1;
	setAttr -k on ".S2" 1;
	setAttr -k on ".S3" 1;
createNode transform -n "c_mouth_CTRL" -p "c_mouth_CTRL_GRP";
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr ".rp" -type "double3" 0 -0.94213755006190936 0.017959868467468769 ;
	setAttr ".sp" -type "double3" 0 -0.94213755006190936 0.017959868467468769 ;
createNode nurbsCurve -n "c_mouth_CTRLShape" -p "c_mouth_CTRL";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.70407939961258448 -0.57076019322906835 0.017959868467468731
		-1.1359959051137897e-016 -0.41693065527063278 0.01795986846746871
		-0.70407939961258381 -0.57076019322906812 0.017959868467468731
		-1.0614660063426757 -0.74856835952196099 0.017959868467468727
		-0.70407939961258403 -1.3626164175355613 0.017959868467468821
		-3.0002945756532031e-016 -1.6216634782957322 0.017959868467468859
		0.70407939961258337 -1.3626164175355608 0.017959868467468821
		1.0614660063426757 -0.74856835952196132 0.017959868467468727
		0.70407939961258448 -0.57076019322906835 0.017959868467468731
		-1.1359959051137897e-016 -0.41693065527063278 0.01795986846746871
		-0.70407939961258381 -0.57076019322906812 0.017959868467468731
		;
createNode nurbsCurve -n "c_mouth_CTRLShape19Orig" -p "c_mouth_CTRL";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.70407939961258448 4.3282413254256795e-017 0.58872006169653679
		-1.1359959051137897e-016 6.1210575836407002e-017 0.43489052373810122
		-0.70407939961258381 4.328241325425682e-017 0.58872006169653657
		-0.99571863591962229 1.7737293509693569e-032 0.9600974185293778
		-0.70407939961258403 -4.3282413254256808e-017 1.3314747753622194
		-3.0002945756532031e-016 -6.1210575836407014e-017 1.4853043133206549
		0.70407939961258337 -4.3282413254256826e-017 1.3314747753622194
		0.99571863591962229 -3.287631968731418e-032 0.96009741852937813
		0.70407939961258448 4.3282413254256795e-017 0.58872006169653679
		-1.1359959051137897e-016 6.1210575836407002e-017 0.43489052373810122
		-0.70407939961258381 4.328241325425682e-017 0.58872006169653657
		;
createNode transform -n "GRP_c_jaw_dn_FRAME" -p "c_mouth_CTRL";
	setAttr ".t" -type "double3" 0 -1.2339426240365641 0 ;
	setAttr ".s" -type "double3" 0.5 0.2 0.4 ;
createNode transform -n "c_jaw_dn_FRAME" -p "GRP_c_jaw_dn_FRAME";
	addAttr -ci true -sn "up" -ln "up" -min 0 -at "double";
	addAttr -ci true -sn "dn" -ln "dn" -min 0 -at "double";
	addAttr -ci true -sn "lf" -ln "lf" -min 0 -at "double";
	addAttr -ci true -sn "rt" -ln "rt" -min 0 -at "double";
	addAttr -ci true -sn "lfup" -ln "lfup" -min 0 -at "double";
	addAttr -ci true -sn "rtup" -ln "rtup" -min 0 -at "double";
	addAttr -ci true -sn "lfdn" -ln "lfdn" -min 0 -at "double";
	addAttr -ci true -sn "rtdn" -ln "rtdn" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_up" -ln "fourAxis_up" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_dn" -ln "fourAxis_dn" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_lf" -ln "fourAxis_lf" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_rt" -ln "fourAxis_rt" -min 0 -at "double";
	addAttr -ci true -sn "up_Vis" -ln "up_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "dn_Vis" -ln "dn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lf_Vis" -ln "lf_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lfup_Vis" -ln "lfup_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rt_Vis" -ln "rt_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rtup_Vis" -ln "rtup_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lfdn_Vis" -ln "lfdn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rtdn_Vis" -ln "rtdn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_up_Vis" -ln "fourAxis_up_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_dn_Vis" -ln "fourAxis_dn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_lf_Vis" -ln "fourAxis_lf_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_rt_Vis" -ln "fourAxis_rt_Vis" -min 0 -max 1 -at "bool";
	setAttr -k on ".up";
	setAttr -k on ".dn";
	setAttr -k on ".lf";
	setAttr -k on ".rt";
	setAttr -k on ".lfup";
	setAttr -k on ".rtup";
	setAttr -k on ".lfdn";
	setAttr -k on ".rtdn";
	setAttr -k on ".fourAxis_up";
	setAttr -k on ".fourAxis_dn";
	setAttr -k on ".fourAxis_lf";
	setAttr -k on ".fourAxis_rt";
	setAttr -cb on ".up_Vis";
	setAttr -cb on ".dn_Vis";
	setAttr -cb on ".lf_Vis";
	setAttr -cb on ".lfup_Vis";
	setAttr -cb on ".rt_Vis";
	setAttr -cb on ".rtup_Vis";
	setAttr -cb on ".lfdn_Vis";
	setAttr -cb on ".rtdn_Vis";
	setAttr -cb on ".fourAxis_up_Vis";
	setAttr -cb on ".fourAxis_dn_Vis";
	setAttr -cb on ".fourAxis_lf_Vis";
	setAttr -cb on ".fourAxis_rt_Vis";
createNode nurbsCurve -n "c_jaw_dn_FRAMEShape" -p "c_jaw_dn_FRAME";
	setAttr -k off ".v" no;
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode transform -n "GRP_c_jaw_dn_CTRL" -p "c_jaw_dn_FRAME";
	addAttr -ci true -k true -sn "T1" -ln "T1" -at "double";
	addAttr -ci true -k true -sn "T2" -ln "T2" -at "double";
	addAttr -ci true -k true -sn "T3" -ln "T3" -at "double";
	addAttr -ci true -k true -sn "R1" -ln "R1" -at "double";
	addAttr -ci true -k true -sn "R2" -ln "R2" -at "double";
	addAttr -ci true -k true -sn "R3" -ln "R3" -at "double";
	addAttr -ci true -sn "S1" -ln "S1" -at "double";
	addAttr -ci true -sn "S2" -ln "S2" -at "double";
	addAttr -ci true -sn "S3" -ln "S3" -at "double";
	setAttr -k on ".S1" 1;
	setAttr -k on ".S2" 1;
	setAttr -k on ".S3" 1;
createNode transform -n "c_jaw_dn_CTRL" -p "GRP_c_jaw_dn_CTRL";
	addAttr -ci true -sn "frameSelectAble" -ln "frameSelectAble" -min 0 -max 2 -en 
		"normal:template:reference" -at "enum";
	addAttr -ci true -sn "sticky_lips" -ln "sticky_lips" -min 0 -max 10 -at "double";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".mntl" -type "double3" -1 -1 0 ;
	setAttr ".mxtl" -type "double3" 1 1 0 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
	setAttr ".frameSelectAble" 2;
	setAttr -k on ".sticky_lips";
createNode nurbsCurve -n "c_jaw_dn_CTRLShape" -p "c_jaw_dn_CTRL";
	setAttr -k off ".v" no;
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		1 32 0 no 3
		33 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32
		33
		-0.050000000000000003 0.050000000000000003 0
		-0.050000000000000003 0.15000000000000002 0
		-0.10000000000000001 0.15000000000000002 0
		0 0.25 0
		0.10000000000000001 0.15000000000000002 0
		0.050000000000000003 0.15000000000000002 0
		0.050000000000000003 0.050000000000000003 0
		0.20000000000000001 0.20000000000000001 0
		0.050000000000000003 0.050000000000000003 0
		0.15000000000000002 0.050000000000000003 0
		0.15000000000000002 0.10000000000000001 0
		0.25 0 0
		0.15000000000000002 -0.10000000000000001 0
		0.15000000000000002 -0.050000000000000003 0
		0.050000000000000003 -0.050000000000000003 0
		0.20000000000000001 -0.20000000000000001 0
		0.050000000000000003 -0.050000000000000003 0
		0.050000000000000003 -0.15000000000000002 0
		0.10000000000000001 -0.15000000000000002 0
		0 -0.25 0
		-0.10000000000000001 -0.15000000000000002 0
		-0.050000000000000003 -0.15000000000000002 0
		-0.050000000000000003 -0.050000000000000003 0
		-0.20000000000000001 -0.20000000000000001 0
		-0.050000000000000003 -0.050000000000000003 0
		-0.15000000000000002 -0.050000000000000003 0
		-0.15000000000000002 -0.10000000000000001 0
		-0.25 0 0
		-0.15000000000000002 0.10000000000000001 0
		-0.15000000000000002 0.050000000000000003 0
		-0.050000000000000003 0.050000000000000003 0
		-0.20000000000000001 0.20000000000000001 0
		-0.050000000000000003 0.050000000000000003 0
		;
createNode nurbsCurve -n "c_jaw_dn_CTRLShape02" -p "c_jaw_dn_CTRL";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.85136933868830866 -0.22049937383370258 1.7954815059504381e-016
		6.0752296470012115e-016 -0.94605804819826345 2.8863719584265979e-016
		-0.85136933868830378 -0.22049937383370258 1.7954815059504381e-016
		-1.2294520160883031 0.16917261955454493 2.2732648051595361e-017
		-1.6637945938711522 1.5983502047688023 -2.2271770375554083e-016
		9.1203104872489069e-017 0.67316458607683849 -1.954454424436372e-016
		1.6637945938711522 1.5983502047688023 -2.2271770375554083e-016
		1.2294520160883045 0.16917261955454493 2.2732648051595361e-017
		0.85136933868830866 -0.22049937383370258 1.7954815059504381e-016
		6.0752296470012115e-016 -0.94605804819826345 2.8863719584265979e-016
		-0.85136933868830378 -0.22049937383370258 1.7954815059504381e-016
		;
createNode transform -n "GRP_c_dn_mouthLip_FRAME" -p "c_jaw_dn_CTRL";
	setAttr ".t" -type "double3" 0 0.45491513965933095 0 ;
	setAttr ".s" -type "double3" 0.6 0.75 0.5 ;
createNode transform -n "c_dn_mouthLip_FRAME" -p "GRP_c_dn_mouthLip_FRAME";
	addAttr -ci true -sn "up" -ln "up" -min 0 -at "double";
	addAttr -ci true -sn "dn" -ln "dn" -min 0 -at "double";
	addAttr -ci true -sn "lf" -ln "lf" -min 0 -at "double";
	addAttr -ci true -sn "rt" -ln "rt" -min 0 -at "double";
	addAttr -ci true -sn "lfup" -ln "lfup" -min 0 -at "double";
	addAttr -ci true -sn "rtup" -ln "rtup" -min 0 -at "double";
	addAttr -ci true -sn "lfdn" -ln "lfdn" -min 0 -at "double";
	addAttr -ci true -sn "rtdn" -ln "rtdn" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_up" -ln "fourAxis_up" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_dn" -ln "fourAxis_dn" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_lf" -ln "fourAxis_lf" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_rt" -ln "fourAxis_rt" -min 0 -at "double";
	addAttr -ci true -sn "up_Vis" -ln "up_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "dn_Vis" -ln "dn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lf_Vis" -ln "lf_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lfup_Vis" -ln "lfup_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rt_Vis" -ln "rt_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rtup_Vis" -ln "rtup_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lfdn_Vis" -ln "lfdn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rtdn_Vis" -ln "rtdn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_up_Vis" -ln "fourAxis_up_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_dn_Vis" -ln "fourAxis_dn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_lf_Vis" -ln "fourAxis_lf_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_rt_Vis" -ln "fourAxis_rt_Vis" -min 0 -max 1 -at "bool";
	setAttr -k on ".up";
	setAttr -k on ".dn";
	setAttr -k on ".lf";
	setAttr -k on ".rt";
	setAttr -k on ".lfup";
	setAttr -k on ".rtup";
	setAttr -k on ".lfdn";
	setAttr -k on ".rtdn";
	setAttr -k on ".fourAxis_up";
	setAttr -k on ".fourAxis_dn";
	setAttr -k on ".fourAxis_lf";
	setAttr -k on ".fourAxis_rt";
	setAttr -cb on ".up_Vis";
	setAttr -cb on ".dn_Vis";
	setAttr -cb on ".lf_Vis";
	setAttr -cb on ".lfup_Vis";
	setAttr -cb on ".rt_Vis";
	setAttr -cb on ".rtup_Vis";
	setAttr -cb on ".lfdn_Vis";
	setAttr -cb on ".rtdn_Vis";
	setAttr -cb on ".fourAxis_up_Vis";
	setAttr -cb on ".fourAxis_dn_Vis";
	setAttr -cb on ".fourAxis_lf_Vis";
	setAttr -cb on ".fourAxis_rt_Vis";
createNode nurbsCurve -n "c_dn_mouthLip_FRAMEShape" -p "c_dn_mouthLip_FRAME";
	setAttr -k off ".v" no;
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode transform -n "GRP_c_dn_mouthLip_CTRL" -p "c_dn_mouthLip_FRAME";
	addAttr -ci true -k true -sn "T1" -ln "T1" -at "double";
	addAttr -ci true -k true -sn "T2" -ln "T2" -at "double";
	addAttr -ci true -k true -sn "T3" -ln "T3" -at "double";
	addAttr -ci true -k true -sn "R1" -ln "R1" -at "double";
	addAttr -ci true -k true -sn "R2" -ln "R2" -at "double";
	addAttr -ci true -k true -sn "R3" -ln "R3" -at "double";
	addAttr -ci true -sn "S1" -ln "S1" -at "double";
	addAttr -ci true -sn "S2" -ln "S2" -at "double";
	addAttr -ci true -sn "S3" -ln "S3" -at "double";
	setAttr -k on ".S1" 1;
	setAttr -k on ".S2" 1;
	setAttr -k on ".S3" 1;
createNode transform -n "c_dn_mouthLip_CTRL" -p "GRP_c_dn_mouthLip_CTRL";
	addAttr -ci true -sn "frameSelectAble" -ln "frameSelectAble" -min 0 -max 2 -en 
		"normal:template:reference" -at "enum";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".mntl" -type "double3" -1 -1 0 ;
	setAttr ".mxtl" -type "double3" 1 1 0 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
	setAttr ".mnrl" -type "double3" -29.999999999999996 -45 -45 ;
	setAttr ".mxrl" -type "double3" 29.999999999999996 45 45 ;
	setAttr ".mrxe" yes;
	setAttr ".xrxe" yes;
	setAttr ".frameSelectAble" 2;
createNode nurbsCurve -n "c_dn_mouthLip_CTRLShape" -p "c_dn_mouthLip_CTRL";
	setAttr -k off ".v" no;
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		1 32 0 no 3
		33 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32
		33
		-0.050000000000000003 0.050000000000000003 0
		-0.050000000000000003 0.15000000000000002 0
		-0.10000000000000001 0.15000000000000002 0
		0 0.25 0
		0.10000000000000001 0.15000000000000002 0
		0.050000000000000003 0.15000000000000002 0
		0.050000000000000003 0.050000000000000003 0
		0.20000000000000001 0.20000000000000001 0
		0.050000000000000003 0.050000000000000003 0
		0.15000000000000002 0.050000000000000003 0
		0.15000000000000002 0.10000000000000001 0
		0.25 0 0
		0.15000000000000002 -0.10000000000000001 0
		0.15000000000000002 -0.050000000000000003 0
		0.050000000000000003 -0.050000000000000003 0
		0.20000000000000001 -0.20000000000000001 0
		0.050000000000000003 -0.050000000000000003 0
		0.050000000000000003 -0.15000000000000002 0
		0.10000000000000001 -0.15000000000000002 0
		0 -0.25 0
		-0.10000000000000001 -0.15000000000000002 0
		-0.050000000000000003 -0.15000000000000002 0
		-0.050000000000000003 -0.050000000000000003 0
		-0.20000000000000001 -0.20000000000000001 0
		-0.050000000000000003 -0.050000000000000003 0
		-0.15000000000000002 -0.050000000000000003 0
		-0.15000000000000002 -0.10000000000000001 0
		-0.25 0 0
		-0.15000000000000002 0.10000000000000001 0
		-0.15000000000000002 0.050000000000000003 0
		-0.050000000000000003 0.050000000000000003 0
		-0.20000000000000001 0.20000000000000001 0
		-0.050000000000000003 0.050000000000000003 0
		;
createNode nurbsCurve -n "c_dn_mouthLip_CTRLShape02" -p "c_dn_mouthLip_CTRL";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.52303097518750874 -0.18164105554797427 1.5032983699872164e-016
		3.6056972985635011e-016 -0.41845967235616205 2.3127667230572574e-016
		-0.5230309751875073 -0.18164105554797427 1.5032983699872164e-016
		-0.75530261391799536 0.019900135768223783 -1.1563833615286273e-017
		-1.0221370084631691 0.2824330223887368 -1.7345750422929411e-016
		5.6029794254841812e-017 0.30683019089815328 -2.3127667230572574e-016
		1.0221370084631691 0.2824330223887368 -1.7345750422929411e-016
		0.75530261391799591 0.019900135768223783 -1.1563833615286273e-017
		0.52303097518750874 -0.18164105554797427 1.5032983699872164e-016
		3.6056972985635011e-016 -0.41845967235616205 2.3127667230572574e-016
		-0.5230309751875073 -0.18164105554797427 1.5032983699872164e-016
		;
createNode transform -n "c_dn_mouthLip_CTRL_joint1_GRP" -p "c_dn_mouthLip_CTRL";
	setAttr ".v" no;
	setAttr ".s" -type "double3" 3.3333333333333335 6.6666666666666661 5 ;
createNode joint -n "c_dn_mouthLip_CTRL_joint1" -p "c_dn_mouthLip_CTRL_joint1_GRP";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 -1.1429595961046979 0 1;
	setAttr ".radi" 0.2;
createNode transform -n "c_dn_mouthLip_FRAME_lockzy" -p "c_dn_mouthLip_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_dn_mouthLip_FRAME_lockzyShape" -p "c_dn_mouthLip_FRAME_lockzy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 0.20000000000000001 0
		-1 -1 0
		1 -1 0
		1 0.20000000000000001 0
		-1 0.20000000000000001 0
		;
createNode transform -n "c_dn_mouthLip_FRAME_lockfy" -p "c_dn_mouthLip_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_dn_mouthLip_FRAME_lockfyShape" -p "c_dn_mouthLip_FRAME_lockfy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -0.20000000000000001 0
		1 -0.20000000000000001 0
		1 1 0
		-1 1 0
		;
createNode transform -n "c_dn_mouthLip_FRAME_lockzx" -p "c_dn_mouthLip_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_dn_mouthLip_FRAME_lockzxShape" -p "c_dn_mouthLip_FRAME_lockzx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		0.20000000000000001 -1 0
		0.20000000000000001 1 0
		-1 1 0
		;
createNode transform -n "c_dn_mouthLip_FRAME_lockfx" -p "c_dn_mouthLip_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_dn_mouthLip_FRAME_lockfxShape" -p "c_dn_mouthLip_FRAME_lockfx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 1 0
		-0.20000000000000001 -1 0
		1 -1 0
		1 1 0
		-0.20000000000000001 1 0
		;
createNode transform -n "c_dn_mouthLip_FRAME_lockzyfy" -p "c_dn_mouthLip_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_dn_mouthLip_FRAME_lockzyfyShape" -p "c_dn_mouthLip_FRAME_lockzyfy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 0.20000000000000001 0
		-1 -0.20000000000000001 0
		1 -0.20000000000000001 0
		1 0.20000000000000001 0
		-1 0.20000000000000001 0
		;
createNode transform -n "c_dn_mouthLip_FRAME_lockzxfx" -p "c_dn_mouthLip_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_dn_mouthLip_FRAME_lockzxfxShape" -p "c_dn_mouthLip_FRAME_lockzxfx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 1 0
		-0.20000000000000001 -1 0
		0.20000000000000001 -1 0
		0.20000000000000001 1 0
		-0.20000000000000001 1 0
		;
createNode transform -n "c_dn_mouthLip_FRAME_lockzyfyzx" -p "c_dn_mouthLip_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_dn_mouthLip_FRAME_lockzyfyzxShape" -p "c_dn_mouthLip_FRAME_lockzyfyzx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 0.20000000000000001 0
		-1 -0.20000000000000001 0
		0.20000000000000001 -0.20000000000000001 0
		0.20000000000000001 0.20000000000000001 0
		-1 0.20000000000000001 0
		;
createNode transform -n "c_dn_mouthLip_FRAME_lockzyfyfx" -p "c_dn_mouthLip_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_dn_mouthLip_FRAME_lockzyfyfxShape" -p "c_dn_mouthLip_FRAME_lockzyfyfx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 0.20000000000000001 0
		-0.20000000000000001 -0.20000000000000001 0
		1 -0.20000000000000001 0
		1 0.20000000000000001 0
		-0.20000000000000001 0.20000000000000001 0
		;
createNode transform -n "c_dn_mouthLip_FRAME_lockzxfxzy" -p "c_dn_mouthLip_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_dn_mouthLip_FRAME_lockzxfxzyShape" -p "c_dn_mouthLip_FRAME_lockzxfxzy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 0.20000000000000001 0
		-0.20000000000000001 -1 0
		0.20000000000000001 -1 0
		0.20000000000000001 0.20000000000000001 0
		-0.20000000000000001 0.20000000000000001 0
		;
createNode transform -n "c_dn_mouthLip_FRAME_lockzxfxfy" -p "c_dn_mouthLip_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_dn_mouthLip_FRAME_lockzxfxfyShape" -p "c_dn_mouthLip_FRAME_lockzxfxfy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 1 0
		-0.20000000000000001 -0.20000000000000001 0
		0.20000000000000001 -0.20000000000000001 0
		0.20000000000000001 1 0
		-0.20000000000000001 1 0
		;
createNode transform -n "c_dn_mouthLip_CTRL_up" -p "c_dn_mouthLip_FRAME";
	setAttr ".t" -type "double3" 0 2.2 0 ;
createNode nurbsCurve -n "curveShape469" -p "c_dn_mouthLip_CTRL_up";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_dn_mouthLip_LOC_up" -p "c_dn_mouthLip_CTRL_up";
	setAttr -k off ".v" no;
createNode transform -n "c_dn_mouthLip_CTRL_dn" -p "c_dn_mouthLip_FRAME";
	setAttr ".t" -type "double3" 0 -2.2 0 ;
createNode nurbsCurve -n "curveShape470" -p "c_dn_mouthLip_CTRL_dn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_dn_mouthLip_LOC_dn" -p "c_dn_mouthLip_CTRL_dn";
	setAttr -k off ".v" no;
createNode transform -n "c_dn_mouthLip_CTRL_lf" -p "c_dn_mouthLip_FRAME";
	setAttr ".t" -type "double3" -2.2 0 0 ;
createNode nurbsCurve -n "curveShape471" -p "c_dn_mouthLip_CTRL_lf";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_dn_mouthLip_LOC_lf" -p "c_dn_mouthLip_CTRL_lf";
	setAttr -k off ".v" no;
createNode transform -n "c_dn_mouthLip_CTRL_lfup" -p "c_dn_mouthLip_FRAME";
	setAttr ".t" -type "double3" -2.2 2.2 0 ;
createNode nurbsCurve -n "curveShape472" -p "c_dn_mouthLip_CTRL_lfup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_dn_mouthLip_LOC_lfup" -p "c_dn_mouthLip_CTRL_lfup";
	setAttr -k off ".v" no;
createNode transform -n "c_dn_mouthLip_CTRL_rt" -p "c_dn_mouthLip_FRAME";
	setAttr ".t" -type "double3" 2.2 0 0 ;
createNode nurbsCurve -n "curveShape473" -p "c_dn_mouthLip_CTRL_rt";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_dn_mouthLip_LOC_rt" -p "c_dn_mouthLip_CTRL_rt";
	setAttr -k off ".v" no;
createNode transform -n "c_dn_mouthLip_CTRL_rtup" -p "c_dn_mouthLip_FRAME";
	setAttr ".t" -type "double3" 2.2 2.2 0 ;
createNode nurbsCurve -n "curveShape474" -p "c_dn_mouthLip_CTRL_rtup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_dn_mouthLip_LOC_rtup" -p "c_dn_mouthLip_CTRL_rtup";
	setAttr -k off ".v" no;
createNode transform -n "c_dn_mouthLip_CTRL_lfdn" -p "c_dn_mouthLip_FRAME";
	setAttr ".t" -type "double3" -2.2 -2.2 0 ;
createNode nurbsCurve -n "curveShape475" -p "c_dn_mouthLip_CTRL_lfdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_dn_mouthLip_LOC_lfdn" -p "c_dn_mouthLip_CTRL_lfdn";
	setAttr -k off ".v" no;
createNode transform -n "c_dn_mouthLip_CTRL_rtdn" -p "c_dn_mouthLip_FRAME";
	setAttr ".t" -type "double3" 2.2 -2.2 0 ;
createNode nurbsCurve -n "curveShape476" -p "c_dn_mouthLip_CTRL_rtdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_dn_mouthLip_LOC_rtdn" -p "c_dn_mouthLip_CTRL_rtdn";
	setAttr -k off ".v" no;
createNode transform -n "c_dn_mouthLip_CTRL_fourAxisup" -p "c_dn_mouthLip_FRAME";
	setAttr ".t" -type "double3" 0 4.4 0 ;
createNode nurbsCurve -n "curveShape477" -p "c_dn_mouthLip_CTRL_fourAxisup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_dn_mouthLip_LOC_fourAxis_up" -p "c_dn_mouthLip_CTRL_fourAxisup";
	setAttr -k off ".v" no;
createNode transform -n "c_dn_mouthLip_CTRL_fourAxisdn" -p "c_dn_mouthLip_FRAME";
	setAttr ".t" -type "double3" 0 -4.4 0 ;
createNode nurbsCurve -n "curveShape478" -p "c_dn_mouthLip_CTRL_fourAxisdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_dn_mouthLip_LOC_fourAxis_dn" -p "c_dn_mouthLip_CTRL_fourAxisdn";
	setAttr -k off ".v" no;
createNode transform -n "c_dn_mouthLip_CTRL_fourAxislf" -p "c_dn_mouthLip_FRAME";
	setAttr ".t" -type "double3" -4.4 0 0 ;
createNode nurbsCurve -n "curveShape479" -p "c_dn_mouthLip_CTRL_fourAxislf";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_dn_mouthLip_LOC_fourAxis_lf" -p "c_dn_mouthLip_CTRL_fourAxislf";
	setAttr -k off ".v" no;
createNode transform -n "c_dn_mouthLip_CTRL_fourAxisrt" -p "c_dn_mouthLip_FRAME";
	setAttr ".t" -type "double3" 4.4 0 0 ;
createNode nurbsCurve -n "curveShape480" -p "c_dn_mouthLip_CTRL_fourAxisrt";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_dn_mouthLip_LOC_fourAxis_rt" -p "c_dn_mouthLip_CTRL_fourAxisrt";
	setAttr -k off ".v" no;
createNode transform -n "c_jaw_dn_CTRL_joint1_GRP" -p "c_jaw_dn_CTRL";
	setAttr ".v" no;
	setAttr ".s" -type "double3" 2 5 2.5 ;
createNode joint -n "c_jaw_dn_CTRL_joint1" -p "c_jaw_dn_CTRL_joint1_GRP";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 -1.2339426240365641 0 1;
	setAttr ".radi" 0.2;
createNode transform -n "c_jaw_dn_FRAME_lockzy" -p "c_jaw_dn_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_jaw_dn_FRAME_lockzyShape" -p "c_jaw_dn_FRAME_lockzy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 0.20000000000000001 0
		-1 -1 0
		1 -1 0
		1 0.20000000000000001 0
		-1 0.20000000000000001 0
		;
createNode transform -n "c_jaw_dn_FRAME_lockfy" -p "c_jaw_dn_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_jaw_dn_FRAME_lockfyShape" -p "c_jaw_dn_FRAME_lockfy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -0.20000000000000001 0
		1 -0.20000000000000001 0
		1 1 0
		-1 1 0
		;
createNode transform -n "c_jaw_dn_FRAME_lockzx" -p "c_jaw_dn_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_jaw_dn_FRAME_lockzxShape" -p "c_jaw_dn_FRAME_lockzx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		0.20000000000000001 -1 0
		0.20000000000000001 1 0
		-1 1 0
		;
createNode transform -n "c_jaw_dn_FRAME_lockfx" -p "c_jaw_dn_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_jaw_dn_FRAME_lockfxShape" -p "c_jaw_dn_FRAME_lockfx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 1 0
		-0.20000000000000001 -1 0
		1 -1 0
		1 1 0
		-0.20000000000000001 1 0
		;
createNode transform -n "c_jaw_dn_FRAME_lockzyfy" -p "c_jaw_dn_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_jaw_dn_FRAME_lockzyfyShape" -p "c_jaw_dn_FRAME_lockzyfy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 0.20000000000000001 0
		-1 -0.20000000000000001 0
		1 -0.20000000000000001 0
		1 0.20000000000000001 0
		-1 0.20000000000000001 0
		;
createNode transform -n "c_jaw_dn_FRAME_lockzxfx" -p "c_jaw_dn_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_jaw_dn_FRAME_lockzxfxShape" -p "c_jaw_dn_FRAME_lockzxfx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 1 0
		-0.20000000000000001 -1 0
		0.20000000000000001 -1 0
		0.20000000000000001 1 0
		-0.20000000000000001 1 0
		;
createNode transform -n "c_jaw_dn_FRAME_lockzyfyzx" -p "c_jaw_dn_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_jaw_dn_FRAME_lockzyfyzxShape" -p "c_jaw_dn_FRAME_lockzyfyzx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 0.20000000000000001 0
		-1 -0.20000000000000001 0
		0.20000000000000001 -0.20000000000000001 0
		0.20000000000000001 0.20000000000000001 0
		-1 0.20000000000000001 0
		;
createNode transform -n "c_jaw_dn_FRAME_lockzyfyfx" -p "c_jaw_dn_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_jaw_dn_FRAME_lockzyfyfxShape" -p "c_jaw_dn_FRAME_lockzyfyfx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 0.20000000000000001 0
		-0.20000000000000001 -0.20000000000000001 0
		1 -0.20000000000000001 0
		1 0.20000000000000001 0
		-0.20000000000000001 0.20000000000000001 0
		;
createNode transform -n "c_jaw_dn_FRAME_lockzxfxzy" -p "c_jaw_dn_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_jaw_dn_FRAME_lockzxfxzyShape" -p "c_jaw_dn_FRAME_lockzxfxzy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 0.20000000000000001 0
		-0.20000000000000001 -1 0
		0.20000000000000001 -1 0
		0.20000000000000001 0.20000000000000001 0
		-0.20000000000000001 0.20000000000000001 0
		;
createNode transform -n "c_jaw_dn_FRAME_lockzxfxfy" -p "c_jaw_dn_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_jaw_dn_FRAME_lockzxfxfyShape" -p "c_jaw_dn_FRAME_lockzxfxfy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 1 0
		-0.20000000000000001 -0.20000000000000001 0
		0.20000000000000001 -0.20000000000000001 0
		0.20000000000000001 1 0
		-0.20000000000000001 1 0
		;
createNode transform -n "c_jaw_dn_CTRL_up" -p "c_jaw_dn_FRAME";
	setAttr ".t" -type "double3" 0 2.2 0 ;
createNode nurbsCurve -n "curveShape121" -p "c_jaw_dn_CTRL_up";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_jaw_dn_LOC_up" -p "c_jaw_dn_CTRL_up";
	setAttr -k off ".v" no;
createNode transform -n "c_jaw_dn_CTRL_dn" -p "c_jaw_dn_FRAME";
	setAttr ".t" -type "double3" 0 -2.2 0 ;
createNode nurbsCurve -n "curveShape122" -p "c_jaw_dn_CTRL_dn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_jaw_dn_LOC_dn" -p "c_jaw_dn_CTRL_dn";
	setAttr -k off ".v" no;
createNode transform -n "c_jaw_dn_CTRL_lf" -p "c_jaw_dn_FRAME";
	setAttr ".t" -type "double3" -2.2 0 0 ;
createNode nurbsCurve -n "curveShape123" -p "c_jaw_dn_CTRL_lf";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_jaw_dn_LOC_lf" -p "c_jaw_dn_CTRL_lf";
	setAttr -k off ".v" no;
createNode transform -n "c_jaw_dn_CTRL_lfup" -p "c_jaw_dn_FRAME";
	setAttr ".t" -type "double3" -2.2 2.2 0 ;
createNode nurbsCurve -n "curveShape124" -p "c_jaw_dn_CTRL_lfup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_jaw_dn_LOC_lfup" -p "c_jaw_dn_CTRL_lfup";
	setAttr -k off ".v" no;
createNode transform -n "c_jaw_dn_CTRL_rt" -p "c_jaw_dn_FRAME";
	setAttr ".t" -type "double3" 2.2 0 0 ;
createNode nurbsCurve -n "curveShape125" -p "c_jaw_dn_CTRL_rt";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_jaw_dn_LOC_rt" -p "c_jaw_dn_CTRL_rt";
	setAttr -k off ".v" no;
createNode transform -n "c_jaw_dn_CTRL_rtup" -p "c_jaw_dn_FRAME";
	setAttr ".t" -type "double3" 2.2 2.2 0 ;
createNode nurbsCurve -n "curveShape126" -p "c_jaw_dn_CTRL_rtup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_jaw_dn_LOC_rtup" -p "c_jaw_dn_CTRL_rtup";
	setAttr -k off ".v" no;
createNode transform -n "c_jaw_dn_CTRL_lfdn" -p "c_jaw_dn_FRAME";
	setAttr ".t" -type "double3" -2.2 -2.2 0 ;
createNode nurbsCurve -n "curveShape127" -p "c_jaw_dn_CTRL_lfdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_jaw_dn_LOC_lfdn" -p "c_jaw_dn_CTRL_lfdn";
	setAttr -k off ".v" no;
createNode transform -n "c_jaw_dn_CTRL_rtdn" -p "c_jaw_dn_FRAME";
	setAttr ".t" -type "double3" 2.2 -2.2 0 ;
createNode nurbsCurve -n "curveShape128" -p "c_jaw_dn_CTRL_rtdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_jaw_dn_LOC_rtdn" -p "c_jaw_dn_CTRL_rtdn";
	setAttr -k off ".v" no;
createNode transform -n "c_jaw_dn_CTRL_fourAxisup" -p "c_jaw_dn_FRAME";
	setAttr ".t" -type "double3" 0 4.4 0 ;
createNode nurbsCurve -n "curveShape129" -p "c_jaw_dn_CTRL_fourAxisup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_jaw_dn_LOC_fourAxis_up" -p "c_jaw_dn_CTRL_fourAxisup";
	setAttr -k off ".v" no;
createNode transform -n "c_jaw_dn_CTRL_fourAxisdn" -p "c_jaw_dn_FRAME";
	setAttr ".t" -type "double3" 0 -4.4 0 ;
createNode nurbsCurve -n "curveShape130" -p "c_jaw_dn_CTRL_fourAxisdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_jaw_dn_LOC_fourAxis_dn" -p "c_jaw_dn_CTRL_fourAxisdn";
	setAttr -k off ".v" no;
createNode transform -n "c_jaw_dn_CTRL_fourAxislf" -p "c_jaw_dn_FRAME";
	setAttr ".t" -type "double3" -4.4 0 0 ;
createNode nurbsCurve -n "curveShape131" -p "c_jaw_dn_CTRL_fourAxislf";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_jaw_dn_LOC_fourAxis_lf" -p "c_jaw_dn_CTRL_fourAxislf";
	setAttr -k off ".v" no;
createNode transform -n "c_jaw_dn_CTRL_fourAxisrt" -p "c_jaw_dn_FRAME";
	setAttr ".t" -type "double3" 4.4 0 0 ;
createNode nurbsCurve -n "curveShape132" -p "c_jaw_dn_CTRL_fourAxisrt";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_jaw_dn_LOC_fourAxis_rt" -p "c_jaw_dn_CTRL_fourAxisrt";
	setAttr -k off ".v" no;
createNode transform -n "GRP_c_up_mouthLip_FRAME" -p "c_mouth_CTRL";
	setAttr ".t" -type "double3" 0 -0.59815755573530272 0 ;
	setAttr ".s" -type "double3" 0.3 0.15 0.2 ;
createNode transform -n "c_up_mouthLip_FRAME" -p "GRP_c_up_mouthLip_FRAME";
	addAttr -ci true -sn "up" -ln "up" -min 0 -at "double";
	addAttr -ci true -sn "dn" -ln "dn" -min 0 -at "double";
	addAttr -ci true -sn "lf" -ln "lf" -min 0 -at "double";
	addAttr -ci true -sn "rt" -ln "rt" -min 0 -at "double";
	addAttr -ci true -sn "lfup" -ln "lfup" -min 0 -at "double";
	addAttr -ci true -sn "rtup" -ln "rtup" -min 0 -at "double";
	addAttr -ci true -sn "lfdn" -ln "lfdn" -min 0 -at "double";
	addAttr -ci true -sn "rtdn" -ln "rtdn" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_up" -ln "fourAxis_up" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_dn" -ln "fourAxis_dn" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_lf" -ln "fourAxis_lf" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_rt" -ln "fourAxis_rt" -min 0 -at "double";
	addAttr -ci true -sn "up_Vis" -ln "up_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "dn_Vis" -ln "dn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lf_Vis" -ln "lf_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lfup_Vis" -ln "lfup_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rt_Vis" -ln "rt_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rtup_Vis" -ln "rtup_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lfdn_Vis" -ln "lfdn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rtdn_Vis" -ln "rtdn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_up_Vis" -ln "fourAxis_up_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_dn_Vis" -ln "fourAxis_dn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_lf_Vis" -ln "fourAxis_lf_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_rt_Vis" -ln "fourAxis_rt_Vis" -min 0 -max 1 -at "bool";
	setAttr -k on ".up";
	setAttr -k on ".dn";
	setAttr -k on ".lf";
	setAttr -k on ".rt";
	setAttr -k on ".lfup";
	setAttr -k on ".rtup";
	setAttr -k on ".lfdn";
	setAttr -k on ".rtdn";
	setAttr -k on ".fourAxis_up";
	setAttr -k on ".fourAxis_dn";
	setAttr -k on ".fourAxis_lf";
	setAttr -k on ".fourAxis_rt";
	setAttr -cb on ".up_Vis";
	setAttr -cb on ".dn_Vis";
	setAttr -cb on ".lf_Vis";
	setAttr -cb on ".lfup_Vis";
	setAttr -cb on ".rt_Vis";
	setAttr -cb on ".rtup_Vis";
	setAttr -cb on ".lfdn_Vis";
	setAttr -cb on ".rtdn_Vis";
	setAttr -cb on ".fourAxis_up_Vis";
	setAttr -cb on ".fourAxis_dn_Vis";
	setAttr -cb on ".fourAxis_lf_Vis";
	setAttr -cb on ".fourAxis_rt_Vis";
createNode nurbsCurve -n "c_up_mouthLip_FRAMEShape" -p "c_up_mouthLip_FRAME";
	setAttr -k off ".v" no;
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode transform -n "GRP_c_up_mouthLip_CTRL" -p "c_up_mouthLip_FRAME";
	addAttr -ci true -k true -sn "T1" -ln "T1" -at "double";
	addAttr -ci true -k true -sn "T2" -ln "T2" -at "double";
	addAttr -ci true -k true -sn "T3" -ln "T3" -at "double";
	addAttr -ci true -k true -sn "R1" -ln "R1" -at "double";
	addAttr -ci true -k true -sn "R2" -ln "R2" -at "double";
	addAttr -ci true -k true -sn "R3" -ln "R3" -at "double";
	addAttr -ci true -sn "S1" -ln "S1" -at "double";
	addAttr -ci true -sn "S2" -ln "S2" -at "double";
	addAttr -ci true -sn "S3" -ln "S3" -at "double";
	setAttr -k on ".S1" 1;
	setAttr -k on ".S2" 1;
	setAttr -k on ".S3" 1;
createNode transform -n "c_up_mouthLip_CTRL" -p "GRP_c_up_mouthLip_CTRL";
	addAttr -ci true -sn "frameSelectAble" -ln "frameSelectAble" -min 0 -max 2 -en 
		"normal:template:reference" -at "enum";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".mntl" -type "double3" -1 -1 0 ;
	setAttr ".mxtl" -type "double3" 1 1 0 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
	setAttr ".mnrl" -type "double3" -29.999999999999996 -45 -45 ;
	setAttr ".mxrl" -type "double3" 29.999999999999996 45 45 ;
	setAttr ".mrxe" yes;
	setAttr ".xrxe" yes;
	setAttr ".frameSelectAble" 2;
createNode nurbsCurve -n "c_up_mouthLip_CTRLShape" -p "c_up_mouthLip_CTRL";
	setAttr -k off ".v" no;
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		1 32 0 no 3
		33 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32
		33
		-0.050000000000000003 0.050000000000000003 0
		-0.050000000000000003 0.15000000000000002 0
		-0.10000000000000001 0.15000000000000002 0
		0 0.25 0
		0.10000000000000001 0.15000000000000002 0
		0.050000000000000003 0.15000000000000002 0
		0.050000000000000003 0.050000000000000003 0
		0.20000000000000001 0.20000000000000001 0
		0.050000000000000003 0.050000000000000003 0
		0.15000000000000002 0.050000000000000003 0
		0.15000000000000002 0.10000000000000001 0
		0.25 0 0
		0.15000000000000002 -0.10000000000000001 0
		0.15000000000000002 -0.050000000000000003 0
		0.050000000000000003 -0.050000000000000003 0
		0.20000000000000001 -0.20000000000000001 0
		0.050000000000000003 -0.050000000000000003 0
		0.050000000000000003 -0.15000000000000002 0
		0.10000000000000001 -0.15000000000000002 0
		0 -0.25 0
		-0.10000000000000001 -0.15000000000000002 0
		-0.050000000000000003 -0.15000000000000002 0
		-0.050000000000000003 -0.050000000000000003 0
		-0.20000000000000001 -0.20000000000000001 0
		-0.050000000000000003 -0.050000000000000003 0
		-0.15000000000000002 -0.050000000000000003 0
		-0.15000000000000002 -0.10000000000000001 0
		-0.25 0 0
		-0.15000000000000002 0.10000000000000001 0
		-0.15000000000000002 0.050000000000000003 0
		-0.050000000000000003 0.050000000000000003 0
		-0.20000000000000001 0.20000000000000001 0
		-0.050000000000000003 0.050000000000000003 0
		;
createNode nurbsCurve -n "c_up_mouthLip_CTRLShape02" -p "c_up_mouthLip_CTRL";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.51499515693823561 0.22410438497654775 1.853121571098203e-016
		3.5502995696952129e-016 0.43972778149270231 2.2027928732579048e-016
		-0.51499515693823272 0.22410438497654775 1.853121571098203e-016
		-0.74369818738002291 0.040601091210125451 1.0476506029969339e-017
		-1.0064329534157157 -0.19843515295540542 -1.4687557994189641e-016
		5.516895567254797e-017 -0.22064877961313506 -2.1680984037383706e-016
		1.0064329534157157 -0.19843515295540542 -1.4687557994189641e-016
		0.74369818738002325 0.040601091210125451 1.0476506029969339e-017
		0.51499515693823561 0.22410438497654775 1.853121571098203e-016
		3.5502995696952129e-016 0.43972778149270231 2.2027928732579048e-016
		-0.51499515693823272 0.22410438497654775 1.853121571098203e-016
		;
createNode transform -n "c_up_mouthLip_CTRL_joint1_GRP" -p "c_up_mouthLip_CTRL";
	setAttr ".v" no;
	setAttr ".s" -type "double3" 3.3333333333333335 6.666666666666667 5 ;
createNode joint -n "c_up_mouthLip_CTRL_joint1" -p "c_up_mouthLip_CTRL_joint1_GRP";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 -0.59815755573530272 0 1;
	setAttr ".radi" 0.2;
createNode transform -n "c_up_mouthLip_FRAME_lockzy" -p "c_up_mouthLip_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_up_mouthLip_FRAME_lockzyShape" -p "c_up_mouthLip_FRAME_lockzy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 0.20000000000000001 0
		-1 -1 0
		1 -1 0
		1 0.20000000000000001 0
		-1 0.20000000000000001 0
		;
createNode transform -n "c_up_mouthLip_FRAME_lockfy" -p "c_up_mouthLip_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_up_mouthLip_FRAME_lockfyShape" -p "c_up_mouthLip_FRAME_lockfy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -0.20000000000000001 0
		1 -0.20000000000000001 0
		1 1 0
		-1 1 0
		;
createNode transform -n "c_up_mouthLip_FRAME_lockzx" -p "c_up_mouthLip_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_up_mouthLip_FRAME_lockzxShape" -p "c_up_mouthLip_FRAME_lockzx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		0.20000000000000001 -1 0
		0.20000000000000001 1 0
		-1 1 0
		;
createNode transform -n "c_up_mouthLip_FRAME_lockfx" -p "c_up_mouthLip_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_up_mouthLip_FRAME_lockfxShape" -p "c_up_mouthLip_FRAME_lockfx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 1 0
		-0.20000000000000001 -1 0
		1 -1 0
		1 1 0
		-0.20000000000000001 1 0
		;
createNode transform -n "c_up_mouthLip_FRAME_lockzyfy" -p "c_up_mouthLip_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_up_mouthLip_FRAME_lockzyfyShape" -p "c_up_mouthLip_FRAME_lockzyfy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 0.20000000000000001 0
		-1 -0.20000000000000001 0
		1 -0.20000000000000001 0
		1 0.20000000000000001 0
		-1 0.20000000000000001 0
		;
createNode transform -n "c_up_mouthLip_FRAME_lockzxfx" -p "c_up_mouthLip_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_up_mouthLip_FRAME_lockzxfxShape" -p "c_up_mouthLip_FRAME_lockzxfx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 1 0
		-0.20000000000000001 -1 0
		0.20000000000000001 -1 0
		0.20000000000000001 1 0
		-0.20000000000000001 1 0
		;
createNode transform -n "c_up_mouthLip_FRAME_lockzyfyzx" -p "c_up_mouthLip_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_up_mouthLip_FRAME_lockzyfyzxShape" -p "c_up_mouthLip_FRAME_lockzyfyzx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 0.20000000000000001 0
		-1 -0.20000000000000001 0
		0.20000000000000001 -0.20000000000000001 0
		0.20000000000000001 0.20000000000000001 0
		-1 0.20000000000000001 0
		;
createNode transform -n "c_up_mouthLip_FRAME_lockzyfyfx" -p "c_up_mouthLip_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_up_mouthLip_FRAME_lockzyfyfxShape" -p "c_up_mouthLip_FRAME_lockzyfyfx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 0.20000000000000001 0
		-0.20000000000000001 -0.20000000000000001 0
		1 -0.20000000000000001 0
		1 0.20000000000000001 0
		-0.20000000000000001 0.20000000000000001 0
		;
createNode transform -n "c_up_mouthLip_FRAME_lockzxfxzy" -p "c_up_mouthLip_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_up_mouthLip_FRAME_lockzxfxzyShape" -p "c_up_mouthLip_FRAME_lockzxfxzy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 0.20000000000000001 0
		-0.20000000000000001 -1 0
		0.20000000000000001 -1 0
		0.20000000000000001 0.20000000000000001 0
		-0.20000000000000001 0.20000000000000001 0
		;
createNode transform -n "c_up_mouthLip_FRAME_lockzxfxfy" -p "c_up_mouthLip_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_up_mouthLip_FRAME_lockzxfxfyShape" -p "c_up_mouthLip_FRAME_lockzxfxfy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 1 0
		-0.20000000000000001 -0.20000000000000001 0
		0.20000000000000001 -0.20000000000000001 0
		0.20000000000000001 1 0
		-0.20000000000000001 1 0
		;
createNode transform -n "c_up_mouthLip_CTRL_up" -p "c_up_mouthLip_FRAME";
	setAttr ".t" -type "double3" 0 2.2 0 ;
createNode nurbsCurve -n "curveShape457" -p "c_up_mouthLip_CTRL_up";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_up_mouthLip_LOC_up" -p "c_up_mouthLip_CTRL_up";
	setAttr -k off ".v" no;
createNode transform -n "c_up_mouthLip_CTRL_dn" -p "c_up_mouthLip_FRAME";
	setAttr ".t" -type "double3" 0 -2.2 0 ;
createNode nurbsCurve -n "curveShape458" -p "c_up_mouthLip_CTRL_dn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_up_mouthLip_LOC_dn" -p "c_up_mouthLip_CTRL_dn";
	setAttr -k off ".v" no;
createNode transform -n "c_up_mouthLip_CTRL_lf" -p "c_up_mouthLip_FRAME";
	setAttr ".t" -type "double3" -2.2 0 0 ;
createNode nurbsCurve -n "curveShape459" -p "c_up_mouthLip_CTRL_lf";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_up_mouthLip_LOC_lf" -p "c_up_mouthLip_CTRL_lf";
	setAttr -k off ".v" no;
createNode transform -n "c_up_mouthLip_CTRL_lfup" -p "c_up_mouthLip_FRAME";
	setAttr ".t" -type "double3" -2.2 2.2 0 ;
createNode nurbsCurve -n "curveShape460" -p "c_up_mouthLip_CTRL_lfup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_up_mouthLip_LOC_lfup" -p "c_up_mouthLip_CTRL_lfup";
	setAttr -k off ".v" no;
createNode transform -n "c_up_mouthLip_CTRL_rt" -p "c_up_mouthLip_FRAME";
	setAttr ".t" -type "double3" 2.2 0 0 ;
createNode nurbsCurve -n "curveShape461" -p "c_up_mouthLip_CTRL_rt";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_up_mouthLip_LOC_rt" -p "c_up_mouthLip_CTRL_rt";
	setAttr -k off ".v" no;
createNode transform -n "c_up_mouthLip_CTRL_rtup" -p "c_up_mouthLip_FRAME";
	setAttr ".t" -type "double3" 2.2 2.2 0 ;
createNode nurbsCurve -n "curveShape462" -p "c_up_mouthLip_CTRL_rtup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_up_mouthLip_LOC_rtup" -p "c_up_mouthLip_CTRL_rtup";
	setAttr -k off ".v" no;
createNode transform -n "c_up_mouthLip_CTRL_lfdn" -p "c_up_mouthLip_FRAME";
	setAttr ".t" -type "double3" -2.2 -2.2 0 ;
createNode nurbsCurve -n "curveShape463" -p "c_up_mouthLip_CTRL_lfdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_up_mouthLip_LOC_lfdn" -p "c_up_mouthLip_CTRL_lfdn";
	setAttr -k off ".v" no;
createNode transform -n "c_up_mouthLip_CTRL_rtdn" -p "c_up_mouthLip_FRAME";
	setAttr ".t" -type "double3" 2.2 -2.2 0 ;
createNode nurbsCurve -n "curveShape464" -p "c_up_mouthLip_CTRL_rtdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_up_mouthLip_LOC_rtdn" -p "c_up_mouthLip_CTRL_rtdn";
	setAttr -k off ".v" no;
createNode transform -n "c_up_mouthLip_CTRL_fourAxisup" -p "c_up_mouthLip_FRAME";
	setAttr ".t" -type "double3" 0 4.4 0 ;
createNode nurbsCurve -n "curveShape465" -p "c_up_mouthLip_CTRL_fourAxisup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_up_mouthLip_LOC_fourAxis_up" -p "c_up_mouthLip_CTRL_fourAxisup";
	setAttr -k off ".v" no;
createNode transform -n "c_up_mouthLip_CTRL_fourAxisdn" -p "c_up_mouthLip_FRAME";
	setAttr ".t" -type "double3" 0 -4.4 0 ;
createNode nurbsCurve -n "curveShape466" -p "c_up_mouthLip_CTRL_fourAxisdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_up_mouthLip_LOC_fourAxis_dn" -p "c_up_mouthLip_CTRL_fourAxisdn";
	setAttr -k off ".v" no;
createNode transform -n "c_up_mouthLip_CTRL_fourAxislf" -p "c_up_mouthLip_FRAME";
	setAttr ".t" -type "double3" -4.4 0 0 ;
createNode nurbsCurve -n "curveShape467" -p "c_up_mouthLip_CTRL_fourAxislf";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_up_mouthLip_LOC_fourAxis_lf" -p "c_up_mouthLip_CTRL_fourAxislf";
	setAttr -k off ".v" no;
createNode transform -n "c_up_mouthLip_CTRL_fourAxisrt" -p "c_up_mouthLip_FRAME";
	setAttr ".t" -type "double3" 4.4 0 0 ;
createNode nurbsCurve -n "curveShape468" -p "c_up_mouthLip_CTRL_fourAxisrt";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_up_mouthLip_LOC_fourAxis_rt" -p "c_up_mouthLip_CTRL_fourAxisrt";
	setAttr -k off ".v" no;
createNode transform -n "GRP_c_Lf_mouthLip_FRAME" -p "c_mouth_CTRL";
	setAttr ".t" -type "double3" 0.54902891329405423 -0.8433908686503121 1.2838979285600505e-016 ;
	setAttr ".s" -type "double3" 0.2 0.2 0.2 ;
createNode transform -n "c_Lf_mouthLip_FRAME" -p "GRP_c_Lf_mouthLip_FRAME";
	addAttr -ci true -sn "up" -ln "up" -min 0 -at "double";
	addAttr -ci true -sn "dn" -ln "dn" -min 0 -at "double";
	addAttr -ci true -sn "lf" -ln "lf" -min 0 -at "double";
	addAttr -ci true -sn "rt" -ln "rt" -min 0 -at "double";
	addAttr -ci true -sn "lfup" -ln "lfup" -min 0 -at "double";
	addAttr -ci true -sn "rtup" -ln "rtup" -min 0 -at "double";
	addAttr -ci true -sn "lfdn" -ln "lfdn" -min 0 -at "double";
	addAttr -ci true -sn "rtdn" -ln "rtdn" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_up" -ln "fourAxis_up" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_dn" -ln "fourAxis_dn" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_lf" -ln "fourAxis_lf" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_rt" -ln "fourAxis_rt" -min 0 -at "double";
	addAttr -ci true -sn "up_Vis" -ln "up_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "dn_Vis" -ln "dn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lf_Vis" -ln "lf_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lfup_Vis" -ln "lfup_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rt_Vis" -ln "rt_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rtup_Vis" -ln "rtup_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lfdn_Vis" -ln "lfdn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rtdn_Vis" -ln "rtdn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_up_Vis" -ln "fourAxis_up_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_dn_Vis" -ln "fourAxis_dn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_lf_Vis" -ln "fourAxis_lf_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_rt_Vis" -ln "fourAxis_rt_Vis" -min 0 -max 1 -at "bool";
	setAttr -k on ".up";
	setAttr -k on ".dn";
	setAttr -k on ".lf";
	setAttr -k on ".rt";
	setAttr -k on ".lfup";
	setAttr -k on ".rtup";
	setAttr -k on ".lfdn";
	setAttr -k on ".rtdn";
	setAttr -k on ".fourAxis_up";
	setAttr -k on ".fourAxis_dn";
	setAttr -k on ".fourAxis_lf";
	setAttr -k on ".fourAxis_rt";
	setAttr -cb on ".up_Vis";
	setAttr -cb on ".dn_Vis";
	setAttr -cb on ".lf_Vis";
	setAttr -cb on ".lfup_Vis";
	setAttr -cb on ".rt_Vis";
	setAttr -cb on ".rtup_Vis";
	setAttr -cb on ".lfdn_Vis";
	setAttr -cb on ".rtdn_Vis";
	setAttr -cb on ".fourAxis_up_Vis";
	setAttr -cb on ".fourAxis_dn_Vis";
	setAttr -cb on ".fourAxis_lf_Vis";
	setAttr -cb on ".fourAxis_rt_Vis";
createNode nurbsCurve -n "c_Lf_mouthLip_FRAMEShape" -p "c_Lf_mouthLip_FRAME";
	setAttr -k off ".v" no;
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode transform -n "GRP_c_Lf_mouthLip_CTRL" -p "c_Lf_mouthLip_FRAME";
	addAttr -ci true -k true -sn "T1" -ln "T1" -at "double";
	addAttr -ci true -k true -sn "T2" -ln "T2" -at "double";
	addAttr -ci true -k true -sn "T3" -ln "T3" -at "double";
	addAttr -ci true -k true -sn "R1" -ln "R1" -at "double";
	addAttr -ci true -k true -sn "R2" -ln "R2" -at "double";
	addAttr -ci true -k true -sn "R3" -ln "R3" -at "double";
	addAttr -ci true -sn "S1" -ln "S1" -at "double";
	addAttr -ci true -sn "S2" -ln "S2" -at "double";
	addAttr -ci true -sn "S3" -ln "S3" -at "double";
	setAttr -k on ".S1" 1;
	setAttr -k on ".S2" 1;
	setAttr -k on ".S3" 1;
createNode transform -n "c_Lf_mouthLip_CTRL" -p "GRP_c_Lf_mouthLip_CTRL";
	addAttr -ci true -sn "frameSelectAble" -ln "frameSelectAble" -min 0 -max 2 -en 
		"normal:template:reference" -at "enum";
	addAttr -ci true -sn "follow" -ln "follow" -min 0 -max 1 -at "double";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".mntl" -type "double3" -1 -1 0 ;
	setAttr ".mxtl" -type "double3" 1 1 0 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
	setAttr ".frameSelectAble" 2;
	setAttr -k on ".follow" 1;
createNode nurbsCurve -n "c_Lf_mouthLip_CTRLShape" -p "c_Lf_mouthLip_CTRL";
	setAttr -k off ".v" no;
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		1 32 0 no 3
		33 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32
		33
		-0.050000000000000003 0.050000000000000003 0
		-0.050000000000000003 0.15000000000000002 0
		-0.10000000000000001 0.15000000000000002 0
		0 0.25 0
		0.10000000000000001 0.15000000000000002 0
		0.050000000000000003 0.15000000000000002 0
		0.050000000000000003 0.050000000000000003 0
		0.20000000000000001 0.20000000000000001 0
		0.050000000000000003 0.050000000000000003 0
		0.15000000000000002 0.050000000000000003 0
		0.15000000000000002 0.10000000000000001 0
		0.25 0 0
		0.15000000000000002 -0.10000000000000001 0
		0.15000000000000002 -0.050000000000000003 0
		0.050000000000000003 -0.050000000000000003 0
		0.20000000000000001 -0.20000000000000001 0
		0.050000000000000003 -0.050000000000000003 0
		0.050000000000000003 -0.15000000000000002 0
		0.10000000000000001 -0.15000000000000002 0
		0 -0.25 0
		-0.10000000000000001 -0.15000000000000002 0
		-0.050000000000000003 -0.15000000000000002 0
		-0.050000000000000003 -0.050000000000000003 0
		-0.20000000000000001 -0.20000000000000001 0
		-0.050000000000000003 -0.050000000000000003 0
		-0.15000000000000002 -0.050000000000000003 0
		-0.15000000000000002 -0.10000000000000001 0
		-0.25 0 0
		-0.15000000000000002 0.10000000000000001 0
		-0.15000000000000002 0.050000000000000003 0
		-0.050000000000000003 0.050000000000000003 0
		-0.20000000000000001 0.20000000000000001 0
		-0.050000000000000003 0.050000000000000003 0
		;
createNode nurbsCurve -n "c_mouthLip_CTRLShape" -p "c_Lf_mouthLip_CTRL";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.068936848867637873 0.42313489882949978 -6.7725824960552165e-017
		-0.32416933414180582 0.59840311263804724 -1.0158873744082823e-016
		-0.35183559156448485 0.38109354808946022 -5.0794368720414115e-017
		-0.35751727485968876 2.175049656820307e-016 0
		-0.35183559156448485 -0.38109354808946022 6.7725824960552165e-017
		-0.32416933414180582 -0.59840311263804769 1.0158873744082823e-016
		0.068936848867637388 -0.42313489882949995 6.7725824960552165e-017
		0.73032412143788772 -3.2430163400238743e-016 0
		0.068936848867637873 0.42313489882949978 -6.7725824960552165e-017
		-0.32416933414180582 0.59840311263804724 -1.0158873744082823e-016
		-0.35183559156448485 0.38109354808946022 -5.0794368720414115e-017
		;
createNode transform -n "c_Lf_mouthLip_CTRL_joint1_GRP" -p "c_Lf_mouthLip_CTRL";
	setAttr ".v" no;
	setAttr ".s" -type "double3" 5 5 5 ;
createNode joint -n "c_Lf_mouthLip_CTRL_joint1" -p "c_Lf_mouthLip_CTRL_joint1_GRP";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0.54902891329405423 -0.8433908686503121 1.2838979285600505e-016 1;
	setAttr ".radi" 0.2;
createNode transform -n "c_Lf_mouthLip_FRAME_lockzy" -p "c_Lf_mouthLip_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Lf_mouthLip_FRAME_lockzyShape" -p "c_Lf_mouthLip_FRAME_lockzy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 0.20000000000000001 0
		-1 -1 0
		1 -1 0
		1 0.20000000000000001 0
		-1 0.20000000000000001 0
		;
createNode transform -n "c_Lf_mouthLip_FRAME_lockfy" -p "c_Lf_mouthLip_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Lf_mouthLip_FRAME_lockfyShape" -p "c_Lf_mouthLip_FRAME_lockfy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -0.20000000000000001 0
		1 -0.20000000000000001 0
		1 1 0
		-1 1 0
		;
createNode transform -n "c_Lf_mouthLip_FRAME_lockzx" -p "c_Lf_mouthLip_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Lf_mouthLip_FRAME_lockzxShape" -p "c_Lf_mouthLip_FRAME_lockzx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		0.20000000000000001 -1 0
		0.20000000000000001 1 0
		-1 1 0
		;
createNode transform -n "c_Lf_mouthLip_FRAME_lockfx" -p "c_Lf_mouthLip_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Lf_mouthLip_FRAME_lockfxShape" -p "c_Lf_mouthLip_FRAME_lockfx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 1 0
		-0.20000000000000001 -1 0
		1 -1 0
		1 1 0
		-0.20000000000000001 1 0
		;
createNode transform -n "c_Lf_mouthLip_FRAME_lockzyfy" -p "c_Lf_mouthLip_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Lf_mouthLip_FRAME_lockzyfyShape" -p "c_Lf_mouthLip_FRAME_lockzyfy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 0.20000000000000001 0
		-1 -0.20000000000000001 0
		1 -0.20000000000000001 0
		1 0.20000000000000001 0
		-1 0.20000000000000001 0
		;
createNode transform -n "c_Lf_mouthLip_FRAME_lockzxfx" -p "c_Lf_mouthLip_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Lf_mouthLip_FRAME_lockzxfxShape" -p "c_Lf_mouthLip_FRAME_lockzxfx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 1 0
		-0.20000000000000001 -1 0
		0.20000000000000001 -1 0
		0.20000000000000001 1 0
		-0.20000000000000001 1 0
		;
createNode transform -n "c_Lf_mouthLip_FRAME_lockzyfyzx" -p "c_Lf_mouthLip_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Lf_mouthLip_FRAME_lockzyfyzxShape" -p "c_Lf_mouthLip_FRAME_lockzyfyzx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 0.20000000000000001 0
		-1 -0.20000000000000001 0
		0.20000000000000001 -0.20000000000000001 0
		0.20000000000000001 0.20000000000000001 0
		-1 0.20000000000000001 0
		;
createNode transform -n "c_Lf_mouthLip_FRAME_lockzyfyfx" -p "c_Lf_mouthLip_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Lf_mouthLip_FRAME_lockzyfyfxShape" -p "c_Lf_mouthLip_FRAME_lockzyfyfx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 0.20000000000000001 0
		-0.20000000000000001 -0.20000000000000001 0
		1 -0.20000000000000001 0
		1 0.20000000000000001 0
		-0.20000000000000001 0.20000000000000001 0
		;
createNode transform -n "c_Lf_mouthLip_FRAME_lockzxfxzy" -p "c_Lf_mouthLip_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Lf_mouthLip_FRAME_lockzxfxzyShape" -p "c_Lf_mouthLip_FRAME_lockzxfxzy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 0.20000000000000001 0
		-0.20000000000000001 -1 0
		0.20000000000000001 -1 0
		0.20000000000000001 0.20000000000000001 0
		-0.20000000000000001 0.20000000000000001 0
		;
createNode transform -n "c_Lf_mouthLip_FRAME_lockzxfxfy" -p "c_Lf_mouthLip_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Lf_mouthLip_FRAME_lockzxfxfyShape" -p "c_Lf_mouthLip_FRAME_lockzxfxfy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 1 0
		-0.20000000000000001 -0.20000000000000001 0
		0.20000000000000001 -0.20000000000000001 0
		0.20000000000000001 1 0
		-0.20000000000000001 1 0
		;
createNode transform -n "c_Lf_mouthLip_CTRL_up" -p "c_Lf_mouthLip_FRAME";
	setAttr ".t" -type "double3" 0 2.2 0 ;
createNode nurbsCurve -n "curveShape505" -p "c_Lf_mouthLip_CTRL_up";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_mouthLip_LOC_up" -p "c_Lf_mouthLip_CTRL_up";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_mouthLip_CTRL_dn" -p "c_Lf_mouthLip_FRAME";
	setAttr ".t" -type "double3" 0 -2.2 0 ;
createNode nurbsCurve -n "curveShape506" -p "c_Lf_mouthLip_CTRL_dn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_mouthLip_LOC_dn" -p "c_Lf_mouthLip_CTRL_dn";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_mouthLip_CTRL_lf" -p "c_Lf_mouthLip_FRAME";
	setAttr ".t" -type "double3" -2.2 0 0 ;
createNode nurbsCurve -n "curveShape507" -p "c_Lf_mouthLip_CTRL_lf";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_mouthLip_LOC_lf" -p "c_Lf_mouthLip_CTRL_lf";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_mouthLip_CTRL_lfup" -p "c_Lf_mouthLip_FRAME";
	setAttr ".t" -type "double3" -2.2 2.2 0 ;
createNode nurbsCurve -n "curveShape508" -p "c_Lf_mouthLip_CTRL_lfup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_mouthLip_LOC_lfup" -p "c_Lf_mouthLip_CTRL_lfup";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_mouthLip_CTRL_rt" -p "c_Lf_mouthLip_FRAME";
	setAttr ".t" -type "double3" 2.2 0 0 ;
createNode nurbsCurve -n "curveShape509" -p "c_Lf_mouthLip_CTRL_rt";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_mouthLip_LOC_rt" -p "c_Lf_mouthLip_CTRL_rt";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_mouthLip_CTRL_rtup" -p "c_Lf_mouthLip_FRAME";
	setAttr ".t" -type "double3" 2.2 2.2 0 ;
createNode nurbsCurve -n "curveShape510" -p "c_Lf_mouthLip_CTRL_rtup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_mouthLip_LOC_rtup" -p "c_Lf_mouthLip_CTRL_rtup";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_mouthLip_CTRL_lfdn" -p "c_Lf_mouthLip_FRAME";
	setAttr ".t" -type "double3" -2.2 -2.2 0 ;
createNode nurbsCurve -n "curveShape511" -p "c_Lf_mouthLip_CTRL_lfdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_mouthLip_LOC_lfdn" -p "c_Lf_mouthLip_CTRL_lfdn";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_mouthLip_CTRL_rtdn" -p "c_Lf_mouthLip_FRAME";
	setAttr ".t" -type "double3" 2.2 -2.2 0 ;
createNode nurbsCurve -n "curveShape512" -p "c_Lf_mouthLip_CTRL_rtdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_mouthLip_LOC_rtdn" -p "c_Lf_mouthLip_CTRL_rtdn";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_mouthLip_CTRL_fourAxisup" -p "c_Lf_mouthLip_FRAME";
	setAttr ".t" -type "double3" 0 4.4 0 ;
createNode nurbsCurve -n "curveShape513" -p "c_Lf_mouthLip_CTRL_fourAxisup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_mouthLip_LOC_fourAxis_up" -p "c_Lf_mouthLip_CTRL_fourAxisup";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_mouthLip_CTRL_fourAxisdn" -p "c_Lf_mouthLip_FRAME";
	setAttr ".t" -type "double3" 0 -4.4 0 ;
createNode nurbsCurve -n "curveShape514" -p "c_Lf_mouthLip_CTRL_fourAxisdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_mouthLip_LOC_fourAxis_dn" -p "c_Lf_mouthLip_CTRL_fourAxisdn";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_mouthLip_CTRL_fourAxislf" -p "c_Lf_mouthLip_FRAME";
	setAttr ".t" -type "double3" -4.4 0 0 ;
createNode nurbsCurve -n "curveShape515" -p "c_Lf_mouthLip_CTRL_fourAxislf";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_mouthLip_LOC_fourAxis_lf" -p "c_Lf_mouthLip_CTRL_fourAxislf";
	setAttr -k off ".v" no;
createNode transform -n "c_Lf_mouthLip_CTRL_fourAxisrt" -p "c_Lf_mouthLip_FRAME";
	setAttr ".t" -type "double3" 4.4 0 0 ;
createNode nurbsCurve -n "curveShape516" -p "c_Lf_mouthLip_CTRL_fourAxisrt";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Lf_mouthLip_LOC_fourAxis_rt" -p "c_Lf_mouthLip_CTRL_fourAxisrt";
	setAttr -k off ".v" no;
createNode transform -n "GRP_c_Rt_mouthLip_FRAME" -p "c_mouth_CTRL";
	setAttr ".t" -type "double3" -0.54902891329405423 -0.8433908686503121 -6.1153142725513633e-017 ;
	setAttr ".r" -type "double3" 0 -180 0 ;
	setAttr ".s" -type "double3" 0.2 0.2 0.2 ;
createNode transform -n "c_Rt_mouthLip_FRAME" -p "GRP_c_Rt_mouthLip_FRAME";
	addAttr -ci true -sn "up" -ln "up" -min 0 -at "double";
	addAttr -ci true -sn "dn" -ln "dn" -min 0 -at "double";
	addAttr -ci true -sn "lf" -ln "lf" -min 0 -at "double";
	addAttr -ci true -sn "rt" -ln "rt" -min 0 -at "double";
	addAttr -ci true -sn "lfup" -ln "lfup" -min 0 -at "double";
	addAttr -ci true -sn "rtup" -ln "rtup" -min 0 -at "double";
	addAttr -ci true -sn "lfdn" -ln "lfdn" -min 0 -at "double";
	addAttr -ci true -sn "rtdn" -ln "rtdn" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_up" -ln "fourAxis_up" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_dn" -ln "fourAxis_dn" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_lf" -ln "fourAxis_lf" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_rt" -ln "fourAxis_rt" -min 0 -at "double";
	addAttr -ci true -sn "up_Vis" -ln "up_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "dn_Vis" -ln "dn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lf_Vis" -ln "lf_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lfup_Vis" -ln "lfup_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rt_Vis" -ln "rt_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rtup_Vis" -ln "rtup_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lfdn_Vis" -ln "lfdn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rtdn_Vis" -ln "rtdn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_up_Vis" -ln "fourAxis_up_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_dn_Vis" -ln "fourAxis_dn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_lf_Vis" -ln "fourAxis_lf_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_rt_Vis" -ln "fourAxis_rt_Vis" -min 0 -max 1 -at "bool";
	setAttr -k on ".up";
	setAttr -k on ".dn";
	setAttr -k on ".lf";
	setAttr -k on ".rt";
	setAttr -k on ".lfup";
	setAttr -k on ".rtup";
	setAttr -k on ".lfdn";
	setAttr -k on ".rtdn";
	setAttr -k on ".fourAxis_up";
	setAttr -k on ".fourAxis_dn";
	setAttr -k on ".fourAxis_lf";
	setAttr -k on ".fourAxis_rt";
	setAttr -cb on ".up_Vis";
	setAttr -cb on ".dn_Vis";
	setAttr -cb on ".lf_Vis";
	setAttr -cb on ".lfup_Vis";
	setAttr -cb on ".rt_Vis";
	setAttr -cb on ".rtup_Vis";
	setAttr -cb on ".lfdn_Vis";
	setAttr -cb on ".rtdn_Vis";
	setAttr -cb on ".fourAxis_up_Vis";
	setAttr -cb on ".fourAxis_dn_Vis";
	setAttr -cb on ".fourAxis_lf_Vis";
	setAttr -cb on ".fourAxis_rt_Vis";
createNode nurbsCurve -n "c_Rt_mouthLip_FRAMEShape" -p "c_Rt_mouthLip_FRAME";
	setAttr -k off ".v" no;
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode transform -n "GRP_c_Rt_mouthLip_CTRL" -p "c_Rt_mouthLip_FRAME";
	addAttr -ci true -k true -sn "T1" -ln "T1" -at "double";
	addAttr -ci true -k true -sn "T2" -ln "T2" -at "double";
	addAttr -ci true -k true -sn "T3" -ln "T3" -at "double";
	addAttr -ci true -k true -sn "R1" -ln "R1" -at "double";
	addAttr -ci true -k true -sn "R2" -ln "R2" -at "double";
	addAttr -ci true -k true -sn "R3" -ln "R3" -at "double";
	addAttr -ci true -sn "S1" -ln "S1" -at "double";
	addAttr -ci true -sn "S2" -ln "S2" -at "double";
	addAttr -ci true -sn "S3" -ln "S3" -at "double";
	setAttr -k on ".S1" 1;
	setAttr -k on ".S2" 1;
	setAttr -k on ".S3" 1;
createNode transform -n "c_Rt_mouthLip_CTRL" -p "GRP_c_Rt_mouthLip_CTRL";
	addAttr -ci true -sn "frameSelectAble" -ln "frameSelectAble" -min 0 -max 2 -en 
		"normal:template:reference" -at "enum";
	addAttr -ci true -sn "follow" -ln "follow" -min 0 -max 1 -at "double";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".mntl" -type "double3" -1 -1 0 ;
	setAttr ".mxtl" -type "double3" 1 1 0 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
	setAttr ".frameSelectAble" 2;
	setAttr -k on ".follow" 1;
createNode nurbsCurve -n "c_Rt_mouthLip_CTRLShape" -p "c_Rt_mouthLip_CTRL";
	setAttr -k off ".v" no;
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		1 32 0 no 3
		33 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32
		33
		-0.050000000000000003 0.050000000000000003 0
		-0.050000000000000003 0.15000000000000002 0
		-0.10000000000000001 0.15000000000000002 0
		0 0.25 0
		0.10000000000000001 0.15000000000000002 0
		0.050000000000000003 0.15000000000000002 0
		0.050000000000000003 0.050000000000000003 0
		0.20000000000000001 0.20000000000000001 0
		0.050000000000000003 0.050000000000000003 0
		0.15000000000000002 0.050000000000000003 0
		0.15000000000000002 0.10000000000000001 0
		0.25 0 0
		0.15000000000000002 -0.10000000000000001 0
		0.15000000000000002 -0.050000000000000003 0
		0.050000000000000003 -0.050000000000000003 0
		0.20000000000000001 -0.20000000000000001 0
		0.050000000000000003 -0.050000000000000003 0
		0.050000000000000003 -0.15000000000000002 0
		0.10000000000000001 -0.15000000000000002 0
		0 -0.25 0
		-0.10000000000000001 -0.15000000000000002 0
		-0.050000000000000003 -0.15000000000000002 0
		-0.050000000000000003 -0.050000000000000003 0
		-0.20000000000000001 -0.20000000000000001 0
		-0.050000000000000003 -0.050000000000000003 0
		-0.15000000000000002 -0.050000000000000003 0
		-0.15000000000000002 -0.10000000000000001 0
		-0.25 0 0
		-0.15000000000000002 0.10000000000000001 0
		-0.15000000000000002 0.050000000000000003 0
		-0.050000000000000003 0.050000000000000003 0
		-0.20000000000000001 0.20000000000000001 0
		-0.050000000000000003 0.050000000000000003 0
		;
createNode transform -n "c_Rt_mouthLip_CTRL_joint1_GRP" -p "c_Rt_mouthLip_CTRL";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 0 -6.4194896428002469e-016 ;
	setAttr ".r" -type "double3" 0 180 0 ;
	setAttr ".s" -type "double3" 5 5 5 ;
createNode joint -n "c_Rt_mouthLip_CTRL_joint1" -p "c_Rt_mouthLip_CTRL_joint1_GRP";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 -0.54902891329405423 -0.8433908686503121 6.7236650130491321e-017 1;
	setAttr ".radi" 0.2;
createNode transform -n "c_Rt_mouthLip_FRAME_lockzy" -p "c_Rt_mouthLip_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Rt_mouthLip_FRAME_lockzyShape" -p "c_Rt_mouthLip_FRAME_lockzy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 0.20000000000000001 0
		-1 -1 0
		1 -1 0
		1 0.20000000000000001 0
		-1 0.20000000000000001 0
		;
createNode transform -n "c_Rt_mouthLip_FRAME_lockfy" -p "c_Rt_mouthLip_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Rt_mouthLip_FRAME_lockfyShape" -p "c_Rt_mouthLip_FRAME_lockfy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -0.20000000000000001 0
		1 -0.20000000000000001 0
		1 1 0
		-1 1 0
		;
createNode transform -n "c_Rt_mouthLip_FRAME_lockzx" -p "c_Rt_mouthLip_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Rt_mouthLip_FRAME_lockzxShape" -p "c_Rt_mouthLip_FRAME_lockzx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		0.20000000000000001 -1 0
		0.20000000000000001 1 0
		-1 1 0
		;
createNode transform -n "c_Rt_mouthLip_FRAME_lockfx" -p "c_Rt_mouthLip_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Rt_mouthLip_FRAME_lockfxShape" -p "c_Rt_mouthLip_FRAME_lockfx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 1 0
		-0.20000000000000001 -1 0
		1 -1 0
		1 1 0
		-0.20000000000000001 1 0
		;
createNode transform -n "c_Rt_mouthLip_FRAME_lockzyfy" -p "c_Rt_mouthLip_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Rt_mouthLip_FRAME_lockzyfyShape" -p "c_Rt_mouthLip_FRAME_lockzyfy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 0.20000000000000001 0
		-1 -0.20000000000000001 0
		1 -0.20000000000000001 0
		1 0.20000000000000001 0
		-1 0.20000000000000001 0
		;
createNode transform -n "c_Rt_mouthLip_FRAME_lockzxfx" -p "c_Rt_mouthLip_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Rt_mouthLip_FRAME_lockzxfxShape" -p "c_Rt_mouthLip_FRAME_lockzxfx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 1 0
		-0.20000000000000001 -1 0
		0.20000000000000001 -1 0
		0.20000000000000001 1 0
		-0.20000000000000001 1 0
		;
createNode transform -n "c_Rt_mouthLip_FRAME_lockzyfyzx" -p "c_Rt_mouthLip_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Rt_mouthLip_FRAME_lockzyfyzxShape" -p "c_Rt_mouthLip_FRAME_lockzyfyzx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 0.20000000000000001 0
		-1 -0.20000000000000001 0
		0.20000000000000001 -0.20000000000000001 0
		0.20000000000000001 0.20000000000000001 0
		-1 0.20000000000000001 0
		;
createNode transform -n "c_Rt_mouthLip_FRAME_lockzyfyfx" -p "c_Rt_mouthLip_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Rt_mouthLip_FRAME_lockzyfyfxShape" -p "c_Rt_mouthLip_FRAME_lockzyfyfx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 0.20000000000000001 0
		-0.20000000000000001 -0.20000000000000001 0
		1 -0.20000000000000001 0
		1 0.20000000000000001 0
		-0.20000000000000001 0.20000000000000001 0
		;
createNode transform -n "c_Rt_mouthLip_FRAME_lockzxfxzy" -p "c_Rt_mouthLip_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Rt_mouthLip_FRAME_lockzxfxzyShape" -p "c_Rt_mouthLip_FRAME_lockzxfxzy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 0.20000000000000001 0
		-0.20000000000000001 -1 0
		0.20000000000000001 -1 0
		0.20000000000000001 0.20000000000000001 0
		-0.20000000000000001 0.20000000000000001 0
		;
createNode transform -n "c_Rt_mouthLip_FRAME_lockzxfxfy" -p "c_Rt_mouthLip_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_Rt_mouthLip_FRAME_lockzxfxfyShape" -p "c_Rt_mouthLip_FRAME_lockzxfxfy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 1 0
		-0.20000000000000001 -0.20000000000000001 0
		0.20000000000000001 -0.20000000000000001 0
		0.20000000000000001 1 0
		-0.20000000000000001 1 0
		;
createNode transform -n "c_Rt_mouthLip_CTRL_up" -p "c_Rt_mouthLip_FRAME";
	setAttr ".t" -type "double3" 0 2.2 0 ;
createNode nurbsCurve -n "curveShape517" -p "c_Rt_mouthLip_CTRL_up";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_mouthLip_LOC_up" -p "c_Rt_mouthLip_CTRL_up";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_mouthLip_CTRL_dn" -p "c_Rt_mouthLip_FRAME";
	setAttr ".t" -type "double3" 0 -2.2 0 ;
createNode nurbsCurve -n "curveShape518" -p "c_Rt_mouthLip_CTRL_dn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_mouthLip_LOC_dn" -p "c_Rt_mouthLip_CTRL_dn";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_mouthLip_CTRL_lf" -p "c_Rt_mouthLip_FRAME";
	setAttr ".t" -type "double3" -2.2 0 0 ;
createNode nurbsCurve -n "curveShape519" -p "c_Rt_mouthLip_CTRL_lf";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_mouthLip_LOC_lf" -p "c_Rt_mouthLip_CTRL_lf";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_mouthLip_CTRL_lfup" -p "c_Rt_mouthLip_FRAME";
	setAttr ".t" -type "double3" -2.2 2.2 0 ;
createNode nurbsCurve -n "curveShape520" -p "c_Rt_mouthLip_CTRL_lfup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_mouthLip_LOC_lfup" -p "c_Rt_mouthLip_CTRL_lfup";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_mouthLip_CTRL_rt" -p "c_Rt_mouthLip_FRAME";
	setAttr ".t" -type "double3" 2.2 0 0 ;
createNode nurbsCurve -n "curveShape521" -p "c_Rt_mouthLip_CTRL_rt";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_mouthLip_LOC_rt" -p "c_Rt_mouthLip_CTRL_rt";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_mouthLip_CTRL_rtup" -p "c_Rt_mouthLip_FRAME";
	setAttr ".t" -type "double3" 2.2 2.2 0 ;
createNode nurbsCurve -n "curveShape522" -p "c_Rt_mouthLip_CTRL_rtup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_mouthLip_LOC_rtup" -p "c_Rt_mouthLip_CTRL_rtup";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_mouthLip_CTRL_lfdn" -p "c_Rt_mouthLip_FRAME";
	setAttr ".t" -type "double3" -2.2 -2.2 0 ;
createNode nurbsCurve -n "curveShape523" -p "c_Rt_mouthLip_CTRL_lfdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_mouthLip_LOC_lfdn" -p "c_Rt_mouthLip_CTRL_lfdn";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_mouthLip_CTRL_rtdn" -p "c_Rt_mouthLip_FRAME";
	setAttr ".t" -type "double3" 2.2 -2.2 0 ;
createNode nurbsCurve -n "curveShape524" -p "c_Rt_mouthLip_CTRL_rtdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_mouthLip_LOC_rtdn" -p "c_Rt_mouthLip_CTRL_rtdn";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_mouthLip_CTRL_fourAxisup" -p "c_Rt_mouthLip_FRAME";
	setAttr ".t" -type "double3" 0 4.4 0 ;
createNode nurbsCurve -n "curveShape525" -p "c_Rt_mouthLip_CTRL_fourAxisup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_mouthLip_LOC_fourAxis_up" -p "c_Rt_mouthLip_CTRL_fourAxisup";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_mouthLip_CTRL_fourAxisdn" -p "c_Rt_mouthLip_FRAME";
	setAttr ".t" -type "double3" 0 -4.4 0 ;
createNode nurbsCurve -n "curveShape526" -p "c_Rt_mouthLip_CTRL_fourAxisdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_mouthLip_LOC_fourAxis_dn" -p "c_Rt_mouthLip_CTRL_fourAxisdn";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_mouthLip_CTRL_fourAxislf" -p "c_Rt_mouthLip_FRAME";
	setAttr ".t" -type "double3" -4.4 0 0 ;
createNode nurbsCurve -n "curveShape527" -p "c_Rt_mouthLip_CTRL_fourAxislf";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_mouthLip_LOC_fourAxis_lf" -p "c_Rt_mouthLip_CTRL_fourAxislf";
	setAttr -k off ".v" no;
createNode transform -n "c_Rt_mouthLip_CTRL_fourAxisrt" -p "c_Rt_mouthLip_FRAME";
	setAttr ".t" -type "double3" 4.4 0 0 ;
createNode nurbsCurve -n "curveShape528" -p "c_Rt_mouthLip_CTRL_fourAxisrt";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_Rt_mouthLip_LOC_fourAxis_rt" -p "c_Rt_mouthLip_CTRL_fourAxisrt";
	setAttr -k off ".v" no;
createNode transform -n "c_muothLip_01_second_CTRL_GRP" -p "c_mouth_CTRL";
	setAttr ".rp" -type "double3" -6.1629758220391547e-033 -0.74241041020009801 0.017959868467468724 ;
	setAttr ".sp" -type "double3" -6.1629758220391547e-033 -0.74241041020009801 0.017959868467468724 ;
createNode transform -n "c_muothLip_01_second_CTRL" -p "c_muothLip_01_second_CTRL_GRP";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".rp" -type "double3" -6.1629758220391547e-033 -0.74241041020009801 0.017959868467468724 ;
	setAttr ".sp" -type "double3" -6.1629758220391547e-033 -0.74241041020009801 0.017959868467468724 ;
createNode nurbsCurve -n "c_muothLip_01_second_CTRLShape" -p "c_muothLip_01_second_CTRL";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.054293777706352721 -0.68811663249374533 0.017959868467468713
		-8.7600218358203329e-018 -0.66562741341530407 0.01795986846746871
		-0.054293777706352665 -0.68811663249374533 0.017959868467468713
		-0.076782996784793944 -0.74241041020009801 0.017959868467468724
		-0.054293777706352679 -0.7967041879064507 0.017959868467468731
		-2.3136215437310647e-017 -0.81919340698489196 0.017959868467468734
		0.054293777706352638 -0.7967041879064507 0.017959868467468731
		0.076782996784793944 -0.74241041020009801 0.017959868467468724
		0.054293777706352721 -0.68811663249374533 0.017959868467468713
		-8.7600218358203329e-018 -0.66562741341530407 0.01795986846746871
		-0.054293777706352665 -0.68811663249374533 0.017959868467468713
		;
createNode transform -n "c_muothLip_07_second_CTRL_GRP" -p "c_mouth_CTRL";
	setAttr ".rp" -type "double3" -0.33969901418059684 -0.84165434081721979 6.1361507227027725e-017 ;
	setAttr ".sp" -type "double3" -0.33969901418059684 -0.84165434081721979 6.1361507227027725e-017 ;
createNode transform -n "c_muothLip_07_second_CTRL" -p "c_muothLip_07_second_CTRL_GRP";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".rp" -type "double3" -0.33969901418059684 -0.84165434081721979 6.1361507227027725e-017 ;
	setAttr ".sp" -type "double3" -0.33969901418059684 -0.84165434081721979 6.1361507227027725e-017 ;
createNode nurbsCurve -n "c_muothLip_07_second_CTRLShape" -p "c_muothLip_07_second_CTRL";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-0.38663219215928918 -0.79472116283852745 5.3814076574143721e-017
		-0.33969901418059684 -0.77528080399448285 5.0687828436648782e-017
		-0.29276583620190449 -0.79472116283852745 5.3814076574143746e-017
		-0.27332547735785989 -0.84165434081721979 6.1361507227027725e-017
		-0.29276583620190449 -0.88858751879591213 6.8908937879911728e-017
		-0.33969901418059684 -0.90802787763995674 7.2035186017406667e-017
		-0.38663219215928912 -0.88858751879591213 6.8908937879911703e-017
		-0.40607255100333378 -0.84165434081721979 6.1361507227027725e-017
		-0.38663219215928918 -0.79472116283852745 5.3814076574143721e-017
		-0.33969901418059684 -0.77528080399448285 5.0687828436648782e-017
		-0.29276583620190449 -0.79472116283852745 5.3814076574143746e-017
		;
createNode transform -n "c_muothLip_03_second_CTRL_GRP" -p "c_mouth_CTRL";
	setAttr ".rp" -type "double3" 0.33969901418059711 -0.84165434081722013 5.4422613323120496e-017 ;
	setAttr ".sp" -type "double3" 0.33969901418059711 -0.84165434081722013 5.4422613323120496e-017 ;
createNode transform -n "c_muothLip_03_second_CTRL" -p "c_muothLip_03_second_CTRL_GRP";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".rp" -type "double3" 0.33969901418059711 -0.84165434081722013 5.4422613323120496e-017 ;
	setAttr ".sp" -type "double3" 0.33969901418059711 -0.84165434081722013 5.4422613323120496e-017 ;
createNode nurbsCurve -n "c_muothLip_03_second_CTRLShape" -p "c_muothLip_03_second_CTRL";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.38663219215928946 -0.79472116283852778 4.6875182670236493e-017
		0.33969901418059711 -0.77528080399448318 4.3748934532741554e-017
		0.29276583620190477 -0.79472116283852778 4.6875182670236518e-017
		0.27332547735786017 -0.84165434081722013 5.4422613323120496e-017
		0.29276583620190477 -0.88858751879591247 6.1970043976004499e-017
		0.33969901418059711 -0.90802787763995707 6.5096292113499438e-017
		0.3866321921592894 -0.88858751879591247 6.1970043976004475e-017
		0.40607255100333406 -0.84165434081722013 5.4422613323120496e-017
		0.38663219215928946 -0.79472116283852778 4.6875182670236493e-017
		0.33969901418059711 -0.77528080399448318 4.3748934532741554e-017
		0.29276583620190477 -0.79472116283852778 4.6875182670236518e-017
		;
createNode transform -n "c_muothLip_02_second_CTRL_GRP" -p "c_mouth_CTRL";
	setAttr ".rp" -type "double3" 0.19294904005457908 -0.76153674180407849 6.2716960036578905e-017 ;
	setAttr ".sp" -type "double3" 0.19294904005457908 -0.76153674180407849 6.2716960036578905e-017 ;
createNode transform -n "c_muothLip_02_second_CTRL" -p "c_muothLip_02_second_CTRL_GRP";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".rp" -type "double3" 0.19294904005457908 -0.76153674180407849 6.2716960036578905e-017 ;
	setAttr ".sp" -type "double3" 0.19294904005457908 -0.76153674180407849 6.2716960036578905e-017 ;
createNode nurbsCurve -n "c_muothLip_02_second_CTRLShape" -p "c_muothLip_02_second_CTRL";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.23988221803327145 -0.71460356382538637 5.5169529383694951e-017
		0.19294904005457908 -0.69516320498134154 5.2043281246199963e-017
		0.14601586207588677 -0.71460356382538615 5.5169529383694927e-017
		0.12657550323184213 -0.76153674180407849 6.2716960036578905e-017
		0.14601586207588674 -0.80846991978277083 7.0264390689462908e-017
		0.19294904005457905 -0.82791027862681543 7.3390638826957847e-017
		0.23988221803327137 -0.80846991978277083 7.0264390689462883e-017
		0.25932257687731602 -0.76153674180407849 6.2716960036578905e-017
		0.23988221803327145 -0.71460356382538637 5.5169529383694951e-017
		0.19294904005457908 -0.69516320498134154 5.2043281246199963e-017
		0.14601586207588677 -0.71460356382538615 5.5169529383694927e-017
		;
createNode transform -n "c_muothLip_04_second_CTRL_GRP" -p "c_mouth_CTRL";
	setAttr ".rp" -type "double3" 0.192949040054579 -0.92323951477704025 6.397888260491427e-017 ;
	setAttr ".sp" -type "double3" 0.192949040054579 -0.92323951477704025 6.397888260491427e-017 ;
createNode transform -n "c_muothLip_04_second_CTRL" -p "c_muothLip_04_second_CTRL_GRP";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".rp" -type "double3" 0.192949040054579 -0.92323951477704014 6.3978882604914246e-017 ;
	setAttr ".sp" -type "double3" 0.192949040054579 -0.92323951477704014 6.3978882604914246e-017 ;
createNode nurbsCurve -n "c_muothLip_04_second_CTRLShape" -p "c_muothLip_04_second_CTRL";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.23988221803327137 -0.87630633679834791 5.6431451952030267e-017
		0.192949040054579 -0.85686597795430319 5.3305203814535304e-017
		0.14601586207588668 -0.8763063367983478 5.6431451952030267e-017
		0.12657550323184205 -0.92323951477704014 6.3978882604914246e-017
		0.14601586207588665 -0.97017269275573248 7.1526313257798249e-017
		0.19294904005457897 -0.98961305159977719 7.4652561395293213e-017
		0.23988221803327128 -0.97017269275573248 7.1526313257798224e-017
		0.25932257687731597 -0.92323951477704014 6.3978882604914246e-017
		0.23988221803327137 -0.87630633679834791 5.6431451952030267e-017
		0.192949040054579 -0.85686597795430319 5.3305203814535304e-017
		0.14601586207588668 -0.8763063367983478 5.6431451952030267e-017
		;
createNode transform -n "c_muothLip_06_second_CTRL_GRP" -p "c_mouth_CTRL";
	setAttr ".rp" -type "double3" -0.19294904005457902 -0.92323951477703992 6.397888260491427e-017 ;
	setAttr ".sp" -type "double3" -0.19294904005457902 -0.92323951477703992 6.397888260491427e-017 ;
createNode transform -n "c_muothLip_06_second_CTRL" -p "c_muothLip_06_second_CTRL_GRP";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".rp" -type "double3" -0.19294904005457902 -0.9232395147770398 6.3978882604914246e-017 ;
	setAttr ".sp" -type "double3" -0.19294904005457902 -0.9232395147770398 6.3978882604914246e-017 ;
createNode nurbsCurve -n "c_muothLip_06_second_CTRLShape" -p "c_muothLip_06_second_CTRL";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-0.23988221803327137 -0.87630633679834757 5.6431451952030267e-017
		-0.192949040054579 -0.85686597795430286 5.3305203814535304e-017
		-0.14601586207588671 -0.87630633679834746 5.6431451952030267e-017
		-0.12657550323184208 -0.9232395147770398 6.3978882604914246e-017
		-0.14601586207588671 -0.97017269275573215 7.1526313257798249e-017
		-0.19294904005457902 -0.98961305159977686 7.4652561395293213e-017
		-0.23988221803327131 -0.97017269275573215 7.1526313257798224e-017
		-0.25932257687731597 -0.9232395147770398 6.3978882604914246e-017
		-0.23988221803327137 -0.87630633679834757 5.6431451952030267e-017
		-0.192949040054579 -0.85686597795430286 5.3305203814535304e-017
		-0.14601586207588671 -0.87630633679834746 5.6431451952030267e-017
		;
createNode transform -n "c_muothLip_08_second_CTRL_GRP" -p "c_mouth_CTRL";
	setAttr ".rp" -type "double3" -0.19294904005457897 -0.76153674180407849 6.2716960036578905e-017 ;
	setAttr ".sp" -type "double3" -0.19294904005457897 -0.76153674180407849 6.2716960036578905e-017 ;
createNode transform -n "c_muothLip_08_second_CTRL" -p "c_muothLip_08_second_CTRL_GRP";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".rp" -type "double3" -0.19294904005457897 -0.76153674180407849 6.2716960036578905e-017 ;
	setAttr ".sp" -type "double3" -0.19294904005457897 -0.76153674180407849 6.2716960036578905e-017 ;
createNode nurbsCurve -n "c_muothLip_08_second_CTRLShape" -p "c_muothLip_08_second_CTRL";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-0.23988221803327131 -0.71460356382538615 5.5169529383694902e-017
		-0.19294904005457894 -0.69516320498134154 5.2043281246199963e-017
		-0.14601586207588665 -0.71460356382538615 5.5169529383694927e-017
		-0.12657550323184202 -0.76153674180407849 6.2716960036578905e-017
		-0.14601586207588665 -0.80846991978277083 7.0264390689462908e-017
		-0.19294904005457897 -0.82791027862681543 7.3390638826957847e-017
		-0.23988221803327126 -0.80846991978277083 7.0264390689462883e-017
		-0.25932257687731591 -0.76153674180407849 6.2716960036578905e-017
		-0.23988221803327131 -0.71460356382538615 5.5169529383694902e-017
		-0.19294904005457894 -0.69516320498134154 5.2043281246199963e-017
		-0.14601586207588665 -0.71460356382538615 5.5169529383694927e-017
		;
createNode transform -n "c_muothLip_05_second_CTRL_GRP" -p "c_mouth_CTRL";
	setAttr ".rp" -type "double3" -6.9388939039072284e-017 -0.9448718128409378 6.5387741795716349e-017 ;
	setAttr ".sp" -type "double3" -6.9388939039072284e-017 -0.9448718128409378 6.5387741795716349e-017 ;
createNode transform -n "c_muothLip_05_second_CTRL" -p "c_muothLip_05_second_CTRL_GRP";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".rp" -type "double3" -6.9388939039072284e-017 -0.94487181284093769 6.5387741795716324e-017 ;
	setAttr ".sp" -type "double3" -6.9388939039072284e-017 -0.94487181284093769 6.5387741795716324e-017 ;
createNode nurbsCurve -n "c_muothLip_05_second_CTRLShape" -p "c_muothLip_05_second_CTRL";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.054293777706352651 -0.890578035134585 5.6656636429106906e-017
		-7.8148960874892609e-017 -0.86808881605614374 5.3040094171748783e-017
		-0.054293777706352735 -0.890578035134585 5.6656636429106906e-017
		-0.076782996784794028 -0.94487181284093769 6.5387741795716324e-017
		-0.054293777706352749 -0.99916559054729015 7.4118847162325693e-017
		-9.2525154476382931e-017 -1.0216548096257319 7.7735389419683891e-017
		0.054293777706352568 -0.99916559054729015 7.4118847162325693e-017
		0.076782996784793889 -0.94487181284093769 6.5387741795716324e-017
		0.054293777706352651 -0.890578035134585 5.6656636429106906e-017
		-7.8148960874892609e-017 -0.86808881605614374 5.3040094171748783e-017
		-0.054293777706352735 -0.890578035134585 5.6656636429106906e-017
		;
createNode transform -n "GRP_c_jaw_up_FRAME" -p "c_mouth_CTRL";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 -0.59562268734120716 0 ;
	setAttr ".s" -type "double3" 0.25 0.25 0.25 ;
createNode transform -n "c_jaw_up_FRAME" -p "GRP_c_jaw_up_FRAME";
	addAttr -ci true -sn "up" -ln "up" -min 0 -at "double";
	addAttr -ci true -sn "dn" -ln "dn" -min 0 -at "double";
	addAttr -ci true -sn "lf" -ln "lf" -min 0 -at "double";
	addAttr -ci true -sn "rt" -ln "rt" -min 0 -at "double";
	addAttr -ci true -sn "lfup" -ln "lfup" -min 0 -at "double";
	addAttr -ci true -sn "rtup" -ln "rtup" -min 0 -at "double";
	addAttr -ci true -sn "lfdn" -ln "lfdn" -min 0 -at "double";
	addAttr -ci true -sn "rtdn" -ln "rtdn" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_up" -ln "fourAxis_up" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_dn" -ln "fourAxis_dn" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_lf" -ln "fourAxis_lf" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_rt" -ln "fourAxis_rt" -min 0 -at "double";
	addAttr -ci true -sn "up_Vis" -ln "up_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "dn_Vis" -ln "dn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lf_Vis" -ln "lf_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lfup_Vis" -ln "lfup_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rt_Vis" -ln "rt_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rtup_Vis" -ln "rtup_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lfdn_Vis" -ln "lfdn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rtdn_Vis" -ln "rtdn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_up_Vis" -ln "fourAxis_up_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_dn_Vis" -ln "fourAxis_dn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_lf_Vis" -ln "fourAxis_lf_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_rt_Vis" -ln "fourAxis_rt_Vis" -min 0 -max 1 -at "bool";
	setAttr -k on ".up";
	setAttr -k on ".dn";
	setAttr -k on ".lf";
	setAttr -k on ".rt";
	setAttr -k on ".lfup";
	setAttr -k on ".rtup";
	setAttr -k on ".lfdn";
	setAttr -k on ".rtdn";
	setAttr -k on ".fourAxis_up";
	setAttr -k on ".fourAxis_dn";
	setAttr -k on ".fourAxis_lf";
	setAttr -k on ".fourAxis_rt";
	setAttr -cb on ".up_Vis";
	setAttr -cb on ".dn_Vis";
	setAttr -cb on ".lf_Vis";
	setAttr -cb on ".lfup_Vis";
	setAttr -cb on ".rt_Vis";
	setAttr -cb on ".rtup_Vis";
	setAttr -cb on ".lfdn_Vis";
	setAttr -cb on ".rtdn_Vis";
	setAttr -cb on ".fourAxis_up_Vis";
	setAttr -cb on ".fourAxis_dn_Vis";
	setAttr -cb on ".fourAxis_lf_Vis";
	setAttr -cb on ".fourAxis_rt_Vis";
createNode nurbsCurve -n "c_jaw_up_FRAMEShape" -p "c_jaw_up_FRAME";
	setAttr -k off ".v" no;
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode transform -n "GRP_c_jaw_up_CTRL" -p "c_jaw_up_FRAME";
	addAttr -ci true -k true -sn "T1" -ln "T1" -at "double";
	addAttr -ci true -k true -sn "T2" -ln "T2" -at "double";
	addAttr -ci true -k true -sn "T3" -ln "T3" -at "double";
	addAttr -ci true -k true -sn "R1" -ln "R1" -at "double";
	addAttr -ci true -k true -sn "R2" -ln "R2" -at "double";
	addAttr -ci true -k true -sn "R3" -ln "R3" -at "double";
	addAttr -ci true -sn "S1" -ln "S1" -at "double";
	addAttr -ci true -sn "S2" -ln "S2" -at "double";
	addAttr -ci true -sn "S3" -ln "S3" -at "double";
	setAttr ".s" -type "double3" 9.9999999999999998e-013 9.9999999999999998e-013 9.9999999999999998e-013 ;
	setAttr -k on ".S1";
	setAttr -k on ".S2";
	setAttr -k on ".S3";
createNode transform -n "c_jaw_up_CTRL" -p "GRP_c_jaw_up_CTRL";
	addAttr -ci true -sn "frameSelectAble" -ln "frameSelectAble" -min 0 -max 2 -en 
		"normal:template:reference" -at "enum";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".mntl" -type "double3" -1 -1 0 ;
	setAttr ".mxtl" -type "double3" 1 1 0 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
	setAttr ".frameSelectAble" 2;
createNode nurbsCurve -n "c_jaw_up_CTRLShape" -p "c_jaw_up_CTRL";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		1 32 0 no 3
		33 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32
		33
		-0.050000000000000003 0.050000000000000003 0
		-0.050000000000000003 0.15000000000000002 0
		-0.10000000000000001 0.15000000000000002 0
		0 0.25 0
		0.10000000000000001 0.15000000000000002 0
		0.050000000000000003 0.15000000000000002 0
		0.050000000000000003 0.050000000000000003 0
		0.20000000000000001 0.20000000000000001 0
		0.050000000000000003 0.050000000000000003 0
		0.15000000000000002 0.050000000000000003 0
		0.15000000000000002 0.10000000000000001 0
		0.25 0 0
		0.15000000000000002 -0.10000000000000001 0
		0.15000000000000002 -0.050000000000000003 0
		0.050000000000000003 -0.050000000000000003 0
		0.20000000000000001 -0.20000000000000001 0
		0.050000000000000003 -0.050000000000000003 0
		0.050000000000000003 -0.15000000000000002 0
		0.10000000000000001 -0.15000000000000002 0
		0 -0.25 0
		-0.10000000000000001 -0.15000000000000002 0
		-0.050000000000000003 -0.15000000000000002 0
		-0.050000000000000003 -0.050000000000000003 0
		-0.20000000000000001 -0.20000000000000001 0
		-0.050000000000000003 -0.050000000000000003 0
		-0.15000000000000002 -0.050000000000000003 0
		-0.15000000000000002 -0.10000000000000001 0
		-0.25 0 0
		-0.15000000000000002 0.10000000000000001 0
		-0.15000000000000002 0.050000000000000003 0
		-0.050000000000000003 0.050000000000000003 0
		-0.20000000000000001 0.20000000000000001 0
		-0.050000000000000003 0.050000000000000003 0
		;
createNode transform -n "c_jaw_up_FRAME_lockzy" -p "c_jaw_up_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_jaw_up_FRAME_lockzyShape" -p "c_jaw_up_FRAME_lockzy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 0.20000000000000001 0
		-1 -1 0
		1 -1 0
		1 0.20000000000000001 0
		-1 0.20000000000000001 0
		;
createNode transform -n "c_jaw_up_FRAME_lockfy" -p "c_jaw_up_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_jaw_up_FRAME_lockfyShape" -p "c_jaw_up_FRAME_lockfy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -0.20000000000000001 0
		1 -0.20000000000000001 0
		1 1 0
		-1 1 0
		;
createNode transform -n "c_jaw_up_FRAME_lockzx" -p "c_jaw_up_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_jaw_up_FRAME_lockzxShape" -p "c_jaw_up_FRAME_lockzx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		0.20000000000000001 -1 0
		0.20000000000000001 1 0
		-1 1 0
		;
createNode transform -n "c_jaw_up_FRAME_lockfx" -p "c_jaw_up_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_jaw_up_FRAME_lockfxShape" -p "c_jaw_up_FRAME_lockfx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 1 0
		-0.20000000000000001 -1 0
		1 -1 0
		1 1 0
		-0.20000000000000001 1 0
		;
createNode transform -n "c_jaw_up_FRAME_lockzyfy" -p "c_jaw_up_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_jaw_up_FRAME_lockzyfyShape" -p "c_jaw_up_FRAME_lockzyfy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 0.20000000000000001 0
		-1 -0.20000000000000001 0
		1 -0.20000000000000001 0
		1 0.20000000000000001 0
		-1 0.20000000000000001 0
		;
createNode transform -n "c_jaw_up_FRAME_lockzxfx" -p "c_jaw_up_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_jaw_up_FRAME_lockzxfxShape" -p "c_jaw_up_FRAME_lockzxfx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 1 0
		-0.20000000000000001 -1 0
		0.20000000000000001 -1 0
		0.20000000000000001 1 0
		-0.20000000000000001 1 0
		;
createNode transform -n "c_jaw_up_FRAME_lockzyfyzx" -p "c_jaw_up_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_jaw_up_FRAME_lockzyfyzxShape" -p "c_jaw_up_FRAME_lockzyfyzx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 0.20000000000000001 0
		-1 -0.20000000000000001 0
		0.20000000000000001 -0.20000000000000001 0
		0.20000000000000001 0.20000000000000001 0
		-1 0.20000000000000001 0
		;
createNode transform -n "c_jaw_up_FRAME_lockzyfyfx" -p "c_jaw_up_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_jaw_up_FRAME_lockzyfyfxShape" -p "c_jaw_up_FRAME_lockzyfyfx";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 0.20000000000000001 0
		-0.20000000000000001 -0.20000000000000001 0
		1 -0.20000000000000001 0
		1 0.20000000000000001 0
		-0.20000000000000001 0.20000000000000001 0
		;
createNode transform -n "c_jaw_up_FRAME_lockzxfxzy" -p "c_jaw_up_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_jaw_up_FRAME_lockzxfxzyShape" -p "c_jaw_up_FRAME_lockzxfxzy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 0.20000000000000001 0
		-0.20000000000000001 -1 0
		0.20000000000000001 -1 0
		0.20000000000000001 0.20000000000000001 0
		-0.20000000000000001 0.20000000000000001 0
		;
createNode transform -n "c_jaw_up_FRAME_lockzxfxfy" -p "c_jaw_up_FRAME";
	setAttr ".v" no;
createNode nurbsCurve -n "c_jaw_up_FRAME_lockzxfxfyShape" -p "c_jaw_up_FRAME_lockzxfxfy";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.20000000000000001 1 0
		-0.20000000000000001 -0.20000000000000001 0
		0.20000000000000001 -0.20000000000000001 0
		0.20000000000000001 1 0
		-0.20000000000000001 1 0
		;
createNode transform -n "c_jaw_up_CTRL_up" -p "c_jaw_up_FRAME";
	setAttr ".t" -type "double3" 0 2.2 0 ;
createNode nurbsCurve -n "curveShape133" -p "c_jaw_up_CTRL_up";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_jaw_up_LOC_up" -p "c_jaw_up_CTRL_up";
	setAttr -k off ".v" no;
createNode transform -n "c_jaw_up_CTRL_dn" -p "c_jaw_up_FRAME";
	setAttr ".t" -type "double3" 0 -2.2 0 ;
createNode nurbsCurve -n "curveShape134" -p "c_jaw_up_CTRL_dn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_jaw_up_LOC_dn" -p "c_jaw_up_CTRL_dn";
	setAttr -k off ".v" no;
createNode transform -n "c_jaw_up_CTRL_lf" -p "c_jaw_up_FRAME";
	setAttr ".t" -type "double3" -2.2 0 0 ;
createNode nurbsCurve -n "curveShape135" -p "c_jaw_up_CTRL_lf";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_jaw_up_LOC_lf" -p "c_jaw_up_CTRL_lf";
	setAttr -k off ".v" no;
createNode transform -n "c_jaw_up_CTRL_lfup" -p "c_jaw_up_FRAME";
	setAttr ".t" -type "double3" -2.2 2.2 0 ;
createNode nurbsCurve -n "curveShape136" -p "c_jaw_up_CTRL_lfup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_jaw_up_LOC_lfup" -p "c_jaw_up_CTRL_lfup";
	setAttr -k off ".v" no;
createNode transform -n "c_jaw_up_CTRL_rt" -p "c_jaw_up_FRAME";
	setAttr ".t" -type "double3" 2.2 0 0 ;
createNode nurbsCurve -n "curveShape137" -p "c_jaw_up_CTRL_rt";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_jaw_up_LOC_rt" -p "c_jaw_up_CTRL_rt";
	setAttr -k off ".v" no;
createNode transform -n "c_jaw_up_CTRL_rtup" -p "c_jaw_up_FRAME";
	setAttr ".t" -type "double3" 2.2 2.2 0 ;
createNode nurbsCurve -n "curveShape138" -p "c_jaw_up_CTRL_rtup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_jaw_up_LOC_rtup" -p "c_jaw_up_CTRL_rtup";
	setAttr -k off ".v" no;
createNode transform -n "c_jaw_up_CTRL_lfdn" -p "c_jaw_up_FRAME";
	setAttr ".t" -type "double3" -2.2 -2.2 0 ;
createNode nurbsCurve -n "curveShape139" -p "c_jaw_up_CTRL_lfdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_jaw_up_LOC_lfdn" -p "c_jaw_up_CTRL_lfdn";
	setAttr -k off ".v" no;
createNode transform -n "c_jaw_up_CTRL_rtdn" -p "c_jaw_up_FRAME";
	setAttr ".t" -type "double3" 2.2 -2.2 0 ;
createNode nurbsCurve -n "curveShape140" -p "c_jaw_up_CTRL_rtdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_jaw_up_LOC_rtdn" -p "c_jaw_up_CTRL_rtdn";
	setAttr -k off ".v" no;
createNode transform -n "c_jaw_up_CTRL_fourAxisup" -p "c_jaw_up_FRAME";
	setAttr ".t" -type "double3" 0 4.4 0 ;
createNode nurbsCurve -n "curveShape141" -p "c_jaw_up_CTRL_fourAxisup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_jaw_up_LOC_fourAxis_up" -p "c_jaw_up_CTRL_fourAxisup";
	setAttr -k off ".v" no;
createNode transform -n "c_jaw_up_CTRL_fourAxisdn" -p "c_jaw_up_FRAME";
	setAttr ".t" -type "double3" 0 -4.4 0 ;
createNode nurbsCurve -n "curveShape142" -p "c_jaw_up_CTRL_fourAxisdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_jaw_up_LOC_fourAxis_dn" -p "c_jaw_up_CTRL_fourAxisdn";
	setAttr -k off ".v" no;
createNode transform -n "c_jaw_up_CTRL_fourAxislf" -p "c_jaw_up_FRAME";
	setAttr ".t" -type "double3" -4.4 0 0 ;
createNode nurbsCurve -n "curveShape143" -p "c_jaw_up_CTRL_fourAxislf";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_jaw_up_LOC_fourAxis_lf" -p "c_jaw_up_CTRL_fourAxislf";
	setAttr -k off ".v" no;
createNode transform -n "c_jaw_up_CTRL_fourAxisrt" -p "c_jaw_up_FRAME";
	setAttr ".t" -type "double3" 4.4 0 0 ;
createNode nurbsCurve -n "curveShape144" -p "c_jaw_up_CTRL_fourAxisrt";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_jaw_up_LOC_fourAxis_rt" -p "c_jaw_up_CTRL_fourAxisrt";
	setAttr -k off ".v" no;
createNode transform -n "CHR_Pier_Lips_Neutre_CTRL_GRP" -p "Facial_CTRL_FRAME";
	setAttr ".t" -type "double3" 3.9685688341519176 0.74690106232520648 0 ;
createNode transform -n "CHR_Pier_Lips_Neutre_CTRL" -p "CHR_Pier_Lips_Neutre_CTRL_GRP";
	setAttr ".rp" -type "double3" 6.6613381477509392e-016 -2.2204460492503131e-016 
		9.8607613152626476e-032 ;
	setAttr ".sp" -type "double3" 6.6613381477509392e-016 -2.2204460492503131e-016 9.8607613152626476e-032 ;
createNode nurbsCurve -n "CHR_Pier_Lips_Neutre_CTRLShape" -p "CHR_Pier_Lips_Neutre_CTRL";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		1.7297813468466088 1.8354919834978998 -2.8795895926052631e-016
		1.6314409172153482e-005 1.8362089566898601 -4.0723546559307856e-016
		-1.7302643941697169 1.8354919834978998 -2.8795895926052646e-016
		-1.730597694015148 0.0064941761325818829 -9.1558587157081199e-032
		-1.7302643941697169 -1.6166247018125222 2.8795895926052646e-016
		1.6314409171679347e-005 -1.6179485866271808 4.0723546559307876e-016
		1.7297813468466088 -1.6166247018125222 2.8795895926052651e-016
		1.7311459989749449 0.0064941761325797891 2.4517502552316324e-031
		1.7297813468466088 1.8354919834978998 -2.8795895926052631e-016
		1.6314409172153482e-005 1.8362089566898601 -4.0723546559307856e-016
		-1.7302643941697169 1.8354919834978998 -2.8795895926052646e-016
		;
createNode transform -n "c_GRP_a_FRAME" -p "CHR_Pier_Lips_Neutre_CTRL";
	setAttr ".t" -type "double3" -0.2234169624570066 1.2544847797476326 -0.0006661546058596621 ;
	setAttr ".r" -type "double3" -3.5311250384401255e-030 0 0 ;
	setAttr ".s" -type "double3" 1.4000000000000001 0.20000000000000007 0.20000000000000007 ;
createNode transform -n "c_a_FRAME" -p "c_GRP_a_FRAME";
	addAttr -ci true -sn "up" -ln "up" -min 0 -at "double";
	addAttr -ci true -sn "dn" -ln "dn" -min 0 -at "double";
	addAttr -ci true -sn "lf" -ln "lf" -min 0 -at "double";
	addAttr -ci true -sn "rt" -ln "rt" -min 0 -at "double";
	addAttr -ci true -sn "lfup" -ln "lfup" -min 0 -at "double";
	addAttr -ci true -sn "rtup" -ln "rtup" -min 0 -at "double";
	addAttr -ci true -sn "lfdn" -ln "lfdn" -min 0 -at "double";
	addAttr -ci true -sn "rtdn" -ln "rtdn" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_up" -ln "fourAxis_up" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_dn" -ln "fourAxis_dn" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_lf" -ln "fourAxis_lf" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_rt" -ln "fourAxis_rt" -min 0 -at "double";
	addAttr -ci true -sn "up_Vis" -ln "up_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "dn_Vis" -ln "dn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lf_Vis" -ln "lf_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lfup_Vis" -ln "lfup_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rt_Vis" -ln "rt_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rtup_Vis" -ln "rtup_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lfdn_Vis" -ln "lfdn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rtdn_Vis" -ln "rtdn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_up_Vis" -ln "fourAxis_up_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_dn_Vis" -ln "fourAxis_dn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_lf_Vis" -ln "fourAxis_lf_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_rt_Vis" -ln "fourAxis_rt_Vis" -min 0 -max 1 -at "bool";
	setAttr -k on ".up";
	setAttr -k on ".dn";
	setAttr -k on ".lf";
	setAttr -k on ".rt";
	setAttr -k on ".lfup";
	setAttr -k on ".rtup";
	setAttr -k on ".lfdn";
	setAttr -k on ".rtdn";
	setAttr -k on ".fourAxis_up";
	setAttr -k on ".fourAxis_dn";
	setAttr -k on ".fourAxis_lf";
	setAttr -k on ".fourAxis_rt";
	setAttr -cb on ".up_Vis";
	setAttr -cb on ".dn_Vis";
	setAttr -cb on ".lf_Vis";
	setAttr -cb on ".lfup_Vis";
	setAttr -cb on ".rt_Vis";
	setAttr -cb on ".rtup_Vis";
	setAttr -cb on ".lfdn_Vis";
	setAttr -cb on ".rtdn_Vis";
	setAttr -cb on ".fourAxis_up_Vis";
	setAttr -cb on ".fourAxis_dn_Vis";
	setAttr -cb on ".fourAxis_lf_Vis";
	setAttr -cb on ".fourAxis_rt_Vis";
createNode nurbsCurve -n "c_a_FRAMEShape" -p "c_a_FRAME";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.078106160309654435 0.42223139237782875 0
		-0.078106160309654435 -0.42223139237782464 0
		1.0738189356316263 -0.42223139237782464 0
		1.0738189356316263 0.42223139237782875 0
		-0.078106160309654435 0.42223139237782875 0
		;
createNode transform -n "c_GRP_a_CTRL" -p "c_a_FRAME";
createNode transform -n "c_a_CTRL" -p "c_GRP_a_CTRL";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".mntl" -type "double3" 0 0 0 ;
	setAttr ".mxtl" -type "double3" 1 0 0 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
createNode nurbsCurve -n "c_a_CTRLShape" -p "c_a_CTRL";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".tw" yes;
	setAttr -s 33 ".cp[0:32]" -type "double3" 0.037387204432272829 0.027434445505786761 
		0 0.037387204432272829 0.082303336517364128 0 0.074755308724820085 0.082303336517364128 
		0 1.9100139725567e-005 0.13717222752894154 0 -0.074717108445368968 0.082303336517364128 
		0 -0.037349004152821698 0.082303336517364128 0 -0.037349004152821698 0.027434445505786761 
		0 -0.1494533170304635 0.10973778202315287 0 -0.037349004152821698 0.027434445505786761 
		0 -0.11208521273791623 0.027434445505786761 0 -0.11208521273791623 0.054868891011575494 
		0 -0.18682142132301072 -1.9493345963744493e-015 0 -0.11208521273791623 -0.054868891011579352 
		0 -0.11208521273791623 -0.027434445505790647 0 -0.037349004152821698 -0.027434445505790647 
		0 -0.1494533170304635 -0.10973778202315682 0 -0.037349004152821698 -0.027434445505790647 
		0 -0.037349004152821698 -0.082303336517367987 0 -0.074717108445368968 -0.082303336517367987 
		0 1.9100139725567e-005 -0.13717222752894548 0 0.074755308724820085 -0.082303336517367987 
		0 0.037387204432272829 -0.082303336517367987 0 0.037387204432272829 -0.027434445505790647 
		0 0.14949151730991461 -0.10973778202315682 0 0.037387204432272829 -0.027434445505790647 
		0 0.11212341301736736 -0.027434445505790647 0 0.11212341301736736 -0.054868891011579352 
		0 0.18685962160246189 -1.9493345963744493e-015 0 0.11212341301736736 0.054868891011575494 
		0 0.11212341301736736 0.027434445505786761 0 0.037387204432272829 0.027434445505786761 
		0 0.14949151730991461 0.10973778202315287 0 0.037387204432272829 0.027434445505786761 
		0;
createNode nurbsCurve -n "c_a_CTRLShapeOrig" -p "c_a_CTRL";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 32 0 no 3
		33 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32
		33
		-0.050000000000000003 0.050000000000000003 0
		-0.050000000000000003 0.15000000000000002 0
		-0.10000000000000001 0.15000000000000002 0
		0 0.25 0
		0.10000000000000001 0.15000000000000002 0
		0.050000000000000003 0.15000000000000002 0
		0.050000000000000003 0.050000000000000003 0
		0.20000000000000001 0.20000000000000001 0
		0.050000000000000003 0.050000000000000003 0
		0.15000000000000002 0.050000000000000003 0
		0.15000000000000002 0.10000000000000001 0
		0.25 0 0
		0.15000000000000002 -0.10000000000000001 0
		0.15000000000000002 -0.050000000000000003 0
		0.050000000000000003 -0.050000000000000003 0
		0.20000000000000001 -0.20000000000000001 0
		0.050000000000000003 -0.050000000000000003 0
		0.050000000000000003 -0.15000000000000002 0
		0.10000000000000001 -0.15000000000000002 0
		0 -0.25 0
		-0.10000000000000001 -0.15000000000000002 0
		-0.050000000000000003 -0.15000000000000002 0
		-0.050000000000000003 -0.050000000000000003 0
		-0.20000000000000001 -0.20000000000000001 0
		-0.050000000000000003 -0.050000000000000003 0
		-0.15000000000000002 -0.050000000000000003 0
		-0.15000000000000002 -0.10000000000000001 0
		-0.25 0 0
		-0.15000000000000002 0.10000000000000001 0
		-0.15000000000000002 0.050000000000000003 0
		-0.050000000000000003 0.050000000000000003 0
		-0.20000000000000001 0.20000000000000001 0
		-0.050000000000000003 0.050000000000000003 0
		;
createNode transform -n "c_a_CTRL_up" -p "c_a_FRAME";
	setAttr ".t" -type "double3" 0 2.2 0 ;
createNode nurbsCurve -n "curveShape337" -p "c_a_CTRL_up";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_a_LOC_up" -p "c_a_CTRL_up";
	setAttr -k off ".v" no;
createNode transform -n "c_a_CTRL_dn" -p "c_a_FRAME";
	setAttr ".t" -type "double3" 0 -2.2 0 ;
createNode nurbsCurve -n "curveShape338" -p "c_a_CTRL_dn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_a_LOC_dn" -p "c_a_CTRL_dn";
	setAttr -k off ".v" no;
createNode transform -n "c_a_CTRL_lf" -p "c_a_FRAME";
	setAttr ".t" -type "double3" -2.2 0 0 ;
createNode nurbsCurve -n "curveShape339" -p "c_a_CTRL_lf";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_a_LOC_lf" -p "c_a_CTRL_lf";
	setAttr -k off ".v" no;
createNode transform -n "c_a_CTRL_lfup" -p "c_a_FRAME";
	setAttr ".t" -type "double3" -2.2 2.2 0 ;
createNode nurbsCurve -n "curveShape340" -p "c_a_CTRL_lfup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_a_LOC_lfup" -p "c_a_CTRL_lfup";
	setAttr -k off ".v" no;
createNode transform -n "c_a_CTRL_rt" -p "c_a_FRAME";
	setAttr ".t" -type "double3" 2.2 0 0 ;
createNode nurbsCurve -n "curveShape341" -p "c_a_CTRL_rt";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_a_LOC_rt" -p "c_a_CTRL_rt";
	setAttr -k off ".v" no;
createNode transform -n "c_a_CTRL_rtup" -p "c_a_FRAME";
	setAttr ".t" -type "double3" 2.2 2.2 0 ;
createNode nurbsCurve -n "curveShape342" -p "c_a_CTRL_rtup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_a_LOC_rtup" -p "c_a_CTRL_rtup";
	setAttr -k off ".v" no;
createNode transform -n "c_a_CTRL_lfdn" -p "c_a_FRAME";
	setAttr ".t" -type "double3" -2.2 -2.2 0 ;
createNode nurbsCurve -n "curveShape343" -p "c_a_CTRL_lfdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_a_LOC_lfdn" -p "c_a_CTRL_lfdn";
	setAttr -k off ".v" no;
createNode transform -n "c_a_CTRL_rtdn" -p "c_a_FRAME";
	setAttr ".t" -type "double3" 2.2 -2.2 0 ;
createNode nurbsCurve -n "curveShape344" -p "c_a_CTRL_rtdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_a_LOC_rtdn" -p "c_a_CTRL_rtdn";
	setAttr -k off ".v" no;
createNode transform -n "c_a_CTRL_fourAxisup" -p "c_a_FRAME";
	setAttr ".t" -type "double3" 0 4.4 0 ;
createNode nurbsCurve -n "curveShape345" -p "c_a_CTRL_fourAxisup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_a_LOC_fourAxis_up" -p "c_a_CTRL_fourAxisup";
	setAttr -k off ".v" no;
createNode transform -n "c_a_CTRL_fourAxisdn" -p "c_a_FRAME";
	setAttr ".t" -type "double3" 0 -4.4 0 ;
createNode nurbsCurve -n "curveShape346" -p "c_a_CTRL_fourAxisdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_a_LOC_fourAxis_dn" -p "c_a_CTRL_fourAxisdn";
	setAttr -k off ".v" no;
createNode transform -n "c_a_CTRL_fourAxislf" -p "c_a_FRAME";
	setAttr ".t" -type "double3" -4.4 0 0 ;
createNode nurbsCurve -n "curveShape347" -p "c_a_CTRL_fourAxislf";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_a_LOC_fourAxis_lf" -p "c_a_CTRL_fourAxislf";
	setAttr -k off ".v" no;
createNode transform -n "c_a_CTRL_fourAxisrt" -p "c_a_FRAME";
	setAttr ".t" -type "double3" 4.4 0 0 ;
createNode nurbsCurve -n "curveShape348" -p "c_a_CTRL_fourAxisrt";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_a_LOC_fourAxis_rt" -p "c_a_CTRL_fourAxisrt";
	setAttr -k off ".v" no;
createNode transform -n "Text_Text_a_1" -p "c_GRP_a_FRAME";
	setAttr ".t" -type "double3" -0.60064458732769055 -0.49286352576273618 -5.4003800142741592e-015 ;
	setAttr ".s" -type "double3" 0.070655207584665439 0.49458645309265803 0.49458645309265836 ;
createNode transform -n "Text_Char_a_5" -p "Text_Text_a_1";
createNode transform -n "Text_curve103" -p "Text_Char_a_5";
	setAttr ".ovdt" 2;
createNode nurbsCurve -n "Text_curveShape103" -p "Text_curve103";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr ".cc" -type "nurbsCurve" 
		2 54 1 no 3
		57 0 0 1 1 2 2 3 4 4 5 5 6 7 7 7.0656260013733121 7.0656260013733121 8.0656260013733121
		 9.0656260013733121 9.0656260013733121 10.065626001373312 10.065626001373312 11.065626001373312
		 11.065626001373312 11.175101482379477 11.175101482379477 12.175101482379477 13.175101482379477
		 13.175101482379477 14.175101482379477 15.175101482379477 15.175101482379477 16.175101482379475
		 17.175101482379475 17.175101482379475 18.175101482379475 18.175101482379475 19.175101482379475
		 19.175101482379475 20.175101482379475 20.175101482379475 20.770415436754998 20.770415436754998
		 21.770415436754998 22.770415436754998 23.770415436754998 23.770415436754998 24.770415436754998
		 24.770415436754998 25.770415436754998 25.770415436754998 25.840727483752786 25.840727483752786
		 26.840727483752786 26.840727483752786 27.840727483752786 28.840727483752786 28.840727483752786
		
		56
		1.1000000000000001 0.27031357289997715 0
		0.82343785763332566 0.075001144426642255 0
		0.7531258106355383 0.045313191424429695 0
		0.64687571526665144 0 0
		0.52812542915999083 0 0
		0.34062561989776458 0 0
		0.10000000000000001 0.24843823910887314 0
		0.10000000000000001 0.45312581063553825 0
		0.10000000000000001 0.58125123979552906 0
		0.15937590600442514 0.67500114442664227 0
		0.23906309605554285 0.80468757152666515 0
		0.63750057221332124 1.0343755245288777 0
		1.1000000000000001 1.2000000000000002 0
		1.1000000000000001 1.2328130006866562 0
		1.1000000000000001 1.265626001373312 0
		1.1000000000000001 1.5140627145799954 0
		0.92968795300221263 1.7000000000000002 0
		0.76718852521553371 1.7000000000000002 0
		0.643750667582208 1.7000000000000002 0
		0.57031357289997719 1.6359380483710995 0
		0.49531395437552456 1.5718760967421987 0
		0.49531395437552456 1.4890638590066378 0
		0.49765697718776225 1.4343762874799726 0
		0.5 1.3796887159533076 0
		0.5 1.2937514305333029 0
		0.41718776226443888 1.2000000000000002 0
		0.34843823910887317 1.2000000000000002 0
		0.28281376363775085 1.2000000000000002 0
		0.20000000000000001 1.2953139543755245 0
		0.20000000000000001 1.3781261921110859 0
		0.20000000000000001 1.5359380483710996 0
		0.52968795300221261 1.8 0
		0.82812542915999099 1.8 0
		1.0562508583199817 1.8 0
		1.2031250476844435 1.7218753337911039 0
		1.3140627145799955 1.6625009536888689 0
		1.3656260013733119 1.5359380483710996 0
		1.4000000000000001 1.4531258106355383 0
		1.4000000000000001 1.198439002059968 0
		1.4000000000000001 0.90078202487220571 0
		1.4000000000000001 0.60312504768444342 0
		1.4000000000000001 0.35156328679331655 0
		1.4187502861066605 0.23906309605554285 0
		1.4625009536888687 0.20000000000000001 0
		1.4921889066910812 0.20000000000000001 0
		1.521875333791104 0.20000000000000001 0
		1.5453131914244298 0.2093751430533303 0
		1.5859388113221944 0.22500038147554743 0
		1.7000000000000002 0.30000000000000004 0
		1.7000000000000002 0.2648439765011063 0
		1.7000000000000002 0.22968795300221254 0
		1.4906263828488595 0 0
		1.3015625238422217 0 0
		1.2093751430533304 0 0
		1.1015625238422218 0.121875333791104 0
		1.1000000000000001 0.27031357289997715 0
		;
createNode transform -n "Text_curve104" -p "Text_Char_a_5";
	setAttr ".ovdt" 2;
createNode nurbsCurve -n "Text_curveShape104" -p "Text_curve104";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr ".cc" -type "nurbsCurve" 
		2 11 1 no 3
		14 0 0 0.70000000000000007 0.70000000000000007 1.7000000000000002 1.7000000000000002
		 2.7000000000000002 3.7000000000000002 3.7000000000000002 4.7000000000000002 5.7000000000000002
		 5.7000000000000002 6.7000000000000002 6.7000000000000002
		13
		1.1000000000000001 0.40000000000000002 0
		1.1000000000000001 0.75 0
		1.1000000000000001 1.1000000000000001 0
		0.79062638284885944 0.97968871595330753 0
		0.70156252384222173 0.92968795300221263 0
		0.53906309605554292 0.84218814373998629 0
		0.40000000000000002 0.64843823910887322 0
		0.40000000000000002 0.53437552452887771 0
		0.40000000000000002 0.39062638284885942 0
		0.57656366826886396 0.20000000000000001 0
		0.69062638284885947 0.20000000000000001 0
		0.84687571526665151 0.20000000000000001 0
		1.1000000000000001 0.40000000000000002 0
		;
createNode transform -n "c_GRP_uo_FRAME" -p "CHR_Pier_Lips_Neutre_CTRL";
	setAttr ".t" -type "double3" -0.22332856081272312 0.88952891443840942 -0.00066615460585969213 ;
	setAttr ".r" -type "double3" -3.5311250384401255e-030 0 0 ;
	setAttr ".s" -type "double3" 1.4000000000000001 0.20000000000000007 0.20000000000000007 ;
createNode transform -n "c_uo_FRAME" -p "c_GRP_uo_FRAME";
	addAttr -ci true -sn "up" -ln "up" -min 0 -at "double";
	addAttr -ci true -sn "dn" -ln "dn" -min 0 -at "double";
	addAttr -ci true -sn "lf" -ln "lf" -min 0 -at "double";
	addAttr -ci true -sn "rt" -ln "rt" -min 0 -at "double";
	addAttr -ci true -sn "lfup" -ln "lfup" -min 0 -at "double";
	addAttr -ci true -sn "rtup" -ln "rtup" -min 0 -at "double";
	addAttr -ci true -sn "lfdn" -ln "lfdn" -min 0 -at "double";
	addAttr -ci true -sn "rtdn" -ln "rtdn" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_up" -ln "fourAxis_up" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_dn" -ln "fourAxis_dn" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_lf" -ln "fourAxis_lf" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_rt" -ln "fourAxis_rt" -min 0 -at "double";
	addAttr -ci true -sn "up_Vis" -ln "up_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "dn_Vis" -ln "dn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lf_Vis" -ln "lf_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lfup_Vis" -ln "lfup_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rt_Vis" -ln "rt_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rtup_Vis" -ln "rtup_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lfdn_Vis" -ln "lfdn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rtdn_Vis" -ln "rtdn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_up_Vis" -ln "fourAxis_up_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_dn_Vis" -ln "fourAxis_dn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_lf_Vis" -ln "fourAxis_lf_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_rt_Vis" -ln "fourAxis_rt_Vis" -min 0 -max 1 -at "bool";
	setAttr -k on ".up";
	setAttr -k on ".dn";
	setAttr -k on ".lf";
	setAttr -k on ".rt";
	setAttr -k on ".lfup";
	setAttr -k on ".rtup";
	setAttr -k on ".lfdn";
	setAttr -k on ".rtdn";
	setAttr -k on ".fourAxis_up";
	setAttr -k on ".fourAxis_dn";
	setAttr -k on ".fourAxis_lf";
	setAttr -k on ".fourAxis_rt";
	setAttr -cb on ".up_Vis";
	setAttr -cb on ".dn_Vis";
	setAttr -cb on ".lf_Vis";
	setAttr -cb on ".lfup_Vis";
	setAttr -cb on ".rt_Vis";
	setAttr -cb on ".rtup_Vis";
	setAttr -cb on ".lfdn_Vis";
	setAttr -cb on ".rtdn_Vis";
	setAttr -cb on ".fourAxis_up_Vis";
	setAttr -cb on ".fourAxis_dn_Vis";
	setAttr -cb on ".fourAxis_lf_Vis";
	setAttr -cb on ".fourAxis_rt_Vis";
createNode nurbsCurve -n "c_uo_FRAMEShape" -p "c_uo_FRAME";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.078106160309654435 0.4222313923778267 0
		-0.078106160309654435 -0.4222313923778267 0
		1.0738189356316263 -0.4222313923778267 0
		1.0738189356316263 0.4222313923778267 0
		-0.078106160309654435 0.4222313923778267 0
		;
createNode transform -n "c_GRP_uo_CTRL" -p "c_uo_FRAME";
createNode transform -n "c_uo_CTRL" -p "c_GRP_uo_CTRL";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".mntl" -type "double3" 0 0 0 ;
	setAttr ".mxtl" -type "double3" 1 0 0 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
createNode nurbsCurve -n "c_uo_CTRLShape" -p "c_uo_CTRL";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".tw" yes;
	setAttr -s 33 ".cp[0:32]" -type "double3" 0.037387204432272829 0.027434445505788704 
		0 0.037387204432272829 0.082303336517366071 0 0.074755308724820085 0.082303336517366071 
		0 1.9100139725567e-005 0.13717222752894354 0 -0.074717108445368968 0.082303336517366071 
		0 -0.037349004152821698 0.082303336517366071 0 -0.037349004152821698 0.027434445505788704 
		0 -0.1494533170304635 0.10973778202315482 0 -0.037349004152821698 0.027434445505788704 
		0 -0.11208521273791623 0.027434445505788704 0 -0.11208521273791623 0.054868891011577409 
		0 -0.18682142132301072 0 0 -0.11208521273791623 -0.054868891011577409 0 -0.11208521273791623 
		-0.027434445505788704 0 -0.037349004152821698 -0.027434445505788704 0 -0.1494533170304635 
		-0.10973778202315482 0 -0.037349004152821698 -0.027434445505788704 0 -0.037349004152821698 
		-0.082303336517366071 0 -0.074717108445368968 -0.082303336517366071 0 1.9100139725567e-005 
		-0.13717222752894354 0 0.074755308724820085 -0.082303336517366071 0 0.037387204432272829 
		-0.082303336517366071 0 0.037387204432272829 -0.027434445505788704 0 0.14949151730991461 
		-0.10973778202315482 0 0.037387204432272829 -0.027434445505788704 0 0.11212341301736736 
		-0.027434445505788704 0 0.11212341301736736 -0.054868891011577409 0 0.18685962160246189 
		0 0 0.11212341301736736 0.054868891011577409 0 0.11212341301736736 0.027434445505788704 
		0 0.037387204432272829 0.027434445505788704 0 0.14949151730991461 0.10973778202315482 
		0 0.037387204432272829 0.027434445505788704 0;
createNode nurbsCurve -n "c_uo_CTRLShapeOrig" -p "c_uo_CTRL";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 32 0 no 3
		33 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32
		33
		-0.050000000000000003 0.050000000000000003 0
		-0.050000000000000003 0.15000000000000002 0
		-0.10000000000000001 0.15000000000000002 0
		0 0.25 0
		0.10000000000000001 0.15000000000000002 0
		0.050000000000000003 0.15000000000000002 0
		0.050000000000000003 0.050000000000000003 0
		0.20000000000000001 0.20000000000000001 0
		0.050000000000000003 0.050000000000000003 0
		0.15000000000000002 0.050000000000000003 0
		0.15000000000000002 0.10000000000000001 0
		0.25 0 0
		0.15000000000000002 -0.10000000000000001 0
		0.15000000000000002 -0.050000000000000003 0
		0.050000000000000003 -0.050000000000000003 0
		0.20000000000000001 -0.20000000000000001 0
		0.050000000000000003 -0.050000000000000003 0
		0.050000000000000003 -0.15000000000000002 0
		0.10000000000000001 -0.15000000000000002 0
		0 -0.25 0
		-0.10000000000000001 -0.15000000000000002 0
		-0.050000000000000003 -0.15000000000000002 0
		-0.050000000000000003 -0.050000000000000003 0
		-0.20000000000000001 -0.20000000000000001 0
		-0.050000000000000003 -0.050000000000000003 0
		-0.15000000000000002 -0.050000000000000003 0
		-0.15000000000000002 -0.10000000000000001 0
		-0.25 0 0
		-0.15000000000000002 0.10000000000000001 0
		-0.15000000000000002 0.050000000000000003 0
		-0.050000000000000003 0.050000000000000003 0
		-0.20000000000000001 0.20000000000000001 0
		-0.050000000000000003 0.050000000000000003 0
		;
createNode transform -n "c_uo_CTRL_up" -p "c_uo_FRAME";
	setAttr ".t" -type "double3" 0 2.2 0 ;
createNode nurbsCurve -n "cuorveShape349" -p "c_uo_CTRL_up";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_uo_LOC_up" -p "c_uo_CTRL_up";
	setAttr -k off ".v" no;
createNode transform -n "c_uo_CTRL_dn" -p "c_uo_FRAME";
	setAttr ".t" -type "double3" 0 -2.2 0 ;
createNode nurbsCurve -n "cuorveShape350" -p "c_uo_CTRL_dn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_uo_LOC_dn" -p "c_uo_CTRL_dn";
	setAttr -k off ".v" no;
createNode transform -n "c_uo_CTRL_lf" -p "c_uo_FRAME";
	setAttr ".t" -type "double3" -2.2 0 0 ;
createNode nurbsCurve -n "cuorveShape351" -p "c_uo_CTRL_lf";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_uo_LOC_lf" -p "c_uo_CTRL_lf";
	setAttr -k off ".v" no;
createNode transform -n "c_uo_CTRL_lfup" -p "c_uo_FRAME";
	setAttr ".t" -type "double3" -2.2 2.2 0 ;
createNode nurbsCurve -n "cuorveShape352" -p "c_uo_CTRL_lfup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_uo_LOC_lfup" -p "c_uo_CTRL_lfup";
	setAttr -k off ".v" no;
createNode transform -n "c_uo_CTRL_rt" -p "c_uo_FRAME";
	setAttr ".t" -type "double3" 2.2 0 0 ;
createNode nurbsCurve -n "cuorveShape353" -p "c_uo_CTRL_rt";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_uo_LOC_rt" -p "c_uo_CTRL_rt";
	setAttr -k off ".v" no;
createNode transform -n "c_uo_CTRL_rtup" -p "c_uo_FRAME";
	setAttr ".t" -type "double3" 2.2 2.2 0 ;
createNode nurbsCurve -n "cuorveShape354" -p "c_uo_CTRL_rtup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_uo_LOC_rtup" -p "c_uo_CTRL_rtup";
	setAttr -k off ".v" no;
createNode transform -n "c_uo_CTRL_lfdn" -p "c_uo_FRAME";
	setAttr ".t" -type "double3" -2.2 -2.2 0 ;
createNode nurbsCurve -n "cuorveShape355" -p "c_uo_CTRL_lfdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_uo_LOC_lfdn" -p "c_uo_CTRL_lfdn";
	setAttr -k off ".v" no;
createNode transform -n "c_uo_CTRL_rtdn" -p "c_uo_FRAME";
	setAttr ".t" -type "double3" 2.2 -2.2 0 ;
createNode nurbsCurve -n "cuorveShape356" -p "c_uo_CTRL_rtdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_uo_LOC_rtdn" -p "c_uo_CTRL_rtdn";
	setAttr -k off ".v" no;
createNode transform -n "c_uo_CTRL_fourAxisup" -p "c_uo_FRAME";
	setAttr ".t" -type "double3" 0 4.4 0 ;
createNode nurbsCurve -n "cuorveShape357" -p "c_uo_CTRL_fourAxisup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_uo_LOC_fourAxis_up" -p "c_uo_CTRL_fourAxisup";
	setAttr -k off ".v" no;
createNode transform -n "c_uo_CTRL_fourAxisdn" -p "c_uo_FRAME";
	setAttr ".t" -type "double3" 0 -4.4 0 ;
createNode nurbsCurve -n "cuorveShape358" -p "c_uo_CTRL_fourAxisdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_uo_LOC_fourAxis_dn" -p "c_uo_CTRL_fourAxisdn";
	setAttr -k off ".v" no;
createNode transform -n "c_uo_CTRL_fourAxislf" -p "c_uo_FRAME";
	setAttr ".t" -type "double3" -4.4 0 0 ;
createNode nurbsCurve -n "cuorveShape359" -p "c_uo_CTRL_fourAxislf";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_uo_LOC_fourAxis_lf" -p "c_uo_CTRL_fourAxislf";
	setAttr -k off ".v" no;
createNode transform -n "c_uo_CTRL_fourAxisrt" -p "c_uo_FRAME";
	setAttr ".t" -type "double3" 4.4 0 0 ;
createNode nurbsCurve -n "cuorveShape360" -p "c_uo_CTRL_fourAxisrt";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_uo_LOC_fourAxis_rt" -p "c_uo_CTRL_fourAxisrt";
	setAttr -k off ".v" no;
createNode transform -n "Text_Text_uo_1" -p "c_GRP_uo_FRAME";
	setAttr ".t" -type "double3" -0.61855490961115578 -0.314 -7.2381644909181395e-015 ;
	setAttr ".s" -type "double3" 0.070655207584665439 0.49458645309265803 0.49458645309265836 ;
createNode transform -n "Text_Char_uo_5" -p "Text_Text_uo_1";
createNode transform -n "Text_cuorve105" -p "Text_Char_uo_5";
	setAttr ".ovdt" 2;
createNode nurbsCurve -n "Text_cuorveShape105" -p "Text_cuorve105";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr ".cc" -type "nurbsCurve" 
		2 49 1 no 3
		52 0 0 1.1000000000000001 1.1000000000000001 2.1000000000000001 3.1000000000000001
		 4.0999999999999996 4.0999999999999996 5.0999999999999996 5.0999999999999996 5.2034674193959543
		 5.2034674193959543 5.7565205930718095 5.7565205930718095 5.8408968805517816 5.8408968805517816
		 6.1799599766073241 6.1799599766073241 7.1799599766073241 8.179959976607325 8.179959976607325
		 9.179959976607325 10.179959976607325 11.179959976607325 11.179959976607325 11.981520974547356
		 11.981520974547356 12.981520974547356 13.981520974547356 14.981520974547356 14.981520974547356
		 15.081520974547356 15.081520974547356 15.681520974547356 15.681520974547356 16.87683340302069
		 16.87683340302069 17.87683340302069 18.87683340302069 18.87683340302069 19.87683340302069
		 20.87683340302069 20.87683340302069 21.923707592385153 21.923707592385153 22.923707592385153
		 23.923707592385153 23.923707592385153 24.023707592385154 24.023707592385154 24.623707592385156
		 24.623707592385156
		51
		1.7000000000000002 1.8 0
		1.7000000000000002 1.25 0
		1.7000000000000002 0.70000000000000007 0
		1.7000000000000002 0.4359380483710994 0
		1.7296879530022125 0.31875028610666062 0
		1.7937514305333029 0.26875104905775543 0
		1.8359380483710994 0.26875104905775543 0
		1.8968764782177463 0.26875104905775543 0
		1.9734386205844208 0.30000000000000004 0
		1.9867193102922105 0.25 0
		2 0.20000000000000001 0
		1.7421881437399862 0.10000000000000001 0
		1.4843762874799726 0 0
		1.4421881437399864 0 0
		1.4000000000000001 0 0
		1.4000000000000001 0.16953154802777143 0
		1.4000000000000001 0.33906309605554286 0
		1.1625009536888686 0.11562523842221713 0
		0.910937666895552 0 0
		0.77187609674219892 0 0
		0.61718776226443894 0 0
		0.3890638590066377 0.17500114442664227 0
		0.30000000000000004 0.44843823910887315 0
		0.30000000000000004 0.69843900205996801 0
		0.30000000000000004 1.0992195010299839 0
		0.30000000000000004 1.4999999999999998 0
		0.30000000000000004 1.5921889066910813 0
		0.24531319142442973 1.6625009536888689 0
		0.13906309605554285 1.7031250476844435 0
		0 1.7000000000000002 0
		0 1.75 0
		0 1.8 0
		0.30000000000000004 1.8000000000000003 0
		0.60000000000000009 1.8000000000000003 0
		0.60000000000000009 1.2023437857633326 0
		0.60000000000000009 0.60468757152666519 0
		0.60000000000000009 0.35625085831998171 0
		0.78750133516441601 0.20000000000000001 0
		0.9203128099488822 0.20000000000000001 0
		1.0109376668955521 0.20000000000000001 0
		1.2421881437399864 0.30468757152666515 0
		1.4000000000000001 0.45312581063553825 0
		1.4000000000000001 0.97656290531776913 0
		1.4000000000000001 1.5 0
		1.4000000000000001 1.6156252384222172 0
		1.2843762874799727 1.6968764782177463 0
		1.1000000000000001 1.7000000000000002 0
		1.1000000000000001 1.75 0
		1.1000000000000001 1.8 0
		1.4000000000000001 1.8000000000000003 0
		1.7000000000000002 1.8000000000000003 0
		;
createNode transform -n "c_GRP_OU_FRAME" -p "CHR_Pier_Lips_Neutre_CTRL";
	setAttr ".t" -type "double3" -0.22338273778773066 0.486034647596569 -0.00066615460586032433 ;
	setAttr ".s" -type "double3" 1.4000000000000001 0.2 0.2 ;
createNode transform -n "c_OU_FRAME" -p "c_GRP_OU_FRAME";
	addAttr -ci true -sn "up" -ln "up" -min 0 -at "double";
	addAttr -ci true -sn "dn" -ln "dn" -min 0 -at "double";
	addAttr -ci true -sn "lf" -ln "lf" -min 0 -at "double";
	addAttr -ci true -sn "rt" -ln "rt" -min 0 -at "double";
	addAttr -ci true -sn "lfup" -ln "lfup" -min 0 -at "double";
	addAttr -ci true -sn "rtup" -ln "rtup" -min 0 -at "double";
	addAttr -ci true -sn "lfdn" -ln "lfdn" -min 0 -at "double";
	addAttr -ci true -sn "rtdn" -ln "rtdn" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_up" -ln "fourAxis_up" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_dn" -ln "fourAxis_dn" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_lf" -ln "fourAxis_lf" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_rt" -ln "fourAxis_rt" -min 0 -at "double";
	addAttr -ci true -sn "up_Vis" -ln "up_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "dn_Vis" -ln "dn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lf_Vis" -ln "lf_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lfup_Vis" -ln "lfup_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rt_Vis" -ln "rt_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rtup_Vis" -ln "rtup_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lfdn_Vis" -ln "lfdn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rtdn_Vis" -ln "rtdn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_up_Vis" -ln "fourAxis_up_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_dn_Vis" -ln "fourAxis_dn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_lf_Vis" -ln "fourAxis_lf_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_rt_Vis" -ln "fourAxis_rt_Vis" -min 0 -max 1 -at "bool";
	setAttr -k on ".up";
	setAttr -k on ".dn";
	setAttr -k on ".lf";
	setAttr -k on ".rt";
	setAttr -k on ".lfup";
	setAttr -k on ".rtup";
	setAttr -k on ".lfdn";
	setAttr -k on ".rtdn";
	setAttr -k on ".fourAxis_up";
	setAttr -k on ".fourAxis_dn";
	setAttr -k on ".fourAxis_lf";
	setAttr -k on ".fourAxis_rt";
	setAttr -cb on ".up_Vis";
	setAttr -cb on ".dn_Vis";
	setAttr -cb on ".lf_Vis";
	setAttr -cb on ".lfup_Vis";
	setAttr -cb on ".rt_Vis";
	setAttr -cb on ".rtup_Vis";
	setAttr -cb on ".lfdn_Vis";
	setAttr -cb on ".rtdn_Vis";
	setAttr -cb on ".fourAxis_up_Vis";
	setAttr -cb on ".fourAxis_dn_Vis";
	setAttr -cb on ".fourAxis_lf_Vis";
	setAttr -cb on ".fourAxis_rt_Vis";
createNode nurbsCurve -n "c_OU_FRAMEShape" -p "c_OU_FRAME";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.078106160309654435 0.4222313923778267 0
		-0.078106160309654435 -0.4222313923778267 0
		1.0738189356316263 -0.4222313923778267 0
		1.0738189356316263 0.4222313923778267 0
		-0.078106160309654435 0.4222313923778267 0
		;
createNode transform -n "c_GRP_OU_CTRL" -p "c_OU_FRAME";
createNode transform -n "c_OU_CTRL" -p "c_GRP_OU_CTRL";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".mntl" -type "double3" 0 0 0 ;
	setAttr ".mxtl" -type "double3" 1 0 0 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
createNode nurbsCurve -n "c_OU_CTRLShape" -p "c_OU_CTRL";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".tw" yes;
	setAttr -s 33 ".cp[0:32]" -type "double3" 0.037349004152821698 0.027434445505788704 
		0 0.037349004152821698 0.082303336517366127 0 0.074717108445368968 0.082303336517366127 
		0 -1.9100139725567e-005 0.13717222752894354 0 -0.074755308724820085 0.082303336517366127 
		0 -0.037387204432272829 0.082303336517366127 0 -0.037387204432272829 0.027434445505788704 
		0 -0.14949151730991461 0.10973778202315482 0 -0.037387204432272829 0.027434445505788704 
		0 -0.11212341301736736 0.027434445505788704 0 -0.11212341301736736 0.054868891011577409 
		0 -0.18685962160246189 0 0 -0.11212341301736736 -0.054868891011577409 0 -0.11212341301736736 
		-0.027434445505788704 0 -0.037387204432272829 -0.027434445505788704 0 -0.14949151730991461 
		-0.10973778202315482 0 -0.037387204432272829 -0.027434445505788704 0 -0.037387204432272829 
		-0.082303336517366127 0 -0.074755308724820085 -0.082303336517366127 0 -1.9100139725567e-005 
		-0.13717222752894354 0 0.074717108445368968 -0.082303336517366127 0 0.037349004152821698 
		-0.082303336517366127 0 0.037349004152821698 -0.027434445505788704 0 0.1494533170304635 
		-0.10973778202315482 0 0.037349004152821698 -0.027434445505788704 0 0.11208521273791623 
		-0.027434445505788704 0 0.11208521273791623 -0.054868891011577409 0 0.18682142132301072 
		0 0 0.11208521273791623 0.054868891011577409 0 0.11208521273791623 0.027434445505788704 
		0 0.037349004152821698 0.027434445505788704 0 0.1494533170304635 0.10973778202315482 
		0 0.037349004152821698 0.027434445505788704 0;
createNode nurbsCurve -n "c_OU_CTRLShapeOrig" -p "c_OU_CTRL";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 32 0 no 3
		33 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32
		33
		-0.050000000000000003 0.050000000000000003 0
		-0.050000000000000003 0.15000000000000002 0
		-0.10000000000000001 0.15000000000000002 0
		0 0.25 0
		0.10000000000000001 0.15000000000000002 0
		0.050000000000000003 0.15000000000000002 0
		0.050000000000000003 0.050000000000000003 0
		0.20000000000000001 0.20000000000000001 0
		0.050000000000000003 0.050000000000000003 0
		0.15000000000000002 0.050000000000000003 0
		0.15000000000000002 0.10000000000000001 0
		0.25 0 0
		0.15000000000000002 -0.10000000000000001 0
		0.15000000000000002 -0.050000000000000003 0
		0.050000000000000003 -0.050000000000000003 0
		0.20000000000000001 -0.20000000000000001 0
		0.050000000000000003 -0.050000000000000003 0
		0.050000000000000003 -0.15000000000000002 0
		0.10000000000000001 -0.15000000000000002 0
		0 -0.25 0
		-0.10000000000000001 -0.15000000000000002 0
		-0.050000000000000003 -0.15000000000000002 0
		-0.050000000000000003 -0.050000000000000003 0
		-0.20000000000000001 -0.20000000000000001 0
		-0.050000000000000003 -0.050000000000000003 0
		-0.15000000000000002 -0.050000000000000003 0
		-0.15000000000000002 -0.10000000000000001 0
		-0.25 0 0
		-0.15000000000000002 0.10000000000000001 0
		-0.15000000000000002 0.050000000000000003 0
		-0.050000000000000003 0.050000000000000003 0
		-0.20000000000000001 0.20000000000000001 0
		-0.050000000000000003 0.050000000000000003 0
		;
createNode transform -n "c_OU_CTRL_up" -p "c_OU_FRAME";
	setAttr ".t" -type "double3" 0 2.2 0 ;
createNode nurbsCurve -n "curveShape433" -p "c_OU_CTRL_up";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_OU_LOC_up" -p "c_OU_CTRL_up";
	setAttr -k off ".v" no;
createNode transform -n "c_OU_CTRL_dn" -p "c_OU_FRAME";
	setAttr ".t" -type "double3" 0 -2.2 0 ;
createNode nurbsCurve -n "curveShape434" -p "c_OU_CTRL_dn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_OU_LOC_dn" -p "c_OU_CTRL_dn";
	setAttr -k off ".v" no;
createNode transform -n "c_OU_CTRL_lf" -p "c_OU_FRAME";
	setAttr ".t" -type "double3" -2.2 0 0 ;
createNode nurbsCurve -n "curveShape435" -p "c_OU_CTRL_lf";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_OU_LOC_lf" -p "c_OU_CTRL_lf";
	setAttr -k off ".v" no;
createNode transform -n "c_OU_CTRL_lfup" -p "c_OU_FRAME";
	setAttr ".t" -type "double3" -2.2 2.2 0 ;
createNode nurbsCurve -n "curveShape436" -p "c_OU_CTRL_lfup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_OU_LOC_lfup" -p "c_OU_CTRL_lfup";
	setAttr -k off ".v" no;
createNode transform -n "c_OU_CTRL_rt" -p "c_OU_FRAME";
	setAttr ".t" -type "double3" 2.2 0 0 ;
createNode nurbsCurve -n "curveShape437" -p "c_OU_CTRL_rt";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_OU_LOC_rt" -p "c_OU_CTRL_rt";
	setAttr -k off ".v" no;
createNode transform -n "c_OU_CTRL_rtup" -p "c_OU_FRAME";
	setAttr ".t" -type "double3" 2.2 2.2 0 ;
createNode nurbsCurve -n "curveShape438" -p "c_OU_CTRL_rtup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_OU_LOC_rtup" -p "c_OU_CTRL_rtup";
	setAttr -k off ".v" no;
createNode transform -n "c_OU_CTRL_lfdn" -p "c_OU_FRAME";
	setAttr ".t" -type "double3" -2.2 -2.2 0 ;
createNode nurbsCurve -n "curveShape439" -p "c_OU_CTRL_lfdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_OU_LOC_lfdn" -p "c_OU_CTRL_lfdn";
	setAttr -k off ".v" no;
createNode transform -n "c_OU_CTRL_rtdn" -p "c_OU_FRAME";
	setAttr ".t" -type "double3" 2.2 -2.2 0 ;
createNode nurbsCurve -n "curveShape440" -p "c_OU_CTRL_rtdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_OU_LOC_rtdn" -p "c_OU_CTRL_rtdn";
	setAttr -k off ".v" no;
createNode transform -n "c_OU_CTRL_fourAxisup" -p "c_OU_FRAME";
	setAttr ".t" -type "double3" 0 4.4 0 ;
createNode nurbsCurve -n "curveShape441" -p "c_OU_CTRL_fourAxisup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_OU_LOC_fourAxis_up" -p "c_OU_CTRL_fourAxisup";
	setAttr -k off ".v" no;
createNode transform -n "c_OU_CTRL_fourAxisdn" -p "c_OU_FRAME";
	setAttr ".t" -type "double3" 0 -4.4 0 ;
createNode nurbsCurve -n "curveShape442" -p "c_OU_CTRL_fourAxisdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_OU_LOC_fourAxis_dn" -p "c_OU_CTRL_fourAxisdn";
	setAttr -k off ".v" no;
createNode transform -n "c_OU_CTRL_fourAxislf" -p "c_OU_FRAME";
	setAttr ".t" -type "double3" -4.4 0 0 ;
createNode nurbsCurve -n "curveShape443" -p "c_OU_CTRL_fourAxislf";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_OU_LOC_fourAxis_lf" -p "c_OU_CTRL_fourAxislf";
	setAttr -k off ".v" no;
createNode transform -n "c_OU_CTRL_fourAxisrt" -p "c_OU_FRAME";
	setAttr ".t" -type "double3" 4.4 0 0 ;
createNode nurbsCurve -n "curveShape444" -p "c_OU_CTRL_fourAxisrt";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_OU_LOC_fourAxis_rt" -p "c_OU_CTRL_fourAxisrt";
	setAttr -k off ".v" no;
createNode transform -n "Text_Text_OU_1" -p "c_GRP_OU_FRAME";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" -0.62372697151285517 -0.314 0 ;
	setAttr ".s" -type "double3" 0.056111918033179206 0.39212312502476143 0.39212312502476143 ;
createNode transform -n "Text_Char_O_2" -p "Text_Text_OU_1";
createNode transform -n "Text_OU_curve1" -p "Text_Char_O_2";
createNode nurbsCurve -n "Text_OU_curveShape1" -p "Text_OU_curve1";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		2 12 1 no 3
		15 0 0 1 2 2 3 4 4 5 6 6 7 7 8 8
		14
		1.4250003814755474 2.6000000000000001 0
		1.9421881437399862 2.6000000000000001 0
		2.7000000000000002 1.8640634775310905 0
		2.7000000000000002 1.3140627145799955 0
		2.7000000000000002 0.74843823910887319 0
		1.9359380483710993 0 0
		1.393751430533303 0 0
		0.84531319142442973 0 0
		0.10000000000000001 0.72968795300221256 0
		0.10000000000000001 1.3093751430533302 0
		0.10000000000000001 1.9015625238422218 0
		0.53125047684443427 2.2750011444266423 0
		0.90468757152666512 2.6000000000000001 0
		1.4250003814755474 2.6000000000000001 0
		;
createNode transform -n "Text_OU_curve2" -p "Text_Char_O_2";
createNode nurbsCurve -n "Text_OU_curveShape2" -p "Text_OU_curve2";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		2 14 1 no 3
		17 0 0 1 1 2 2 3 3 4 4 5 6 6 7 7 8 8
		16
		1.3875013351644161 2.5 0
		1.0109376668955521 2.5 0
		0.78281376363775079 2.2453131914244295 0
		0.5 1.9296879530022126 0
		0.5 1.3187502861066607 0
		0.5 0.6937514305333029 0
		0.79375143053330288 0.35625085831998171 0
		1.0187502861066606 0.10000000000000001 0
		1.3890638590066378 0.10000000000000001 0
		1.7843762874799727 0.10000000000000001 0
		2.3000000000000003 0.66093842984664686 0
		2.3000000000000003 1.265626001373312 0
		2.3000000000000003 1.9218753337911041 0
		2.017187762264439 2.2437506675822081 0
		1.7890638590066379 2.5 0
		1.3875013351644161 2.5 0
		;
createNode transform -n "c_GRP_fv_FRAME" -p "CHR_Pier_Lips_Neutre_CTRL";
	setAttr ".t" -type "double3" -0.22332856081272312 0.080795514917181177 -0.0006661546058598217 ;
	setAttr ".r" -type "double3" -3.5311250384401255e-030 0 0 ;
	setAttr ".s" -type "double3" 1.4000000000000001 0.20000000000000007 0.20000000000000007 ;
createNode transform -n "c_fv_FRAME" -p "c_GRP_fv_FRAME";
	addAttr -ci true -sn "up" -ln "up" -min 0 -at "double";
	addAttr -ci true -sn "dn" -ln "dn" -min 0 -at "double";
	addAttr -ci true -sn "lf" -ln "lf" -min 0 -at "double";
	addAttr -ci true -sn "rt" -ln "rt" -min 0 -at "double";
	addAttr -ci true -sn "lfup" -ln "lfup" -min 0 -at "double";
	addAttr -ci true -sn "rtup" -ln "rtup" -min 0 -at "double";
	addAttr -ci true -sn "lfdn" -ln "lfdn" -min 0 -at "double";
	addAttr -ci true -sn "rtdn" -ln "rtdn" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_up" -ln "fourAxis_up" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_dn" -ln "fourAxis_dn" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_lf" -ln "fourAxis_lf" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_rt" -ln "fourAxis_rt" -min 0 -at "double";
	addAttr -ci true -sn "up_Vis" -ln "up_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "dn_Vis" -ln "dn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lf_Vis" -ln "lf_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lfup_Vis" -ln "lfup_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rt_Vis" -ln "rt_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rtup_Vis" -ln "rtup_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lfdn_Vis" -ln "lfdn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rtdn_Vis" -ln "rtdn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_up_Vis" -ln "fourAxis_up_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_dn_Vis" -ln "fourAxis_dn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_lf_Vis" -ln "fourAxis_lf_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_rt_Vis" -ln "fourAxis_rt_Vis" -min 0 -max 1 -at "bool";
	setAttr -k on ".up";
	setAttr -k on ".dn";
	setAttr -k on ".lf";
	setAttr -k on ".rt";
	setAttr -k on ".lfup";
	setAttr -k on ".rtup";
	setAttr -k on ".lfdn";
	setAttr -k on ".rtdn";
	setAttr -k on ".fourAxis_up";
	setAttr -k on ".fourAxis_dn";
	setAttr -k on ".fourAxis_lf";
	setAttr -k on ".fourAxis_rt";
	setAttr -cb on ".up_Vis";
	setAttr -cb on ".dn_Vis";
	setAttr -cb on ".lf_Vis";
	setAttr -cb on ".lfup_Vis";
	setAttr -cb on ".rt_Vis";
	setAttr -cb on ".rtup_Vis";
	setAttr -cb on ".lfdn_Vis";
	setAttr -cb on ".rtdn_Vis";
	setAttr -cb on ".fourAxis_up_Vis";
	setAttr -cb on ".fourAxis_dn_Vis";
	setAttr -cb on ".fourAxis_lf_Vis";
	setAttr -cb on ".fourAxis_rt_Vis";
createNode nurbsCurve -n "c_fv_FRAMEShape" -p "c_fv_FRAME";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.078106160309654435 0.42223139237782875 0
		-0.078106160309654435 -0.42223139237782464 0
		1.0738189356316263 -0.42223139237782464 0
		1.0738189356316263 0.42223139237782875 0
		-0.078106160309654435 0.42223139237782875 0
		;
createNode transform -n "c_GRP_fv_CTRL" -p "c_fv_FRAME";
createNode transform -n "c_fv_CTRL" -p "c_GRP_fv_CTRL";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".mntl" -type "double3" 0 0 0 ;
	setAttr ".mxtl" -type "double3" 1 0 0 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
createNode nurbsCurve -n "c_fv_CTRLShape" -p "c_fv_CTRL";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".tw" yes;
	setAttr -s 33 ".cp[0:32]" -type "double3" 0.037387204432272829 0.027434445505786761 
		0 0.037387204432272829 0.082303336517364128 0 0.074755308724820085 0.082303336517364128 
		0 1.9100139725567e-005 0.13717222752894154 0 -0.074717108445368968 0.082303336517364128 
		0 -0.037349004152821698 0.082303336517364128 0 -0.037349004152821698 0.027434445505786761 
		0 -0.1494533170304635 0.10973778202315287 0 -0.037349004152821698 0.027434445505786761 
		0 -0.11208521273791623 0.027434445505786761 0 -0.11208521273791623 0.054868891011575494 
		0 -0.18682142132301072 -1.9493345963744493e-015 0 -0.11208521273791623 -0.054868891011579352 
		0 -0.11208521273791623 -0.027434445505790647 0 -0.037349004152821698 -0.027434445505790647 
		0 -0.1494533170304635 -0.10973778202315682 0 -0.037349004152821698 -0.027434445505790647 
		0 -0.037349004152821698 -0.082303336517367987 0 -0.074717108445368968 -0.082303336517367987 
		0 1.9100139725567e-005 -0.13717222752894548 0 0.074755308724820085 -0.082303336517367987 
		0 0.037387204432272829 -0.082303336517367987 0 0.037387204432272829 -0.027434445505790647 
		0 0.14949151730991461 -0.10973778202315682 0 0.037387204432272829 -0.027434445505790647 
		0 0.11212341301736736 -0.027434445505790647 0 0.11212341301736736 -0.054868891011579352 
		0 0.18685962160246189 -1.9493345963744493e-015 0 0.11212341301736736 0.054868891011575494 
		0 0.11212341301736736 0.027434445505786761 0 0.037387204432272829 0.027434445505786761 
		0 0.14949151730991461 0.10973778202315287 0 0.037387204432272829 0.027434445505786761 
		0;
createNode nurbsCurve -n "c_fv_CTRLShapeOrig" -p "c_fv_CTRL";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 32 0 no 3
		33 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32
		33
		-0.050000000000000003 0.050000000000000003 0
		-0.050000000000000003 0.15000000000000002 0
		-0.10000000000000001 0.15000000000000002 0
		0 0.25 0
		0.10000000000000001 0.15000000000000002 0
		0.050000000000000003 0.15000000000000002 0
		0.050000000000000003 0.050000000000000003 0
		0.20000000000000001 0.20000000000000001 0
		0.050000000000000003 0.050000000000000003 0
		0.15000000000000002 0.050000000000000003 0
		0.15000000000000002 0.10000000000000001 0
		0.25 0 0
		0.15000000000000002 -0.10000000000000001 0
		0.15000000000000002 -0.050000000000000003 0
		0.050000000000000003 -0.050000000000000003 0
		0.20000000000000001 -0.20000000000000001 0
		0.050000000000000003 -0.050000000000000003 0
		0.050000000000000003 -0.15000000000000002 0
		0.10000000000000001 -0.15000000000000002 0
		0 -0.25 0
		-0.10000000000000001 -0.15000000000000002 0
		-0.050000000000000003 -0.15000000000000002 0
		-0.050000000000000003 -0.050000000000000003 0
		-0.20000000000000001 -0.20000000000000001 0
		-0.050000000000000003 -0.050000000000000003 0
		-0.15000000000000002 -0.050000000000000003 0
		-0.15000000000000002 -0.10000000000000001 0
		-0.25 0 0
		-0.15000000000000002 0.10000000000000001 0
		-0.15000000000000002 0.050000000000000003 0
		-0.050000000000000003 0.050000000000000003 0
		-0.20000000000000001 0.20000000000000001 0
		-0.050000000000000003 0.050000000000000003 0
		;
createNode transform -n "c_fv_CTRL_up" -p "c_fv_FRAME";
	setAttr ".t" -type "double3" 0 2.2 0 ;
createNode nurbsCurve -n "curveShape361" -p "c_fv_CTRL_up";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_fv_LOC_up" -p "c_fv_CTRL_up";
	setAttr -k off ".v" no;
createNode transform -n "c_fv_CTRL_dn" -p "c_fv_FRAME";
	setAttr ".t" -type "double3" 0 -2.2 0 ;
createNode nurbsCurve -n "curveShape362" -p "c_fv_CTRL_dn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_fv_LOC_dn" -p "c_fv_CTRL_dn";
	setAttr -k off ".v" no;
createNode transform -n "c_fv_CTRL_lf" -p "c_fv_FRAME";
	setAttr ".t" -type "double3" -2.2 0 0 ;
createNode nurbsCurve -n "curveShape363" -p "c_fv_CTRL_lf";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_fv_LOC_lf" -p "c_fv_CTRL_lf";
	setAttr -k off ".v" no;
createNode transform -n "c_fv_CTRL_lfup" -p "c_fv_FRAME";
	setAttr ".t" -type "double3" -2.2 2.2 0 ;
createNode nurbsCurve -n "curveShape364" -p "c_fv_CTRL_lfup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_fv_LOC_lfup" -p "c_fv_CTRL_lfup";
	setAttr -k off ".v" no;
createNode transform -n "c_fv_CTRL_rt" -p "c_fv_FRAME";
	setAttr ".t" -type "double3" 2.2 0 0 ;
createNode nurbsCurve -n "curveShape365" -p "c_fv_CTRL_rt";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_fv_LOC_rt" -p "c_fv_CTRL_rt";
	setAttr -k off ".v" no;
createNode transform -n "c_fv_CTRL_rtup" -p "c_fv_FRAME";
	setAttr ".t" -type "double3" 2.2 2.2 0 ;
createNode nurbsCurve -n "curveShape366" -p "c_fv_CTRL_rtup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_fv_LOC_rtup" -p "c_fv_CTRL_rtup";
	setAttr -k off ".v" no;
createNode transform -n "c_fv_CTRL_lfdn" -p "c_fv_FRAME";
	setAttr ".t" -type "double3" -2.2 -2.2 0 ;
createNode nurbsCurve -n "curveShape367" -p "c_fv_CTRL_lfdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_fv_LOC_lfdn" -p "c_fv_CTRL_lfdn";
	setAttr -k off ".v" no;
createNode transform -n "c_fv_CTRL_rtdn" -p "c_fv_FRAME";
	setAttr ".t" -type "double3" 2.2 -2.2 0 ;
createNode nurbsCurve -n "curveShape368" -p "c_fv_CTRL_rtdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_fv_LOC_rtdn" -p "c_fv_CTRL_rtdn";
	setAttr -k off ".v" no;
createNode transform -n "c_fv_CTRL_fourAxisup" -p "c_fv_FRAME";
	setAttr ".t" -type "double3" 0 4.4 0 ;
createNode nurbsCurve -n "curveShape369" -p "c_fv_CTRL_fourAxisup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_fv_LOC_fourAxis_up" -p "c_fv_CTRL_fourAxisup";
	setAttr -k off ".v" no;
createNode transform -n "c_fv_CTRL_fourAxisdn" -p "c_fv_FRAME";
	setAttr ".t" -type "double3" 0 -4.4 0 ;
createNode nurbsCurve -n "curveShape370" -p "c_fv_CTRL_fourAxisdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_fv_LOC_fourAxis_dn" -p "c_fv_CTRL_fourAxisdn";
	setAttr -k off ".v" no;
createNode transform -n "c_fv_CTRL_fourAxislf" -p "c_fv_FRAME";
	setAttr ".t" -type "double3" -4.4 0 0 ;
createNode nurbsCurve -n "curveShape371" -p "c_fv_CTRL_fourAxislf";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_fv_LOC_fourAxis_lf" -p "c_fv_CTRL_fourAxislf";
	setAttr -k off ".v" no;
createNode transform -n "c_fv_CTRL_fourAxisrt" -p "c_fv_FRAME";
	setAttr ".t" -type "double3" 4.4 0 0 ;
createNode nurbsCurve -n "curveShape372" -p "c_fv_CTRL_fourAxisrt";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_fv_LOC_fourAxis_rt" -p "c_fv_CTRL_fourAxisrt";
	setAttr -k off ".v" no;
createNode transform -n "Text_Text_fxv_1" -p "c_GRP_fv_FRAME";
	setAttr ".t" -type "double3" -0.70882437862030412 -0.314 -8.0099265904992442e-015 ;
	setAttr ".r" -type "double3" 1.2722218725854073e-014 0 0 ;
	setAttr ".s" -type "double3" 0.070655207584665453 0.49458645309265814 0.49458645309265836 ;
createNode transform -n "Text_Char_f_2" -p "Text_Text_fxv_1";
createNode transform -n "Text_curve109" -p "Text_Char_f_2";
	setAttr ".ovdt" 2;
createNode nurbsCurve -n "Text_curveShape109" -p "Text_curve109";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr ".cc" -type "nurbsCurve" 
		2 58 1 no 3
		61 0 0 1.2000000000000002 1.2000000000000002 2.2000000000000002 2.2000000000000002
		 3.2000000000000002 3.2000000000000002 3.3578118562600139 3.3578118562600139 3.457811856260014
		 3.457811856260014 4.4578118562600135 4.4578118562600135 4.5578118562600132 4.5578118562600132
		 4.6296879530022119 4.6296879530022119 5.6296879530022119 6.6296879530022119 7.6296879530022119
		 7.6296879530022119 8.8296879530022121 8.8296879530022121 9.1296879530022128 9.1296879530022128
		 9.2296879530022125 9.2296879530022125 9.5296879530022132 9.5296879530022132 9.6375005722133213
		 9.6375005722133213 10.637500572213321 11.637500572213321 12.637500572213321 12.637500572213321
		 13.637500572213321 13.637500572213321 14.637500572213321 14.637500572213321 15.637500572213321
		 16.63750057221332 16.63750057221332 17.63750057221332 18.63750057221332 19.63750057221332
		 19.63750057221332 20.63750057221332 20.63750057221332 21.63750057221332 22.63750057221332
		 23.63750057221332 23.63750057221332 23.759375906004422 23.759375906004422 24.259375906004422
		 24.259375906004422 24.359375906004423 24.359375906004423 24.859375906004423 24.859375906004423
		
		60
		0.70000000000000007 1.7000000000000002 0
		0.70000000000000007 1.1000000000000001 0
		0.70000000000000007 0.5 0
		0.70000000000000007 0.25156328679331658 0
		0.7531258106355383 0.18593881132219425 0
		0.82343785763332566 0.10000000000000001 0
		0.94218814373998638 0.10000000000000001 0
		1.0210940718699932 0.10000000000000001 0
		1.1000000000000001 0.10000000000000001 0
		1.1000000000000001 0.05000000000000001 0
		1.1000000000000001 0 0
		0.60000000000000009 0 0
		0.10000000000000001 0 0
		0.10000000000000002 0.05000000000000001 0
		0.10000000000000002 0.10000000000000002 0
		0.13593804837109941 0.10000000000000001 0
		0.17187609674219884 0.10000000000000001 0
		0.24062561989776454 0.10000000000000001 0
		0.35625085831998171 0.17812619211108568 0
		0.40000000000000002 0.3093751430533303 0
		0.40000000000000002 0.5 0
		0.40000000000000002 1.1000000000000001 0
		0.40000000000000002 1.7000000000000002 0
		0.25 1.7000000000000002 0
		0.10000000000000001 1.7000000000000002 0
		0.10000000000000002 1.75 0
		0.10000000000000002 1.8 0
		0.25 1.8000000000000003 0
		0.40000000000000002 1.8000000000000003 0
		0.40000000000000002 1.8539063096055544 0
		0.40000000000000002 1.9078126192111089 0
		0.40000000000000002 2.151563286793317 0
		0.56718852521553376 2.4906263828488595 0
		0.90937514305333034 2.7000000000000002 0
		1.1234378576333257 2.7000000000000002 0
		1.3234378576333257 2.7000000000000002 0
		1.4906263828488595 2.5921889066910815 0
		1.6000000000000001 2.5203128099488823 0
		1.6000000000000001 2.4312504768444345 0
		1.6000000000000001 2.3843762874799728 0
		1.5 2.3000000000000003 0
		1.4421881437399864 2.3000000000000003 0
		1.398439002059968 2.3000000000000003 0
		1.3 2.35468833447776 0
		1.1578133821622034 2.5359380483710994 0
		1.0984390020599679 2.5687510490577559 0
		1.0390630960555429 2.6000000000000001 0
		0.965626001373312 2.6000000000000001 0
		0.87656366826886412 2.6000000000000001 0
		0.7531258106355383 2.5093751430533304 0
		0.70000000000000007 2.3187502861066607 0
		0.70000000000000007 1.9218753337911041 0
		0.70000000000000007 1.860937666895552 0
		0.70000000000000007 1.8 0
		0.95000000000000018 1.8 0
		1.2000000000000002 1.8 0
		1.2000000000000002 1.75 0
		1.2000000000000002 1.7000000000000002 0
		0.95000000000000018 1.7000000000000002 0
		0.70000000000000007 1.7000000000000002 0
		;
createNode transform -n "Text_Char_x_3" -p "Text_Text_fxv_1";
createNode transform -n "Text_curve110" -p "Text_Char_x_3";
	setAttr ".ovdt" 2;
createNode nurbsCurve -n "Text_curveShape110" -p "Text_curve110";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 2 no 3
		5 0 2.8455561668265763 3.0471186906687979 5.893168584820339 6.0931685848203392
		
		5
		1.1000000000000001 2.7000000000000002 0
		0.20156252384222173 0 0
		0 0 0
		0.90000000000000002 2.7000000000000002 0
		1.1000000000000001 2.7000000000000002 0
		;
createNode transform -n "Text_Char_v_1" -p "Text_Text_fxv_1";
createNode transform -n "Text_curve111" -p "Text_Char_v_1";
	setAttr ".ovdt" 2;
createNode nurbsCurve -n "Text_curveShape111" -p "Text_curve111";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr ".cc" -type "nurbsCurve" 
		2 44 1 no 3
		47 0 0 0.84062561989776463 0.84062561989776463 0.9406256198977645 0.9406256198977645
		 0.99375143053330284 0.99375143053330284 1.9937514305333028 2.9937514305333028 2.9937514305333028
		 3.9937514305333028 3.9937514305333028 5.1174764712859124 5.1174764712859124 6.2770991929457836
		 6.2770991929457836 7.2770991929457836 7.2770991929457836 8.2770991929457836 8.2770991929457836
		 9.2770991929457836 10.277099192945784 10.277099192945784 10.377099192945783 10.377099192945783
		 10.898974526736888 10.898974526736888 10.998974526736887 10.998974526736887 11.998974526736887
		 11.998974526736887 12.998974526736887 12.998974526736887 14.565625327688638 14.565625327688638
		 14.66718785153086 14.66718785153086 16.245258770980801 16.245258770980801 17.245258770980801
		 18.245258770980801 18.245258770980801 19.245258770980801 19.245258770980801 19.345258770980802
		 19.345258770980802
		46
		-0.054686808575570317 1.8 0
		0.36562600137331203 1.8 0
		0.78593881132219434 1.8 0
		0.78593881132219423 1.75 0
		0.78593881132219423 1.7000000000000002 0
		0.75937590600442517 1.7000000000000002 0
		0.732813000686656 1.7000000000000002 0
		0.65781338216220342 1.7000000000000002 0
		0.53906309605554292 1.6234378576333257 0
		0.53906309605554292 1.5578133821622036 0
		0.53906309605554292 1.4859388113221943 0
		0.60000000000000009 1.3890638590066378 0
		0.82500038147554744 0.8742198825055314 0
		1.0500007629510948 0.35937590600442515 0
		1.2750003814755475 0.893750667582208 0
		1.5 1.428125429159991 0
		1.5437506675822081 1.5406256198977646 0
		1.5437506675822081 1.6000000000000001 0
		1.5437506675822081 1.6281254291599909 0
		1.5296879530022127 1.6468757152666513 0
		1.5078126192111085 1.6781261921110859 0
		1.4421881437399864 1.7000000000000002 0
		1.3437506675822082 1.7000000000000002 0
		1.3437506675822082 1.75 0
		1.3437506675822082 1.8 0
		1.60468833447776 1.8 0
		1.8656260013733121 1.8 0
		1.8656260013733121 1.75 0
		1.8656260013733121 1.7000000000000002 0
		1.7656260013733123 1.6921889066910811 0
		1.7281254291599908 1.6546883344777603 0
		1.660938429846647 1.5906263828488596 0
		1.6078126192111086 1.4406256198977647 0
		1.300000762951095 0.72031280994888236 0
		0.99218890669108117 0 0
		0.9414076447699703 0 0
		0.89062638284885942 0 0
		0.57031357289997708 0.72109407186999308 0
		0.25000076295109486 1.4421881437399862 0
		0.20781261921110861 1.5453131914244298 0
		0.13125047684443428 1.6359380483710995 0
		0.07343862058442055 1.6671885252155338 0
		0.040625619897764559 1.6843762874799726 0
		-0.054686808575570317 1.7000000000000002 0
		-0.054686808575570317 1.75 0
		-0.054686808575570317 1.8 0
		;
createNode transform -n "c_GRP_the_FRAME" -p "CHR_Pier_Lips_Neutre_CTRL";
	setAttr ".t" -type "double3" -0.22332856081272312 -0.30476334335845368 -0.0006661546058598578 ;
	setAttr ".r" -type "double3" -3.5311250384401255e-030 0 0 ;
	setAttr ".s" -type "double3" 1.4000000000000001 0.20000000000000007 0.20000000000000007 ;
createNode transform -n "c_the_FRAME" -p "c_GRP_the_FRAME";
	addAttr -ci true -sn "up" -ln "up" -min 0 -at "double";
	addAttr -ci true -sn "dn" -ln "dn" -min 0 -at "double";
	addAttr -ci true -sn "lf" -ln "lf" -min 0 -at "double";
	addAttr -ci true -sn "rt" -ln "rt" -min 0 -at "double";
	addAttr -ci true -sn "lfup" -ln "lfup" -min 0 -at "double";
	addAttr -ci true -sn "rtup" -ln "rtup" -min 0 -at "double";
	addAttr -ci true -sn "lfdn" -ln "lfdn" -min 0 -at "double";
	addAttr -ci true -sn "rtdn" -ln "rtdn" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_up" -ln "fourAxis_up" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_dn" -ln "fourAxis_dn" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_lf" -ln "fourAxis_lf" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_rt" -ln "fourAxis_rt" -min 0 -at "double";
	addAttr -ci true -sn "up_Vis" -ln "up_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "dn_Vis" -ln "dn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lf_Vis" -ln "lf_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lfup_Vis" -ln "lfup_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rt_Vis" -ln "rt_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rtup_Vis" -ln "rtup_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lfdn_Vis" -ln "lfdn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rtdn_Vis" -ln "rtdn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_up_Vis" -ln "fourAxis_up_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_dn_Vis" -ln "fourAxis_dn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_lf_Vis" -ln "fourAxis_lf_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_rt_Vis" -ln "fourAxis_rt_Vis" -min 0 -max 1 -at "bool";
	setAttr -k on ".up";
	setAttr -k on ".dn";
	setAttr -k on ".lf";
	setAttr -k on ".rt";
	setAttr -k on ".lfup";
	setAttr -k on ".rtup";
	setAttr -k on ".lfdn";
	setAttr -k on ".rtdn";
	setAttr -k on ".fourAxis_up";
	setAttr -k on ".fourAxis_dn";
	setAttr -k on ".fourAxis_lf";
	setAttr -k on ".fourAxis_rt";
	setAttr -cb on ".up_Vis";
	setAttr -cb on ".dn_Vis";
	setAttr -cb on ".lf_Vis";
	setAttr -cb on ".lfup_Vis";
	setAttr -cb on ".rt_Vis";
	setAttr -cb on ".rtup_Vis";
	setAttr -cb on ".lfdn_Vis";
	setAttr -cb on ".rtdn_Vis";
	setAttr -cb on ".fourAxis_up_Vis";
	setAttr -cb on ".fourAxis_dn_Vis";
	setAttr -cb on ".fourAxis_lf_Vis";
	setAttr -cb on ".fourAxis_rt_Vis";
createNode nurbsCurve -n "c_the_FRAMEShape" -p "c_the_FRAME";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.078106160309654435 0.42223139237782875 0
		-0.078106160309654435 -0.42223139237782464 0
		1.0738189356316263 -0.42223139237782464 0
		1.0738189356316263 0.42223139237782875 0
		-0.078106160309654435 0.42223139237782875 0
		;
createNode transform -n "c_GRP_the_CTRL" -p "c_the_FRAME";
createNode transform -n "c_the_CTRL" -p "c_GRP_the_CTRL";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".mntl" -type "double3" 0 0 0 ;
	setAttr ".mxtl" -type "double3" 1 0 0 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
createNode nurbsCurve -n "c_the_CTRLShape" -p "c_the_CTRL";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".tw" yes;
	setAttr -s 33 ".cp[0:32]" -type "double3" 0.037387204432272829 0.027434445505786761 
		0 0.037387204432272829 0.082303336517364128 0 0.074755308724820085 0.082303336517364128 
		0 1.9100139725567e-005 0.13717222752894154 0 -0.074717108445368968 0.082303336517364128 
		0 -0.037349004152821698 0.082303336517364128 0 -0.037349004152821698 0.027434445505786761 
		0 -0.1494533170304635 0.10973778202315287 0 -0.037349004152821698 0.027434445505786761 
		0 -0.11208521273791623 0.027434445505786761 0 -0.11208521273791623 0.054868891011575494 
		0 -0.18682142132301072 -1.9493345963744493e-015 0 -0.11208521273791623 -0.054868891011579352 
		0 -0.11208521273791623 -0.027434445505790647 0 -0.037349004152821698 -0.027434445505790647 
		0 -0.1494533170304635 -0.10973778202315682 0 -0.037349004152821698 -0.027434445505790647 
		0 -0.037349004152821698 -0.082303336517367987 0 -0.074717108445368968 -0.082303336517367987 
		0 1.9100139725567e-005 -0.13717222752894548 0 0.074755308724820085 -0.082303336517367987 
		0 0.037387204432272829 -0.082303336517367987 0 0.037387204432272829 -0.027434445505790647 
		0 0.14949151730991461 -0.10973778202315682 0 0.037387204432272829 -0.027434445505790647 
		0 0.11212341301736736 -0.027434445505790647 0 0.11212341301736736 -0.054868891011579352 
		0 0.18685962160246189 -1.9493345963744493e-015 0 0.11212341301736736 0.054868891011575494 
		0 0.11212341301736736 0.027434445505786761 0 0.037387204432272829 0.027434445505786761 
		0 0.14949151730991461 0.10973778202315287 0 0.037387204432272829 0.027434445505786761 
		0;
createNode nurbsCurve -n "c_the_CTRLShapeOrig" -p "c_the_CTRL";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 32 0 no 3
		33 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32
		33
		-0.050000000000000003 0.050000000000000003 0
		-0.050000000000000003 0.15000000000000002 0
		-0.10000000000000001 0.15000000000000002 0
		0 0.25 0
		0.10000000000000001 0.15000000000000002 0
		0.050000000000000003 0.15000000000000002 0
		0.050000000000000003 0.050000000000000003 0
		0.20000000000000001 0.20000000000000001 0
		0.050000000000000003 0.050000000000000003 0
		0.15000000000000002 0.050000000000000003 0
		0.15000000000000002 0.10000000000000001 0
		0.25 0 0
		0.15000000000000002 -0.10000000000000001 0
		0.15000000000000002 -0.050000000000000003 0
		0.050000000000000003 -0.050000000000000003 0
		0.20000000000000001 -0.20000000000000001 0
		0.050000000000000003 -0.050000000000000003 0
		0.050000000000000003 -0.15000000000000002 0
		0.10000000000000001 -0.15000000000000002 0
		0 -0.25 0
		-0.10000000000000001 -0.15000000000000002 0
		-0.050000000000000003 -0.15000000000000002 0
		-0.050000000000000003 -0.050000000000000003 0
		-0.20000000000000001 -0.20000000000000001 0
		-0.050000000000000003 -0.050000000000000003 0
		-0.15000000000000002 -0.050000000000000003 0
		-0.15000000000000002 -0.10000000000000001 0
		-0.25 0 0
		-0.15000000000000002 0.10000000000000001 0
		-0.15000000000000002 0.050000000000000003 0
		-0.050000000000000003 0.050000000000000003 0
		-0.20000000000000001 0.20000000000000001 0
		-0.050000000000000003 0.050000000000000003 0
		;
createNode transform -n "c_the_CTRL_up" -p "c_the_FRAME";
	setAttr ".t" -type "double3" 0 2.2 0 ;
createNode nurbsCurve -n "curveShape373" -p "c_the_CTRL_up";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_the_LOC_up" -p "c_the_CTRL_up";
	setAttr -k off ".v" no;
createNode transform -n "c_the_CTRL_dn" -p "c_the_FRAME";
	setAttr ".t" -type "double3" 0 -2.2 0 ;
createNode nurbsCurve -n "curveShape374" -p "c_the_CTRL_dn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_the_LOC_dn" -p "c_the_CTRL_dn";
	setAttr -k off ".v" no;
createNode transform -n "c_the_CTRL_lf" -p "c_the_FRAME";
	setAttr ".t" -type "double3" -2.2 0 0 ;
createNode nurbsCurve -n "curveShape375" -p "c_the_CTRL_lf";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_the_LOC_lf" -p "c_the_CTRL_lf";
	setAttr -k off ".v" no;
createNode transform -n "c_the_CTRL_lfup" -p "c_the_FRAME";
	setAttr ".t" -type "double3" -2.2 2.2 0 ;
createNode nurbsCurve -n "curveShape376" -p "c_the_CTRL_lfup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_the_LOC_lfup" -p "c_the_CTRL_lfup";
	setAttr -k off ".v" no;
createNode transform -n "c_the_CTRL_rt" -p "c_the_FRAME";
	setAttr ".t" -type "double3" 2.2 0 0 ;
createNode nurbsCurve -n "curveShape377" -p "c_the_CTRL_rt";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_the_LOC_rt" -p "c_the_CTRL_rt";
	setAttr -k off ".v" no;
createNode transform -n "c_the_CTRL_rtup" -p "c_the_FRAME";
	setAttr ".t" -type "double3" 2.2 2.2 0 ;
createNode nurbsCurve -n "curveShape378" -p "c_the_CTRL_rtup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_the_LOC_rtup" -p "c_the_CTRL_rtup";
	setAttr -k off ".v" no;
createNode transform -n "c_the_CTRL_lfdn" -p "c_the_FRAME";
	setAttr ".t" -type "double3" -2.2 -2.2 0 ;
createNode nurbsCurve -n "curveShape379" -p "c_the_CTRL_lfdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_the_LOC_lfdn" -p "c_the_CTRL_lfdn";
	setAttr -k off ".v" no;
createNode transform -n "c_the_CTRL_rtdn" -p "c_the_FRAME";
	setAttr ".t" -type "double3" 2.2 -2.2 0 ;
createNode nurbsCurve -n "curveShape380" -p "c_the_CTRL_rtdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_the_LOC_rtdn" -p "c_the_CTRL_rtdn";
	setAttr -k off ".v" no;
createNode transform -n "c_the_CTRL_fourAxisup" -p "c_the_FRAME";
	setAttr ".t" -type "double3" 0 4.4 0 ;
createNode nurbsCurve -n "curveShape381" -p "c_the_CTRL_fourAxisup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_the_LOC_fourAxis_up" -p "c_the_CTRL_fourAxisup";
	setAttr -k off ".v" no;
createNode transform -n "c_the_CTRL_fourAxisdn" -p "c_the_FRAME";
	setAttr ".t" -type "double3" 0 -4.4 0 ;
createNode nurbsCurve -n "curveShape382" -p "c_the_CTRL_fourAxisdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_the_LOC_fourAxis_dn" -p "c_the_CTRL_fourAxisdn";
	setAttr -k off ".v" no;
createNode transform -n "c_the_CTRL_fourAxislf" -p "c_the_FRAME";
	setAttr ".t" -type "double3" -4.4 0 0 ;
createNode nurbsCurve -n "curveShape383" -p "c_the_CTRL_fourAxislf";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_the_LOC_fourAxis_lf" -p "c_the_CTRL_fourAxislf";
	setAttr -k off ".v" no;
createNode transform -n "c_the_CTRL_fourAxisrt" -p "c_the_FRAME";
	setAttr ".t" -type "double3" 4.4 0 0 ;
createNode nurbsCurve -n "curveShape384" -p "c_the_CTRL_fourAxisrt";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_the_LOC_fourAxis_rt" -p "c_the_CTRL_fourAxisrt";
	setAttr -k off ".v" no;
createNode transform -n "Text_Text_the_1" -p "c_GRP_the_FRAME";
	setAttr ".t" -type "double3" -0.83879860884999935 -0.314 -8.697729926581066e-015 ;
	setAttr ".r" -type "double3" 1.2722218725854073e-014 0 0 ;
	setAttr ".s" -type "double3" 0.070655207584665453 0.49458645309265814 0.49458645309265836 ;
createNode transform -n "Text_Char_t_1" -p "Text_Text_the_1";
createNode transform -n "Text_curve112" -p "Text_Char_t_1";
	setAttr ".ovdt" 2;
createNode nurbsCurve -n "Text_curveShape112" -p "Text_curve112";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr ".cc" -type "nurbsCurve" 
		2 37 1 no 3
		40 0 0 0.60000000000000031 0.60000000000000031 1.0078126192111088 1.0078126192111088
		 1.1078126192111086 1.1078126192111086 1.5156252384222171 1.5156252384222171 2.710937666895552
		 2.710937666895552 3.710937666895552 4.7109376668955516 4.7109376668955516 5.7109376668955516
		 6.7109376668955516 6.7109376668955516 6.8109376668955512 6.8109376668955512 7.8109376668955512
		 8.8109376668955512 8.8109376668955512 9.8109376668955512 10.810937666895551 11.810937666895551
		 11.810937666895551 13.026561379415579 13.026561379415579 13.32656137941558 13.32656137941558
		 13.373437094682231 13.373437094682231 14.373437094682231 15.373437094682231 15.373437094682231
		 16.373437094682231 16.373437094682231 16.473437094682232 16.473437094682232
		39
		0.60000000000000009 2.4000000000000004 0
		0.60000000000000009 2.1000000000000001 0
		0.60000000000000009 1.7999999999999998 0
		0.80390630960555431 1.8000000000000003 0
		1.0078126192111085 1.8000000000000003 0
		1.0078126192111085 1.75 0
		1.0078126192111085 1.7000000000000002 0
		0.80390630960555431 1.7000000000000002 0
		0.60000000000000009 1.7000000000000002 0
		0.60000000000000009 1.1023437857633325 0
		0.60000000000000009 0.5046875715266651 0
		0.60000000000000009 0.32500038147554744 0
		0.70000000000000007 0.20000000000000001 0
		0.77968871595330747 0.20000000000000001 0
		0.84375066758220807 0.20000000000000001 0
		0.96718852521553367 0.25000076295109486 0
		1 0.30000000000000004 0
		1.05 0.30000000000000004 0
		1.1000000000000001 0.30000000000000004 0
		1.0312504768444344 0.15000076295109485 0
		0.77968871595330747 0 0
		0.64531319142442978 0 0
		0.55625085831998167 0 0
		0.38281376363775088 0.10000000000000001 0
		0.30000000000000004 0.28750133516441595 0
		0.30000000000000004 0.48437628747997252 0
		0.30000000000000004 1.0921881437399863 0
		0.30000000000000004 1.7000000000000002 0
		0.15000000000000002 1.7000000000000002 0
		0 1.7000000000000002 0
		0 1.7234378576333258 0
		0 1.7468757152666514 0
		0.10937514305333029 1.787501335164416 0
		0.33750057221332114 1.9796887159533076 0
		0.40468757152666512 2.1234378576333257 0
		0.43906309605554289 2.1984390020599682 0
		0.5 2.4000000000000004 0
		0.55000000000000004 2.4000000000000004 0
		0.60000000000000009 2.4000000000000004 0
		;
createNode transform -n "Text_Char_h_3" -p "Text_Text_the_1";
createNode transform -n "Text_curve113" -p "Text_Char_h_3";
	setAttr ".ovdt" 2;
createNode nurbsCurve -n "Text_curveShape113" -p "Text_curve113";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr ".cc" -type "nurbsCurve" 
		2 69 1 no 3
		72 0 0 1.2359365224689098 1.2359365224689098 2.2359365224689096 3.2359365224689096
		 3.2359365224689096 4.2359365224689096 5.2359365224689096 5.2359365224689096 6.2359365224689096
		 6.2359365224689096 6.8515617608911263 6.8515617608911263 7.8515617608911263 7.8515617608911263
		 8.8515617608911263 9.8515617608911263 9.8515617608911263 9.951561760891126 9.951561760891126
		 10.851561760891126 10.851561760891126 10.951561760891126 10.951561760891126 10.993749904631112
		 10.993749904631112 11.993749904631112 12.993749904631112 12.993749904631112 13.993749904631112
		 13.993749904631112 14.626562905317769 14.626562905317769 15.626562905317769 16.626562905317769
		 17.626562905317769 17.626562905317769 18.626562905317769 19.626562905317769 19.626562905317769
		 20.571876096742198 20.571876096742198 21.571876096742198 22.571876096742198 23.571876096742198
		 23.571876096742198 23.671876096742199 23.671876096742199 24.571876096742198 24.571876096742198
		 24.671876096742199 24.671876096742199 25.671876096742199 25.671876096742199 26.671876096742199
		 27.671876096742199 27.671876096742199 29.271876096742201 29.271876096742201 30.271876096742201
		 31.271876096742201 32.271876096742204 32.271876096742204 33.271876096742204 33.271876096742204
		 33.375343907866828 33.375343907866828 33.92694201747323 33.92694201747323 34.012879302893232
		 34.012879302893232
		71
		0.60000000000000009 2.7000000000000002 0
		0.60000000000000009 2.0820317387655454 0
		0.60000000000000009 1.4640634775310903 0
		0.82500038147554733 1.6781261921110859 0
		1.0890638590066377 1.8 0
		1.2203128099488822 1.8 0
		1.3796887159533076 1.8 0
		1.606250095368887 1.6359380483710995 0
		1.660938429846647 1.4609384298466468 0
		1.7000000000000002 1.339063096055543 0
		1.7000000000000002 1.0156252384222171 0
		1.7000000000000004 0.7078126192111085 0
		1.7000000000000004 0.40000000000000002 0
		1.7000000000000002 0.24687571526665142 0
		1.7312504768444343 0.19062638284885938 0
		1.7531258106355385 0.14843823910887313 0
		1.8593759060044253 0.10000000000000001 0
		2 0.10000000000000001 0
		2 0.05000000000000001 0
		2 0 0
		1.55 0 0
		1.1000000000000001 0 0
		1.1000000000000001 0.05000000000000001 0
		1.1000000000000001 0.10000000000000002 0
		1.1210940718699933 0.10000000000000001 0
		1.1421881437399863 0.10000000000000001 0
		1.2718760967421989 0.10000000000000001 0
		1.3734386205844207 0.1687510490577554 0
		1.393751430533303 0.23437552452887772 0
		1.4000000000000001 0.26250095368886855 0
		1.4000000000000001 0.40000000000000002 0
		1.4000000000000001 0.71640650034332798 0
		1.4000000000000001 1.032813000686656 0
		1.4000000000000001 1.3250003814755473 0
		1.3343755245288778 1.5078126192111085 0
		1.1890638590066378 1.6000000000000001 0
		1.087501335164416 1.6000000000000001 0
		0.98281376363775097 1.6000000000000001 0
		0.7578133821622034 1.4984390020599681 0
		0.60000000000000009 1.3453131914244298 0
		0.60000000000000009 0.87265659571221499 0
		0.60000000000000009 0.40000000000000002 0
		0.60000000000000009 0.23437552452887772 0
		0.64218814373998634 0.15468833447775998 0
		0.7578133821622034 0.10000000000000001 0
		0.90000000000000002 0.10000000000000001 0
		0.90000000000000002 0.05000000000000001 0
		0.90000000000000002 0 0
		0.45000000000000001 0 0
		0 0 0
		0 0.05000000000000001 0
		0 0.10000000000000002 0
		0.13125047684443428 0.10000000000000001 0
		0.20625009536888683 0.132813000686656 0
		0.24843823910887314 0.15156328679331654 0
		0.30000000000000004 0.24843823910887314 0
		0.30000000000000004 0.40000000000000002 0
		0.30000000000000004 1.2 0
		0.30000000000000004 2 0
		0.30000000000000004 2.2625009536888689 0
		0.27031357289997715 2.3828137636377509 0
		0.21093766689555202 2.4296879530022126 0
		0.15937590600442514 2.4296879530022126 0
		0.11875028610666057 2.4296879530022126 0
		0.026562905317769132 2.4000000000000004 0
		0.013281452658884566 2.4500000000000002 0
		0 2.5 0
		0.25703135728999776 2.6000000000000001 0
		0.51406271457999553 2.7000000000000002 0
		0.55703135728999786 2.7000000000000002 0
		0.60000000000000009 2.7000000000000002 0
		;
createNode transform -n "Text_Char_e_5" -p "Text_Text_the_1";
createNode transform -n "Text_curve114" -p "Text_Char_e_5";
	setAttr ".ovdt" 2;
createNode nurbsCurve -n "Text_curveShape114" -p "Text_curve114";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr ".cc" -type "nurbsCurve" 
		2 22 1 no 3
		25 0 0 1 1 2 2 3 4 4 4.1062611577537087 4.1062611577537087 5.1062611577537087
		 6.1062611577537087 6.1062611577537087 7.1062611577537087 8.1062611577537087 8.1062611577537087
		 9.1062611577537087 10.106261157753709 10.106261157753709 11.106261157753709 12.106261157753709
		 12.106261157753709 13.30626115775371 13.30626115775371
		24
		0.40000000000000002 1.1000000000000001 0
		0.3968764782177463 0.72500038147554746 0
		0.58125123979552906 0.51250019073777364 0
		0.76406347753109038 0.30000000000000004 0
		1.0109376668955521 0.30000000000000004 0
		1.1750011444266424 0.30000000000000004 0
		1.4171877622644389 0.43125047684443429 0
		1.5 0.70000000000000007 0
		1.5500000000000003 0.68203173876554524 0
		1.6000000000000003 0.6640634775310903 0
		1.5593759060044252 0.36250095368886859 0
		1.1687510490577553 0 0
		0.87343862058442068 0 0
		0.55468833447776 0 0
		0.10000000000000001 0.47656366826886398 0
		0.10000000000000001 0.87812619211108578 0
		0.10000000000000001 1.3125001907377738 0
		0.56718852521553376 1.8 0
		0.91875028610666054 1.8 0
		1.2171877622644389 1.8 0
		1.6000000000000001 1.4187502861066605 0
		1.6000000000000001 1.1000000000000001 0
		1 1.1000000000000001 0
		0.40000000000000002 1.1000000000000001 0
		;
createNode transform -n "Text_curve115" -p "Text_Char_e_5";
	setAttr ".ovdt" 2;
createNode nurbsCurve -n "Text_curveShape115" -p "Text_curve115";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr ".cc" -type "nurbsCurve" 
		2 9 1 no 3
		12 0 0 0.80000000000000016 0.80000000000000016 1.8000000000000003 1.8000000000000003
		 2.8000000000000003 3.8000000000000003 3.8000000000000003 4.8000000000000007 5.8000000000000007
		 5.8000000000000007
		11
		0.40000000000000002 1.2000000000000002 0
		0.80000000000000004 1.2000000000000002 0
		1.2000000000000002 1.2000000000000002 0
		1.1906263828488595 1.3796887159533076 0
		1.1609384298466467 1.4546883344777601 0
		1.1125001907377736 1.5687510490577554 0
		0.9265629053177693 1.7000000000000002 0
		0.82500038147554733 1.7000000000000002 0
		0.66718852521553373 1.7000000000000002 0
		0.42031280994888232 1.4359380483710995 0
		0.40000000000000002 1.2000000000000002 0
		;
createNode transform -n "Text_Text_x_1" -p "Text_Text_the_1";
	setAttr ".t" -type "double3" 4.803395549848986 -0.45184965928146426 4.4966294669590237e-014 ;
	setAttr ".s" -type "double3" 1.0599610494009097 1.0599610494009095 1.0599610494009095 ;
createNode transform -n "Text_Char_x_1" -p "Text_Text_x_1";
createNode transform -n "Text_x_curve1" -p "Text_Char_x_1";
createNode nurbsCurve -n "Text_x_curveShape1" -p "Text_x_curve1";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 2 no 3
		5 0 2.8455561668265763 3.0471186906687979 5.893168584820339 6.0931685848203392
		
		5
		1.1000000000000001 2.7000000000000002 0
		0.20156252384222173 0 0
		0 0 0
		0.90000000000000002 2.7000000000000002 0
		1.1000000000000001 2.7000000000000002 0
		;
createNode transform -n "Text_Text_L_1" -p "Text_Text_the_1";
	setAttr ".t" -type "double3" 6.3656023377975925 -0.25487694048786719 0.013468921392739827 ;
	setAttr ".r" -type "double3" 1.2722218725854064e-014 0 0 ;
createNode transform -n "Text_Char_L_1" -p "Text_Text_L_1";
createNode transform -n "Text_L_curve1" -p "Text_Char_L_1";
createNode nurbsCurve -n "Text_L_curveShape1" -p "Text_L_curve1";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		2 44 1 no 3
		47 0 0 0.10077805625567643 0.10077805625567643 0.81677951285535033 0.81677951285535033
		 2.8167795128553506 2.8167795128553506 2.9167795128553506 2.9167795128553506 3.0214670843820159
		 3.0214670843820159 4.0214670843820155 4.0214670843820155 5.0214670843820155 5.0214670843820155
		 6.6214670843820151 6.6214670843820151 7.6214670843820151 7.6214670843820151 8.6214670843820151
		 8.6214670843820151 8.7261546559086796 8.7261546559086796 8.8261546559086792 8.8261546559086792
		 9.9261546559086788 9.9261546559086788 10.026154655908678 10.026154655908678 11.026154655908678
		 12.026154655908678 13.026154655908678 13.026154655908678 14.718342036697571 14.718342036697571
		 15.718342036697571 15.718342036697571 16.718342036697571 17.718342036697571 17.718342036697571
		 17.904279322117574 17.904279322117574 18.904279322117574 19.904279322117574 20.904279322117574
		 20.904279322117574
		46
		2.1000000000000001 0.70000000000000007 0
		2.1500000000000004 0.69375066758220805 0
		2.2000000000000002 0.68750133516441603 0
		2.1000000000000001 0.34375066758220801 0
		2 0 0
		1 0 0
		0 0 0
		0 0.050000000000000003 0
		0 0.10000000000000001 0
		0.052343785763332575 0.10000000000000001 0
		0.10468757152666515 0.10000000000000001 0
		0.28125123979552907 0.10000000000000001 0
		0.35625085831998171 0.2093751430533303 0
		0.40000000000000002 0.27187609674219887 0
		0.40000000000000002 0.5 0
		0.40000000000000008 1.3 0
		0.40000000000000008 2.1000000000000001 0
		0.40000000000000002 2.3500007629510948 0
		0.34218814373998629 2.4140627145799955 0
		0.26250095368886855 2.5 0
		0.10468757152666515 2.5 0
		0.052343785763332568 2.5 0
		0 2.5 0
		0 2.5499999999999998 0
		0 2.6000000000000001 0
		0.55000000000000004 2.6000000000000001 0
		1.1000000000000001 2.6000000000000001 0
		1.1000000000000001 2.5499999999999998 0
		1.1000000000000001 2.5 0
		0.90937514305333034 2.5015625238422219 0
		0.75625085831998173 2.4281254291599907 0
		0.70000000000000007 2.3140627145799955 0
		0.70000000000000007 2.1000000000000001 0
		0.70000000000000007 1.2539063096055543 0
		0.70000000000000007 0.40781261921110856 0
		0.70000000000000007 0.24375066758220801 0
		0.72968795300221256 0.18125123979552912 0
		0.7531258106355383 0.13906309605554285 0
		0.84687571526665151 0.10000000000000001 0
		1.0921889066910813 0.10000000000000001 0
		1.1851575494010835 0.10000000000000001 0
		1.2781261921110858 0.10000000000000001 0
		1.5703135728999771 0.10000000000000001 0
		1.8078126192111086 0.19531395437552457 0
		2.0031250476844433 0.43906309605554289 0
		2.1000000000000001 0.70000000000000007 0
		;
createNode transform -n "c_GRP_eeesz_FRAME" -p "CHR_Pier_Lips_Neutre_CTRL";
	setAttr ".t" -type "double3" -0.22325700193618547 -0.70038354008854486 -0.00066615460585989564 ;
	setAttr ".r" -type "double3" -3.5311250384401255e-030 0 0 ;
	setAttr ".s" -type "double3" 1.4000000000000001 0.20000000000000007 0.20000000000000007 ;
createNode transform -n "c_eeesz_FRAME" -p "c_GRP_eeesz_FRAME";
	addAttr -ci true -sn "up" -ln "up" -min 0 -at "double";
	addAttr -ci true -sn "dn" -ln "dn" -min 0 -at "double";
	addAttr -ci true -sn "lf" -ln "lf" -min 0 -at "double";
	addAttr -ci true -sn "rt" -ln "rt" -min 0 -at "double";
	addAttr -ci true -sn "lfup" -ln "lfup" -min 0 -at "double";
	addAttr -ci true -sn "rtup" -ln "rtup" -min 0 -at "double";
	addAttr -ci true -sn "lfdn" -ln "lfdn" -min 0 -at "double";
	addAttr -ci true -sn "rtdn" -ln "rtdn" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_up" -ln "fourAxis_up" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_dn" -ln "fourAxis_dn" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_lf" -ln "fourAxis_lf" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_rt" -ln "fourAxis_rt" -min 0 -at "double";
	addAttr -ci true -sn "up_Vis" -ln "up_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "dn_Vis" -ln "dn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lf_Vis" -ln "lf_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lfup_Vis" -ln "lfup_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rt_Vis" -ln "rt_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rtup_Vis" -ln "rtup_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lfdn_Vis" -ln "lfdn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rtdn_Vis" -ln "rtdn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_up_Vis" -ln "fourAxis_up_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_dn_Vis" -ln "fourAxis_dn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_lf_Vis" -ln "fourAxis_lf_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_rt_Vis" -ln "fourAxis_rt_Vis" -min 0 -max 1 -at "bool";
	setAttr -k on ".up";
	setAttr -k on ".dn";
	setAttr -k on ".lf";
	setAttr -k on ".rt";
	setAttr -k on ".lfup";
	setAttr -k on ".rtup";
	setAttr -k on ".lfdn";
	setAttr -k on ".rtdn";
	setAttr -k on ".fourAxis_up";
	setAttr -k on ".fourAxis_dn";
	setAttr -k on ".fourAxis_lf";
	setAttr -k on ".fourAxis_rt";
	setAttr -cb on ".up_Vis";
	setAttr -cb on ".dn_Vis";
	setAttr -cb on ".lf_Vis";
	setAttr -cb on ".lfup_Vis";
	setAttr -cb on ".rt_Vis";
	setAttr -cb on ".rtup_Vis";
	setAttr -cb on ".lfdn_Vis";
	setAttr -cb on ".rtdn_Vis";
	setAttr -cb on ".fourAxis_up_Vis";
	setAttr -cb on ".fourAxis_dn_Vis";
	setAttr -cb on ".fourAxis_lf_Vis";
	setAttr -cb on ".fourAxis_rt_Vis";
createNode nurbsCurve -n "c_eeesz_FRAMEShape" -p "c_eeesz_FRAME";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.078106160309654435 0.42223139237782875 0
		-0.078106160309654435 -0.42223139237782464 0
		1.0738189356316263 -0.42223139237782464 0
		1.0738189356316263 0.42223139237782875 0
		-0.078106160309654435 0.42223139237782875 0
		;
createNode transform -n "c_GRP_eeesz_CTRL" -p "c_eeesz_FRAME";
createNode transform -n "c_eeesz_CTRL" -p "c_GRP_eeesz_CTRL";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".mntl" -type "double3" 0 0 0 ;
	setAttr ".mxtl" -type "double3" 1 0 0 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
createNode nurbsCurve -n "c_eeesz_CTRLShape" -p "c_eeesz_CTRL";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".tw" yes;
	setAttr -s 33 ".cp[0:32]" -type "double3" 0.037349004152821698 0.027434445505786761 
		0 0.037349004152821698 0.082303336517364128 0 0.074717108445368968 0.082303336517364128 
		0 -1.9100139725567e-005 0.13717222752894154 0 -0.074755308724820085 0.082303336517364128 
		0 -0.037387204432272829 0.082303336517364128 0 -0.037387204432272829 0.027434445505786761 
		0 -0.14949151730991461 0.10973778202315287 0 -0.037387204432272829 0.027434445505786761 
		0 -0.11212341301736736 0.027434445505786761 0 -0.11212341301736736 0.054868891011575494 
		0 -0.18685962160246189 -1.9493345963744493e-015 0 -0.11212341301736736 -0.054868891011579352 
		0 -0.11212341301736736 -0.027434445505790647 0 -0.037387204432272829 -0.027434445505790647 
		0 -0.14949151730991461 -0.10973778202315682 0 -0.037387204432272829 -0.027434445505790647 
		0 -0.037387204432272829 -0.082303336517367987 0 -0.074755308724820085 -0.082303336517367987 
		0 -1.9100139725567e-005 -0.13717222752894548 0 0.074717108445368968 -0.082303336517367987 
		0 0.037349004152821698 -0.082303336517367987 0 0.037349004152821698 -0.027434445505790647 
		0 0.1494533170304635 -0.10973778202315682 0 0.037349004152821698 -0.027434445505790647 
		0 0.11208521273791623 -0.027434445505790647 0 0.11208521273791623 -0.054868891011579352 
		0 0.18682142132301072 -1.9493345963744493e-015 0 0.11208521273791623 0.054868891011575494 
		0 0.11208521273791623 0.027434445505786761 0 0.037349004152821698 0.027434445505786761 
		0 0.1494533170304635 0.10973778202315287 0 0.037349004152821698 0.027434445505786761 
		0;
createNode nurbsCurve -n "c_eeesz_CTRLShapeOrig" -p "c_eeesz_CTRL";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 32 0 no 3
		33 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32
		33
		-0.050000000000000003 0.050000000000000003 0
		-0.050000000000000003 0.15000000000000002 0
		-0.10000000000000001 0.15000000000000002 0
		0 0.25 0
		0.10000000000000001 0.15000000000000002 0
		0.050000000000000003 0.15000000000000002 0
		0.050000000000000003 0.050000000000000003 0
		0.20000000000000001 0.20000000000000001 0
		0.050000000000000003 0.050000000000000003 0
		0.15000000000000002 0.050000000000000003 0
		0.15000000000000002 0.10000000000000001 0
		0.25 0 0
		0.15000000000000002 -0.10000000000000001 0
		0.15000000000000002 -0.050000000000000003 0
		0.050000000000000003 -0.050000000000000003 0
		0.20000000000000001 -0.20000000000000001 0
		0.050000000000000003 -0.050000000000000003 0
		0.050000000000000003 -0.15000000000000002 0
		0.10000000000000001 -0.15000000000000002 0
		0 -0.25 0
		-0.10000000000000001 -0.15000000000000002 0
		-0.050000000000000003 -0.15000000000000002 0
		-0.050000000000000003 -0.050000000000000003 0
		-0.20000000000000001 -0.20000000000000001 0
		-0.050000000000000003 -0.050000000000000003 0
		-0.15000000000000002 -0.050000000000000003 0
		-0.15000000000000002 -0.10000000000000001 0
		-0.25 0 0
		-0.15000000000000002 0.10000000000000001 0
		-0.15000000000000002 0.050000000000000003 0
		-0.050000000000000003 0.050000000000000003 0
		-0.20000000000000001 0.20000000000000001 0
		-0.050000000000000003 0.050000000000000003 0
		;
createNode transform -n "c_eeesz_CTRL_up" -p "c_eeesz_FRAME";
	setAttr ".t" -type "double3" 0 2.2 0 ;
createNode nurbsCurve -n "curveShape385" -p "c_eeesz_CTRL_up";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_eeesz_LOC_up" -p "c_eeesz_CTRL_up";
	setAttr -k off ".v" no;
createNode transform -n "c_eeesz_CTRL_dn" -p "c_eeesz_FRAME";
	setAttr ".t" -type "double3" 0 -2.2 0 ;
createNode nurbsCurve -n "curveShape386" -p "c_eeesz_CTRL_dn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_eeesz_LOC_dn" -p "c_eeesz_CTRL_dn";
	setAttr -k off ".v" no;
createNode transform -n "c_eeesz_CTRL_lf" -p "c_eeesz_FRAME";
	setAttr ".t" -type "double3" -2.2 0 0 ;
createNode nurbsCurve -n "curveShape387" -p "c_eeesz_CTRL_lf";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_eeesz_LOC_lf" -p "c_eeesz_CTRL_lf";
	setAttr -k off ".v" no;
createNode transform -n "c_eeesz_CTRL_lfup" -p "c_eeesz_FRAME";
	setAttr ".t" -type "double3" -2.2 2.2 0 ;
createNode nurbsCurve -n "curveShape388" -p "c_eeesz_CTRL_lfup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_eeesz_LOC_lfup" -p "c_eeesz_CTRL_lfup";
	setAttr -k off ".v" no;
createNode transform -n "c_eeesz_CTRL_rt" -p "c_eeesz_FRAME";
	setAttr ".t" -type "double3" 2.2 0 0 ;
createNode nurbsCurve -n "curveShape389" -p "c_eeesz_CTRL_rt";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_eeesz_LOC_rt" -p "c_eeesz_CTRL_rt";
	setAttr -k off ".v" no;
createNode transform -n "c_eeesz_CTRL_rtup" -p "c_eeesz_FRAME";
	setAttr ".t" -type "double3" 2.2 2.2 0 ;
createNode nurbsCurve -n "curveShape390" -p "c_eeesz_CTRL_rtup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_eeesz_LOC_rtup" -p "c_eeesz_CTRL_rtup";
	setAttr -k off ".v" no;
createNode transform -n "c_eeesz_CTRL_lfdn" -p "c_eeesz_FRAME";
	setAttr ".t" -type "double3" -2.2 -2.2 0 ;
createNode nurbsCurve -n "curveShape391" -p "c_eeesz_CTRL_lfdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_eeesz_LOC_lfdn" -p "c_eeesz_CTRL_lfdn";
	setAttr -k off ".v" no;
createNode transform -n "c_eeesz_CTRL_rtdn" -p "c_eeesz_FRAME";
	setAttr ".t" -type "double3" 2.2 -2.2 0 ;
createNode nurbsCurve -n "curveShape392" -p "c_eeesz_CTRL_rtdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_eeesz_LOC_rtdn" -p "c_eeesz_CTRL_rtdn";
	setAttr -k off ".v" no;
createNode transform -n "c_eeesz_CTRL_fourAxisup" -p "c_eeesz_FRAME";
	setAttr ".t" -type "double3" 0 4.4 0 ;
createNode nurbsCurve -n "curveShape393" -p "c_eeesz_CTRL_fourAxisup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_eeesz_LOC_fourAxis_up" -p "c_eeesz_CTRL_fourAxisup";
	setAttr -k off ".v" no;
createNode transform -n "c_eeesz_CTRL_fourAxisdn" -p "c_eeesz_FRAME";
	setAttr ".t" -type "double3" 0 -4.4 0 ;
createNode nurbsCurve -n "curveShape394" -p "c_eeesz_CTRL_fourAxisdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_eeesz_LOC_fourAxis_dn" -p "c_eeesz_CTRL_fourAxisdn";
	setAttr -k off ".v" no;
createNode transform -n "c_eeesz_CTRL_fourAxislf" -p "c_eeesz_FRAME";
	setAttr ".t" -type "double3" -4.4 0 0 ;
createNode nurbsCurve -n "curveShape395" -p "c_eeesz_CTRL_fourAxislf";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_eeesz_LOC_fourAxis_lf" -p "c_eeesz_CTRL_fourAxislf";
	setAttr -k off ".v" no;
createNode transform -n "c_eeesz_CTRL_fourAxisrt" -p "c_eeesz_FRAME";
	setAttr ".t" -type "double3" 4.4 0 0 ;
createNode nurbsCurve -n "curveShape396" -p "c_eeesz_CTRL_fourAxisrt";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_eeesz_LOC_fourAxis_rt" -p "c_eeesz_CTRL_fourAxisrt";
	setAttr -k off ".v" no;
createNode transform -n "Text_Text_eeexsxz_1" -p "c_GRP_eeesz_FRAME";
	setAttr ".t" -type "double3" -0.86729855940926215 -0.31400000000001121 -9.2086273694416068e-015 ;
	setAttr ".r" -type "double3" 1.2722218725854073e-014 0 0 ;
	setAttr ".s" -type "double3" 0.070656095642445294 0.494592669497117 0.49459266949711722 ;
createNode transform -n "Text_Char_e_6" -p "Text_Text_eeexsxz_1";
createNode transform -n "Text_curve116" -p "Text_Char_e_6";
	setAttr ".ovdt" 2;
createNode nurbsCurve -n "Text_curveShape116" -p "Text_curve116";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr ".cc" -type "nurbsCurve" 
		2 22 1 no 3
		25 0 0 1 1 2 2 3 4 4 4.1062611577537087 4.1062611577537087 5.1062611577537087
		 6.1062611577537087 6.1062611577537087 7.1062611577537087 8.1062611577537087 8.1062611577537087
		 9.1062611577537087 10.106261157753709 10.106261157753709 11.106261157753709 12.106261157753709
		 12.106261157753709 13.30626115775371 13.30626115775371
		24
		0.40000000000000002 1.1000000000000001 0
		0.3968764782177463 0.72500038147554746 0
		0.58125123979552906 0.51250019073777364 0
		0.76406347753109038 0.30000000000000004 0
		1.0109376668955521 0.30000000000000004 0
		1.1750011444266424 0.30000000000000004 0
		1.4171877622644389 0.43125047684443429 0
		1.5 0.70000000000000007 0
		1.5500000000000003 0.68203173876554524 0
		1.6000000000000003 0.6640634775310903 0
		1.5593759060044252 0.36250095368886859 0
		1.1687510490577553 0 0
		0.87343862058442068 0 0
		0.55468833447776 0 0
		0.10000000000000001 0.47656366826886398 0
		0.10000000000000001 0.87812619211108578 0
		0.10000000000000001 1.3125001907377738 0
		0.56718852521553376 1.8 0
		0.91875028610666054 1.8 0
		1.2171877622644389 1.8 0
		1.6000000000000001 1.4187502861066605 0
		1.6000000000000001 1.1000000000000001 0
		1 1.1000000000000001 0
		0.40000000000000002 1.1000000000000001 0
		;
createNode transform -n "Text_curve117" -p "Text_Char_e_6";
	setAttr ".ovdt" 2;
createNode nurbsCurve -n "Text_curveShape117" -p "Text_curve117";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr ".cc" -type "nurbsCurve" 
		2 9 1 no 3
		12 0 0 0.80000000000000016 0.80000000000000016 1.8000000000000003 1.8000000000000003
		 2.8000000000000003 3.8000000000000003 3.8000000000000003 4.8000000000000007 5.8000000000000007
		 5.8000000000000007
		11
		0.40000000000000002 1.2000000000000002 0
		0.80000000000000004 1.2000000000000002 0
		1.2000000000000002 1.2000000000000002 0
		1.1906263828488595 1.3796887159533076 0
		1.1609384298466467 1.4546883344777601 0
		1.1125001907377736 1.5687510490577554 0
		0.9265629053177693 1.7000000000000002 0
		0.82500038147554733 1.7000000000000002 0
		0.66718852521553373 1.7000000000000002 0
		0.42031280994888232 1.4359380483710995 0
		0.40000000000000002 1.2000000000000002 0
		;
createNode transform -n "Text_Char_e_7" -p "Text_Text_eeexsxz_1";
createNode transform -n "Text_curve118" -p "Text_Char_e_7";
	setAttr ".ovdt" 2;
createNode nurbsCurve -n "Text_curveShape118" -p "Text_curve118";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr ".cc" -type "nurbsCurve" 
		2 22 1 no 3
		25 0 0 1 1 2 2 3 4 4 4.1062611577537087 4.1062611577537087 5.1062611577537087
		 6.1062611577537087 6.1062611577537087 7.1062611577537087 8.1062611577537087 8.1062611577537087
		 9.1062611577537087 10.106261157753709 10.106261157753709 11.106261157753709 12.106261157753709
		 12.106261157753709 13.30626115775371 13.30626115775371
		24
		0.40000000000000002 1.1000000000000001 0
		0.3968764782177463 0.72500038147554746 0
		0.58125123979552906 0.51250019073777364 0
		0.76406347753109038 0.30000000000000004 0
		1.0109376668955521 0.30000000000000004 0
		1.1750011444266424 0.30000000000000004 0
		1.4171877622644389 0.43125047684443429 0
		1.5 0.70000000000000007 0
		1.5500000000000003 0.68203173876554524 0
		1.6000000000000003 0.6640634775310903 0
		1.5593759060044252 0.36250095368886859 0
		1.1687510490577553 0 0
		0.87343862058442068 0 0
		0.55468833447776 0 0
		0.10000000000000001 0.47656366826886398 0
		0.10000000000000001 0.87812619211108578 0
		0.10000000000000001 1.3125001907377738 0
		0.56718852521553376 1.8 0
		0.91875028610666054 1.8 0
		1.2171877622644389 1.8 0
		1.6000000000000001 1.4187502861066605 0
		1.6000000000000001 1.1000000000000001 0
		1 1.1000000000000001 0
		0.40000000000000002 1.1000000000000001 0
		;
createNode transform -n "Text_curve119" -p "Text_Char_e_7";
	setAttr ".ovdt" 2;
createNode nurbsCurve -n "Text_curveShape119" -p "Text_curve119";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr ".cc" -type "nurbsCurve" 
		2 9 1 no 3
		12 0 0 0.80000000000000016 0.80000000000000016 1.8000000000000003 1.8000000000000003
		 2.8000000000000003 3.8000000000000003 3.8000000000000003 4.8000000000000007 5.8000000000000007
		 5.8000000000000007
		11
		0.40000000000000002 1.2000000000000002 0
		0.80000000000000004 1.2000000000000002 0
		1.2000000000000002 1.2000000000000002 0
		1.1906263828488595 1.3796887159533076 0
		1.1609384298466467 1.4546883344777601 0
		1.1125001907377736 1.5687510490577554 0
		0.9265629053177693 1.7000000000000002 0
		0.82500038147554733 1.7000000000000002 0
		0.66718852521553373 1.7000000000000002 0
		0.42031280994888232 1.4359380483710995 0
		0.40000000000000002 1.2000000000000002 0
		;
createNode transform -n "Text_Char_e_8" -p "Text_Text_eeexsxz_1";
createNode transform -n "Text_curve120" -p "Text_Char_e_8";
	setAttr ".ovdt" 2;
createNode nurbsCurve -n "Text_curveShape120" -p "Text_curve120";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr ".cc" -type "nurbsCurve" 
		2 22 1 no 3
		25 0 0 1 1 2 2 3 4 4 4.1062611577537087 4.1062611577537087 5.1062611577537087
		 6.1062611577537087 6.1062611577537087 7.1062611577537087 8.1062611577537087 8.1062611577537087
		 9.1062611577537087 10.106261157753709 10.106261157753709 11.106261157753709 12.106261157753709
		 12.106261157753709 13.30626115775371 13.30626115775371
		24
		0.40000000000000002 1.1000000000000001 0
		0.3968764782177463 0.72500038147554746 0
		0.58125123979552906 0.51250019073777364 0
		0.76406347753109038 0.30000000000000004 0
		1.0109376668955521 0.30000000000000004 0
		1.1750011444266424 0.30000000000000004 0
		1.4171877622644389 0.43125047684443429 0
		1.5 0.70000000000000007 0
		1.5500000000000003 0.68203173876554524 0
		1.6000000000000003 0.6640634775310903 0
		1.5593759060044252 0.36250095368886859 0
		1.1687510490577553 0 0
		0.87343862058442068 0 0
		0.55468833447776 0 0
		0.10000000000000001 0.47656366826886398 0
		0.10000000000000001 0.87812619211108578 0
		0.10000000000000001 1.3125001907377738 0
		0.56718852521553376 1.8 0
		0.91875028610666054 1.8 0
		1.2171877622644389 1.8 0
		1.6000000000000001 1.4187502861066605 0
		1.6000000000000001 1.1000000000000001 0
		1 1.1000000000000001 0
		0.40000000000000002 1.1000000000000001 0
		;
createNode transform -n "Text_curve121" -p "Text_Char_e_8";
	setAttr ".ovdt" 2;
createNode nurbsCurve -n "Text_curveShape121" -p "Text_curve121";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr ".cc" -type "nurbsCurve" 
		2 9 1 no 3
		12 0 0 0.80000000000000016 0.80000000000000016 1.8000000000000003 1.8000000000000003
		 2.8000000000000003 3.8000000000000003 3.8000000000000003 4.8000000000000007 5.8000000000000007
		 5.8000000000000007
		11
		0.40000000000000002 1.2000000000000002 0
		0.80000000000000004 1.2000000000000002 0
		1.2000000000000002 1.2000000000000002 0
		1.1906263828488595 1.3796887159533076 0
		1.1609384298466467 1.4546883344777601 0
		1.1125001907377736 1.5687510490577554 0
		0.9265629053177693 1.7000000000000002 0
		0.82500038147554733 1.7000000000000002 0
		0.66718852521553373 1.7000000000000002 0
		0.42031280994888232 1.4359380483710995 0
		0.40000000000000002 1.2000000000000002 0
		;
createNode transform -n "Text_Char_x_4" -p "Text_Text_eeexsxz_1";
createNode transform -n "Text_curve122" -p "Text_Char_x_4";
	setAttr ".ovdt" 2;
createNode nurbsCurve -n "Text_curveShape122" -p "Text_curve122";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 2 no 3
		5 0 2.8455561668265763 3.0471186906687979 5.893168584820339 6.0931685848203392
		
		5
		1.1000000000000001 2.7000000000000002 0
		0.20156252384222173 0 0
		0 0 0
		0.90000000000000002 2.7000000000000002 0
		1.1000000000000001 2.7000000000000002 0
		;
createNode transform -n "Text_Char_s_3" -p "Text_Text_eeexsxz_1";
createNode transform -n "Text_curve123" -p "Text_Char_s_3";
	setAttr ".ovdt" 2;
createNode nurbsCurve -n "Text_curveShape123" -p "Text_curve123";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr ".cc" -type "nurbsCurve" 
		2 56 1 no 3
		59 0 0 0.59999999999999987 0.59999999999999987 0.69999999999999973 0.69999999999999973
		 1.6999999999999997 2.6999999999999997 2.6999999999999997 3.6999999999999997 4.6999999999999993
		 4.6999999999999993 5.6999999999999993 5.6999999999999993 6.6999999999999993 6.6999999999999993
		 7.0117020743554583 7.0117020743554583 8.0117020743554583 8.0117020743554583 9.0117020743554583
		 10.011702074355458 10.011702074355458 11.011702074355458 11.011702074355458 12.011702074355458
		 12.011702074355458 13.011702074355458 13.011702074355458 13.111702074355458 13.111702074355458
		 13.711702074355458 13.711702074355458 13.811702074355457 13.811702074355457 14.811702074355457
		 15.811702074355457 15.811702074355457 16.811702074355459 17.811702074355459 17.811702074355459
		 18.811702074355459 19.811702074355459 20.811702074355459 20.811702074355459 21.811702074355459
		 21.811702074355459 22.811702074355459 23.811702074355459 23.811702074355459 24.811702074355459
		 24.811702074355459 25.811702074355459 25.811702074355459 26.811702074355459 27.811702074355459
		 27.811702074355459 27.91170207435546 27.91170207435546
		58
		1.3 1.8 0
		1.3 1.5 0
		1.3 1.2000000000000002 0
		1.25 1.2000000000000002 0
		1.2000000000000002 1.2000000000000002 0
		1.1250003814755474 1.4906263828488595 0
		0.89062638284885942 1.7000000000000002 0
		0.70781261921110861 1.7000000000000002 0
		0.57031357289997719 1.7000000000000002 0
		0.40000000000000002 1.5609384298466469 0
		0.40000000000000002 1.4765636682688641 0
		0.40000000000000002 1.3718760967421988 0
		0.47500114442664226 1.2968764782177464 0
		0.54687571526665146 1.2203128099488822 0
		0.72968795300221256 1.1343755245288778 0
		0.87031280994888238 1.0671877622644388 0
		1.0109376668955521 1 0
		1.4000000000000001 0.81562523842221712 0
		1.4000000000000001 0.51562523842221719 0
		1.4000000000000001 0.28437628747997257 0
		1.0468757152666515 0 0
		0.82812542915999099 0 0
		0.67031357289997717 0 0
		0.46875104905775544 0.075001144426642255 0
		0.40625009536888684 0.10000000000000001 0
		0.36718852521553375 0.10000000000000001 0
		0.32500038147554744 0.10000000000000001 0
		0.30000000000000004 0 0
		0.25 0 0
		0.20000000000000001 0 0
		0.20000000000000001 0.30000000000000004 0
		0.20000000000000001 0.60000000000000009 0
		0.25 0.60000000000000009 0
		0.30000000000000004 0.60000000000000009 0
		0.35156328679331655 0.35156328679331655 0
		0.63750057221332124 0.10000000000000001 0
		0.81562523842221712 0.10000000000000001 0
		0.94218814373998638 0.10000000000000001 0
		1.1000000000000001 0.26250095368886855 0
		1.1000000000000001 0.376563668268864 0
		1.1000000000000001 0.51562523842221719 0
		0.94843823910887315 0.70468757152666517 0
		0.39062638284885942 0.97031357289997711 0
		0.29531395437552455 1.0734386205844206 0
		0.20000000000000001 1.1750011444266424 0
		0.20000000000000001 1.3296879530022128 0
		0.20000000000000001 1.5296879530022127 0
		0.49687647821774628 1.8 0
		0.73125047684443434 1.8 0
		0.83437552452887775 1.8 0
		0.9812512397955292 1.7390630960555429 0
		1.0796887159533075 1.7000000000000002 0
		1.1125001907377736 1.7000000000000002 0
		1.1421881437399863 1.7000000000000002 0
		1.176563668268864 1.737500572213321 0
		1.2000000000000002 1.8 0
		1.25 1.8 0
		1.3 1.8 0
		;
createNode transform -n "Text_Char_x_5" -p "Text_Text_eeexsxz_1";
createNode transform -n "Text_curve124" -p "Text_Char_x_5";
	setAttr ".ovdt" 2;
createNode nurbsCurve -n "Text_curveShape124" -p "Text_curve124";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 2 no 3
		5 0 2.8455561668265763 3.0471186906687979 5.893168584820339 6.0931685848203392
		
		5
		1.1000000000000001 2.7000000000000002 0
		0.20156252384222173 0 0
		0 0 0
		0.90000000000000002 2.7000000000000002 0
		1.1000000000000001 2.7000000000000002 0
		;
createNode transform -n "Text_Char_z_1" -p "Text_Text_eeexsxz_1";
createNode transform -n "Text_curve125" -p "Text_Char_z_1";
	setAttr ".ovdt" 2;
createNode nurbsCurve -n "Text_curveShape125" -p "Text_curve125";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr ".cc" -type "nurbsCurve" 
		2 33 1 no 3
		36 0 0 0.5 0.5 2.1000000000000001 2.1000000000000001 2.1531258106355384 2.1531258106355384
		 4.2009882679800654 4.2009882679800654 4.818176030244504 4.818176030244504 5.818176030244504
		 6.818176030244504 6.818176030244504 7.818176030244504 7.818176030244504 7.9181760302445037
		 7.9181760302445037 8.3181760302445031 8.3181760302445031 9.8181760302445031 9.8181760302445031
		 9.8713003149778515 9.8713003149778515 11.919163092491214 11.919163092491214 12.636349328853463
		 12.636349328853463 13.636349328853463 14.636349328853463 14.636349328853463 15.636349328853463
		 15.636349328853463 15.736349328853462 15.736349328853462
		35
		1.6000000000000001 0.5 0
		1.6000000000000001 0.25 0
		1.6000000000000001 0 0
		0.80000000000000016 0 0
		0 0 0
		0 0.026562905317769132 0
		0 0.053125810635538263 0
		0.60859388113221946 0.87656290531776926 0
		1.2171877622644389 1.7000000000000002 0
		0.90859388113221951 1.7000000000000002 0
		0.60000000000000009 1.7000000000000002 0
		0.41250019073777366 1.7000000000000002 0
		0.29687647821774626 1.6593759060044253 0
		0.25937590600442512 1.6015625238422218 0
		0.20781261921110861 1.5203128099488823 0
		0.20000000000000001 1.4000000000000001 0
		0.15000000000000002 1.4000000000000001 0
		0.10000000000000002 1.4000000000000001 0
		0.10000000000000001 1.6000000000000001 0
		0.10000000000000001 1.8 0
		0.8500000000000002 1.8 0
		1.6000000000000003 1.8 0
		1.6000000000000001 1.7734378576333258 0
		1.6000000000000001 1.7468757152666514 0
		0.99140688181887549 0.92343785763332575 0
		0.38281376363775088 0.10000000000000001 0
		0.74140688181887549 0.10000000000000001 0
		1.1000000000000001 0.10000000000000001 0
		1.282813763637751 0.10000000000000001 0
		1.4125001907377737 0.16562600137331196 0
		1.4531258106355383 0.24843823910887314 0
		1.4812512397955293 0.30781261921110858 0
		1.5 0.5 0
		1.55 0.5 0
		1.6000000000000001 0.5 0
		;
createNode transform -n "c_GRP_mbp_FRAME" -p "CHR_Pier_Lips_Neutre_CTRL";
	setAttr ".t" -type "double3" -0.22325700193618681 -1.0901709717696679 -0.00066615460585993304 ;
	setAttr ".r" -type "double3" -3.5311250384401255e-030 0 0 ;
	setAttr ".s" -type "double3" 1.4000000000000001 0.20000000000000007 0.20000000000000007 ;
createNode transform -n "c_mbp_FRAME" -p "c_GRP_mbp_FRAME";
	addAttr -ci true -sn "up" -ln "up" -min 0 -at "double";
	addAttr -ci true -sn "dn" -ln "dn" -min 0 -at "double";
	addAttr -ci true -sn "lf" -ln "lf" -min 0 -at "double";
	addAttr -ci true -sn "rt" -ln "rt" -min 0 -at "double";
	addAttr -ci true -sn "lfup" -ln "lfup" -min 0 -at "double";
	addAttr -ci true -sn "rtup" -ln "rtup" -min 0 -at "double";
	addAttr -ci true -sn "lfdn" -ln "lfdn" -min 0 -at "double";
	addAttr -ci true -sn "rtdn" -ln "rtdn" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_up" -ln "fourAxis_up" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_dn" -ln "fourAxis_dn" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_lf" -ln "fourAxis_lf" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_rt" -ln "fourAxis_rt" -min 0 -at "double";
	addAttr -ci true -sn "up_Vis" -ln "up_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "dn_Vis" -ln "dn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lf_Vis" -ln "lf_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lfup_Vis" -ln "lfup_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rt_Vis" -ln "rt_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rtup_Vis" -ln "rtup_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lfdn_Vis" -ln "lfdn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rtdn_Vis" -ln "rtdn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_up_Vis" -ln "fourAxis_up_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_dn_Vis" -ln "fourAxis_dn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_lf_Vis" -ln "fourAxis_lf_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_rt_Vis" -ln "fourAxis_rt_Vis" -min 0 -max 1 -at "bool";
	setAttr -k on ".up";
	setAttr -k on ".dn";
	setAttr -k on ".lf";
	setAttr -k on ".rt";
	setAttr -k on ".lfup";
	setAttr -k on ".rtup";
	setAttr -k on ".lfdn";
	setAttr -k on ".rtdn";
	setAttr -k on ".fourAxis_up";
	setAttr -k on ".fourAxis_dn";
	setAttr -k on ".fourAxis_lf";
	setAttr -k on ".fourAxis_rt";
	setAttr -cb on ".up_Vis";
	setAttr -cb on ".dn_Vis";
	setAttr -cb on ".lf_Vis";
	setAttr -cb on ".lfup_Vis";
	setAttr -cb on ".rt_Vis";
	setAttr -cb on ".rtup_Vis";
	setAttr -cb on ".lfdn_Vis";
	setAttr -cb on ".rtdn_Vis";
	setAttr -cb on ".fourAxis_up_Vis";
	setAttr -cb on ".fourAxis_dn_Vis";
	setAttr -cb on ".fourAxis_lf_Vis";
	setAttr -cb on ".fourAxis_rt_Vis";
createNode nurbsCurve -n "c_mbp_FRAMEShape" -p "c_mbp_FRAME";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.078106160309654435 0.4222313923778267 0
		-0.078106160309654435 -0.4222313923778267 0
		1.0738189356316263 -0.4222313923778267 0
		1.0738189356316263 0.4222313923778267 0
		-0.078106160309654435 0.4222313923778267 0
		;
createNode transform -n "c_GRP_mbp_CTRL" -p "c_mbp_FRAME";
createNode transform -n "c_mbp_CTRL" -p "c_GRP_mbp_CTRL";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".mntl" -type "double3" 0 0 0 ;
	setAttr ".mxtl" -type "double3" 1 0 0 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
createNode nurbsCurve -n "c_mbp_CTRLShape" -p "c_mbp_CTRL";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".tw" yes;
	setAttr -s 33 ".cp[0:32]" -type "double3" 0.037349004152821698 0.027434445505788704 
		0 0.037349004152821698 0.082303336517366071 0 0.074717108445368968 0.082303336517366071 
		0 -1.9100139725567e-005 0.13717222752894354 0 -0.074755308724820085 0.082303336517366071 
		0 -0.037387204432272829 0.082303336517366071 0 -0.037387204432272829 0.027434445505788704 
		0 -0.14949151730991461 0.10973778202315482 0 -0.037387204432272829 0.027434445505788704 
		0 -0.11212341301736736 0.027434445505788704 0 -0.11212341301736736 0.054868891011577409 
		0 -0.18685962160246189 0 0 -0.11212341301736736 -0.054868891011577409 0 -0.11212341301736736 
		-0.027434445505788704 0 -0.037387204432272829 -0.027434445505788704 0 -0.14949151730991461 
		-0.10973778202315482 0 -0.037387204432272829 -0.027434445505788704 0 -0.037387204432272829 
		-0.082303336517366071 0 -0.074755308724820085 -0.082303336517366071 0 -1.9100139725567e-005 
		-0.13717222752894354 0 0.074717108445368968 -0.082303336517366071 0 0.037349004152821698 
		-0.082303336517366071 0 0.037349004152821698 -0.027434445505788704 0 0.1494533170304635 
		-0.10973778202315482 0 0.037349004152821698 -0.027434445505788704 0 0.11208521273791623 
		-0.027434445505788704 0 0.11208521273791623 -0.054868891011577409 0 0.18682142132301072 
		0 0 0.11208521273791623 0.054868891011577409 0 0.11208521273791623 0.027434445505788704 
		0 0.037349004152821698 0.027434445505788704 0 0.1494533170304635 0.10973778202315482 
		0 0.037349004152821698 0.027434445505788704 0;
createNode nurbsCurve -n "c_mbp_CTRLShapeOrig" -p "c_mbp_CTRL";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 32 0 no 3
		33 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32
		33
		-0.050000000000000003 0.050000000000000003 0
		-0.050000000000000003 0.15000000000000002 0
		-0.10000000000000001 0.15000000000000002 0
		0 0.25 0
		0.10000000000000001 0.15000000000000002 0
		0.050000000000000003 0.15000000000000002 0
		0.050000000000000003 0.050000000000000003 0
		0.20000000000000001 0.20000000000000001 0
		0.050000000000000003 0.050000000000000003 0
		0.15000000000000002 0.050000000000000003 0
		0.15000000000000002 0.10000000000000001 0
		0.25 0 0
		0.15000000000000002 -0.10000000000000001 0
		0.15000000000000002 -0.050000000000000003 0
		0.050000000000000003 -0.050000000000000003 0
		0.20000000000000001 -0.20000000000000001 0
		0.050000000000000003 -0.050000000000000003 0
		0.050000000000000003 -0.15000000000000002 0
		0.10000000000000001 -0.15000000000000002 0
		0 -0.25 0
		-0.10000000000000001 -0.15000000000000002 0
		-0.050000000000000003 -0.15000000000000002 0
		-0.050000000000000003 -0.050000000000000003 0
		-0.20000000000000001 -0.20000000000000001 0
		-0.050000000000000003 -0.050000000000000003 0
		-0.15000000000000002 -0.050000000000000003 0
		-0.15000000000000002 -0.10000000000000001 0
		-0.25 0 0
		-0.15000000000000002 0.10000000000000001 0
		-0.15000000000000002 0.050000000000000003 0
		-0.050000000000000003 0.050000000000000003 0
		-0.20000000000000001 0.20000000000000001 0
		-0.050000000000000003 0.050000000000000003 0
		;
createNode transform -n "c_mbp_CTRL_up" -p "c_mbp_FRAME";
	setAttr ".t" -type "double3" 0 2.2 0 ;
createNode nurbsCurve -n "curveShape397" -p "c_mbp_CTRL_up";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_mbp_LOC_up" -p "c_mbp_CTRL_up";
	setAttr -k off ".v" no;
createNode transform -n "c_mbp_CTRL_dn" -p "c_mbp_FRAME";
	setAttr ".t" -type "double3" 0 -2.2 0 ;
createNode nurbsCurve -n "curveShape398" -p "c_mbp_CTRL_dn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_mbp_LOC_dn" -p "c_mbp_CTRL_dn";
	setAttr -k off ".v" no;
createNode transform -n "c_mbp_CTRL_lf" -p "c_mbp_FRAME";
	setAttr ".t" -type "double3" -2.2 0 0 ;
createNode nurbsCurve -n "curveShape399" -p "c_mbp_CTRL_lf";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_mbp_LOC_lf" -p "c_mbp_CTRL_lf";
	setAttr -k off ".v" no;
createNode transform -n "c_mbp_CTRL_lfup" -p "c_mbp_FRAME";
	setAttr ".t" -type "double3" -2.2 2.2 0 ;
createNode nurbsCurve -n "curveShape400" -p "c_mbp_CTRL_lfup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_mbp_LOC_lfup" -p "c_mbp_CTRL_lfup";
	setAttr -k off ".v" no;
createNode transform -n "c_mbp_CTRL_rt" -p "c_mbp_FRAME";
	setAttr ".t" -type "double3" 2.2 0 0 ;
createNode nurbsCurve -n "curveShape401" -p "c_mbp_CTRL_rt";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_mbp_LOC_rt" -p "c_mbp_CTRL_rt";
	setAttr -k off ".v" no;
createNode transform -n "c_mbp_CTRL_rtup" -p "c_mbp_FRAME";
	setAttr ".t" -type "double3" 2.2 2.2 0 ;
createNode nurbsCurve -n "curveShape402" -p "c_mbp_CTRL_rtup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_mbp_LOC_rtup" -p "c_mbp_CTRL_rtup";
	setAttr -k off ".v" no;
createNode transform -n "c_mbp_CTRL_lfdn" -p "c_mbp_FRAME";
	setAttr ".t" -type "double3" -2.2 -2.2 0 ;
createNode nurbsCurve -n "curveShape403" -p "c_mbp_CTRL_lfdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_mbp_LOC_lfdn" -p "c_mbp_CTRL_lfdn";
	setAttr -k off ".v" no;
createNode transform -n "c_mbp_CTRL_rtdn" -p "c_mbp_FRAME";
	setAttr ".t" -type "double3" 2.2 -2.2 0 ;
createNode nurbsCurve -n "curveShape404" -p "c_mbp_CTRL_rtdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_mbp_LOC_rtdn" -p "c_mbp_CTRL_rtdn";
	setAttr -k off ".v" no;
createNode transform -n "c_mbp_CTRL_fourAxisup" -p "c_mbp_FRAME";
	setAttr ".t" -type "double3" 0 4.4 0 ;
createNode nurbsCurve -n "curveShape405" -p "c_mbp_CTRL_fourAxisup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_mbp_LOC_fourAxis_up" -p "c_mbp_CTRL_fourAxisup";
	setAttr -k off ".v" no;
createNode transform -n "c_mbp_CTRL_fourAxisdn" -p "c_mbp_FRAME";
	setAttr ".t" -type "double3" 0 -4.4 0 ;
createNode nurbsCurve -n "curveShape406" -p "c_mbp_CTRL_fourAxisdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_mbp_LOC_fourAxis_dn" -p "c_mbp_CTRL_fourAxisdn";
	setAttr -k off ".v" no;
createNode transform -n "c_mbp_CTRL_fourAxislf" -p "c_mbp_FRAME";
	setAttr ".t" -type "double3" -4.4 0 0 ;
createNode nurbsCurve -n "curveShape407" -p "c_mbp_CTRL_fourAxislf";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_mbp_LOC_fourAxis_lf" -p "c_mbp_CTRL_fourAxislf";
	setAttr -k off ".v" no;
createNode transform -n "c_mbp_CTRL_fourAxisrt" -p "c_mbp_FRAME";
	setAttr ".t" -type "double3" 4.4 0 0 ;
createNode nurbsCurve -n "curveShape408" -p "c_mbp_CTRL_fourAxisrt";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_mbp_LOC_fourAxis_rt" -p "c_mbp_CTRL_fourAxisrt";
	setAttr -k off ".v" no;
createNode transform -n "Text_Text_mxbxp_1" -p "c_GRP_mbp_FRAME";
	setAttr ".t" -type "double3" -0.82701235004471507 -0.314 -9.748761466595726e-015 ;
	setAttr ".r" -type "double3" 1.2722218725854073e-014 0 0 ;
	setAttr ".s" -type "double3" 0.070656095642445294 0.494592669497117 0.49459266949711722 ;
createNode transform -n "Text_Char_m_1" -p "Text_Text_mxbxp_1";
createNode transform -n "Text_curve126" -p "Text_Char_m_1";
	setAttr ".ovdt" 2;
createNode nurbsCurve -n "Text_curveShape126" -p "Text_curve126";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr ".cc" -type "nurbsCurve" 
		2 109 1 no 3
		112 0 0 1 1 2 3 3 4 5 5 6 7 7 8 9 9 10 10 10.750000762951094 10.750000762951094
		 11.750000762951094 11.750000762951094 12.750000762951094 13.750000762951094 13.750000762951094
		 13.850000762951094 13.850000762951094 14.650000762951095 14.650000762951095 14.750000762951094
		 14.750000762951094 14.775001144426643 14.775001144426643 15.775001144426643 15.775001144426643
		 16.775001144426643 16.775001144426643 17.775001144426643 17.775001144426643 18.542189669642177
		 18.542189669642177 19.542189669642177 19.542189669642177 20.542189669642177 20.542189669642177
		 21.542189669642177 22.542189669642177 22.542189669642177 22.562741462046965 22.562741462046965
		 22.647116223624749 22.647116223624749 23.498679510418064 23.498679510418064 24.498679510418064
		 25.498679510418064 26.498679510418064 26.498679510418064 26.598679510418066 26.598679510418066
		 27.398679510418066 27.398679510418066 27.498679510418068 27.498679510418068 28.498679510418068
		 29.498679510418068 29.498679510418068 30.498679510418068 30.498679510418068 31.265868035633602
		 31.265868035633602 32.265868035633602 32.265868035633602 33.265868035633602 33.265868035633602
		 34.265868035633602 34.265868035633602 35.265868035633602 35.265868035633602 36.222118893953585
		 36.222118893953585 37.222118893953585 38.222118893953585 39.222118893953585 39.222118893953585
		 39.322118893953586 39.322118893953586 40.222118893953585 40.222118893953585 40.322118893953586
		 40.322118893953586 41.322118893953586 42.322118893953586 43.322118893953586 43.322118893953586
		 44.022118893953589 44.022118893953589 45.022118893953589 45.022118893953589 46.022118893953589
		 47.022118893953589 47.022118893953589 48.022118893953589 48.022118893953589 48.126432721193616
		 48.126432721193616 48.682402018309688 48.682402018309688 48.76365173220303 48.76365173220303
		 49.108963397725269 49.108963397725269
		111
		0.60000000000000009 1.4546883344777601 0
		0.77968871595330747 1.6312504768444342 0
		0.81250019073777369 1.6578133821622036 0
		0.89375143053330286 1.7250003814755475 0
		1.0812512397955292 1.8 0
		1.1734386205844207 1.8 0
		1.3296879530022128 1.8 0
		1.5531258106355383 1.6234378576333257 0
		1.5906263828488596 1.4546883344777601 0
		1.7765636682688641 1.6671885252155338 0
		2.0312504768444342 1.8 0
		2.1656260013733122 1.8 0
		2.2984390020599679 1.8 0
		2.5015625238422219 1.6578133821622036 0
		2.5609384298466473 1.4953139543755247 0
		2.6000000000000001 1.3859388113221944 0
		2.6000000000000001 1.1500007629510949 0
		2.6000000000000001 0.77500038147554751 0
		2.6000000000000001 0.40000000000000002 0
		2.6000000000000001 0.24843823910887314 0
		2.6281254291599909 0.19375143053330282 0
		2.6500007629510947 0.15468833447775998 0
		2.7671885252155342 0.10000000000000001 0
		2.9000000000000004 0.10000000000000001 0
		2.9000000000000004 0.05000000000000001 0
		2.9000000000000004 0 0
		2.5 0 0
		2.1000000000000001 0 0
		2.1000000000000001 0.05000000000000001 0
		2.1000000000000001 0.10000000000000002 0
		2.1125001907377738 0.10000000000000002 0
		2.1250003814755476 0.10000000000000002 0
		2.2046875715266654 0.10000000000000001 0
		2.2500007629510947 0.14062561989776454 0
		2.2812512397955294 0.1687510490577554 0
		2.2953139543755245 0.22968795300221256 0
		2.3000000000000003 0.25937590600442512 0
		2.3000000000000003 0.40000000000000002 0
		2.3000000000000003 0.78359426260776677 0
		2.3000000000000003 1.1671885252155336 0
		2.3000000000000003 1.3859388113221944 0
		2.2515632867933166 1.4750011444266424 0
		2.1812512397955293 1.6000000000000001 0
		2.0265629053177689 1.6000000000000001 0
		1.932813000686656 1.6000000000000001 0
		1.7406256198977645 1.4968764782177464 0
		1.6031250476844434 1.3562508583199817 0
		1.6015625238422218 1.3460944533455406 0
		1.5999999999999999 1.3359380483710996 0
		1.6000000000000001 1.2937506675822081 0
		1.6000000000000001 1.2515632867933166 0
		1.6000000000000001 0.82578164339665827 0
		1.6000000000000001 0.40000000000000002 0
		1.6000000000000001 0.23437552452887772 0
		1.6421881437399861 0.15468833447775998 0
		1.7593759060044254 0.10000000000000001 0
		1.9000000000000001 0.10000000000000001 0
		1.9000000000000001 0.05000000000000001 0
		1.9000000000000001 0 0
		1.5 0 0
		1.1000000000000001 0 0
		1.1000000000000001 0.05000000000000001 0
		1.1000000000000001 0.10000000000000002 0
		1.2015625238422218 0.10000000000000001 0
		1.2781261921110858 0.16250095368886855 0
		1.2937514305333029 0.22656290531776913 0
		1.3 0.25625085831998168 0
		1.3 0.40000000000000002 0
		1.3 0.78359426260776677 0
		1.3 1.1671885252155336 0
		1.3 1.3859388113221944 0
		1.2406256198977648 1.4781261921110858 0
		1.1625009536888686 1.6000000000000001 0
		1.0203128099488823 1.6000000000000001 0
		0.92343785763332564 1.6000000000000001 0
		0.82968795300221265 1.5453131914244298 0
		0.68125123979552915 1.4609384298466468 0
		0.60000000000000009 1.3562508583199817 0
		0.60000000000000009 0.87812542915999092 0
		0.60000000000000009 0.40000000000000002 0
		0.60000000000000009 0.24218814373998626 0
		0.65000076295109488 0.14687571526665141 0
		0.74843823910887319 0.10000000000000001 0
		0.90000000000000002 0.10000000000000001 0
		0.90000000000000002 0.05000000000000001 0
		0.90000000000000002 0 0
		0.45000000000000001 0 0
		0 0 0
		0 0.05000000000000001 0
		0 0.10000000000000002 0
		0.13593804837109943 0.10000000000000001 0
		0.24375066758220801 0.14687571526665141 0
		0.30000000000000004 0.25156328679331658 0
		0.30000000000000004 0.40000000000000002 0
		0.30000000000000004 0.75 0
		0.30000000000000004 1.1000000000000001 0
		0.30000000000000004 1.3531258106355384 0
		0.28281376363775085 1.428125429159991 0
		0.26875104905775543 1.482813763637751 0
		0.21093766689555202 1.5281254291599911 0
		0.15937590600442514 1.5281254291599911 0
		0.10468757152666515 1.5281254291599911 0
		0.02968795300221256 1.5 0
		0.01484397650110628 1.55 0
		0 1.6000000000000001 0
		0.25937514305333031 1.7000000000000002 0
		0.51875028610666063 1.8 0
		0.55937514305333036 1.7999999999999998 0
		0.60000000000000009 1.7999999999999998 0
		0.60000000000000009 1.62734416723888 0
		0.60000000000000009 1.4546883344777599 0
		;
createNode transform -n "Text_Char_x_6" -p "Text_Text_mxbxp_1";
createNode transform -n "Text_curve127" -p "Text_Char_x_6";
	setAttr ".ovdt" 2;
createNode nurbsCurve -n "Text_curveShape127" -p "Text_curve127";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 2 no 3
		5 0 2.8455561668265763 3.0471186906687979 5.893168584820339 6.0931685848203392
		
		5
		1.1000000000000001 2.7000000000000002 0
		0.20156252384222173 0 0
		0 0 0
		0.90000000000000002 2.7000000000000002 0
		1.1000000000000001 2.7000000000000002 0
		;
createNode transform -n "Text_Char_b_1" -p "Text_Text_mxbxp_1";
createNode transform -n "Text_curve128" -p "Text_Char_b_1";
	setAttr ".ovdt" 2;
createNode nurbsCurve -n "Text_curveShape128" -p "Text_curve128";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr ".cc" -type "nurbsCurve" 
		2 27 1 no 3
		30 0 0 1 1 2 3 3 4 4 5 5 6 7 7 8.8140611886778064 8.8140611886778064 9.8140611886778064
		 10.814061188677806 11.814061188677806 11.814061188677806 12.814061188677806 12.814061188677806
		 12.91752899980243 12.91752899980243 13.47058359611094 13.47058359611094 13.554958357688722
		 13.554958357688722 14.740895643108727 14.740895643108727
		29
		0.60000000000000009 1.5140627145799954 0
		0.85000076295109483 1.8 0
		1.139063096055543 1.8 0
		1.4046875715266651 1.8 0
		1.8 1.3531258106355384 0
		1.8 0.965626001373312 0
		1.8 0.51406271457999553 0
		1.4968764782177464 0.23750057221332113 0
		1.2375005722133212 0 0
		0.91875028610666054 0 0
		0.76875104905775549 0 0
		0.46093842984664679 0.093751430533302815 0
		0.30000000000000004 0.18593881132219425 0
		0.30000000000000004 1.0929694056610972 0
		0.30000000000000004 2 0
		0.30000000000000004 2.2625009536888689 0
		0.27031357289997715 2.3828137636377509 0
		0.2093751430533303 2.4296879530022126 0
		0.16250095368886855 2.4296879530022126 0
		0.10781261921110857 2.4296879530022126 0
		0.026562905317769132 2.4000000000000004 0
		0.013281452658884566 2.4500000000000002 0
		0 2.5 0
		0.2578126192111086 2.6000000000000001 0
		0.51562523842221719 2.7000000000000002 0
		0.55781261921110858 2.7000000000000002 0
		0.60000000000000009 2.7000000000000002 0
		0.60000000000000009 2.1070313572899977 0
		0.60000000000000009 1.5140627145799954 0
		;
createNode transform -n "Text_curve129" -p "Text_Char_b_1";
	setAttr ".ovdt" 2;
createNode nurbsCurve -n "Text_curveShape129" -p "Text_curve129";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr ".cc" -type "nurbsCurve" 
		2 14 1 no 3
		17 0 0 1.087501335164416 1.087501335164416 2.0875013351644158 3.0875013351644158
		 3.0875013351644158 4.0875013351644158 5.0875013351644158 5.0875013351644158 6.0875013351644158
		 7.0875013351644158 7.0875013351644158 8.0875013351644149 8.0875013351644149 9.0875013351644149
		 9.0875013351644149
		16
		0.60000000000000009 1.3875013351644161 0
		0.60000000000000009 0.84375066758220807 0
		0.60000000000000009 0.30000000000000004 0
		0.69843900205996801 0.20156252384222173 0
		0.90937514305333034 0.10000000000000001 0
		1.0203128099488823 0.10000000000000001 0
		1.1968764782177463 0.10000000000000001 0
		1.5 0.49687647821774628 0
		1.5 0.87656366826886412 0
		1.5 1.2250003814755475 0
		1.1968764782177463 1.6000000000000001 0
		1.0031250476844435 1.6000000000000001 0
		0.90000000000000002 1.6000000000000001 0
		0.79687647821774632 1.5468757152666515 0
		0.72031280994888236 1.5062500953688869 0
		0.60000000000000009 1.3875013351644161 0
		;
createNode transform -n "Text_Char_x_7" -p "Text_Text_mxbxp_1";
createNode transform -n "Text_curve130" -p "Text_Char_x_7";
	setAttr ".ovdt" 2;
createNode nurbsCurve -n "Text_curveShape130" -p "Text_curve130";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 2 no 3
		5 0 2.8455561668265763 3.0471186906687979 5.893168584820339 6.0931685848203392
		
		5
		1.1000000000000001 2.7000000000000002 0
		0.20156252384222173 0 0
		0 0 0
		0.90000000000000002 2.7000000000000002 0
		1.1000000000000001 2.7000000000000002 0
		;
createNode transform -n "Text_Char_p_6" -p "Text_Text_mxbxp_1";
createNode transform -n "Text_curve131" -p "Text_Char_p_6";
	setAttr ".ovdt" 2;
createNode nurbsCurve -n "Text_curveShape131" -p "Text_curve131";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr ".cc" -type "nurbsCurve" 
		2 49 1 no 3
		52 0 0 0.56472689764648587 0.56472689764648587 0.63660146848649513 0.63660146848649513
		 0.97878808632429171 0.97878808632429171 1.9787880863242917 2.9787880863242915 2.9787880863242915
		 3.9787880863242915 3.9787880863242915 4.9787880863242915 4.9787880863242915 5.9787880863242915
		 5.9787880863242915 6.9787880863242915 6.9787880863242915 7.9787880863242915 7.9787880863242915
		 8.9787880863242915 8.9787880863242915 9.519413706222057 9.519413706222057 10.519413706222057
		 11.519413706222057 12.519413706222057 12.519413706222057 12.619413706222057 12.619413706222057
		 13.519413706222057 13.519413706222057 13.619413706222057 13.619413706222057 13.666289421488708
		 13.666289421488708 14.666289421488708 14.666289421488708 15.666289421488708 16.666289421488706
		 16.666289421488706 18.366289421488705 18.366289421488705 19.366289421488705 20.366289421488705
		 21.366289421488705 21.366289421488705 22.366289421488705 22.366289421488705 22.468999368282773
		 22.468999368282773
		51
		0 1.6000000000000001 0
		0.26406271457999542 1.7000000000000002 0
		0.52812542915999083 1.8 0
		0.56406271457999546 1.8 0
		0.60000000000000009 1.8 0
		0.60000000000000009 1.6289066910811019 0
		0.60000000000000009 1.4578133821622035 0
		0.73437552452887767 1.648438239108873 0
		1.0031250476844435 1.8 0
		1.1531258106355382 1.8 0
		1.4125001907377737 1.8 0
		1.587501335164416 1.6000000000000001 0
		1.8 1.35468833447776 0
		1.8 0.96250095368886857 0
		1.8 0.52343785763332573 0
		1.5437506675822081 0.23593804837109944 0
		1.3328130006866561 0 0
		1.0109376668955521 0 0
		0.87187609674219879 0 0
		0.77031357289997715 0.035938048371099415 0
		0.6937514305333029 0.062500953688868544 0
		0.60000000000000009 0.14062561989776454 0
		0.60000000000000009 -0.12968719005111773 0
		0.60000000000000009 -0.40000000000000002 0
		0.60000000000000009 -0.56093690394445717 0
		0.643750667582208 -0.6484367132066835 0
		0.75468833447775996 -0.70000000000000007 0
		0.90000000000000002 -0.70000000000000007 0
		0.90000000000000002 -0.75 0
		0.90000000000000002 -0.80000000000000004 0
		0.45000000000000001 -0.80000000000000004 0
		0 -0.80000000000000004 0
		0 -0.75 0
		0 -0.70000000000000007 0
		0.023437857633325704 -0.70000000000000007 0
		0.046875715266651408 -0.70000000000000007 0
		0.15156328679331654 -0.70156099794003213 0
		0.22500038147554743 -0.66562447547112236 0
		0.26093842984664684 -0.64687418936446184 0
		0.30000000000000004 -0.56562447547112238 0
		0.30000000000000004 -0.40000000000000002 0
		0.30000000000000004 0.44999999999999996 0
		0.30000000000000004 1.3 0
		0.30000000000000004 1.4203128099488822 0
		0.26875104905775543 1.4859388113221943 0
		0.20000000000000001 1.5281254291599911 0
		0.14218814373998628 1.5281254291599911 0
		0.095313954375524534 1.5281254291599911 0
		0.023437857633325704 1.5 0
		0.011718928816662852 1.55 0
		0 1.6000000000000003 0
		;
createNode transform -n "Text_curve132" -p "Text_Char_p_6";
	setAttr ".ovdt" 2;
createNode nurbsCurve -n "Text_curveShape132" -p "Text_curve132";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr ".cc" -type "nurbsCurve" 
		2 18 1 no 3
		21 0 0 0.67031204699778746 0.67031204699778746 1.6703120469977875 1.6703120469977875
		 2.6703120469977875 3.6703120469977875 3.6703120469977875 4.6703120469977879 4.6703120469977879
		 5.6703120469977879 5.6703120469977879 6.6703120469977879 6.6703120469977879 7.6703120469977879
		 7.6703120469977879 8.6703120469977879 8.6703120469977879 9.6703120469977879 9.6703120469977879
		
		20
		0.60000000000000009 1.3421881437399863 0
		0.60000000000000009 1.0070321202410926 0
		0.60000000000000009 0.67187609674219884 0
		0.60000000000000009 0.45468833447775997 0
		0.61718776226443894 0.38593881132219426 0
		0.64531319142442978 0.27187609674219887 0
		0.85937590600442515 0.10000000000000001 0
		1.021875333791104 0.10000000000000001 0
		1.2187502861066606 0.10000000000000001 0
		1.3406256198977646 0.25312581063553824 0
		1.5 0.45312581063553825 0
		1.5 0.81406271457999546 0
		1.5 1.2265629053177693 0
		1.3187502861066607 1.4468757152666516 0
		1.1937514305333028 1.6000000000000001 0
		1.0203128099488823 1.6000000000000001 0
		0.9265629053177693 1.6000000000000001 0
		0.83437552452887775 1.5531258106355383 0
		0.7625009536888685 1.5187502861066606 0
		0.60000000000000009 1.3421881437399863 0
		;
createNode transform -n "Tongue_CTRL_FRAME_GRP" -p "Facial_CTRL_FRAME";
	setAttr ".t" -type "double3" 2.825654945048738 -1.6458176208502269 1.4629246414722524e-014 ;
createNode transform -n "Tongue_CTRL_FRAME" -p "Tongue_CTRL_FRAME_GRP";
	setAttr ".rp" -type "double3" 0 -1.1102230246251565e-016 1.2325951644078309e-032 ;
	setAttr ".sp" -type "double3" 0 -1.1102230246251565e-016 1.2325951644078309e-032 ;
createNode nurbsCurve -n "Tongue_CTRL_FRAMEShape" -p "Tongue_CTRL_FRAME";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.5122654344667138 0.65207464972691498 -1.2601436025374895e-016
		-0.00028161702442203488 0.65718996548908704 -1.7821121732462098e-016
		-0.51198107902138268 0.65207464972691498 -1.26014360253749e-016
		-0.51349456996414833 3.2112695072372299e-016 -5.1641152288041213e-032
		-0.51198107902138268 -0.73955370635802198 1.2601436025374897e-016
		-0.0002816170244221472 -0.73382996981571047 1.78211217324621e-016
		0.5122654344667138 -0.73955370635802198 1.2601436025374902e-016
		0.51208374642112942 -5.9521325992805852e-016 9.5717592467817795e-032
		0.5122654344667138 0.65207464972691498 -1.2601436025374895e-016
		-0.00028161702442203488 0.65718996548908704 -1.7821121732462098e-016
		-0.51198107902138268 0.65207464972691498 -1.26014360253749e-016
		;
createNode transform -n "c_GRP_tongue_FRAME" -p "Tongue_CTRL_FRAME";
	setAttr ".t" -type "double3" 0.0018534490175259322 -0.27870463710619764 2.8164575519356529e-016 ;
	setAttr ".r" -type "double3" -1.272221872585407e-014 0 0 ;
	setAttr ".s" -type "double3" 0.3 0.30000000000000004 0.30000000000000004 ;
createNode transform -n "c_tongue_FRAME" -p "c_GRP_tongue_FRAME";
	addAttr -ci true -sn "up" -ln "up" -min 0 -at "double";
	addAttr -ci true -sn "dn" -ln "dn" -min 0 -at "double";
	addAttr -ci true -sn "lf" -ln "lf" -min 0 -at "double";
	addAttr -ci true -sn "rt" -ln "rt" -min 0 -at "double";
	addAttr -ci true -sn "lfup" -ln "lfup" -min 0 -at "double";
	addAttr -ci true -sn "rtup" -ln "rtup" -min 0 -at "double";
	addAttr -ci true -sn "lfdn" -ln "lfdn" -min 0 -at "double";
	addAttr -ci true -sn "rtdn" -ln "rtdn" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_up" -ln "fourAxis_up" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_dn" -ln "fourAxis_dn" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_lf" -ln "fourAxis_lf" -min 0 -at "double";
	addAttr -ci true -sn "fourAxis_rt" -ln "fourAxis_rt" -min 0 -at "double";
	addAttr -ci true -sn "up_Vis" -ln "up_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "dn_Vis" -ln "dn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lf_Vis" -ln "lf_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lfup_Vis" -ln "lfup_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rt_Vis" -ln "rt_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rtup_Vis" -ln "rtup_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "lfdn_Vis" -ln "lfdn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "rtdn_Vis" -ln "rtdn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_up_Vis" -ln "fourAxis_up_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_dn_Vis" -ln "fourAxis_dn_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_lf_Vis" -ln "fourAxis_lf_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fourAxis_rt_Vis" -ln "fourAxis_rt_Vis" -min 0 -max 1 -at "bool";
	setAttr -k on ".up";
	setAttr -k on ".dn";
	setAttr -k on ".lf";
	setAttr -k on ".rt";
	setAttr -k on ".lfup";
	setAttr -k on ".rtup";
	setAttr -k on ".lfdn";
	setAttr -k on ".rtdn";
	setAttr -k on ".fourAxis_up";
	setAttr -k on ".fourAxis_dn";
	setAttr -k on ".fourAxis_lf";
	setAttr -k on ".fourAxis_rt";
	setAttr -cb on ".up_Vis";
	setAttr -cb on ".dn_Vis";
	setAttr -cb on ".lf_Vis";
	setAttr -cb on ".lfup_Vis";
	setAttr -cb on ".rt_Vis";
	setAttr -cb on ".rtup_Vis";
	setAttr -cb on ".lfdn_Vis";
	setAttr -cb on ".rtdn_Vis";
	setAttr -cb on ".fourAxis_up_Vis";
	setAttr -cb on ".fourAxis_dn_Vis";
	setAttr -cb on ".fourAxis_lf_Vis";
	setAttr -cb on ".fourAxis_rt_Vis";
createNode nurbsCurve -n "c_tongue_FRAMEShape" -p "c_tongue_FRAME";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode transform -n "c_GRP_tongue_CTRL" -p "c_tongue_FRAME";
createNode transform -n "c_tongue_CTRL" -p "c_GRP_tongue_CTRL";
	addAttr -ci true -sn "ikfk_switch" -ln "ikfk_switch" -min 0 -max 2 -en "ik:fk:both" 
		-at "enum";
	addAttr -ci true -sn "second_vis" -ln "second_vis" -min 0 -max 1 -en "off:on" -at "enum";
	addAttr -ci true -sn "stretch" -ln "stretch" -at "double";
	addAttr -ci true -sn "rotateWeight" -ln "rotateWeight" -at "double";
	addAttr -ci true -sn "drivenJoint" -ln "drivenJoint" -min 1 -max 12 -at "double";
	addAttr -ci true -sn "tx_scale" -ln "tx_scale" -at "double";
	addAttr -ci true -sn "ty_scale" -ln "ty_scale" -at "double";
	addAttr -ci true -sn "rx_scale" -ln "rx_scale" -at "double";
	addAttr -ci true -sn "ry_scale" -ln "ry_scale" -at "double";
	addAttr -ci true -sn "rz_scale" -ln "rz_scale" -at "double";
	addAttr -ci true -sn "output_tx" -ln "output_tx" -at "double";
	addAttr -ci true -sn "output_ty" -ln "output_ty" -at "double";
	addAttr -ci true -sn "output_rx" -ln "output_rx" -at "double";
	addAttr -ci true -sn "output_ry" -ln "output_ry" -at "double";
	addAttr -ci true -sn "output_rz" -ln "output_rz" -at "double";
	addAttr -ci true -sn "stretch_scale" -ln "stretch_scale" -at "double";
	addAttr -ci true -sn "output_stretch" -ln "output_stretch" -at "double";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 7.5730646901217133e-029 -7.5730646901217133e-029 0 ;
	setAttr -l on -k off ".tz";
	setAttr ".r" -type "double3" 3.4424487873851071 0 0 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".mntl" -type "double3" -1 -1 0 ;
	setAttr ".mxtl" -type "double3" 1 1 0 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
	setAttr -l on ".ikfk_switch" 2;
	setAttr -k on ".second_vis" 1;
	setAttr -k on ".stretch";
	setAttr -k on ".rotateWeight" 0.5;
	setAttr -k on ".drivenJoint" 12;
	setAttr -cb on ".tx_scale" 2;
	setAttr -cb on ".ty_scale" 2;
	setAttr -cb on ".rx_scale" 1;
	setAttr -cb on ".ry_scale" 1;
	setAttr -cb on ".rz_scale" 1;
	setAttr -cb on ".stretch_scale" 1;
createNode nurbsCurve -n "c_tongue_CTRLShape" -p "c_tongue_CTRL";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".cc" -type "nurbsCurve" 
		1 32 0 no 3
		33 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32
		33
		-0.050000000000000003 0.050000000000000003 0
		-0.050000000000000003 0.15000000000000002 0
		-0.10000000000000001 0.15000000000000002 0
		0 0.25 0
		0.10000000000000001 0.15000000000000002 0
		0.050000000000000003 0.15000000000000002 0
		0.050000000000000003 0.050000000000000003 0
		0.20000000000000001 0.20000000000000001 0
		0.050000000000000003 0.050000000000000003 0
		0.15000000000000002 0.050000000000000003 0
		0.15000000000000002 0.10000000000000001 0
		0.25 0 0
		0.15000000000000002 -0.10000000000000001 0
		0.15000000000000002 -0.050000000000000003 0
		0.050000000000000003 -0.050000000000000003 0
		0.20000000000000001 -0.20000000000000001 0
		0.050000000000000003 -0.050000000000000003 0
		0.050000000000000003 -0.15000000000000002 0
		0.10000000000000001 -0.15000000000000002 0
		0 -0.25 0
		-0.10000000000000001 -0.15000000000000002 0
		-0.050000000000000003 -0.15000000000000002 0
		-0.050000000000000003 -0.050000000000000003 0
		-0.20000000000000001 -0.20000000000000001 0
		-0.050000000000000003 -0.050000000000000003 0
		-0.15000000000000002 -0.050000000000000003 0
		-0.15000000000000002 -0.10000000000000001 0
		-0.25 0 0
		-0.15000000000000002 0.10000000000000001 0
		-0.15000000000000002 0.050000000000000003 0
		-0.050000000000000003 0.050000000000000003 0
		-0.20000000000000001 0.20000000000000001 0
		-0.050000000000000003 0.050000000000000003 0
		;
createNode transform -n "c_tongue_CTRL_up" -p "c_tongue_FRAME";
	setAttr ".t" -type "double3" 0 2.2 0 ;
createNode nurbsCurve -n "curveShape445" -p "c_tongue_CTRL_up";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_tongue_LOC_up" -p "c_tongue_CTRL_up";
	setAttr -k off ".v" no;
createNode transform -n "c_tongue_CTRL_dn" -p "c_tongue_FRAME";
	setAttr ".t" -type "double3" 0 -2.2 0 ;
createNode nurbsCurve -n "curveShape446" -p "c_tongue_CTRL_dn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_tongue_LOC_dn" -p "c_tongue_CTRL_dn";
	setAttr -k off ".v" no;
createNode transform -n "c_tongue_CTRL_lf" -p "c_tongue_FRAME";
	setAttr ".t" -type "double3" -2.2 0 0 ;
createNode nurbsCurve -n "curveShape447" -p "c_tongue_CTRL_lf";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_tongue_LOC_lf" -p "c_tongue_CTRL_lf";
	setAttr -k off ".v" no;
createNode transform -n "c_tongue_CTRL_lfup" -p "c_tongue_FRAME";
	setAttr ".t" -type "double3" -2.2 2.2 0 ;
createNode nurbsCurve -n "curveShape448" -p "c_tongue_CTRL_lfup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_tongue_LOC_lfup" -p "c_tongue_CTRL_lfup";
	setAttr -k off ".v" no;
createNode transform -n "c_tongue_CTRL_rt" -p "c_tongue_FRAME";
	setAttr ".t" -type "double3" 2.2 0 0 ;
createNode nurbsCurve -n "curveShape449" -p "c_tongue_CTRL_rt";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_tongue_LOC_rt" -p "c_tongue_CTRL_rt";
	setAttr -k off ".v" no;
createNode transform -n "c_tongue_CTRL_rtup" -p "c_tongue_FRAME";
	setAttr ".t" -type "double3" 2.2 2.2 0 ;
createNode nurbsCurve -n "curveShape450" -p "c_tongue_CTRL_rtup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_tongue_LOC_rtup" -p "c_tongue_CTRL_rtup";
	setAttr -k off ".v" no;
createNode transform -n "c_tongue_CTRL_lfdn" -p "c_tongue_FRAME";
	setAttr ".t" -type "double3" -2.2 -2.2 0 ;
createNode nurbsCurve -n "curveShape451" -p "c_tongue_CTRL_lfdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_tongue_LOC_lfdn" -p "c_tongue_CTRL_lfdn";
	setAttr -k off ".v" no;
createNode transform -n "c_tongue_CTRL_rtdn" -p "c_tongue_FRAME";
	setAttr ".t" -type "double3" 2.2 -2.2 0 ;
createNode nurbsCurve -n "curveShape452" -p "c_tongue_CTRL_rtdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_tongue_LOC_rtdn" -p "c_tongue_CTRL_rtdn";
	setAttr -k off ".v" no;
createNode transform -n "c_tongue_CTRL_fourAxisup" -p "c_tongue_FRAME";
	setAttr ".t" -type "double3" 0 4.4 0 ;
createNode nurbsCurve -n "curveShape453" -p "c_tongue_CTRL_fourAxisup";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_tongue_LOC_fourAxis_up" -p "c_tongue_CTRL_fourAxisup";
	setAttr -k off ".v" no;
createNode transform -n "c_tongue_CTRL_fourAxisdn" -p "c_tongue_FRAME";
	setAttr ".t" -type "double3" 0 -4.4 0 ;
createNode nurbsCurve -n "curveShape454" -p "c_tongue_CTRL_fourAxisdn";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_tongue_LOC_fourAxis_dn" -p "c_tongue_CTRL_fourAxisdn";
	setAttr -k off ".v" no;
createNode transform -n "c_tongue_CTRL_fourAxislf" -p "c_tongue_FRAME";
	setAttr ".t" -type "double3" -4.4 0 0 ;
createNode nurbsCurve -n "curveShape455" -p "c_tongue_CTRL_fourAxislf";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_tongue_LOC_fourAxis_lf" -p "c_tongue_CTRL_fourAxislf";
	setAttr -k off ".v" no;
createNode transform -n "c_tongue_CTRL_fourAxisrt" -p "c_tongue_FRAME";
	setAttr ".t" -type "double3" 4.4 0 0 ;
createNode nurbsCurve -n "curveShape456" -p "c_tongue_CTRL_fourAxisrt";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		-1 -1 0
		1 -1 0
		1 1 0
		-1 1 0
		;
createNode locator -n "c_tongue_LOC_fourAxis_rt" -p "c_tongue_CTRL_fourAxisrt";
	setAttr -k off ".v" no;
createNode transform -n "c_Text_Tongue_1" -p "c_GRP_tongue_FRAME";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" -1.0200426241499958 1.4876383600923235 0 ;
	setAttr ".s" -type "double3" 0.16217460513091964 0.12 0.12 ;
	setAttr ".rp" -type "double3" 0.95683017027242567 0.10799999999999998 0 ;
	setAttr ".sp" -type "double3" 5.8999999999999995 0.9 0 ;
	setAttr ".spt" -type "double3" -4.9431698297275739 -0.792 0 ;
createNode transform -n "c_Char_T_1" -p "c_Text_Tongue_1";
createNode transform -n "c_tongue_curve1" -p "c_Char_T_1";
createNode nurbsCurve -n "c_tongue_curveShape1" -p "c_tongue_curve1";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		2 45 1 no 3
		48 0 0 0.54374914168001798 0.54374914168001798 0.64374914168001807 0.64374914168001807
		 1.6437491416800181 1.6437491416800181 2.6437491416800181 3.6437491416800181 3.6437491416800181
		 3.992187380788891 3.992187380788891 5.9921873807888915 5.9921873807888915 6.9921873807888915
		 6.9921873807888915 7.9921873807888915 7.9921873807888915 8.0906248569466701 8.0906248569466701
		 8.1906248569466698 8.1906248569466698 9.2906248569466694 9.2906248569466694 9.390624856946669
		 9.390624856946669 9.4906248569466687 9.4906248569466687 10.490624856946669 10.490624856946669
		 11.490624856946669 11.490624856946669 13.490624856946669 13.490624856946669 13.793748378728923
		 13.793748378728923 14.793748378728923 14.793748378728923 15.793748378728923 16.793748378728921
		 16.793748378728921 16.893748378728922 16.893748378728922 17.43749752040894 17.43749752040894
		 19.537497520408941 19.537497520408941
		47
		2.2000000000000002 2.6000000000000001 0
		2.2000000000000002 2.3281254291599911 0
		2.2000000000000002 2.0562508583199821 0
		2.1500000000000004 2.0562508583199821 0
		2.1000000000000001 2.0562508583199821 0
		2.0796887159533077 2.2156252384222173 0
		2.0453131914244298 2.2843762874799727 0
		1.9890638590066378 2.3953139543755246 0
		1.8015625238422217 2.5 0
		1.648438239108873 2.5 0
		1.4742191195544365 2.5 0
		1.3 2.5 0
		1.3 1.5 0
		1.3 0.5 0
		1.3 0.24687571526665142 0
		1.3562508583199817 0.18437628747997256 0
		1.4359380483710995 0.10000000000000001 0
		1.6015625238422218 0.10000000000000001 0
		1.6507812619211109 0.10000000000000001 0
		1.7 0.10000000000000001 0
		1.7000000000000004 0.05000000000000001 0
		1.7000000000000004 0 0
		1.1500000000000001 0 0
		0.60000000000000009 0 0
		0.60000000000000009 0.05000000000000001 0
		0.60000000000000009 0.10000000000000002 0
		0.65000000000000013 0.10000000000000001 0
		0.70000000000000007 0.10000000000000001 0
		0.87968871595330755 0.10000000000000001 0
		0.95468833447776003 0.20468757152666514 0
		1 0.27031357289997715 0
		1 0.5 0
		1 1.5 0
		1 2.5 0
		0.84843823910887317 2.5 0
		0.69687647821774634 2.5 0
		0.52187533379110407 2.5 0
		0.44687571526665143 2.473438620584421 0
		0.35000076295109483 2.4375005722133212 0
		0.21250019073777371 2.2312504768444343 0
		0.20000000000000001 2.0562508583199821 0
		0.15000000000000002 2.0562508583199821 0
		0.10000000000000002 2.0562508583199821 0
		0.10000000000000001 2.3281254291599911 0
		0.10000000000000001 2.6000000000000001 0
		1.1500000000000001 2.6000000000000001 0
		2.2000000000000002 2.6000000000000001 0
		;
createNode transform -n "c_Char_o_1" -p "c_Text_Tongue_1";
createNode transform -n "c_tongue_curve2" -p "c_Char_o_1";
createNode nurbsCurve -n "c_tongue_curveShape2" -p "c_tongue_curve2";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		2 15 1 no 3
		18 0 0 1 1 2 2 3 4 5 5 6 6 7 7 8 9 10 10
		17
		0.95156328679331659 1.8 0
		1.3515632867933167 1.8 0
		1.5937514305333029 1.5078126192111085 0
		1.8 1.2562508583199818 0
		1.8 0.93281300068665607 0
		1.8 0.70468757152666517 0
		1.5734386205844206 0.23750057221332113 0
		1.1750011444266424 0 0
		0.9312504768444344 0 0
		0.53281300068665594 0 0
		0.29843900205996798 0.30625009536888687 0
		0.10000000000000001 0.56406347753109032 0
		0.10000000000000001 0.88437628747997266 0
		0.10000000000000001 1.1171877622644388 0
		0.34062561989776458 1.5796887159533075 0
		0.732813000686656 1.8 0
		0.95156328679331659 1.8 0
		;
createNode transform -n "c_tongue_curve3" -p "c_Char_o_1";
createNode nurbsCurve -n "c_tongue_curveShape3" -p "c_tongue_curve3";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		2 13 1 no 3
		16 0 0 1 2 3 3 4 5 5 6 7 7 8 8 9 9
		15
		0.89062638284885942 1.7000000000000002 0
		0.78437628747997257 1.7000000000000002 0
		0.57031357289997719 1.5796887159533075 0
		0.43750057221332117 1.2765636682688641 0
		0.43750057221332117 1.0390630960555429 0
		0.43750057221332117 0.65625085831998176 0
		0.75625085831998173 0.10000000000000001 0
		1.0156252384222171 0.10000000000000001 0
		1.210937666895552 0.10000000000000001 0
		1.4625009536888687 0.40625009536888684 0
		1.4625009536888687 0.77968871595330747 0
		1.4625009536888687 1.2484382391088733 0
		1.2515632867933166 1.5156252384222171 0
		1.110937666895552 1.7000000000000002 0
		0.89062638284885942 1.7000000000000002 0
		;
createNode transform -n "c_Char_n_1" -p "c_Text_Tongue_1";
createNode transform -n "c_tongue_curve4" -p "c_Char_n_1";
createNode nurbsCurve -n "c_tongue_curveShape4" -p "c_tongue_curve4";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		2 67 1 no 3
		70 0 0 1 1 2 3 3 4 4 4.7437506675822076 4.7437506675822076 5.7437506675822076
		 5.7437506675822076 6.7437506675822076 7.7437506675822076 7.7437506675822076 7.8437506675822073
		 7.8437506675822073 8.7437506675822068 8.7437506675822068 8.8437506675822064 8.8437506675822064
		 8.8828137636377491 8.8828137636377491 9.8828137636377491 10.882813763637749 10.882813763637749
		 11.882813763637749 11.882813763637749 12.617189288166626 12.617189288166626 13.617189288166626
		 14.617189288166626 14.617189288166626 15.617189288166626 15.617189288166626 16.564065003433278
		 16.564065003433278 17.564065003433278 17.564065003433278 18.564065003433278 19.564065003433278
		 19.564065003433278 19.664065003433279 19.664065003433279 20.564065003433278 20.564065003433278
		 20.664065003433279 20.664065003433279 20.707815671015489 20.707815671015489 21.707815671015489
		 22.707815671015489 22.707815671015489 23.407815671015488 23.407815671015488 24.407815671015488
		 25.407815671015488 26.407815671015488 26.407815671015488 27.407815671015488 27.407815671015488
		 27.512129498255511 27.512129498255511 28.068098795371586 28.068098795371586 28.149348509264925
		 28.149348509264925 28.48841007941828 28.48841007941828
		69
		0.60000000000000009 1.4609384298466468 0
		0.92500038147554742 1.8 0
		1.2203128099488822 1.8 0
		1.3718760967421988 1.8 0
		1.5906263828488596 1.6578133821622036 0
		1.656250858319982 1.4937514305333028 0
		1.7000000000000002 1.3796887159533076 0
		1.7000000000000002 1.143750667582208 0
		1.7000000000000002 0.77187533379110396 0
		1.7000000000000002 0.39999999999999997 0
		1.7000000000000002 0.24687571526665142 0
		1.7296879530022125 0.19375143053330282 0
		1.7531258106355385 0.14843823910887313 0
		1.8578133821622036 0.10000000000000001 0
		2 0.10000000000000001 0
		2 0.05000000000000001 0
		2 0 0
		1.55 0 0
		1.1000000000000001 0 0
		1.1000000000000001 0.05000000000000001 0
		1.1000000000000001 0.10000000000000002 0
		1.1195315480277714 0.10000000000000001 0
		1.139063096055543 0.10000000000000001 0
		1.2687510490577554 0.10000000000000001 0
		1.3718760967421988 0.1687510490577554 0
		1.3921889066910813 0.23437552452887772 0
		1.4000000000000001 0.26093842984664684 0
		1.4000000000000001 0.40000000000000002 0
		1.4000000000000004 0.76718776226443897 0
		1.4000000000000004 1.1343755245288778 0
		1.4000000000000001 1.3781261921110859 0
		1.2625009536888685 1.6000000000000001 0
		1.1000000000000001 1.6000000000000001 0
		0.84843823910887317 1.6000000000000001 0
		0.60000000000000009 1.3468757152666515 0
		0.60000000000000009 0.87343785763332571 0
		0.60000000000000009 0.40000000000000002 0
		0.60000000000000009 0.23750057221332113 0
		0.62187533379110405 0.19843900205996798 0
		0.65000076295109488 0.14687571526665141 0
		0.74843823910887319 0.10000000000000001 0
		0.90000000000000002 0.10000000000000001 0
		0.90000000000000002 0.05000000000000001 0
		0.90000000000000002 0 0
		0.45000000000000001 0 0
		0 0 0
		0 0.05000000000000001 0
		0 0.10000000000000002 0
		0.021875333791103992 0.099999999999999992 0
		0.043750667582207983 0.099999999999999992 0
		0.19375143053330282 0.10000000000000001 0
		0.30000000000000004 0.22500038147554743 0
		0.30000000000000004 0.40000000000000002 0
		0.30000000000000004 0.75 0
		0.30000000000000004 1.1000000000000001 0
		0.30000000000000004 1.3656260013733119 0
		0.27031357289997715 1.482813763637751 0
		0.21093766689555202 1.5281254291599911 0
		0.15937590600442514 1.5281254291599911 0
		0.10468757152666515 1.5281254291599911 0
		0.02968795300221256 1.5 0
		0.01484397650110628 1.55 0
		0 1.6000000000000001 0
		0.25937514305333031 1.7000000000000002 0
		0.51875028610666063 1.8 0
		0.55937514305333036 1.7999999999999998 0
		0.60000000000000009 1.7999999999999998 0
		0.60000000000000009 1.6304692149233233 0
		0.60000000000000009 1.4609384298466468 0
		;
createNode transform -n "c_Char_g_1" -p "c_Text_Tongue_1";
createNode transform -n "c_tongue_curve5" -p "c_Char_g_1";
createNode nurbsCurve -n "c_tongue_curveShape5" -p "c_tongue_curve5";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		2 61 1 no 3
		64 0 0 1 2 2 3 4 4 5 5 5.36406347753109 5.36406347753109 6.36406347753109 7.36406347753109
		 7.36406347753109 8.36406347753109 8.36406347753109 9.36406347753109 9.36406347753109
		 10.36406347753109 11.36406347753109 11.36406347753109 11.570313572899977 11.570313572899977
		 12.570313572899977 12.570313572899977 13.570313572899977 14.570313572899977 14.570313572899977
		 15.570313572899977 15.570313572899977 16.570313572899977 17.570313572899977 17.570313572899977
		 18.570313572899977 19.570313572899977 19.570313572899977 20.570313572899977 20.570313572899977
		 21.570313572899977 21.570313572899977 22.570313572899977 23.570313572899977 23.570313572899977
		 24.570313572899977 24.570313572899977 25.570313572899977 25.570313572899977 26.570313572899977
		 26.570313572899977 27.570313572899977 27.570313572899977 28.570313572899977 28.570313572899977
		 29.570313572899977 29.570313572899977 30.570313572899977 30.570313572899977 31.570313572899977
		 32.570313572899977 32.570313572899977 33.570313572899977 34.570313572899977 34.570313572899977
		
		63
		0.53750057221332115 0.67968871595330738 0
		0.37500114442664229 0.75468833447775996 0
		0.20000000000000001 1.0250003814755473 0
		0.20000000000000001 1.1890638590066378 0
		0.20000000000000001 1.4390630960555431 0
		0.5843762874799725 1.8 0
		0.88593881132219432 1.8 0
		1.1312504768444345 1.8 0
		1.3125001907377738 1.7000000000000002 0
		1.494531929503319 1.7000000000000004 0
		1.676563668268864 1.7000000000000004 0
		1.7562508583199818 1.7000000000000002 0
		1.782813763637751 1.693751430533303 0
		1.7890638590066379 1.6875013351644161 0
		1.8 1.6781261921110859 0
		1.8 1.6515632867933168 0
		1.8 1.6234378576333257 0
		1.7921889066910812 1.6125001907377738 0
		1.787501335164416 1.606250095368887 0
		1.7640634775310904 1.6000000000000001 0
		1.698439002059968 1.6000000000000001 0
		1.5953139543755246 1.6000000000000003 0
		1.4921889066910812 1.6000000000000003 0
		1.6000000000000001 1.4546883344777601 0
		1.6000000000000001 1.228125429159991 0
		1.6000000000000001 0.96875104905775533 0
		1.2203128099488822 0.60000000000000009 0
		0.90000000000000002 0.60000000000000009 0
		0.76875104905775549 0.60000000000000009 0
		0.63125047684443425 0.64062561989776468 0
		0.55468833447776 0.56562600137331198 0
		0.5 0.45156328679331659 0
		0.5 0.410937666895552 0
		0.5 0.37812619211108567 0
		0.56250095368886854 0.31406271457999546 0
		0.65156328679331654 0.30000000000000004 0
		0.70468757152666517 0.30000000000000004 0
		0.9156252384222171 0.30000000000000004 0
		1.3015625238422217 0.30000000000000004 0
		1.4171877622644389 0.30000000000000004 0
		1.5921889066910813 0.27500114442664225 0
		1.8 0.056250858319981695 0
		1.8 -0.10312352178225376 0
		1.8 -0.32343633173113606 0
		1.6031250476844434 -0.51562371252002748 0
		1.3125001907377738 -0.80000000000000004 0
		0.84531319142442973 -0.80000000000000004 0
		0.48750133516441602 -0.80000000000000004 0
		0.23906309605554285 -0.64218661783779662 0
		0.10000000000000001 -0.55156176089112685 0
		0.10000000000000001 -0.45312428473334859 0
		0.10000000000000001 -0.40937361715114062 0
		0.11718776226443886 -0.36562447547112231 0
		0.14375066758220797 -0.29843747615777833 0
		0.22656290531776913 -0.17968719005111775 0
		0.23750057221332113 -0.16249942778667889 0
		0.38750133516441598 0.017187762264438852 0
		0.28437628747997257 0.079688715953307399 0
		0.20000000000000001 0.1796887159533074 0
		0.20000000000000001 0.24218814373998626 0
		0.20000000000000001 0.31406271457999546 0
		0.32031280994888234 0.5046875715266651 0
		0.53750057221332115 0.67968871595330738 0
		;
createNode transform -n "c_tongue_curve6" -p "c_Char_g_1";
createNode nurbsCurve -n "c_tongue_curveShape6" -p "c_tongue_curve6";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		2 13 1 no 3
		16 0 0 1 2 2 3 3 4 4 5 6 6 7 7 8 8
		15
		0.87187609674219879 1.7000000000000002 0
		0.71406271457999548 1.7000000000000002 0
		0.5 1.4859388113221943 0
		0.5 1.2640634775310904 0
		0.5 0.97812619211108576 0
		0.64531319142442978 0.82031280994888223 0
		0.75625085831998173 0.70000000000000007 0
		0.92812542915999097 0.70000000000000007 0
		1.0906263828488594 0.70000000000000007 0
		1.3 0.9062500953688869 0
		1.3 1.1281254291599909 0
		1.3 1.4171877622644389 0
		1.1531258106355382 1.5796887159533075 0
		1.0437506675822081 1.7000000000000002 0
		0.87187609674219879 1.7000000000000002 0
		;
createNode transform -n "c_tongue_curve7" -p "c_Char_g_1";
createNode nurbsCurve -n "c_tongue_curveShape7" -p "c_tongue_curve7";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		2 15 1 no 3
		18 0 0 1 2 2 3 3 4 4 5 6 6 7 7 8 8 9 9
		17
		0.4828137636377508 0 0
		0.44218814373998633 -0.095312428473334862 0
		0.40000000000000002 -0.25937438010223546 0
		0.40000000000000002 -0.32812390325780116 0
		0.40000000000000002 -0.41718623636224922 0
		0.50781261921110854 -0.48437476157778286 0
		0.6937514305333029 -0.60000000000000009 0
		1.0468757152666515 -0.60000000000000009 0
		1.3812512397955292 -0.60000000000000009 0
		1.7000000000000002 -0.34531166552224007 0
		1.7000000000000002 -0.20000000000000001 0
		1.7000000000000002 -0.096874952315556581 0
		1.5968764782177463 -0.051561760891126879 0
		1.4921889066910812 -0.0078110933089188929 0
		1.1812512397955293 0 0
		0.72656290531776913 0 0
		0.4828137636377508 0 0
		;
createNode transform -n "c_Char_u_1" -p "c_Text_Tongue_1";
createNode transform -n "c_tongue_curve8" -p "c_Char_u_1";
createNode nurbsCurve -n "c_tongue_curveShape8" -p "c_tongue_curve8";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		2 49 1 no 3
		52 0 0 1.1000000000000001 1.1000000000000001 2.1000000000000001 3.1000000000000001
		 4.0999999999999996 4.0999999999999996 5.0999999999999996 5.0999999999999996 5.2034674193959543
		 5.2034674193959543 5.7565205930718095 5.7565205930718095 5.8408968805517816 5.8408968805517816
		 6.1799599766073241 6.1799599766073241 7.1799599766073241 8.179959976607325 8.179959976607325
		 9.179959976607325 10.179959976607325 11.179959976607325 11.179959976607325 11.981520974547356
		 11.981520974547356 12.981520974547356 13.981520974547356 14.981520974547356 14.981520974547356
		 15.081520974547356 15.081520974547356 15.681520974547356 15.681520974547356 16.87683340302069
		 16.87683340302069 17.87683340302069 18.87683340302069 18.87683340302069 19.87683340302069
		 20.87683340302069 20.87683340302069 21.923707592385153 21.923707592385153 22.923707592385153
		 23.923707592385153 23.923707592385153 24.023707592385154 24.023707592385154 24.623707592385156
		 24.623707592385156
		51
		1.7000000000000002 1.8 0
		1.7000000000000002 1.25 0
		1.7000000000000002 0.70000000000000007 0
		1.7000000000000002 0.4359380483710994 0
		1.7296879530022125 0.31875028610666062 0
		1.7937514305333029 0.26875104905775543 0
		1.8359380483710994 0.26875104905775543 0
		1.8968764782177463 0.26875104905775543 0
		1.9734386205844208 0.30000000000000004 0
		1.9867193102922105 0.25 0
		2 0.20000000000000001 0
		1.7421881437399862 0.10000000000000001 0
		1.4843762874799726 0 0
		1.4421881437399864 0 0
		1.4000000000000001 0 0
		1.4000000000000001 0.16953154802777143 0
		1.4000000000000001 0.33906309605554286 0
		1.1625009536888686 0.11562523842221713 0
		0.910937666895552 0 0
		0.77187609674219892 0 0
		0.61718776226443894 0 0
		0.3890638590066377 0.17500114442664227 0
		0.30000000000000004 0.44843823910887315 0
		0.30000000000000004 0.69843900205996801 0
		0.30000000000000004 1.0992195010299839 0
		0.30000000000000004 1.4999999999999998 0
		0.30000000000000004 1.5921889066910813 0
		0.24531319142442973 1.6625009536888689 0
		0.13906309605554285 1.7031250476844435 0
		0 1.7000000000000002 0
		0 1.75 0
		0 1.8 0
		0.30000000000000004 1.8000000000000003 0
		0.60000000000000009 1.8000000000000003 0
		0.60000000000000009 1.2023437857633326 0
		0.60000000000000009 0.60468757152666519 0
		0.60000000000000009 0.35625085831998171 0
		0.78750133516441601 0.20000000000000001 0
		0.9203128099488822 0.20000000000000001 0
		1.0109376668955521 0.20000000000000001 0
		1.2421881437399864 0.30468757152666515 0
		1.4000000000000001 0.45312581063553825 0
		1.4000000000000001 0.97656290531776913 0
		1.4000000000000001 1.5 0
		1.4000000000000001 1.6156252384222172 0
		1.2843762874799727 1.6968764782177463 0
		1.1000000000000001 1.7000000000000002 0
		1.1000000000000001 1.75 0
		1.1000000000000001 1.8 0
		1.4000000000000001 1.8000000000000003 0
		1.7000000000000002 1.8000000000000003 0
		;
createNode transform -n "c_Char_e_1" -p "c_Text_Tongue_1";
createNode transform -n "c_tongue_curve9" -p "c_Char_e_1";
createNode nurbsCurve -n "c_tongue_curveShape9" -p "c_tongue_curve9";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		2 22 1 no 3
		25 0 0 1 1 2 2 3 4 4 4.1062611577537087 4.1062611577537087 5.1062611577537087
		 6.1062611577537087 6.1062611577537087 7.1062611577537087 8.1062611577537087 8.1062611577537087
		 9.1062611577537087 10.106261157753709 10.106261157753709 11.106261157753709 12.106261157753709
		 12.106261157753709 13.30626115775371 13.30626115775371
		24
		0.40000000000000002 1.1000000000000001 0
		0.3968764782177463 0.72500038147554746 0
		0.58125123979552906 0.51250019073777364 0
		0.76406347753109038 0.30000000000000004 0
		1.0109376668955521 0.30000000000000004 0
		1.1750011444266424 0.30000000000000004 0
		1.4171877622644389 0.43125047684443429 0
		1.5 0.70000000000000007 0
		1.5500000000000003 0.68203173876554524 0
		1.6000000000000003 0.6640634775310903 0
		1.5593759060044252 0.36250095368886859 0
		1.1687510490577553 0 0
		0.87343862058442068 0 0
		0.55468833447776 0 0
		0.10000000000000001 0.47656366826886398 0
		0.10000000000000001 0.87812619211108578 0
		0.10000000000000001 1.3125001907377738 0
		0.56718852521553376 1.8 0
		0.91875028610666054 1.8 0
		1.2171877622644389 1.8 0
		1.6000000000000001 1.4187502861066605 0
		1.6000000000000001 1.1000000000000001 0
		1 1.1000000000000001 0
		0.40000000000000002 1.1000000000000001 0
		;
createNode transform -n "c_tongue_curve10" -p "c_Char_e_1";
createNode nurbsCurve -n "c_tongue_curveShape10" -p "c_tongue_curve10";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		2 9 1 no 3
		12 0 0 0.80000000000000016 0.80000000000000016 1.8000000000000003 1.8000000000000003
		 2.8000000000000003 3.8000000000000003 3.8000000000000003 4.8000000000000007 5.8000000000000007
		 5.8000000000000007
		11
		0.40000000000000002 1.2000000000000002 0
		0.80000000000000004 1.2000000000000002 0
		1.2000000000000002 1.2000000000000002 0
		1.1906263828488595 1.3796887159533076 0
		1.1609384298466467 1.4546883344777601 0
		1.1125001907377736 1.5687510490577554 0
		0.9265629053177693 1.7000000000000002 0
		0.82500038147554733 1.7000000000000002 0
		0.66718852521553373 1.7000000000000002 0
		0.42031280994888232 1.4359380483710995 0
		0.40000000000000002 1.2000000000000002 0
		;
createNode transform -n "Text_Text_xx_8" -p "c_Text_Tongue_1";
	setAttr ".t" -type "double3" -180.50887148417249 -96.966439453634706 -4.051186284857432e-014 ;
	setAttr ".r" -type "double3" 1.2722218725854073e-014 0 0 ;
	setAttr ".s" -type "double3" 3.0830967622604182 4.1666666666666652 4.166666666666667 ;
	setAttr ".rp" -type "double3" 186.25977095767342 103.35874023895869 0 ;
	setAttr ".sp" -type "double3" 60.413209613672421 24.806097657350094 0 ;
	setAttr ".spt" -type "double3" 125.846561344001 78.552642581608595 0 ;
createNode transform -n "Text_Char_x_32" -p "Text_Text_xx_8";
	setAttr ".rp" -type "double3" 59.689124103592931 24.814709033034241 0 ;
	setAttr ".sp" -type "double3" 59.689124103592931 24.814709033034241 0 ;
createNode transform -n "Text_curve361" -p "Text_Char_x_32";
	setAttr ".rp" -type "double3" 59.689124103592931 24.814709033034241 0 ;
	setAttr ".sp" -type "double3" 59.689124103592931 24.814709033034241 0 ;
createNode nurbsCurve -n "Text_curveShape361" -p "Text_curve361";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		2 64 0 no 3
		67 0 0 0.26590124240527646 0.26590124240527646 0.540900860929729 0.540900860929729
		 2.2627746688186434 2.2627746688186434 2.6284006701919553 2.6284006701919553 2.8834292168530653
		 2.8834292168530653 3.8834292168530653 3.8834292168530653 4.8428051228574907 4.8428051228574907
		 4.9790655472257903 4.9790655472257903 5.3674376536332966 5.3674376536332966 5.6049071130790882
		 5.6049071130790882 6.2752191600768761 6.2752191600768761 6.9611564454968811 6.9611564454968811
		 8.6517813024435508 8.6517813024435508 9.1688523943903615 9.1688523943903615 9.5572245007978669
		 9.5572245007978669 10.62284897626899 10.62284897626899 11.490035975582334 11.490035975582334
		 12.490035975582334 13.490035975582334 13.490035975582334 13.892545528620637 13.892545528620637
		 14.892545528620637 15.892545528620637 15.892545528620637 15.970389958351628 15.970389958351628
		 16.970389958351628 16.970389958351628 17.823514243084976 17.823514243084976 19.468825908607215
		 19.468825908607215 19.641183658573343 19.641183658573343 20.641183658573343 20.641183658573343
		 21.859932418777813 21.859932418777813 22.545869704197816 22.545869704197816 23.245869704197816
		 23.245869704197816 23.546665341197322 23.546665341197322 24.546665341197322 25.546665341197322
		 25.546665341197322
		66
		59.280376971453052 24.162550939344296 0
		59.325155564374157 24.18206977724347 0
		59.369934157295269 24.201588615142644 0
		59.369934157295269 24.252107844868299 0
		59.369934157295269 24.30262707459395 0
		59.686253645031542 24.30262707459395 0
		60.002573132767822 24.30262707459395 0
		60.002573132767822 24.235459185212285 0
		60.002573132767822 24.16829129583062 0
		60.047351725688927 24.182069496925251 0
		60.092130318610039 24.195847698019882 0
		60.086389401487281 24.240625730304554 0
		60.086389401487281 24.313534256490762 0
		60.086389401487281 24.489777889295603 0
		60.086389401487281 24.666021522100444 0
		60.108778697947834 24.677216030171611 0
		60.131167994408386 24.688410538242778 0
		60.078065351977493 24.736059589725269 0
		60.024962709546593 24.78370864120776 0
		59.997119541819416 24.750124836676036 0
		59.969276374092232 24.716541032144313 0
		59.84613566403651 24.716541032144313 0
		59.722994953980788 24.716541032144313 0
		59.722994953980788 24.842552200761418 0
		59.722994953980788 24.968563369378526 0
		60.033573804912521 24.968563369378526 0
		60.344152655844255 24.968563369378526 0
		60.276985046780808 25.035730978441972 0
		60.209817437717362 25.102898587505418 0
		60.162168386234868 25.049795945074521 0
		60.114519334752373 24.996693302643624 0
		59.91875714436658 24.996693302643624 0
		59.722994953980788 24.996693302643624 0
		59.722994953980788 25.156001229936315 0
		59.722994953980788 25.315309157229002 0
		59.8906274914197 25.332531908597293 0
		60.075481658954025 25.354920924739627 0
		60.148390185140236 25.349180007616866 0
		60.103611872537343 25.408023567170524 0
		60.058833559934456 25.466867126724186 0
		59.862496997518164 25.399699517660736 0
		59.387156348027119 25.321050074351767 0
		59.140874927915668 25.298661058209429 0
		59.143458340620917 25.284595811258662 0
		59.146041753326159 25.270530564307894 0
		59.392323173437603 25.28201239855342 0
		59.638604593549054 25.310142331818518 0
		59.638604593549054 25.15341781723107 0
		59.638604593549054 24.996693302643624 0
		59.336350072445327 24.996693302643624 0
		59.034095551341601 24.996693302643624 0
		59.056484847802153 24.974304006183068 0
		59.078874144262713 24.951914709722512 0
		59.129393093670146 24.968563369378526 0
		59.190820346247264 24.968563369378526 0
		59.414712469898163 24.968563369378526 0
		59.638604593549054 24.968563369378526 0
		59.638604593549054 24.842552200761418 0
		59.638604593549054 24.716541032144313 0
		59.510010012226708 24.716541032144313 0
		59.381415430904354 24.716541032144313 0
		59.330896201178703 24.738930048286651 0
		59.280376971453052 24.761319064428985 0
		59.286117888575809 24.655113779567191 0
		59.286117888575809 24.325016090736288 0
		59.280376971453052 24.162550939344296 0
		;
createNode transform -n "Text_curve362" -p "Text_Char_x_32";
	setAttr ".rp" -type "double3" 59.686253645031542 24.509296727194773 0 ;
	setAttr ".sp" -type "double3" 59.686253645031542 24.509296727194773 0 ;
createNode nurbsCurve -n "Text_curveShape362" -p "Text_curve362";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 2 no 3
		5 0 1.7218738078889144 2.6968734264133669 4.4187472343022813 5.3937468528267338
		
		5
		59.369934157295269 24.688410538242778 0
		60.002573132767822 24.688410538242778 0
		60.002573132767822 24.330182916146772 0
		59.369934157295269 24.330182916146772 0
		59.369934157295269 24.688410538242778 0
		;
createNode transform -n "Text_Char_x_33" -p "Text_Text_xx_8";
	setAttr ".rp" -type "double3" 61.157100727189018 24.806097657350094 0 ;
	setAttr ".sp" -type "double3" 61.157100727189018 24.806097657350094 0 ;
createNode transform -n "Text_curve363" -p "Text_Char_x_33";
	setAttr ".rp" -type "double3" 60.919143356587355 25.220298660756598 0 ;
	setAttr ".sp" -type "double3" 60.919143356587355 25.220298660756598 0 ;
createNode nurbsCurve -n "Text_curveShape363" -p "Text_curve363";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		2 6 0 no 3
		9 0 0 0.067784778425098294 0.067784778425098294 1.0677847784250982 2.0677847784250982
		 3.0677847784250982 4.0677847784250982 4.0677847784250982
		8
		60.779066941019479 25.37156958439564 0
		60.773613350071081 25.360374796006251 0
		60.768159759122675 25.349180007616866 0
		60.913402719782809 25.242974722755072 0
		61.008700262111361 25.069027737117555 0
		61.070126954052043 25.209103872367209 0
		60.974829411723498 25.30440197533219 0
		60.779066941019479 25.37156958439564 0
		;
createNode transform -n "Text_curve364" -p "Text_Char_x_33";
	setAttr ".rp" -type "double3" 60.807197154602804 24.949044251161133 0 ;
	setAttr ".sp" -type "double3" 60.807197154602804 24.949044251161133 0 ;
createNode nurbsCurve -n "Text_curveShape364" -p "Text_curve364";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		2 6 0 no 3
		9 0 0 0.064081450900134743 0.064081450900134743 1.0640814509001348 2.0640814509001348
		 3.0640814509001348 4.0640814509001348 4.0640814509001348
		8
		60.672861656157693 25.102898587505418 0
		60.664537606647905 25.094574257677412 0
		60.656213557138116 25.086249927849405 0
		60.801456517798258 24.962822452255764 0
		60.896754060126803 24.795189914816849 0
		60.958180752067491 24.918043859334652 0
		60.891013143004038 25.019082318785959 0
		60.672861656157693 25.102898587505418 0
		;
createNode transform -n "Text_curve365" -p "Text_Char_x_33";
	setAttr ".rp" -type "double3" 61.157100727189018 24.806097657350094 0 ;
	setAttr ".sp" -type "double3" 61.157100727189018 24.806097657350094 0 ;
createNode nurbsCurve -n "Text_curveShape365" -p "Text_curve365";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		2 40 0 no 3
		43 0 0 0.46980385166832 0.46980385166832 1.4698038516683201 2.4698038516683201
		 2.4698038516683201 4.1760539470372073 4.1760539470372073 4.3484116970033346 4.3484116970033346
		 5.3484116970033346 5.3484116970033346 6.6140361724744565 6.6140361724744565 7.6140361724744565
		 8.6140361724744565 8.6140361724744565 8.6765746902350696 8.6765746902350696 9.6765746902350696
		 10.67657469023507 10.67657469023507 11.67657469023507 12.67657469023507 13.67657469023507
		 14.67657469023507 14.67657469023507 15.67657469023507 15.67657469023507 17.200012547868397
		 17.200012547868397 17.653540786648872 17.653540786648872 18.020352631698941 18.020352631698941
		 18.96410177337896 18.96410177337896 19.96410177337896 20.96410177337896 20.96410177337896
		 21.19285212119263 21.19285212119263
		42
		61.338797950942265 25.399699517660736 0
		61.26043555348943 25.435866734897704 0
		61.182073156036601 25.472033952134669 0
		61.187814073159359 25.354920924739627 0
		61.176332799550273 24.923784776457413 0
		61.153943222771503 24.738930048286651 0
		60.840493913278387 24.738930048286651 0
		60.527044603785271 24.738930048286651 0
		60.54943390024583 24.716540751826095 0
		60.571823196706383 24.694151455365539 0
		60.622342706750253 24.710800115021552 0
		60.683769398690941 24.710800115021552 0
		60.91627289802598 24.710800115021552 0
		61.148776397361011 24.710800115021552 0
		61.086775613708056 24.492648628175203 0
		60.773326584533159 24.263015307083329 0
		60.521877778374787 24.184939955486634 0
		60.524461191080029 24.173745447415463 0
		60.527044603785271 24.162550939344296 0
		60.745770182343897 24.207328971628968 0
		61.092516530830814 24.392183699799734 0
		61.187814073159359 24.576464336258223 0
		61.534560421646276 24.380702426190645 0
		61.730896423426131 24.140161362565522 0
		61.74180416595938 24.35831284941187 0
		61.48461500331468 24.492648628175203 0
		61.198721815692615 24.604594830159758 0
		61.221110831834949 24.660854696689956 0
		61.232592666080471 24.710800115021552 0
		61.512458171041864 24.710800115021552 0
		61.792323676003249 24.710800115021552 0
		61.736350575010974 24.772513852818374 0
		61.680377474018691 24.834227590615196 0
		61.632728422536204 24.786578819450924 0
		61.585079371053709 24.738930048286651 0
		61.411706477128469 24.738930048286651 0
		61.238333583203236 24.738930048286651 0
		61.254981682222805 24.923784776457413 0
		61.265889424756054 25.175807113691626 0
		61.271630341878819 25.349180007616866 0
		61.305214146410542 25.374439762638801 0
		61.338797950942265 25.399699517660736 0
		;
createNode transform -n "tongue_Mo" -p "Tongue_CTRL_FRAME";
	setAttr ".v" no;
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" -0.016199337489479326 -1.1039667583415613 0.18697255440670127 ;
	setAttr ".s" -type "double3" 1.6737132556643721 1.6737132556643721 1.6737132556643721 ;
createNode transform -n "polyToCurve1" -p "tongue_Mo";
createNode nurbsCurve -n "polyToCurveShape1" -p "polyToCurve1";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 30;
	setAttr ".cc" -type "nurbsCurve" 
		3 52 0 no 3
		57 0 0 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
		 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52
		 52 52
		55
		-0.085021004080772719 -0.025496006011962988 -0.16833050549030368
		-0.084226075847065388 -0.025900636727909428 -0.16480477703291721
		-0.082636219379650239 -0.026709898159802126 -0.15775332011814322
		-0.080710646025293264 -0.0273752854234506 -0.14714715750616814
		-0.080170543802432562 -0.026093540332441205 -0.13733460864188327
		-0.080074157532571494 -0.024866525738495421 -0.1257318128272133
		-0.079690305691867871 -0.025585338069607728 -0.10900571823841457
		-0.079313616512118754 -0.027183649130312768 -0.090226265716331827
		-0.079055865058651156 -0.029290702568767629 -0.071132798547064641
		-0.078734429306962714 -0.031710879282070094 -0.052384012867646199
		-0.078205649081644471 -0.034090010567147742 -0.035475258830979545
		-0.07746445860461848 -0.036532988872599897 -0.019635917675521249
		-0.076468116958251051 -0.039059528539432856 -0.0046932610805313565
		-0.075186078792216254 -0.041570995187303568 0.0096510321234434503
		-0.073573204756285662 -0.043905949007708708 0.023656959921925701
		-0.071630580636416932 -0.046272520626304513 0.03761222018743797
		-0.069342452732523083 -0.048857397791930428 0.051817138685108989
		-0.066714110745452526 -0.051563469326441007 0.066493829722590839
		-0.063721731736690879 -0.054362179846168653 0.082205551584250067
		-0.060436944623378779 -0.057234549715252242 0.098229108706690133
		-0.056898604014066795 -0.060175976357756539 0.11415092991850791
		-0.05318114287400099 -0.063114773219988332 0.12960531085433419
		-0.049217179110838671 -0.066334600093999108 0.14438858705913726
		-0.045471124258634317 -0.068764815364202467 0.15760088882712731
		-0.041947045047877954 -0.069421854233772298 0.16822194296731841
		-0.039958683205309244 -0.068328146039145804 0.17640884844291235
		-0.042203711080884318 -0.064884620693934913 0.18214909488039752
		-0.044534470590701973 -0.059972211669763506 0.18493079006398452
		-0.042071789025730291 -0.05388973396068996 0.18410480331186155
		-0.039707860259563327 -0.047784472912983336 0.18006998202062424
		-0.041645623034586465 -0.043375468206757313 0.17287820666672712
		-0.045073625331905808 -0.039246271834515602 0.16292071088688054
		-0.048603994757404616 -0.034375290980809471 0.15026206708264059
		-0.052168886475675295 -0.029296999749607731 0.13593360299433632
		-0.055178698777308743 -0.024252828743208818 0.12095804025766463
		-0.057810829891412126 -0.019100315650127479 0.10542576958450156
		-0.060037489551921376 -0.01376751471218597 0.089595627718125181
		-0.061884708585086878 -0.0082843068772433144 0.073985266432252492
		-0.063341041037896173 -0.0025804047541578704 0.059404633486489056
		-0.064491127011145954 0.003115632416331328 0.04523576699590863
		-0.065397062938209544 0.0085013780755473067 0.031226989412785112
		-0.066115100919784009 0.013868721565898577 0.017089395494941644
		-0.066732751311996755 0.019405388521395544 0.0024305885653783895
		-0.067218380485323539 0.025121443508606619 -0.012690634619226674
		-0.067549500607774954 0.031166378842506892 -0.028263624779479697
		-0.0677860952362975 0.037309636911955837 -0.044536336160494364
		-0.067949389875236341 0.043561850858665464 -0.062102996525919288
		-0.068132813221986346 0.049348940739102932 -0.079914136040810269
		-0.068477822080809603 0.054166022927050854 -0.096354140462768759
		-0.068861378821915051 0.057816141612105319 -0.11371576018478288
		-0.06893926150851494 0.060429176646831402 -0.13492737943998756
		-0.069516524569272639 0.060519737416187831 -0.15646666127948486
		-0.071623988470890396 0.055564452607003906 -0.17507358308995152
		-0.073367995527538407 0.051059580312360672 -0.18695085881936674
		-0.074239999055862413 0.048807144165039049 -0.19288949668407435
		;
createNode transform -n "polyToCurve2" -p "tongue_Mo";
createNode nurbsCurve -n "polyToCurveShape2" -p "polyToCurve2";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 30;
	setAttr ".cc" -type "nurbsCurve" 
		3 52 0 no 3
		57 0 0 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
		 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52
		 52 52
		55
		-0.055179998278618067 -0.02940654754638683 -0.16757300496101443
		-0.054757027752845015 -0.029585540078561578 -0.16403379033513482
		-0.053911086701298544 -0.029943525142910866 -0.15695536108337446
		-0.052241136984663851 -0.030791464040388915 -0.14653387782619912
		-0.05188490130179859 -0.029760544764004769 -0.13732376260654011
		-0.051852494501443032 -0.028834736659107071 -0.12629746035612352
		-0.051671984908561827 -0.029556437778272427 -0.10962152381634166
		-0.051504308973600497 -0.031060542528966593 -0.090729194596896309
		-0.05139906892352001 -0.033068837784034973 -0.0715738139682012
		-0.051218402808864166 -0.035363044199906581 -0.052761859206918504
		-0.050834977021966488 -0.037593572816656137 -0.035810603530557934
		-0.050266831116619587 -0.039876139356119986 -0.019940933331729617
		-0.04949354689365125 -0.042246287787231586 -0.0049806878132574329
		-0.048503231058837248 -0.044594944408692751 0.0093736511826573964
		-0.047276189105344708 -0.04675105779842912 0.023388565955107545
		-0.045815495879264236 -0.048936105087898044 0.037347324877378185
		-0.044112944987487364 -0.051325811973318307 0.051547053760708166
		-0.042182707992407302 -0.053886381338253637 0.066212684942048058
		-0.039996019273839133 -0.056685011347618566 0.081886909918833253
		-0.03767343928011252 -0.059594441852081105 0.097913532325914474
		-0.035295340832593988 -0.062536926690873254 0.11392254831213398
		-0.032953454158330717 -0.065431122074538772 0.12959800471124699
		-0.030703243255377842 -0.068484482174233682 0.14476742908500992
		-0.028733946683130285 -0.070752866945036949 0.1586304648156463
		-0.026791872694618028 -0.071420060062065693 0.17042155764196518
		-0.026261309735526959 -0.070309744537072408 0.17986409627441194
		-0.030108588971749794 -0.066696696970291861 0.18669092903691445
		-0.033333946375075897 -0.061411420271377359 0.19010865926951248
		-0.02991048543921955 -0.054534730757669903 0.18893479101658783
		-0.025885968291902248 -0.047590464806305528 0.18406955989591459
		-0.026336421751977191 -0.042646140591487691 0.17580211998523201
		-0.028150077008659943 -0.038151529039313056 0.16478339876288101
		-0.029849263187414814 -0.033141685375603122 0.15147508164615636
		-0.031607612715524702 -0.027928274875396446 0.1367345853379564
		-0.033079816722174166 -0.022450148199986655 0.12157864247775699
		-0.03434500587605379 -0.01686080441528828 0.1059909906694938
		-0.035367336316188387 -0.011342724195517842 0.090125911025814728
		-0.036146523338625176 -0.0057478133804717748 0.074488282152916641
		-0.036636825812755583 0.00012289349578947784 0.059828989280665427
		-0.036938791525143524 0.0059343018625155966 0.04556431592352158
		-0.037117121980981216 0.011294495052706492 0.031457291083753211
		-0.03723359253998005 0.016572904818191056 0.017218518834292387
		-0.037390287460803348 0.021988079062292415 0.0024508606112228796
		-0.037531003903416765 0.02760075266355903 -0.012759471376155103
		-0.037634456696365011 0.033587938060313592 -0.028399012376468611
		-0.037698021796516178 0.039819350476628525 -0.044646692107428478
		-0.037680815036888131 0.046493651442502358 -0.061960434782765028
		-0.037676309265157144 0.052801014478561177 -0.079489792163154133
		-0.037789189063737863 0.05804420219320236 -0.095727071273170483
		-0.0379448009514518 0.062084108852915043 -0.11310205346943672
		-0.037982732108602639 0.064981437620134308 -0.1347370699005114
		-0.038264878077831313 0.065439524415488656 -0.1570469570290739
		-0.041726157070604245 0.058428897918265256 -0.17573792905278546
		-0.040900051594246513 0.056282087982032422 -0.18928464641394727
		-0.040486998856067651 0.055208683013916002 -0.19605800509452814
		;
createNode transform -n "polyToCurve3" -p "tongue_Mo";
createNode nurbsCurve -n "polyToCurveShape3" -p "polyToCurve3";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 30;
	setAttr ".cc" -type "nurbsCurve" 
		3 52 0 no 3
		57 0 0 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
		 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52
		 52 52
		55
		-0.019902499392628746 0.046973705291748227 -0.19323749840259624
		-0.019293729023385962 0.049724300620081638 -0.18724662780345935
		-0.018076188284900253 0.055225491276748119 -0.17526488660518447
		-0.016622238303269702 0.061340094607723133 -0.15651296445753299
		-0.016271601165361124 0.061433132740682059 -0.13484107822855954
		-0.016320843864464203 0.058609022697060177 -0.1135542159724595
		-0.016255887819779609 0.054725714287709802 -0.096227909308752801
		-0.01623959912049917 0.049638226599464465 -0.079910097320992565
		-0.016279699498053819 0.043608300262886854 -0.062364293828224567
		-0.016327588148343623 0.037273720457700429 -0.045019172133001155
		-0.016324680894397165 0.031428819331265304 -0.028697492064778597
		-0.016308671938297676 0.025865696611055266 -0.012980329048006344
		-0.016293494718120444 0.020701014626342457 0.0022670907382659079
		-0.016291847348486162 0.015755417719148249 0.017074549135277131
		-0.016342492497386653 0.010986651284391431 0.031392093424841484
		-0.016381181118942895 0.0061000744927509542 0.045593701106181259
		-0.016369660491708186 0.00065603907270437374 0.059964445543291132
		-0.016268670782692583 -0.0049526872542111824 0.074721086423657893
		-0.01601477145822388 -0.010411101187777686 0.090403873762881629
		-0.015642240722026045 -0.015925557737994971 0.10632740995045337
		-0.015156509104881311 -0.021706796768394005 0.12201520736061036
		-0.014580712627491431 -0.027426660400971737 0.13738078597705161
		-0.013887010853397688 -0.032770833921182491 0.15254864270984358
		-0.013233735744105263 -0.037908527707918728 0.16640926975846548
		-0.012468413816623147 -0.042615080505310925 0.17814549320188339
		-0.012495598616529225 -0.047757792502031757 0.18700480830812091
		-0.015242432417445455 -0.054768287395927026 0.19194914899340626
		-0.017488664376384466 -0.061728933403616675 0.19301811479926229
		-0.015374527543984662 -0.067307115539870538 0.18960632391920637
		-0.012745712512985608 -0.071179407108044934 0.1826105649064412
		-0.0127724877799253 -0.072261740742603567 0.17250974083225523
		-0.013621330332300213 -0.071503423464954308 0.15995194752187383
		-0.014447558066262668 -0.069258489970311532 0.1455063714912691
		-0.015454933516203117 -0.066228689871697624 0.12988864373935774
		-0.01658495014256519 -0.063283813729640662 0.113972714479495
		-0.017779761003468328 -0.060273773397580298 0.097853080802819056
		-0.018980869396889116 -0.057307858816565645 0.081807646733005335
		-0.020131746001524356 -0.054477726281532114 0.066160409917128959
		-0.02115025741777208 -0.051940640804806384 0.051503806604852168
		-0.022054708013316434 -0.049609066187361946 0.037310424946048366
		-0.022834891803297772 -0.047493134373785176 0.023350419241316606
		-0.023494206444357974 -0.045457105943951047 0.0093234378896829562
		-0.024030396057718319 -0.04333124668579616 -0.0050608875648929892
		-0.024450204088837645 -0.04122767291965572 -0.020062352256616692
		-0.024757031125458708 -0.039230288234741971 -0.035982290856181737
		-0.024958672213988477 -0.037253996612539773 -0.052986453210213613
		-0.02503964614544232 -0.035115217446044747 -0.071849370189897829
		-0.025073238152660476 -0.033193308089880726 -0.091046033392320536
		-0.025132017954368792 -0.031711710286860484 -0.11000247153341866
		-0.025202684411826753 -0.030954590265313536 -0.12664005942434381
		-0.025200236471849227 -0.031764471411928188 -0.13734330241569104
		-0.025412365948171051 -0.032689723994449263 -0.1461487034945835
		-0.02623315477484045 -0.032222530830184823 -0.15629793903193692
		-0.026916717321056712 -0.03165682871748348 -0.16313930915780139
		-0.027258498594164841 -0.031373977661132806 -0.16655999422073361
		;
createNode transform -n "polyToCurve4" -p "tongue_Mo";
createNode nurbsCurve -n "polyToCurveShape4" -p "polyToCurve4";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 30;
	setAttr ".cc" -type "nurbsCurve" 
		3 52 0 no 3
		57 0 0 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
		 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52
		 52 52
		55
		0.00068200123496353886 0.038738727569580224 -0.19041699171066356
		0.00078242423393194986 0.043318525150755516 -0.18517768978634491
		0.00098327023186876557 0.05247812031310576 -0.17469908593770664
		0.001054548901257265 0.057165322366340476 -0.15595929631890118
		0.0010947921168957251 0.057812192810367806 -0.13495096534151388
		0.0010841650897321668 0.055089083571259259 -0.11403544066663003
		0.0010721786518887075 0.051422166036050543 -0.096748910982718594
		0.0010497508136610655 0.046555840902027912 -0.080320463908973322
		0.0010240450732189991 0.040861643436738732 -0.062693195646259997
		0.00099583021113206979 0.034884341316490465 -0.045261179731019369
		0.00096826817459968193 0.029348171664920389 -0.028872131479345
		0.0009413569317216977 0.024086261407418715 -0.013108143522123666
		0.00091634316209975248 0.019232168448058667 0.0021437208855818774
		0.00089265106035856098 0.014608836974469009 0.016950680651908554
		0.00087030828978052139 0.010198208843375517 0.03129933598317132
		0.0008487455360411631 0.0056568489516718003 0.045544468553874402
		0.00082740166162251531 0.0005111688924296161 0.059967852085222373
		0.00080627979939206906 -0.0048664295661517793 0.074775088291682335
		0.00078517488260492147 -0.010201196704924285 0.090483079019155727
		0.00076415316651323132 -0.015673764785676583 0.10643956349379242
		0.00074325039014551224 -0.021498815409147821 0.12218623748918682
		0.00072235303566533528 -0.027299450825625099 0.13765815548424365
		0.00070309585920396854 -0.032710662332245032 0.15302918358455181
		0.00068027257166847742 -0.03791146439767782 0.16712502973076498
		0.00066772801452222145 -0.042682996052743172 0.17911526216195864
		0.00060994914018141198 -0.047853874907136662 0.18814265782323797
		0.00038607746241279336 -0.054778767985408955 0.19297418129477345
		0.00020599972656376944 -0.061660666073820397 0.19390728494546883
		0.00031965064535907937 -0.067308904145288381 0.19062658337466784
		0.00048603341836908056 -0.071259116664358774 0.1837375544711437
		0.00051094239636337367 -0.072303480348968885 0.17346004136568166
		0.00050395420529167345 -0.071481703411816658 0.16063565233845317
		0.00051571656787520741 -0.069210200295211494 0.1459323628557021
		0.00052881054456902627 -0.066151029028229918 0.13009109330379923
		0.00054304935631105009 -0.063146001668733021 0.11405987975037261
		0.00055737586248246959 -0.06007227057342767 0.09788544002245346
		0.00057048685117369797 -0.057059842597940579 0.081829716482190049
		0.00058293515424342037 -0.054191966301490133 0.066194982195662888
		0.00059493722799195791 -0.05162093933051299 0.051544792231529114
		0.0006062017814078899 -0.04926962129194995 0.037357131119908786
		0.00061636016648830918 -0.047147603983775176 0.023399099965010987
		0.00062586929237765446 -0.045146988477608709 0.0093669264734296594
		0.00063495213907120468 -0.043142161015113124 -0.0050365805805891919
		0.00064395581585688561 -0.041195857884071846 -0.020064007416436182
		0.00065341886377400351 -0.039368088334309576 -0.036013231784536678
		0.0006629983494478753 -0.037541419721532826 -0.053045547965873775
		0.00067325121171215685 -0.035483452535411991 -0.071929977452012572
		0.00068200380215384447 -0.033599096623839579 -0.091141138130575519
		0.00068727157983666397 -0.03210641420128317 -0.11011785203602026
		0.00068904276416261226 -0.031333548657576316 -0.12673628235027379
		0.00068606540787212705 -0.032088079927418488 -0.13735166644582275
		0.00068007547001839273 -0.033149760590694001 -0.14596538026798955
		0.0005365767048612929 -0.032408435730283486 -0.15609750579812326
		0.0006208597060894203 -0.033030417094013761 -0.16239715758634338
		0.00066300120670348395 -0.033341407775878899 -0.16554698348045346
		;
createNode transform -n "polyToCurve5" -p "tongue_Mo";
createNode nurbsCurve -n "polyToCurveShape5" -p "polyToCurve5";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 30;
	setAttr ".cc" -type "nurbsCurve" 
		3 52 0 no 3
		57 0 0 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
		 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52
		 52 52
		55
		0.02786200121045123 -0.030302524566650505 -0.16647198796272342
		0.027656341130718277 -0.030609967411029834 -0.16305457522520309
		0.027245020971252178 -0.031224853099788282 -0.15621974975016129
		0.026750916562550003 -0.031752322886148064 -0.14607838156970882
		0.02662743786908606 -0.030847822205910865 -0.13727487765209437
		0.026622838550800991 -0.030043251207481737 -0.12657155665706443
		0.02654720971841782 -0.030805406798724577 -0.10993461879374408
		0.026462833609082387 -0.032292486985411629 -0.090979458341990144
		0.026390721740428332 -0.034227843186342866 -0.071786019754782757
		0.026264788557538797 -0.036382812070300821 -0.052926942128817031
		0.026021631810400646 -0.038374954107265109 -0.035926325969109586
		0.025674190750412731 -0.040388949312374439 -0.020009731503661664
		0.025216117469415562 -0.042506790107601479 -0.0050104883479457525
		0.024641848844007316 -0.044654099742324593 0.0093706558588210684
		0.023943250188384307 -0.046729892133450565 0.023391181944912076
		0.023121665930070458 -0.048895987700574448 0.037343074892352481
		0.022171962880004857 -0.051285762612868442 0.051527396007958214
		0.02110549508143934 -0.053883563538434563 0.066174397145622232
		0.019904811854677292 -0.056770083037988792 0.081815101394975054
		0.018651261233310717 -0.059789659601301164 0.097848256364120784
		0.017399145262749858 -0.062852854702824715 0.11394253629772078
		0.016212173590448478 -0.065841691960900756 0.129819184309728
		0.015152423308587669 -0.068893189961912404 0.14537235934586187
		0.014279144417813309 -0.071152925273486267 0.15975198816590996
		0.013458254792847169 -0.071901862954744516 0.17224589466934648
		0.01333184466792172 -0.070870856118309344 0.18233445697344491
		0.015295125624778966 -0.067295090529163049 0.18948293597389201
		0.016954662671496545 -0.061942533289327376 0.19302432842085757
		0.015428738858949345 -0.054754536636063396 0.19183614556798761
		0.013577394876677475 -0.047446130928594822 0.18675010480043755
		0.013781322925781787 -0.042250595338300542 0.17791823535015014
		0.014596823582773186 -0.037554535665935494 0.16625747055820517
		0.015341391089880481 -0.032409096323488241 0.15246309967047161
		0.016112119887252144 -0.027053940648648033 0.137352710053496
		0.016771509074205333 -0.021302245082965004 0.12201018968567376
		0.017340850091672504 -0.015484614725762156 0.10633201538071206
		0.017797471220926436 -0.0099415617634212323 0.090417068289490171
		0.018135777802703312 -0.0044565413820997785 0.074741665762326076
		0.018321303865236872 0.0011804198637767169 0.059996070369321072
		0.018418013987634159 0.0066485239101536494 0.045637148710435053
		0.018464768331851778 0.01154952970449903 0.031446964214985842
		0.018502414176474379 0.016325739655343646 0.01714009956786466
		0.01859795132680701 0.021269512397921405 0.0023451970127201407
		0.018711782364591381 0.026432438199612045 -0.012897858697415453
		0.018832926179888663 0.032005125072312769 -0.028635992581059491
		0.018942522477392587 0.037862878417775546 -0.04498013307989978
		0.019001745563908341 0.044209262465670113 -0.062325776211663422
		0.019059510522840821 0.050250108744239727 -0.079866188970331098
		0.019162595904850793 0.055341478647917601 -0.096182869530060722
		0.019278607966937394 0.059236246807595358 -0.11350675447852963
		0.019260846621889208 0.062095214625410254 -0.13478641951975578
		0.019499009452951011 0.062050663182122726 -0.15645049018232152
		0.020504373595567796 0.05599568219433302 -0.1751975094314259
		0.021345124736578014 0.050537658835285479 -0.1871764949638261
		0.021765500307083126 0.047808647155761705 -0.19316598773002619
		;
createNode transform -n "polyToCurve6" -p "tongue_Mo";
createNode nurbsCurve -n "polyToCurveShape6" -p "polyToCurve6";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 30;
	setAttr ".cc" -type "nurbsCurve" 
		3 52 0 no 3
		57 0 0 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
		 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52
		 52 52
		55
		0.055061001330614298 -0.027263641357421979 -0.1673969924449927
		0.054968047761199568 -0.027701011133734077 -0.16387092085927774
		0.054782140622369774 -0.028575750686358085 -0.15681877768784694
		0.053673294940465924 -0.029340853282953938 -0.14640229798093865
		0.053493222177688184 -0.028392307479471659 -0.13719702304908124
		0.053436721270500531 -0.02746472746690503 -0.12617049597828953
		0.053248598959127577 -0.028198135722897557 -0.10949580403626197
		0.053037768541606953 -0.029709665723679123 -0.090605650286091702
		0.052870913294166121 -0.031739271828996114 -0.071455656477403984
		0.052619440615420641 -0.034058513865925476 -0.052650064411327815
		0.052172959346516432 -0.036313009580174242 -0.035704538583766016
		0.051543369622509258 -0.038620539575569234 -0.019840253846025495
		0.050710380637098665 -0.041012421628140699 -0.004883704972589574
		0.049660263461952917 -0.043393661966839497 0.0094654480135050959
		0.048372022720153049 -0.045609601378350517 0.023470270029168926
		0.04684741282067615 -0.047870553965739499 0.0374160914800961
		0.045076115161366725 -0.050345770723312561 0.051601197696884621
		0.043073509860811147 -0.053003781763948786 0.066249811173445305
		0.040811819672236078 -0.055920484535966999 0.081907867881935909
		0.038410220438500946 -0.05894302802595696 0.097908445671526886
		0.035945431940143754 -0.061972442293457948 0.11387146673355347
		0.03351706749050911 -0.064922981578387898 0.12948228924378685
		0.031187111114276987 -0.067975128186576583 0.14455708669235506
		0.029145248684584145 -0.070231227977239283 0.15832315652401194
		0.027240466746647436 -0.070875907828098564 0.17001049838774876
		0.026556892013338378 -0.069842806990147874 0.17942731326897773
		0.029408358807144763 -0.066674628822304613 0.18648698824031143
		0.031954674965105366 -0.061728807878504544 0.19010423290991513
		0.029608826341500409 -0.054510291085360228 0.18874856266729823
		0.026925034975989547 -0.047119244683721313 0.18366903664790787
		0.027725722725229815 -0.042095696274440216 0.17545129023012696
		0.029619331871857422 -0.037625008704078741 0.1645550206676141
		0.031457612430351785 -0.03264022284381763 0.15134610560598377
		0.033333096589468147 -0.027438332220665544 0.13669172865493426
		0.034932559434934368 -0.021886162507151301 0.12157863784027538
		0.036325055818661689 -0.016207258136729269 0.10601392814869572
		0.03747543982909194 -0.010640096186674015 0.090163895255791202
		0.038383200595992581 -0.0050067044012505274 0.074537551020473741
		0.039002423724357541 0.00090682131955926201 0.059895588687676284
		0.039434240948818623 0.0067542083869943448 0.04564919264084006
		0.039742666461769549 0.012136075570275566 0.031559731636750167
		0.03999309378926072 0.017425652892534081 0.017337345810271756
		0.040291435009921349 0.022838140677065074 0.0025889490370357019
		0.040580036899614334 0.028448246792636626 -0.01261436644502179
		0.040839073913389645 0.034450087324189915 -0.028284666687865924
		0.041060930389184985 0.040700637946530387 -0.044565540594356329
		0.041205951112454578 0.047390885203706545 -0.061880244968784824
		0.04135051860215247 0.053712912573076234 -0.079401909214191907
		0.041594164270595479 0.058959906573242266 -0.095637639671259406
		0.041827830926989079 0.063019544624280444 -0.11300871762785282
		0.041911855601627669 0.065961322951466561 -0.13463202122021775
		0.042037631746971692 0.066532971657879539 -0.15692784389213912
		0.04455980858745761 0.059477120093903713 -0.17561490337955654
		0.04341926989138982 0.057744751192596797 -0.18914829029277858
		0.042849000543355935 0.056878566741943345 -0.19591498374938959
		;
createNode transform -n "polyToCurve7" -p "tongue_Mo";
createNode nurbsCurve -n "polyToCurveShape7" -p "polyToCurve7";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 30;
	setAttr ".cc" -type "nurbsCurve" 
		3 52 0 no 3
		57 0 0 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
		 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52
		 52 52
		55
		0.075420998036861711 0.049673080444336125 -0.19271849095821453
		0.074950743259181121 0.051897228892712526 -0.1867812494893073
		0.074010233703819442 0.05634552578946498 -0.17490676655149165
		0.072857568648429183 0.061223016555163566 -0.15630589970811748
		0.072502488301235166 0.061069837315049516 -0.13477951483165568
		0.072358978159699813 0.058413316037361218 -0.11357999019158219
		0.071929113173628212 0.054752282309761501 -0.096221602172786636
		0.071488065717054378 0.049936515846455976 -0.079782057308426302
		0.071188023774316572 0.044146137413299355 -0.061974877963587416
		0.070899836650320028 0.037888953443084676 -0.044406893027389378
		0.070556396414812997 0.031733458861454115 -0.028113749162949054
		0.07012358394399705 0.025677708955519962 -0.012522560116832473
		0.069536896871667878 0.019963146960364917 0.0025924056682524554
		0.068820332290864095 0.014428103957812992 0.017236965617530294
		0.06800579373550554 0.0090533081054350283 0.031362390079205799
		0.067005014813583993 0.0036530114111158491 0.045358051841686405
		0.065761144902247992 -0.0020665974101219094 0.059512895291620335
		0.064211929634841486 -0.0078006003220724958 0.074079475982417237
		0.062272394543930111 -0.013304699798282891 0.089681614715093422
		0.0599539834156015 -0.01869084559705551 0.10549454955025499
		0.057230673181580316 -0.024019644399012368 0.12098308208878503
		0.054129800559930198 -0.029200827892302668 0.13590261065433065
		0.050481495801909991 -0.034178128842138764 0.15017386582916051
		0.046851221123734112 -0.038910150703494434 0.16276601007747277
		0.043354276613339737 -0.042996116773619343 0.17261130106442027
		0.041171189501128982 -0.047457900289831205 0.179741273172803
		0.042649607583095536 -0.053860729070769262 0.1839250482382937
		0.04440340219519856 -0.060173762669718689 0.18488194275370815
		0.042515818247471797 -0.064856473155523356 0.18195033587273227
		0.040926338110198857 -0.068003150800125631 0.17604225085530129
		0.043028600486327166 -0.069044634237199129 0.16789698264321098
		0.046543269529178796 -0.068430750450351907 0.15737145297234187
		0.050344336299012325 -0.066123684185366363 0.14421723020960614
		0.054365414074514694 -0.063017200789369177 0.12948975881056496
		0.058144004050909567 -0.060072833902174778 0.11409749180731502
		0.061742567650750348 -0.057049463392151264 0.098232882427677665
		0.065081218398815643 -0.053992951492052195 0.082252075548900114
		0.068124545880910325 -0.051003884746180832 0.066572359858384153
		0.070802700899999141 -0.048211623746105783 0.051915777767579309
		0.073139158065882323 -0.045575708592102311 0.037724034100939441
		0.0751289118247076 -0.043156334452581144 0.023779963410298286
		0.076787687576512484 -0.040780896713473222 0.0097821295265759431
		0.078114988547765246 -0.038246345728727309 -0.0045573262144295258
		0.079154386298281171 -0.035704211762614471 -0.01949630177557846
		0.079932720596147117 -0.033244413420675363 -0.035330829954945311
		0.08049973474682702 -0.030848736033245155 -0.052234364911077281
		0.080871819235469281 -0.028409103381431339 -0.070976921601467888
		0.081176006401114567 -0.026285018718364434 -0.090064939834403973
		0.081589665797110827 -0.024680768807053419 -0.10884206342544603
		0.081978355079941667 -0.023953926898927679 -0.1255667847171775
		0.082116679621947949 -0.0251637451458036 -0.13716837254750613
		0.08245495523581893 -0.026409473609502167 -0.14697809654256574
		0.083535632571883206 -0.025668778367021628 -0.15757682886213195
		0.084416545457742992 -0.024800035141302128 -0.16462226697633706
		0.084857001900672899 -0.024365663528442376 -0.16814498603343961
		;
createNode transform -n "polyToCurve8" -p "tongue_Mo";
createNode nurbsCurve -n "polyToCurveShape8" -p "polyToCurve8";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 30;
	setAttr ".cc" -type "nurbsCurve" 
		3 56 0 no 3
		61 0 0 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
		 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52
		 53 54 55 56 56 56
		59
		0.11976899951696442 0.0073647499084472934 -0.18013697862625189
		0.11877256286477585 0.0082553224352215349 -0.17536986207642838
		0.11677968956039805 0.010036467488769954 -0.16583562897678017
		0.11718638657642672 0.011235121994537462 -0.1515173214246982
		0.1167401161107563 0.012475370968720012 -0.1361372778363307
		0.11643380547715994 0.012726602444958384 -0.11997366595649803
		0.11572441094434791 0.011219929115990894 -0.1028808982919405
		0.11497091590287405 0.0086848345449750553 -0.085085551823726763
		0.11440865704077566 0.0055749980077350542 -0.066355346000330787
		0.11386535192054398 0.0019489450590535217 -0.04792117651933895
		0.11329930019219833 -0.0020390262759517478 -0.031169805583557513
		0.11255404757758643 -0.0062225541325435282 -0.015401353125761264
		0.11146142461700895 -0.01040576555112185 -0.00045821088905943725
		0.11001487650509026 -0.014522895791046734 0.013899730234071438
		0.10815366914139285 -0.018409039661240179 0.027852648247489446
		0.10587221565472837 -0.022165745553531738 0.041737944719097669
		0.10315390886210293 -0.025701571168554031 0.055905449219906644
		0.099971165005784651 -0.029430583388726134 0.070498089272038697
		0.096316055890068919 -0.033992330462753378 0.086012185604783853
		0.092113141750209224 -0.038618925992866211 0.10173736582507145
		0.087296868785651488 -0.042643834764802137 0.1172483674562104
		0.081830008582435165 -0.046402551474065405 0.13218611435114014
		0.075537169515379116 -0.050145754621333999 0.14624374170048962
		0.068767466224040008 -0.053461357578426343 0.15883944243215686
		0.062349441791933469 -0.055848158485370045 0.16912919981033808
		0.054669508671030272 -0.057824181538143352 0.17759268860676122
		0.044149462887205219 -0.059997826637446086 0.18454371667049202
		0.03151167445055085 -0.061596764809041166 0.18963559981297082
		0.016639724355774505 -0.061715265540098985 0.19256636659888235
		0.00047194331297458045 -0.061361933347166366 0.19351532898956617
		-0.01699777059395817 -0.061567337492906972 0.19260222186645834
		-0.033052478421393743 -0.061359853226118644 0.1897037156269831
		-0.044147175667879401 -0.059870358409003288 0.18464327273107503
		-0.052772201435520687 -0.057821914463966603 0.17770025187264163
		-0.060074966184068435 -0.055881921701954898 0.16916962832277369
		-0.066539430153069165 -0.053348241319539448 0.15882810421671387
		-0.073265760973417582 -0.049356076576193633 0.14631947636771808
		-0.079552925744787145 -0.045060801594202227 0.13233725719903369
		-0.085003556488356474 -0.041525914445963222 0.11733284859458676
		-0.089806960182973364 -0.038162246540474669 0.10167651309301773
		-0.093998410992349513 -0.034833088542876693 0.08568389212717395
		-0.097642549968929709 -0.03124456075869303 0.069970519129976622
		-0.10081335896947272 -0.026809172064002761 0.055514739789896642
		-0.10351813449480537 -0.02227104740969188 0.041543892811496397
		-0.10578129243257524 -0.018337967237244897 0.027690061354487195
		-0.10762527765919722 -0.014531473951396048 0.013717447158043503
		-0.1090594105065823 -0.01060014981674947 -0.00068156421050716916
		-0.1101472122750245 -0.0065706556950693848 -0.015659452251811565
		-0.11090833988972662 -0.002233669580957312 -0.031401608877571069
		-0.11148366210454724 0.0019542776593790621 -0.048116933639020219
		-0.11199457388109182 0.0056182237741384091 -0.06654614482807536
		-0.11251893000358333 0.0087227849255940206 -0.085279323420740419
		-0.11324869225953665 0.011267328818569074 -0.10307412970196221
		-0.11396266637982881 0.012772638573529144 -0.12016872285072988
		-0.11420116714293348 0.012499485974328177 -0.13634054864770914
		-0.11487140567627735 0.011227272735723768 -0.15172940757282927
		-0.11550686119915743 0.0099918040700125912 -0.16604742342590847
		-0.11834828674436176 0.0081870288672502879 -0.17558579621831427
		-0.11976899951696393 0.0072846412658691389 -0.18035498261451718
		;
createNode transform -n "polyToCurve9" -p "tongue_Mo";
createNode nurbsCurve -n "polyToCurveShape9" -p "polyToCurve9";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 30;
	setAttr ".cc" -type "nurbsCurve" 
		3 56 0 no 3
		61 0 0 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
		 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52
		 53 54 55 56 56 56
		59
		-0.11388099938631101 0.024845123291015719 -0.1850379854440696
		-0.11337714331650724 0.02599463643552221 -0.17990010728375105
		-0.11236943117689896 0.028293662724535002 -0.16962435096311293
		-0.11111178993811473 0.030967976829016277 -0.15362800662382084
		-0.11065675503337682 0.031656763787367356 -0.13578657047861586
		-0.11037417503222069 0.030897027746440497 -0.11755617016270767
		-0.10969413621015965 0.028685999116804389 -0.10033570781139382
		-0.10898478363248193 0.025431697288215576 -0.083034433266786417
		-0.10848821757044239 0.021516292238250932 -0.064529384335335532
		-0.10801283749577303 0.01701456261405879 -0.046315965148923888
		-0.10749004294764251 0.012004646628648676 -0.029766963467413289
		-0.10679302340184246 0.0068586355620463869 -0.01412713210281968
		-0.10577226269095505 0.0020383125382859813 0.00086593248939138628
		-0.1044274113941049 -0.0026472597616596367 0.015318018183196743
		-0.10271671134776975 -0.0071587928552805267 0.029310391143709633
		-0.10061469379864699 -0.011725181023183949 0.043179020042017256
		-0.098093375249616255 -0.016737926419941856 0.057174697628078364
		-0.095118318251113651 -0.021669916941163398 0.07163421783040444
		-0.091668127316699349 -0.026014189948587098 0.087293581062922121
		-0.08767569305435223 -0.030101799199610667 0.10320596062877178
		-0.08307652869435056 -0.034010992489128616 0.11878067011456316
		-0.077841192113514771 -0.037993225057201284 0.13368537841662265
		-0.071766594545193227 -0.042637232503078444 0.14760161413011225
		-0.065308920920805549 -0.047009421546853815 0.15989720116317235
		-0.059459573005157536 -0.050315264666512267 0.16959251828309757
		-0.052409766829908118 -0.052726300187115521 0.17741125069039257
		-0.042461483831345959 -0.054001321089004371 0.18384958471990775
		-0.030273784856937196 -0.054584035884355613 0.18861039573610708
		-0.01530523320085031 -0.054803343484155394 0.19162621553988909
		0.00054072498040902818 -0.054762465672322513 0.19270426115668429
		0.015502591995308276 -0.054776406754188399 0.1915034077520982
		0.029695920039218872 -0.054538718076456168 0.18840112329954101
		0.043028743191019896 -0.053957937844983817 0.18365961924926949
		0.054362129284517266 -0.052704109787608776 0.17728380855725068
		0.061697616594524066 -0.050287013409338513 0.16954516766870356
		0.067521906107999852 -0.047095979584578201 0.15990657519387094
		0.074016129705785666 -0.043275369715791975 0.14755532104639846
		0.080098555332822757 -0.039069871723746923 0.13358982657545398
		0.085350385179026766 -0.034844462084187615 0.11875328443733486
		0.089963903688830227 -0.030382636534160477 0.10329858121406846
		0.093970136321865336 -0.025431198473142777 0.087566587809599278
		0.097434062213747064 -0.020465201392400441 0.072036543925517713
		0.10042366360161441 -0.016006819770970467 0.057486522882089906
		0.10296077787055444 -0.011661494035747346 0.043360894653165963
		0.10508225352421999 -0.0072130268561466562 0.029472182993657073
		0.10681072651401673 -0.002648505984872678 0.015493910483094642
		0.10816735420663789 0.0021608315647717144 0.0010703369777565429
		0.10919333145303024 0.0070836309051549437 -0.013898225597679186
		0.10987871909818574 0.012128343548757241 -0.029553533764576336
		0.11039780830565171 0.017004313281910179 -0.046125122328569745
		0.1109113092529178 0.021474541037680216 -0.06434295597323493
		0.11144993633625898 0.025386506888329771 -0.082847546289584392
		0.1121820740125553 0.028630098621163086 -0.10014995122550682
		0.11285528816678507 0.030841094024166481 -0.11736863050435209
		0.11320577128035274 0.031620613764191327 -0.13558961001699507
		0.11343616213152427 0.030962516991937701 -0.15342142802274195
		0.11366709143284195 0.028324830006255859 -0.16941577663545165
		0.11380969673515434 0.026052391353810544 -0.17969158447624692
		0.11388099938631055 0.024916172027587884 -0.18482948839664456
		;
createNode transform -n "polyToCurve10" -p "tongue_Mo";
createNode nurbsCurve -n "polyToCurveShape10" -p "polyToCurve10";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 30;
	setAttr ".cc" -type "nurbsCurve" 
		3 56 0 no 3
		61 0 0 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
		 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52
		 53 54 55 56 56 56
		59
		0.11721099913120314 -0.0070514678955078394 -0.17451497912406988
		0.11695434958120854 -0.0069891474761951712 -0.17040712426375287
		0.11644105048121854 -0.0068645066375697924 -0.16219141454311786
		0.11576979629820507 -0.0064446185444470006 -0.14959072590418776
		0.11544101412108808 -0.0049758946665454922 -0.13666051181411673
		0.11511814916316242 -0.0039743544933466745 -0.12244912263111428
		0.11444639886785707 -0.0050343230243250214 -0.10550728786774835
		0.11372428408975498 -0.0071049747829899351 -0.087275200440504505
		0.11319810336289053 -0.0096982293330349443 -0.068385296234161549
		0.11266981049952482 -0.012720176553276178 -0.049811620559939172
		0.11206239337611068 -0.015925890972152631 -0.03297760160972437
		0.11125909303733343 -0.019280338204647203 -0.017167481922801948
		0.11012558206450972 -0.022694545522385656 -0.0022330959960728505
		0.10863759842777873 -0.026085402483749163 0.012104903851468949
		0.10672642317945052 -0.029299257970932129 0.026069665626996332
		0.10439118906116474 -0.032458761284220344 0.039977953855053143
		0.10161458767979153 -0.03555205007263227 0.05416735376350771
		0.098376955271191543 -0.038829008172033767 0.068798551249596496
		0.094671616087180221 -0.042718168950064583 0.084385230269629352
		0.090442074163514352 -0.046671721460234385 0.10020598188310943
		0.085636093790622994 -0.050211122267001224 0.1158367785346044
		0.080234039687692355 -0.053557102207783418 0.13089898114175577
		0.07406824823080653 -0.056976727691884402 0.14512899058448439
		0.067530479323913234 -0.059852448567575212 0.15775721239641882
		0.061699360474913825 -0.061247605159124231 0.16771848593332325
		0.054346580546587114 -0.062386592448121482 0.17563546357105767
		0.042894197666608243 -0.064645907309750214 0.18173770881999929
		0.02946964214125523 -0.066632584387414553 0.18613923822548073
		0.015372236011490955 -0.067093885281373389 0.189184837392884
		0.0005084236682269018 -0.066985625996287573 0.19041194146625454
		-0.015435294958329014 -0.067119010039286192 0.1893185696303035
		-0.030499730917492678 -0.066675136503208304 0.18636775536841457
		-0.042595393405420089 -0.064688396621303171 0.18194688056219879
		-0.05242669363931797 -0.062410117479438199 0.17578074038775315
		-0.059452572808809889 -0.06127838556495506 0.16778696084393052
		-0.065319994896282416 -0.059767313906668292 0.15777443134396768
		-0.07181892932361264 -0.056348785658439517 0.1452099716974399
		-0.077979300961986631 -0.052467576932489733 0.13103768493515239
		-0.083367973960058989 -0.049221203716197516 0.1159174896829815
		-0.088164278723230807 -0.046123329538181053 0.10016893777640934
		-0.092386269743068461 -0.043139337531206634 0.084145940243818232
		-0.096084638901232935 -0.040011584869640626 0.068405338143144076
		-0.099314161124035127 -0.03628462602394944 0.053857108925145898
		-0.10208068651806738 -0.03251725224131162 0.039795754370103985
		-0.10440094523151908 -0.029242344675179697 0.025906162345134109
		-0.10629707206022072 -0.026082188076993543 0.011927152049354952
		-0.1077724271382651 -0.022816530113998871 -0.0024393257488713
		-0.10890019870940813 -0.019505863192101305 -0.017397777890115013
		-0.10971776165209442 -0.016049076633357591 -0.033191124857067704
		-0.11033573738254741 -0.012710727356659896 -0.050002174955058508
		-0.11084275955880055 -0.0096673787082481692 -0.068574662299013045
		-0.1113422110372093 -0.0070819007280055494 -0.087468640535829006
		-0.11204208627448198 -0.005006193280599364 -0.10570135579764418
		-0.11271740764489907 -0.003949730238087798 -0.12264487533668759
		-0.11297174018281322 -0.0049743118404999226 -0.13686208511005754
		-0.11352762917882989 -0.0064748588484391531 -0.14979773043183411
		-0.11523546193306786 -0.0069282337167990999 -0.16239894734127408
		-0.11662215462745937 -0.0070763523094896728 -0.17061397865846117
		-0.11731550097465512 -0.0071504116058349592 -0.17472149431705472
		;
createNode transform -n "polyToCurve11" -p "tongue_Mo";
createNode nurbsCurve -n "polyToCurveShape11" -p "polyToCurve11";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 30;
	setAttr ".cc" -type "nurbsCurve" 
		3 24 2 no 3
		29 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
		 26
		27
		0.01371528526307325 -0.070546399221943737 0.1821002112359224
		0.026645912958860526 -0.069676859938650734 0.17902239450579333
		0.042577456547486466 -0.067667925635651105 0.17601695040498205
		0.052294032088566915 -0.065565148112922231 0.17092612577178509
		0.053827940066393111 -0.062981932609605176 0.1758608505087321
		0.054374087978807391 -0.057947003727099322 0.17762852121405356
		0.053852647386625346 -0.052372763763774026 0.17766873552776899
		0.052390199403020719 -0.047623331617737456 0.17403655780829325
		0.042807563302072991 -0.047931925657781774 0.17955932370536651
		0.027068189652099776 -0.047337412749731737 0.18322758932580735
		0.013954367098717505 -0.047801389432539955 0.18640631844208774
		0.00063398326300677214 -0.048246685205533227 0.18790193698709484
		-0.012996698112383468 -0.048089133410526362 0.18664600832037856
		-0.026340431530526322 -0.047811319059007991 0.18362790512048985
		-0.041432356160780656 -0.04820832092328111 0.17985752174468958
		-0.05047899698530188 -0.04775849106271747 0.17420494592336538
		-0.052074157760060961 -0.052387416678647457 0.17779472377098576
		-0.052784496133313492 -0.057913628721716091 0.17770326474372913
		-0.052098805303711943 -0.062998006407510646 0.17600612578337943
		-0.050575023426470245 -0.065701597769212972 0.17112903506312205
		-0.04166210270845138 -0.067942991832196237 0.17635357796590254
		-0.026762054750535065 -0.070145493987848015 0.17946308465285762
		-0.013235378934855132 -0.07083076739917385 0.1823629551591936
		0.00057370509691301937 -0.070817921133779299 0.1836434190473735
		0.01371528526307325 -0.070546399221943737 0.1821002112359224
		0.026645912958860526 -0.069676859938650734 0.17902239450579333
		0.042577456547486466 -0.067667925635651105 0.17601695040498205
		;
createNode transform -n "polyToCurve12" -p "tongue_Mo";
createNode nurbsCurve -n "polyToCurveShape12" -p "polyToCurve12";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 30;
	setAttr ".cc" -type "nurbsCurve" 
		3 56 0 no 3
		61 0 0 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
		 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52
		 53 54 55 56 56 56
		59
		-0.1079929992556576 0.042405605316162269 -0.18972098827362133
		-0.10444091876298209 0.042960270657655279 -0.18401136766039
		-0.097336757777630484 0.044069601340640981 -0.17259212643392632
		-0.09820719866123849 0.048880107238831634 -0.15532293679302461
		-0.097087571070371317 0.048810738950630483 -0.13527481403945402
		-0.097039968478515509 0.047049858631243065 -0.11525886909275192
		-0.09640996465849197 0.044048853259497305 -0.097942453972293286
		-0.095830367881409084 0.039992264302908871 -0.081118240060429239
		-0.095434893536452736 0.035129633455965606 -0.062917298389595935
		-0.095066304636423696 0.029717347015775109 -0.04499164791926482
		-0.094643471727826639 0.024019950778499399 -0.028612525147484111
		-0.094071966410394905 0.018262507940723583 -0.013053348489895681
		-0.093225284324212648 0.012804832227367535 0.001978277903961522
		-0.092118881523044344 0.0075072178495668258 0.016513719441159598
		-0.09074327507262793 0.0024145366265990093 0.030558812672211881
		-0.089046866984135664 -0.0026671305409679382 0.044482517665391595
		-0.086990498771475702 -0.0080139697458425519 0.058562753765653612
		-0.084527279586873394 -0.013334308190253916 0.073078412639290408
		-0.081609630733574481 -0.018414832555409575 0.088692010893787684
		-0.078200725487077932 -0.023296650499472275 0.10453063776275315
		-0.074246451026390298 -0.027858011516868803 0.12005881203323748
		-0.06975135520753091 -0.032374176764050473 0.13492702979718765
		-0.064469503959093538 -0.037265875819052545 0.14897559198892416
		-0.059098364350434314 -0.041974952913960972 0.16109951347238421
		-0.054105273531381871 -0.045546692351669693 0.17072868195982627
		-0.049934776597796347 -0.049591503496947381 0.17609833280230633
		-0.041578121937463637 -0.047716995527963331 0.17935001605231871
		-0.026301588810208307 -0.04794360822074293 0.18376454102165735
		-0.013006303216663127 -0.048051302173471672 0.18660697041729785
		0.00063356095942235994 -0.048265721006422853 0.18792145270668895
		0.013965661416295275 -0.04776307748036264 0.18636729347499659
		0.027023434683681322 -0.047471624771962199 0.1833641734830137
		0.042975288855784367 -0.047433389535609501 0.17905201205284615
		0.051764052153421093 -0.049483264098887328 0.17592922027178773
		0.056189510827205115 -0.045431569975939189 0.17060539733854294
		0.061183397505848301 -0.041929992392251966 0.16106161852818801
		0.066605024786597411 -0.037540813120878737 0.14893896251340136
		0.07191399479967088 -0.032895811723449943 0.13489257438784732
		0.076444006896306468 -0.028179458648171101 0.12008824504534217
		0.080432082012457981 -0.023295963007513222 0.10463520516161763
		0.083875073872888811 -0.018160106077147485 0.0888545108370489
		0.086827138755993766 -0.012924641818281188 0.07327620848157583
		0.089325539632953407 -0.007713314737803352 0.058744404825743855
		0.091417989006338851 -0.0025279344583269219 0.044637393786800011
		0.093152775538666466 0.0025280122479737818 0.030713641122793536
		0.094565701935863597 0.0076358123204967902 0.016676603940133386
		0.095705237011632527 0.01296416236481843 0.002153544077444228
		0.096581626403290891 0.018447346608891066 -0.012868498078697051
		0.097173412746410615 0.024183420738252238 -0.028433326662178314
		0.097623995045954287 0.029849766985796968 -0.04482115744897408
		0.098053977370734874 0.035248611802191777 -0.062749071639489964
		0.098510331868796971 0.04010347821960502 -0.080950310621966337
		0.099130438426173736 0.044152218738886785 -0.09777540780502296
		0.099763677895270866 0.047154071403980376 -0.11508969126147157
		0.099885456556143906 0.048944355531177479 -0.13509548760657852
		0.10075525682694872 0.04903267980342485 -0.15513251343631332
		0.098980503792482466 0.044338004887596726 -0.1724000917987859
		0.10498883410126561 0.043091064393684583 -0.18381469604428724
		0.10799299925565717 0.042467594146728509 -0.18952199816703791
		;
createNode transform -n "polyToCurve13" -p "tongue_Mo";
createNode nurbsCurve -n "polyToCurveShape13" -p "polyToCurve13";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 30;
	setAttr ".cc" -type "nurbsCurve" 
		3 56 0 no 3
		61 0 0 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
		 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52
		 53 54 55 56 56 56
		59
		0.11465299874544187 -0.02146768569946297 -0.16889297962188785
		0.11136606465053638 -0.020540997097757124 -0.1657499513878733
		0.10479219646072457 -0.018687619894345302 -0.15946389491984317
		0.1060815819522795 -0.02002680645694193 -0.14789781949168035
		0.10508040954008566 -0.018254520489540738 -0.1370619617363712
		0.10499781206864771 -0.01698522620992815 -0.12442879603518034
		0.10437578743281931 -0.017779021298313762 -0.10762938635526206
		0.10377530773137542 -0.019568280473258152 -0.089054993517680647
		0.10333339009306984 -0.021855619308887353 -0.070052658907498316
		0.10286398673093751 -0.024490412917571168 -0.051386104800318771
		0.10224708009729287 -0.027128801570548516 -0.034517693093017811
		0.10142155189707243 -0.029853105365165795 -0.018698501602219378
		0.10029752665079524 -0.03265742944528599 -0.0037631806674295184
		0.098841124254157225 -0.035462558942529351 0.01057663655899989
		0.096988777285952732 -0.038132188113753997 0.02456488858070844
		0.094739538106870094 -0.040831694727163102 0.038500210090062284
		0.092074576377397202 -0.043681123534879608 0.052696165093826637
		0.088983928075060989 -0.046680167841203615 0.067351937681443846
		0.085454128208088731 -0.049941081984421654 0.083020420595513414
		0.081476938745171215 -0.053246227613098336 0.098954118946360359
		0.077029486390707863 -0.056403865358977935 0.1147207594200451
		0.072142256694189832 -0.059448552619126883 0.12992754761324496
		0.066635893292688611 -0.062692677045881939 0.14441030724009041
		0.061117048624689779 -0.065111008505500681 0.15705086594229628
		0.056110532314168987 -0.066184541608722738 0.16705166575602909
		0.051682427036619946 -0.064706989774961227 0.17328659780246072
		0.042741284502650988 -0.067897949962695756 0.17538424705309955
		0.026602206186463827 -0.069614920942946149 0.17919273589879306
		0.013726284394821403 -0.070564130852272047 0.18205154903025242
		0.00057341534055723494 -0.070808933582752337 0.18366772649048912
		-0.013245219042072841 -0.070848985947545615 0.18231438760550353
		-0.026722404565329955 -0.070081607319961187 0.17963304743794106
		-0.04181086334115499 -0.06818031992991283 0.17572229439371181
		-0.050019631078948225 -0.064816172020731685 0.1734842065829563
		-0.054171614058022989 -0.066302381278041597 0.16721672329435927
		-0.059211655830938549 -0.065157210422311179 0.15714047263951259
		-0.064688186133283573 -0.062433928530214323 0.14451115176460763
		-0.070177082696766896 -0.058911167835388828 0.13003707636971354
		-0.07504072963126418 -0.055854347018153089 0.11477760789890529
		-0.079468015187942317 -0.052856375815647179 0.098935306263719144
		-0.083428352866550606 -0.049970133237703891 0.082909898000662993
		-0.086942551028373907 -0.047081130146677391 0.067169468207833372
		-0.090016837184233645 -0.04401660684877632 0.052518890779433176
		-0.092664233319943959 -0.041004254030650819 0.038347548148335985
		-0.094892585142378902 -0.038291735749658093 0.024411020021752671
		-0.096723693696078375 -0.035646372198276238 0.010415543775224759
		-0.098159336841674466 -0.032879947655187862 -0.0039342577835918893
		-0.099267474542905229 -0.030106733918336664 -0.018877972418303784
		-0.10009215203823411 -0.027361262060232112 -0.034695648403438556
		-0.10070702547465193 -0.024694538535913635 -0.051561281398730514
		-0.10115470103731553 -0.022062556013415897 -0.07023150281119378
		-0.10157232914710949 -0.019784886926161472 -0.089238442497661233
		-0.10214819658003095 -0.017996740091435672 -0.10781461938500803
		-0.10277158986063797 -0.017207199025572877 -0.12461552002069577
		-0.10279142823957489 -0.018504498869986612 -0.13725175609205251
		-0.1040169662052961 -0.02028639356553243 -0.14809051581030272
		-0.10370435215382293 -0.019073840871222519 -0.15965836389849072
		-0.11114278567283851 -0.020748256608766877 -0.16594479197922507
		-0.11486200243234632 -0.021585464477539059 -0.16908800601959226
		;
createNode transform -n "polyToCurve14" -p "tongue_Mo";
createNode nurbsCurve -n "polyToCurveShape14" -p "polyToCurve14";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 30;
	setAttr ".cc" -type "nurbsCurve" 
		3 24 2 no 3
		29 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
		 26
		27
		-0.012539333688653962 -0.042653694218603135 0.17787024204202834
		0.00067347628374067874 -0.04289201806270064 0.17905535700439201
		0.013806562324335896 -0.042275557043625289 0.17763706610258909
		0.027399784599865879 -0.042008801705913389 0.17507689530506967
		0.044041557063189803 -0.042816274611572391 0.17208457087400128
		0.057873504287763326 -0.045078617929462057 0.16953730866764494
		0.062169918759084557 -0.050008790051347285 0.16917862259605931
		0.062121322452593657 -0.055834364870519973 0.16911925535905215
		0.062179533499785125 -0.061331923531758349 0.1672932862312512
		0.057835045324961074 -0.066067402672368519 0.16597421939825507
		0.043721890124572525 -0.068954630520283666 0.16735396292476706
		0.0268614038241182 -0.070726513448401168 0.16961156326203641
		0.013496502302286101 -0.071716981968765414 0.17199224732969928
		0.00059659524260389498 -0.072036791891869262 0.17348947119426703
		-0.012849126062923858 -0.07209059194172393 0.17226324012376223
		-0.026657084973104313 -0.071330633889819084 0.17005904402632127
		-0.042685281278764954 -0.069329724233161194 0.16768137538739245
		-0.055819777628033813 -0.066130847519210903 0.16611296352216179
		-0.059953351355519338 -0.06132979327132447 0.16735834290402646
		-0.059923796725317627 -0.055840953058821259 0.1691566799507675
		-0.059962958072517711 -0.050004237091351905 0.16922180665668837
		-0.055781350760040316 -0.045138878971278891 0.16963461839348731
		-0.042365873964225385 -0.043193472826907775 0.17235229386985676
		-0.026119131172937009 -0.042619847290059652 0.17545972566215018
		-0.012539333688653962 -0.042653694218603135 0.17787024204202834
		0.00067347628374067874 -0.04289201806270064 0.17905535700439201
		0.013806562324335896 -0.042275557043625289 0.17763706610258909
		;
createNode transform -n "polyToCurve15" -p "tongue_Mo";
createNode nurbsCurve -n "polyToCurveShape15" -p "polyToCurve15";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 30;
	setAttr ".cc" -type "nurbsCurve" 
		3 24 2 no 3
		29 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
		 26
		27
		0.06849281650714692 -0.059755342979708886 0.15724018866138262
		0.062919307598037905 -0.065297975408924347 0.15639856032041285
		0.047044573214074237 -0.068374008088260399 0.15683100680165596
		0.028448414510245695 -0.070097312466610759 0.15787743717312813
		0.014170341382977824 -0.071012689973725202 0.15951945563978831
		0.00059747574926870544 -0.071258681655364559 0.16067094690414746
		-0.013517768593992558 -0.071393077703751584 0.15973177027626057
		-0.028231768565924475 -0.0707029321092493 0.15822587435935581
		-0.04598605986180717 -0.068711203881414523 0.15707557823358173
		-0.060872713240718773 -0.065267968154887515 0.15648589799913359
		-0.066229510696359628 -0.059582075023579165 0.15727059536627366
		-0.06676072569762817 -0.053100158619234492 0.15852637843372105
		-0.066226034288968491 -0.046648254063401874 0.15942541243853028
		-0.060796988385702307 -0.041297008480582049 0.16055490886202348
		-0.045554247064882106 -0.038876091827464147 0.16245727993701481
		-0.027530142534018094 -0.037934470729031562 0.1644390886460817
		-0.013111175808851169 -0.037779967374100616 0.16619716212096164
		0.00068447810651612131 -0.037965685027861872 0.16710347777485682
		0.014465177543895123 -0.037396808486589425 0.16603349140821219
		0.028964820082819243 -0.03732491534584878 0.16417377380497153
		0.047336204805692249 -0.038539484057055588 0.16228889183793579
		0.062931017666343278 -0.041331996848933059 0.16051986600614226
		0.068467850172664879 -0.046824881199761949 0.15942247808753782
		0.068998952382934034 -0.053314779812285246 0.15851701111819363
		0.06849281650714692 -0.059755342979708886 0.15724018866138262
		0.062919307598037905 -0.065297975408924347 0.15639856032041285
		0.047044573214074237 -0.068374008088260399 0.15683100680165596
		;
createNode transform -n "polyToCurve16" -p "tongue_Mo";
createNode nurbsCurve -n "polyToCurveShape16" -p "polyToCurve16";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 30;
	setAttr ".cc" -type "nurbsCurve" 
		3 24 2 no 3
		29 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
		 26
		27
		0.01502908429435873 -0.068875052759394803 0.14521323185016788
		0.030382701736129683 -0.067985713631624548 0.14423582027597071
		0.050850869432022897 -0.066236815023219528 0.14387727954167687
		0.068499849397778312 -0.063009714263778632 0.14398519413712554
		0.074952611475895006 -0.057054597258366438 0.14480158640593008
		0.075727216643412518 -0.05008835826586594 0.14598061609624025
		0.07488467482826254 -0.04303889722562463 0.14727647277630862
		0.068419064316784156 -0.03702338300131338 0.14863117873640663
		0.050956559364447387 -0.033856627356341151 0.14990885523155573
		0.030661703177857089 -0.032373601530841671 0.1510974843427263
		0.015179506144205586 -0.032273198812467506 0.15233237910087763
		0.00069478009274888039 -0.032778464822071501 0.15303557850409857
		-0.013743617470345275 -0.03266650644773892 0.15242522639261527
		-0.02908280201274888 -0.032974033175424924 0.15124814245704121
		-0.049079916987785861 -0.034083906260717584 0.15000051442146201
		-0.06625602093233264 -0.036734777282803339 0.14865238202568951
		-0.072623734683083543 -0.042389617550268766 0.14731886868488608
		-0.073465531557714736 -0.049258329130501446 0.14606117931798751
		-0.072669538885404519 -0.056410415155630722 0.14487968091175538
		-0.066431326061372739 -0.062730043740017671 0.14407210008484156
		-0.049746639937570607 -0.066473502291525141 0.14405407479669943
		-0.030103097824724059 -0.068593936061777244 0.1444721486047186
		-0.014341342663469848 -0.069272671185975299 0.14535551660977397
		0.00060197234777934817 -0.069081452421250258 0.14597186214086252
		0.01502908429435873 -0.068875052759394803 0.14521323185016788
		0.030382701736129683 -0.067985713631624548 0.14423582027597071
		0.050850869432022897 -0.066236815023219528 0.14387727954167687
		;
createNode transform -n "polyToCurve17" -p "tongue_Mo";
createNode nurbsCurve -n "polyToCurveShape17" -p "polyToCurve17";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 30;
	setAttr ".cc" -type "nurbsCurve" 
		3 24 2 no 3
		29 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
		 26
		27
		0.016052789215289052 -0.065967934509919321 0.12977248289660526
		0.032580584466608449 -0.065091923504335902 0.12931812219121638
		0.054825685973315559 -0.063303868276020733 0.12931273870000995
		0.074066668349952888 -0.05995792464631132 0.12970468022805845
		0.081142047098125239 -0.053755186050301648 0.13070979748309311
		0.082005644041466347 -0.046437589964432771 0.13201782350793431
		0.080989449378335812 -0.038894249385775313 0.13345547502874883
		0.073797294672225858 -0.032384731187534391 0.13482818814502986
		0.054526382823721499 -0.028870344517003113 0.13582927748375245
		0.032328545316419453 -0.027134975548988093 0.13662209240953882
		0.015881994170564739 -0.026869467513767224 0.13737401089811191
		0.00070485773202303597 -0.027314258392219841 0.13776599352224447
		-0.014365666705957821 -0.027280779958498695 0.13741005797784536
		-0.03060856139242462 -0.027746894063061481 0.1366807684990981
		-0.052559618530885102 -0.029036576860391843 0.13585893345544983
		-0.071611203979789234 -0.031922917212564732 0.13483801695095332
		-0.078716941372978841 -0.037892348671635281 0.13353152193409615
		-0.079728922230947269 -0.045128813322146577 0.13215969320618629
		-0.078848390153824166 -0.052717595450361948 0.13083105898185093
		-0.071981624295250971 -0.05944110200317574 0.12979427196962035
		-0.053662359226222416 -0.063450943457330058 0.12942891826417938
		-0.032209293480874424 -0.065724793509545118 0.12945081532865774
		-0.015312867608546362 -0.066395779678371042 0.12984981662365849
		0.00060852162408621445 -0.066149150975060286 0.13018357906538011
		0.016052789215289052 -0.065967934509919321 0.12977248289660526
		0.032580584466608449 -0.065091923504335902 0.12931812219121638
		0.054825685973315559 -0.063303868276020733 0.12931273870000995
		;
createNode transform -n "polyToCurve18" -p "tongue_Mo";
createNode nurbsCurve -n "polyToCurveShape18" -p "polyToCurve18";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 30;
	setAttr ".cc" -type "nurbsCurve" 
		3 24 2 no 3
		29 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
		 26
		27
		-0.014906326756152718 -0.021590256425360548 0.12200724657636766
		0.00071518705630572586 -0.021556966685197167 0.12220918943467726
		0.016505086294315588 -0.02115035408299629 0.12199866457587638
		0.033803474059251909 -0.021589152688384062 0.12152163639458406
		0.057669407652125498 -0.023683275546615624 0.12093499796613331
		0.078525372092156653 -0.027647996208527433 0.12006786025673621
		0.086351208385604769 -0.034634348937054166 0.11867432072295568
		0.08753379411365439 -0.042644964641156261 0.11713640237603823
		0.086644240646151616 -0.05038260903808519 0.11569701976030283
		0.079109732326855239 -0.056897911965902437 0.1145275957330953
		0.058653971059572999 -0.060335984797523792 0.11395730153476337
		0.034958381423553654 -0.062116148645638136 0.11375580656062097
		0.017221518973255533 -0.062955199409443885 0.11389607403797636
		0.00061555857640673386 -0.063105824102328498 0.11409748311816201
		-0.016425369446010561 -0.063428810470914962 0.11393004578315291
		-0.034488575899300003 -0.062816652214695234 0.1138149161752974
		-0.057428583761732516 -0.060477851372666147 0.11401201976696976
		-0.077009592665811394 -0.056325170672936027 0.11457514395703403
		-0.084341061994432656 -0.049406397690655614 0.11577021862150791
		-0.085241634891850701 -0.041524959923694378 0.11722056298736951
		-0.084066510328957469 -0.033820468547184075 0.11869269408565321
		-0.076315323746543054 -0.027332160104488308 0.12002268015930606
		-0.055610079492456999 -0.023953764360210617 0.12090950095514698
		-0.031938869816412412 -0.022261412825762977 0.12153084958562721
		-0.014906326756152718 -0.021590256425360548 0.12200724657636766
		0.00071518705630572586 -0.021556966685197167 0.12220918943467726
		0.016505086294315588 -0.02115035408299629 0.12199866457587638
		;
createNode transform -n "polyToCurve19" -p "tongue_Mo";
createNode nurbsCurve -n "polyToCurveShape19" -p "polyToCurve19";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 30;
	setAttr ".cc" -type "nurbsCurve" 
		3 24 2 no 3
		29 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
		 26
		27
		0.091511920186526596 -0.046820805182583941 0.1001323445332893
		0.083648913441681072 -0.053791711762196506 0.098818367174760557
		0.062283795627971567 -0.057342205594862868 0.098151842578978327
		0.037411397148506345 -0.059103104831588045 0.097855359563807739
		0.018468749175105353 -0.059910414022075684 0.097839836455333895
		0.00062260821673078238 -0.060036815236725424 0.097935957752292496
		-0.017616142384107896 -0.060437251602868731 0.097847688846340597
		-0.036842902247651493 -0.059900944499413231 0.097865971274347707
		-0.060997365881927515 -0.057558675857165793 0.098152013578775302
		-0.081535748517260156 -0.053340707147759903 0.098798890727537322
		-0.089200783299497294 -0.046328479100912645 0.10008115447573616
		-0.090072476879645036 -0.038199235873180568 0.10161567241123556
		-0.088739117393249051 -0.02988256657453214 0.10317894898158589
		-0.080418481773829653 -0.022702877074448936 0.10456662536282964
		-0.058245939218860288 -0.018765371200250514 0.10542792355238606
		-0.033057269292928917 -0.016657244188391783 0.10597842671974035
		-0.015352160180316351 -0.015841742110231111 0.10632688572771021
		0.00072566654948598777 -0.01579591628837786 0.10644275127281547
		0.01703453192162287 -0.01536966400433913 0.10632967964325497
		0.035068586440292072 -0.015907693452780015 0.10599384963029236
		0.060399344885243997 -0.018354853431908673 0.10549316750398692
		0.082653035454965496 -0.022760619412602885 0.10467637533705153
		0.091035922114092727 -0.030126085675263405 0.10328490768398546
		0.092379412343927825 -0.038541244589529483 0.10169819103813622
		0.091511920186526596 -0.046820805182583941 0.1001323445332893
		0.083648913441681072 -0.053791711762196506 0.098818367174760557
		0.062283795627971567 -0.057342205594862868 0.098151842578978327
		;
createNode transform -n "polyToCurve20" -p "tongue_Mo";
createNode nurbsCurve -n "polyToCurveShape20" -p "polyToCurve20";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 30;
	setAttr ".cc" -type "nurbsCurve" 
		3 24 2 no 3
		29 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
		 26
		27
		0.019727964135293118 -0.056907144911921934 0.081859624482244847
		0.039834952309946797 -0.056097507838242314 0.081923221214494565
		0.065663235631419944 -0.05433157167517226 0.082237219062868364
		0.087704092321241461 -0.050601359574838078 0.082941447045827218
		0.09579777471561042 -0.042953713444664879 0.084384731816132055
		0.09661030257642568 -0.03395719210304541 0.086065079953331514
		0.095109545271197984 -0.025236349396205251 0.087639145939435295
		0.086230027505355036 -0.01767004214807109 0.088979812719820292
		0.062729860946548144 -0.012944511159612215 0.08977106022588506
		0.036106019965166346 -0.010262158345926368 0.090236430795508568
		0.017456074942717822 -0.0097812027619801779 0.090490276809938014
		0.00073619305130443965 -0.010320433789136324 0.090544416291369167
		-0.015689714651340204 -0.010282043275016996 0.090479025912463817
		-0.033947331792344854 -0.011074042875810333 0.090203471510039018
		-0.060481832677170881 -0.013401299820588112 0.089690004998559641
		-0.083970834213086751 -0.017775439238321578 0.088830055410776668
		-0.09280135845700864 -0.025787232151296476 0.087366867388713826
		-0.09429025250674547 -0.03490410810864096 0.085716977798116212
		-0.093480785612612971 -0.043335496905533774 0.084147822203123043
		-0.085580601615297167 -0.050446168826108688 0.082849770336641856
		-0.064320785587331258 -0.05469786673046112 0.082197462976913271
		-0.039174238380005229 -0.057009102685884695 0.081905522552076573
		-0.018822485277909369 -0.057486591113493989 0.081854303788428562
		0.00062919489109873258 -0.05702746781192148 0.081921339976704213
		0.019727964135293118 -0.056907144911921934 0.081859624482244847
		0.039834952309946797 -0.056097507838242314 0.081923221214494565
		0.065663235631419944 -0.05433157167517226 0.082237219062868364
		;
createNode transform -n "polyToCurve21" -p "tongue_Mo";
createNode nurbsCurve -n "polyToCurveShape21" -p "polyToCurve21";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 30;
	setAttr ".cc" -type "nurbsCurve" 
		3 24 2 no 3
		29 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
		 26
		27
		0.099552280277526245 -0.039165533928561494 0.068919314530825185
		0.091292883583919696 -0.047446617136868416 0.06738276020915307
		0.068740602248328952 -0.051390874435128145 0.066673981113656869
		0.04212681026986366 -0.053209999353728658 0.06637860813140066
		0.020934130964017809 -0.05405051047226863 0.066319896678733642
		0.00063542094165201682 -0.054178058568750735 0.066381891184624869
		-0.019978650034170872 -0.054685902394185082 0.066306976124728564
		-0.04137893163217609 -0.05423773660914763 0.066343297368371287
		-0.067345419682222865 -0.051919499850674289 0.066604537894904559
		-0.089160017113717446 -0.047557718940395281 0.067236560256875105
		-0.097229906002197303 -0.040160885087970534 0.068555882754955624
		-0.097959345321966595 -0.031269043766346892 0.070164310531087404
		-0.096314682519468398 -0.021383443510658632 0.071867583624417752
		-0.087016700143372663 -0.012628966344003217 0.073370505050968676
		-0.062327764734570676 -0.0078667261932845508 0.074218811455864273
		-0.034589605873292982 -0.0053892758822177058 0.074695576101396696
		-0.01590406727114347 -0.0047872545244800595 0.074906913098776839
		0.00074675986988082899 -0.0050275171770886203 0.074929436546373157
		0.017754723533646113 -0.0042584228694985318 0.074926625028932478
		0.036896232300151634 -0.0045260987980727651 0.074743865088079994
		0.064671013218906698 -0.0073972744350823483 0.074307602686183666
		0.089300972835085882 -0.012458501982258237 0.073538138145761989
		0.098634263946418443 -0.020340705741658631 0.072243594387445598
		0.1002920201310713 -0.029477498884572809 0.070686770765332071
		0.099552280277526245 -0.039165533928561494 0.068919314530825185
		0.091292883583919696 -0.047446617136868416 0.06738276020915307
		0.068740602248328952 -0.051390874435128145 0.066673981113656869
		;
createNode transform -n "polyToCurve22" -p "tongue_Mo";
createNode nurbsCurve -n "polyToCurveShape22" -p "polyToCurve22";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 30;
	setAttr ".cc" -type "nurbsCurve" 
		3 24 2 no 3
		29 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
		 26
		27
		0.10282582615417959 -0.035840466738507389 0.054201181117258482
		0.0944329341850179 -0.044447246181328871 0.052628249277258274
		0.071464208775136609 -0.048606905271406584 0.051922629990280224
		0.044184738284702429 -0.050551221066174747 0.051640735842797603
		0.022022221427366099 -0.051445629096401775 0.051585120131418791
		0.00064138854426623419 -0.051588864248047213 0.051645839753353392
		-0.02101888975650491 -0.052144258836336166 0.051562803148964255
		-0.043353313210415807 -0.051683456104240071 0.051589008985399518
		-0.070017841237052209 -0.04924765107592724 0.051829385823511542
		-0.092289824175970175 -0.044591520723032463 0.052468052422550211
		-0.10049699512142979 -0.036538077631674368 0.053890984029878186
		-0.10114416522890506 -0.02692350998256985 0.055597539742009934
		-0.099340464279455185 -0.016520178885800096 0.05729222817403333
		-0.08960049067665056 -0.0073425781393909048 0.058745576017590923
		-0.063793714647929906 -0.0021668262904009227 0.059537413193987948
		-0.034964650502747968 0.00051958979818697874 0.059944338629324107
		-0.015980301470331634 0.00076652953661785178 0.060053787536499273
		0.00075736250880933476 0.00018583555814923001 0.060013080976418269
		0.017915483417241976 0.0013252231595266833 0.06008485379306093
		0.037419711080637977 0.001426933760531147 0.060010599850102007
		0.066232808717172548 -0.0016581689636751956 0.059641845267205305
		0.091910578131901996 -0.0072082364824905204 0.058911128120383432
		0.10167216502726846 -0.015814720353402527 0.057604863893755187
		0.10349025622580575 -0.025686856636980414 0.056012946482665867
		0.10282582615417959 -0.035840466738507389 0.054201181117258482
		0.0944329341850179 -0.044447246181328871 0.052628249277258274
		0.071464208775136609 -0.048606905271406584 0.051922629990280224
		;
createNode transform -n "polyToCurve23" -p "tongue_Mo";
createNode nurbsCurve -n "polyToCurveShape23" -p "polyToCurve23";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 30;
	setAttr ".cc" -type "nurbsCurve" 
		3 24 2 no 3
		29 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
		 26
		27
		0.02298792791019031 -0.049066777062867661 0.037362865939012786
		0.046003231328749679 -0.048094399755960249 0.03741973877060701
		0.073836935952705601 -0.045993211889747081 0.037694012683030791
		0.097137269870803941 -0.041603545264702349 0.038396088136563498
		0.10563549063516925 -0.032732697636198453 0.039983528877580138
		0.10622653467168701 -0.022152017397138367 0.041818631237282668
		0.10425481127943177 -0.011432825843370964 0.043451822591402983
		0.09410324879792735 -0.0019825020214309878 0.044776362959693151
		0.067482464706150727 0.004065793585810315 0.045450346738914703
		0.037753890291784178 0.0073180839915137005 0.045729742877254419
		0.017984028121845165 0.0067216008587107443 0.045682772694927265
		0.0007681253751130097 0.0051195577549177336 0.045530795824352113
		-0.015963837526510875 0.0061369416363659338 0.045639106346970111
		-0.035149652740278099 0.0063756639999420104 0.045644122235929528
		-0.064946665420190772 0.0035149983349734974 0.045327948822947745
		-0.091766297621385828 -0.0020521543796309261 0.044618773410275404
		-0.10190938585451972 -0.011574336119641938 0.04324859470864964
		-0.10386502073116508 -0.02244794453169386 0.041588016769103078
		-0.10329772058048502 -0.032865214717815991 0.03977971067959489
		-0.094981949353396711 -0.04168717628759392 0.038239429336598775
		-0.072340837591980039 -0.046711438880244295 0.037582675440520762
		-0.045092680334492083 -0.049320497508903244 0.037352848315781208
		-0.021939558692903934 -0.049827861219526315 0.037330850579744453
		0.00064693382578098367 -0.049238097552871826 0.037419675053984545
		0.02298792791019031 -0.049066777062867661 0.037362865939012786
		0.046003231328749679 -0.048094399755960249 0.03741973877060701
		0.073836935952705601 -0.045993211889747081 0.037694012683030791
		;
createNode transform -n "polyToCurve24" -p "tongue_Mo";
createNode nurbsCurve -n "polyToCurveShape24" -p "polyToCurve24";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 30;
	setAttr ".cc" -type "nurbsCurve" 
		3 24 2 no 3
		29 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
		 26
		27
		0.023826961332672578 -0.046888230650212588 0.023360704713831192
		0.047576778966148162 -0.04581276220346478 0.023425741195460946
		0.075861689978886093 -0.043563341995889147 0.023698950178530805
		0.099418954080191163 -0.038915812943471732 0.024404475422492879
		0.10799826518949265 -0.029596412383330589 0.026019549176820058
		0.10852246535211531 -0.01843973320191683 0.027878848160601582
		0.10641364211027539 -0.0069694548234979555 0.029513326200926632
		0.095923484671825418 0.003155445028257286 0.030811384223268196
		0.068487212283706342 0.0095676015445752532 0.031409699199053259
		0.037976188260419132 0.012868496556503229 0.031594396817509161
		0.018006035272570969 0.011682575761668925 0.031438178590190477
		0.00077917214704249088 0.0095735827515574072 0.031217994021542766
		-0.015900094105005542 0.011081614502853386 0.031382338523940539
		-0.035221794189935741 0.011902056557585682 0.03148927588515172
		-0.065853601136899462 0.0089953461297494312 0.031272557089543428
		-0.093558280966369547 0.0031064251801304625 0.030653615959692734
		-0.10405212377920794 -0.0069228130551052735 0.029344466941902011
		-0.10614217448404407 -0.018422785188102905 0.027707119149362427
		-0.10564776015183384 -0.029540436527566084 0.025848641925125832
		-0.097248324396459238 -0.038984287747653237 0.024245869025912421
		-0.074317209831871178 -0.044339981737649796 0.023575054055079144
		-0.046592314749719296 -0.047123097160878445 0.023345006815767459
		-0.022737014540986211 -0.04770291032333477 0.02332015862630905
		0.00065189123708562537 -0.047103971186285419 0.023409898544490122
		0.023826961332672578 -0.046888230650212588 0.023360704713831192
		0.047576778966148162 -0.04581276220346478 0.023425741195460946
		0.075861689978886093 -0.043563341995889147 0.023698950178530805
		;
createNode transform -n "polyToCurve25" -p "tongue_Mo";
createNode nurbsCurve -n "polyToCurveShape25" -p "polyToCurve25";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 30;
	setAttr ".cc" -type "nurbsCurve" 
		3 24 2 no 3
		29 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
		 26
		27
		-0.10756508139855321 -0.026362394070518508 0.011821912131729086
		-0.10799502857799327 -0.01458719860062465 0.013688817543109084
		-0.10579661785377426 -0.002352824412076578 0.015301103550889417
		-0.095017119611020537 0.0082889768626394494 0.016555164697653901
		-0.066578989180926473 0.014445157193986433 0.017070206075662609
		-0.035257141613233463 0.017312047193446051 0.017179171023861749
		-0.015834223979634531 0.015880847390650682 0.016995336927832221
		0.00079066091672412434 0.013873900001611135 0.016796862036446328
		0.018028836006263097 0.01648927776254985 0.017062994470497531
		0.038166371428653471 0.018290989642464395 0.017303719648061353
		0.069312154919824301 0.015023591455945567 0.017220190918790099
		0.097409028681745058 0.0083435154024362173 0.016718174960488739
		0.10817255063708513 -0.0023622291908353922 0.015480710276518822
		0.11039328254573999 -0.014540817892634684 0.013877145915733868
		0.10992891894668623 -0.026380887640611042 0.012004064434187665
		0.10129344061141617 -0.036271045000884287 0.010362781461899159
		0.077548119551023795 -0.041174785714120594 0.0096530639422776465
		0.048908731882196896 -0.043556079194330105 0.0093761181394641027
		0.024540410137405183 -0.044797568398413472 0.0092908206796268808
		0.00065639060800975904 -0.045106728438364836 0.0093239162442222048
		-0.023411183094092639 -0.045653236773603258 0.0092437396919568936
		-0.047853771875523872 -0.044933129318754074 0.0092844082931183812
		-0.075956389649707273 -0.041991369188036629 0.0095211100773163054
		-0.099106306427502469 -0.036350852242087686 0.010198978801161772
		-0.10756508139855321 -0.026362394070518508 0.011821912131729086
		-0.10799502857799327 -0.01458719860062465 0.013688817543109084
		-0.10579661785377426 -0.002352824412076578 0.015301103550889417
		;
createNode transform -n "polyToCurve26" -p "tongue_Mo";
createNode nurbsCurve -n "polyToCurveShape26" -p "polyToCurve26";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 30;
	setAttr ".cc" -type "nurbsCurve" 
		3 24 2 no 3
		29 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
		 26
		27
		-0.10906770181589628 -0.023129738356267124 -0.0025763423627837376
		-0.10944291399624667 -0.01068035141808673 -0.00073292226609428127
		-0.10717077415426379 0.0023484150895576603 0.00083976957132017864
		-0.096183474941393343 0.013651316990642214 0.002028460098290981
		-0.067187311305840366 0.020035371627744068 0.0024198726800738488
		-0.035331766505739291 0.022818915629851173 0.0024131643890857434
		-0.015811368969038904 0.020814939554328296 0.002189959738081928
		0.00080274421724109348 0.018346498958621792 0.0019895797713032157
		0.018099772740760082 0.021422836755502144 0.0022691419216011441
		0.03840416667366145 0.023798381436361857 0.0025568815358987793
		0.070022431304530924 0.020610099863247189 0.0025821075195014568
		0.098597611847571917 0.013719619836967701 0.0021987166301139422
		0.10955539768667404 0.0024512291575648324 0.0010453082087781985
		0.11185427219439766 -0.010446085310610826 -0.00050291658921202656
		0.11144213608097754 -0.023035400068747026 -0.0023681082198900691
		0.10277620319986208 -0.033556237220187225 -0.0040196125082327047
		0.078905833869703623 -0.038685033168729177 -0.0047280293843651655
		0.050002489405124625 -0.041174121514197755 -0.0050117469888754113
		0.02512936415421467 -0.042682368847447284 -0.0051346083095853952
		0.00066056345587046288 -0.043166612599186943 -0.0051308487349183167
		-0.0239619843129097 -0.043562671196173602 -0.0051853999411157169
		-0.048878620973566454 -0.042592468241118613 -0.0051100160525444811
		-0.077267781553929091 -0.03952369077129772 -0.0048645691772395312
		-0.1005732580578332 -0.033654866909774435 -0.0041896370404383093
		-0.10906770181589628 -0.023129738356267124 -0.0025763423627837376
		-0.10944291399624667 -0.01068035141808673 -0.00073292226609428127
		-0.10717077415426379 0.0023484150895576603 0.00083976957132017864
		;
createNode transform -n "polyToCurve27" -p "tongue_Mo";
createNode nurbsCurve -n "polyToCurveShape27" -p "polyToCurve27";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 30;
	setAttr ".cc" -type "nurbsCurve" 
		3 24 2 no 3
		29 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
		 26
		27
		-0.067666998135446327 0.025828142235619314 -0.012698823030462587
		-0.097070544344049423 0.019205367637470442 -0.012995363115686449
		-0.10820744618292075 0.0072252019632629422 -0.014167365632113004
		-0.1105340701714371 -0.0066286740981577053 -0.015744733665344131
		-0.11021287262912599 -0.019826947774153839 -0.017574681721643406
		-0.10170542294128569 -0.030952594348836519 -0.019178101535618112
		-0.07828682265826746 -0.037030820248667218 -0.019854707920119188
		-0.049678886900955864 -0.04020561927395673 -0.020115257322549932
		-0.024393478131349327 -0.041491120704364434 -0.020239287383749607
		0.0006645558822514061 -0.041302124528305999 -0.020220180512132042
		0.025599448868841759 -0.040594062088707354 -0.020185832520284545
		0.050872160929759873 -0.03875916860169739 -0.020012229660655093
		0.079968725897378759 -0.036176853035447876 -0.019714507701021018
		0.10391818983520214 -0.030841025476756465 -0.019003102732110675
		0.11258932909954325 -0.01965769756340089 -0.017347961463872408
		0.11294884135802494 -0.0062699736106128475 -0.015485676630552683
		0.11059222058943539 0.0074025836230550554 -0.013942760909390339
		0.099501675402656822 0.019283337829787868 -0.012819378829614684
		0.07060623317255689 0.026401034576454964 -0.012533498593909214
		0.038661020986934289 0.029519965480450612 -0.012658210683279202
		0.018200339412947256 0.026600318644946306 -0.012986842028901451
		0.00081562833215912366 0.023083150179479716 -0.013276651482944817
		-0.015812813677817152 0.025992466350712087 -0.013067536644870056
		-0.035417236992262707 0.02853960479044413 -0.012804919379849051
		-0.067666998135446327 0.025828142235619314 -0.012698823030462587
		-0.097070544344049423 0.019205367637470442 -0.012995363115686449
		-0.10820744618292075 0.0072252019632629422 -0.014167365632113004
		;
createNode transform -n "polyToCurve28" -p "tongue_Mo";
createNode nurbsCurve -n "polyToCurveShape28" -p "polyToCurve28";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 30;
	setAttr ".cc" -type "nurbsCurve" 
		3 24 2 no 3
		29 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
		 26
		27
		-0.068006440536709942 0.031885621822209075 -0.02830625648934592
		-0.097691572891643069 0.024963050876455818 -0.028585177846269707
		-0.10893942586142413 0.012321832722504766 -0.029848129047496001
		-0.11131675635843057 -0.0023585970985061143 -0.031533257005921543
		-0.11105778265165377 -0.016438500713520585 -0.033401664250305226
		-0.10255909574293159 -0.028300297157396872 -0.035024538188025055
		-0.079048942553804902 -0.034606631381379239 -0.035722030352960323
		-0.050266618297639495 -0.037877087763253159 -0.036008306190882293
		-0.024709726281584715 -0.039498492411494376 -0.036189951466056691
		0.00066852261287828757 -0.039531765085276296 -0.036209856756879773
		0.0259562654506236 -0.038584078213587052 -0.036133103946895874
		0.051531922140661407 -0.036403499895458567 -0.035899704884926734
		0.080770693623144305 -0.033733013990009601 -0.035576549027549649
		0.10477030681429408 -0.028195045645967896 -0.034848085435042794
		0.11342193814372728 -0.016345528020235034 -0.033186487931581819
		0.11372041765967071 -0.0021269209474083593 -0.031295471682051809
		0.11131299149262956 0.012423497606987634 -0.029633377239930151
		0.10013363252886869 0.025034248878832804 -0.028408502263615458
		0.071051750833759766 0.032470303405543681 -0.028155575804921781
		0.038908370407454596 0.035585035316985612 -0.02835364423708011
		0.018312030491133779 0.032138789335302911 -0.028748420960060386
		0.00082951719598628915 0.028175624221075203 -0.029074633945459699
		-0.015819839433696442 0.031522003136627959 -0.028810892349392242
		-0.035485143131912047 0.034591057598868019 -0.028471266018276528
		-0.068006440536709942 0.031885621822209075 -0.02830625648934592
		-0.097691572891643069 0.024963050876455818 -0.028585177846269707
		-0.10893942586142413 0.012321832722504766 -0.029848129047496001
		;
createNode transform -n "polyToCurve29" -p "tongue_Mo";
createNode nurbsCurve -n "polyToCurveShape29" -p "polyToCurve29";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 30;
	setAttr ".cc" -type "nurbsCurve" 
		3 24 2 no 3
		29 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
		 26
		27
		-0.068244653058876711 0.038083686881855747 -0.04466650163170173
		-0.098151865741924263 0.030661964473335281 -0.045076444585337799
		-0.10949146779567651 0.017287427502444414 -0.04652413516519175
		-0.11191187359001063 0.0017675148174241609 -0.048387223074512827
		-0.11169860004768829 -0.013155821966728772 -0.050342460720255236
		-0.10319719697385958 -0.025703591746193879 -0.05201742094384209
		-0.079587567043445689 -0.032231783294665736 -0.052760132239682282
		-0.050651766238542444 -0.035593505364602381 -0.053086158869706614
		-0.024913025196522116 -0.037508782673110364 -0.053327086529538069
		0.00067250089094101424 -0.037732856099938594 -0.05338296881947608
		0.026201685106148089 -0.036577012709010925 -0.053266439212607722
		0.051992266472171131 -0.034093138664908824 -0.052971388489677057
		0.081350884120313965 -0.031336769530157495 -0.052608459456819599
		0.10540767588358624 -0.025608244174849401 -0.051839984807464622
		0.11405482947199674 -0.013176326348875077 -0.050146372441022671
		0.1143127449788845 0.0018087230246343689 -0.048183905435234854
		0.11186355554166444 0.017273186192972197 -0.046327863401083941
		0.10061429444160068 0.030718669894974612 -0.044901619934771743
		0.071402637005577391 0.038683234690996549 -0.044532684881641596
		0.03911892434459964 0.041983801363774789 -0.044683839698284135
		0.018410412211406751 0.03802508414303548 -0.045159030280757781
		0.00084418846987235636 0.033581763248165308 -0.045562340211227952
		-0.015811531998431154 0.037395043206977591 -0.045201654843816698
		-0.035512793468796808 0.040970065323918232 -0.044769514758712485
		-0.068244653058876711 0.038083686881855747 -0.04466650163170173
		-0.098151865741924263 0.030661964473335281 -0.045076444585337799
		-0.10949146779567651 0.017287427502444414 -0.04652413516519175
		;
createNode transform -n "polyToCurve30" -p "tongue_Mo";
createNode nurbsCurve -n "polyToCurveShape30" -p "polyToCurve30";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 30;
	setAttr ".cc" -type "nurbsCurve" 
		3 24 2 no 3
		29 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
		 26
		27
		-0.015766970997830965 0.04360307985666266 -0.062401348177487326
		0.00085942245969203182 0.039259409425507 -0.062897741265592347
		0.018471042476911993 0.044246038384607625 -0.062362112905696862
		0.039265422894786926 0.048706474038626019 -0.061803233929514173
		0.071702519397195047 0.044905156773296762 -0.061913380982207326
		0.10106449699873267 0.036082917789085359 -0.062631704255990642
		0.11238972902373744 0.021710864464618417 -0.064327556548578663
		0.11486956857860471 0.0053626086511470586 -0.066402561985150058
		0.11460289266747432 -0.010227527458946636 -0.068490307779268997
		0.10590536881099985 -0.02307056751042889 -0.070264212760010047
		0.081748486941202778 -0.028971373153634686 -0.071104575055965374
		0.05226370153160334 -0.03181410817947572 -0.071524478092597848
		0.026337569278079325 -0.034497461061903559 -0.071875853104038809
		0.00067653049061037487 -0.035782719402133664 -0.072022588903325815
		-0.025005684241922267 -0.035445987844759483 -0.07194038710880693
		-0.050844288477507306 -0.033341503733598905 -0.071645829945649039
		-0.079936149336795104 -0.029886935113758679 -0.071262602708473247
		-0.10368262024640292 -0.023168094525965927 -0.070445231917715845
		-0.11223152846627436 -0.010170336326139812 -0.068682204688984561
		-0.1124402525618548 0.0053872968861892424 -0.066595413938352999
		-0.10998834893774986 0.021771106438243194 -0.064516975853685002
		-0.098556843115520973 0.036039706193845805 -0.062804618328250128
		-0.068420525281379665 0.044298213908901693 -0.062043632297128289
		-0.035477523735530481 0.047673419234390169 -0.061883310712301597
		-0.015766970997830965 0.04360307985666266 -0.062401348177487326
		0.00085942245969203182 0.039259409425507 -0.062897741265592347
		0.018471042476911993 0.044246038384607625 -0.062362112905696862
		;
createNode transform -n "polyToCurve31" -p "tongue_Mo";
createNode nurbsCurve -n "polyToCurveShape31" -p "polyToCurve31";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 30;
	setAttr ".cc" -type "nurbsCurve" 
		3 24 2 no 3
		29 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
		 26
		27
		0.072024639949362687 0.050667303145077711 -0.079435382370745572
		0.039412087770003164 0.05508554182581428 -0.079008636032240259
		0.018529198773748149 0.050192971601645313 -0.079655594921725859
		0.00087350070090699882 0.044693747838771468 -0.080342385827334523
		-0.015727974597375408 0.049539210104639575 -0.079698823956703108
		-0.035455586116584954 0.05403633267162522 -0.079094910690137021
		-0.068624922108598538 0.050057370739354276 -0.079568207915775083
		-0.099003190309937081 0.04085782109352231 -0.080745938724719704
		-0.11052864639313106 0.025658888793721985 -0.082780749716435828
		-0.11300371245028722 0.0084357042178873978 -0.085133887550490173
		-0.11277548998316465 -0.0076250133940389377 -0.087421268221633527
		-0.10414801762140288 -0.020936825568489477 -0.089331619730746159
		-0.080224653757946351 -0.027826528168787543 -0.090252144970974793
		-0.050954004162836283 -0.031367698944318151 -0.090703379963754313
		-0.025047619328409838 -0.033570121761261042 -0.091046451272411802
		0.00067986476056758089 -0.0339519741325554 -0.091146790164417721
		0.026416698286499677 -0.032608234970083486 -0.090978770005036999
		0.052442607994283963 -0.029818283943195845 -0.090576601657246444
		0.082083456167390878 -0.026894699732711438 -0.090088884950450004
		0.10638907799060193 -0.020832864216107319 -0.089146602833212796
		0.11517064034321628 -0.0076816059303251123 -0.087226722979012641
		0.11546999924928004 0.0084068364222100126 -0.084939891042515148
		0.11296609427949846 0.025588525521254964 -0.082592164365170861
		0.10155875226622531 0.040889728683321844 -0.080574543781003899
		0.072024639949362687 0.050667303145077711 -0.079435382370745572
		0.039412087770003164 0.05508554182581428 -0.079008636032240259
		0.018529198773748149 0.050192971601645313 -0.079655594921725859
		;
createNode transform -n "polyToCurve32" -p "tongue_Mo";
createNode nurbsCurve -n "polyToCurveShape32" -p "polyToCurve32";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 30;
	setAttr ".cc" -type "nurbsCurve" 
		3 24 2 no 3
		29 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
		 26
		27
		-0.025098754262517221 -0.032141198257434403 -0.10966188918640288
		0.00068175595511251494 -0.032511239431897578 -0.10977357268789048
		0.02649186332794046 -0.031172146131369292 -0.10959264861618864
		0.052625301772382636 -0.02835754146010571 -0.10914532295107665
		0.082475815242700479 -0.025364624139658006 -0.10858542191947822
		0.10698446194458232 -0.019145982855285657 -0.10751296755571048
		0.11586260653406208 -0.0057210363428859034 -0.10536404276330433
		0.11619314066958907 0.010813506827903491 -0.10278433586502542
		0.11366719597141188 0.028758162462210655 -0.10008142465534756
		0.10217159602410165 0.044901838699840844 -0.097705947140095201
		0.072442183424765771 0.055500907298972821 -0.096236419818024027
		0.039623166866495835 0.060453493209614517 -0.095596829708299733
		0.018620155732518927 0.055257203335774607 -0.096337446804099391
		0.0008847123184396573 0.049369963573629813 -0.097157804571694109
		-0.015736374495053305 0.054596530969864797 -0.096382883342428075
		-0.03552320860759748 0.059394018976964717 -0.095686612514259167
		-0.068948657557291515 0.054889325209220872 -0.096370797253916493
		-0.099587641548063086 0.044877854227899805 -0.097876656475980012
		-0.11121097126731712 0.028836793832701643 -0.10026950181469774
		-0.11370397691317082 0.010847691922616868 -0.1029787708708276
		-0.1134494865270441 -0.0056628227727113477 -0.10555997971206274
		-0.10472604078385148 -0.019252804945541012 -0.10770024927532912
		-0.080583055688425803 -0.026305003789881713 -0.10875146317666444
		-0.051090733292431821 -0.029918707070835472 -0.10927484944642647
		-0.025098754262517221 -0.032141198257434403 -0.10966188918640288
		0.00068175595511251494 -0.032511239431897578 -0.10977357268789048
		0.02649186332794046 -0.031172146131369292 -0.10959264861618864
		;
createNode transform -n "polyToCurve33" -p "tongue_Mo";
createNode nurbsCurve -n "polyToCurveShape33" -p "polyToCurve33";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 30;
	setAttr ".cc" -type "nurbsCurve" 
		3 24 2 no 3
		29 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
		 26
		27
		-0.015768906273643642 0.058516172260556748 -0.11420146886458488
		0.00089153041551506081 0.052970653495635248 -0.11487182672790686
		0.018706415739581622 0.059191906873090297 -0.11415286314647899
		0.039820681026774128 0.064643399500589935 -0.11351302758238696
		0.072828203745965658 0.059233903131217937 -0.11409955785980387
		0.10273401812281671 0.047896371733083122 -0.11540981868282704
		0.11430633035208498 0.030893469805452892 -0.11749082780069556
		0.11684965845754429 0.012144837507934922 -0.11984095330912352
		0.11649478481065768 -0.0048711099945106745 -0.12205819885233676
		0.10753121197008261 -0.018568033218673955 -0.12389054142358877
		0.082827812582411148 -0.024831203785113269 -0.12478616762169657
		0.052777303458787235 -0.027767373217563649 -0.1252423628672282
		0.026551679813557136 -0.030548656443501434 -0.12561919184345741
		0.00068197908370663774 -0.031864234872261171 -0.12577659276805173
		-0.025150088103813008 -0.031523092855867831 -0.12568908490194761
		-0.051224618747712551 -0.029337936493726732 -0.12537307920557897
		-0.080918301133585419 -0.025781090377027086 -0.12495372605855846
		-0.10525965636176743 -0.018682683382442302 -0.1240795946851872
		-0.11406905770660683 -0.0048182111836501925 -0.1222563506965272
		-0.11434756987643396 0.012176102019173201 -0.12003794471887427
		-0.11184118773768488 0.030971172172242115 -0.11768144011581917
		-0.10013527057297314 0.047870083162707959 -0.11558325369350524
		-0.069275139638391409 0.05860752189506574 -0.11423828942721476
		-0.035626769769487851 0.063559595263498789 -0.11360814917312098
		-0.015768906273643642 0.058516172260556748 -0.11420146886458488
		0.00089153041551506081 0.052970653495635248 -0.11487182672790686
		0.018706415739581622 0.059191906873090297 -0.11415286314647899
		;
createNode transform -n "polyToCurve34" -p "tongue_Mo";
createNode nurbsCurve -n "polyToCurveShape34" -p "polyToCurve34";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 30;
	setAttr ".cc" -type "nurbsCurve" 
		3 24 2 no 3
		29 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
		 26
		27
		-0.015802325541918464 0.061039263784934031 -0.13490248266885738
		0.0008924339234284383 0.055178414470340963 -0.13501226492081181
		0.018750472307070346 0.061750255499687212 -0.13484705593738511
		0.039926680762169549 0.067488332009303736 -0.1347024340076417
		0.073055689737940355 0.061694224538049042 -0.13480785437146459
		0.10307706032040106 0.049650451677489348 -0.13507009767184414
		0.11469682995533943 0.031668142068949204 -0.13551591000478846
		0.11725015530917668 0.011963046102011666 -0.13601476084415848
		0.11688320533642667 -0.0056571181830810694 -0.13646514528572243
		0.10786902532208359 -0.019657125096982298 -0.13680655374583134
		0.083041725584635323 -0.025744496079716045 -0.13688310214474006
		0.052864101164181276 -0.028383271702927933 -0.13687940906650475
		0.026584774693522696 -0.031097227804220372 -0.13696014768619508
		0.00068030665781635498 -0.032414680025747183 -0.13702944896496008
		-0.025192621458903358 -0.032079681079149519 -0.13703038479640223
		-0.051325817075693357 -0.029968795593567844 -0.13701098437216644
		-0.081137346944580038 -0.026713516330209477 -0.13705206626473682
		-0.10559177393436224 -0.019793111604515152 -0.13699815541126276
		-0.11444982636952281 -0.0056256253483485969 -0.13666837223082173
		-0.11474091817284311 0.011973776526351922 -0.13621930181527636
		-0.1122252415978648 0.031728374429403308 -0.13571474546305956
		-0.10047110056982241 0.049604785463676457 -0.13525217497353764
		-0.069487807571286156 0.061025405373453197 -0.13495761662589839
		-0.035712618590757465 0.066346178644317383 -0.13480929768607669
		-0.015802325541918464 0.061039263784934031 -0.13490248266885738
		0.0008924339234284383 0.055178414470340963 -0.13501226492081181
		0.018750472307070346 0.061750255499687212 -0.13484705593738511
		;
createNode transform -n "polyToCurve35" -p "tongue_Mo";
createNode nurbsCurve -n "polyToCurveShape35" -p "polyToCurve35";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 30;
	setAttr ".cc" -type "nurbsCurve" 
		3 24 2 no 3
		29 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
		 26
		27
		-0.070254222820334777 0.060720723329901 -0.15607458178485861
		-0.036556546021722085 0.066007338618647993 -0.15663758406726361
		-0.016287994596339797 0.060418355384899085 -0.15603790896101016
		0.00087178173773732074 0.054338242279347235 -0.15536860269764355
		0.019097125599481339 0.061180278075875061 -0.15597491674820199
		0.040500973900235472 0.067234194954811047 -0.15651761993509744
		0.073521169990296384 0.061453271771018468 -0.15591290362508622
		0.10335734275971083 0.049260147274774707 -0.15474064572584328
		0.11493644665701758 0.030919218749290392 -0.15315014656823547
		0.11751438188464955 0.010858489450628459 -0.15134986669124789
		0.11727137781511122 -0.0069008501348349124 -0.14949257912587935
		0.1083613566832442 -0.020873964414828871 -0.14789464672695693
		0.083482129291709853 -0.026652658441582638 -0.1470459685373684
		0.053182259309553871 -0.028985819795219966 -0.14657906665179823
		0.026757376045910775 -0.03173553370150449 -0.14626275746446252
		0.00066436160407779476 -0.03315401227574577 -0.14617805711965476
		-0.025471878469197441 -0.032743975242807033 -0.14633570732092624
		-0.05185970277308341 -0.030615984999791204 -0.14671516897078599
		-0.081849846393898015 -0.027662010853037024 -0.14721825173893818
		-0.10639025895662234 -0.021040551799700123 -0.14808838280644779
		-0.11515276302325733 -0.0068996959753765382 -0.14970040021512623
		-0.11531640781383547 0.010837354728916247 -0.15156197045940534
		-0.11277525680153236 0.030950658028759119 -0.15335732025934054
		-0.10105591097498443 0.049182346968760872 -0.15493169638683843
		-0.070254222820334777 0.060720723329901 -0.15607458178485861
		-0.036556546021722085 0.066007338618647993 -0.15663758406726361
		-0.016287994596339797 0.060418355384899085 -0.15603790896101016
		;
createNode transform -n "polyToCurve36" -p "tongue_Mo";
createNode nurbsCurve -n "polyToCurveShape36" -p "polyToCurve36";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 30;
	setAttr ".cc" -type "nurbsCurve" 
		3 24 2 no 3
		29 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
		 26
		27
		-0.072241918839776181 0.056271223449926931 -0.17513497795070884
		-0.038934328071256512 0.060796644685718132 -0.17644048014278824
		-0.017677274102286672 0.054905996902354308 -0.17515977977327354
		0.00081393363996811558 0.048795132704254361 -0.17373041000522141
		0.020091170606352345 0.055730003461963717 -0.17509121194641067
		0.04210338808239051 0.062126892556167053 -0.17631125780743276
		0.074621143715620661 0.057082445081678673 -0.17496619794400597
		0.10373153857433007 0.045821527266654408 -0.17247540724942903
		0.11512297326448653 0.02848373934306718 -0.16938705181766223
		0.11776209564471653 0.0094215243942800224 -0.16589040840243829
		0.11790278852005066 -0.0074240950760099981 -0.162048130492461
		0.10937174765724481 -0.020679257096831851 -0.15878843279071225
		0.084513587416674293 -0.026103848288829345 -0.15744451710025945
		0.054028390119028248 -0.028355600373461104 -0.15686389679561594
		0.027235710879490546 -0.031381247623332088 -0.1561742968574899
		0.00062176802669439439 -0.033073669005647122 -0.15586828427036561
		-0.026233399489924064 -0.032448987662367978 -0.15625495296481046
		-0.053291653714106164 -0.030084205341829172 -0.15701235767631588
		-0.083665467733634064 -0.027186303149117821 -0.15762394341351363
		-0.10832300299456141 -0.02088146615593782 -0.15898281210148363
		-0.11673889756549455 -0.0074550537733039874 -0.16225678556702641
		-0.11650638465636326 0.0093634759116293653 -0.16610505970664377
		-0.11390341382660002 0.028480280394883456 -0.16959705945916667
		-0.10235047409630346 0.045703153515916847 -0.17267009833834232
		-0.072241918839776181 0.056271223449926931 -0.17513497795070884
		-0.038934328071256512 0.060796644685718132 -0.17644048014278824
		-0.017677274102286672 0.054905996902354308 -0.17515977977327354
		;
createNode transform -n "polyToCurve37" -p "tongue_Mo";
createNode nurbsCurve -n "polyToCurveShape37" -p "polyToCurve37";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 30;
	setAttr ".cc" -type "nurbsCurve" 
		3 24 2 no 3
		29 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
		 26
		27
		0.022478678130682734 0.047746780961279628 -0.19309448475552765
		0.0005710249553153965 0.034415073834516467 -0.18906117456033505
		-0.020670770542163104 0.047025289118134979 -0.19316276726710901
		-0.037302939142435022 0.059326001443431947 -0.19771274678680173
		-0.073039466024502744 0.046922803191633312 -0.19233427615285306
		-0.11597919109472846 0.045825650780269171 -0.19028712870623243
		-0.11100176513052666 0.024208225584262728 -0.18484313866394106
		-0.12329974470102838 0.0064121866287736506 -0.18056822930241689
		-0.11441325316714346 -0.0061491245041424957 -0.17501383981349455
		-0.12294024847832861 -0.024718158247213417 -0.16770537734593344
		-0.082997767513620091 -0.024491029372238175 -0.16869268692032544
		-0.055194705951825317 -0.03029376033561124 -0.16750690791458325
		-0.027303398350785737 -0.030773214563637158 -0.16671771118742437
		0.00085730778997920138 -0.034857247376636979 -0.16498221266012095
		0.027852174431089862 -0.029846242585088341 -0.16663533905481268
		0.054906001748368093 -0.027572929682911997 -0.1673083588969651
		0.08288982655912229 -0.02344388682779492 -0.16851318002727925
		0.12267670341918013 -0.024845504176562595 -0.16750883719455562
		0.11432135223680581 -0.0059802106627320347 -0.17480934892582173
		0.12330388242081276 0.0064575394544438705 -0.18034364184657284
		0.11107711518172686 0.02433855229564014 -0.1846379554453943
		0.11567365317014328 0.045685283528522899 -0.19008146675171758
		0.0741862676716432 0.047725878470639346 -0.19216816654996335
		0.040107264364452437 0.061449685254935299 -0.19755681279771178
		0.022478678130682734 0.047746780961279628 -0.19309448475552765
		0.0005710249553153965 0.034415073834516467 -0.18906117456033505
		-0.020670770542163104 0.047025289118134979 -0.19316276726710901
		;
createNode transform -s -n "persp";
	setAttr ".v" no;
	setAttr ".t" -type "double3" -0.11311220085472684 2.4226370125052501 14.368952678834123 ;
	setAttr ".r" -type "double3" -11.738352729602637 -3.0000000000006488 -4.9764367233621779e-017 ;
createNode camera -s -n "perspShape" -p "persp";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999986;
	setAttr ".coi" 14.703058612047137;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".tp" -type "double3" 2.0747733802976995 0 0.037734458701718494 ;
	setAttr ".hc" -type "string" "viewSet -p %camera";
createNode transform -s -n "top";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 100.1 0 ;
	setAttr ".r" -type "double3" -89.999999999999986 0 0 ;
createNode camera -s -n "topShape" -p "top";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 100.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "top";
	setAttr ".den" -type "string" "top_depth";
	setAttr ".man" -type "string" "top_mask";
	setAttr ".hc" -type "string" "viewSet -t %camera";
	setAttr ".o" yes;
createNode transform -s -n "front";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 0 100.1 ;
createNode camera -s -n "frontShape" -p "front";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 100.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "front";
	setAttr ".den" -type "string" "front_depth";
	setAttr ".man" -type "string" "front_mask";
	setAttr ".hc" -type "string" "viewSet -f %camera";
	setAttr ".o" yes;
createNode transform -s -n "side";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 100.1 0 0 ;
	setAttr ".r" -type "double3" 0 89.999999999999986 0 ;
createNode camera -s -n "sideShape" -p "side";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 100.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
parent -s -nc -r -add "|GRP_PANNEL_TEMPLATE|Facial_CTRL_FRAME_GRP|Facial_CTRL_FRAME|head_CTRL_GRP|head_CTRL|c_eyebrows_GRP|c_Lf_eyebrows_CTRL_GRP_GRP|c_Lf_eyebrows_CTRL_GRP|c_Lf_eyebrows_CTRL|GRP_c_Lf_eyebrows_01_FRAME|c_Lf_eyebrows_01_FRAME|GRP_c_Lf_eyebrows_01_CTRL|c_Lf_eyebrows_01_CTRL|c_eyebrows_CTRLShape" "c_Rt_eyebrows_03_CTRL" ;
parent -s -nc -r -add "|GRP_PANNEL_TEMPLATE|Facial_CTRL_FRAME_GRP|Facial_CTRL_FRAME|head_CTRL_GRP|head_CTRL|c_eyebrows_GRP|c_Lf_eyebrows_CTRL_GRP_GRP|c_Lf_eyebrows_CTRL_GRP|c_Lf_eyebrows_CTRL|GRP_c_Lf_eyebrows_01_FRAME|c_Lf_eyebrows_01_FRAME|GRP_c_Lf_eyebrows_01_CTRL|c_Lf_eyebrows_01_CTRL|c_eyebrows_CTRLShape" "c_Rt_eyebrows_02_CTRL" ;
parent -s -nc -r -add "|GRP_PANNEL_TEMPLATE|Facial_CTRL_FRAME_GRP|Facial_CTRL_FRAME|head_CTRL_GRP|head_CTRL|c_eyebrows_GRP|c_Lf_eyebrows_CTRL_GRP_GRP|c_Lf_eyebrows_CTRL_GRP|c_Lf_eyebrows_CTRL|GRP_c_Lf_eyebrows_01_FRAME|c_Lf_eyebrows_01_FRAME|GRP_c_Lf_eyebrows_01_CTRL|c_Lf_eyebrows_01_CTRL|c_eyebrows_CTRLShape" "c_Rt_eyebrows_01_CTRL" ;
parent -s -nc -r -add "|GRP_PANNEL_TEMPLATE|Facial_CTRL_FRAME_GRP|Facial_CTRL_FRAME|head_CTRL_GRP|head_CTRL|c_eyebrows_GRP|c_Lf_eyebrows_CTRL_GRP_GRP|c_Lf_eyebrows_CTRL_GRP|c_Lf_eyebrows_CTRL|GRP_c_Lf_eyebrows_01_FRAME|c_Lf_eyebrows_01_FRAME|GRP_c_Lf_eyebrows_01_CTRL|c_Lf_eyebrows_01_CTRL|c_eyebrows_CTRLShape" "c_Lf_eyebrows_02_CTRL" ;
parent -s -nc -r -add "|GRP_PANNEL_TEMPLATE|Facial_CTRL_FRAME_GRP|Facial_CTRL_FRAME|head_CTRL_GRP|head_CTRL|c_eyebrows_GRP|c_Lf_eyebrows_CTRL_GRP_GRP|c_Lf_eyebrows_CTRL_GRP|c_Lf_eyebrows_CTRL|GRP_c_Lf_eyebrows_01_FRAME|c_Lf_eyebrows_01_FRAME|GRP_c_Lf_eyebrows_01_CTRL|c_Lf_eyebrows_01_CTRL|c_eyebrows_CTRLShape" "c_Lf_eyebrows_03_CTRL" ;
parent -s -nc -r -add "|GRP_PANNEL_TEMPLATE|Facial_CTRL_FRAME_GRP|Facial_CTRL_FRAME|head_CTRL_GRP|head_CTRL|GRP_c_Lf_cheek_FRAME|c_Lf_cheek_FRAME|GRP_c_Lf_cheek_CTRL|c_Lf_cheek_CTRL|c_eyeStretch_CTRLShape" "c_Rt_cheek_CTRL" ;
parent -s -nc -r -add "|GRP_PANNEL_TEMPLATE|Facial_CTRL_FRAME_GRP|Facial_CTRL_FRAME|head_CTRL_GRP|head_CTRL|c_Lf_eyelids_CTRL_GRP|c_Lf_eyelids_CTRL|GRP_c_Lf_up_eyelids_FRAME|c_Lf_up_eyelids_FRAME|GRP_c_Lf_up_eyelids_CTRL|c_Lf_up_eyelids_CTRL|c_up_eyelids_CTRLShape" "c_Rt_up_eyelids_CTRL" ;
parent -s -nc -r -add "|GRP_PANNEL_TEMPLATE|Facial_CTRL_FRAME_GRP|Facial_CTRL_FRAME|head_CTRL_GRP|head_CTRL|c_Lf_eyelids_CTRL_GRP|c_Lf_eyelids_CTRL|GRP_c_Lf_dn_eyelids_FRAME|c_Lf_dn_eyelids_FRAME|GRP_c_Lf_dn_eyelids_CTRL|c_Lf_dn_eyelids_CTRL|c_dn_eyelids_CTRLShape" "c_Rt_dn_eyelids_CTRL" ;
parent -s -nc -r -add "|GRP_PANNEL_TEMPLATE|Facial_CTRL_FRAME_GRP|Facial_CTRL_FRAME|head_CTRL_GRP|head_CTRL|c_mouth_CTRL_GRP|c_mouth_CTRL|GRP_c_Lf_mouthLip_FRAME|c_Lf_mouthLip_FRAME|GRP_c_Lf_mouthLip_CTRL|c_Lf_mouthLip_CTRL|c_mouthLip_CTRLShape" "c_Rt_mouthLip_CTRL" ;
createNode mentalrayItemsList -s -n "mentalrayItemsList";
createNode mentalrayGlobals -s -n "mentalrayGlobals";
createNode mentalrayOptions -s -n "miDefaultOptions";
	addAttr -ci true -m -sn "stringOptions" -ln "stringOptions" -at "compound" -nc 
		3;
	addAttr -ci true -sn "name" -ln "name" -dt "string" -p "stringOptions";
	addAttr -ci true -sn "value" -ln "value" -dt "string" -p "stringOptions";
	addAttr -ci true -sn "type" -ln "type" -dt "string" -p "stringOptions";
	setAttr -s 45 ".stringOptions";
	setAttr ".stringOptions[0].name" -type "string" "rast motion factor";
	setAttr ".stringOptions[0].value" -type "string" "1.0";
	setAttr ".stringOptions[0].type" -type "string" "scalar";
	setAttr ".stringOptions[1].name" -type "string" "rast transparency depth";
	setAttr ".stringOptions[1].value" -type "string" "8";
	setAttr ".stringOptions[1].type" -type "string" "integer";
	setAttr ".stringOptions[2].name" -type "string" "rast useopacity";
	setAttr ".stringOptions[2].value" -type "string" "true";
	setAttr ".stringOptions[2].type" -type "string" "boolean";
	setAttr ".stringOptions[3].name" -type "string" "importon";
	setAttr ".stringOptions[3].value" -type "string" "false";
	setAttr ".stringOptions[3].type" -type "string" "boolean";
	setAttr ".stringOptions[4].name" -type "string" "importon density";
	setAttr ".stringOptions[4].value" -type "string" "1.0";
	setAttr ".stringOptions[4].type" -type "string" "scalar";
	setAttr ".stringOptions[5].name" -type "string" "importon merge";
	setAttr ".stringOptions[5].value" -type "string" "0.0";
	setAttr ".stringOptions[5].type" -type "string" "scalar";
	setAttr ".stringOptions[6].name" -type "string" "importon trace depth";
	setAttr ".stringOptions[6].value" -type "string" "0";
	setAttr ".stringOptions[6].type" -type "string" "integer";
	setAttr ".stringOptions[7].name" -type "string" "importon traverse";
	setAttr ".stringOptions[7].value" -type "string" "true";
	setAttr ".stringOptions[7].type" -type "string" "boolean";
	setAttr ".stringOptions[8].name" -type "string" "shadowmap pixel samples";
	setAttr ".stringOptions[8].value" -type "string" "3";
	setAttr ".stringOptions[8].type" -type "string" "integer";
	setAttr ".stringOptions[9].name" -type "string" "ambient occlusion";
	setAttr ".stringOptions[9].value" -type "string" "false";
	setAttr ".stringOptions[9].type" -type "string" "boolean";
	setAttr ".stringOptions[10].name" -type "string" "ambient occlusion rays";
	setAttr ".stringOptions[10].value" -type "string" "256";
	setAttr ".stringOptions[10].type" -type "string" "integer";
	setAttr ".stringOptions[11].name" -type "string" "ambient occlusion cache";
	setAttr ".stringOptions[11].value" -type "string" "false";
	setAttr ".stringOptions[11].type" -type "string" "boolean";
	setAttr ".stringOptions[12].name" -type "string" "ambient occlusion cache density";
	setAttr ".stringOptions[12].value" -type "string" "1.0";
	setAttr ".stringOptions[12].type" -type "string" "scalar";
	setAttr ".stringOptions[13].name" -type "string" "ambient occlusion cache points";
	setAttr ".stringOptions[13].value" -type "string" "64";
	setAttr ".stringOptions[13].type" -type "string" "integer";
	setAttr ".stringOptions[14].name" -type "string" "irradiance particles";
	setAttr ".stringOptions[14].value" -type "string" "false";
	setAttr ".stringOptions[14].type" -type "string" "boolean";
	setAttr ".stringOptions[15].name" -type "string" "irradiance particles rays";
	setAttr ".stringOptions[15].value" -type "string" "256";
	setAttr ".stringOptions[15].type" -type "string" "integer";
	setAttr ".stringOptions[16].name" -type "string" "irradiance particles interpolate";
	setAttr ".stringOptions[16].value" -type "string" "1";
	setAttr ".stringOptions[16].type" -type "string" "integer";
	setAttr ".stringOptions[17].name" -type "string" "irradiance particles interppoints";
	setAttr ".stringOptions[17].value" -type "string" "64";
	setAttr ".stringOptions[17].type" -type "string" "integer";
	setAttr ".stringOptions[18].name" -type "string" "irradiance particles indirect passes";
	setAttr ".stringOptions[18].value" -type "string" "0";
	setAttr ".stringOptions[18].type" -type "string" "integer";
	setAttr ".stringOptions[19].name" -type "string" "irradiance particles scale";
	setAttr ".stringOptions[19].value" -type "string" "1.0";
	setAttr ".stringOptions[19].type" -type "string" "scalar";
	setAttr ".stringOptions[20].name" -type "string" "irradiance particles env";
	setAttr ".stringOptions[20].value" -type "string" "true";
	setAttr ".stringOptions[20].type" -type "string" "boolean";
	setAttr ".stringOptions[21].name" -type "string" "irradiance particles env rays";
	setAttr ".stringOptions[21].value" -type "string" "256";
	setAttr ".stringOptions[21].type" -type "string" "integer";
	setAttr ".stringOptions[22].name" -type "string" "irradiance particles env scale";
	setAttr ".stringOptions[22].value" -type "string" "1";
	setAttr ".stringOptions[22].type" -type "string" "integer";
	setAttr ".stringOptions[23].name" -type "string" "irradiance particles rebuild";
	setAttr ".stringOptions[23].value" -type "string" "true";
	setAttr ".stringOptions[23].type" -type "string" "boolean";
	setAttr ".stringOptions[24].name" -type "string" "irradiance particles file";
	setAttr ".stringOptions[24].value" -type "string" "";
	setAttr ".stringOptions[24].type" -type "string" "string";
	setAttr ".stringOptions[25].name" -type "string" "geom displace motion factor";
	setAttr ".stringOptions[25].value" -type "string" "1.0";
	setAttr ".stringOptions[25].type" -type "string" "scalar";
	setAttr ".stringOptions[26].name" -type "string" "contrast all buffers";
	setAttr ".stringOptions[26].value" -type "string" "true";
	setAttr ".stringOptions[26].type" -type "string" "boolean";
	setAttr ".stringOptions[27].name" -type "string" "finalgather normal tolerance";
	setAttr ".stringOptions[27].value" -type "string" "25.842";
	setAttr ".stringOptions[27].type" -type "string" "scalar";
	setAttr ".stringOptions[28].name" -type "string" "trace camera clip";
	setAttr ".stringOptions[28].value" -type "string" "false";
	setAttr ".stringOptions[28].type" -type "string" "boolean";
	setAttr ".stringOptions[29].name" -type "string" "unified sampling";
	setAttr ".stringOptions[29].value" -type "string" "true";
	setAttr ".stringOptions[29].type" -type "string" "boolean";
	setAttr ".stringOptions[30].name" -type "string" "samples quality";
	setAttr ".stringOptions[30].value" -type "string" "0.25 0.25 0.25 0.25";
	setAttr ".stringOptions[30].type" -type "string" "color";
	setAttr ".stringOptions[31].name" -type "string" "samples min";
	setAttr ".stringOptions[31].value" -type "string" "1.0";
	setAttr ".stringOptions[31].type" -type "string" "scalar";
	setAttr ".stringOptions[32].name" -type "string" "samples max";
	setAttr ".stringOptions[32].value" -type "string" "100.0";
	setAttr ".stringOptions[32].type" -type "string" "scalar";
	setAttr ".stringOptions[33].name" -type "string" "samples error cutoff";
	setAttr ".stringOptions[33].value" -type "string" "0.0 0.0 0.0 0.0";
	setAttr ".stringOptions[33].type" -type "string" "color";
	setAttr ".stringOptions[34].name" -type "string" "samples per object";
	setAttr ".stringOptions[34].value" -type "string" "false";
	setAttr ".stringOptions[34].type" -type "string" "boolean";
	setAttr ".stringOptions[35].name" -type "string" "progressive";
	setAttr ".stringOptions[35].value" -type "string" "false";
	setAttr ".stringOptions[35].type" -type "string" "boolean";
	setAttr ".stringOptions[36].name" -type "string" "progressive max time";
	setAttr ".stringOptions[36].value" -type "string" "0";
	setAttr ".stringOptions[36].type" -type "string" "integer";
	setAttr ".stringOptions[37].name" -type "string" "progressive subsampling size";
	setAttr ".stringOptions[37].value" -type "string" "1";
	setAttr ".stringOptions[37].type" -type "string" "integer";
	setAttr ".stringOptions[38].name" -type "string" "iray";
	setAttr ".stringOptions[38].value" -type "string" "false";
	setAttr ".stringOptions[38].type" -type "string" "boolean";
	setAttr ".stringOptions[39].name" -type "string" "light relative scale";
	setAttr ".stringOptions[39].value" -type "string" "0.31831";
	setAttr ".stringOptions[39].type" -type "string" "scalar";
	setAttr ".stringOptions[40].name" -type "string" "trace camera motion vectors";
	setAttr ".stringOptions[40].value" -type "string" "false";
	setAttr ".stringOptions[40].type" -type "string" "boolean";
	setAttr ".stringOptions[41].name" -type "string" "ray differentials";
	setAttr ".stringOptions[41].value" -type "string" "true";
	setAttr ".stringOptions[41].type" -type "string" "boolean";
	setAttr ".stringOptions[42].name" -type "string" "environment lighting mode";
	setAttr ".stringOptions[42].value" -type "string" "off";
	setAttr ".stringOptions[42].type" -type "string" "string";
	setAttr ".stringOptions[43].name" -type "string" "environment lighting quality";
	setAttr ".stringOptions[43].value" -type "string" "0.167";
	setAttr ".stringOptions[43].type" -type "string" "scalar";
	setAttr ".stringOptions[44].name" -type "string" "environment lighting shadow";
	setAttr ".stringOptions[44].value" -type "string" "transparent";
	setAttr ".stringOptions[44].type" -type "string" "string";
createNode mentalrayFramebuffer -s -n "miDefaultFramebuffer";
createNode clamp -n "A_dnclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "A_dnclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "A_lfclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "A_lfclamp_NYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "A_lfclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "A_lfclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "A_rtclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "A_rtclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "A_upclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "A_upclamp_NXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "A_upclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "A_upclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_dn_mouthLip_dnclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_dn_mouthLip_dnclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_dn_mouthLip_lfclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_dn_mouthLip_lfclamp_NYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_dn_mouthLip_lfclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_dn_mouthLip_lfclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_dn_mouthLip_rtclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_dn_mouthLip_rtclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_dn_mouthLip_upclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_dn_mouthLip_upclamp_NXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_dn_mouthLip_upclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_dn_mouthLip_upclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_jaw_dn_dnclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_jaw_dn_dnclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_jaw_dn_lfclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_jaw_dn_lfclamp_NYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_jaw_dn_lfclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_jaw_dn_lfclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_jaw_dn_rtclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_jaw_dn_rtclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_jaw_dn_upclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_jaw_dn_upclamp_NXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_jaw_dn_upclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_jaw_dn_upclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_jaw_up_dnclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_jaw_up_dnclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_jaw_up_lfclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_jaw_up_lfclamp_NYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_jaw_up_lfclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_jaw_up_lfclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_jaw_up_rtclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_jaw_up_rtclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_jaw_up_upclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_jaw_up_upclamp_NXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_jaw_up_upclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_jaw_up_upclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_dn_eyelids_dnclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_dn_eyelids_dnclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_dn_eyelids_lfclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_dn_eyelids_lfclamp_NYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_dn_eyelids_lfclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_dn_eyelids_lfclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_dn_eyelids_rtclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_dn_eyelids_rtclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_dn_eyelids_upclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_dn_eyelids_upclamp_NXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_dn_eyelids_upclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_dn_eyelids_upclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_eyebrows_01_dnclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_eyebrows_01_dnclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_eyebrows_01_lfclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_eyebrows_01_lfclamp_NYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_eyebrows_01_lfclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_eyebrows_01_lfclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_eyebrows_01_rtclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_eyebrows_01_rtclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_eyebrows_01_upclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_eyebrows_01_upclamp_NXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_eyebrows_01_upclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_eyebrows_01_upclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_eyebrows_02_dnclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_eyebrows_02_dnclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_eyebrows_02_lfclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_eyebrows_02_lfclamp_NYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_eyebrows_02_lfclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_eyebrows_02_lfclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_eyebrows_02_rtclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_eyebrows_02_rtclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_eyebrows_02_upclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_eyebrows_02_upclamp_NXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_eyebrows_02_upclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_eyebrows_02_upclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_eyebrows_03_dnclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_eyebrows_03_dnclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_eyebrows_03_lfclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_eyebrows_03_lfclamp_NYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_eyebrows_03_lfclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_eyebrows_03_lfclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_eyebrows_03_rtclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_eyebrows_03_rtclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_eyebrows_03_upclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_eyebrows_03_upclamp_NXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_eyebrows_03_upclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_eyebrows_03_upclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_eyeStretch_dnclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_eyeStretch_dnclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_eyeStretch_lfclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_eyeStretch_lfclamp_NYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_eyeStretch_lfclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_eyeStretch_lfclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_eyeStretch_rtclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_eyeStretch_rtclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_eyeStretch_upclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_eyeStretch_upclamp_NXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_eyeStretch_upclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_eyeStretch_upclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_mouthLip_dnclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_mouthLip_dnclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_mouthLip_lfclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_mouthLip_lfclamp_NYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_mouthLip_lfclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_mouthLip_lfclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_mouthLip_rtclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_mouthLip_rtclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_mouthLip_upclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_mouthLip_upclamp_NXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_mouthLip_upclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_mouthLip_upclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_up_eyelids_dnclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_up_eyelids_dnclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_up_eyelids_lfclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_up_eyelids_lfclamp_NYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_up_eyelids_lfclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_up_eyelids_lfclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_up_eyelids_rtclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_up_eyelids_rtclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_up_eyelids_upclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_up_eyelids_upclamp_NXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_up_eyelids_upclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Lf_up_eyelids_upclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_nose_dnclamp_finalrange";
	setAttr ".mx" -type "float3" 1 0 0 ;
createNode clamp -n "c_nose_dnclamp_PYrange";
	setAttr ".mx" -type "float3" 1 0 0 ;
createNode clamp -n "c_nose_lfclamp_finalrange";
	setAttr ".mx" -type "float3" 1 0 0 ;
createNode clamp -n "c_nose_lfclamp_NYrange";
	setAttr ".mx" -type "float3" 1 0 0 ;
createNode clamp -n "c_nose_lfclamp_PXrange";
	setAttr ".mx" -type "float3" 1 0 0 ;
createNode clamp -n "c_nose_lfclamp_PYrange";
	setAttr ".mx" -type "float3" 1 0 0 ;
createNode clamp -n "c_nose_rtclamp_finalrange";
	setAttr ".mx" -type "float3" 1 0 0 ;
createNode clamp -n "c_nose_rtclamp_PXrange";
	setAttr ".mx" -type "float3" 1 0 0 ;
createNode clamp -n "c_nose_upclamp_finalrange";
	setAttr ".mx" -type "float3" 1 0 0 ;
createNode clamp -n "c_nose_upclamp_NXrange";
	setAttr ".mx" -type "float3" 1 0 0 ;
createNode clamp -n "c_nose_upclamp_PXrange";
	setAttr ".mx" -type "float3" 1 0 0 ;
createNode clamp -n "c_nose_upclamp_PYrange";
	setAttr ".mx" -type "float3" 1 0 0 ;
createNode clamp -n "c_Rt_dn_eyelids_dnclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_dn_eyelids_dnclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_dn_eyelids_lfclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_dn_eyelids_lfclamp_NYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_dn_eyelids_lfclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_dn_eyelids_lfclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_dn_eyelids_rtclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_dn_eyelids_rtclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_dn_eyelids_upclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_dn_eyelids_upclamp_NXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_dn_eyelids_upclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_dn_eyelids_upclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_eyebrows_01_dnclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_eyebrows_01_dnclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_eyebrows_01_lfclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_eyebrows_01_lfclamp_NYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_eyebrows_01_lfclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_eyebrows_01_lfclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_eyebrows_01_rtclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_eyebrows_01_rtclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_eyebrows_01_upclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_eyebrows_01_upclamp_NXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_eyebrows_01_upclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_eyebrows_01_upclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_eyebrows_02_dnclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_eyebrows_02_dnclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_eyebrows_02_lfclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_eyebrows_02_lfclamp_NYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_eyebrows_02_lfclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_eyebrows_02_lfclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_eyebrows_02_rtclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_eyebrows_02_rtclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_eyebrows_02_upclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_eyebrows_02_upclamp_NXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_eyebrows_02_upclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_eyebrows_02_upclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_eyebrows_03_dnclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_eyebrows_03_dnclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_eyebrows_03_lfclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_eyebrows_03_lfclamp_NYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_eyebrows_03_lfclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_eyebrows_03_lfclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_eyebrows_03_rtclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_eyebrows_03_rtclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_eyebrows_03_upclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_eyebrows_03_upclamp_NXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_eyebrows_03_upclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_eyebrows_03_upclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_eyeStretch_dnclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_eyeStretch_dnclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_eyeStretch_lfclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_eyeStretch_lfclamp_NYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_eyeStretch_lfclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_eyeStretch_lfclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_eyeStretch_rtclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_eyeStretch_rtclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_eyeStretch_upclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_eyeStretch_upclamp_NXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_eyeStretch_upclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_eyeStretch_upclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_mouthLip_dnclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_mouthLip_dnclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_mouthLip_lfclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_mouthLip_lfclamp_NYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_mouthLip_lfclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_mouthLip_lfclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_mouthLip_rtclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_mouthLip_rtclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_mouthLip_upclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_mouthLip_upclamp_NXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_mouthLip_upclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_mouthLip_upclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_up_eyelids_dnclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_up_eyelids_dnclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_up_eyelids_lfclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_up_eyelids_lfclamp_NYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_up_eyelids_lfclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_up_eyelids_lfclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_up_eyelids_rtclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_up_eyelids_rtclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_up_eyelids_upclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_up_eyelids_upclamp_NXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_up_eyelids_upclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_Rt_up_eyelids_upclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_up_mouthLip_dnclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_up_mouthLip_dnclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_up_mouthLip_lfclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_up_mouthLip_lfclamp_NYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_up_mouthLip_lfclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_up_mouthLip_lfclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_up_mouthLip_rtclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_up_mouthLip_rtclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_up_mouthLip_upclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_up_mouthLip_upclamp_NXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_up_mouthLip_upclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "c_up_mouthLip_upclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "E_dnclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "E_dnclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "E_lfclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "E_lfclamp_NYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "E_lfclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "E_lfclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "E_rtclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "E_rtclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "E_upclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "E_upclamp_NXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "E_upclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "E_upclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "FV_dnclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "FV_dnclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "FV_lfclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "FV_lfclamp_NYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "FV_lfclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "FV_lfclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "FV_rtclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "FV_rtclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "FV_upclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "FV_upclamp_NXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "FV_upclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "FV_upclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "I_dnclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "I_dnclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "I_lfclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "I_lfclamp_NYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "I_lfclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "I_lfclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "I_rtclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "I_rtclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "I_upclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "I_upclamp_NXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "I_upclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "I_upclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "O_dnclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "O_dnclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "O_lfclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "O_lfclamp_NYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "O_lfclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "O_lfclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "O_rtclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "O_rtclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "O_upclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "O_upclamp_NXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "O_upclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "O_upclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "OU_dnclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "OU_dnclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "OU_lfclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "OU_lfclamp_NYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "OU_lfclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "OU_lfclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "OU_rtclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "OU_rtclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "OU_upclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "OU_upclamp_NXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "OU_upclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "OU_upclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "tongue_dnclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "tongue_dnclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "tongue_lfclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "tongue_lfclamp_NYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "tongue_lfclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "tongue_lfclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "tongue_rtclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "tongue_rtclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "tongue_upclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "tongue_upclamp_NXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "tongue_upclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "tongue_upclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "U_dnclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "U_dnclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "U_lfclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "U_lfclamp_NYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "U_lfclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "U_lfclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "U_rtclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "U_rtclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "U_upclamp_finalrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "U_upclamp_NXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "U_upclamp_PXrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode clamp -n "U_upclamp_PYrange";
	setAttr ".mx" -type "float3" 2 0 0 ;
createNode dagPose -n "bindPose1";
	setAttr -s 36 ".wm";
	setAttr ".wm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".wm[1]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".wm[2]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".wm[3]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".wm[4]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".wm[5]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".wm[6]" -type "matrix" 0.5 0 0 0 0 0.20000000000000001 0 0 0 0 0.40000000000000002 0
		 0 -1.2339426240365641 0 1;
	setAttr ".wm[7]" -type "matrix" 0.5 0 0 0 0 0.20000000000000001 0 0 0 0 0.40000000000000002 0
		 0 -1.2339426240365641 0 1;
	setAttr ".wm[8]" -type "matrix" 0.5 0 0 0 0 0.20000000000000001 0 0 0 0 0.40000000000000002 0
		 0 -1.2339426240365641 0 1;
	setAttr ".wm[9]" -type "matrix" 0.5 0 0 0 0 0.20000000000000001 0 0 0 0 0.40000000000000002 0
		 0 -1.2339426240365641 0 1;
	setAttr ".wm[10]" -type "matrix" 0.29999999999999999 0 0 0 0 0.15000000000000002 0 0
		 0 0 0.20000000000000001 0 0 -1.1429595961046979 0 1;
	setAttr ".wm[11]" -type "matrix" 0.29999999999999999 0 0 0 0 0.15000000000000002 0 0
		 0 0 0.20000000000000001 0 0 -1.1429595961046979 0 1;
	setAttr ".wm[12]" -type "matrix" 0.29999999999999999 0 0 0 0 0.15000000000000002 0 0
		 0 0 0.20000000000000001 0 0 -1.1429595961046979 0 1;
	setAttr ".wm[13]" -type "matrix" 0.29999999999999999 0 0 0 0 0.15000000000000002 0 0
		 0 0 0.20000000000000001 0 0 -1.1429595961046979 0 1;
	setAttr ".wm[14]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 -1.1429595961046979 0 1;
	setAttr ".wm[16]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 -1.2339426240365641 0 1;
	setAttr ".wm[18]" -type "matrix" 0.29999999999999999 0 0 0 0 0.14999999999999999 0 0
		 0 0 0.20000000000000001 0 0 -0.59815755573530272 0 1;
	setAttr ".wm[19]" -type "matrix" 0.29999999999999999 0 0 0 0 0.14999999999999999 0 0
		 0 0 0.20000000000000001 0 0 -0.59815755573530272 0 1;
	setAttr ".wm[20]" -type "matrix" 0.29999999999999999 0 0 0 0 0.14999999999999999 0 0
		 0 0 0.20000000000000001 0 0 -0.59815755573530272 0 1;
	setAttr ".wm[21]" -type "matrix" 0.29999999999999999 0 0 0 0 0.14999999999999999 0 0
		 0 0 0.20000000000000001 0 0 -0.59815755573530272 0 1;
	setAttr ".wm[22]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 -0.59815755573530272 0 1;
	setAttr ".wm[24]" -type "matrix" 0.20000000000000001 0 0 0 0 0.20000000000000001 0 0
		 0 0 0.20000000000000001 0 0.54902891329405423 -0.8433908686503121 1.2838979285600505e-016 1;
	setAttr ".wm[25]" -type "matrix" 0.20000000000000001 0 0 0 0 0.20000000000000001 0 0
		 0 0 0.20000000000000001 0 0.54902891329405423 -0.8433908686503121 1.2838979285600505e-016 1;
	setAttr ".wm[26]" -type "matrix" 0.20000000000000001 0 0 0 0 0.20000000000000001 0 0
		 0 0 0.20000000000000001 0 0.54902891329405423 -0.8433908686503121 1.2838979285600505e-016 1;
	setAttr ".wm[27]" -type "matrix" 0.20000000000000001 0 0 0 0 0.20000000000000001 0 0
		 0 0 0.20000000000000001 0 0.54902891329405423 -0.8433908686503121 1.2838979285600505e-016 1;
	setAttr ".wm[28]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0.54902891329405423 -0.8433908686503121 1.2838979285600505e-016 1;
	setAttr ".wm[30]" -type "matrix" -0.20000000000000001 0 2.4492935982947065e-017 0
		 0 0.20000000000000001 0 0 -2.4492935982947065e-017 0 -0.20000000000000001 0 -0.54902891329405423 -0.8433908686503121 -6.1153142725513633e-017 1;
	setAttr ".wm[31]" -type "matrix" -0.20000000000000001 0 2.4492935982947065e-017 0
		 0 0.20000000000000001 0 0 -2.4492935982947065e-017 0 -0.20000000000000001 0 -0.54902891329405423 -0.8433908686503121 -6.1153142725513633e-017 1;
	setAttr ".wm[32]" -type "matrix" -0.20000000000000001 0 2.4492935982947065e-017 0
		 0 0.20000000000000001 0 0 -2.4492935982947065e-017 0 -0.20000000000000001 0 -0.54902891329405423 -0.8433908686503121 -6.1153142725513633e-017 1;
	setAttr ".wm[33]" -type "matrix" -0.20000000000000001 0 2.4492935982947065e-017 0
		 0 0.20000000000000001 0 0 -2.4492935982947065e-017 0 -0.20000000000000001 0 -0.54902891329405423 -0.8433908686503121 -6.1153142725513633e-017 1;
	setAttr ".wm[34]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 -0.54902891329405423 -0.8433908686503121 6.7236650130491321e-017 1;
	setAttr -s 36 ".xm";
	setAttr ".xm[0]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[1]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[2]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[3]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0.017959868467468498 0
		 0 0 0 0 0.017959868467468498 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[4]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 -1.0192970667831824
		 0.0089799342337343845 0 0 0 0 -1.0192970667831824 0.0089799342337343845 0 0 0 0 0 0 1 
		0 0 0 1 1 1 1 yes;
	setAttr ".xm[5]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 -0.94213755006190936
		 0.017959868467468769 0 0 0 0 -0.94213755006190936 0.017959868467468769 0 0 0 0 0 0 1 
		0 0 0 1 1 1 1 yes;
	setAttr ".xm[6]" -type "matrix" "xform" 0.5 0.20000000000000001 0.40000000000000002 0
		 0 0 0 0 -1.2339426240365641 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1
		 1 1 yes;
	setAttr ".xm[7]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[8]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[9]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[10]" -type "matrix" "xform" 0.59999999999999998 0.75 0.5 0 0 0 0 0
		 0.45491513965933095 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[11]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[12]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[13]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[14]" -type "matrix" "xform" 3.3333333333333335 6.6666666666666661 5 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[15]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[16]" -type "matrix" "xform" 2 5 2.5 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[17]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[18]" -type "matrix" "xform" 0.29999999999999999 0.14999999999999999
		 0.20000000000000001 0 0 0 0 0 -0.59815755573530272 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[19]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[20]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[21]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[22]" -type "matrix" "xform" 3.3333333333333335 6.666666666666667 5 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[23]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[24]" -type "matrix" "xform" 0.20000000000000001 0.20000000000000001
		 0.20000000000000001 0 0 0 0 0.54902891329405423 -0.8433908686503121 1.2838979285600505e-016 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[25]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[26]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[27]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[28]" -type "matrix" "xform" 5 5 5 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[29]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[30]" -type "matrix" "xform" 0.20000000000000001 0.20000000000000001
		 0.20000000000000001 0 -3.1415926535897931 0 0 -0.54902891329405423 -0.8433908686503121
		 -6.1153142725513633e-017 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[31]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[32]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[33]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[34]" -type "matrix" "xform" 5 5 5 0 3.1415926535897931 0 0 0 0
		 -6.4194896428002469e-016 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[35]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr -s 36 ".m";
	setAttr -s 36 ".p";
	setAttr -s 36 ".g[0:35]" yes yes yes yes yes yes yes yes yes yes yes 
		yes yes yes yes no yes no yes yes yes yes yes no yes yes yes yes yes no yes yes yes 
		yes yes no;
	setAttr ".bp" yes;
createNode displayLayer -n "defaultLayer";
createNode displayLayerManager -n "layerManager";
createNode expression -n "c_tongue_CTRL_ex";
	setAttr -k on ".nds";
	setAttr -s 12 ".in";
	setAttr -s 12 ".in";
	setAttr -s 6 ".out";
	setAttr ".ixp" -type "string" "//c_tongue_CTRL_ex\n.O[0]=.I[0]*.I[1];\n.O[1]=.I[2]*.I[3];\n.O[2]=.I[4]*.I[5];\n.O[3]=.I[6]*.I[7];\n.O[4]=.I[8]*.I[9];\n.O[5]=.I[10]*.I[11];";
createNode lightLinker -s -n "lightLinker1";
	setAttr -s 2 ".lnk";
	setAttr -s 2 ".slnk";
createNode makeTextCurves -n "makeTextCurves10";
	setAttr ".t" -type "string" "Tongue";
	setAttr ".f" -type "string" "Times New Roman|h-13|w400|c0";
	setAttr -s 6 ".p";
createNode makeTextCurves -n "makeTextCurves22";
	setAttr ".t" -type "string" "a";
	setAttr ".f" -type "string" "Times New Roman|h-13|w400|c0";
createNode makeTextCurves -n "makeTextCurves23";
	setAttr ".t" -type "string" "u/o";
	setAttr ".f" -type "string" "Times New Roman|h-13|w400|c0";
createNode makeTextCurves -n "makeTextCurves24";
	setAttr ".t" -type "string" "f/v";
	setAttr ".f" -type "string" "Times New Roman|h-13|w400|c0";
	setAttr -s 3 ".p";
createNode makeTextCurves -n "makeTextCurves25";
	setAttr ".t" -type "string" "the";
	setAttr ".f" -type "string" "Times New Roman|h-13|w400|c0";
	setAttr -s 3 ".p";
createNode makeTextCurves -n "makeTextCurves26";
	setAttr ".t" -type "string" "eee/s/z";
	setAttr ".f" -type "string" "Times New Roman|h-13|w400|c0";
	setAttr -s 7 ".p";
createNode makeTextCurves -n "makeTextCurves27";
	setAttr ".t" -type "string" "m/b/p";
	setAttr ".f" -type "string" "Times New Roman|h-13|w400|c0";
	setAttr -s 5 ".p";
createNode makeTextCurves -n "makeTextCurves49";
	setAttr ".t" -type "string" "/";
	setAttr ".f" -type "string" "Times New Roman|h-13|w400|c0";
createNode makeTextCurves -n "makeTextCurves50";
	setAttr ".t" -type "string" "L";
	setAttr ".f" -type "string" "Times New Roman|h-13|w400|c0";
createNode makeTextCurves -n "makeTextCurves9";
	setAttr ".t" -type "string" "OU";
	setAttr ".f" -type "string" "Times New Roman|h-13|w400|c0";
createNode multiplyDivide -n "A_dnmult_Yinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "A_dnScale";
createNode multiplyDivide -n "A_lfdnmult";
createNode multiplyDivide -n "A_lfmult_Xinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "A_lfmult_Yinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "A_lfScale";
createNode multiplyDivide -n "A_lfupmult";
createNode multiplyDivide -n "A_rtdnmult";
createNode multiplyDivide -n "A_rtScale";
createNode multiplyDivide -n "A_rtupmult";
createNode multiplyDivide -n "A_upmult_Xinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "A_upScale";
createNode multiplyDivide -n "c_dn_mouthLip_dnmult_Yinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_dn_mouthLip_dnScale";
createNode multiplyDivide -n "c_dn_mouthLip_lfdnmult";
createNode multiplyDivide -n "c_dn_mouthLip_lfmult_Xinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_dn_mouthLip_lfmult_Yinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_dn_mouthLip_lfScale";
createNode multiplyDivide -n "c_dn_mouthLip_lfupmult";
createNode multiplyDivide -n "c_dn_mouthLip_rtdnmult";
createNode multiplyDivide -n "c_dn_mouthLip_rtScale";
createNode multiplyDivide -n "c_dn_mouthLip_rtupmult";
createNode multiplyDivide -n "c_dn_mouthLip_upmult_Xinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_dn_mouthLip_upScale";
createNode multiplyDivide -n "c_jaw_dn_dnmult_Yinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_jaw_dn_dnScale";
createNode multiplyDivide -n "c_jaw_dn_lfdnmult";
createNode multiplyDivide -n "c_jaw_dn_lfmult_Xinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_jaw_dn_lfmult_Yinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_jaw_dn_lfScale";
createNode multiplyDivide -n "c_jaw_dn_lfupmult";
createNode multiplyDivide -n "c_jaw_dn_rtdnmult";
createNode multiplyDivide -n "c_jaw_dn_rtScale";
createNode multiplyDivide -n "c_jaw_dn_rtupmult";
createNode multiplyDivide -n "c_jaw_dn_upmult_Xinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_jaw_dn_upScale";
createNode multiplyDivide -n "c_jaw_up_dnmult_Yinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_jaw_up_dnScale";
createNode multiplyDivide -n "c_jaw_up_lfdnmult";
createNode multiplyDivide -n "c_jaw_up_lfmult_Xinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_jaw_up_lfmult_Yinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_jaw_up_lfScale";
createNode multiplyDivide -n "c_jaw_up_lfupmult";
createNode multiplyDivide -n "c_jaw_up_rtdnmult";
createNode multiplyDivide -n "c_jaw_up_rtScale";
createNode multiplyDivide -n "c_jaw_up_rtupmult";
createNode multiplyDivide -n "c_jaw_up_upmult_Xinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_jaw_up_upScale";
createNode multiplyDivide -n "c_Lf_dn_eyelids_dnmult_Yinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_Lf_dn_eyelids_dnScale";
createNode multiplyDivide -n "c_Lf_dn_eyelids_lfdnmult";
createNode multiplyDivide -n "c_Lf_dn_eyelids_lfmult_Xinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_Lf_dn_eyelids_lfmult_Yinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_Lf_dn_eyelids_lfScale";
createNode multiplyDivide -n "c_Lf_dn_eyelids_lfupmult";
createNode multiplyDivide -n "c_Lf_dn_eyelids_rtdnmult";
createNode multiplyDivide -n "c_Lf_dn_eyelids_rtScale";
createNode multiplyDivide -n "c_Lf_dn_eyelids_rtupmult";
createNode multiplyDivide -n "c_Lf_dn_eyelids_upmult_Xinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_Lf_dn_eyelids_upScale";
createNode multiplyDivide -n "c_Lf_eyebrows_01_dnmult_Yinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_Lf_eyebrows_01_dnScale";
createNode multiplyDivide -n "c_Lf_eyebrows_01_lfdnmult";
createNode multiplyDivide -n "c_Lf_eyebrows_01_lfmult_Xinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_Lf_eyebrows_01_lfmult_Yinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_Lf_eyebrows_01_lfScale";
createNode multiplyDivide -n "c_Lf_eyebrows_01_lfupmult";
createNode multiplyDivide -n "c_Lf_eyebrows_01_rtdnmult";
createNode multiplyDivide -n "c_Lf_eyebrows_01_rtScale";
createNode multiplyDivide -n "c_Lf_eyebrows_01_rtupmult";
createNode multiplyDivide -n "c_Lf_eyebrows_01_upmult_Xinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_Lf_eyebrows_01_upScale";
createNode multiplyDivide -n "c_Lf_eyebrows_02_dnmult_Yinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_Lf_eyebrows_02_dnScale";
createNode multiplyDivide -n "c_Lf_eyebrows_02_lfdnmult";
createNode multiplyDivide -n "c_Lf_eyebrows_02_lfmult_Xinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_Lf_eyebrows_02_lfmult_Yinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_Lf_eyebrows_02_lfScale";
createNode multiplyDivide -n "c_Lf_eyebrows_02_lfupmult";
createNode multiplyDivide -n "c_Lf_eyebrows_02_rtdnmult";
createNode multiplyDivide -n "c_Lf_eyebrows_02_rtScale";
createNode multiplyDivide -n "c_Lf_eyebrows_02_rtupmult";
createNode multiplyDivide -n "c_Lf_eyebrows_02_upmult_Xinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_Lf_eyebrows_02_upScale";
createNode multiplyDivide -n "c_Lf_eyebrows_03_dnmult_Yinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_Lf_eyebrows_03_dnScale";
createNode multiplyDivide -n "c_Lf_eyebrows_03_lfdnmult";
createNode multiplyDivide -n "c_Lf_eyebrows_03_lfmult_Xinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_Lf_eyebrows_03_lfmult_Yinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_Lf_eyebrows_03_lfScale";
createNode multiplyDivide -n "c_Lf_eyebrows_03_lfupmult";
createNode multiplyDivide -n "c_Lf_eyebrows_03_rtdnmult";
createNode multiplyDivide -n "c_Lf_eyebrows_03_rtScale";
createNode multiplyDivide -n "c_Lf_eyebrows_03_rtupmult";
createNode multiplyDivide -n "c_Lf_eyebrows_03_upmult_Xinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_Lf_eyebrows_03_upScale";
createNode multiplyDivide -n "c_Lf_eyeStretch_dnmult_Yinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_Lf_eyeStretch_dnScale";
createNode multiplyDivide -n "c_Lf_eyeStretch_lfdnmult";
createNode multiplyDivide -n "c_Lf_eyeStretch_lfmult_Xinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_Lf_eyeStretch_lfmult_Yinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_Lf_eyeStretch_lfScale";
createNode multiplyDivide -n "c_Lf_eyeStretch_lfupmult";
createNode multiplyDivide -n "c_Lf_eyeStretch_rtdnmult";
createNode multiplyDivide -n "c_Lf_eyeStretch_rtScale";
createNode multiplyDivide -n "c_Lf_eyeStretch_rtupmult";
createNode multiplyDivide -n "c_Lf_eyeStretch_upmult_Xinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_Lf_eyeStretch_upScale";
createNode multiplyDivide -n "c_Lf_mouthLip_dnmult_Yinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_Lf_mouthLip_dnScale";
createNode multiplyDivide -n "c_Lf_mouthLip_lfdnmult";
createNode multiplyDivide -n "c_Lf_mouthLip_lfmult_Xinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_Lf_mouthLip_lfmult_Yinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_Lf_mouthLip_lfScale";
createNode multiplyDivide -n "c_Lf_mouthLip_lfupmult";
createNode multiplyDivide -n "c_Lf_mouthLip_rtdnmult";
createNode multiplyDivide -n "c_Lf_mouthLip_rtScale";
createNode multiplyDivide -n "c_Lf_mouthLip_rtupmult";
createNode multiplyDivide -n "c_Lf_mouthLip_upmult_Xinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_Lf_mouthLip_upScale";
createNode multiplyDivide -n "c_Lf_up_eyelids_dnmult_Yinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_Lf_up_eyelids_dnScale";
createNode multiplyDivide -n "c_Lf_up_eyelids_lfdnmult";
createNode multiplyDivide -n "c_Lf_up_eyelids_lfmult_Xinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_Lf_up_eyelids_lfmult_Yinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_Lf_up_eyelids_lfScale";
createNode multiplyDivide -n "c_Lf_up_eyelids_lfupmult";
createNode multiplyDivide -n "c_Lf_up_eyelids_rtdnmult";
createNode multiplyDivide -n "c_Lf_up_eyelids_rtScale";
createNode multiplyDivide -n "c_Lf_up_eyelids_rtupmult";
createNode multiplyDivide -n "c_Lf_up_eyelids_upmult_Xinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_Lf_up_eyelids_upScale";
createNode multiplyDivide -n "c_nose_dnmult_Yinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_nose_dnScale";
createNode multiplyDivide -n "c_nose_lfdnmult";
createNode multiplyDivide -n "c_nose_lfmult_Xinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_nose_lfmult_Yinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_nose_lfScale";
createNode multiplyDivide -n "c_nose_lfupmult";
createNode multiplyDivide -n "c_nose_rtdnmult";
createNode multiplyDivide -n "c_nose_rtScale";
createNode multiplyDivide -n "c_nose_rtupmult";
createNode multiplyDivide -n "c_nose_upmult_Xinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_nose_upScale";
createNode multiplyDivide -n "c_Rt_dn_eyelids_dnmult_Yinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_Rt_dn_eyelids_dnScale";
createNode multiplyDivide -n "c_Rt_dn_eyelids_lfdnmult";
createNode multiplyDivide -n "c_Rt_dn_eyelids_lfmult_Xinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_Rt_dn_eyelids_lfmult_Yinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_Rt_dn_eyelids_lfScale";
createNode multiplyDivide -n "c_Rt_dn_eyelids_lfupmult";
createNode multiplyDivide -n "c_Rt_dn_eyelids_rtdnmult";
createNode multiplyDivide -n "c_Rt_dn_eyelids_rtScale";
createNode multiplyDivide -n "c_Rt_dn_eyelids_rtupmult";
createNode multiplyDivide -n "c_Rt_dn_eyelids_upmult_Xinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_Rt_dn_eyelids_upScale";
createNode multiplyDivide -n "c_Rt_eyebrows_01_dnmult_Yinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_Rt_eyebrows_01_dnScale";
createNode multiplyDivide -n "c_Rt_eyebrows_01_lfdnmult";
createNode multiplyDivide -n "c_Rt_eyebrows_01_lfmult_Xinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_Rt_eyebrows_01_lfmult_Yinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_Rt_eyebrows_01_lfScale";
createNode multiplyDivide -n "c_Rt_eyebrows_01_lfupmult";
createNode multiplyDivide -n "c_Rt_eyebrows_01_rtdnmult";
createNode multiplyDivide -n "c_Rt_eyebrows_01_rtScale";
createNode multiplyDivide -n "c_Rt_eyebrows_01_rtupmult";
createNode multiplyDivide -n "c_Rt_eyebrows_01_upmult_Xinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_Rt_eyebrows_01_upScale";
createNode multiplyDivide -n "c_Rt_eyebrows_02_dnmult_Yinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_Rt_eyebrows_02_dnScale";
createNode multiplyDivide -n "c_Rt_eyebrows_02_lfdnmult";
createNode multiplyDivide -n "c_Rt_eyebrows_02_lfmult_Xinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_Rt_eyebrows_02_lfmult_Yinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_Rt_eyebrows_02_lfScale";
createNode multiplyDivide -n "c_Rt_eyebrows_02_lfupmult";
createNode multiplyDivide -n "c_Rt_eyebrows_02_rtdnmult";
createNode multiplyDivide -n "c_Rt_eyebrows_02_rtScale";
createNode multiplyDivide -n "c_Rt_eyebrows_02_rtupmult";
createNode multiplyDivide -n "c_Rt_eyebrows_02_upmult_Xinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_Rt_eyebrows_02_upScale";
createNode multiplyDivide -n "c_Rt_eyebrows_03_dnmult_Yinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_Rt_eyebrows_03_dnScale";
createNode multiplyDivide -n "c_Rt_eyebrows_03_lfdnmult";
createNode multiplyDivide -n "c_Rt_eyebrows_03_lfmult_Xinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_Rt_eyebrows_03_lfmult_Yinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_Rt_eyebrows_03_lfScale";
createNode multiplyDivide -n "c_Rt_eyebrows_03_lfupmult";
createNode multiplyDivide -n "c_Rt_eyebrows_03_rtdnmult";
createNode multiplyDivide -n "c_Rt_eyebrows_03_rtScale";
createNode multiplyDivide -n "c_Rt_eyebrows_03_rtupmult";
createNode multiplyDivide -n "c_Rt_eyebrows_03_upmult_Xinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_Rt_eyebrows_03_upScale";
createNode multiplyDivide -n "c_Rt_eyeStretch_dnmult_Yinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_Rt_eyeStretch_dnScale";
createNode multiplyDivide -n "c_Rt_eyeStretch_lfdnmult";
createNode multiplyDivide -n "c_Rt_eyeStretch_lfmult_Xinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_Rt_eyeStretch_lfmult_Yinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_Rt_eyeStretch_lfScale";
createNode multiplyDivide -n "c_Rt_eyeStretch_lfupmult";
createNode multiplyDivide -n "c_Rt_eyeStretch_rtdnmult";
createNode multiplyDivide -n "c_Rt_eyeStretch_rtScale";
createNode multiplyDivide -n "c_Rt_eyeStretch_rtupmult";
createNode multiplyDivide -n "c_Rt_eyeStretch_upmult_Xinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_Rt_eyeStretch_upScale";
createNode multiplyDivide -n "c_Rt_mouthLip_dnmult_Yinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_Rt_mouthLip_dnScale";
createNode multiplyDivide -n "c_Rt_mouthLip_lfdnmult";
createNode multiplyDivide -n "c_Rt_mouthLip_lfmult_Xinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_Rt_mouthLip_lfmult_Yinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_Rt_mouthLip_lfScale";
createNode multiplyDivide -n "c_Rt_mouthLip_lfupmult";
createNode multiplyDivide -n "c_Rt_mouthLip_rtdnmult";
createNode multiplyDivide -n "c_Rt_mouthLip_rtScale";
createNode multiplyDivide -n "c_Rt_mouthLip_rtupmult";
createNode multiplyDivide -n "c_Rt_mouthLip_upmult_Xinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_Rt_mouthLip_upScale";
createNode multiplyDivide -n "c_Rt_up_eyelids_dnmult_Yinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_Rt_up_eyelids_dnScale";
createNode multiplyDivide -n "c_Rt_up_eyelids_lfdnmult";
createNode multiplyDivide -n "c_Rt_up_eyelids_lfmult_Xinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_Rt_up_eyelids_lfmult_Yinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_Rt_up_eyelids_lfScale";
createNode multiplyDivide -n "c_Rt_up_eyelids_lfupmult";
createNode multiplyDivide -n "c_Rt_up_eyelids_rtdnmult";
createNode multiplyDivide -n "c_Rt_up_eyelids_rtScale";
createNode multiplyDivide -n "c_Rt_up_eyelids_rtupmult";
createNode multiplyDivide -n "c_Rt_up_eyelids_upmult_Xinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_Rt_up_eyelids_upScale";
createNode multiplyDivide -n "c_up_mouthLip_dnmult_Yinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_up_mouthLip_dnScale";
createNode multiplyDivide -n "c_up_mouthLip_lfdnmult";
createNode multiplyDivide -n "c_up_mouthLip_lfmult_Xinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_up_mouthLip_lfmult_Yinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_up_mouthLip_lfScale";
createNode multiplyDivide -n "c_up_mouthLip_lfupmult";
createNode multiplyDivide -n "c_up_mouthLip_rtdnmult";
createNode multiplyDivide -n "c_up_mouthLip_rtScale";
createNode multiplyDivide -n "c_up_mouthLip_rtupmult";
createNode multiplyDivide -n "c_up_mouthLip_upmult_Xinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "c_up_mouthLip_upScale";
createNode multiplyDivide -n "E_dnmult_Yinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "E_dnScale";
createNode multiplyDivide -n "E_lfdnmult";
createNode multiplyDivide -n "E_lfmult_Xinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "E_lfmult_Yinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "E_lfScale";
createNode multiplyDivide -n "E_lfupmult";
createNode multiplyDivide -n "E_rtdnmult";
createNode multiplyDivide -n "E_rtScale";
createNode multiplyDivide -n "E_rtupmult";
createNode multiplyDivide -n "E_upmult_Xinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "E_upScale";
createNode multiplyDivide -n "FV_dnmult_Yinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "FV_dnScale";
createNode multiplyDivide -n "FV_lfdnmult";
createNode multiplyDivide -n "FV_lfmult_Xinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "FV_lfmult_Yinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "FV_lfScale";
createNode multiplyDivide -n "FV_lfupmult";
createNode multiplyDivide -n "FV_rtdnmult";
createNode multiplyDivide -n "FV_rtScale";
createNode multiplyDivide -n "FV_rtupmult";
createNode multiplyDivide -n "FV_upmult_Xinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "FV_upScale";
createNode multiplyDivide -n "I_dnmult_Yinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "I_dnScale";
createNode multiplyDivide -n "I_lfdnmult";
createNode multiplyDivide -n "I_lfmult_Xinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "I_lfmult_Yinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "I_lfScale";
createNode multiplyDivide -n "I_lfupmult";
createNode multiplyDivide -n "I_rtdnmult";
createNode multiplyDivide -n "I_rtScale";
createNode multiplyDivide -n "I_rtupmult";
createNode multiplyDivide -n "I_upmult_Xinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "I_upScale";
createNode multiplyDivide -n "O_dnmult_Yinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "O_dnScale";
createNode multiplyDivide -n "O_lfdnmult";
createNode multiplyDivide -n "O_lfmult_Xinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "O_lfmult_Yinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "O_lfScale";
createNode multiplyDivide -n "O_lfupmult";
createNode multiplyDivide -n "O_rtdnmult";
createNode multiplyDivide -n "O_rtScale";
createNode multiplyDivide -n "O_rtupmult";
createNode multiplyDivide -n "O_upmult_Xinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "O_upScale";
createNode multiplyDivide -n "OU_dnmult_Yinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "OU_dnScale";
createNode multiplyDivide -n "OU_lfdnmult";
createNode multiplyDivide -n "OU_lfmult_Xinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "OU_lfmult_Yinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "OU_lfScale";
createNode multiplyDivide -n "OU_lfupmult";
createNode multiplyDivide -n "OU_rtdnmult";
createNode multiplyDivide -n "OU_rtScale";
createNode multiplyDivide -n "OU_rtupmult";
createNode multiplyDivide -n "OU_upmult_Xinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "OU_upScale";
createNode multiplyDivide -n "tongue_dnmult_Yinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "tongue_dnScale";
createNode multiplyDivide -n "tongue_lfdnmult";
createNode multiplyDivide -n "tongue_lfmult_Xinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "tongue_lfmult_Yinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "tongue_lfScale";
createNode multiplyDivide -n "tongue_lfupmult";
createNode multiplyDivide -n "tongue_rtdnmult";
createNode multiplyDivide -n "tongue_rtScale";
createNode multiplyDivide -n "tongue_rtupmult";
createNode multiplyDivide -n "tongue_upmult_Xinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "tongue_upScale";
createNode multiplyDivide -n "U_dnmult_Yinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "U_dnScale";
createNode multiplyDivide -n "U_lfdnmult";
createNode multiplyDivide -n "U_lfmult_Xinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "U_lfmult_Yinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "U_lfScale";
createNode multiplyDivide -n "U_lfupmult";
createNode multiplyDivide -n "U_rtdnmult";
createNode multiplyDivide -n "U_rtScale";
createNode multiplyDivide -n "U_rtupmult";
createNode multiplyDivide -n "U_upmult_Xinverse";
	setAttr ".i1" -type "float3" -1 0 0 ;
createNode multiplyDivide -n "U_upScale";
createNode plusMinusAverage -n "A_lfplus_Yplus";
	setAttr -s 2 ".i1";
	setAttr -s 2 ".i1";
createNode plusMinusAverage -n "A_upplus_Xplus";
	setAttr -s 2 ".i1";
	setAttr -s 2 ".i1";
createNode plusMinusAverage -n "c_dn_mouthLip_lfplus_Yplus";
	setAttr -s 2 ".i1";
	setAttr -s 2 ".i1";
createNode plusMinusAverage -n "c_dn_mouthLip_upplus_Xplus";
	setAttr -s 2 ".i1";
	setAttr -s 2 ".i1";
createNode plusMinusAverage -n "c_jaw_dn_lfplus_Yplus";
	setAttr -s 2 ".i1";
	setAttr -s 2 ".i1";
createNode plusMinusAverage -n "c_jaw_dn_upplus_Xplus";
	setAttr -s 2 ".i1";
	setAttr -s 2 ".i1";
createNode plusMinusAverage -n "c_jaw_up_lfplus_Yplus";
	setAttr -s 2 ".i1";
	setAttr -s 2 ".i1";
createNode plusMinusAverage -n "c_jaw_up_upplus_Xplus";
	setAttr -s 2 ".i1";
	setAttr -s 2 ".i1";
createNode plusMinusAverage -n "c_Lf_dn_eyelids_lfplus_Yplus";
	setAttr -s 2 ".i1";
	setAttr -s 2 ".i1";
createNode plusMinusAverage -n "c_Lf_dn_eyelids_upplus_Xplus";
	setAttr -s 2 ".i1";
	setAttr -s 2 ".i1";
createNode plusMinusAverage -n "c_Lf_eyebrows_01_lfplus_Yplus";
	setAttr -s 2 ".i1";
	setAttr -s 2 ".i1";
createNode plusMinusAverage -n "c_Lf_eyebrows_01_plus";
	setAttr -s 2 ".i1[0:1]"  0 0;
	setAttr -s 2 ".i3";
	setAttr -s 2 ".i3";
createNode plusMinusAverage -n "c_Lf_eyebrows_01_upplus_Xplus";
	setAttr -s 2 ".i1";
	setAttr -s 2 ".i1";
createNode plusMinusAverage -n "c_Lf_eyebrows_02_lfplus_Yplus";
	setAttr -s 2 ".i1";
	setAttr -s 2 ".i1";
createNode plusMinusAverage -n "c_Lf_eyebrows_02_plus";
	setAttr -s 2 ".i1[0:1]"  0 0;
	setAttr -s 2 ".i3";
	setAttr -s 2 ".i3";
createNode plusMinusAverage -n "c_Lf_eyebrows_02_upplus_Xplus";
	setAttr -s 2 ".i1";
	setAttr -s 2 ".i1";
createNode plusMinusAverage -n "c_Lf_eyebrows_03_lfplus_Yplus";
	setAttr -s 2 ".i1";
	setAttr -s 2 ".i1";
createNode plusMinusAverage -n "c_Lf_eyebrows_03_plus";
	setAttr -s 2 ".i1[0:1]"  0 0;
	setAttr -s 2 ".i3";
	setAttr -s 2 ".i3";
createNode plusMinusAverage -n "c_Lf_eyebrows_03_upplus_Xplus";
	setAttr -s 2 ".i1";
	setAttr -s 2 ".i1";
createNode plusMinusAverage -n "c_Lf_eyeStretch_lfplus_Yplus";
	setAttr -s 2 ".i1";
	setAttr -s 2 ".i1";
createNode plusMinusAverage -n "c_Lf_eyeStretch_upplus_Xplus";
	setAttr -s 2 ".i1";
	setAttr -s 2 ".i1";
createNode plusMinusAverage -n "c_Lf_mouthLip_lfplus_Yplus";
	setAttr -s 2 ".i1";
	setAttr -s 2 ".i1";
createNode plusMinusAverage -n "c_Lf_mouthLip_upplus_Xplus";
	setAttr -s 2 ".i1";
	setAttr -s 2 ".i1";
createNode plusMinusAverage -n "c_Lf_up_eyelids_lfplus_Yplus";
	setAttr -s 2 ".i1";
	setAttr -s 2 ".i1";
createNode plusMinusAverage -n "c_Lf_up_eyelids_upplus_Xplus";
	setAttr -s 2 ".i1";
	setAttr -s 2 ".i1";
createNode plusMinusAverage -n "c_nose_lfplus_Yplus";
	setAttr -s 2 ".i1";
	setAttr -s 2 ".i1";
createNode plusMinusAverage -n "c_nose_upplus_Xplus";
	setAttr -s 2 ".i1";
	setAttr -s 2 ".i1";
createNode plusMinusAverage -n "c_Rt_dn_eyelids_lfplus_Yplus";
	setAttr -s 2 ".i1";
	setAttr -s 2 ".i1";
createNode plusMinusAverage -n "c_Rt_dn_eyelids_upplus_Xplus";
	setAttr -s 2 ".i1";
	setAttr -s 2 ".i1";
createNode plusMinusAverage -n "c_Rt_eyebrows_01_lfplus_Yplus";
	setAttr -s 2 ".i1";
	setAttr -s 2 ".i1";
createNode plusMinusAverage -n "c_Rt_eyebrows_01_plus";
	setAttr -s 2 ".i1[0:1]"  0 0;
	setAttr -s 2 ".i3";
	setAttr -s 2 ".i3";
createNode plusMinusAverage -n "c_Rt_eyebrows_01_upplus_Xplus";
	setAttr -s 2 ".i1";
	setAttr -s 2 ".i1";
createNode plusMinusAverage -n "c_Rt_eyebrows_02_lfplus_Yplus";
	setAttr -s 2 ".i1";
	setAttr -s 2 ".i1";
createNode plusMinusAverage -n "c_Rt_eyebrows_02_plus";
	setAttr -s 2 ".i1[0:1]"  0 0;
	setAttr -s 2 ".i3";
	setAttr -s 2 ".i3";
createNode plusMinusAverage -n "c_Rt_eyebrows_02_upplus_Xplus";
	setAttr -s 2 ".i1";
	setAttr -s 2 ".i1";
createNode plusMinusAverage -n "c_Rt_eyebrows_03_lfplus_Yplus";
	setAttr -s 2 ".i1";
	setAttr -s 2 ".i1";
createNode plusMinusAverage -n "c_Rt_eyebrows_03_plus";
	setAttr -s 2 ".i1[0:1]"  0 0;
	setAttr -s 2 ".i3";
	setAttr -s 2 ".i3";
createNode plusMinusAverage -n "c_Rt_eyebrows_03_upplus_Xplus";
	setAttr -s 2 ".i1";
	setAttr -s 2 ".i1";
createNode plusMinusAverage -n "c_Rt_eyeStretch_lfplus_Yplus";
	setAttr -s 2 ".i1";
	setAttr -s 2 ".i1";
createNode plusMinusAverage -n "c_Rt_eyeStretch_upplus_Xplus";
	setAttr -s 2 ".i1";
	setAttr -s 2 ".i1";
createNode plusMinusAverage -n "c_Rt_mouthLip_lfplus_Yplus";
	setAttr -s 2 ".i1";
	setAttr -s 2 ".i1";
createNode plusMinusAverage -n "c_Rt_mouthLip_upplus_Xplus";
	setAttr -s 2 ".i1";
	setAttr -s 2 ".i1";
createNode plusMinusAverage -n "c_Rt_up_eyelids_lfplus_Yplus";
	setAttr -s 2 ".i1";
	setAttr -s 2 ".i1";
createNode plusMinusAverage -n "c_Rt_up_eyelids_upplus_Xplus";
	setAttr -s 2 ".i1";
	setAttr -s 2 ".i1";
createNode plusMinusAverage -n "c_up_mouthLip_lfplus_Yplus";
	setAttr -s 2 ".i1";
	setAttr -s 2 ".i1";
createNode plusMinusAverage -n "c_up_mouthLip_upplus_Xplus";
	setAttr -s 2 ".i1";
	setAttr -s 2 ".i1";
createNode plusMinusAverage -n "E_lfplus_Yplus";
	setAttr -s 2 ".i1";
	setAttr -s 2 ".i1";
createNode plusMinusAverage -n "E_upplus_Xplus";
	setAttr -s 2 ".i1";
	setAttr -s 2 ".i1";
createNode plusMinusAverage -n "FV_lfplus_Yplus";
	setAttr -s 2 ".i1";
	setAttr -s 2 ".i1";
createNode plusMinusAverage -n "FV_upplus_Xplus";
	setAttr -s 2 ".i1";
	setAttr -s 2 ".i1";
createNode plusMinusAverage -n "I_lfplus_Yplus";
	setAttr -s 2 ".i1";
	setAttr -s 2 ".i1";
createNode plusMinusAverage -n "I_upplus_Xplus";
	setAttr -s 2 ".i1";
	setAttr -s 2 ".i1";
createNode plusMinusAverage -n "O_lfplus_Yplus";
	setAttr -s 2 ".i1";
	setAttr -s 2 ".i1";
createNode plusMinusAverage -n "O_upplus_Xplus";
	setAttr -s 2 ".i1";
	setAttr -s 2 ".i1";
createNode plusMinusAverage -n "OU_lfplus_Yplus";
	setAttr -s 2 ".i1";
	setAttr -s 2 ".i1";
createNode plusMinusAverage -n "OU_upplus_Xplus";
	setAttr -s 2 ".i1";
	setAttr -s 2 ".i1";
createNode plusMinusAverage -n "tongue_lfplus_Yplus";
	setAttr -s 2 ".i1";
	setAttr -s 2 ".i1";
createNode plusMinusAverage -n "tongue_upplus_Xplus";
	setAttr -s 2 ".i1";
	setAttr -s 2 ".i1";
createNode plusMinusAverage -n "U_lfplus_Yplus";
	setAttr -s 2 ".i1";
	setAttr -s 2 ".i1";
createNode plusMinusAverage -n "U_upplus_Xplus";
	setAttr -s 2 ".i1";
	setAttr -s 2 ".i1";
createNode renderLayer -n "defaultRenderLayer";
	setAttr ".g" yes;
createNode reverse -n "A_lfreverse_Y";
createNode reverse -n "A_upreverse_X";
createNode reverse -n "c_dn_mouthLip_lfreverse_Y";
createNode reverse -n "c_dn_mouthLip_upreverse_X";
createNode reverse -n "c_jaw_dn_lfreverse_Y";
createNode reverse -n "c_jaw_dn_upreverse_X";
createNode reverse -n "c_jaw_up_lfreverse_Y";
createNode reverse -n "c_jaw_up_upreverse_X";
createNode reverse -n "c_Lf_dn_eyelids_lfreverse_Y";
createNode reverse -n "c_Lf_dn_eyelids_upreverse_X";
createNode reverse -n "c_Lf_eyebrows_01_lfreverse_Y";
createNode reverse -n "c_Lf_eyebrows_01_upreverse_X";
createNode reverse -n "c_Lf_eyebrows_02_lfreverse_Y";
createNode reverse -n "c_Lf_eyebrows_02_upreverse_X";
createNode reverse -n "c_Lf_eyebrows_03_lfreverse_Y";
createNode reverse -n "c_Lf_eyebrows_03_upreverse_X";
createNode reverse -n "c_Lf_eyeStretch_lfreverse_Y";
createNode reverse -n "c_Lf_eyeStretch_upreverse_X";
createNode reverse -n "c_Lf_mouthLip_lfreverse_Y";
createNode reverse -n "c_Lf_mouthLip_upreverse_X";
createNode reverse -n "c_Lf_up_eyelids_lfreverse_Y";
createNode reverse -n "c_Lf_up_eyelids_upreverse_X";
createNode reverse -n "c_nose_lfreverse_Y";
createNode reverse -n "c_nose_upreverse_X";
createNode reverse -n "c_Rt_dn_eyelids_lfreverse_Y";
createNode reverse -n "c_Rt_dn_eyelids_upreverse_X";
createNode reverse -n "c_Rt_eyebrows_01_lfreverse_Y";
createNode reverse -n "c_Rt_eyebrows_01_upreverse_X";
createNode reverse -n "c_Rt_eyebrows_02_lfreverse_Y";
createNode reverse -n "c_Rt_eyebrows_02_upreverse_X";
createNode reverse -n "c_Rt_eyebrows_03_lfreverse_Y";
createNode reverse -n "c_Rt_eyebrows_03_upreverse_X";
createNode reverse -n "c_Rt_eyeStretch_lfreverse_Y";
createNode reverse -n "c_Rt_eyeStretch_upreverse_X";
createNode reverse -n "c_Rt_mouthLip_lfreverse_Y";
createNode reverse -n "c_Rt_mouthLip_upreverse_X";
createNode reverse -n "c_Rt_up_eyelids_lfreverse_Y";
createNode reverse -n "c_Rt_up_eyelids_upreverse_X";
createNode reverse -n "c_up_mouthLip_lfreverse_Y";
createNode reverse -n "c_up_mouthLip_upreverse_X";
createNode reverse -n "E_lfreverse_Y";
createNode reverse -n "E_upreverse_X";
createNode reverse -n "FV_lfreverse_Y";
createNode reverse -n "FV_upreverse_X";
createNode reverse -n "I_lfreverse_Y";
createNode reverse -n "I_upreverse_X";
createNode reverse -n "O_lfreverse_Y";
createNode reverse -n "O_upreverse_X";
createNode reverse -n "OU_lfreverse_Y";
createNode reverse -n "OU_upreverse_X";
createNode reverse -n "tongue_lfreverse_Y";
createNode reverse -n "tongue_upreverse_X";
createNode reverse -n "U_lfreverse_Y";
createNode reverse -n "U_upreverse_X";
createNode script -n "sceneConfigurationScriptNode";
	setAttr ".b" -type "string" "playbackOptions -min 1 -max 24 -ast 1 -aet 48 ";
	setAttr ".st" 6;
createNode script -n "uiConfigurationScriptNode";
	setAttr ".b" -type "string" (
		"// Maya Mel UI Configuration File.\n//\n//  This script is machine generated.  Edit at your own risk.\n//\n//\n\nglobal string $gMainPane;\nif (`paneLayout -exists $gMainPane`) {\n\n\tglobal int $gUseScenePanelConfig;\n\tint    $useSceneConfig = $gUseScenePanelConfig;\n\tint    $menusOkayInPanels = `optionVar -q allowMenusInPanels`;\tint    $nVisPanes = `paneLayout -q -nvp $gMainPane`;\n\tint    $nPanes = 0;\n\tstring $editorName;\n\tstring $panelName;\n\tstring $itemFilterName;\n\tstring $panelConfig;\n\n\t//\n\t//  get current state of the UI\n\t//\n\tsceneUIReplacement -update $gMainPane;\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Top View\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `modelPanel -unParent -l (localizedPanelLabel(\"Top View\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            modelEditor -e \n                -camera \"top\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"wireframe\" \n"
		+ "                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 1\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 8192\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -maxConstantTransparency 1\n                -rendererName \"base_OpenGL_Renderer\" \n"
		+ "                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 256 256 \n                -bumpResolution 512 512 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 1\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n"
		+ "                -imagePlane 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -clipGhosts 1\n                -greasePencils 1\n                -shadows 0\n                $editorName;\n            modelEditor -e -viewSelected 0 $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Top View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"top\" \n            -useInteractiveMode 0\n"
		+ "            -displayLights \"default\" \n            -displayAppearance \"wireframe\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 1\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 8192\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -maxConstantTransparency 1\n            -rendererName \"base_OpenGL_Renderer\" \n            -objectFilterShowInHUD 1\n"
		+ "            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -fluids 1\n"
		+ "            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Side View\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `modelPanel -unParent -l (localizedPanelLabel(\"Side View\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            modelEditor -e \n                -camera \"side\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n"
		+ "                -displayAppearance \"wireframe\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 1\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 8192\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -maxConstantTransparency 1\n                -rendererName \"base_OpenGL_Renderer\" \n"
		+ "                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 256 256 \n                -bumpResolution 512 512 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 1\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n"
		+ "                -imagePlane 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -clipGhosts 1\n                -greasePencils 1\n                -shadows 0\n                $editorName;\n            modelEditor -e -viewSelected 0 $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Side View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"side\" \n            -useInteractiveMode 0\n"
		+ "            -displayLights \"default\" \n            -displayAppearance \"wireframe\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 1\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 8192\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -maxConstantTransparency 1\n            -rendererName \"base_OpenGL_Renderer\" \n            -objectFilterShowInHUD 1\n"
		+ "            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -fluids 1\n"
		+ "            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Persp View\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `modelPanel -unParent -l (localizedPanelLabel(\"Persp View\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            modelEditor -e \n                -camera \"persp\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n"
		+ "                -displayAppearance \"smoothShaded\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 1\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 8192\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -maxConstantTransparency 1\n"
		+ "                -rendererName \"base_OpenGL_Renderer\" \n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 256 256 \n                -bumpResolution 512 512 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 1\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n"
		+ "                -hulls 1\n                -grid 1\n                -imagePlane 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -clipGhosts 1\n                -greasePencils 1\n                -shadows 0\n                $editorName;\n            modelEditor -e -viewSelected 0 $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Persp View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n"
		+ "            -camera \"persp\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 1\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 8192\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -maxConstantTransparency 1\n            -rendererName \"base_OpenGL_Renderer\" \n"
		+ "            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n"
		+ "            -dynamics 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"Outliner\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `outlinerPanel -unParent -l (localizedPanelLabel(\"Outliner\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            outlinerEditor -e \n                -docTag \"isolOutln_fromSeln\" \n                -showShapes 0\n"
		+ "                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 0\n                -showConnected 0\n                -showAnimCurvesOnly 0\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 0\n                -showDagOnly 1\n                -showAssets 1\n                -showContainedOnly 1\n                -showPublishedAsConnected 0\n                -showContainerContents 1\n                -ignoreDagHierarchy 0\n                -expandConnections 0\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 1\n                -showLeafs 1\n                -showNumericAttrsOnly 0\n                -highlightActive 1\n                -autoSelectNewObjects 0\n                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 0\n                -setFilter \"defaultSetFilter\" \n                -showSetMembers 1\n"
		+ "                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 0\n                -mapMotionTrails 0\n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"Outliner\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -docTag \"isolOutln_fromSeln\" \n            -showShapes 0\n"
		+ "            -showReferenceNodes 0\n            -showReferenceMembers 0\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n"
		+ "            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\tif ($useSceneConfig) {\n\t\toutlinerPanel -e -to $panelName;\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"graphEditor\" (localizedPanelLabel(\"Graph Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"graphEditor\" -l (localizedPanelLabel(\"Graph Editor\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n"
		+ "            outlinerEditor -e \n                -showShapes 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 1\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 0\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 1\n                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 1\n"
		+ "                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 1\n                -mapMotionTrails 1\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"GraphEd\");\n            animCurveEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 1\n"
		+ "                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -showResults \"off\" \n                -showBufferCurves \"off\" \n                -smoothness \"fine\" \n                -resultSamples 1\n                -resultScreenSamples 0\n                -resultUpdate \"delayed\" \n                -showUpstreamCurves 1\n                -stackedCurves 1\n                -stackedCurvesMin -1\n                -stackedCurvesMax 1\n                -stackedCurvesSpace 0.2\n                -displayNormalized 1\n                -preSelectionHighlight 0\n                -constrainDrag 0\n                -classicMode 1\n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Graph Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n"
		+ "                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 1\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 0\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 1\n                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 1\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n"
		+ "                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 1\n                -mapMotionTrails 1\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"GraphEd\");\n            animCurveEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 1\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n"
		+ "                -showResults \"off\" \n                -showBufferCurves \"off\" \n                -smoothness \"fine\" \n                -resultSamples 1\n                -resultScreenSamples 0\n                -resultUpdate \"delayed\" \n                -showUpstreamCurves 1\n                -stackedCurves 1\n                -stackedCurvesMin -1\n                -stackedCurvesMax 1\n                -stackedCurvesSpace 0.2\n                -displayNormalized 1\n                -preSelectionHighlight 0\n                -constrainDrag 0\n                -classicMode 1\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dopeSheetPanel\" (localizedPanelLabel(\"Dope Sheet\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"dopeSheetPanel\" -l (localizedPanelLabel(\"Dope Sheet\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n"
		+ "                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 0\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 0\n                -showCompounds 1\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 0\n                -doNotSelectNewObjects 1\n                -dropIsParent 1\n                -transmitFilters 0\n                -setFilter \"0\" \n                -showSetMembers 0\n"
		+ "                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 0\n                -mapMotionTrails 1\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"DopeSheetEd\");\n            dopeSheetEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -autoFit 0\n"
		+ "                -snapTime \"integer\" \n                -snapValue \"none\" \n                -outliner \"dopeSheetPanel1OutlineEd\" \n                -showSummary 1\n                -showScene 0\n                -hierarchyBelow 0\n                -showTicks 1\n                -selectionWindow 0 0 0 0 \n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dope Sheet\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 0\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n"
		+ "                -showPublishedAsConnected 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 0\n                -showCompounds 1\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 0\n                -doNotSelectNewObjects 1\n                -dropIsParent 1\n                -transmitFilters 0\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n"
		+ "                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 0\n                -mapMotionTrails 1\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"DopeSheetEd\");\n            dopeSheetEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -outliner \"dopeSheetPanel1OutlineEd\" \n                -showSummary 1\n                -showScene 0\n                -hierarchyBelow 0\n                -showTicks 1\n                -selectionWindow 0 0 0 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"clipEditorPanel\" (localizedPanelLabel(\"Trax Editor\")) `;\n"
		+ "\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"clipEditorPanel\" -l (localizedPanelLabel(\"Trax Editor\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = clipEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -manageSequencer 0 \n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Trax Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = clipEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n"
		+ "                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -manageSequencer 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"sequenceEditorPanel\" (localizedPanelLabel(\"Camera Sequencer\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"sequenceEditorPanel\" -l (localizedPanelLabel(\"Camera Sequencer\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = sequenceEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -manageSequencer 1 \n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n"
		+ "\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Camera Sequencer\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = sequenceEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -manageSequencer 1 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperGraphPanel\" (localizedPanelLabel(\"Hypergraph Hierarchy\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"hyperGraphPanel\" -l (localizedPanelLabel(\"Hypergraph Hierarchy\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"HyperGraphEd\");\n            hyperGraph -e \n                -graphLayoutStyle \"hierarchicalLayout\" \n"
		+ "                -orientation \"horiz\" \n                -mergeConnections 0\n                -zoom 1\n                -animateTransition 0\n                -showRelationships 1\n                -showShapes 0\n                -showDeformers 0\n                -showExpressions 0\n                -showConstraints 0\n                -showConnectionFromSelected 0\n                -showConnectionToSelected 0\n                -showUnderworld 0\n                -showInvisible 0\n                -transitionFrames 1\n                -opaqueContainers 0\n                -freeform 0\n                -imagePosition 0 0 \n                -imageScale 1\n                -imageEnabled 0\n                -graphType \"DAG\" \n                -heatMapDisplay 0\n                -updateSelection 1\n                -updateNodeAdded 1\n                -useDrawOverrideColor 0\n                -limitGraphTraversal -1\n                -range 0 0 \n                -iconSize \"smallIcons\" \n                -showCachedConnections 0\n                $editorName;\n\t\t}\n\t} else {\n"
		+ "\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypergraph Hierarchy\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"HyperGraphEd\");\n            hyperGraph -e \n                -graphLayoutStyle \"hierarchicalLayout\" \n                -orientation \"horiz\" \n                -mergeConnections 0\n                -zoom 1\n                -animateTransition 0\n                -showRelationships 1\n                -showShapes 0\n                -showDeformers 0\n                -showExpressions 0\n                -showConstraints 0\n                -showConnectionFromSelected 0\n                -showConnectionToSelected 0\n                -showUnderworld 0\n                -showInvisible 0\n                -transitionFrames 1\n                -opaqueContainers 0\n                -freeform 0\n                -imagePosition 0 0 \n                -imageScale 1\n                -imageEnabled 0\n                -graphType \"DAG\" \n                -heatMapDisplay 0\n                -updateSelection 1\n"
		+ "                -updateNodeAdded 1\n                -useDrawOverrideColor 0\n                -limitGraphTraversal -1\n                -range 0 0 \n                -iconSize \"smallIcons\" \n                -showCachedConnections 0\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperShadePanel\" (localizedPanelLabel(\"Hypershade\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"hyperShadePanel\" -l (localizedPanelLabel(\"Hypershade\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypershade\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"visorPanel\" (localizedPanelLabel(\"Visor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"visorPanel\" -l (localizedPanelLabel(\"Visor\")) -mbv $menusOkayInPanels `;\n"
		+ "\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Visor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"nodeEditorPanel\" (localizedPanelLabel(\"Node Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"nodeEditorPanel\" -l (localizedPanelLabel(\"Node Editor\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"NodeEditorEd\");\n            nodeEditor -e \n                -allAttributes 0\n                -allNodes 0\n                -autoSizeNodes 1\n                -createNodeCommand \"nodeEdCreateNodeCommand\" \n                -defaultPinnedState 0\n                -ignoreAssets 1\n                -additiveGraphingMode 0\n                -settingsChangedCallback \"nodeEdSyncControls\" \n                -traversalDepthLimit -1\n                -keyPressCommand \"nodeEdKeyPressCommand\" \n                -keyReleaseCommand \"nodeEdKeyReleaseCommand\" \n"
		+ "                -nodeTitleMode \"name\" \n                -gridSnap 0\n                -gridVisibility 1\n                -popupMenuScript \"nodeEdBuildPanelMenus\" \n                -island 0\n                -showNamespace 1\n                -showShapes 1\n                -showSGShapes 0\n                -showTransforms 1\n                -syncedSelection 1\n                -extendToShapes 1\n                $editorName;\n\t\t\tif (`objExists nodeEditorPanel1Info`) nodeEditor -e -restoreInfo nodeEditorPanel1Info $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Node Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"NodeEditorEd\");\n            nodeEditor -e \n                -allAttributes 0\n                -allNodes 0\n                -autoSizeNodes 1\n                -createNodeCommand \"nodeEdCreateNodeCommand\" \n                -defaultPinnedState 0\n                -ignoreAssets 1\n                -additiveGraphingMode 0\n                -settingsChangedCallback \"nodeEdSyncControls\" \n"
		+ "                -traversalDepthLimit -1\n                -keyPressCommand \"nodeEdKeyPressCommand\" \n                -keyReleaseCommand \"nodeEdKeyReleaseCommand\" \n                -nodeTitleMode \"name\" \n                -gridSnap 0\n                -gridVisibility 1\n                -popupMenuScript \"nodeEdBuildPanelMenus\" \n                -island 0\n                -showNamespace 1\n                -showShapes 1\n                -showSGShapes 0\n                -showTransforms 1\n                -syncedSelection 1\n                -extendToShapes 1\n                $editorName;\n\t\t\tif (`objExists nodeEditorPanel1Info`) nodeEditor -e -restoreInfo nodeEditorPanel1Info $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"createNodePanel\" (localizedPanelLabel(\"Create Node\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"createNodePanel\" -l (localizedPanelLabel(\"Create Node\")) -mbv $menusOkayInPanels `;\n"
		+ "\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Create Node\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"polyTexturePlacementPanel\" (localizedPanelLabel(\"UV Texture Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"polyTexturePlacementPanel\" -l (localizedPanelLabel(\"UV Texture Editor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"UV Texture Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"renderWindowPanel\" (localizedPanelLabel(\"Render View\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"renderWindowPanel\" -l (localizedPanelLabel(\"Render View\")) -mbv $menusOkayInPanels `;\n"
		+ "\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Render View\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"blendShapePanel\" (localizedPanelLabel(\"Blend Shape\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\tblendShapePanel -unParent -l (localizedPanelLabel(\"Blend Shape\")) -mbv $menusOkayInPanels ;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tblendShapePanel -edit -l (localizedPanelLabel(\"Blend Shape\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynRelEdPanel\" (localizedPanelLabel(\"Dynamic Relationships\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"dynRelEdPanel\" -l (localizedPanelLabel(\"Dynamic Relationships\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n"
		+ "\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dynamic Relationships\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"relationshipPanel\" (localizedPanelLabel(\"Relationship Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"relationshipPanel\" -l (localizedPanelLabel(\"Relationship Editor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Relationship Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"referenceEditorPanel\" (localizedPanelLabel(\"Reference Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"referenceEditorPanel\" -l (localizedPanelLabel(\"Reference Editor\")) -mbv $menusOkayInPanels `;\n"
		+ "\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Reference Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"componentEditorPanel\" (localizedPanelLabel(\"Component Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"componentEditorPanel\" -l (localizedPanelLabel(\"Component Editor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Component Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynPaintScriptedPanelType\" (localizedPanelLabel(\"Paint Effects\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"dynPaintScriptedPanelType\" -l (localizedPanelLabel(\"Paint Effects\")) -mbv $menusOkayInPanels `;\n"
		+ "\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Paint Effects\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"scriptEditorPanel\" (localizedPanelLabel(\"Script Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"scriptEditorPanel\" -l (localizedPanelLabel(\"Script Editor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Script Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\tif ($useSceneConfig) {\n\t\tscriptedPanel -e -to $panelName;\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"Stereo\" (localizedPanelLabel(\"Stereo\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"Stereo\" -l (localizedPanelLabel(\"Stereo\")) -mbv $menusOkayInPanels `;\n"
		+ "string $editorName = ($panelName+\"Editor\");\n            stereoCameraView -e \n                -camera \"persp\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"wireframe\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 1\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 8192\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n"
		+ "                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -maxConstantTransparency 1\n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 4 4 \n                -bumpResolution 4 4 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 0\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n"
		+ "                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -imagePlane 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -clipGhosts 1\n                -greasePencils 1\n                -shadows 0\n                -displayMode \"centerEye\" \n                -viewColor 0 0 0 1 \n                -useCustomBackground 1\n                $editorName;\n            stereoCameraView -e -viewSelected 0 $editorName;\n"
		+ "\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Stereo\")) -mbv $menusOkayInPanels  $panelName;\nstring $editorName = ($panelName+\"Editor\");\n            stereoCameraView -e \n                -camera \"persp\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"wireframe\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 1\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n"
		+ "                -textureMaxSize 8192\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -maxConstantTransparency 1\n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 4 4 \n                -bumpResolution 4 4 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 0\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n"
		+ "                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -imagePlane 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -clipGhosts 1\n                -greasePencils 1\n                -shadows 0\n                -displayMode \"centerEye\" \n"
		+ "                -viewColor 0 0 0 1 \n                -useCustomBackground 1\n                $editorName;\n            stereoCameraView -e -viewSelected 0 $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Front View\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `modelPanel -unParent -l (localizedPanelLabel(\"Front View\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            modelEditor -e \n                -camera \"front\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"wireframe\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 1\n                -backfaceCulling 0\n"
		+ "                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 8192\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -maxConstantTransparency 1\n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 4 4 \n                -bumpResolution 4 4 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 0\n"
		+ "                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -imagePlane 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n"
		+ "                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -clipGhosts 1\n                -greasePencils 1\n                -shadows 0\n                $editorName;\n            modelEditor -e -viewSelected 0 $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Front View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"front\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"wireframe\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 1\n            -backfaceCulling 0\n            -xray 0\n"
		+ "            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 8192\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -maxConstantTransparency 1\n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 4 4 \n            -bumpResolution 4 4 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 0\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n"
		+ "            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n"
		+ "            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"nodeEditorPanel\" (localizedPanelLabel(\"Node Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"nodeEditorPanel\" -l (localizedPanelLabel(\"Node Editor\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"NodeEditorEd\");\n            nodeEditor -e \n                -allAttributes 0\n                -allNodes 0\n                -autoSizeNodes 1\n                -createNodeCommand \"nodeEdCreateNodeCommand\" \n                -defaultPinnedState 0\n                -ignoreAssets 1\n                -additiveGraphingMode 0\n                -settingsChangedCallback \"nodeEdSyncControls\" \n                -traversalDepthLimit -1\n                -keyPressCommand \"nodeEdKeyPressCommand\" \n                -keyReleaseCommand \"nodeEdKeyReleaseCommand\" \n                -nodeTitleMode \"name\" \n"
		+ "                -gridSnap 0\n                -gridVisibility 1\n                -popupMenuScript \"nodeEdBuildPanelMenus\" \n                -island 0\n                -showNamespace 1\n                -showShapes 1\n                -showSGShapes 0\n                -showTransforms 1\n                -syncedSelection 1\n                -extendToShapes 1\n                $editorName;\n\t\t\tif (`objExists nodeEditorPanel2Info`) nodeEditor -e -restoreInfo nodeEditorPanel2Info $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Node Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"NodeEditorEd\");\n            nodeEditor -e \n                -allAttributes 0\n                -allNodes 0\n                -autoSizeNodes 1\n                -createNodeCommand \"nodeEdCreateNodeCommand\" \n                -defaultPinnedState 0\n                -ignoreAssets 1\n                -additiveGraphingMode 0\n                -settingsChangedCallback \"nodeEdSyncControls\" \n"
		+ "                -traversalDepthLimit -1\n                -keyPressCommand \"nodeEdKeyPressCommand\" \n                -keyReleaseCommand \"nodeEdKeyReleaseCommand\" \n                -nodeTitleMode \"name\" \n                -gridSnap 0\n                -gridVisibility 1\n                -popupMenuScript \"nodeEdBuildPanelMenus\" \n                -island 0\n                -showNamespace 1\n                -showShapes 1\n                -showSGShapes 0\n                -showTransforms 1\n                -syncedSelection 1\n                -extendToShapes 1\n                $editorName;\n\t\t\tif (`objExists nodeEditorPanel2Info`) nodeEditor -e -restoreInfo nodeEditorPanel2Info $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\tif ($useSceneConfig) {\n\t\tscriptedPanel -e -to $panelName;\n\t}\n\n\n\tif ($useSceneConfig) {\n        string $configName = `getPanel -cwl (localizedPanelLabel(\"Current Layout\"))`;\n        if (\"\" != $configName) {\n\t\t\tpanelConfiguration -edit -label (localizedPanelLabel(\"Current Layout\")) \n\t\t\t\t-defaultImage \"vacantCell.xP:/\"\n"
		+ "\t\t\t\t-image \"\"\n\t\t\t\t-sc false\n\t\t\t\t-configString \"global string $gMainPane; paneLayout -e -cn \\\"single\\\" -ps 1 100 100 $gMainPane;\"\n\t\t\t\t-removeAllPanels\n\t\t\t\t-ap false\n\t\t\t\t\t(localizedPanelLabel(\"Persp View\")) \n\t\t\t\t\t\"modelPanel\"\n"
		+ "\t\t\t\t\t\"$panelName = `modelPanel -unParent -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels `;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 1\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 8192\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -maxConstantTransparency 1\\n    -rendererName \\\"base_OpenGL_Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName\"\n"
		+ "\t\t\t\t\t\"modelPanel -edit -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels  $panelName;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 1\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 8192\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -maxConstantTransparency 1\\n    -rendererName \\\"base_OpenGL_Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName\"\n"
		+ "\t\t\t\t$configName;\n\n            setNamedPanelLayout (localizedPanelLabel(\"Current Layout\"));\n        }\n\n        panelHistory -e -clear mainPanelHistory;\n        setFocus `paneLayout -q -p1 $gMainPane`;\n        sceneUIReplacement -deleteRemaining;\n        sceneUIReplacement -clear;\n\t}\n\n\ngrid -spacing 5 -size 12 -divisions 5 -displayAxes yes -displayGridLines yes -displayDivisionLines yes -displayPerspectiveLabels no -displayOrthographicLabels no -displayAxesBold yes -perspectiveLabelPosition axis -orthographicLabelPosition edge;\nviewManip -drawCompass 0 -compassAngle 0 -frontParameters \"\" -homeParameters \"\" -selectionLockParameters \"\";\n}\n");
	setAttr ".st" 3;
createNode script -n "xgenGlobals";
	setAttr ".a" -type "string" "import maya.cmds as cmds\nif cmds.about(batch=True):\n\txgg.Playblast=False\nelse:\n\txgui.createDescriptionEditor(False).setGlobals( previewSel=0, previewMode=0, clearSel=0, clearMode=0, playblast=1, clearCache=0, autoCreateMR=1 )";
	setAttr ".stp" 1;
createNode unitConversion -n "unitConversion1";
	setAttr ".cf" 57.295779513082323;
createNode unitConversion -n "unitConversion2";
	setAttr ".cf" 57.295779513082323;
createNode unitConversion -n "unitConversion3";
	setAttr ".cf" 57.295779513082323;
createNode renderLayerManager -n "renderLayerManager";
createNode hyperGraphInfo -n "nodeEditorPanel2Info";
createNode hyperView -n "hyperView1";
	setAttr ".vl" -type "double2" -91.6666666666667 -533.49004282102885 ;
	setAttr ".vh" -type "double2" 842.85714285714289 13.251947582933497 ;
	setAttr ".dag" no;
createNode hyperLayout -n "hyperLayout1";
	setAttr ".ihi" 0;
	setAttr ".anf" yes;
createNode hyperGraphInfo -n "nodeEditorPanel1Info";
createNode hyperView -n "hyperView2";
	setAttr ".dag" no;
createNode hyperLayout -n "hyperLayout2";
	setAttr ".ihi" 0;
	setAttr ".anf" yes;
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
	setAttr -av -k on ".pa" 1;
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
	setAttr ".otfna" -type "stringArray" 18 "NURBS Curves" "NURBS Surfaces" "Polygons" "Subdiv Surfaces" "Particles" "Fluids" "Image Planes" "UI:" "Lights" "Cameras" "Locators" "Joints" "IK Handles" "Deformers" "Motion Trails" "Components" "Misc. UI" "Ornaments"  ;
	setAttr ".otfva" -type "Int32Array" 18 0 1 1 1 1 1
		 1 0 0 0 0 0 0 0 0 0 0 0 ;
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
connectAttr "c_Lf_eyebrows_01_upclamp_finalrange.opr" "c_Lf_eyebrows_01_FRAME.up"
		;
connectAttr "c_Lf_eyebrows_01_dnclamp_finalrange.opr" "c_Lf_eyebrows_01_FRAME.dn"
		;
connectAttr "c_Lf_eyebrows_01_lfclamp_finalrange.opr" "c_Lf_eyebrows_01_FRAME.lf"
		;
connectAttr "c_Lf_eyebrows_01_rtclamp_finalrange.opr" "c_Lf_eyebrows_01_FRAME.rt"
		;
connectAttr "c_Lf_eyebrows_01_lfupmult.ox" "c_Lf_eyebrows_01_FRAME.lfup";
connectAttr "c_Lf_eyebrows_01_rtupmult.ox" "c_Lf_eyebrows_01_FRAME.rtup";
connectAttr "c_Lf_eyebrows_01_lfdnmult.ox" "c_Lf_eyebrows_01_FRAME.lfdn";
connectAttr "c_Lf_eyebrows_01_rtdnmult.ox" "c_Lf_eyebrows_01_FRAME.rtdn";
connectAttr "c_Lf_eyebrows_01_lfclamp_NYrange.opr" "c_Lf_eyebrows_01_FRAME.fourAxis_up"
		;
connectAttr "c_Lf_eyebrows_01_lfclamp_PYrange.opr" "c_Lf_eyebrows_01_FRAME.fourAxis_dn"
		;
connectAttr "c_Lf_eyebrows_01_upclamp_PXrange.opr" "c_Lf_eyebrows_01_FRAME.fourAxis_lf"
		;
connectAttr "c_Lf_eyebrows_01_upclamp_NXrange.opr" "c_Lf_eyebrows_01_FRAME.fourAxis_rt"
		;
connectAttr "c_Lf_eyebrows_01_CTRL.frameSelectAble" "c_Lf_eyebrows_01_FRAMEShape.ovdt"
		;
connectAttr "c_Lf_eyebrows_01_CTRL.frameSelectAble" "c_Lf_eyebrows_01_FRAME_lockzyShape.ovdt"
		;
connectAttr "c_Lf_eyebrows_01_CTRL.frameSelectAble" "c_Lf_eyebrows_01_FRAME_lockfyShape.ovdt"
		;
connectAttr "c_Lf_eyebrows_01_CTRL.frameSelectAble" "c_Lf_eyebrows_01_FRAME_lockzxShape.ovdt"
		;
connectAttr "c_Lf_eyebrows_01_CTRL.frameSelectAble" "c_Lf_eyebrows_01_FRAME_lockfxShape.ovdt"
		;
connectAttr "c_Lf_eyebrows_01_CTRL.frameSelectAble" "c_Lf_eyebrows_01_FRAME_lockzyfyShape.ovdt"
		;
connectAttr "c_Lf_eyebrows_01_CTRL.frameSelectAble" "c_Lf_eyebrows_01_FRAME_lockzxfxShape.ovdt"
		;
connectAttr "c_Lf_eyebrows_01_CTRL.frameSelectAble" "c_Lf_eyebrows_01_FRAME_lockzyfyzxShape.ovdt"
		;
connectAttr "c_Lf_eyebrows_01_CTRL.frameSelectAble" "c_Lf_eyebrows_01_FRAME_lockzyfyfxShape.ovdt"
		;
connectAttr "c_Lf_eyebrows_01_CTRL.frameSelectAble" "c_Lf_eyebrows_01_FRAME_lockzxfxzyShape.ovdt"
		;
connectAttr "c_Lf_eyebrows_01_CTRL.frameSelectAble" "c_Lf_eyebrows_01_FRAME_lockzxfxfyShape.ovdt"
		;
connectAttr "c_Lf_eyebrows_01_FRAME.up_Vis" "c_Lf_eyebrows_01_CTRL_up.v";
connectAttr "c_Lf_eyebrows_01_FRAME.dn_Vis" "c_Lf_eyebrows_01_CTRL_dn.v";
connectAttr "c_Lf_eyebrows_01_FRAME.lf_Vis" "c_Lf_eyebrows_01_CTRL_lf.v";
connectAttr "c_Lf_eyebrows_01_FRAME.lfup_Vis" "c_Lf_eyebrows_01_CTRL_lfup.v";
connectAttr "c_Lf_eyebrows_01_FRAME.rt_Vis" "c_Lf_eyebrows_01_CTRL_rt.v";
connectAttr "c_Lf_eyebrows_01_FRAME.rtup_Vis" "c_Lf_eyebrows_01_CTRL_rtup.v";
connectAttr "c_Lf_eyebrows_01_FRAME.lfdn_Vis" "c_Lf_eyebrows_01_CTRL_lfdn.v";
connectAttr "c_Lf_eyebrows_01_FRAME.rtdn_Vis" "c_Lf_eyebrows_01_CTRL_rtdn.v";
connectAttr "c_Lf_eyebrows_01_FRAME.fourAxis_up_Vis" "c_Lf_eyebrows_01_CTRL_fourAxisup.v"
		;
connectAttr "c_Lf_eyebrows_01_FRAME.fourAxis_dn_Vis" "c_Lf_eyebrows_01_CTRL_fourAxisdn.v"
		;
connectAttr "c_Lf_eyebrows_01_FRAME.fourAxis_lf_Vis" "c_Lf_eyebrows_01_CTRL_fourAxislf.v"
		;
connectAttr "c_Lf_eyebrows_01_FRAME.fourAxis_rt_Vis" "c_Lf_eyebrows_01_CTRL_fourAxisrt.v"
		;
connectAttr "c_Lf_eyebrows_02_upclamp_finalrange.opr" "c_Lf_eyebrows_02_FRAME.up"
		;
connectAttr "c_Lf_eyebrows_02_dnclamp_finalrange.opr" "c_Lf_eyebrows_02_FRAME.dn"
		;
connectAttr "c_Lf_eyebrows_02_lfclamp_finalrange.opr" "c_Lf_eyebrows_02_FRAME.lf"
		;
connectAttr "c_Lf_eyebrows_02_rtclamp_finalrange.opr" "c_Lf_eyebrows_02_FRAME.rt"
		;
connectAttr "c_Lf_eyebrows_02_lfupmult.ox" "c_Lf_eyebrows_02_FRAME.lfup";
connectAttr "c_Lf_eyebrows_02_rtupmult.ox" "c_Lf_eyebrows_02_FRAME.rtup";
connectAttr "c_Lf_eyebrows_02_lfdnmult.ox" "c_Lf_eyebrows_02_FRAME.lfdn";
connectAttr "c_Lf_eyebrows_02_rtdnmult.ox" "c_Lf_eyebrows_02_FRAME.rtdn";
connectAttr "c_Lf_eyebrows_02_lfclamp_NYrange.opr" "c_Lf_eyebrows_02_FRAME.fourAxis_up"
		;
connectAttr "c_Lf_eyebrows_02_lfclamp_PYrange.opr" "c_Lf_eyebrows_02_FRAME.fourAxis_dn"
		;
connectAttr "c_Lf_eyebrows_02_upclamp_PXrange.opr" "c_Lf_eyebrows_02_FRAME.fourAxis_lf"
		;
connectAttr "c_Lf_eyebrows_02_upclamp_NXrange.opr" "c_Lf_eyebrows_02_FRAME.fourAxis_rt"
		;
connectAttr "c_Lf_eyebrows_02_CTRL.frameSelectAble" "c_Lf_eyebrows_02_FRAMEShape.ovdt"
		;
connectAttr "c_Lf_eyebrows_02_CTRL.frameSelectAble" "c_Lf_eyebrows_02_FRAME_lockzyShape.ovdt"
		;
connectAttr "c_Lf_eyebrows_02_CTRL.frameSelectAble" "c_Lf_eyebrows_02_FRAME_lockfyShape.ovdt"
		;
connectAttr "c_Lf_eyebrows_02_CTRL.frameSelectAble" "c_Lf_eyebrows_02_FRAME_lockzxShape.ovdt"
		;
connectAttr "c_Lf_eyebrows_02_CTRL.frameSelectAble" "c_Lf_eyebrows_02_FRAME_lockfxShape.ovdt"
		;
connectAttr "c_Lf_eyebrows_02_CTRL.frameSelectAble" "c_Lf_eyebrows_02_FRAME_lockzyfyShape.ovdt"
		;
connectAttr "c_Lf_eyebrows_02_CTRL.frameSelectAble" "c_Lf_eyebrows_02_FRAME_lockzxfxShape.ovdt"
		;
connectAttr "c_Lf_eyebrows_02_CTRL.frameSelectAble" "c_Lf_eyebrows_02_FRAME_lockzyfyzxShape.ovdt"
		;
connectAttr "c_Lf_eyebrows_02_CTRL.frameSelectAble" "c_Lf_eyebrows_02_FRAME_lockzyfyfxShape.ovdt"
		;
connectAttr "c_Lf_eyebrows_02_CTRL.frameSelectAble" "c_Lf_eyebrows_02_FRAME_lockzxfxzyShape.ovdt"
		;
connectAttr "c_Lf_eyebrows_02_CTRL.frameSelectAble" "c_Lf_eyebrows_02_FRAME_lockzxfxfyShape.ovdt"
		;
connectAttr "c_Lf_eyebrows_02_FRAME.up_Vis" "c_Lf_eyebrows_02_CTRL_up.v";
connectAttr "c_Lf_eyebrows_02_FRAME.dn_Vis" "c_Lf_eyebrows_02_CTRL_dn.v";
connectAttr "c_Lf_eyebrows_02_FRAME.lf_Vis" "c_Lf_eyebrows_02_CTRL_lf.v";
connectAttr "c_Lf_eyebrows_02_FRAME.lfup_Vis" "c_Lf_eyebrows_02_CTRL_lfup.v";
connectAttr "c_Lf_eyebrows_02_FRAME.rt_Vis" "c_Lf_eyebrows_02_CTRL_rt.v";
connectAttr "c_Lf_eyebrows_02_FRAME.rtup_Vis" "c_Lf_eyebrows_02_CTRL_rtup.v";
connectAttr "c_Lf_eyebrows_02_FRAME.lfdn_Vis" "c_Lf_eyebrows_02_CTRL_lfdn.v";
connectAttr "c_Lf_eyebrows_02_FRAME.rtdn_Vis" "c_Lf_eyebrows_02_CTRL_rtdn.v";
connectAttr "c_Lf_eyebrows_02_FRAME.fourAxis_up_Vis" "c_Lf_eyebrows_02_CTRL_fourAxisup.v"
		;
connectAttr "c_Lf_eyebrows_02_FRAME.fourAxis_dn_Vis" "c_Lf_eyebrows_02_CTRL_fourAxisdn.v"
		;
connectAttr "c_Lf_eyebrows_02_FRAME.fourAxis_lf_Vis" "c_Lf_eyebrows_02_CTRL_fourAxislf.v"
		;
connectAttr "c_Lf_eyebrows_02_FRAME.fourAxis_rt_Vis" "c_Lf_eyebrows_02_CTRL_fourAxisrt.v"
		;
connectAttr "c_Lf_eyebrows_03_upclamp_finalrange.opr" "c_Lf_eyebrows_03_FRAME.up"
		;
connectAttr "c_Lf_eyebrows_03_dnclamp_finalrange.opr" "c_Lf_eyebrows_03_FRAME.dn"
		;
connectAttr "c_Lf_eyebrows_03_lfclamp_finalrange.opr" "c_Lf_eyebrows_03_FRAME.lf"
		;
connectAttr "c_Lf_eyebrows_03_rtclamp_finalrange.opr" "c_Lf_eyebrows_03_FRAME.rt"
		;
connectAttr "c_Lf_eyebrows_03_lfupmult.ox" "c_Lf_eyebrows_03_FRAME.lfup";
connectAttr "c_Lf_eyebrows_03_rtupmult.ox" "c_Lf_eyebrows_03_FRAME.rtup";
connectAttr "c_Lf_eyebrows_03_lfdnmult.ox" "c_Lf_eyebrows_03_FRAME.lfdn";
connectAttr "c_Lf_eyebrows_03_rtdnmult.ox" "c_Lf_eyebrows_03_FRAME.rtdn";
connectAttr "c_Lf_eyebrows_03_lfclamp_NYrange.opr" "c_Lf_eyebrows_03_FRAME.fourAxis_up"
		;
connectAttr "c_Lf_eyebrows_03_lfclamp_PYrange.opr" "c_Lf_eyebrows_03_FRAME.fourAxis_dn"
		;
connectAttr "c_Lf_eyebrows_03_upclamp_PXrange.opr" "c_Lf_eyebrows_03_FRAME.fourAxis_lf"
		;
connectAttr "c_Lf_eyebrows_03_upclamp_NXrange.opr" "c_Lf_eyebrows_03_FRAME.fourAxis_rt"
		;
connectAttr "c_Lf_eyebrows_03_CTRL.frameSelectAble" "c_Lf_eyebrows_03_FRAMEShape.ovdt"
		;
connectAttr "c_Lf_eyebrows_03_CTRL.frameSelectAble" "c_Lf_eyebrows_03_FRAME_lockzyShape.ovdt"
		;
connectAttr "c_Lf_eyebrows_03_CTRL.frameSelectAble" "c_Lf_eyebrows_03_FRAME_lockfyShape.ovdt"
		;
connectAttr "c_Lf_eyebrows_03_CTRL.frameSelectAble" "c_Lf_eyebrows_03_FRAME_lockzxShape.ovdt"
		;
connectAttr "c_Lf_eyebrows_03_CTRL.frameSelectAble" "c_Lf_eyebrows_03_FRAME_lockfxShape.ovdt"
		;
connectAttr "c_Lf_eyebrows_03_CTRL.frameSelectAble" "c_Lf_eyebrows_03_FRAME_lockzyfyShape.ovdt"
		;
connectAttr "c_Lf_eyebrows_03_CTRL.frameSelectAble" "c_Lf_eyebrows_03_FRAME_lockzxfxShape.ovdt"
		;
connectAttr "c_Lf_eyebrows_03_CTRL.frameSelectAble" "c_Lf_eyebrows_03_FRAME_lockzyfyzxShape.ovdt"
		;
connectAttr "c_Lf_eyebrows_03_CTRL.frameSelectAble" "c_Lf_eyebrows_03_FRAME_lockzyfyfxShape.ovdt"
		;
connectAttr "c_Lf_eyebrows_03_CTRL.frameSelectAble" "c_Lf_eyebrows_03_FRAME_lockzxfxzyShape.ovdt"
		;
connectAttr "c_Lf_eyebrows_03_CTRL.frameSelectAble" "c_Lf_eyebrows_03_FRAME_lockzxfxfyShape.ovdt"
		;
connectAttr "c_Lf_eyebrows_03_FRAME.up_Vis" "c_Lf_eyebrows_03_CTRL_up.v";
connectAttr "c_Lf_eyebrows_03_FRAME.dn_Vis" "c_Lf_eyebrows_03_CTRL_dn.v";
connectAttr "c_Lf_eyebrows_03_FRAME.lf_Vis" "c_Lf_eyebrows_03_CTRL_lf.v";
connectAttr "c_Lf_eyebrows_03_FRAME.lfup_Vis" "c_Lf_eyebrows_03_CTRL_lfup.v";
connectAttr "c_Lf_eyebrows_03_FRAME.rt_Vis" "c_Lf_eyebrows_03_CTRL_rt.v";
connectAttr "c_Lf_eyebrows_03_FRAME.rtup_Vis" "c_Lf_eyebrows_03_CTRL_rtup.v";
connectAttr "c_Lf_eyebrows_03_FRAME.lfdn_Vis" "c_Lf_eyebrows_03_CTRL_lfdn.v";
connectAttr "c_Lf_eyebrows_03_FRAME.rtdn_Vis" "c_Lf_eyebrows_03_CTRL_rtdn.v";
connectAttr "c_Lf_eyebrows_03_FRAME.fourAxis_up_Vis" "c_Lf_eyebrows_03_CTRL_fourAxisup.v"
		;
connectAttr "c_Lf_eyebrows_03_FRAME.fourAxis_dn_Vis" "c_Lf_eyebrows_03_CTRL_fourAxisdn.v"
		;
connectAttr "c_Lf_eyebrows_03_FRAME.fourAxis_lf_Vis" "c_Lf_eyebrows_03_CTRL_fourAxislf.v"
		;
connectAttr "c_Lf_eyebrows_03_FRAME.fourAxis_rt_Vis" "c_Lf_eyebrows_03_CTRL_fourAxisrt.v"
		;
connectAttr "c_Rt_eyebrows_01_upclamp_finalrange.opr" "c_Rt_eyebrows_01_FRAME.up"
		;
connectAttr "c_Rt_eyebrows_01_dnclamp_finalrange.opr" "c_Rt_eyebrows_01_FRAME.dn"
		;
connectAttr "c_Rt_eyebrows_01_lfclamp_finalrange.opr" "c_Rt_eyebrows_01_FRAME.lf"
		;
connectAttr "c_Rt_eyebrows_01_rtclamp_finalrange.opr" "c_Rt_eyebrows_01_FRAME.rt"
		;
connectAttr "c_Rt_eyebrows_01_lfupmult.ox" "c_Rt_eyebrows_01_FRAME.lfup";
connectAttr "c_Rt_eyebrows_01_rtupmult.ox" "c_Rt_eyebrows_01_FRAME.rtup";
connectAttr "c_Rt_eyebrows_01_lfdnmult.ox" "c_Rt_eyebrows_01_FRAME.lfdn";
connectAttr "c_Rt_eyebrows_01_rtdnmult.ox" "c_Rt_eyebrows_01_FRAME.rtdn";
connectAttr "c_Rt_eyebrows_01_lfclamp_NYrange.opr" "c_Rt_eyebrows_01_FRAME.fourAxis_up"
		;
connectAttr "c_Rt_eyebrows_01_lfclamp_PYrange.opr" "c_Rt_eyebrows_01_FRAME.fourAxis_dn"
		;
connectAttr "c_Rt_eyebrows_01_upclamp_PXrange.opr" "c_Rt_eyebrows_01_FRAME.fourAxis_lf"
		;
connectAttr "c_Rt_eyebrows_01_upclamp_NXrange.opr" "c_Rt_eyebrows_01_FRAME.fourAxis_rt"
		;
connectAttr "c_Rt_eyebrows_01_CTRL.frameSelectAble" "c_Rt_eyebrows_01_FRAMEShape.ovdt"
		;
connectAttr "c_Rt_eyebrows_01_CTRL.frameSelectAble" "c_Rt_eyebrows_01_FRAME_lockzyShape.ovdt"
		;
connectAttr "c_Rt_eyebrows_01_CTRL.frameSelectAble" "c_Rt_eyebrows_01_FRAME_lockfyShape.ovdt"
		;
connectAttr "c_Rt_eyebrows_01_CTRL.frameSelectAble" "c_Rt_eyebrows_01_FRAME_lockzxShape.ovdt"
		;
connectAttr "c_Rt_eyebrows_01_CTRL.frameSelectAble" "c_Rt_eyebrows_01_FRAME_lockfxShape.ovdt"
		;
connectAttr "c_Rt_eyebrows_01_CTRL.frameSelectAble" "c_Rt_eyebrows_01_FRAME_lockzyfyShape.ovdt"
		;
connectAttr "c_Rt_eyebrows_01_CTRL.frameSelectAble" "c_Rt_eyebrows_01_FRAME_lockzxfxShape.ovdt"
		;
connectAttr "c_Rt_eyebrows_01_CTRL.frameSelectAble" "c_Rt_eyebrows_01_FRAME_lockzyfyzxShape.ovdt"
		;
connectAttr "c_Rt_eyebrows_01_CTRL.frameSelectAble" "c_Rt_eyebrows_01_FRAME_lockzyfyfxShape.ovdt"
		;
connectAttr "c_Rt_eyebrows_01_CTRL.frameSelectAble" "c_Rt_eyebrows_01_FRAME_lockzxfxzyShape.ovdt"
		;
connectAttr "c_Rt_eyebrows_01_CTRL.frameSelectAble" "c_Rt_eyebrows_01_FRAME_lockzxfxfyShape.ovdt"
		;
connectAttr "c_Rt_eyebrows_01_FRAME.up_Vis" "c_Rt_eyebrows_01_CTRL_up.v";
connectAttr "c_Rt_eyebrows_01_FRAME.dn_Vis" "c_Rt_eyebrows_01_CTRL_dn.v";
connectAttr "c_Rt_eyebrows_01_FRAME.lf_Vis" "c_Rt_eyebrows_01_CTRL_lf.v";
connectAttr "c_Rt_eyebrows_01_FRAME.lfup_Vis" "c_Rt_eyebrows_01_CTRL_lfup.v";
connectAttr "c_Rt_eyebrows_01_FRAME.rt_Vis" "c_Rt_eyebrows_01_CTRL_rt.v";
connectAttr "c_Rt_eyebrows_01_FRAME.rtup_Vis" "c_Rt_eyebrows_01_CTRL_rtup.v";
connectAttr "c_Rt_eyebrows_01_FRAME.lfdn_Vis" "c_Rt_eyebrows_01_CTRL_lfdn.v";
connectAttr "c_Rt_eyebrows_01_FRAME.rtdn_Vis" "c_Rt_eyebrows_01_CTRL_rtdn.v";
connectAttr "c_Rt_eyebrows_01_FRAME.fourAxis_up_Vis" "c_Rt_eyebrows_01_CTRL_fourAxisup.v"
		;
connectAttr "c_Rt_eyebrows_01_FRAME.fourAxis_dn_Vis" "c_Rt_eyebrows_01_CTRL_fourAxisdn.v"
		;
connectAttr "c_Rt_eyebrows_01_FRAME.fourAxis_lf_Vis" "c_Rt_eyebrows_01_CTRL_fourAxislf.v"
		;
connectAttr "c_Rt_eyebrows_01_FRAME.fourAxis_rt_Vis" "c_Rt_eyebrows_01_CTRL_fourAxisrt.v"
		;
connectAttr "c_Rt_eyebrows_02_upclamp_finalrange.opr" "c_Rt_eyebrows_02_FRAME.up"
		;
connectAttr "c_Rt_eyebrows_02_dnclamp_finalrange.opr" "c_Rt_eyebrows_02_FRAME.dn"
		;
connectAttr "c_Rt_eyebrows_02_lfclamp_finalrange.opr" "c_Rt_eyebrows_02_FRAME.lf"
		;
connectAttr "c_Rt_eyebrows_02_rtclamp_finalrange.opr" "c_Rt_eyebrows_02_FRAME.rt"
		;
connectAttr "c_Rt_eyebrows_02_lfupmult.ox" "c_Rt_eyebrows_02_FRAME.lfup";
connectAttr "c_Rt_eyebrows_02_rtupmult.ox" "c_Rt_eyebrows_02_FRAME.rtup";
connectAttr "c_Rt_eyebrows_02_lfdnmult.ox" "c_Rt_eyebrows_02_FRAME.lfdn";
connectAttr "c_Rt_eyebrows_02_rtdnmult.ox" "c_Rt_eyebrows_02_FRAME.rtdn";
connectAttr "c_Rt_eyebrows_02_lfclamp_NYrange.opr" "c_Rt_eyebrows_02_FRAME.fourAxis_up"
		;
connectAttr "c_Rt_eyebrows_02_lfclamp_PYrange.opr" "c_Rt_eyebrows_02_FRAME.fourAxis_dn"
		;
connectAttr "c_Rt_eyebrows_02_upclamp_PXrange.opr" "c_Rt_eyebrows_02_FRAME.fourAxis_lf"
		;
connectAttr "c_Rt_eyebrows_02_upclamp_NXrange.opr" "c_Rt_eyebrows_02_FRAME.fourAxis_rt"
		;
connectAttr "c_Rt_eyebrows_02_CTRL.frameSelectAble" "c_Rt_eyebrows_02_FRAMEShape.ovdt"
		;
connectAttr "c_Rt_eyebrows_02_CTRL.frameSelectAble" "c_Rt_eyebrows_02_FRAME_lockzyShape.ovdt"
		;
connectAttr "c_Rt_eyebrows_02_CTRL.frameSelectAble" "c_Rt_eyebrows_02_FRAME_lockfyShape.ovdt"
		;
connectAttr "c_Rt_eyebrows_02_CTRL.frameSelectAble" "c_Rt_eyebrows_02_FRAME_lockzxShape.ovdt"
		;
connectAttr "c_Rt_eyebrows_02_CTRL.frameSelectAble" "c_Rt_eyebrows_02_FRAME_lockfxShape.ovdt"
		;
connectAttr "c_Rt_eyebrows_02_CTRL.frameSelectAble" "c_Rt_eyebrows_02_FRAME_lockzyfyShape.ovdt"
		;
connectAttr "c_Rt_eyebrows_02_CTRL.frameSelectAble" "c_Rt_eyebrows_02_FRAME_lockzxfxShape.ovdt"
		;
connectAttr "c_Rt_eyebrows_02_CTRL.frameSelectAble" "c_Rt_eyebrows_02_FRAME_lockzyfyzxShape.ovdt"
		;
connectAttr "c_Rt_eyebrows_02_CTRL.frameSelectAble" "c_Rt_eyebrows_02_FRAME_lockzyfyfxShape.ovdt"
		;
connectAttr "c_Rt_eyebrows_02_CTRL.frameSelectAble" "c_Rt_eyebrows_02_FRAME_lockzxfxzyShape.ovdt"
		;
connectAttr "c_Rt_eyebrows_02_CTRL.frameSelectAble" "c_Rt_eyebrows_02_FRAME_lockzxfxfyShape.ovdt"
		;
connectAttr "c_Rt_eyebrows_02_FRAME.up_Vis" "c_Rt_eyebrows_02_CTRL_up.v";
connectAttr "c_Rt_eyebrows_02_FRAME.dn_Vis" "c_Rt_eyebrows_02_CTRL_dn.v";
connectAttr "c_Rt_eyebrows_02_FRAME.lf_Vis" "c_Rt_eyebrows_02_CTRL_lf.v";
connectAttr "c_Rt_eyebrows_02_FRAME.lfup_Vis" "c_Rt_eyebrows_02_CTRL_lfup.v";
connectAttr "c_Rt_eyebrows_02_FRAME.rt_Vis" "c_Rt_eyebrows_02_CTRL_rt.v";
connectAttr "c_Rt_eyebrows_02_FRAME.rtup_Vis" "c_Rt_eyebrows_02_CTRL_rtup.v";
connectAttr "c_Rt_eyebrows_02_FRAME.lfdn_Vis" "c_Rt_eyebrows_02_CTRL_lfdn.v";
connectAttr "c_Rt_eyebrows_02_FRAME.rtdn_Vis" "c_Rt_eyebrows_02_CTRL_rtdn.v";
connectAttr "c_Rt_eyebrows_02_FRAME.fourAxis_up_Vis" "c_Rt_eyebrows_02_CTRL_fourAxisup.v"
		;
connectAttr "c_Rt_eyebrows_02_FRAME.fourAxis_dn_Vis" "c_Rt_eyebrows_02_CTRL_fourAxisdn.v"
		;
connectAttr "c_Rt_eyebrows_02_FRAME.fourAxis_lf_Vis" "c_Rt_eyebrows_02_CTRL_fourAxislf.v"
		;
connectAttr "c_Rt_eyebrows_02_FRAME.fourAxis_rt_Vis" "c_Rt_eyebrows_02_CTRL_fourAxisrt.v"
		;
connectAttr "c_Rt_eyebrows_03_upclamp_finalrange.opr" "c_Rt_eyebrows_03_FRAME.up"
		;
connectAttr "c_Rt_eyebrows_03_dnclamp_finalrange.opr" "c_Rt_eyebrows_03_FRAME.dn"
		;
connectAttr "c_Rt_eyebrows_03_lfclamp_finalrange.opr" "c_Rt_eyebrows_03_FRAME.lf"
		;
connectAttr "c_Rt_eyebrows_03_rtclamp_finalrange.opr" "c_Rt_eyebrows_03_FRAME.rt"
		;
connectAttr "c_Rt_eyebrows_03_lfupmult.ox" "c_Rt_eyebrows_03_FRAME.lfup";
connectAttr "c_Rt_eyebrows_03_rtupmult.ox" "c_Rt_eyebrows_03_FRAME.rtup";
connectAttr "c_Rt_eyebrows_03_lfdnmult.ox" "c_Rt_eyebrows_03_FRAME.lfdn";
connectAttr "c_Rt_eyebrows_03_rtdnmult.ox" "c_Rt_eyebrows_03_FRAME.rtdn";
connectAttr "c_Rt_eyebrows_03_lfclamp_NYrange.opr" "c_Rt_eyebrows_03_FRAME.fourAxis_up"
		;
connectAttr "c_Rt_eyebrows_03_lfclamp_PYrange.opr" "c_Rt_eyebrows_03_FRAME.fourAxis_dn"
		;
connectAttr "c_Rt_eyebrows_03_upclamp_PXrange.opr" "c_Rt_eyebrows_03_FRAME.fourAxis_lf"
		;
connectAttr "c_Rt_eyebrows_03_upclamp_NXrange.opr" "c_Rt_eyebrows_03_FRAME.fourAxis_rt"
		;
connectAttr "c_Rt_eyebrows_03_CTRL.frameSelectAble" "c_Rt_eyebrows_03_FRAMEShape.ovdt"
		;
connectAttr "c_Rt_eyebrows_03_CTRL.frameSelectAble" "c_Rt_eyebrows_03_FRAME_lockzyShape.ovdt"
		;
connectAttr "c_Rt_eyebrows_03_CTRL.frameSelectAble" "c_Rt_eyebrows_03_FRAME_lockfyShape.ovdt"
		;
connectAttr "c_Rt_eyebrows_03_CTRL.frameSelectAble" "c_Rt_eyebrows_03_FRAME_lockzxShape.ovdt"
		;
connectAttr "c_Rt_eyebrows_03_CTRL.frameSelectAble" "c_Rt_eyebrows_03_FRAME_lockfxShape.ovdt"
		;
connectAttr "c_Rt_eyebrows_03_CTRL.frameSelectAble" "c_Rt_eyebrows_03_FRAME_lockzyfyShape.ovdt"
		;
connectAttr "c_Rt_eyebrows_03_CTRL.frameSelectAble" "c_Rt_eyebrows_03_FRAME_lockzxfxShape.ovdt"
		;
connectAttr "c_Rt_eyebrows_03_CTRL.frameSelectAble" "c_Rt_eyebrows_03_FRAME_lockzyfyzxShape.ovdt"
		;
connectAttr "c_Rt_eyebrows_03_CTRL.frameSelectAble" "c_Rt_eyebrows_03_FRAME_lockzyfyfxShape.ovdt"
		;
connectAttr "c_Rt_eyebrows_03_CTRL.frameSelectAble" "c_Rt_eyebrows_03_FRAME_lockzxfxzyShape.ovdt"
		;
connectAttr "c_Rt_eyebrows_03_CTRL.frameSelectAble" "c_Rt_eyebrows_03_FRAME_lockzxfxfyShape.ovdt"
		;
connectAttr "c_Rt_eyebrows_03_FRAME.up_Vis" "c_Rt_eyebrows_03_CTRL_up.v";
connectAttr "c_Rt_eyebrows_03_FRAME.dn_Vis" "c_Rt_eyebrows_03_CTRL_dn.v";
connectAttr "c_Rt_eyebrows_03_FRAME.lf_Vis" "c_Rt_eyebrows_03_CTRL_lf.v";
connectAttr "c_Rt_eyebrows_03_FRAME.lfup_Vis" "c_Rt_eyebrows_03_CTRL_lfup.v";
connectAttr "c_Rt_eyebrows_03_FRAME.rt_Vis" "c_Rt_eyebrows_03_CTRL_rt.v";
connectAttr "c_Rt_eyebrows_03_FRAME.rtup_Vis" "c_Rt_eyebrows_03_CTRL_rtup.v";
connectAttr "c_Rt_eyebrows_03_FRAME.lfdn_Vis" "c_Rt_eyebrows_03_CTRL_lfdn.v";
connectAttr "c_Rt_eyebrows_03_FRAME.rtdn_Vis" "c_Rt_eyebrows_03_CTRL_rtdn.v";
connectAttr "c_Rt_eyebrows_03_FRAME.fourAxis_up_Vis" "c_Rt_eyebrows_03_CTRL_fourAxisup.v"
		;
connectAttr "c_Rt_eyebrows_03_FRAME.fourAxis_dn_Vis" "c_Rt_eyebrows_03_CTRL_fourAxisdn.v"
		;
connectAttr "c_Rt_eyebrows_03_FRAME.fourAxis_lf_Vis" "c_Rt_eyebrows_03_CTRL_fourAxislf.v"
		;
connectAttr "c_Rt_eyebrows_03_FRAME.fourAxis_rt_Vis" "c_Rt_eyebrows_03_CTRL_fourAxisrt.v"
		;
connectAttr "c_nose_upclamp_finalrange.opr" "c_nose_FRAME.up";
connectAttr "c_nose_dnclamp_finalrange.opr" "c_nose_FRAME.dn";
connectAttr "c_nose_lfclamp_finalrange.opr" "c_nose_FRAME.lf";
connectAttr "c_nose_rtclamp_finalrange.opr" "c_nose_FRAME.rt";
connectAttr "c_nose_lfupmult.ox" "c_nose_FRAME.lfup";
connectAttr "c_nose_rtupmult.ox" "c_nose_FRAME.rtup";
connectAttr "c_nose_lfdnmult.ox" "c_nose_FRAME.lfdn";
connectAttr "c_nose_rtdnmult.ox" "c_nose_FRAME.rtdn";
connectAttr "c_nose_lfclamp_NYrange.opr" "c_nose_FRAME.fourAxis_up";
connectAttr "c_nose_lfclamp_PYrange.opr" "c_nose_FRAME.fourAxis_dn";
connectAttr "c_nose_upclamp_PXrange.opr" "c_nose_FRAME.fourAxis_lf";
connectAttr "c_nose_upclamp_NXrange.opr" "c_nose_FRAME.fourAxis_rt";
connectAttr "c_nose_CTRL.frameSelectAble" "c_nose_FRAMEShape.ovdt";
connectAttr "c_nose_CTRL.frameSelectAble" "c_nose_FRAME_lockzyShape.ovdt";
connectAttr "c_nose_CTRL.frameSelectAble" "c_nose_FRAME_lockfyShape.ovdt";
connectAttr "c_nose_CTRL.frameSelectAble" "c_nose_FRAME_lockzxShape.ovdt";
connectAttr "c_nose_CTRL.frameSelectAble" "c_nose_FRAME_lockfxShape.ovdt";
connectAttr "c_nose_CTRL.frameSelectAble" "c_nose_FRAME_lockzyfyShape.ovdt";
connectAttr "c_nose_CTRL.frameSelectAble" "c_nose_FRAME_lockzxfxShape.ovdt";
connectAttr "c_nose_CTRL.frameSelectAble" "c_nose_FRAME_lockzyfyzxShape.ovdt";
connectAttr "c_nose_CTRL.frameSelectAble" "c_nose_FRAME_lockzyfyfxShape.ovdt";
connectAttr "c_nose_CTRL.frameSelectAble" "c_nose_FRAME_lockzxfxzyShape.ovdt";
connectAttr "c_nose_CTRL.frameSelectAble" "c_nose_FRAME_lockzxfxfyShape.ovdt";
connectAttr "c_nose_FRAME.up_Vis" "c_nose_CTRL_up.v";
connectAttr "c_nose_FRAME.dn_Vis" "c_nose_CTRL_dn.v";
connectAttr "c_nose_FRAME.lf_Vis" "c_nose_CTRL_lf.v";
connectAttr "c_nose_FRAME.lfup_Vis" "c_nose_CTRL_lfup.v";
connectAttr "c_nose_FRAME.rt_Vis" "c_nose_CTRL_rt.v";
connectAttr "c_nose_FRAME.rtup_Vis" "c_nose_CTRL_rtup.v";
connectAttr "c_nose_FRAME.lfdn_Vis" "c_nose_CTRL_lfdn.v";
connectAttr "c_nose_FRAME.rtdn_Vis" "c_nose_CTRL_rtdn.v";
connectAttr "c_nose_FRAME.fourAxis_up_Vis" "c_nose_CTRL_fourAxisup.v";
connectAttr "c_nose_FRAME.fourAxis_dn_Vis" "c_nose_CTRL_fourAxisdn.v";
connectAttr "c_nose_FRAME.fourAxis_lf_Vis" "c_nose_CTRL_fourAxislf.v";
connectAttr "c_nose_FRAME.fourAxis_rt_Vis" "c_nose_CTRL_fourAxisrt.v";
connectAttr "c_Lf_eyeStretch_upclamp_finalrange.opr" "c_Lf_cheek_FRAME.up";
connectAttr "c_Lf_eyeStretch_dnclamp_finalrange.opr" "c_Lf_cheek_FRAME.dn";
connectAttr "c_Lf_eyeStretch_lfclamp_finalrange.opr" "c_Lf_cheek_FRAME.lf";
connectAttr "c_Lf_eyeStretch_rtclamp_finalrange.opr" "c_Lf_cheek_FRAME.rt";
connectAttr "c_Lf_eyeStretch_lfupmult.ox" "c_Lf_cheek_FRAME.lfup";
connectAttr "c_Lf_eyeStretch_rtupmult.ox" "c_Lf_cheek_FRAME.rtup";
connectAttr "c_Lf_eyeStretch_lfdnmult.ox" "c_Lf_cheek_FRAME.lfdn";
connectAttr "c_Lf_eyeStretch_rtdnmult.ox" "c_Lf_cheek_FRAME.rtdn";
connectAttr "c_Lf_eyeStretch_lfclamp_NYrange.opr" "c_Lf_cheek_FRAME.fourAxis_up"
		;
connectAttr "c_Lf_eyeStretch_lfclamp_PYrange.opr" "c_Lf_cheek_FRAME.fourAxis_dn"
		;
connectAttr "c_Lf_eyeStretch_upclamp_PXrange.opr" "c_Lf_cheek_FRAME.fourAxis_lf"
		;
connectAttr "c_Lf_eyeStretch_upclamp_NXrange.opr" "c_Lf_cheek_FRAME.fourAxis_rt"
		;
connectAttr "c_Lf_cheek_CTRL.frameSelectAble" "c_Lf_cheek_FRAMEShape.ovdt";
connectAttr "c_Lf_cheek_CTRL.frameSelectAble" "c_Lf_cheek_FRAME_lockzyShape.ovdt"
		;
connectAttr "c_Lf_cheek_CTRL.frameSelectAble" "c_Lf_cheek_FRAME_lockfyShape.ovdt"
		;
connectAttr "c_Lf_cheek_CTRL.frameSelectAble" "c_Lf_cheek_FRAME_lockzxShape.ovdt"
		;
connectAttr "c_Lf_cheek_CTRL.frameSelectAble" "c_Lf_cheek_FRAME_lockfxShape.ovdt"
		;
connectAttr "c_Lf_cheek_CTRL.frameSelectAble" "c_Lf_cheek_FRAME_lockzyfyShape.ovdt"
		;
connectAttr "c_Lf_cheek_CTRL.frameSelectAble" "c_Lf_cheek_FRAME_lockzxfxShape.ovdt"
		;
connectAttr "c_Lf_cheek_CTRL.frameSelectAble" "c_Lf_cheek_FRAME_lockzyfyzxShape.ovdt"
		;
connectAttr "c_Lf_cheek_CTRL.frameSelectAble" "c_Lf_cheek_FRAME_lockzyfyfxShape.ovdt"
		;
connectAttr "c_Lf_cheek_CTRL.frameSelectAble" "c_Lf_cheek_FRAME_lockzxfxzyShape.ovdt"
		;
connectAttr "c_Lf_cheek_CTRL.frameSelectAble" "c_Lf_cheek_FRAME_lockzxfxfyShape.ovdt"
		;
connectAttr "c_Lf_cheek_FRAME.up_Vis" "c_Lf_cheek_CTRL_up.v";
connectAttr "c_Lf_cheek_FRAME.dn_Vis" "c_Lf_cheek_CTRL_dn.v";
connectAttr "c_Lf_cheek_FRAME.lf_Vis" "c_Lf_cheek_CTRL_lf.v";
connectAttr "c_Lf_cheek_FRAME.lfup_Vis" "c_Lf_cheek_CTRL_lfup.v";
connectAttr "c_Lf_cheek_FRAME.rt_Vis" "c_Lf_cheek_CTRL_rt.v";
connectAttr "c_Lf_cheek_FRAME.rtup_Vis" "c_Lf_cheek_CTRL_rtup.v";
connectAttr "c_Lf_cheek_FRAME.lfdn_Vis" "c_Lf_cheek_CTRL_lfdn.v";
connectAttr "c_Lf_cheek_FRAME.rtdn_Vis" "c_Lf_cheek_CTRL_rtdn.v";
connectAttr "c_Lf_cheek_FRAME.fourAxis_up_Vis" "c_Lf_cheek_CTRL_fourAxisup.v";
connectAttr "c_Lf_cheek_FRAME.fourAxis_dn_Vis" "c_Lf_cheek_CTRL_fourAxisdn.v";
connectAttr "c_Lf_cheek_FRAME.fourAxis_lf_Vis" "c_Lf_cheek_CTRL_fourAxislf.v";
connectAttr "c_Lf_cheek_FRAME.fourAxis_rt_Vis" "c_Lf_cheek_CTRL_fourAxisrt.v";
connectAttr "c_Rt_eyeStretch_upclamp_finalrange.opr" "c_Rt_cheek_FRAME.up";
connectAttr "c_Rt_eyeStretch_dnclamp_finalrange.opr" "c_Rt_cheek_FRAME.dn";
connectAttr "c_Rt_eyeStretch_lfclamp_finalrange.opr" "c_Rt_cheek_FRAME.lf";
connectAttr "c_Rt_eyeStretch_rtclamp_finalrange.opr" "c_Rt_cheek_FRAME.rt";
connectAttr "c_Rt_eyeStretch_lfupmult.ox" "c_Rt_cheek_FRAME.lfup";
connectAttr "c_Rt_eyeStretch_rtupmult.ox" "c_Rt_cheek_FRAME.rtup";
connectAttr "c_Rt_eyeStretch_lfdnmult.ox" "c_Rt_cheek_FRAME.lfdn";
connectAttr "c_Rt_eyeStretch_rtdnmult.ox" "c_Rt_cheek_FRAME.rtdn";
connectAttr "c_Rt_eyeStretch_lfclamp_NYrange.opr" "c_Rt_cheek_FRAME.fourAxis_up"
		;
connectAttr "c_Rt_eyeStretch_lfclamp_PYrange.opr" "c_Rt_cheek_FRAME.fourAxis_dn"
		;
connectAttr "c_Rt_eyeStretch_upclamp_PXrange.opr" "c_Rt_cheek_FRAME.fourAxis_lf"
		;
connectAttr "c_Rt_eyeStretch_upclamp_NXrange.opr" "c_Rt_cheek_FRAME.fourAxis_rt"
		;
connectAttr "c_Rt_cheek_CTRL.frameSelectAble" "c_Rt_cheek_FRAMEShape.ovdt";
connectAttr "c_Rt_cheek_CTRL.frameSelectAble" "c_Rt_cheek_FRAME_lockzyShape.ovdt"
		;
connectAttr "c_Rt_cheek_CTRL.frameSelectAble" "c_Rt_cheek_FRAME_lockfyShape.ovdt"
		;
connectAttr "c_Rt_cheek_CTRL.frameSelectAble" "c_Rt_cheek_FRAME_lockzxShape.ovdt"
		;
connectAttr "c_Rt_cheek_CTRL.frameSelectAble" "c_Rt_cheek_FRAME_lockfxShape.ovdt"
		;
connectAttr "c_Rt_cheek_CTRL.frameSelectAble" "c_Rt_cheek_FRAME_lockzyfyShape.ovdt"
		;
connectAttr "c_Rt_cheek_CTRL.frameSelectAble" "c_Rt_cheek_FRAME_lockzxfxShape.ovdt"
		;
connectAttr "c_Rt_cheek_CTRL.frameSelectAble" "c_Rt_cheek_FRAME_lockzyfyzxShape.ovdt"
		;
connectAttr "c_Rt_cheek_CTRL.frameSelectAble" "c_Rt_cheek_FRAME_lockzyfyfxShape.ovdt"
		;
connectAttr "c_Rt_cheek_CTRL.frameSelectAble" "c_Rt_cheek_FRAME_lockzxfxzyShape.ovdt"
		;
connectAttr "c_Rt_cheek_CTRL.frameSelectAble" "c_Rt_cheek_FRAME_lockzxfxfyShape.ovdt"
		;
connectAttr "c_Rt_cheek_FRAME.up_Vis" "c_Rt_cheek_CTRL_up.v";
connectAttr "c_Rt_cheek_FRAME.dn_Vis" "c_Rt_cheek_CTRL_dn.v";
connectAttr "c_Rt_cheek_FRAME.lf_Vis" "c_Rt_cheek_CTRL_lf.v";
connectAttr "c_Rt_cheek_FRAME.lfup_Vis" "c_Rt_cheek_CTRL_lfup.v";
connectAttr "c_Rt_cheek_FRAME.rt_Vis" "c_Rt_cheek_CTRL_rt.v";
connectAttr "c_Rt_cheek_FRAME.rtup_Vis" "c_Rt_cheek_CTRL_rtup.v";
connectAttr "c_Rt_cheek_FRAME.lfdn_Vis" "c_Rt_cheek_CTRL_lfdn.v";
connectAttr "c_Rt_cheek_FRAME.rtdn_Vis" "c_Rt_cheek_CTRL_rtdn.v";
connectAttr "c_Rt_cheek_FRAME.fourAxis_up_Vis" "c_Rt_cheek_CTRL_fourAxisup.v";
connectAttr "c_Rt_cheek_FRAME.fourAxis_dn_Vis" "c_Rt_cheek_CTRL_fourAxisdn.v";
connectAttr "c_Rt_cheek_FRAME.fourAxis_lf_Vis" "c_Rt_cheek_CTRL_fourAxislf.v";
connectAttr "c_Rt_cheek_FRAME.fourAxis_rt_Vis" "c_Rt_cheek_CTRL_fourAxisrt.v";
connectAttr "c_Lf_up_eyelids_upclamp_finalrange.opr" "c_Lf_up_eyelids_FRAME.up";
connectAttr "c_Lf_up_eyelids_dnclamp_finalrange.opr" "c_Lf_up_eyelids_FRAME.dn";
connectAttr "c_Lf_up_eyelids_lfclamp_finalrange.opr" "c_Lf_up_eyelids_FRAME.lf";
connectAttr "c_Lf_up_eyelids_rtclamp_finalrange.opr" "c_Lf_up_eyelids_FRAME.rt";
connectAttr "c_Lf_up_eyelids_lfupmult.ox" "c_Lf_up_eyelids_FRAME.lfup";
connectAttr "c_Lf_up_eyelids_rtupmult.ox" "c_Lf_up_eyelids_FRAME.rtup";
connectAttr "c_Lf_up_eyelids_lfdnmult.ox" "c_Lf_up_eyelids_FRAME.lfdn";
connectAttr "c_Lf_up_eyelids_rtdnmult.ox" "c_Lf_up_eyelids_FRAME.rtdn";
connectAttr "c_Lf_up_eyelids_lfclamp_NYrange.opr" "c_Lf_up_eyelids_FRAME.fourAxis_up"
		;
connectAttr "c_Lf_up_eyelids_lfclamp_PYrange.opr" "c_Lf_up_eyelids_FRAME.fourAxis_dn"
		;
connectAttr "c_Lf_up_eyelids_upclamp_PXrange.opr" "c_Lf_up_eyelids_FRAME.fourAxis_lf"
		;
connectAttr "c_Lf_up_eyelids_upclamp_NXrange.opr" "c_Lf_up_eyelids_FRAME.fourAxis_rt"
		;
connectAttr "c_Lf_up_eyelids_CTRL.frameSelectAble" "c_Lf_up_eyelids_FRAMEShape.ovdt"
		;
connectAttr "c_Lf_up_eyelids_CTRL.frameSelectAble" "c_Lf_up_eyelids_FRAME_lockzyShape.ovdt"
		;
connectAttr "c_Lf_up_eyelids_CTRL.frameSelectAble" "c_Lf_up_eyelids_FRAME_lockfyShape.ovdt"
		;
connectAttr "c_Lf_up_eyelids_CTRL.frameSelectAble" "c_Lf_up_eyelids_FRAME_lockzxShape.ovdt"
		;
connectAttr "c_Lf_up_eyelids_CTRL.frameSelectAble" "c_Lf_up_eyelids_FRAME_lockfxShape.ovdt"
		;
connectAttr "c_Lf_up_eyelids_CTRL.frameSelectAble" "c_Lf_up_eyelids_FRAME_lockzyfyShape.ovdt"
		;
connectAttr "c_Lf_up_eyelids_CTRL.frameSelectAble" "c_Lf_up_eyelids_FRAME_lockzxfxShape.ovdt"
		;
connectAttr "c_Lf_up_eyelids_CTRL.frameSelectAble" "c_Lf_up_eyelids_FRAME_lockzyfyzxShape.ovdt"
		;
connectAttr "c_Lf_up_eyelids_CTRL.frameSelectAble" "c_Lf_up_eyelids_FRAME_lockzyfyfxShape.ovdt"
		;
connectAttr "c_Lf_up_eyelids_CTRL.frameSelectAble" "c_Lf_up_eyelids_FRAME_lockzxfxzyShape.ovdt"
		;
connectAttr "c_Lf_up_eyelids_CTRL.frameSelectAble" "c_Lf_up_eyelids_FRAME_lockzxfxfyShape.ovdt"
		;
connectAttr "c_Lf_up_eyelids_FRAME.up_Vis" "c_Lf_up_eyelids_CTRL_up.v";
connectAttr "c_Lf_up_eyelids_FRAME.dn_Vis" "c_Lf_up_eyelids_CTRL_dn.v";
connectAttr "c_Lf_up_eyelids_FRAME.lf_Vis" "c_Lf_up_eyelids_CTRL_lf.v";
connectAttr "c_Lf_up_eyelids_FRAME.lfup_Vis" "c_Lf_up_eyelids_CTRL_lfup.v";
connectAttr "c_Lf_up_eyelids_FRAME.rt_Vis" "c_Lf_up_eyelids_CTRL_rt.v";
connectAttr "c_Lf_up_eyelids_FRAME.rtup_Vis" "c_Lf_up_eyelids_CTRL_rtup.v";
connectAttr "c_Lf_up_eyelids_FRAME.lfdn_Vis" "c_Lf_up_eyelids_CTRL_lfdn.v";
connectAttr "c_Lf_up_eyelids_FRAME.rtdn_Vis" "c_Lf_up_eyelids_CTRL_rtdn.v";
connectAttr "c_Lf_up_eyelids_FRAME.fourAxis_up_Vis" "c_Lf_up_eyelids_CTRL_fourAxisup.v"
		;
connectAttr "c_Lf_up_eyelids_FRAME.fourAxis_dn_Vis" "c_Lf_up_eyelids_CTRL_fourAxisdn.v"
		;
connectAttr "c_Lf_up_eyelids_FRAME.fourAxis_lf_Vis" "c_Lf_up_eyelids_CTRL_fourAxislf.v"
		;
connectAttr "c_Lf_up_eyelids_FRAME.fourAxis_rt_Vis" "c_Lf_up_eyelids_CTRL_fourAxisrt.v"
		;
connectAttr "c_Lf_dn_eyelids_upclamp_finalrange.opr" "c_Lf_dn_eyelids_FRAME.up";
connectAttr "c_Lf_dn_eyelids_dnclamp_finalrange.opr" "c_Lf_dn_eyelids_FRAME.dn";
connectAttr "c_Lf_dn_eyelids_lfclamp_finalrange.opr" "c_Lf_dn_eyelids_FRAME.lf";
connectAttr "c_Lf_dn_eyelids_rtclamp_finalrange.opr" "c_Lf_dn_eyelids_FRAME.rt";
connectAttr "c_Lf_dn_eyelids_lfupmult.ox" "c_Lf_dn_eyelids_FRAME.lfup";
connectAttr "c_Lf_dn_eyelids_rtupmult.ox" "c_Lf_dn_eyelids_FRAME.rtup";
connectAttr "c_Lf_dn_eyelids_lfdnmult.ox" "c_Lf_dn_eyelids_FRAME.lfdn";
connectAttr "c_Lf_dn_eyelids_rtdnmult.ox" "c_Lf_dn_eyelids_FRAME.rtdn";
connectAttr "c_Lf_dn_eyelids_lfclamp_NYrange.opr" "c_Lf_dn_eyelids_FRAME.fourAxis_up"
		;
connectAttr "c_Lf_dn_eyelids_lfclamp_PYrange.opr" "c_Lf_dn_eyelids_FRAME.fourAxis_dn"
		;
connectAttr "c_Lf_dn_eyelids_upclamp_PXrange.opr" "c_Lf_dn_eyelids_FRAME.fourAxis_lf"
		;
connectAttr "c_Lf_dn_eyelids_upclamp_NXrange.opr" "c_Lf_dn_eyelids_FRAME.fourAxis_rt"
		;
connectAttr "c_Lf_dn_eyelids_CTRL.frameSelectAble" "c_Lf_dn_eyelids_FRAMEShape.ovdt"
		;
connectAttr "c_Lf_dn_eyelids_CTRL.frameSelectAble" "c_Lf_dn_eyelids_FRAME_lockzyShape.ovdt"
		;
connectAttr "c_Lf_dn_eyelids_CTRL.frameSelectAble" "c_Lf_dn_eyelids_FRAME_lockfyShape.ovdt"
		;
connectAttr "c_Lf_dn_eyelids_CTRL.frameSelectAble" "c_Lf_dn_eyelids_FRAME_lockzxShape.ovdt"
		;
connectAttr "c_Lf_dn_eyelids_CTRL.frameSelectAble" "c_Lf_dn_eyelids_FRAME_lockfxShape.ovdt"
		;
connectAttr "c_Lf_dn_eyelids_CTRL.frameSelectAble" "c_Lf_dn_eyelids_FRAME_lockzyfyShape.ovdt"
		;
connectAttr "c_Lf_dn_eyelids_CTRL.frameSelectAble" "c_Lf_dn_eyelids_FRAME_lockzxfxShape.ovdt"
		;
connectAttr "c_Lf_dn_eyelids_CTRL.frameSelectAble" "c_Lf_dn_eyelids_FRAME_lockzyfyzxShape.ovdt"
		;
connectAttr "c_Lf_dn_eyelids_CTRL.frameSelectAble" "c_Lf_dn_eyelids_FRAME_lockzyfyfxShape.ovdt"
		;
connectAttr "c_Lf_dn_eyelids_CTRL.frameSelectAble" "c_Lf_dn_eyelids_FRAME_lockzxfxzyShape.ovdt"
		;
connectAttr "c_Lf_dn_eyelids_CTRL.frameSelectAble" "c_Lf_dn_eyelids_FRAME_lockzxfxfyShape.ovdt"
		;
connectAttr "c_Lf_dn_eyelids_FRAME.up_Vis" "c_Lf_dn_eyelids_CTRL_up.v";
connectAttr "c_Lf_dn_eyelids_FRAME.dn_Vis" "c_Lf_dn_eyelids_CTRL_dn.v";
connectAttr "c_Lf_dn_eyelids_FRAME.lf_Vis" "c_Lf_dn_eyelids_CTRL_lf.v";
connectAttr "c_Lf_dn_eyelids_FRAME.lfup_Vis" "c_Lf_dn_eyelids_CTRL_lfup.v";
connectAttr "c_Lf_dn_eyelids_FRAME.rt_Vis" "c_Lf_dn_eyelids_CTRL_rt.v";
connectAttr "c_Lf_dn_eyelids_FRAME.rtup_Vis" "c_Lf_dn_eyelids_CTRL_rtup.v";
connectAttr "c_Lf_dn_eyelids_FRAME.lfdn_Vis" "c_Lf_dn_eyelids_CTRL_lfdn.v";
connectAttr "c_Lf_dn_eyelids_FRAME.rtdn_Vis" "c_Lf_dn_eyelids_CTRL_rtdn.v";
connectAttr "c_Lf_dn_eyelids_FRAME.fourAxis_up_Vis" "c_Lf_dn_eyelids_CTRL_fourAxisup.v"
		;
connectAttr "c_Lf_dn_eyelids_FRAME.fourAxis_dn_Vis" "c_Lf_dn_eyelids_CTRL_fourAxisdn.v"
		;
connectAttr "c_Lf_dn_eyelids_FRAME.fourAxis_lf_Vis" "c_Lf_dn_eyelids_CTRL_fourAxislf.v"
		;
connectAttr "c_Lf_dn_eyelids_FRAME.fourAxis_rt_Vis" "c_Lf_dn_eyelids_CTRL_fourAxisrt.v"
		;
connectAttr "c_Rt_up_eyelids_upclamp_finalrange.opr" "c_Rt_up_eyelids_FRAME.up";
connectAttr "c_Rt_up_eyelids_dnclamp_finalrange.opr" "c_Rt_up_eyelids_FRAME.dn";
connectAttr "c_Rt_up_eyelids_lfclamp_finalrange.opr" "c_Rt_up_eyelids_FRAME.lf";
connectAttr "c_Rt_up_eyelids_rtclamp_finalrange.opr" "c_Rt_up_eyelids_FRAME.rt";
connectAttr "c_Rt_up_eyelids_lfupmult.ox" "c_Rt_up_eyelids_FRAME.lfup";
connectAttr "c_Rt_up_eyelids_rtupmult.ox" "c_Rt_up_eyelids_FRAME.rtup";
connectAttr "c_Rt_up_eyelids_lfdnmult.ox" "c_Rt_up_eyelids_FRAME.lfdn";
connectAttr "c_Rt_up_eyelids_rtdnmult.ox" "c_Rt_up_eyelids_FRAME.rtdn";
connectAttr "c_Rt_up_eyelids_lfclamp_NYrange.opr" "c_Rt_up_eyelids_FRAME.fourAxis_up"
		;
connectAttr "c_Rt_up_eyelids_lfclamp_PYrange.opr" "c_Rt_up_eyelids_FRAME.fourAxis_dn"
		;
connectAttr "c_Rt_up_eyelids_upclamp_PXrange.opr" "c_Rt_up_eyelids_FRAME.fourAxis_lf"
		;
connectAttr "c_Rt_up_eyelids_upclamp_NXrange.opr" "c_Rt_up_eyelids_FRAME.fourAxis_rt"
		;
connectAttr "c_Rt_up_eyelids_CTRL.frameSelectAble" "c_Rt_up_eyelids_FRAMEShape.ovdt"
		;
connectAttr "c_Rt_up_eyelids_CTRL.frameSelectAble" "c_Rt_up_eyelids_FRAME_lockzyShape.ovdt"
		;
connectAttr "c_Rt_up_eyelids_CTRL.frameSelectAble" "c_Rt_up_eyelids_FRAME_lockfyShape.ovdt"
		;
connectAttr "c_Rt_up_eyelids_CTRL.frameSelectAble" "c_Rt_up_eyelids_FRAME_lockzxShape.ovdt"
		;
connectAttr "c_Rt_up_eyelids_CTRL.frameSelectAble" "c_Rt_up_eyelids_FRAME_lockfxShape.ovdt"
		;
connectAttr "c_Rt_up_eyelids_CTRL.frameSelectAble" "c_Rt_up_eyelids_FRAME_lockzyfyShape.ovdt"
		;
connectAttr "c_Rt_up_eyelids_CTRL.frameSelectAble" "c_Rt_up_eyelids_FRAME_lockzxfxShape.ovdt"
		;
connectAttr "c_Rt_up_eyelids_CTRL.frameSelectAble" "c_Rt_up_eyelids_FRAME_lockzyfyzxShape.ovdt"
		;
connectAttr "c_Rt_up_eyelids_CTRL.frameSelectAble" "c_Rt_up_eyelids_FRAME_lockzyfyfxShape.ovdt"
		;
connectAttr "c_Rt_up_eyelids_CTRL.frameSelectAble" "c_Rt_up_eyelids_FRAME_lockzxfxzyShape.ovdt"
		;
connectAttr "c_Rt_up_eyelids_CTRL.frameSelectAble" "c_Rt_up_eyelids_FRAME_lockzxfxfyShape.ovdt"
		;
connectAttr "c_Rt_up_eyelids_FRAME.up_Vis" "c_Rt_up_eyelids_CTRL_up.v";
connectAttr "c_Rt_up_eyelids_FRAME.dn_Vis" "c_Rt_up_eyelids_CTRL_dn.v";
connectAttr "c_Rt_up_eyelids_FRAME.lf_Vis" "c_Rt_up_eyelids_CTRL_lf.v";
connectAttr "c_Rt_up_eyelids_FRAME.lfup_Vis" "c_Rt_up_eyelids_CTRL_lfup.v";
connectAttr "c_Rt_up_eyelids_FRAME.rt_Vis" "c_Rt_up_eyelids_CTRL_rt.v";
connectAttr "c_Rt_up_eyelids_FRAME.rtup_Vis" "c_Rt_up_eyelids_CTRL_rtup.v";
connectAttr "c_Rt_up_eyelids_FRAME.lfdn_Vis" "c_Rt_up_eyelids_CTRL_lfdn.v";
connectAttr "c_Rt_up_eyelids_FRAME.rtdn_Vis" "c_Rt_up_eyelids_CTRL_rtdn.v";
connectAttr "c_Rt_up_eyelids_FRAME.fourAxis_up_Vis" "c_Rt_up_eyelids_CTRL_fourAxisup.v"
		;
connectAttr "c_Rt_up_eyelids_FRAME.fourAxis_dn_Vis" "c_Rt_up_eyelids_CTRL_fourAxisdn.v"
		;
connectAttr "c_Rt_up_eyelids_FRAME.fourAxis_lf_Vis" "c_Rt_up_eyelids_CTRL_fourAxislf.v"
		;
connectAttr "c_Rt_up_eyelids_FRAME.fourAxis_rt_Vis" "c_Rt_up_eyelids_CTRL_fourAxisrt.v"
		;
connectAttr "c_Rt_dn_eyelids_upclamp_finalrange.opr" "c_Rt_dn_eyelids_FRAME.up";
connectAttr "c_Rt_dn_eyelids_dnclamp_finalrange.opr" "c_Rt_dn_eyelids_FRAME.dn";
connectAttr "c_Rt_dn_eyelids_lfclamp_finalrange.opr" "c_Rt_dn_eyelids_FRAME.lf";
connectAttr "c_Rt_dn_eyelids_rtclamp_finalrange.opr" "c_Rt_dn_eyelids_FRAME.rt";
connectAttr "c_Rt_dn_eyelids_lfupmult.ox" "c_Rt_dn_eyelids_FRAME.lfup";
connectAttr "c_Rt_dn_eyelids_rtupmult.ox" "c_Rt_dn_eyelids_FRAME.rtup";
connectAttr "c_Rt_dn_eyelids_lfdnmult.ox" "c_Rt_dn_eyelids_FRAME.lfdn";
connectAttr "c_Rt_dn_eyelids_rtdnmult.ox" "c_Rt_dn_eyelids_FRAME.rtdn";
connectAttr "c_Rt_dn_eyelids_lfclamp_NYrange.opr" "c_Rt_dn_eyelids_FRAME.fourAxis_up"
		;
connectAttr "c_Rt_dn_eyelids_lfclamp_PYrange.opr" "c_Rt_dn_eyelids_FRAME.fourAxis_dn"
		;
connectAttr "c_Rt_dn_eyelids_upclamp_PXrange.opr" "c_Rt_dn_eyelids_FRAME.fourAxis_lf"
		;
connectAttr "c_Rt_dn_eyelids_upclamp_NXrange.opr" "c_Rt_dn_eyelids_FRAME.fourAxis_rt"
		;
connectAttr "c_Rt_dn_eyelids_CTRL.frameSelectAble" "c_Rt_dn_eyelids_FRAMEShape.ovdt"
		;
connectAttr "c_Rt_dn_eyelids_CTRL.frameSelectAble" "c_Rt_dn_eyelids_FRAME_lockzyShape.ovdt"
		;
connectAttr "c_Rt_dn_eyelids_CTRL.frameSelectAble" "c_Rt_dn_eyelids_FRAME_lockfyShape.ovdt"
		;
connectAttr "c_Rt_dn_eyelids_CTRL.frameSelectAble" "c_Rt_dn_eyelids_FRAME_lockzxShape.ovdt"
		;
connectAttr "c_Rt_dn_eyelids_CTRL.frameSelectAble" "c_Rt_dn_eyelids_FRAME_lockfxShape.ovdt"
		;
connectAttr "c_Rt_dn_eyelids_CTRL.frameSelectAble" "c_Rt_dn_eyelids_FRAME_lockzyfyShape.ovdt"
		;
connectAttr "c_Rt_dn_eyelids_CTRL.frameSelectAble" "c_Rt_dn_eyelids_FRAME_lockzxfxShape.ovdt"
		;
connectAttr "c_Rt_dn_eyelids_CTRL.frameSelectAble" "c_Rt_dn_eyelids_FRAME_lockzyfyzxShape.ovdt"
		;
connectAttr "c_Rt_dn_eyelids_CTRL.frameSelectAble" "c_Rt_dn_eyelids_FRAME_lockzyfyfxShape.ovdt"
		;
connectAttr "c_Rt_dn_eyelids_CTRL.frameSelectAble" "c_Rt_dn_eyelids_FRAME_lockzxfxzyShape.ovdt"
		;
connectAttr "c_Rt_dn_eyelids_CTRL.frameSelectAble" "c_Rt_dn_eyelids_FRAME_lockzxfxfyShape.ovdt"
		;
connectAttr "c_Rt_dn_eyelids_FRAME.up_Vis" "c_Rt_dn_eyelids_CTRL_up.v";
connectAttr "c_Rt_dn_eyelids_FRAME.dn_Vis" "c_Rt_dn_eyelids_CTRL_dn.v";
connectAttr "c_Rt_dn_eyelids_FRAME.lf_Vis" "c_Rt_dn_eyelids_CTRL_lf.v";
connectAttr "c_Rt_dn_eyelids_FRAME.lfup_Vis" "c_Rt_dn_eyelids_CTRL_lfup.v";
connectAttr "c_Rt_dn_eyelids_FRAME.rt_Vis" "c_Rt_dn_eyelids_CTRL_rt.v";
connectAttr "c_Rt_dn_eyelids_FRAME.rtup_Vis" "c_Rt_dn_eyelids_CTRL_rtup.v";
connectAttr "c_Rt_dn_eyelids_FRAME.lfdn_Vis" "c_Rt_dn_eyelids_CTRL_lfdn.v";
connectAttr "c_Rt_dn_eyelids_FRAME.rtdn_Vis" "c_Rt_dn_eyelids_CTRL_rtdn.v";
connectAttr "c_Rt_dn_eyelids_FRAME.fourAxis_up_Vis" "c_Rt_dn_eyelids_CTRL_fourAxisup.v"
		;
connectAttr "c_Rt_dn_eyelids_FRAME.fourAxis_dn_Vis" "c_Rt_dn_eyelids_CTRL_fourAxisdn.v"
		;
connectAttr "c_Rt_dn_eyelids_FRAME.fourAxis_lf_Vis" "c_Rt_dn_eyelids_CTRL_fourAxislf.v"
		;
connectAttr "c_Rt_dn_eyelids_FRAME.fourAxis_rt_Vis" "c_Rt_dn_eyelids_CTRL_fourAxisrt.v"
		;
connectAttr "c_jaw_dn_upclamp_finalrange.opr" "c_jaw_dn_FRAME.up";
connectAttr "c_jaw_dn_dnclamp_finalrange.opr" "c_jaw_dn_FRAME.dn";
connectAttr "c_jaw_dn_lfclamp_finalrange.opr" "c_jaw_dn_FRAME.lf";
connectAttr "c_jaw_dn_rtclamp_finalrange.opr" "c_jaw_dn_FRAME.rt";
connectAttr "c_jaw_dn_lfupmult.ox" "c_jaw_dn_FRAME.lfup";
connectAttr "c_jaw_dn_rtupmult.ox" "c_jaw_dn_FRAME.rtup";
connectAttr "c_jaw_dn_lfdnmult.ox" "c_jaw_dn_FRAME.lfdn";
connectAttr "c_jaw_dn_rtdnmult.ox" "c_jaw_dn_FRAME.rtdn";
connectAttr "c_jaw_dn_lfclamp_NYrange.opr" "c_jaw_dn_FRAME.fourAxis_up";
connectAttr "c_jaw_dn_lfclamp_PYrange.opr" "c_jaw_dn_FRAME.fourAxis_dn";
connectAttr "c_jaw_dn_upclamp_PXrange.opr" "c_jaw_dn_FRAME.fourAxis_lf";
connectAttr "c_jaw_dn_upclamp_NXrange.opr" "c_jaw_dn_FRAME.fourAxis_rt";
connectAttr "c_jaw_dn_CTRL.frameSelectAble" "c_jaw_dn_FRAMEShape.ovdt";
connectAttr "c_dn_mouthLip_upclamp_finalrange.opr" "c_dn_mouthLip_FRAME.up";
connectAttr "c_dn_mouthLip_dnclamp_finalrange.opr" "c_dn_mouthLip_FRAME.dn";
connectAttr "c_dn_mouthLip_lfclamp_finalrange.opr" "c_dn_mouthLip_FRAME.lf";
connectAttr "c_dn_mouthLip_rtclamp_finalrange.opr" "c_dn_mouthLip_FRAME.rt";
connectAttr "c_dn_mouthLip_lfupmult.ox" "c_dn_mouthLip_FRAME.lfup";
connectAttr "c_dn_mouthLip_rtupmult.ox" "c_dn_mouthLip_FRAME.rtup";
connectAttr "c_dn_mouthLip_lfdnmult.ox" "c_dn_mouthLip_FRAME.lfdn";
connectAttr "c_dn_mouthLip_rtdnmult.ox" "c_dn_mouthLip_FRAME.rtdn";
connectAttr "c_dn_mouthLip_lfclamp_NYrange.opr" "c_dn_mouthLip_FRAME.fourAxis_up"
		;
connectAttr "c_dn_mouthLip_lfclamp_PYrange.opr" "c_dn_mouthLip_FRAME.fourAxis_dn"
		;
connectAttr "c_dn_mouthLip_upclamp_PXrange.opr" "c_dn_mouthLip_FRAME.fourAxis_lf"
		;
connectAttr "c_dn_mouthLip_upclamp_NXrange.opr" "c_dn_mouthLip_FRAME.fourAxis_rt"
		;
connectAttr "c_dn_mouthLip_CTRL.frameSelectAble" "c_dn_mouthLip_FRAMEShape.ovdt"
		;
connectAttr "c_dn_mouthLip_CTRL.frameSelectAble" "c_dn_mouthLip_FRAME_lockzyShape.ovdt"
		;
connectAttr "c_dn_mouthLip_CTRL.frameSelectAble" "c_dn_mouthLip_FRAME_lockfyShape.ovdt"
		;
connectAttr "c_dn_mouthLip_CTRL.frameSelectAble" "c_dn_mouthLip_FRAME_lockzxShape.ovdt"
		;
connectAttr "c_dn_mouthLip_CTRL.frameSelectAble" "c_dn_mouthLip_FRAME_lockfxShape.ovdt"
		;
connectAttr "c_dn_mouthLip_CTRL.frameSelectAble" "c_dn_mouthLip_FRAME_lockzyfyShape.ovdt"
		;
connectAttr "c_dn_mouthLip_CTRL.frameSelectAble" "c_dn_mouthLip_FRAME_lockzxfxShape.ovdt"
		;
connectAttr "c_dn_mouthLip_CTRL.frameSelectAble" "c_dn_mouthLip_FRAME_lockzyfyzxShape.ovdt"
		;
connectAttr "c_dn_mouthLip_CTRL.frameSelectAble" "c_dn_mouthLip_FRAME_lockzyfyfxShape.ovdt"
		;
connectAttr "c_dn_mouthLip_CTRL.frameSelectAble" "c_dn_mouthLip_FRAME_lockzxfxzyShape.ovdt"
		;
connectAttr "c_dn_mouthLip_CTRL.frameSelectAble" "c_dn_mouthLip_FRAME_lockzxfxfyShape.ovdt"
		;
connectAttr "c_dn_mouthLip_FRAME.up_Vis" "c_dn_mouthLip_CTRL_up.v";
connectAttr "c_dn_mouthLip_FRAME.dn_Vis" "c_dn_mouthLip_CTRL_dn.v";
connectAttr "c_dn_mouthLip_FRAME.lf_Vis" "c_dn_mouthLip_CTRL_lf.v";
connectAttr "c_dn_mouthLip_FRAME.lfup_Vis" "c_dn_mouthLip_CTRL_lfup.v";
connectAttr "c_dn_mouthLip_FRAME.rt_Vis" "c_dn_mouthLip_CTRL_rt.v";
connectAttr "c_dn_mouthLip_FRAME.rtup_Vis" "c_dn_mouthLip_CTRL_rtup.v";
connectAttr "c_dn_mouthLip_FRAME.lfdn_Vis" "c_dn_mouthLip_CTRL_lfdn.v";
connectAttr "c_dn_mouthLip_FRAME.rtdn_Vis" "c_dn_mouthLip_CTRL_rtdn.v";
connectAttr "c_dn_mouthLip_FRAME.fourAxis_up_Vis" "c_dn_mouthLip_CTRL_fourAxisup.v"
		;
connectAttr "c_dn_mouthLip_FRAME.fourAxis_dn_Vis" "c_dn_mouthLip_CTRL_fourAxisdn.v"
		;
connectAttr "c_dn_mouthLip_FRAME.fourAxis_lf_Vis" "c_dn_mouthLip_CTRL_fourAxislf.v"
		;
connectAttr "c_dn_mouthLip_FRAME.fourAxis_rt_Vis" "c_dn_mouthLip_CTRL_fourAxisrt.v"
		;
connectAttr "c_jaw_dn_CTRL.frameSelectAble" "c_jaw_dn_FRAME_lockzyShape.ovdt";
connectAttr "c_jaw_dn_CTRL.frameSelectAble" "c_jaw_dn_FRAME_lockfyShape.ovdt";
connectAttr "c_jaw_dn_CTRL.frameSelectAble" "c_jaw_dn_FRAME_lockzxShape.ovdt";
connectAttr "c_jaw_dn_CTRL.frameSelectAble" "c_jaw_dn_FRAME_lockfxShape.ovdt";
connectAttr "c_jaw_dn_CTRL.frameSelectAble" "c_jaw_dn_FRAME_lockzyfyShape.ovdt";
connectAttr "c_jaw_dn_CTRL.frameSelectAble" "c_jaw_dn_FRAME_lockzxfxShape.ovdt";
connectAttr "c_jaw_dn_CTRL.frameSelectAble" "c_jaw_dn_FRAME_lockzyfyzxShape.ovdt"
		;
connectAttr "c_jaw_dn_CTRL.frameSelectAble" "c_jaw_dn_FRAME_lockzyfyfxShape.ovdt"
		;
connectAttr "c_jaw_dn_CTRL.frameSelectAble" "c_jaw_dn_FRAME_lockzxfxzyShape.ovdt"
		;
connectAttr "c_jaw_dn_CTRL.frameSelectAble" "c_jaw_dn_FRAME_lockzxfxfyShape.ovdt"
		;
connectAttr "c_jaw_dn_FRAME.up_Vis" "c_jaw_dn_CTRL_up.v";
connectAttr "c_jaw_dn_FRAME.dn_Vis" "c_jaw_dn_CTRL_dn.v";
connectAttr "c_jaw_dn_FRAME.lf_Vis" "c_jaw_dn_CTRL_lf.v";
connectAttr "c_jaw_dn_FRAME.lfup_Vis" "c_jaw_dn_CTRL_lfup.v";
connectAttr "c_jaw_dn_FRAME.rt_Vis" "c_jaw_dn_CTRL_rt.v";
connectAttr "c_jaw_dn_FRAME.rtup_Vis" "c_jaw_dn_CTRL_rtup.v";
connectAttr "c_jaw_dn_FRAME.lfdn_Vis" "c_jaw_dn_CTRL_lfdn.v";
connectAttr "c_jaw_dn_FRAME.rtdn_Vis" "c_jaw_dn_CTRL_rtdn.v";
connectAttr "c_jaw_dn_FRAME.fourAxis_up_Vis" "c_jaw_dn_CTRL_fourAxisup.v";
connectAttr "c_jaw_dn_FRAME.fourAxis_dn_Vis" "c_jaw_dn_CTRL_fourAxisdn.v";
connectAttr "c_jaw_dn_FRAME.fourAxis_lf_Vis" "c_jaw_dn_CTRL_fourAxislf.v";
connectAttr "c_jaw_dn_FRAME.fourAxis_rt_Vis" "c_jaw_dn_CTRL_fourAxisrt.v";
connectAttr "c_up_mouthLip_upclamp_finalrange.opr" "c_up_mouthLip_FRAME.up";
connectAttr "c_up_mouthLip_dnclamp_finalrange.opr" "c_up_mouthLip_FRAME.dn";
connectAttr "c_up_mouthLip_lfclamp_finalrange.opr" "c_up_mouthLip_FRAME.lf";
connectAttr "c_up_mouthLip_rtclamp_finalrange.opr" "c_up_mouthLip_FRAME.rt";
connectAttr "c_up_mouthLip_lfupmult.ox" "c_up_mouthLip_FRAME.lfup";
connectAttr "c_up_mouthLip_rtupmult.ox" "c_up_mouthLip_FRAME.rtup";
connectAttr "c_up_mouthLip_lfdnmult.ox" "c_up_mouthLip_FRAME.lfdn";
connectAttr "c_up_mouthLip_rtdnmult.ox" "c_up_mouthLip_FRAME.rtdn";
connectAttr "c_up_mouthLip_lfclamp_NYrange.opr" "c_up_mouthLip_FRAME.fourAxis_up"
		;
connectAttr "c_up_mouthLip_lfclamp_PYrange.opr" "c_up_mouthLip_FRAME.fourAxis_dn"
		;
connectAttr "c_up_mouthLip_upclamp_PXrange.opr" "c_up_mouthLip_FRAME.fourAxis_lf"
		;
connectAttr "c_up_mouthLip_upclamp_NXrange.opr" "c_up_mouthLip_FRAME.fourAxis_rt"
		;
connectAttr "c_up_mouthLip_CTRL.frameSelectAble" "c_up_mouthLip_FRAMEShape.ovdt"
		;
connectAttr "c_up_mouthLip_CTRL.frameSelectAble" "c_up_mouthLip_FRAME_lockzyShape.ovdt"
		;
connectAttr "c_up_mouthLip_CTRL.frameSelectAble" "c_up_mouthLip_FRAME_lockfyShape.ovdt"
		;
connectAttr "c_up_mouthLip_CTRL.frameSelectAble" "c_up_mouthLip_FRAME_lockzxShape.ovdt"
		;
connectAttr "c_up_mouthLip_CTRL.frameSelectAble" "c_up_mouthLip_FRAME_lockfxShape.ovdt"
		;
connectAttr "c_up_mouthLip_CTRL.frameSelectAble" "c_up_mouthLip_FRAME_lockzyfyShape.ovdt"
		;
connectAttr "c_up_mouthLip_CTRL.frameSelectAble" "c_up_mouthLip_FRAME_lockzxfxShape.ovdt"
		;
connectAttr "c_up_mouthLip_CTRL.frameSelectAble" "c_up_mouthLip_FRAME_lockzyfyzxShape.ovdt"
		;
connectAttr "c_up_mouthLip_CTRL.frameSelectAble" "c_up_mouthLip_FRAME_lockzyfyfxShape.ovdt"
		;
connectAttr "c_up_mouthLip_CTRL.frameSelectAble" "c_up_mouthLip_FRAME_lockzxfxzyShape.ovdt"
		;
connectAttr "c_up_mouthLip_CTRL.frameSelectAble" "c_up_mouthLip_FRAME_lockzxfxfyShape.ovdt"
		;
connectAttr "c_up_mouthLip_FRAME.up_Vis" "c_up_mouthLip_CTRL_up.v";
connectAttr "c_up_mouthLip_FRAME.dn_Vis" "c_up_mouthLip_CTRL_dn.v";
connectAttr "c_up_mouthLip_FRAME.lf_Vis" "c_up_mouthLip_CTRL_lf.v";
connectAttr "c_up_mouthLip_FRAME.lfup_Vis" "c_up_mouthLip_CTRL_lfup.v";
connectAttr "c_up_mouthLip_FRAME.rt_Vis" "c_up_mouthLip_CTRL_rt.v";
connectAttr "c_up_mouthLip_FRAME.rtup_Vis" "c_up_mouthLip_CTRL_rtup.v";
connectAttr "c_up_mouthLip_FRAME.lfdn_Vis" "c_up_mouthLip_CTRL_lfdn.v";
connectAttr "c_up_mouthLip_FRAME.rtdn_Vis" "c_up_mouthLip_CTRL_rtdn.v";
connectAttr "c_up_mouthLip_FRAME.fourAxis_up_Vis" "c_up_mouthLip_CTRL_fourAxisup.v"
		;
connectAttr "c_up_mouthLip_FRAME.fourAxis_dn_Vis" "c_up_mouthLip_CTRL_fourAxisdn.v"
		;
connectAttr "c_up_mouthLip_FRAME.fourAxis_lf_Vis" "c_up_mouthLip_CTRL_fourAxislf.v"
		;
connectAttr "c_up_mouthLip_FRAME.fourAxis_rt_Vis" "c_up_mouthLip_CTRL_fourAxisrt.v"
		;
connectAttr "c_Lf_mouthLip_upclamp_finalrange.opr" "c_Lf_mouthLip_FRAME.up";
connectAttr "c_Lf_mouthLip_dnclamp_finalrange.opr" "c_Lf_mouthLip_FRAME.dn";
connectAttr "c_Lf_mouthLip_lfclamp_finalrange.opr" "c_Lf_mouthLip_FRAME.lf";
connectAttr "c_Lf_mouthLip_rtclamp_finalrange.opr" "c_Lf_mouthLip_FRAME.rt";
connectAttr "c_Lf_mouthLip_lfupmult.ox" "c_Lf_mouthLip_FRAME.lfup";
connectAttr "c_Lf_mouthLip_rtupmult.ox" "c_Lf_mouthLip_FRAME.rtup";
connectAttr "c_Lf_mouthLip_lfdnmult.ox" "c_Lf_mouthLip_FRAME.lfdn";
connectAttr "c_Lf_mouthLip_rtdnmult.ox" "c_Lf_mouthLip_FRAME.rtdn";
connectAttr "c_Lf_mouthLip_lfclamp_NYrange.opr" "c_Lf_mouthLip_FRAME.fourAxis_up"
		;
connectAttr "c_Lf_mouthLip_lfclamp_PYrange.opr" "c_Lf_mouthLip_FRAME.fourAxis_dn"
		;
connectAttr "c_Lf_mouthLip_upclamp_PXrange.opr" "c_Lf_mouthLip_FRAME.fourAxis_lf"
		;
connectAttr "c_Lf_mouthLip_upclamp_NXrange.opr" "c_Lf_mouthLip_FRAME.fourAxis_rt"
		;
connectAttr "c_Lf_mouthLip_CTRL.frameSelectAble" "c_Lf_mouthLip_FRAMEShape.ovdt"
		;
connectAttr "c_Lf_mouthLip_CTRL.frameSelectAble" "c_Lf_mouthLip_FRAME_lockzyShape.ovdt"
		;
connectAttr "c_Lf_mouthLip_CTRL.frameSelectAble" "c_Lf_mouthLip_FRAME_lockfyShape.ovdt"
		;
connectAttr "c_Lf_mouthLip_CTRL.frameSelectAble" "c_Lf_mouthLip_FRAME_lockzxShape.ovdt"
		;
connectAttr "c_Lf_mouthLip_CTRL.frameSelectAble" "c_Lf_mouthLip_FRAME_lockfxShape.ovdt"
		;
connectAttr "c_Lf_mouthLip_CTRL.frameSelectAble" "c_Lf_mouthLip_FRAME_lockzyfyShape.ovdt"
		;
connectAttr "c_Lf_mouthLip_CTRL.frameSelectAble" "c_Lf_mouthLip_FRAME_lockzxfxShape.ovdt"
		;
connectAttr "c_Lf_mouthLip_CTRL.frameSelectAble" "c_Lf_mouthLip_FRAME_lockzyfyzxShape.ovdt"
		;
connectAttr "c_Lf_mouthLip_CTRL.frameSelectAble" "c_Lf_mouthLip_FRAME_lockzyfyfxShape.ovdt"
		;
connectAttr "c_Lf_mouthLip_CTRL.frameSelectAble" "c_Lf_mouthLip_FRAME_lockzxfxzyShape.ovdt"
		;
connectAttr "c_Lf_mouthLip_CTRL.frameSelectAble" "c_Lf_mouthLip_FRAME_lockzxfxfyShape.ovdt"
		;
connectAttr "c_Lf_mouthLip_FRAME.up_Vis" "c_Lf_mouthLip_CTRL_up.v";
connectAttr "c_Lf_mouthLip_FRAME.dn_Vis" "c_Lf_mouthLip_CTRL_dn.v";
connectAttr "c_Lf_mouthLip_FRAME.lf_Vis" "c_Lf_mouthLip_CTRL_lf.v";
connectAttr "c_Lf_mouthLip_FRAME.lfup_Vis" "c_Lf_mouthLip_CTRL_lfup.v";
connectAttr "c_Lf_mouthLip_FRAME.rt_Vis" "c_Lf_mouthLip_CTRL_rt.v";
connectAttr "c_Lf_mouthLip_FRAME.rtup_Vis" "c_Lf_mouthLip_CTRL_rtup.v";
connectAttr "c_Lf_mouthLip_FRAME.lfdn_Vis" "c_Lf_mouthLip_CTRL_lfdn.v";
connectAttr "c_Lf_mouthLip_FRAME.rtdn_Vis" "c_Lf_mouthLip_CTRL_rtdn.v";
connectAttr "c_Lf_mouthLip_FRAME.fourAxis_up_Vis" "c_Lf_mouthLip_CTRL_fourAxisup.v"
		;
connectAttr "c_Lf_mouthLip_FRAME.fourAxis_dn_Vis" "c_Lf_mouthLip_CTRL_fourAxisdn.v"
		;
connectAttr "c_Lf_mouthLip_FRAME.fourAxis_lf_Vis" "c_Lf_mouthLip_CTRL_fourAxislf.v"
		;
connectAttr "c_Lf_mouthLip_FRAME.fourAxis_rt_Vis" "c_Lf_mouthLip_CTRL_fourAxisrt.v"
		;
connectAttr "c_Rt_mouthLip_upclamp_finalrange.opr" "c_Rt_mouthLip_FRAME.up";
connectAttr "c_Rt_mouthLip_dnclamp_finalrange.opr" "c_Rt_mouthLip_FRAME.dn";
connectAttr "c_Rt_mouthLip_lfclamp_finalrange.opr" "c_Rt_mouthLip_FRAME.lf";
connectAttr "c_Rt_mouthLip_rtclamp_finalrange.opr" "c_Rt_mouthLip_FRAME.rt";
connectAttr "c_Rt_mouthLip_lfupmult.ox" "c_Rt_mouthLip_FRAME.lfup";
connectAttr "c_Rt_mouthLip_rtupmult.ox" "c_Rt_mouthLip_FRAME.rtup";
connectAttr "c_Rt_mouthLip_lfdnmult.ox" "c_Rt_mouthLip_FRAME.lfdn";
connectAttr "c_Rt_mouthLip_rtdnmult.ox" "c_Rt_mouthLip_FRAME.rtdn";
connectAttr "c_Rt_mouthLip_lfclamp_NYrange.opr" "c_Rt_mouthLip_FRAME.fourAxis_up"
		;
connectAttr "c_Rt_mouthLip_lfclamp_PYrange.opr" "c_Rt_mouthLip_FRAME.fourAxis_dn"
		;
connectAttr "c_Rt_mouthLip_upclamp_PXrange.opr" "c_Rt_mouthLip_FRAME.fourAxis_lf"
		;
connectAttr "c_Rt_mouthLip_upclamp_NXrange.opr" "c_Rt_mouthLip_FRAME.fourAxis_rt"
		;
connectAttr "c_Rt_mouthLip_CTRL.frameSelectAble" "c_Rt_mouthLip_FRAMEShape.ovdt"
		;
connectAttr "c_Rt_mouthLip_CTRL.frameSelectAble" "c_Rt_mouthLip_FRAME_lockzyShape.ovdt"
		;
connectAttr "c_Rt_mouthLip_CTRL.frameSelectAble" "c_Rt_mouthLip_FRAME_lockfyShape.ovdt"
		;
connectAttr "c_Rt_mouthLip_CTRL.frameSelectAble" "c_Rt_mouthLip_FRAME_lockzxShape.ovdt"
		;
connectAttr "c_Rt_mouthLip_CTRL.frameSelectAble" "c_Rt_mouthLip_FRAME_lockfxShape.ovdt"
		;
connectAttr "c_Rt_mouthLip_CTRL.frameSelectAble" "c_Rt_mouthLip_FRAME_lockzyfyShape.ovdt"
		;
connectAttr "c_Rt_mouthLip_CTRL.frameSelectAble" "c_Rt_mouthLip_FRAME_lockzxfxShape.ovdt"
		;
connectAttr "c_Rt_mouthLip_CTRL.frameSelectAble" "c_Rt_mouthLip_FRAME_lockzyfyzxShape.ovdt"
		;
connectAttr "c_Rt_mouthLip_CTRL.frameSelectAble" "c_Rt_mouthLip_FRAME_lockzyfyfxShape.ovdt"
		;
connectAttr "c_Rt_mouthLip_CTRL.frameSelectAble" "c_Rt_mouthLip_FRAME_lockzxfxzyShape.ovdt"
		;
connectAttr "c_Rt_mouthLip_CTRL.frameSelectAble" "c_Rt_mouthLip_FRAME_lockzxfxfyShape.ovdt"
		;
connectAttr "c_Rt_mouthLip_FRAME.up_Vis" "c_Rt_mouthLip_CTRL_up.v";
connectAttr "c_Rt_mouthLip_FRAME.dn_Vis" "c_Rt_mouthLip_CTRL_dn.v";
connectAttr "c_Rt_mouthLip_FRAME.lf_Vis" "c_Rt_mouthLip_CTRL_lf.v";
connectAttr "c_Rt_mouthLip_FRAME.lfup_Vis" "c_Rt_mouthLip_CTRL_lfup.v";
connectAttr "c_Rt_mouthLip_FRAME.rt_Vis" "c_Rt_mouthLip_CTRL_rt.v";
connectAttr "c_Rt_mouthLip_FRAME.rtup_Vis" "c_Rt_mouthLip_CTRL_rtup.v";
connectAttr "c_Rt_mouthLip_FRAME.lfdn_Vis" "c_Rt_mouthLip_CTRL_lfdn.v";
connectAttr "c_Rt_mouthLip_FRAME.rtdn_Vis" "c_Rt_mouthLip_CTRL_rtdn.v";
connectAttr "c_Rt_mouthLip_FRAME.fourAxis_up_Vis" "c_Rt_mouthLip_CTRL_fourAxisup.v"
		;
connectAttr "c_Rt_mouthLip_FRAME.fourAxis_dn_Vis" "c_Rt_mouthLip_CTRL_fourAxisdn.v"
		;
connectAttr "c_Rt_mouthLip_FRAME.fourAxis_lf_Vis" "c_Rt_mouthLip_CTRL_fourAxislf.v"
		;
connectAttr "c_Rt_mouthLip_FRAME.fourAxis_rt_Vis" "c_Rt_mouthLip_CTRL_fourAxisrt.v"
		;
connectAttr "c_jaw_up_upclamp_finalrange.opr" "c_jaw_up_FRAME.up";
connectAttr "c_jaw_up_dnclamp_finalrange.opr" "c_jaw_up_FRAME.dn";
connectAttr "c_jaw_up_lfclamp_finalrange.opr" "c_jaw_up_FRAME.lf";
connectAttr "c_jaw_up_rtclamp_finalrange.opr" "c_jaw_up_FRAME.rt";
connectAttr "c_jaw_up_lfupmult.ox" "c_jaw_up_FRAME.lfup";
connectAttr "c_jaw_up_rtupmult.ox" "c_jaw_up_FRAME.rtup";
connectAttr "c_jaw_up_lfdnmult.ox" "c_jaw_up_FRAME.lfdn";
connectAttr "c_jaw_up_rtdnmult.ox" "c_jaw_up_FRAME.rtdn";
connectAttr "c_jaw_up_lfclamp_NYrange.opr" "c_jaw_up_FRAME.fourAxis_up";
connectAttr "c_jaw_up_lfclamp_PYrange.opr" "c_jaw_up_FRAME.fourAxis_dn";
connectAttr "c_jaw_up_upclamp_PXrange.opr" "c_jaw_up_FRAME.fourAxis_lf";
connectAttr "c_jaw_up_upclamp_NXrange.opr" "c_jaw_up_FRAME.fourAxis_rt";
connectAttr "c_jaw_up_CTRL.frameSelectAble" "c_jaw_up_FRAMEShape.ovdt";
connectAttr "c_jaw_up_CTRL.frameSelectAble" "c_jaw_up_FRAME_lockzyShape.ovdt";
connectAttr "c_jaw_up_CTRL.frameSelectAble" "c_jaw_up_FRAME_lockfyShape.ovdt";
connectAttr "c_jaw_up_CTRL.frameSelectAble" "c_jaw_up_FRAME_lockzxShape.ovdt";
connectAttr "c_jaw_up_CTRL.frameSelectAble" "c_jaw_up_FRAME_lockfxShape.ovdt";
connectAttr "c_jaw_up_CTRL.frameSelectAble" "c_jaw_up_FRAME_lockzyfyShape.ovdt";
connectAttr "c_jaw_up_CTRL.frameSelectAble" "c_jaw_up_FRAME_lockzxfxShape.ovdt";
connectAttr "c_jaw_up_CTRL.frameSelectAble" "c_jaw_up_FRAME_lockzyfyzxShape.ovdt"
		;
connectAttr "c_jaw_up_CTRL.frameSelectAble" "c_jaw_up_FRAME_lockzyfyfxShape.ovdt"
		;
connectAttr "c_jaw_up_CTRL.frameSelectAble" "c_jaw_up_FRAME_lockzxfxzyShape.ovdt"
		;
connectAttr "c_jaw_up_CTRL.frameSelectAble" "c_jaw_up_FRAME_lockzxfxfyShape.ovdt"
		;
connectAttr "c_jaw_up_FRAME.up_Vis" "c_jaw_up_CTRL_up.v";
connectAttr "c_jaw_up_FRAME.dn_Vis" "c_jaw_up_CTRL_dn.v";
connectAttr "c_jaw_up_FRAME.lf_Vis" "c_jaw_up_CTRL_lf.v";
connectAttr "c_jaw_up_FRAME.lfup_Vis" "c_jaw_up_CTRL_lfup.v";
connectAttr "c_jaw_up_FRAME.rt_Vis" "c_jaw_up_CTRL_rt.v";
connectAttr "c_jaw_up_FRAME.rtup_Vis" "c_jaw_up_CTRL_rtup.v";
connectAttr "c_jaw_up_FRAME.lfdn_Vis" "c_jaw_up_CTRL_lfdn.v";
connectAttr "c_jaw_up_FRAME.rtdn_Vis" "c_jaw_up_CTRL_rtdn.v";
connectAttr "c_jaw_up_FRAME.fourAxis_up_Vis" "c_jaw_up_CTRL_fourAxisup.v";
connectAttr "c_jaw_up_FRAME.fourAxis_dn_Vis" "c_jaw_up_CTRL_fourAxisdn.v";
connectAttr "c_jaw_up_FRAME.fourAxis_lf_Vis" "c_jaw_up_CTRL_fourAxislf.v";
connectAttr "c_jaw_up_FRAME.fourAxis_rt_Vis" "c_jaw_up_CTRL_fourAxisrt.v";
connectAttr "A_upclamp_finalrange.opr" "c_a_FRAME.up";
connectAttr "A_dnclamp_finalrange.opr" "c_a_FRAME.dn";
connectAttr "A_lfclamp_finalrange.opr" "c_a_FRAME.lf";
connectAttr "A_rtclamp_finalrange.opr" "c_a_FRAME.rt";
connectAttr "A_lfupmult.ox" "c_a_FRAME.lfup";
connectAttr "A_rtupmult.ox" "c_a_FRAME.rtup";
connectAttr "A_lfdnmult.ox" "c_a_FRAME.lfdn";
connectAttr "A_rtdnmult.ox" "c_a_FRAME.rtdn";
connectAttr "A_lfclamp_NYrange.opr" "c_a_FRAME.fourAxis_up";
connectAttr "A_lfclamp_PYrange.opr" "c_a_FRAME.fourAxis_dn";
connectAttr "A_upclamp_PXrange.opr" "c_a_FRAME.fourAxis_lf";
connectAttr "A_upclamp_NXrange.opr" "c_a_FRAME.fourAxis_rt";
connectAttr "c_a_CTRLShapeOrig.ws" "c_a_CTRLShape.cr";
connectAttr "c_a_FRAME.up_Vis" "c_a_CTRL_up.v";
connectAttr "c_a_FRAME.dn_Vis" "c_a_CTRL_dn.v";
connectAttr "c_a_FRAME.lf_Vis" "c_a_CTRL_lf.v";
connectAttr "c_a_FRAME.lfup_Vis" "c_a_CTRL_lfup.v";
connectAttr "c_a_FRAME.rt_Vis" "c_a_CTRL_rt.v";
connectAttr "c_a_FRAME.rtup_Vis" "c_a_CTRL_rtup.v";
connectAttr "c_a_FRAME.lfdn_Vis" "c_a_CTRL_lfdn.v";
connectAttr "c_a_FRAME.rtdn_Vis" "c_a_CTRL_rtdn.v";
connectAttr "c_a_FRAME.fourAxis_up_Vis" "c_a_CTRL_fourAxisup.v";
connectAttr "c_a_FRAME.fourAxis_dn_Vis" "c_a_CTRL_fourAxisdn.v";
connectAttr "c_a_FRAME.fourAxis_lf_Vis" "c_a_CTRL_fourAxislf.v";
connectAttr "c_a_FRAME.fourAxis_rt_Vis" "c_a_CTRL_fourAxisrt.v";
connectAttr "makeTextCurves22.p[0]" "Text_Char_a_5.t";
connectAttr "E_upclamp_finalrange.opr" "c_uo_FRAME.up";
connectAttr "E_dnclamp_finalrange.opr" "c_uo_FRAME.dn";
connectAttr "E_lfclamp_finalrange.opr" "c_uo_FRAME.lf";
connectAttr "E_rtclamp_finalrange.opr" "c_uo_FRAME.rt";
connectAttr "E_lfupmult.ox" "c_uo_FRAME.lfup";
connectAttr "E_rtupmult.ox" "c_uo_FRAME.rtup";
connectAttr "E_lfdnmult.ox" "c_uo_FRAME.lfdn";
connectAttr "E_rtdnmult.ox" "c_uo_FRAME.rtdn";
connectAttr "E_lfclamp_NYrange.opr" "c_uo_FRAME.fourAxis_up";
connectAttr "E_lfclamp_PYrange.opr" "c_uo_FRAME.fourAxis_dn";
connectAttr "E_upclamp_PXrange.opr" "c_uo_FRAME.fourAxis_lf";
connectAttr "E_upclamp_NXrange.opr" "c_uo_FRAME.fourAxis_rt";
connectAttr "c_uo_CTRLShapeOrig.ws" "c_uo_CTRLShape.cr";
connectAttr "c_uo_FRAME.up_Vis" "c_uo_CTRL_up.v";
connectAttr "c_uo_FRAME.dn_Vis" "c_uo_CTRL_dn.v";
connectAttr "c_uo_FRAME.lf_Vis" "c_uo_CTRL_lf.v";
connectAttr "c_uo_FRAME.lfup_Vis" "c_uo_CTRL_lfup.v";
connectAttr "c_uo_FRAME.rt_Vis" "c_uo_CTRL_rt.v";
connectAttr "c_uo_FRAME.rtup_Vis" "c_uo_CTRL_rtup.v";
connectAttr "c_uo_FRAME.lfdn_Vis" "c_uo_CTRL_lfdn.v";
connectAttr "c_uo_FRAME.rtdn_Vis" "c_uo_CTRL_rtdn.v";
connectAttr "c_uo_FRAME.fourAxis_up_Vis" "c_uo_CTRL_fourAxisup.v";
connectAttr "c_uo_FRAME.fourAxis_dn_Vis" "c_uo_CTRL_fourAxisdn.v";
connectAttr "c_uo_FRAME.fourAxis_lf_Vis" "c_uo_CTRL_fourAxislf.v";
connectAttr "c_uo_FRAME.fourAxis_rt_Vis" "c_uo_CTRL_fourAxisrt.v";
connectAttr "makeTextCurves23.p[0]" "Text_Char_uo_5.t";
connectAttr "OU_upclamp_finalrange.opr" "c_OU_FRAME.up";
connectAttr "OU_dnclamp_finalrange.opr" "c_OU_FRAME.dn";
connectAttr "OU_lfclamp_finalrange.opr" "c_OU_FRAME.lf";
connectAttr "OU_rtclamp_finalrange.opr" "c_OU_FRAME.rt";
connectAttr "OU_lfupmult.ox" "c_OU_FRAME.lfup";
connectAttr "OU_rtupmult.ox" "c_OU_FRAME.rtup";
connectAttr "OU_lfdnmult.ox" "c_OU_FRAME.lfdn";
connectAttr "OU_rtdnmult.ox" "c_OU_FRAME.rtdn";
connectAttr "OU_lfclamp_NYrange.opr" "c_OU_FRAME.fourAxis_up";
connectAttr "OU_lfclamp_PYrange.opr" "c_OU_FRAME.fourAxis_dn";
connectAttr "OU_upclamp_PXrange.opr" "c_OU_FRAME.fourAxis_lf";
connectAttr "OU_upclamp_NXrange.opr" "c_OU_FRAME.fourAxis_rt";
connectAttr "c_OU_CTRLShapeOrig.ws" "c_OU_CTRLShape.cr";
connectAttr "c_OU_FRAME.up_Vis" "c_OU_CTRL_up.v";
connectAttr "c_OU_FRAME.dn_Vis" "c_OU_CTRL_dn.v";
connectAttr "c_OU_FRAME.lf_Vis" "c_OU_CTRL_lf.v";
connectAttr "c_OU_FRAME.lfup_Vis" "c_OU_CTRL_lfup.v";
connectAttr "c_OU_FRAME.rt_Vis" "c_OU_CTRL_rt.v";
connectAttr "c_OU_FRAME.rtup_Vis" "c_OU_CTRL_rtup.v";
connectAttr "c_OU_FRAME.lfdn_Vis" "c_OU_CTRL_lfdn.v";
connectAttr "c_OU_FRAME.rtdn_Vis" "c_OU_CTRL_rtdn.v";
connectAttr "c_OU_FRAME.fourAxis_up_Vis" "c_OU_CTRL_fourAxisup.v";
connectAttr "c_OU_FRAME.fourAxis_dn_Vis" "c_OU_CTRL_fourAxisdn.v";
connectAttr "c_OU_FRAME.fourAxis_lf_Vis" "c_OU_CTRL_fourAxislf.v";
connectAttr "c_OU_FRAME.fourAxis_rt_Vis" "c_OU_CTRL_fourAxisrt.v";
connectAttr "makeTextCurves9.p[0]" "Text_Char_O_2.t";
connectAttr "I_upclamp_finalrange.opr" "c_fv_FRAME.up";
connectAttr "I_dnclamp_finalrange.opr" "c_fv_FRAME.dn";
connectAttr "I_lfclamp_finalrange.opr" "c_fv_FRAME.lf";
connectAttr "I_rtclamp_finalrange.opr" "c_fv_FRAME.rt";
connectAttr "I_lfupmult.ox" "c_fv_FRAME.lfup";
connectAttr "I_rtupmult.ox" "c_fv_FRAME.rtup";
connectAttr "I_lfdnmult.ox" "c_fv_FRAME.lfdn";
connectAttr "I_rtdnmult.ox" "c_fv_FRAME.rtdn";
connectAttr "I_lfclamp_NYrange.opr" "c_fv_FRAME.fourAxis_up";
connectAttr "I_lfclamp_PYrange.opr" "c_fv_FRAME.fourAxis_dn";
connectAttr "I_upclamp_PXrange.opr" "c_fv_FRAME.fourAxis_lf";
connectAttr "I_upclamp_NXrange.opr" "c_fv_FRAME.fourAxis_rt";
connectAttr "c_fv_CTRLShapeOrig.ws" "c_fv_CTRLShape.cr";
connectAttr "c_fv_FRAME.up_Vis" "c_fv_CTRL_up.v";
connectAttr "c_fv_FRAME.dn_Vis" "c_fv_CTRL_dn.v";
connectAttr "c_fv_FRAME.lf_Vis" "c_fv_CTRL_lf.v";
connectAttr "c_fv_FRAME.lfup_Vis" "c_fv_CTRL_lfup.v";
connectAttr "c_fv_FRAME.rt_Vis" "c_fv_CTRL_rt.v";
connectAttr "c_fv_FRAME.rtup_Vis" "c_fv_CTRL_rtup.v";
connectAttr "c_fv_FRAME.lfdn_Vis" "c_fv_CTRL_lfdn.v";
connectAttr "c_fv_FRAME.rtdn_Vis" "c_fv_CTRL_rtdn.v";
connectAttr "c_fv_FRAME.fourAxis_up_Vis" "c_fv_CTRL_fourAxisup.v";
connectAttr "c_fv_FRAME.fourAxis_dn_Vis" "c_fv_CTRL_fourAxisdn.v";
connectAttr "c_fv_FRAME.fourAxis_lf_Vis" "c_fv_CTRL_fourAxislf.v";
connectAttr "c_fv_FRAME.fourAxis_rt_Vis" "c_fv_CTRL_fourAxisrt.v";
connectAttr "makeTextCurves24.p[0]" "Text_Char_f_2.t";
connectAttr "makeTextCurves24.p[1]" "Text_Char_x_3.t";
connectAttr "makeTextCurves24.p[2]" "Text_Char_v_1.t";
connectAttr "O_upclamp_finalrange.opr" "c_the_FRAME.up";
connectAttr "O_dnclamp_finalrange.opr" "c_the_FRAME.dn";
connectAttr "O_lfclamp_finalrange.opr" "c_the_FRAME.lf";
connectAttr "O_rtclamp_finalrange.opr" "c_the_FRAME.rt";
connectAttr "O_lfupmult.ox" "c_the_FRAME.lfup";
connectAttr "O_rtupmult.ox" "c_the_FRAME.rtup";
connectAttr "O_lfdnmult.ox" "c_the_FRAME.lfdn";
connectAttr "O_rtdnmult.ox" "c_the_FRAME.rtdn";
connectAttr "O_lfclamp_NYrange.opr" "c_the_FRAME.fourAxis_up";
connectAttr "O_lfclamp_PYrange.opr" "c_the_FRAME.fourAxis_dn";
connectAttr "O_upclamp_PXrange.opr" "c_the_FRAME.fourAxis_lf";
connectAttr "O_upclamp_NXrange.opr" "c_the_FRAME.fourAxis_rt";
connectAttr "c_the_CTRLShapeOrig.ws" "c_the_CTRLShape.cr";
connectAttr "c_the_FRAME.up_Vis" "c_the_CTRL_up.v";
connectAttr "c_the_FRAME.dn_Vis" "c_the_CTRL_dn.v";
connectAttr "c_the_FRAME.lf_Vis" "c_the_CTRL_lf.v";
connectAttr "c_the_FRAME.lfup_Vis" "c_the_CTRL_lfup.v";
connectAttr "c_the_FRAME.rt_Vis" "c_the_CTRL_rt.v";
connectAttr "c_the_FRAME.rtup_Vis" "c_the_CTRL_rtup.v";
connectAttr "c_the_FRAME.lfdn_Vis" "c_the_CTRL_lfdn.v";
connectAttr "c_the_FRAME.rtdn_Vis" "c_the_CTRL_rtdn.v";
connectAttr "c_the_FRAME.fourAxis_up_Vis" "c_the_CTRL_fourAxisup.v";
connectAttr "c_the_FRAME.fourAxis_dn_Vis" "c_the_CTRL_fourAxisdn.v";
connectAttr "c_the_FRAME.fourAxis_lf_Vis" "c_the_CTRL_fourAxislf.v";
connectAttr "c_the_FRAME.fourAxis_rt_Vis" "c_the_CTRL_fourAxisrt.v";
connectAttr "makeTextCurves25.p[0]" "Text_Char_t_1.t";
connectAttr "makeTextCurves25.p[1]" "Text_Char_h_3.t";
connectAttr "makeTextCurves25.p[2]" "Text_Char_e_5.t";
connectAttr "makeTextCurves49.p[0]" "Text_Char_x_1.t";
connectAttr "makeTextCurves50.p[0]" "Text_Char_L_1.t";
connectAttr "U_upclamp_finalrange.opr" "c_eeesz_FRAME.up";
connectAttr "U_dnclamp_finalrange.opr" "c_eeesz_FRAME.dn";
connectAttr "U_lfclamp_finalrange.opr" "c_eeesz_FRAME.lf";
connectAttr "U_rtclamp_finalrange.opr" "c_eeesz_FRAME.rt";
connectAttr "U_lfupmult.ox" "c_eeesz_FRAME.lfup";
connectAttr "U_rtupmult.ox" "c_eeesz_FRAME.rtup";
connectAttr "U_lfdnmult.ox" "c_eeesz_FRAME.lfdn";
connectAttr "U_rtdnmult.ox" "c_eeesz_FRAME.rtdn";
connectAttr "U_lfclamp_NYrange.opr" "c_eeesz_FRAME.fourAxis_up";
connectAttr "U_lfclamp_PYrange.opr" "c_eeesz_FRAME.fourAxis_dn";
connectAttr "U_upclamp_PXrange.opr" "c_eeesz_FRAME.fourAxis_lf";
connectAttr "U_upclamp_NXrange.opr" "c_eeesz_FRAME.fourAxis_rt";
connectAttr "c_eeesz_CTRLShapeOrig.ws" "c_eeesz_CTRLShape.cr";
connectAttr "c_eeesz_FRAME.up_Vis" "c_eeesz_CTRL_up.v";
connectAttr "c_eeesz_FRAME.dn_Vis" "c_eeesz_CTRL_dn.v";
connectAttr "c_eeesz_FRAME.lf_Vis" "c_eeesz_CTRL_lf.v";
connectAttr "c_eeesz_FRAME.lfup_Vis" "c_eeesz_CTRL_lfup.v";
connectAttr "c_eeesz_FRAME.rt_Vis" "c_eeesz_CTRL_rt.v";
connectAttr "c_eeesz_FRAME.rtup_Vis" "c_eeesz_CTRL_rtup.v";
connectAttr "c_eeesz_FRAME.lfdn_Vis" "c_eeesz_CTRL_lfdn.v";
connectAttr "c_eeesz_FRAME.rtdn_Vis" "c_eeesz_CTRL_rtdn.v";
connectAttr "c_eeesz_FRAME.fourAxis_up_Vis" "c_eeesz_CTRL_fourAxisup.v";
connectAttr "c_eeesz_FRAME.fourAxis_dn_Vis" "c_eeesz_CTRL_fourAxisdn.v";
connectAttr "c_eeesz_FRAME.fourAxis_lf_Vis" "c_eeesz_CTRL_fourAxislf.v";
connectAttr "c_eeesz_FRAME.fourAxis_rt_Vis" "c_eeesz_CTRL_fourAxisrt.v";
connectAttr "makeTextCurves26.p[0]" "Text_Char_e_6.t";
connectAttr "makeTextCurves26.p[1]" "Text_Char_e_7.t";
connectAttr "makeTextCurves26.p[2]" "Text_Char_e_8.t";
connectAttr "makeTextCurves26.p[3]" "Text_Char_x_4.t";
connectAttr "makeTextCurves26.p[4]" "Text_Char_s_3.t";
connectAttr "makeTextCurves26.p[5]" "Text_Char_x_5.t";
connectAttr "makeTextCurves26.p[6]" "Text_Char_z_1.t";
connectAttr "FV_upclamp_finalrange.opr" "c_mbp_FRAME.up";
connectAttr "FV_dnclamp_finalrange.opr" "c_mbp_FRAME.dn";
connectAttr "FV_lfclamp_finalrange.opr" "c_mbp_FRAME.lf";
connectAttr "FV_rtclamp_finalrange.opr" "c_mbp_FRAME.rt";
connectAttr "FV_lfupmult.ox" "c_mbp_FRAME.lfup";
connectAttr "FV_rtupmult.ox" "c_mbp_FRAME.rtup";
connectAttr "FV_lfdnmult.ox" "c_mbp_FRAME.lfdn";
connectAttr "FV_rtdnmult.ox" "c_mbp_FRAME.rtdn";
connectAttr "FV_lfclamp_NYrange.opr" "c_mbp_FRAME.fourAxis_up";
connectAttr "FV_lfclamp_PYrange.opr" "c_mbp_FRAME.fourAxis_dn";
connectAttr "FV_upclamp_PXrange.opr" "c_mbp_FRAME.fourAxis_lf";
connectAttr "FV_upclamp_NXrange.opr" "c_mbp_FRAME.fourAxis_rt";
connectAttr "c_mbp_CTRLShapeOrig.ws" "c_mbp_CTRLShape.cr";
connectAttr "c_mbp_FRAME.up_Vis" "c_mbp_CTRL_up.v";
connectAttr "c_mbp_FRAME.dn_Vis" "c_mbp_CTRL_dn.v";
connectAttr "c_mbp_FRAME.lf_Vis" "c_mbp_CTRL_lf.v";
connectAttr "c_mbp_FRAME.lfup_Vis" "c_mbp_CTRL_lfup.v";
connectAttr "c_mbp_FRAME.rt_Vis" "c_mbp_CTRL_rt.v";
connectAttr "c_mbp_FRAME.rtup_Vis" "c_mbp_CTRL_rtup.v";
connectAttr "c_mbp_FRAME.lfdn_Vis" "c_mbp_CTRL_lfdn.v";
connectAttr "c_mbp_FRAME.rtdn_Vis" "c_mbp_CTRL_rtdn.v";
connectAttr "c_mbp_FRAME.fourAxis_up_Vis" "c_mbp_CTRL_fourAxisup.v";
connectAttr "c_mbp_FRAME.fourAxis_dn_Vis" "c_mbp_CTRL_fourAxisdn.v";
connectAttr "c_mbp_FRAME.fourAxis_lf_Vis" "c_mbp_CTRL_fourAxislf.v";
connectAttr "c_mbp_FRAME.fourAxis_rt_Vis" "c_mbp_CTRL_fourAxisrt.v";
connectAttr "makeTextCurves27.p[0]" "Text_Char_m_1.t";
connectAttr "makeTextCurves27.p[1]" "Text_Char_x_6.t";
connectAttr "makeTextCurves27.p[2]" "Text_Char_b_1.t";
connectAttr "makeTextCurves27.p[3]" "Text_Char_x_7.t";
connectAttr "makeTextCurves27.p[4]" "Text_Char_p_6.t";
connectAttr "tongue_upclamp_finalrange.opr" "c_tongue_FRAME.up";
connectAttr "tongue_dnclamp_finalrange.opr" "c_tongue_FRAME.dn";
connectAttr "tongue_lfclamp_finalrange.opr" "c_tongue_FRAME.lf";
connectAttr "tongue_rtclamp_finalrange.opr" "c_tongue_FRAME.rt";
connectAttr "tongue_lfupmult.ox" "c_tongue_FRAME.lfup";
connectAttr "tongue_rtupmult.ox" "c_tongue_FRAME.rtup";
connectAttr "tongue_lfdnmult.ox" "c_tongue_FRAME.lfdn";
connectAttr "tongue_rtdnmult.ox" "c_tongue_FRAME.rtdn";
connectAttr "tongue_lfclamp_NYrange.opr" "c_tongue_FRAME.fourAxis_up";
connectAttr "tongue_lfclamp_PYrange.opr" "c_tongue_FRAME.fourAxis_dn";
connectAttr "tongue_upclamp_PXrange.opr" "c_tongue_FRAME.fourAxis_lf";
connectAttr "tongue_upclamp_NXrange.opr" "c_tongue_FRAME.fourAxis_rt";
connectAttr "c_tongue_CTRL_ex.out[0]" "c_tongue_CTRL.output_tx";
connectAttr "c_tongue_CTRL_ex.out[1]" "c_tongue_CTRL.output_ty";
connectAttr "c_tongue_CTRL_ex.out[2]" "c_tongue_CTRL.output_rx";
connectAttr "c_tongue_CTRL_ex.out[3]" "c_tongue_CTRL.output_ry";
connectAttr "c_tongue_CTRL_ex.out[4]" "c_tongue_CTRL.output_rz";
connectAttr "c_tongue_CTRL_ex.out[5]" "c_tongue_CTRL.output_stretch";
connectAttr "c_tongue_FRAME.up_Vis" "c_tongue_CTRL_up.v";
connectAttr "c_tongue_FRAME.dn_Vis" "c_tongue_CTRL_dn.v";
connectAttr "c_tongue_FRAME.lf_Vis" "c_tongue_CTRL_lf.v";
connectAttr "c_tongue_FRAME.lfup_Vis" "c_tongue_CTRL_lfup.v";
connectAttr "c_tongue_FRAME.rt_Vis" "c_tongue_CTRL_rt.v";
connectAttr "c_tongue_FRAME.rtup_Vis" "c_tongue_CTRL_rtup.v";
connectAttr "c_tongue_FRAME.lfdn_Vis" "c_tongue_CTRL_lfdn.v";
connectAttr "c_tongue_FRAME.rtdn_Vis" "c_tongue_CTRL_rtdn.v";
connectAttr "c_tongue_FRAME.fourAxis_up_Vis" "c_tongue_CTRL_fourAxisup.v";
connectAttr "c_tongue_FRAME.fourAxis_dn_Vis" "c_tongue_CTRL_fourAxisdn.v";
connectAttr "c_tongue_FRAME.fourAxis_lf_Vis" "c_tongue_CTRL_fourAxislf.v";
connectAttr "c_tongue_FRAME.fourAxis_rt_Vis" "c_tongue_CTRL_fourAxisrt.v";
connectAttr "makeTextCurves10.p[0]" "c_Char_T_1.t";
connectAttr "makeTextCurves10.p[1]" "c_Char_o_1.t";
connectAttr "makeTextCurves10.p[2]" "c_Char_n_1.t";
connectAttr "makeTextCurves10.p[3]" "c_Char_g_1.t";
connectAttr "makeTextCurves10.p[4]" "c_Char_u_1.t";
connectAttr "makeTextCurves10.p[5]" "c_Char_e_1.t";
connectAttr ":mentalrayGlobals.msg" ":mentalrayItemsList.glb";
connectAttr ":miDefaultOptions.msg" ":mentalrayItemsList.opt" -na;
connectAttr ":miDefaultFramebuffer.msg" ":mentalrayItemsList.fb" -na;
connectAttr ":miDefaultOptions.msg" ":mentalrayGlobals.opt";
connectAttr ":miDefaultFramebuffer.msg" ":mentalrayGlobals.fb";
connectAttr "A_dnScale.ox" "A_dnclamp_finalrange.ipr";
connectAttr "A_dnmult_Yinverse.ox" "A_dnclamp_PYrange.ipr";
connectAttr "A_lfScale.ox" "A_lfclamp_finalrange.ipr";
connectAttr "c_a_CTRL.ty" "A_lfclamp_NYrange.ipr";
connectAttr "A_lfmult_Xinverse.ox" "A_lfclamp_PXrange.ipr";
connectAttr "A_lfmult_Yinverse.ox" "A_lfclamp_PYrange.ipr";
connectAttr "A_rtScale.ox" "A_rtclamp_finalrange.ipr";
connectAttr "c_a_CTRL.tx" "A_rtclamp_PXrange.ipr";
connectAttr "A_upScale.ox" "A_upclamp_finalrange.ipr";
connectAttr "c_a_CTRL.tx" "A_upclamp_NXrange.ipr";
connectAttr "A_upmult_Xinverse.ox" "A_upclamp_PXrange.ipr";
connectAttr "c_a_CTRL.ty" "A_upclamp_PYrange.ipr";
connectAttr "c_dn_mouthLip_dnScale.ox" "c_dn_mouthLip_dnclamp_finalrange.ipr";
connectAttr "c_dn_mouthLip_dnmult_Yinverse.ox" "c_dn_mouthLip_dnclamp_PYrange.ipr"
		;
connectAttr "c_dn_mouthLip_lfScale.ox" "c_dn_mouthLip_lfclamp_finalrange.ipr";
connectAttr "c_dn_mouthLip_CTRL.ty" "c_dn_mouthLip_lfclamp_NYrange.ipr";
connectAttr "c_dn_mouthLip_lfmult_Xinverse.ox" "c_dn_mouthLip_lfclamp_PXrange.ipr"
		;
connectAttr "c_dn_mouthLip_lfmult_Yinverse.ox" "c_dn_mouthLip_lfclamp_PYrange.ipr"
		;
connectAttr "c_dn_mouthLip_rtScale.ox" "c_dn_mouthLip_rtclamp_finalrange.ipr";
connectAttr "c_dn_mouthLip_CTRL.tx" "c_dn_mouthLip_rtclamp_PXrange.ipr";
connectAttr "c_dn_mouthLip_upScale.ox" "c_dn_mouthLip_upclamp_finalrange.ipr";
connectAttr "c_dn_mouthLip_CTRL.tx" "c_dn_mouthLip_upclamp_NXrange.ipr";
connectAttr "c_dn_mouthLip_upmult_Xinverse.ox" "c_dn_mouthLip_upclamp_PXrange.ipr"
		;
connectAttr "c_dn_mouthLip_CTRL.ty" "c_dn_mouthLip_upclamp_PYrange.ipr";
connectAttr "c_jaw_dn_dnScale.ox" "c_jaw_dn_dnclamp_finalrange.ipr";
connectAttr "c_jaw_dn_dnmult_Yinverse.ox" "c_jaw_dn_dnclamp_PYrange.ipr";
connectAttr "c_jaw_dn_lfScale.ox" "c_jaw_dn_lfclamp_finalrange.ipr";
connectAttr "c_jaw_dn_CTRL.ty" "c_jaw_dn_lfclamp_NYrange.ipr";
connectAttr "c_jaw_dn_lfmult_Xinverse.ox" "c_jaw_dn_lfclamp_PXrange.ipr";
connectAttr "c_jaw_dn_lfmult_Yinverse.ox" "c_jaw_dn_lfclamp_PYrange.ipr";
connectAttr "c_jaw_dn_rtScale.ox" "c_jaw_dn_rtclamp_finalrange.ipr";
connectAttr "c_jaw_dn_CTRL.tx" "c_jaw_dn_rtclamp_PXrange.ipr";
connectAttr "c_jaw_dn_upScale.ox" "c_jaw_dn_upclamp_finalrange.ipr";
connectAttr "c_jaw_dn_CTRL.tx" "c_jaw_dn_upclamp_NXrange.ipr";
connectAttr "c_jaw_dn_upmult_Xinverse.ox" "c_jaw_dn_upclamp_PXrange.ipr";
connectAttr "c_jaw_dn_CTRL.ty" "c_jaw_dn_upclamp_PYrange.ipr";
connectAttr "c_jaw_up_dnScale.ox" "c_jaw_up_dnclamp_finalrange.ipr";
connectAttr "c_jaw_up_dnmult_Yinverse.ox" "c_jaw_up_dnclamp_PYrange.ipr";
connectAttr "c_jaw_up_lfScale.ox" "c_jaw_up_lfclamp_finalrange.ipr";
connectAttr "c_jaw_up_CTRL.ty" "c_jaw_up_lfclamp_NYrange.ipr";
connectAttr "c_jaw_up_lfmult_Xinverse.ox" "c_jaw_up_lfclamp_PXrange.ipr";
connectAttr "c_jaw_up_lfmult_Yinverse.ox" "c_jaw_up_lfclamp_PYrange.ipr";
connectAttr "c_jaw_up_rtScale.ox" "c_jaw_up_rtclamp_finalrange.ipr";
connectAttr "c_jaw_up_CTRL.tx" "c_jaw_up_rtclamp_PXrange.ipr";
connectAttr "c_jaw_up_upScale.ox" "c_jaw_up_upclamp_finalrange.ipr";
connectAttr "c_jaw_up_CTRL.tx" "c_jaw_up_upclamp_NXrange.ipr";
connectAttr "c_jaw_up_upmult_Xinverse.ox" "c_jaw_up_upclamp_PXrange.ipr";
connectAttr "c_jaw_up_CTRL.ty" "c_jaw_up_upclamp_PYrange.ipr";
connectAttr "c_Lf_dn_eyelids_dnScale.ox" "c_Lf_dn_eyelids_dnclamp_finalrange.ipr"
		;
connectAttr "c_Lf_dn_eyelids_dnmult_Yinverse.ox" "c_Lf_dn_eyelids_dnclamp_PYrange.ipr"
		;
connectAttr "c_Lf_dn_eyelids_lfScale.ox" "c_Lf_dn_eyelids_lfclamp_finalrange.ipr"
		;
connectAttr "c_Lf_dn_eyelids_CTRL.ty" "c_Lf_dn_eyelids_lfclamp_NYrange.ipr";
connectAttr "c_Lf_dn_eyelids_lfmult_Xinverse.ox" "c_Lf_dn_eyelids_lfclamp_PXrange.ipr"
		;
connectAttr "c_Lf_dn_eyelids_lfmult_Yinverse.ox" "c_Lf_dn_eyelids_lfclamp_PYrange.ipr"
		;
connectAttr "c_Lf_dn_eyelids_rtScale.ox" "c_Lf_dn_eyelids_rtclamp_finalrange.ipr"
		;
connectAttr "c_Lf_dn_eyelids_CTRL.tx" "c_Lf_dn_eyelids_rtclamp_PXrange.ipr";
connectAttr "c_Lf_dn_eyelids_upScale.ox" "c_Lf_dn_eyelids_upclamp_finalrange.ipr"
		;
connectAttr "c_Lf_dn_eyelids_CTRL.tx" "c_Lf_dn_eyelids_upclamp_NXrange.ipr";
connectAttr "c_Lf_dn_eyelids_upmult_Xinverse.ox" "c_Lf_dn_eyelids_upclamp_PXrange.ipr"
		;
connectAttr "c_Lf_dn_eyelids_CTRL.ty" "c_Lf_dn_eyelids_upclamp_PYrange.ipr";
connectAttr "c_Lf_eyebrows_01_dnScale.ox" "c_Lf_eyebrows_01_dnclamp_finalrange.ipr"
		;
connectAttr "c_Lf_eyebrows_01_dnmult_Yinverse.ox" "c_Lf_eyebrows_01_dnclamp_PYrange.ipr"
		;
connectAttr "c_Lf_eyebrows_01_lfScale.ox" "c_Lf_eyebrows_01_lfclamp_finalrange.ipr"
		;
connectAttr "c_Lf_eyebrows_01_plus.o3y" "c_Lf_eyebrows_01_lfclamp_NYrange.ipr";
connectAttr "c_Lf_eyebrows_01_lfmult_Xinverse.ox" "c_Lf_eyebrows_01_lfclamp_PXrange.ipr"
		;
connectAttr "c_Lf_eyebrows_01_lfmult_Yinverse.ox" "c_Lf_eyebrows_01_lfclamp_PYrange.ipr"
		;
connectAttr "c_Lf_eyebrows_01_rtScale.ox" "c_Lf_eyebrows_01_rtclamp_finalrange.ipr"
		;
connectAttr "c_Lf_eyebrows_01_plus.o3x" "c_Lf_eyebrows_01_rtclamp_PXrange.ipr";
connectAttr "c_Lf_eyebrows_01_upScale.ox" "c_Lf_eyebrows_01_upclamp_finalrange.ipr"
		;
connectAttr "c_Lf_eyebrows_01_plus.o3x" "c_Lf_eyebrows_01_upclamp_NXrange.ipr";
connectAttr "c_Lf_eyebrows_01_upmult_Xinverse.ox" "c_Lf_eyebrows_01_upclamp_PXrange.ipr"
		;
connectAttr "c_Lf_eyebrows_01_plus.o3y" "c_Lf_eyebrows_01_upclamp_PYrange.ipr";
connectAttr "c_Lf_eyebrows_02_dnScale.ox" "c_Lf_eyebrows_02_dnclamp_finalrange.ipr"
		;
connectAttr "c_Lf_eyebrows_02_dnmult_Yinverse.ox" "c_Lf_eyebrows_02_dnclamp_PYrange.ipr"
		;
connectAttr "c_Lf_eyebrows_02_lfScale.ox" "c_Lf_eyebrows_02_lfclamp_finalrange.ipr"
		;
connectAttr "c_Lf_eyebrows_02_plus.o3y" "c_Lf_eyebrows_02_lfclamp_NYrange.ipr";
connectAttr "c_Lf_eyebrows_02_lfmult_Xinverse.ox" "c_Lf_eyebrows_02_lfclamp_PXrange.ipr"
		;
connectAttr "c_Lf_eyebrows_02_lfmult_Yinverse.ox" "c_Lf_eyebrows_02_lfclamp_PYrange.ipr"
		;
connectAttr "c_Lf_eyebrows_02_rtScale.ox" "c_Lf_eyebrows_02_rtclamp_finalrange.ipr"
		;
connectAttr "c_Lf_eyebrows_02_plus.o3x" "c_Lf_eyebrows_02_rtclamp_PXrange.ipr";
connectAttr "c_Lf_eyebrows_02_upScale.ox" "c_Lf_eyebrows_02_upclamp_finalrange.ipr"
		;
connectAttr "c_Lf_eyebrows_02_plus.o3x" "c_Lf_eyebrows_02_upclamp_NXrange.ipr";
connectAttr "c_Lf_eyebrows_02_upmult_Xinverse.ox" "c_Lf_eyebrows_02_upclamp_PXrange.ipr"
		;
connectAttr "c_Lf_eyebrows_02_plus.o3y" "c_Lf_eyebrows_02_upclamp_PYrange.ipr";
connectAttr "c_Lf_eyebrows_03_dnScale.ox" "c_Lf_eyebrows_03_dnclamp_finalrange.ipr"
		;
connectAttr "c_Lf_eyebrows_03_dnmult_Yinverse.ox" "c_Lf_eyebrows_03_dnclamp_PYrange.ipr"
		;
connectAttr "c_Lf_eyebrows_03_lfScale.ox" "c_Lf_eyebrows_03_lfclamp_finalrange.ipr"
		;
connectAttr "c_Lf_eyebrows_03_plus.o3y" "c_Lf_eyebrows_03_lfclamp_NYrange.ipr";
connectAttr "c_Lf_eyebrows_03_lfmult_Xinverse.ox" "c_Lf_eyebrows_03_lfclamp_PXrange.ipr"
		;
connectAttr "c_Lf_eyebrows_03_lfmult_Yinverse.ox" "c_Lf_eyebrows_03_lfclamp_PYrange.ipr"
		;
connectAttr "c_Lf_eyebrows_03_rtScale.ox" "c_Lf_eyebrows_03_rtclamp_finalrange.ipr"
		;
connectAttr "c_Lf_eyebrows_03_plus.o3x" "c_Lf_eyebrows_03_rtclamp_PXrange.ipr";
connectAttr "c_Lf_eyebrows_03_upScale.ox" "c_Lf_eyebrows_03_upclamp_finalrange.ipr"
		;
connectAttr "c_Lf_eyebrows_03_plus.o3x" "c_Lf_eyebrows_03_upclamp_NXrange.ipr";
connectAttr "c_Lf_eyebrows_03_upmult_Xinverse.ox" "c_Lf_eyebrows_03_upclamp_PXrange.ipr"
		;
connectAttr "c_Lf_eyebrows_03_plus.o3y" "c_Lf_eyebrows_03_upclamp_PYrange.ipr";
connectAttr "c_Lf_eyeStretch_dnScale.ox" "c_Lf_eyeStretch_dnclamp_finalrange.ipr"
		;
connectAttr "c_Lf_eyeStretch_dnmult_Yinverse.ox" "c_Lf_eyeStretch_dnclamp_PYrange.ipr"
		;
connectAttr "c_Lf_eyeStretch_lfScale.ox" "c_Lf_eyeStretch_lfclamp_finalrange.ipr"
		;
connectAttr "c_Lf_cheek_CTRL.ty" "c_Lf_eyeStretch_lfclamp_NYrange.ipr";
connectAttr "c_Lf_eyeStretch_lfmult_Xinverse.ox" "c_Lf_eyeStretch_lfclamp_PXrange.ipr"
		;
connectAttr "c_Lf_eyeStretch_lfmult_Yinverse.ox" "c_Lf_eyeStretch_lfclamp_PYrange.ipr"
		;
connectAttr "c_Lf_eyeStretch_rtScale.ox" "c_Lf_eyeStretch_rtclamp_finalrange.ipr"
		;
connectAttr "c_Lf_cheek_CTRL.tx" "c_Lf_eyeStretch_rtclamp_PXrange.ipr";
connectAttr "c_Lf_eyeStretch_upScale.ox" "c_Lf_eyeStretch_upclamp_finalrange.ipr"
		;
connectAttr "c_Lf_cheek_CTRL.tx" "c_Lf_eyeStretch_upclamp_NXrange.ipr";
connectAttr "c_Lf_eyeStretch_upmult_Xinverse.ox" "c_Lf_eyeStretch_upclamp_PXrange.ipr"
		;
connectAttr "c_Lf_cheek_CTRL.ty" "c_Lf_eyeStretch_upclamp_PYrange.ipr";
connectAttr "c_Lf_mouthLip_dnScale.ox" "c_Lf_mouthLip_dnclamp_finalrange.ipr";
connectAttr "c_Lf_mouthLip_dnmult_Yinverse.ox" "c_Lf_mouthLip_dnclamp_PYrange.ipr"
		;
connectAttr "c_Lf_mouthLip_lfScale.ox" "c_Lf_mouthLip_lfclamp_finalrange.ipr";
connectAttr "c_Lf_mouthLip_CTRL.ty" "c_Lf_mouthLip_lfclamp_NYrange.ipr";
connectAttr "c_Lf_mouthLip_lfmult_Xinverse.ox" "c_Lf_mouthLip_lfclamp_PXrange.ipr"
		;
connectAttr "c_Lf_mouthLip_lfmult_Yinverse.ox" "c_Lf_mouthLip_lfclamp_PYrange.ipr"
		;
connectAttr "c_Lf_mouthLip_rtScale.ox" "c_Lf_mouthLip_rtclamp_finalrange.ipr";
connectAttr "c_Lf_mouthLip_CTRL.tx" "c_Lf_mouthLip_rtclamp_PXrange.ipr";
connectAttr "c_Lf_mouthLip_upScale.ox" "c_Lf_mouthLip_upclamp_finalrange.ipr";
connectAttr "c_Lf_mouthLip_CTRL.tx" "c_Lf_mouthLip_upclamp_NXrange.ipr";
connectAttr "c_Lf_mouthLip_upmult_Xinverse.ox" "c_Lf_mouthLip_upclamp_PXrange.ipr"
		;
connectAttr "c_Lf_mouthLip_CTRL.ty" "c_Lf_mouthLip_upclamp_PYrange.ipr";
connectAttr "c_Lf_up_eyelids_dnScale.ox" "c_Lf_up_eyelids_dnclamp_finalrange.ipr"
		;
connectAttr "c_Lf_up_eyelids_dnmult_Yinverse.ox" "c_Lf_up_eyelids_dnclamp_PYrange.ipr"
		;
connectAttr "c_Lf_up_eyelids_lfScale.ox" "c_Lf_up_eyelids_lfclamp_finalrange.ipr"
		;
connectAttr "c_Lf_up_eyelids_CTRL.ty" "c_Lf_up_eyelids_lfclamp_NYrange.ipr";
connectAttr "c_Lf_up_eyelids_lfmult_Xinverse.ox" "c_Lf_up_eyelids_lfclamp_PXrange.ipr"
		;
connectAttr "c_Lf_up_eyelids_lfmult_Yinverse.ox" "c_Lf_up_eyelids_lfclamp_PYrange.ipr"
		;
connectAttr "c_Lf_up_eyelids_rtScale.ox" "c_Lf_up_eyelids_rtclamp_finalrange.ipr"
		;
connectAttr "c_Lf_up_eyelids_CTRL.tx" "c_Lf_up_eyelids_rtclamp_PXrange.ipr";
connectAttr "c_Lf_up_eyelids_upScale.ox" "c_Lf_up_eyelids_upclamp_finalrange.ipr"
		;
connectAttr "c_Lf_up_eyelids_CTRL.tx" "c_Lf_up_eyelids_upclamp_NXrange.ipr";
connectAttr "c_Lf_up_eyelids_upmult_Xinverse.ox" "c_Lf_up_eyelids_upclamp_PXrange.ipr"
		;
connectAttr "c_Lf_up_eyelids_CTRL.ty" "c_Lf_up_eyelids_upclamp_PYrange.ipr";
connectAttr "c_nose_dnScale.ox" "c_nose_dnclamp_finalrange.ipr";
connectAttr "c_nose_dnmult_Yinverse.ox" "c_nose_dnclamp_PYrange.ipr";
connectAttr "c_nose_lfScale.ox" "c_nose_lfclamp_finalrange.ipr";
connectAttr "c_nose_CTRL.ty" "c_nose_lfclamp_NYrange.ipr";
connectAttr "c_nose_lfmult_Xinverse.ox" "c_nose_lfclamp_PXrange.ipr";
connectAttr "c_nose_lfmult_Yinverse.ox" "c_nose_lfclamp_PYrange.ipr";
connectAttr "c_nose_rtScale.ox" "c_nose_rtclamp_finalrange.ipr";
connectAttr "c_nose_CTRL.tx" "c_nose_rtclamp_PXrange.ipr";
connectAttr "c_nose_upScale.ox" "c_nose_upclamp_finalrange.ipr";
connectAttr "c_nose_CTRL.tx" "c_nose_upclamp_NXrange.ipr";
connectAttr "c_nose_upmult_Xinverse.ox" "c_nose_upclamp_PXrange.ipr";
connectAttr "c_nose_CTRL.ty" "c_nose_upclamp_PYrange.ipr";
connectAttr "c_Rt_dn_eyelids_dnScale.ox" "c_Rt_dn_eyelids_dnclamp_finalrange.ipr"
		;
connectAttr "c_Rt_dn_eyelids_dnmult_Yinverse.ox" "c_Rt_dn_eyelids_dnclamp_PYrange.ipr"
		;
connectAttr "c_Rt_dn_eyelids_lfScale.ox" "c_Rt_dn_eyelids_lfclamp_finalrange.ipr"
		;
connectAttr "c_Rt_dn_eyelids_CTRL.ty" "c_Rt_dn_eyelids_lfclamp_NYrange.ipr";
connectAttr "c_Rt_dn_eyelids_lfmult_Xinverse.ox" "c_Rt_dn_eyelids_lfclamp_PXrange.ipr"
		;
connectAttr "c_Rt_dn_eyelids_lfmult_Yinverse.ox" "c_Rt_dn_eyelids_lfclamp_PYrange.ipr"
		;
connectAttr "c_Rt_dn_eyelids_rtScale.ox" "c_Rt_dn_eyelids_rtclamp_finalrange.ipr"
		;
connectAttr "c_Rt_dn_eyelids_CTRL.tx" "c_Rt_dn_eyelids_rtclamp_PXrange.ipr";
connectAttr "c_Rt_dn_eyelids_upScale.ox" "c_Rt_dn_eyelids_upclamp_finalrange.ipr"
		;
connectAttr "c_Rt_dn_eyelids_CTRL.tx" "c_Rt_dn_eyelids_upclamp_NXrange.ipr";
connectAttr "c_Rt_dn_eyelids_upmult_Xinverse.ox" "c_Rt_dn_eyelids_upclamp_PXrange.ipr"
		;
connectAttr "c_Rt_dn_eyelids_CTRL.ty" "c_Rt_dn_eyelids_upclamp_PYrange.ipr";
connectAttr "c_Rt_eyebrows_01_dnScale.ox" "c_Rt_eyebrows_01_dnclamp_finalrange.ipr"
		;
connectAttr "c_Rt_eyebrows_01_dnmult_Yinverse.ox" "c_Rt_eyebrows_01_dnclamp_PYrange.ipr"
		;
connectAttr "c_Rt_eyebrows_01_lfScale.ox" "c_Rt_eyebrows_01_lfclamp_finalrange.ipr"
		;
connectAttr "c_Rt_eyebrows_01_plus.o3y" "c_Rt_eyebrows_01_lfclamp_NYrange.ipr";
connectAttr "c_Rt_eyebrows_01_lfmult_Xinverse.ox" "c_Rt_eyebrows_01_lfclamp_PXrange.ipr"
		;
connectAttr "c_Rt_eyebrows_01_lfmult_Yinverse.ox" "c_Rt_eyebrows_01_lfclamp_PYrange.ipr"
		;
connectAttr "c_Rt_eyebrows_01_rtScale.ox" "c_Rt_eyebrows_01_rtclamp_finalrange.ipr"
		;
connectAttr "c_Rt_eyebrows_01_plus.o3x" "c_Rt_eyebrows_01_rtclamp_PXrange.ipr";
connectAttr "c_Rt_eyebrows_01_upScale.ox" "c_Rt_eyebrows_01_upclamp_finalrange.ipr"
		;
connectAttr "c_Rt_eyebrows_01_plus.o3x" "c_Rt_eyebrows_01_upclamp_NXrange.ipr";
connectAttr "c_Rt_eyebrows_01_upmult_Xinverse.ox" "c_Rt_eyebrows_01_upclamp_PXrange.ipr"
		;
connectAttr "c_Rt_eyebrows_01_plus.o3y" "c_Rt_eyebrows_01_upclamp_PYrange.ipr";
connectAttr "c_Rt_eyebrows_02_dnScale.ox" "c_Rt_eyebrows_02_dnclamp_finalrange.ipr"
		;
connectAttr "c_Rt_eyebrows_02_dnmult_Yinverse.ox" "c_Rt_eyebrows_02_dnclamp_PYrange.ipr"
		;
connectAttr "c_Rt_eyebrows_02_lfScale.ox" "c_Rt_eyebrows_02_lfclamp_finalrange.ipr"
		;
connectAttr "c_Rt_eyebrows_02_plus.o3y" "c_Rt_eyebrows_02_lfclamp_NYrange.ipr";
connectAttr "c_Rt_eyebrows_02_lfmult_Xinverse.ox" "c_Rt_eyebrows_02_lfclamp_PXrange.ipr"
		;
connectAttr "c_Rt_eyebrows_02_lfmult_Yinverse.ox" "c_Rt_eyebrows_02_lfclamp_PYrange.ipr"
		;
connectAttr "c_Rt_eyebrows_02_rtScale.ox" "c_Rt_eyebrows_02_rtclamp_finalrange.ipr"
		;
connectAttr "c_Rt_eyebrows_02_plus.o3x" "c_Rt_eyebrows_02_rtclamp_PXrange.ipr";
connectAttr "c_Rt_eyebrows_02_upScale.ox" "c_Rt_eyebrows_02_upclamp_finalrange.ipr"
		;
connectAttr "c_Rt_eyebrows_02_plus.o3x" "c_Rt_eyebrows_02_upclamp_NXrange.ipr";
connectAttr "c_Rt_eyebrows_02_upmult_Xinverse.ox" "c_Rt_eyebrows_02_upclamp_PXrange.ipr"
		;
connectAttr "c_Rt_eyebrows_02_plus.o3y" "c_Rt_eyebrows_02_upclamp_PYrange.ipr";
connectAttr "c_Rt_eyebrows_03_dnScale.ox" "c_Rt_eyebrows_03_dnclamp_finalrange.ipr"
		;
connectAttr "c_Rt_eyebrows_03_dnmult_Yinverse.ox" "c_Rt_eyebrows_03_dnclamp_PYrange.ipr"
		;
connectAttr "c_Rt_eyebrows_03_lfScale.ox" "c_Rt_eyebrows_03_lfclamp_finalrange.ipr"
		;
connectAttr "c_Rt_eyebrows_03_plus.o3y" "c_Rt_eyebrows_03_lfclamp_NYrange.ipr";
connectAttr "c_Rt_eyebrows_03_lfmult_Xinverse.ox" "c_Rt_eyebrows_03_lfclamp_PXrange.ipr"
		;
connectAttr "c_Rt_eyebrows_03_lfmult_Yinverse.ox" "c_Rt_eyebrows_03_lfclamp_PYrange.ipr"
		;
connectAttr "c_Rt_eyebrows_03_rtScale.ox" "c_Rt_eyebrows_03_rtclamp_finalrange.ipr"
		;
connectAttr "c_Rt_eyebrows_03_plus.o3x" "c_Rt_eyebrows_03_rtclamp_PXrange.ipr";
connectAttr "c_Rt_eyebrows_03_upScale.ox" "c_Rt_eyebrows_03_upclamp_finalrange.ipr"
		;
connectAttr "c_Rt_eyebrows_03_plus.o3x" "c_Rt_eyebrows_03_upclamp_NXrange.ipr";
connectAttr "c_Rt_eyebrows_03_upmult_Xinverse.ox" "c_Rt_eyebrows_03_upclamp_PXrange.ipr"
		;
connectAttr "c_Rt_eyebrows_03_plus.o3y" "c_Rt_eyebrows_03_upclamp_PYrange.ipr";
connectAttr "c_Rt_eyeStretch_dnScale.ox" "c_Rt_eyeStretch_dnclamp_finalrange.ipr"
		;
connectAttr "c_Rt_eyeStretch_dnmult_Yinverse.ox" "c_Rt_eyeStretch_dnclamp_PYrange.ipr"
		;
connectAttr "c_Rt_eyeStretch_lfScale.ox" "c_Rt_eyeStretch_lfclamp_finalrange.ipr"
		;
connectAttr "c_Rt_cheek_CTRL.ty" "c_Rt_eyeStretch_lfclamp_NYrange.ipr";
connectAttr "c_Rt_eyeStretch_lfmult_Xinverse.ox" "c_Rt_eyeStretch_lfclamp_PXrange.ipr"
		;
connectAttr "c_Rt_eyeStretch_lfmult_Yinverse.ox" "c_Rt_eyeStretch_lfclamp_PYrange.ipr"
		;
connectAttr "c_Rt_eyeStretch_rtScale.ox" "c_Rt_eyeStretch_rtclamp_finalrange.ipr"
		;
connectAttr "c_Rt_cheek_CTRL.tx" "c_Rt_eyeStretch_rtclamp_PXrange.ipr";
connectAttr "c_Rt_eyeStretch_upScale.ox" "c_Rt_eyeStretch_upclamp_finalrange.ipr"
		;
connectAttr "c_Rt_cheek_CTRL.tx" "c_Rt_eyeStretch_upclamp_NXrange.ipr";
connectAttr "c_Rt_eyeStretch_upmult_Xinverse.ox" "c_Rt_eyeStretch_upclamp_PXrange.ipr"
		;
connectAttr "c_Rt_cheek_CTRL.ty" "c_Rt_eyeStretch_upclamp_PYrange.ipr";
connectAttr "c_Rt_mouthLip_dnScale.ox" "c_Rt_mouthLip_dnclamp_finalrange.ipr";
connectAttr "c_Rt_mouthLip_dnmult_Yinverse.ox" "c_Rt_mouthLip_dnclamp_PYrange.ipr"
		;
connectAttr "c_Rt_mouthLip_lfScale.ox" "c_Rt_mouthLip_lfclamp_finalrange.ipr";
connectAttr "c_Rt_mouthLip_CTRL.ty" "c_Rt_mouthLip_lfclamp_NYrange.ipr";
connectAttr "c_Rt_mouthLip_lfmult_Xinverse.ox" "c_Rt_mouthLip_lfclamp_PXrange.ipr"
		;
connectAttr "c_Rt_mouthLip_lfmult_Yinverse.ox" "c_Rt_mouthLip_lfclamp_PYrange.ipr"
		;
connectAttr "c_Rt_mouthLip_rtScale.ox" "c_Rt_mouthLip_rtclamp_finalrange.ipr";
connectAttr "c_Rt_mouthLip_CTRL.tx" "c_Rt_mouthLip_rtclamp_PXrange.ipr";
connectAttr "c_Rt_mouthLip_upScale.ox" "c_Rt_mouthLip_upclamp_finalrange.ipr";
connectAttr "c_Rt_mouthLip_CTRL.tx" "c_Rt_mouthLip_upclamp_NXrange.ipr";
connectAttr "c_Rt_mouthLip_upmult_Xinverse.ox" "c_Rt_mouthLip_upclamp_PXrange.ipr"
		;
connectAttr "c_Rt_mouthLip_CTRL.ty" "c_Rt_mouthLip_upclamp_PYrange.ipr";
connectAttr "c_Rt_up_eyelids_dnScale.ox" "c_Rt_up_eyelids_dnclamp_finalrange.ipr"
		;
connectAttr "c_Rt_up_eyelids_dnmult_Yinverse.ox" "c_Rt_up_eyelids_dnclamp_PYrange.ipr"
		;
connectAttr "c_Rt_up_eyelids_lfScale.ox" "c_Rt_up_eyelids_lfclamp_finalrange.ipr"
		;
connectAttr "c_Rt_up_eyelids_CTRL.ty" "c_Rt_up_eyelids_lfclamp_NYrange.ipr";
connectAttr "c_Rt_up_eyelids_lfmult_Xinverse.ox" "c_Rt_up_eyelids_lfclamp_PXrange.ipr"
		;
connectAttr "c_Rt_up_eyelids_lfmult_Yinverse.ox" "c_Rt_up_eyelids_lfclamp_PYrange.ipr"
		;
connectAttr "c_Rt_up_eyelids_rtScale.ox" "c_Rt_up_eyelids_rtclamp_finalrange.ipr"
		;
connectAttr "c_Rt_up_eyelids_CTRL.tx" "c_Rt_up_eyelids_rtclamp_PXrange.ipr";
connectAttr "c_Rt_up_eyelids_upScale.ox" "c_Rt_up_eyelids_upclamp_finalrange.ipr"
		;
connectAttr "c_Rt_up_eyelids_CTRL.tx" "c_Rt_up_eyelids_upclamp_NXrange.ipr";
connectAttr "c_Rt_up_eyelids_upmult_Xinverse.ox" "c_Rt_up_eyelids_upclamp_PXrange.ipr"
		;
connectAttr "c_Rt_up_eyelids_CTRL.ty" "c_Rt_up_eyelids_upclamp_PYrange.ipr";
connectAttr "c_up_mouthLip_dnScale.ox" "c_up_mouthLip_dnclamp_finalrange.ipr";
connectAttr "c_up_mouthLip_dnmult_Yinverse.ox" "c_up_mouthLip_dnclamp_PYrange.ipr"
		;
connectAttr "c_up_mouthLip_lfScale.ox" "c_up_mouthLip_lfclamp_finalrange.ipr";
connectAttr "c_up_mouthLip_CTRL.ty" "c_up_mouthLip_lfclamp_NYrange.ipr";
connectAttr "c_up_mouthLip_lfmult_Xinverse.ox" "c_up_mouthLip_lfclamp_PXrange.ipr"
		;
connectAttr "c_up_mouthLip_lfmult_Yinverse.ox" "c_up_mouthLip_lfclamp_PYrange.ipr"
		;
connectAttr "c_up_mouthLip_rtScale.ox" "c_up_mouthLip_rtclamp_finalrange.ipr";
connectAttr "c_up_mouthLip_CTRL.tx" "c_up_mouthLip_rtclamp_PXrange.ipr";
connectAttr "c_up_mouthLip_upScale.ox" "c_up_mouthLip_upclamp_finalrange.ipr";
connectAttr "c_up_mouthLip_CTRL.tx" "c_up_mouthLip_upclamp_NXrange.ipr";
connectAttr "c_up_mouthLip_upmult_Xinverse.ox" "c_up_mouthLip_upclamp_PXrange.ipr"
		;
connectAttr "c_up_mouthLip_CTRL.ty" "c_up_mouthLip_upclamp_PYrange.ipr";
connectAttr "E_dnScale.ox" "E_dnclamp_finalrange.ipr";
connectAttr "E_dnmult_Yinverse.ox" "E_dnclamp_PYrange.ipr";
connectAttr "E_lfScale.ox" "E_lfclamp_finalrange.ipr";
connectAttr "c_uo_CTRL.ty" "E_lfclamp_NYrange.ipr";
connectAttr "E_lfmult_Xinverse.ox" "E_lfclamp_PXrange.ipr";
connectAttr "E_lfmult_Yinverse.ox" "E_lfclamp_PYrange.ipr";
connectAttr "E_rtScale.ox" "E_rtclamp_finalrange.ipr";
connectAttr "c_uo_CTRL.tx" "E_rtclamp_PXrange.ipr";
connectAttr "E_upScale.ox" "E_upclamp_finalrange.ipr";
connectAttr "c_uo_CTRL.tx" "E_upclamp_NXrange.ipr";
connectAttr "E_upmult_Xinverse.ox" "E_upclamp_PXrange.ipr";
connectAttr "c_uo_CTRL.ty" "E_upclamp_PYrange.ipr";
connectAttr "FV_dnScale.ox" "FV_dnclamp_finalrange.ipr";
connectAttr "FV_dnmult_Yinverse.ox" "FV_dnclamp_PYrange.ipr";
connectAttr "FV_lfScale.ox" "FV_lfclamp_finalrange.ipr";
connectAttr "c_mbp_CTRL.ty" "FV_lfclamp_NYrange.ipr";
connectAttr "FV_lfmult_Xinverse.ox" "FV_lfclamp_PXrange.ipr";
connectAttr "FV_lfmult_Yinverse.ox" "FV_lfclamp_PYrange.ipr";
connectAttr "FV_rtScale.ox" "FV_rtclamp_finalrange.ipr";
connectAttr "c_mbp_CTRL.tx" "FV_rtclamp_PXrange.ipr";
connectAttr "FV_upScale.ox" "FV_upclamp_finalrange.ipr";
connectAttr "c_mbp_CTRL.tx" "FV_upclamp_NXrange.ipr";
connectAttr "FV_upmult_Xinverse.ox" "FV_upclamp_PXrange.ipr";
connectAttr "c_mbp_CTRL.ty" "FV_upclamp_PYrange.ipr";
connectAttr "I_dnScale.ox" "I_dnclamp_finalrange.ipr";
connectAttr "I_dnmult_Yinverse.ox" "I_dnclamp_PYrange.ipr";
connectAttr "I_lfScale.ox" "I_lfclamp_finalrange.ipr";
connectAttr "c_fv_CTRL.ty" "I_lfclamp_NYrange.ipr";
connectAttr "I_lfmult_Xinverse.ox" "I_lfclamp_PXrange.ipr";
connectAttr "I_lfmult_Yinverse.ox" "I_lfclamp_PYrange.ipr";
connectAttr "I_rtScale.ox" "I_rtclamp_finalrange.ipr";
connectAttr "c_fv_CTRL.tx" "I_rtclamp_PXrange.ipr";
connectAttr "I_upScale.ox" "I_upclamp_finalrange.ipr";
connectAttr "c_fv_CTRL.tx" "I_upclamp_NXrange.ipr";
connectAttr "I_upmult_Xinverse.ox" "I_upclamp_PXrange.ipr";
connectAttr "c_fv_CTRL.ty" "I_upclamp_PYrange.ipr";
connectAttr "O_dnScale.ox" "O_dnclamp_finalrange.ipr";
connectAttr "O_dnmult_Yinverse.ox" "O_dnclamp_PYrange.ipr";
connectAttr "O_lfScale.ox" "O_lfclamp_finalrange.ipr";
connectAttr "c_the_CTRL.ty" "O_lfclamp_NYrange.ipr";
connectAttr "O_lfmult_Xinverse.ox" "O_lfclamp_PXrange.ipr";
connectAttr "O_lfmult_Yinverse.ox" "O_lfclamp_PYrange.ipr";
connectAttr "O_rtScale.ox" "O_rtclamp_finalrange.ipr";
connectAttr "c_the_CTRL.tx" "O_rtclamp_PXrange.ipr";
connectAttr "O_upScale.ox" "O_upclamp_finalrange.ipr";
connectAttr "c_the_CTRL.tx" "O_upclamp_NXrange.ipr";
connectAttr "O_upmult_Xinverse.ox" "O_upclamp_PXrange.ipr";
connectAttr "c_the_CTRL.ty" "O_upclamp_PYrange.ipr";
connectAttr "OU_dnScale.ox" "OU_dnclamp_finalrange.ipr";
connectAttr "OU_dnmult_Yinverse.ox" "OU_dnclamp_PYrange.ipr";
connectAttr "OU_lfScale.ox" "OU_lfclamp_finalrange.ipr";
connectAttr "c_OU_CTRL.ty" "OU_lfclamp_NYrange.ipr";
connectAttr "OU_lfmult_Xinverse.ox" "OU_lfclamp_PXrange.ipr";
connectAttr "OU_lfmult_Yinverse.ox" "OU_lfclamp_PYrange.ipr";
connectAttr "OU_rtScale.ox" "OU_rtclamp_finalrange.ipr";
connectAttr "c_OU_CTRL.tx" "OU_rtclamp_PXrange.ipr";
connectAttr "OU_upScale.ox" "OU_upclamp_finalrange.ipr";
connectAttr "c_OU_CTRL.tx" "OU_upclamp_NXrange.ipr";
connectAttr "OU_upmult_Xinverse.ox" "OU_upclamp_PXrange.ipr";
connectAttr "c_OU_CTRL.ty" "OU_upclamp_PYrange.ipr";
connectAttr "tongue_dnScale.ox" "tongue_dnclamp_finalrange.ipr";
connectAttr "tongue_dnmult_Yinverse.ox" "tongue_dnclamp_PYrange.ipr";
connectAttr "tongue_lfScale.ox" "tongue_lfclamp_finalrange.ipr";
connectAttr "c_tongue_CTRL.ty" "tongue_lfclamp_NYrange.ipr";
connectAttr "tongue_lfmult_Xinverse.ox" "tongue_lfclamp_PXrange.ipr";
connectAttr "tongue_lfmult_Yinverse.ox" "tongue_lfclamp_PYrange.ipr";
connectAttr "tongue_rtScale.ox" "tongue_rtclamp_finalrange.ipr";
connectAttr "c_tongue_CTRL.tx" "tongue_rtclamp_PXrange.ipr";
connectAttr "tongue_upScale.ox" "tongue_upclamp_finalrange.ipr";
connectAttr "c_tongue_CTRL.tx" "tongue_upclamp_NXrange.ipr";
connectAttr "tongue_upmult_Xinverse.ox" "tongue_upclamp_PXrange.ipr";
connectAttr "c_tongue_CTRL.ty" "tongue_upclamp_PYrange.ipr";
connectAttr "U_dnScale.ox" "U_dnclamp_finalrange.ipr";
connectAttr "U_dnmult_Yinverse.ox" "U_dnclamp_PYrange.ipr";
connectAttr "U_lfScale.ox" "U_lfclamp_finalrange.ipr";
connectAttr "c_eeesz_CTRL.ty" "U_lfclamp_NYrange.ipr";
connectAttr "U_lfmult_Xinverse.ox" "U_lfclamp_PXrange.ipr";
connectAttr "U_lfmult_Yinverse.ox" "U_lfclamp_PYrange.ipr";
connectAttr "U_rtScale.ox" "U_rtclamp_finalrange.ipr";
connectAttr "c_eeesz_CTRL.tx" "U_rtclamp_PXrange.ipr";
connectAttr "U_upScale.ox" "U_upclamp_finalrange.ipr";
connectAttr "c_eeesz_CTRL.tx" "U_upclamp_NXrange.ipr";
connectAttr "U_upmult_Xinverse.ox" "U_upclamp_PXrange.ipr";
connectAttr "c_eeesz_CTRL.ty" "U_upclamp_PYrange.ipr";
connectAttr "Facial_CTRL_FRAME_GRP.msg" "bindPose1.m[0]";
connectAttr "Facial_CTRL_FRAME.msg" "bindPose1.m[1]";
connectAttr "head_CTRL_GRP.msg" "bindPose1.m[2]";
connectAttr "head_CTRL.msg" "bindPose1.m[3]";
connectAttr "c_mouth_CTRL_GRP.msg" "bindPose1.m[4]";
connectAttr "c_mouth_CTRL.msg" "bindPose1.m[5]";
connectAttr "GRP_c_jaw_dn_FRAME.msg" "bindPose1.m[6]";
connectAttr "c_jaw_dn_FRAME.msg" "bindPose1.m[7]";
connectAttr "GRP_c_jaw_dn_CTRL.msg" "bindPose1.m[8]";
connectAttr "c_jaw_dn_CTRL.msg" "bindPose1.m[9]";
connectAttr "GRP_c_dn_mouthLip_FRAME.msg" "bindPose1.m[10]";
connectAttr "c_dn_mouthLip_FRAME.msg" "bindPose1.m[11]";
connectAttr "GRP_c_dn_mouthLip_CTRL.msg" "bindPose1.m[12]";
connectAttr "c_dn_mouthLip_CTRL.msg" "bindPose1.m[13]";
connectAttr "c_dn_mouthLip_CTRL_joint1_GRP.msg" "bindPose1.m[14]";
connectAttr "c_dn_mouthLip_CTRL_joint1.msg" "bindPose1.m[15]";
connectAttr "c_jaw_dn_CTRL_joint1_GRP.msg" "bindPose1.m[16]";
connectAttr "c_jaw_dn_CTRL_joint1.msg" "bindPose1.m[17]";
connectAttr "GRP_c_up_mouthLip_FRAME.msg" "bindPose1.m[18]";
connectAttr "c_up_mouthLip_FRAME.msg" "bindPose1.m[19]";
connectAttr "GRP_c_up_mouthLip_CTRL.msg" "bindPose1.m[20]";
connectAttr "c_up_mouthLip_CTRL.msg" "bindPose1.m[21]";
connectAttr "c_up_mouthLip_CTRL_joint1_GRP.msg" "bindPose1.m[22]";
connectAttr "c_up_mouthLip_CTRL_joint1.msg" "bindPose1.m[23]";
connectAttr "GRP_c_Lf_mouthLip_FRAME.msg" "bindPose1.m[24]";
connectAttr "c_Lf_mouthLip_FRAME.msg" "bindPose1.m[25]";
connectAttr "GRP_c_Lf_mouthLip_CTRL.msg" "bindPose1.m[26]";
connectAttr "c_Lf_mouthLip_CTRL.msg" "bindPose1.m[27]";
connectAttr "c_Lf_mouthLip_CTRL_joint1_GRP.msg" "bindPose1.m[28]";
connectAttr "c_Lf_mouthLip_CTRL_joint1.msg" "bindPose1.m[29]";
connectAttr "GRP_c_Rt_mouthLip_FRAME.msg" "bindPose1.m[30]";
connectAttr "c_Rt_mouthLip_FRAME.msg" "bindPose1.m[31]";
connectAttr "GRP_c_Rt_mouthLip_CTRL.msg" "bindPose1.m[32]";
connectAttr "c_Rt_mouthLip_CTRL.msg" "bindPose1.m[33]";
connectAttr "c_Rt_mouthLip_CTRL_joint1_GRP.msg" "bindPose1.m[34]";
connectAttr "c_Rt_mouthLip_CTRL_joint1.msg" "bindPose1.m[35]";
connectAttr "bindPose1.w" "bindPose1.p[0]";
connectAttr "bindPose1.m[0]" "bindPose1.p[1]";
connectAttr "bindPose1.m[1]" "bindPose1.p[2]";
connectAttr "bindPose1.m[2]" "bindPose1.p[3]";
connectAttr "bindPose1.m[3]" "bindPose1.p[4]";
connectAttr "bindPose1.m[4]" "bindPose1.p[5]";
connectAttr "bindPose1.m[5]" "bindPose1.p[6]";
connectAttr "bindPose1.m[6]" "bindPose1.p[7]";
connectAttr "bindPose1.m[7]" "bindPose1.p[8]";
connectAttr "bindPose1.m[8]" "bindPose1.p[9]";
connectAttr "bindPose1.m[9]" "bindPose1.p[10]";
connectAttr "bindPose1.m[10]" "bindPose1.p[11]";
connectAttr "bindPose1.m[11]" "bindPose1.p[12]";
connectAttr "bindPose1.m[12]" "bindPose1.p[13]";
connectAttr "bindPose1.m[13]" "bindPose1.p[14]";
connectAttr "bindPose1.m[14]" "bindPose1.p[15]";
connectAttr "bindPose1.m[9]" "bindPose1.p[16]";
connectAttr "bindPose1.m[16]" "bindPose1.p[17]";
connectAttr "bindPose1.m[5]" "bindPose1.p[18]";
connectAttr "bindPose1.m[18]" "bindPose1.p[19]";
connectAttr "bindPose1.m[19]" "bindPose1.p[20]";
connectAttr "bindPose1.m[20]" "bindPose1.p[21]";
connectAttr "bindPose1.m[21]" "bindPose1.p[22]";
connectAttr "bindPose1.m[22]" "bindPose1.p[23]";
connectAttr "bindPose1.m[5]" "bindPose1.p[24]";
connectAttr "bindPose1.m[24]" "bindPose1.p[25]";
connectAttr "bindPose1.m[25]" "bindPose1.p[26]";
connectAttr "bindPose1.m[26]" "bindPose1.p[27]";
connectAttr "bindPose1.m[27]" "bindPose1.p[28]";
connectAttr "bindPose1.m[28]" "bindPose1.p[29]";
connectAttr "bindPose1.m[5]" "bindPose1.p[30]";
connectAttr "bindPose1.m[30]" "bindPose1.p[31]";
connectAttr "bindPose1.m[31]" "bindPose1.p[32]";
connectAttr "bindPose1.m[32]" "bindPose1.p[33]";
connectAttr "bindPose1.m[33]" "bindPose1.p[34]";
connectAttr "bindPose1.m[34]" "bindPose1.p[35]";
connectAttr "c_dn_mouthLip_CTRL_joint1.bps" "bindPose1.wm[15]";
connectAttr "c_jaw_dn_CTRL_joint1.bps" "bindPose1.wm[17]";
connectAttr "c_up_mouthLip_CTRL_joint1.bps" "bindPose1.wm[23]";
connectAttr "c_Lf_mouthLip_CTRL_joint1.bps" "bindPose1.wm[29]";
connectAttr "c_Rt_mouthLip_CTRL_joint1.bps" "bindPose1.wm[35]";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "c_tongue_CTRL.tx" "c_tongue_CTRL_ex.in[0]";
connectAttr "c_tongue_CTRL.tx_scale" "c_tongue_CTRL_ex.in[1]";
connectAttr "c_tongue_CTRL.ty" "c_tongue_CTRL_ex.in[2]";
connectAttr "c_tongue_CTRL.ty_scale" "c_tongue_CTRL_ex.in[3]";
connectAttr "unitConversion1.o" "c_tongue_CTRL_ex.in[4]";
connectAttr "c_tongue_CTRL.rx_scale" "c_tongue_CTRL_ex.in[5]";
connectAttr "unitConversion2.o" "c_tongue_CTRL_ex.in[6]";
connectAttr "c_tongue_CTRL.ry_scale" "c_tongue_CTRL_ex.in[7]";
connectAttr "unitConversion3.o" "c_tongue_CTRL_ex.in[8]";
connectAttr "c_tongue_CTRL.rz_scale" "c_tongue_CTRL_ex.in[9]";
connectAttr "c_tongue_CTRL.stretch" "c_tongue_CTRL_ex.in[10]";
connectAttr "c_tongue_CTRL.stretch_scale" "c_tongue_CTRL_ex.in[11]";
connectAttr "Facial_CTRL_FRAME_GRP.msg" "c_tongue_CTRL_ex.tim";
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
connectAttr "c_a_CTRL.ty" "A_dnmult_Yinverse.i2x";
connectAttr "A_dnclamp_PYrange.opr" "A_dnScale.i1x";
connectAttr "A_upreverse_X.ox" "A_dnScale.i2x";
connectAttr "A_lfclamp_PYrange.opr" "A_lfdnmult.i1x";
connectAttr "A_upclamp_PXrange.opr" "A_lfdnmult.i2x";
connectAttr "c_a_CTRL.tx" "A_lfmult_Xinverse.i2x";
connectAttr "c_a_CTRL.ty" "A_lfmult_Yinverse.i2x";
connectAttr "A_lfclamp_PXrange.opr" "A_lfScale.i1x";
connectAttr "A_lfreverse_Y.ox" "A_lfScale.i2x";
connectAttr "A_lfclamp_NYrange.opr" "A_lfupmult.i1x";
connectAttr "A_upclamp_PXrange.opr" "A_lfupmult.i2x";
connectAttr "A_lfclamp_PYrange.opr" "A_rtdnmult.i1x";
connectAttr "A_upclamp_NXrange.opr" "A_rtdnmult.i2x";
connectAttr "A_rtclamp_PXrange.opr" "A_rtScale.i1x";
connectAttr "A_lfreverse_Y.ox" "A_rtScale.i2x";
connectAttr "A_lfclamp_NYrange.opr" "A_rtupmult.i1x";
connectAttr "A_upclamp_NXrange.opr" "A_rtupmult.i2x";
connectAttr "c_a_CTRL.tx" "A_upmult_Xinverse.i2x";
connectAttr "A_upclamp_PYrange.opr" "A_upScale.i1x";
connectAttr "A_upreverse_X.ox" "A_upScale.i2x";
connectAttr "c_dn_mouthLip_CTRL.ty" "c_dn_mouthLip_dnmult_Yinverse.i2x";
connectAttr "c_dn_mouthLip_dnclamp_PYrange.opr" "c_dn_mouthLip_dnScale.i1x";
connectAttr "c_dn_mouthLip_upreverse_X.ox" "c_dn_mouthLip_dnScale.i2x";
connectAttr "c_dn_mouthLip_lfclamp_PYrange.opr" "c_dn_mouthLip_lfdnmult.i1x";
connectAttr "c_dn_mouthLip_upclamp_PXrange.opr" "c_dn_mouthLip_lfdnmult.i2x";
connectAttr "c_dn_mouthLip_CTRL.tx" "c_dn_mouthLip_lfmult_Xinverse.i2x";
connectAttr "c_dn_mouthLip_CTRL.ty" "c_dn_mouthLip_lfmult_Yinverse.i2x";
connectAttr "c_dn_mouthLip_lfclamp_PXrange.opr" "c_dn_mouthLip_lfScale.i1x";
connectAttr "c_dn_mouthLip_lfreverse_Y.ox" "c_dn_mouthLip_lfScale.i2x";
connectAttr "c_dn_mouthLip_lfclamp_NYrange.opr" "c_dn_mouthLip_lfupmult.i1x";
connectAttr "c_dn_mouthLip_upclamp_PXrange.opr" "c_dn_mouthLip_lfupmult.i2x";
connectAttr "c_dn_mouthLip_lfclamp_PYrange.opr" "c_dn_mouthLip_rtdnmult.i1x";
connectAttr "c_dn_mouthLip_upclamp_NXrange.opr" "c_dn_mouthLip_rtdnmult.i2x";
connectAttr "c_dn_mouthLip_rtclamp_PXrange.opr" "c_dn_mouthLip_rtScale.i1x";
connectAttr "c_dn_mouthLip_lfreverse_Y.ox" "c_dn_mouthLip_rtScale.i2x";
connectAttr "c_dn_mouthLip_lfclamp_NYrange.opr" "c_dn_mouthLip_rtupmult.i1x";
connectAttr "c_dn_mouthLip_upclamp_NXrange.opr" "c_dn_mouthLip_rtupmult.i2x";
connectAttr "c_dn_mouthLip_CTRL.tx" "c_dn_mouthLip_upmult_Xinverse.i2x";
connectAttr "c_dn_mouthLip_upclamp_PYrange.opr" "c_dn_mouthLip_upScale.i1x";
connectAttr "c_dn_mouthLip_upreverse_X.ox" "c_dn_mouthLip_upScale.i2x";
connectAttr "c_jaw_dn_CTRL.ty" "c_jaw_dn_dnmult_Yinverse.i2x";
connectAttr "c_jaw_dn_dnclamp_PYrange.opr" "c_jaw_dn_dnScale.i1x";
connectAttr "c_jaw_dn_upreverse_X.ox" "c_jaw_dn_dnScale.i2x";
connectAttr "c_jaw_dn_lfclamp_PYrange.opr" "c_jaw_dn_lfdnmult.i1x";
connectAttr "c_jaw_dn_upclamp_PXrange.opr" "c_jaw_dn_lfdnmult.i2x";
connectAttr "c_jaw_dn_CTRL.tx" "c_jaw_dn_lfmult_Xinverse.i2x";
connectAttr "c_jaw_dn_CTRL.ty" "c_jaw_dn_lfmult_Yinverse.i2x";
connectAttr "c_jaw_dn_lfclamp_PXrange.opr" "c_jaw_dn_lfScale.i1x";
connectAttr "c_jaw_dn_lfreverse_Y.ox" "c_jaw_dn_lfScale.i2x";
connectAttr "c_jaw_dn_lfclamp_NYrange.opr" "c_jaw_dn_lfupmult.i1x";
connectAttr "c_jaw_dn_upclamp_PXrange.opr" "c_jaw_dn_lfupmult.i2x";
connectAttr "c_jaw_dn_lfclamp_PYrange.opr" "c_jaw_dn_rtdnmult.i1x";
connectAttr "c_jaw_dn_upclamp_NXrange.opr" "c_jaw_dn_rtdnmult.i2x";
connectAttr "c_jaw_dn_rtclamp_PXrange.opr" "c_jaw_dn_rtScale.i1x";
connectAttr "c_jaw_dn_lfreverse_Y.ox" "c_jaw_dn_rtScale.i2x";
connectAttr "c_jaw_dn_lfclamp_NYrange.opr" "c_jaw_dn_rtupmult.i1x";
connectAttr "c_jaw_dn_upclamp_NXrange.opr" "c_jaw_dn_rtupmult.i2x";
connectAttr "c_jaw_dn_CTRL.tx" "c_jaw_dn_upmult_Xinverse.i2x";
connectAttr "c_jaw_dn_upclamp_PYrange.opr" "c_jaw_dn_upScale.i1x";
connectAttr "c_jaw_dn_upreverse_X.ox" "c_jaw_dn_upScale.i2x";
connectAttr "c_jaw_up_CTRL.ty" "c_jaw_up_dnmult_Yinverse.i2x";
connectAttr "c_jaw_up_dnclamp_PYrange.opr" "c_jaw_up_dnScale.i1x";
connectAttr "c_jaw_up_upreverse_X.ox" "c_jaw_up_dnScale.i2x";
connectAttr "c_jaw_up_lfclamp_PYrange.opr" "c_jaw_up_lfdnmult.i1x";
connectAttr "c_jaw_up_upclamp_PXrange.opr" "c_jaw_up_lfdnmult.i2x";
connectAttr "c_jaw_up_CTRL.tx" "c_jaw_up_lfmult_Xinverse.i2x";
connectAttr "c_jaw_up_CTRL.ty" "c_jaw_up_lfmult_Yinverse.i2x";
connectAttr "c_jaw_up_lfclamp_PXrange.opr" "c_jaw_up_lfScale.i1x";
connectAttr "c_jaw_up_lfreverse_Y.ox" "c_jaw_up_lfScale.i2x";
connectAttr "c_jaw_up_lfclamp_NYrange.opr" "c_jaw_up_lfupmult.i1x";
connectAttr "c_jaw_up_upclamp_PXrange.opr" "c_jaw_up_lfupmult.i2x";
connectAttr "c_jaw_up_lfclamp_PYrange.opr" "c_jaw_up_rtdnmult.i1x";
connectAttr "c_jaw_up_upclamp_NXrange.opr" "c_jaw_up_rtdnmult.i2x";
connectAttr "c_jaw_up_rtclamp_PXrange.opr" "c_jaw_up_rtScale.i1x";
connectAttr "c_jaw_up_lfreverse_Y.ox" "c_jaw_up_rtScale.i2x";
connectAttr "c_jaw_up_lfclamp_NYrange.opr" "c_jaw_up_rtupmult.i1x";
connectAttr "c_jaw_up_upclamp_NXrange.opr" "c_jaw_up_rtupmult.i2x";
connectAttr "c_jaw_up_CTRL.tx" "c_jaw_up_upmult_Xinverse.i2x";
connectAttr "c_jaw_up_upclamp_PYrange.opr" "c_jaw_up_upScale.i1x";
connectAttr "c_jaw_up_upreverse_X.ox" "c_jaw_up_upScale.i2x";
connectAttr "c_Lf_dn_eyelids_CTRL.ty" "c_Lf_dn_eyelids_dnmult_Yinverse.i2x";
connectAttr "c_Lf_dn_eyelids_dnclamp_PYrange.opr" "c_Lf_dn_eyelids_dnScale.i1x";
connectAttr "c_Lf_dn_eyelids_upreverse_X.ox" "c_Lf_dn_eyelids_dnScale.i2x";
connectAttr "c_Lf_dn_eyelids_lfclamp_PYrange.opr" "c_Lf_dn_eyelids_lfdnmult.i1x"
		;
connectAttr "c_Lf_dn_eyelids_upclamp_PXrange.opr" "c_Lf_dn_eyelids_lfdnmult.i2x"
		;
connectAttr "c_Lf_dn_eyelids_CTRL.tx" "c_Lf_dn_eyelids_lfmult_Xinverse.i2x";
connectAttr "c_Lf_dn_eyelids_CTRL.ty" "c_Lf_dn_eyelids_lfmult_Yinverse.i2x";
connectAttr "c_Lf_dn_eyelids_lfclamp_PXrange.opr" "c_Lf_dn_eyelids_lfScale.i1x";
connectAttr "c_Lf_dn_eyelids_lfreverse_Y.ox" "c_Lf_dn_eyelids_lfScale.i2x";
connectAttr "c_Lf_dn_eyelids_lfclamp_NYrange.opr" "c_Lf_dn_eyelids_lfupmult.i1x"
		;
connectAttr "c_Lf_dn_eyelids_upclamp_PXrange.opr" "c_Lf_dn_eyelids_lfupmult.i2x"
		;
connectAttr "c_Lf_dn_eyelids_lfclamp_PYrange.opr" "c_Lf_dn_eyelids_rtdnmult.i1x"
		;
connectAttr "c_Lf_dn_eyelids_upclamp_NXrange.opr" "c_Lf_dn_eyelids_rtdnmult.i2x"
		;
connectAttr "c_Lf_dn_eyelids_rtclamp_PXrange.opr" "c_Lf_dn_eyelids_rtScale.i1x";
connectAttr "c_Lf_dn_eyelids_lfreverse_Y.ox" "c_Lf_dn_eyelids_rtScale.i2x";
connectAttr "c_Lf_dn_eyelids_lfclamp_NYrange.opr" "c_Lf_dn_eyelids_rtupmult.i1x"
		;
connectAttr "c_Lf_dn_eyelids_upclamp_NXrange.opr" "c_Lf_dn_eyelids_rtupmult.i2x"
		;
connectAttr "c_Lf_dn_eyelids_CTRL.tx" "c_Lf_dn_eyelids_upmult_Xinverse.i2x";
connectAttr "c_Lf_dn_eyelids_upclamp_PYrange.opr" "c_Lf_dn_eyelids_upScale.i1x";
connectAttr "c_Lf_dn_eyelids_upreverse_X.ox" "c_Lf_dn_eyelids_upScale.i2x";
connectAttr "c_Lf_eyebrows_01_plus.o3y" "c_Lf_eyebrows_01_dnmult_Yinverse.i2x";
connectAttr "c_Lf_eyebrows_01_dnclamp_PYrange.opr" "c_Lf_eyebrows_01_dnScale.i1x"
		;
connectAttr "c_Lf_eyebrows_01_upreverse_X.ox" "c_Lf_eyebrows_01_dnScale.i2x";
connectAttr "c_Lf_eyebrows_01_lfclamp_PYrange.opr" "c_Lf_eyebrows_01_lfdnmult.i1x"
		;
connectAttr "c_Lf_eyebrows_01_upclamp_PXrange.opr" "c_Lf_eyebrows_01_lfdnmult.i2x"
		;
connectAttr "c_Lf_eyebrows_01_plus.o3x" "c_Lf_eyebrows_01_lfmult_Xinverse.i2x";
connectAttr "c_Lf_eyebrows_01_plus.o3y" "c_Lf_eyebrows_01_lfmult_Yinverse.i2x";
connectAttr "c_Lf_eyebrows_01_lfclamp_PXrange.opr" "c_Lf_eyebrows_01_lfScale.i1x"
		;
connectAttr "c_Lf_eyebrows_01_lfreverse_Y.ox" "c_Lf_eyebrows_01_lfScale.i2x";
connectAttr "c_Lf_eyebrows_01_lfclamp_NYrange.opr" "c_Lf_eyebrows_01_lfupmult.i1x"
		;
connectAttr "c_Lf_eyebrows_01_upclamp_PXrange.opr" "c_Lf_eyebrows_01_lfupmult.i2x"
		;
connectAttr "c_Lf_eyebrows_01_lfclamp_PYrange.opr" "c_Lf_eyebrows_01_rtdnmult.i1x"
		;
connectAttr "c_Lf_eyebrows_01_upclamp_NXrange.opr" "c_Lf_eyebrows_01_rtdnmult.i2x"
		;
connectAttr "c_Lf_eyebrows_01_rtclamp_PXrange.opr" "c_Lf_eyebrows_01_rtScale.i1x"
		;
connectAttr "c_Lf_eyebrows_01_lfreverse_Y.ox" "c_Lf_eyebrows_01_rtScale.i2x";
connectAttr "c_Lf_eyebrows_01_lfclamp_NYrange.opr" "c_Lf_eyebrows_01_rtupmult.i1x"
		;
connectAttr "c_Lf_eyebrows_01_upclamp_NXrange.opr" "c_Lf_eyebrows_01_rtupmult.i2x"
		;
connectAttr "c_Lf_eyebrows_01_plus.o3x" "c_Lf_eyebrows_01_upmult_Xinverse.i2x";
connectAttr "c_Lf_eyebrows_01_upclamp_PYrange.opr" "c_Lf_eyebrows_01_upScale.i1x"
		;
connectAttr "c_Lf_eyebrows_01_upreverse_X.ox" "c_Lf_eyebrows_01_upScale.i2x";
connectAttr "c_Lf_eyebrows_02_plus.o3y" "c_Lf_eyebrows_02_dnmult_Yinverse.i2x";
connectAttr "c_Lf_eyebrows_02_dnclamp_PYrange.opr" "c_Lf_eyebrows_02_dnScale.i1x"
		;
connectAttr "c_Lf_eyebrows_02_upreverse_X.ox" "c_Lf_eyebrows_02_dnScale.i2x";
connectAttr "c_Lf_eyebrows_02_lfclamp_PYrange.opr" "c_Lf_eyebrows_02_lfdnmult.i1x"
		;
connectAttr "c_Lf_eyebrows_02_upclamp_PXrange.opr" "c_Lf_eyebrows_02_lfdnmult.i2x"
		;
connectAttr "c_Lf_eyebrows_02_plus.o3x" "c_Lf_eyebrows_02_lfmult_Xinverse.i2x";
connectAttr "c_Lf_eyebrows_02_plus.o3y" "c_Lf_eyebrows_02_lfmult_Yinverse.i2x";
connectAttr "c_Lf_eyebrows_02_lfclamp_PXrange.opr" "c_Lf_eyebrows_02_lfScale.i1x"
		;
connectAttr "c_Lf_eyebrows_02_lfreverse_Y.ox" "c_Lf_eyebrows_02_lfScale.i2x";
connectAttr "c_Lf_eyebrows_02_lfclamp_NYrange.opr" "c_Lf_eyebrows_02_lfupmult.i1x"
		;
connectAttr "c_Lf_eyebrows_02_upclamp_PXrange.opr" "c_Lf_eyebrows_02_lfupmult.i2x"
		;
connectAttr "c_Lf_eyebrows_02_lfclamp_PYrange.opr" "c_Lf_eyebrows_02_rtdnmult.i1x"
		;
connectAttr "c_Lf_eyebrows_02_upclamp_NXrange.opr" "c_Lf_eyebrows_02_rtdnmult.i2x"
		;
connectAttr "c_Lf_eyebrows_02_rtclamp_PXrange.opr" "c_Lf_eyebrows_02_rtScale.i1x"
		;
connectAttr "c_Lf_eyebrows_02_lfreverse_Y.ox" "c_Lf_eyebrows_02_rtScale.i2x";
connectAttr "c_Lf_eyebrows_02_lfclamp_NYrange.opr" "c_Lf_eyebrows_02_rtupmult.i1x"
		;
connectAttr "c_Lf_eyebrows_02_upclamp_NXrange.opr" "c_Lf_eyebrows_02_rtupmult.i2x"
		;
connectAttr "c_Lf_eyebrows_02_plus.o3x" "c_Lf_eyebrows_02_upmult_Xinverse.i2x";
connectAttr "c_Lf_eyebrows_02_upclamp_PYrange.opr" "c_Lf_eyebrows_02_upScale.i1x"
		;
connectAttr "c_Lf_eyebrows_02_upreverse_X.ox" "c_Lf_eyebrows_02_upScale.i2x";
connectAttr "c_Lf_eyebrows_03_plus.o3y" "c_Lf_eyebrows_03_dnmult_Yinverse.i2x";
connectAttr "c_Lf_eyebrows_03_dnclamp_PYrange.opr" "c_Lf_eyebrows_03_dnScale.i1x"
		;
connectAttr "c_Lf_eyebrows_03_upreverse_X.ox" "c_Lf_eyebrows_03_dnScale.i2x";
connectAttr "c_Lf_eyebrows_03_lfclamp_PYrange.opr" "c_Lf_eyebrows_03_lfdnmult.i1x"
		;
connectAttr "c_Lf_eyebrows_03_upclamp_PXrange.opr" "c_Lf_eyebrows_03_lfdnmult.i2x"
		;
connectAttr "c_Lf_eyebrows_03_plus.o3x" "c_Lf_eyebrows_03_lfmult_Xinverse.i2x";
connectAttr "c_Lf_eyebrows_03_plus.o3y" "c_Lf_eyebrows_03_lfmult_Yinverse.i2x";
connectAttr "c_Lf_eyebrows_03_lfclamp_PXrange.opr" "c_Lf_eyebrows_03_lfScale.i1x"
		;
connectAttr "c_Lf_eyebrows_03_lfreverse_Y.ox" "c_Lf_eyebrows_03_lfScale.i2x";
connectAttr "c_Lf_eyebrows_03_lfclamp_NYrange.opr" "c_Lf_eyebrows_03_lfupmult.i1x"
		;
connectAttr "c_Lf_eyebrows_03_upclamp_PXrange.opr" "c_Lf_eyebrows_03_lfupmult.i2x"
		;
connectAttr "c_Lf_eyebrows_03_lfclamp_PYrange.opr" "c_Lf_eyebrows_03_rtdnmult.i1x"
		;
connectAttr "c_Lf_eyebrows_03_upclamp_NXrange.opr" "c_Lf_eyebrows_03_rtdnmult.i2x"
		;
connectAttr "c_Lf_eyebrows_03_rtclamp_PXrange.opr" "c_Lf_eyebrows_03_rtScale.i1x"
		;
connectAttr "c_Lf_eyebrows_03_lfreverse_Y.ox" "c_Lf_eyebrows_03_rtScale.i2x";
connectAttr "c_Lf_eyebrows_03_lfclamp_NYrange.opr" "c_Lf_eyebrows_03_rtupmult.i1x"
		;
connectAttr "c_Lf_eyebrows_03_upclamp_NXrange.opr" "c_Lf_eyebrows_03_rtupmult.i2x"
		;
connectAttr "c_Lf_eyebrows_03_plus.o3x" "c_Lf_eyebrows_03_upmult_Xinverse.i2x";
connectAttr "c_Lf_eyebrows_03_upclamp_PYrange.opr" "c_Lf_eyebrows_03_upScale.i1x"
		;
connectAttr "c_Lf_eyebrows_03_upreverse_X.ox" "c_Lf_eyebrows_03_upScale.i2x";
connectAttr "c_Lf_cheek_CTRL.ty" "c_Lf_eyeStretch_dnmult_Yinverse.i2x";
connectAttr "c_Lf_eyeStretch_dnclamp_PYrange.opr" "c_Lf_eyeStretch_dnScale.i1x";
connectAttr "c_Lf_eyeStretch_upreverse_X.ox" "c_Lf_eyeStretch_dnScale.i2x";
connectAttr "c_Lf_eyeStretch_lfclamp_PYrange.opr" "c_Lf_eyeStretch_lfdnmult.i1x"
		;
connectAttr "c_Lf_eyeStretch_upclamp_PXrange.opr" "c_Lf_eyeStretch_lfdnmult.i2x"
		;
connectAttr "c_Lf_cheek_CTRL.tx" "c_Lf_eyeStretch_lfmult_Xinverse.i2x";
connectAttr "c_Lf_cheek_CTRL.ty" "c_Lf_eyeStretch_lfmult_Yinverse.i2x";
connectAttr "c_Lf_eyeStretch_lfclamp_PXrange.opr" "c_Lf_eyeStretch_lfScale.i1x";
connectAttr "c_Lf_eyeStretch_lfreverse_Y.ox" "c_Lf_eyeStretch_lfScale.i2x";
connectAttr "c_Lf_eyeStretch_lfclamp_NYrange.opr" "c_Lf_eyeStretch_lfupmult.i1x"
		;
connectAttr "c_Lf_eyeStretch_upclamp_PXrange.opr" "c_Lf_eyeStretch_lfupmult.i2x"
		;
connectAttr "c_Lf_eyeStretch_lfclamp_PYrange.opr" "c_Lf_eyeStretch_rtdnmult.i1x"
		;
connectAttr "c_Lf_eyeStretch_upclamp_NXrange.opr" "c_Lf_eyeStretch_rtdnmult.i2x"
		;
connectAttr "c_Lf_eyeStretch_rtclamp_PXrange.opr" "c_Lf_eyeStretch_rtScale.i1x";
connectAttr "c_Lf_eyeStretch_lfreverse_Y.ox" "c_Lf_eyeStretch_rtScale.i2x";
connectAttr "c_Lf_eyeStretch_lfclamp_NYrange.opr" "c_Lf_eyeStretch_rtupmult.i1x"
		;
connectAttr "c_Lf_eyeStretch_upclamp_NXrange.opr" "c_Lf_eyeStretch_rtupmult.i2x"
		;
connectAttr "c_Lf_cheek_CTRL.tx" "c_Lf_eyeStretch_upmult_Xinverse.i2x";
connectAttr "c_Lf_eyeStretch_upclamp_PYrange.opr" "c_Lf_eyeStretch_upScale.i1x";
connectAttr "c_Lf_eyeStretch_upreverse_X.ox" "c_Lf_eyeStretch_upScale.i2x";
connectAttr "c_Lf_mouthLip_CTRL.ty" "c_Lf_mouthLip_dnmult_Yinverse.i2x";
connectAttr "c_Lf_mouthLip_dnclamp_PYrange.opr" "c_Lf_mouthLip_dnScale.i1x";
connectAttr "c_Lf_mouthLip_upreverse_X.ox" "c_Lf_mouthLip_dnScale.i2x";
connectAttr "c_Lf_mouthLip_lfclamp_PYrange.opr" "c_Lf_mouthLip_lfdnmult.i1x";
connectAttr "c_Lf_mouthLip_upclamp_PXrange.opr" "c_Lf_mouthLip_lfdnmult.i2x";
connectAttr "c_Lf_mouthLip_CTRL.tx" "c_Lf_mouthLip_lfmult_Xinverse.i2x";
connectAttr "c_Lf_mouthLip_CTRL.ty" "c_Lf_mouthLip_lfmult_Yinverse.i2x";
connectAttr "c_Lf_mouthLip_lfclamp_PXrange.opr" "c_Lf_mouthLip_lfScale.i1x";
connectAttr "c_Lf_mouthLip_lfreverse_Y.ox" "c_Lf_mouthLip_lfScale.i2x";
connectAttr "c_Lf_mouthLip_lfclamp_NYrange.opr" "c_Lf_mouthLip_lfupmult.i1x";
connectAttr "c_Lf_mouthLip_upclamp_PXrange.opr" "c_Lf_mouthLip_lfupmult.i2x";
connectAttr "c_Lf_mouthLip_lfclamp_PYrange.opr" "c_Lf_mouthLip_rtdnmult.i1x";
connectAttr "c_Lf_mouthLip_upclamp_NXrange.opr" "c_Lf_mouthLip_rtdnmult.i2x";
connectAttr "c_Lf_mouthLip_rtclamp_PXrange.opr" "c_Lf_mouthLip_rtScale.i1x";
connectAttr "c_Lf_mouthLip_lfreverse_Y.ox" "c_Lf_mouthLip_rtScale.i2x";
connectAttr "c_Lf_mouthLip_lfclamp_NYrange.opr" "c_Lf_mouthLip_rtupmult.i1x";
connectAttr "c_Lf_mouthLip_upclamp_NXrange.opr" "c_Lf_mouthLip_rtupmult.i2x";
connectAttr "c_Lf_mouthLip_CTRL.tx" "c_Lf_mouthLip_upmult_Xinverse.i2x";
connectAttr "c_Lf_mouthLip_upclamp_PYrange.opr" "c_Lf_mouthLip_upScale.i1x";
connectAttr "c_Lf_mouthLip_upreverse_X.ox" "c_Lf_mouthLip_upScale.i2x";
connectAttr "c_Lf_up_eyelids_CTRL.ty" "c_Lf_up_eyelids_dnmult_Yinverse.i2x";
connectAttr "c_Lf_up_eyelids_dnclamp_PYrange.opr" "c_Lf_up_eyelids_dnScale.i1x";
connectAttr "c_Lf_up_eyelids_upreverse_X.ox" "c_Lf_up_eyelids_dnScale.i2x";
connectAttr "c_Lf_up_eyelids_lfclamp_PYrange.opr" "c_Lf_up_eyelids_lfdnmult.i1x"
		;
connectAttr "c_Lf_up_eyelids_upclamp_PXrange.opr" "c_Lf_up_eyelids_lfdnmult.i2x"
		;
connectAttr "c_Lf_up_eyelids_CTRL.tx" "c_Lf_up_eyelids_lfmult_Xinverse.i2x";
connectAttr "c_Lf_up_eyelids_CTRL.ty" "c_Lf_up_eyelids_lfmult_Yinverse.i2x";
connectAttr "c_Lf_up_eyelids_lfclamp_PXrange.opr" "c_Lf_up_eyelids_lfScale.i1x";
connectAttr "c_Lf_up_eyelids_lfreverse_Y.ox" "c_Lf_up_eyelids_lfScale.i2x";
connectAttr "c_Lf_up_eyelids_lfclamp_NYrange.opr" "c_Lf_up_eyelids_lfupmult.i1x"
		;
connectAttr "c_Lf_up_eyelids_upclamp_PXrange.opr" "c_Lf_up_eyelids_lfupmult.i2x"
		;
connectAttr "c_Lf_up_eyelids_lfclamp_PYrange.opr" "c_Lf_up_eyelids_rtdnmult.i1x"
		;
connectAttr "c_Lf_up_eyelids_upclamp_NXrange.opr" "c_Lf_up_eyelids_rtdnmult.i2x"
		;
connectAttr "c_Lf_up_eyelids_rtclamp_PXrange.opr" "c_Lf_up_eyelids_rtScale.i1x";
connectAttr "c_Lf_up_eyelids_lfreverse_Y.ox" "c_Lf_up_eyelids_rtScale.i2x";
connectAttr "c_Lf_up_eyelids_lfclamp_NYrange.opr" "c_Lf_up_eyelids_rtupmult.i1x"
		;
connectAttr "c_Lf_up_eyelids_upclamp_NXrange.opr" "c_Lf_up_eyelids_rtupmult.i2x"
		;
connectAttr "c_Lf_up_eyelids_CTRL.tx" "c_Lf_up_eyelids_upmult_Xinverse.i2x";
connectAttr "c_Lf_up_eyelids_upclamp_PYrange.opr" "c_Lf_up_eyelids_upScale.i1x";
connectAttr "c_Lf_up_eyelids_upreverse_X.ox" "c_Lf_up_eyelids_upScale.i2x";
connectAttr "c_nose_CTRL.ty" "c_nose_dnmult_Yinverse.i2x";
connectAttr "c_nose_dnclamp_PYrange.opr" "c_nose_dnScale.i1x";
connectAttr "c_nose_upreverse_X.ox" "c_nose_dnScale.i2x";
connectAttr "c_nose_lfclamp_PYrange.opr" "c_nose_lfdnmult.i1x";
connectAttr "c_nose_upclamp_PXrange.opr" "c_nose_lfdnmult.i2x";
connectAttr "c_nose_CTRL.tx" "c_nose_lfmult_Xinverse.i2x";
connectAttr "c_nose_CTRL.ty" "c_nose_lfmult_Yinverse.i2x";
connectAttr "c_nose_lfclamp_PXrange.opr" "c_nose_lfScale.i1x";
connectAttr "c_nose_lfreverse_Y.ox" "c_nose_lfScale.i2x";
connectAttr "c_nose_lfclamp_NYrange.opr" "c_nose_lfupmult.i1x";
connectAttr "c_nose_upclamp_PXrange.opr" "c_nose_lfupmult.i2x";
connectAttr "c_nose_lfclamp_PYrange.opr" "c_nose_rtdnmult.i1x";
connectAttr "c_nose_upclamp_NXrange.opr" "c_nose_rtdnmult.i2x";
connectAttr "c_nose_rtclamp_PXrange.opr" "c_nose_rtScale.i1x";
connectAttr "c_nose_lfreverse_Y.ox" "c_nose_rtScale.i2x";
connectAttr "c_nose_lfclamp_NYrange.opr" "c_nose_rtupmult.i1x";
connectAttr "c_nose_upclamp_NXrange.opr" "c_nose_rtupmult.i2x";
connectAttr "c_nose_CTRL.tx" "c_nose_upmult_Xinverse.i2x";
connectAttr "c_nose_upclamp_PYrange.opr" "c_nose_upScale.i1x";
connectAttr "c_nose_upreverse_X.ox" "c_nose_upScale.i2x";
connectAttr "c_Rt_dn_eyelids_CTRL.ty" "c_Rt_dn_eyelids_dnmult_Yinverse.i2x";
connectAttr "c_Rt_dn_eyelids_dnclamp_PYrange.opr" "c_Rt_dn_eyelids_dnScale.i1x";
connectAttr "c_Rt_dn_eyelids_upreverse_X.ox" "c_Rt_dn_eyelids_dnScale.i2x";
connectAttr "c_Rt_dn_eyelids_lfclamp_PYrange.opr" "c_Rt_dn_eyelids_lfdnmult.i1x"
		;
connectAttr "c_Rt_dn_eyelids_upclamp_PXrange.opr" "c_Rt_dn_eyelids_lfdnmult.i2x"
		;
connectAttr "c_Rt_dn_eyelids_CTRL.tx" "c_Rt_dn_eyelids_lfmult_Xinverse.i2x";
connectAttr "c_Rt_dn_eyelids_CTRL.ty" "c_Rt_dn_eyelids_lfmult_Yinverse.i2x";
connectAttr "c_Rt_dn_eyelids_lfclamp_PXrange.opr" "c_Rt_dn_eyelids_lfScale.i1x";
connectAttr "c_Rt_dn_eyelids_lfreverse_Y.ox" "c_Rt_dn_eyelids_lfScale.i2x";
connectAttr "c_Rt_dn_eyelids_lfclamp_NYrange.opr" "c_Rt_dn_eyelids_lfupmult.i1x"
		;
connectAttr "c_Rt_dn_eyelids_upclamp_PXrange.opr" "c_Rt_dn_eyelids_lfupmult.i2x"
		;
connectAttr "c_Rt_dn_eyelids_lfclamp_PYrange.opr" "c_Rt_dn_eyelids_rtdnmult.i1x"
		;
connectAttr "c_Rt_dn_eyelids_upclamp_NXrange.opr" "c_Rt_dn_eyelids_rtdnmult.i2x"
		;
connectAttr "c_Rt_dn_eyelids_rtclamp_PXrange.opr" "c_Rt_dn_eyelids_rtScale.i1x";
connectAttr "c_Rt_dn_eyelids_lfreverse_Y.ox" "c_Rt_dn_eyelids_rtScale.i2x";
connectAttr "c_Rt_dn_eyelids_lfclamp_NYrange.opr" "c_Rt_dn_eyelids_rtupmult.i1x"
		;
connectAttr "c_Rt_dn_eyelids_upclamp_NXrange.opr" "c_Rt_dn_eyelids_rtupmult.i2x"
		;
connectAttr "c_Rt_dn_eyelids_CTRL.tx" "c_Rt_dn_eyelids_upmult_Xinverse.i2x";
connectAttr "c_Rt_dn_eyelids_upclamp_PYrange.opr" "c_Rt_dn_eyelids_upScale.i1x";
connectAttr "c_Rt_dn_eyelids_upreverse_X.ox" "c_Rt_dn_eyelids_upScale.i2x";
connectAttr "c_Rt_eyebrows_01_plus.o3y" "c_Rt_eyebrows_01_dnmult_Yinverse.i2x";
connectAttr "c_Rt_eyebrows_01_dnclamp_PYrange.opr" "c_Rt_eyebrows_01_dnScale.i1x"
		;
connectAttr "c_Rt_eyebrows_01_upreverse_X.ox" "c_Rt_eyebrows_01_dnScale.i2x";
connectAttr "c_Rt_eyebrows_01_lfclamp_PYrange.opr" "c_Rt_eyebrows_01_lfdnmult.i1x"
		;
connectAttr "c_Rt_eyebrows_01_upclamp_PXrange.opr" "c_Rt_eyebrows_01_lfdnmult.i2x"
		;
connectAttr "c_Rt_eyebrows_01_plus.o3x" "c_Rt_eyebrows_01_lfmult_Xinverse.i2x";
connectAttr "c_Rt_eyebrows_01_plus.o3y" "c_Rt_eyebrows_01_lfmult_Yinverse.i2x";
connectAttr "c_Rt_eyebrows_01_lfclamp_PXrange.opr" "c_Rt_eyebrows_01_lfScale.i1x"
		;
connectAttr "c_Rt_eyebrows_01_lfreverse_Y.ox" "c_Rt_eyebrows_01_lfScale.i2x";
connectAttr "c_Rt_eyebrows_01_lfclamp_NYrange.opr" "c_Rt_eyebrows_01_lfupmult.i1x"
		;
connectAttr "c_Rt_eyebrows_01_upclamp_PXrange.opr" "c_Rt_eyebrows_01_lfupmult.i2x"
		;
connectAttr "c_Rt_eyebrows_01_lfclamp_PYrange.opr" "c_Rt_eyebrows_01_rtdnmult.i1x"
		;
connectAttr "c_Rt_eyebrows_01_upclamp_NXrange.opr" "c_Rt_eyebrows_01_rtdnmult.i2x"
		;
connectAttr "c_Rt_eyebrows_01_rtclamp_PXrange.opr" "c_Rt_eyebrows_01_rtScale.i1x"
		;
connectAttr "c_Rt_eyebrows_01_lfreverse_Y.ox" "c_Rt_eyebrows_01_rtScale.i2x";
connectAttr "c_Rt_eyebrows_01_lfclamp_NYrange.opr" "c_Rt_eyebrows_01_rtupmult.i1x"
		;
connectAttr "c_Rt_eyebrows_01_upclamp_NXrange.opr" "c_Rt_eyebrows_01_rtupmult.i2x"
		;
connectAttr "c_Rt_eyebrows_01_plus.o3x" "c_Rt_eyebrows_01_upmult_Xinverse.i2x";
connectAttr "c_Rt_eyebrows_01_upclamp_PYrange.opr" "c_Rt_eyebrows_01_upScale.i1x"
		;
connectAttr "c_Rt_eyebrows_01_upreverse_X.ox" "c_Rt_eyebrows_01_upScale.i2x";
connectAttr "c_Rt_eyebrows_02_plus.o3y" "c_Rt_eyebrows_02_dnmult_Yinverse.i2x";
connectAttr "c_Rt_eyebrows_02_dnclamp_PYrange.opr" "c_Rt_eyebrows_02_dnScale.i1x"
		;
connectAttr "c_Rt_eyebrows_02_upreverse_X.ox" "c_Rt_eyebrows_02_dnScale.i2x";
connectAttr "c_Rt_eyebrows_02_lfclamp_PYrange.opr" "c_Rt_eyebrows_02_lfdnmult.i1x"
		;
connectAttr "c_Rt_eyebrows_02_upclamp_PXrange.opr" "c_Rt_eyebrows_02_lfdnmult.i2x"
		;
connectAttr "c_Rt_eyebrows_02_plus.o3x" "c_Rt_eyebrows_02_lfmult_Xinverse.i2x";
connectAttr "c_Rt_eyebrows_02_plus.o3y" "c_Rt_eyebrows_02_lfmult_Yinverse.i2x";
connectAttr "c_Rt_eyebrows_02_lfclamp_PXrange.opr" "c_Rt_eyebrows_02_lfScale.i1x"
		;
connectAttr "c_Rt_eyebrows_02_lfreverse_Y.ox" "c_Rt_eyebrows_02_lfScale.i2x";
connectAttr "c_Rt_eyebrows_02_lfclamp_NYrange.opr" "c_Rt_eyebrows_02_lfupmult.i1x"
		;
connectAttr "c_Rt_eyebrows_02_upclamp_PXrange.opr" "c_Rt_eyebrows_02_lfupmult.i2x"
		;
connectAttr "c_Rt_eyebrows_02_lfclamp_PYrange.opr" "c_Rt_eyebrows_02_rtdnmult.i1x"
		;
connectAttr "c_Rt_eyebrows_02_upclamp_NXrange.opr" "c_Rt_eyebrows_02_rtdnmult.i2x"
		;
connectAttr "c_Rt_eyebrows_02_rtclamp_PXrange.opr" "c_Rt_eyebrows_02_rtScale.i1x"
		;
connectAttr "c_Rt_eyebrows_02_lfreverse_Y.ox" "c_Rt_eyebrows_02_rtScale.i2x";
connectAttr "c_Rt_eyebrows_02_lfclamp_NYrange.opr" "c_Rt_eyebrows_02_rtupmult.i1x"
		;
connectAttr "c_Rt_eyebrows_02_upclamp_NXrange.opr" "c_Rt_eyebrows_02_rtupmult.i2x"
		;
connectAttr "c_Rt_eyebrows_02_plus.o3x" "c_Rt_eyebrows_02_upmult_Xinverse.i2x";
connectAttr "c_Rt_eyebrows_02_upclamp_PYrange.opr" "c_Rt_eyebrows_02_upScale.i1x"
		;
connectAttr "c_Rt_eyebrows_02_upreverse_X.ox" "c_Rt_eyebrows_02_upScale.i2x";
connectAttr "c_Rt_eyebrows_03_plus.o3y" "c_Rt_eyebrows_03_dnmult_Yinverse.i2x";
connectAttr "c_Rt_eyebrows_03_dnclamp_PYrange.opr" "c_Rt_eyebrows_03_dnScale.i1x"
		;
connectAttr "c_Rt_eyebrows_03_upreverse_X.ox" "c_Rt_eyebrows_03_dnScale.i2x";
connectAttr "c_Rt_eyebrows_03_lfclamp_PYrange.opr" "c_Rt_eyebrows_03_lfdnmult.i1x"
		;
connectAttr "c_Rt_eyebrows_03_upclamp_PXrange.opr" "c_Rt_eyebrows_03_lfdnmult.i2x"
		;
connectAttr "c_Rt_eyebrows_03_plus.o3x" "c_Rt_eyebrows_03_lfmult_Xinverse.i2x";
connectAttr "c_Rt_eyebrows_03_plus.o3y" "c_Rt_eyebrows_03_lfmult_Yinverse.i2x";
connectAttr "c_Rt_eyebrows_03_lfclamp_PXrange.opr" "c_Rt_eyebrows_03_lfScale.i1x"
		;
connectAttr "c_Rt_eyebrows_03_lfreverse_Y.ox" "c_Rt_eyebrows_03_lfScale.i2x";
connectAttr "c_Rt_eyebrows_03_lfclamp_NYrange.opr" "c_Rt_eyebrows_03_lfupmult.i1x"
		;
connectAttr "c_Rt_eyebrows_03_upclamp_PXrange.opr" "c_Rt_eyebrows_03_lfupmult.i2x"
		;
connectAttr "c_Rt_eyebrows_03_lfclamp_PYrange.opr" "c_Rt_eyebrows_03_rtdnmult.i1x"
		;
connectAttr "c_Rt_eyebrows_03_upclamp_NXrange.opr" "c_Rt_eyebrows_03_rtdnmult.i2x"
		;
connectAttr "c_Rt_eyebrows_03_rtclamp_PXrange.opr" "c_Rt_eyebrows_03_rtScale.i1x"
		;
connectAttr "c_Rt_eyebrows_03_lfreverse_Y.ox" "c_Rt_eyebrows_03_rtScale.i2x";
connectAttr "c_Rt_eyebrows_03_lfclamp_NYrange.opr" "c_Rt_eyebrows_03_rtupmult.i1x"
		;
connectAttr "c_Rt_eyebrows_03_upclamp_NXrange.opr" "c_Rt_eyebrows_03_rtupmult.i2x"
		;
connectAttr "c_Rt_eyebrows_03_plus.o3x" "c_Rt_eyebrows_03_upmult_Xinverse.i2x";
connectAttr "c_Rt_eyebrows_03_upclamp_PYrange.opr" "c_Rt_eyebrows_03_upScale.i1x"
		;
connectAttr "c_Rt_eyebrows_03_upreverse_X.ox" "c_Rt_eyebrows_03_upScale.i2x";
connectAttr "c_Rt_cheek_CTRL.ty" "c_Rt_eyeStretch_dnmult_Yinverse.i2x";
connectAttr "c_Rt_eyeStretch_dnclamp_PYrange.opr" "c_Rt_eyeStretch_dnScale.i1x";
connectAttr "c_Rt_eyeStretch_upreverse_X.ox" "c_Rt_eyeStretch_dnScale.i2x";
connectAttr "c_Rt_eyeStretch_lfclamp_PYrange.opr" "c_Rt_eyeStretch_lfdnmult.i1x"
		;
connectAttr "c_Rt_eyeStretch_upclamp_PXrange.opr" "c_Rt_eyeStretch_lfdnmult.i2x"
		;
connectAttr "c_Rt_cheek_CTRL.tx" "c_Rt_eyeStretch_lfmult_Xinverse.i2x";
connectAttr "c_Rt_cheek_CTRL.ty" "c_Rt_eyeStretch_lfmult_Yinverse.i2x";
connectAttr "c_Rt_eyeStretch_lfclamp_PXrange.opr" "c_Rt_eyeStretch_lfScale.i1x";
connectAttr "c_Rt_eyeStretch_lfreverse_Y.ox" "c_Rt_eyeStretch_lfScale.i2x";
connectAttr "c_Rt_eyeStretch_lfclamp_NYrange.opr" "c_Rt_eyeStretch_lfupmult.i1x"
		;
connectAttr "c_Rt_eyeStretch_upclamp_PXrange.opr" "c_Rt_eyeStretch_lfupmult.i2x"
		;
connectAttr "c_Rt_eyeStretch_lfclamp_PYrange.opr" "c_Rt_eyeStretch_rtdnmult.i1x"
		;
connectAttr "c_Rt_eyeStretch_upclamp_NXrange.opr" "c_Rt_eyeStretch_rtdnmult.i2x"
		;
connectAttr "c_Rt_eyeStretch_rtclamp_PXrange.opr" "c_Rt_eyeStretch_rtScale.i1x";
connectAttr "c_Rt_eyeStretch_lfreverse_Y.ox" "c_Rt_eyeStretch_rtScale.i2x";
connectAttr "c_Rt_eyeStretch_lfclamp_NYrange.opr" "c_Rt_eyeStretch_rtupmult.i1x"
		;
connectAttr "c_Rt_eyeStretch_upclamp_NXrange.opr" "c_Rt_eyeStretch_rtupmult.i2x"
		;
connectAttr "c_Rt_cheek_CTRL.tx" "c_Rt_eyeStretch_upmult_Xinverse.i2x";
connectAttr "c_Rt_eyeStretch_upclamp_PYrange.opr" "c_Rt_eyeStretch_upScale.i1x";
connectAttr "c_Rt_eyeStretch_upreverse_X.ox" "c_Rt_eyeStretch_upScale.i2x";
connectAttr "c_Rt_mouthLip_CTRL.ty" "c_Rt_mouthLip_dnmult_Yinverse.i2x";
connectAttr "c_Rt_mouthLip_dnclamp_PYrange.opr" "c_Rt_mouthLip_dnScale.i1x";
connectAttr "c_Rt_mouthLip_upreverse_X.ox" "c_Rt_mouthLip_dnScale.i2x";
connectAttr "c_Rt_mouthLip_lfclamp_PYrange.opr" "c_Rt_mouthLip_lfdnmult.i1x";
connectAttr "c_Rt_mouthLip_upclamp_PXrange.opr" "c_Rt_mouthLip_lfdnmult.i2x";
connectAttr "c_Rt_mouthLip_CTRL.tx" "c_Rt_mouthLip_lfmult_Xinverse.i2x";
connectAttr "c_Rt_mouthLip_CTRL.ty" "c_Rt_mouthLip_lfmult_Yinverse.i2x";
connectAttr "c_Rt_mouthLip_lfclamp_PXrange.opr" "c_Rt_mouthLip_lfScale.i1x";
connectAttr "c_Rt_mouthLip_lfreverse_Y.ox" "c_Rt_mouthLip_lfScale.i2x";
connectAttr "c_Rt_mouthLip_lfclamp_NYrange.opr" "c_Rt_mouthLip_lfupmult.i1x";
connectAttr "c_Rt_mouthLip_upclamp_PXrange.opr" "c_Rt_mouthLip_lfupmult.i2x";
connectAttr "c_Rt_mouthLip_lfclamp_PYrange.opr" "c_Rt_mouthLip_rtdnmult.i1x";
connectAttr "c_Rt_mouthLip_upclamp_NXrange.opr" "c_Rt_mouthLip_rtdnmult.i2x";
connectAttr "c_Rt_mouthLip_rtclamp_PXrange.opr" "c_Rt_mouthLip_rtScale.i1x";
connectAttr "c_Rt_mouthLip_lfreverse_Y.ox" "c_Rt_mouthLip_rtScale.i2x";
connectAttr "c_Rt_mouthLip_lfclamp_NYrange.opr" "c_Rt_mouthLip_rtupmult.i1x";
connectAttr "c_Rt_mouthLip_upclamp_NXrange.opr" "c_Rt_mouthLip_rtupmult.i2x";
connectAttr "c_Rt_mouthLip_CTRL.tx" "c_Rt_mouthLip_upmult_Xinverse.i2x";
connectAttr "c_Rt_mouthLip_upclamp_PYrange.opr" "c_Rt_mouthLip_upScale.i1x";
connectAttr "c_Rt_mouthLip_upreverse_X.ox" "c_Rt_mouthLip_upScale.i2x";
connectAttr "c_Rt_up_eyelids_CTRL.ty" "c_Rt_up_eyelids_dnmult_Yinverse.i2x";
connectAttr "c_Rt_up_eyelids_dnclamp_PYrange.opr" "c_Rt_up_eyelids_dnScale.i1x";
connectAttr "c_Rt_up_eyelids_upreverse_X.ox" "c_Rt_up_eyelids_dnScale.i2x";
connectAttr "c_Rt_up_eyelids_lfclamp_PYrange.opr" "c_Rt_up_eyelids_lfdnmult.i1x"
		;
connectAttr "c_Rt_up_eyelids_upclamp_PXrange.opr" "c_Rt_up_eyelids_lfdnmult.i2x"
		;
connectAttr "c_Rt_up_eyelids_CTRL.tx" "c_Rt_up_eyelids_lfmult_Xinverse.i2x";
connectAttr "c_Rt_up_eyelids_CTRL.ty" "c_Rt_up_eyelids_lfmult_Yinverse.i2x";
connectAttr "c_Rt_up_eyelids_lfclamp_PXrange.opr" "c_Rt_up_eyelids_lfScale.i1x";
connectAttr "c_Rt_up_eyelids_lfreverse_Y.ox" "c_Rt_up_eyelids_lfScale.i2x";
connectAttr "c_Rt_up_eyelids_lfclamp_NYrange.opr" "c_Rt_up_eyelids_lfupmult.i1x"
		;
connectAttr "c_Rt_up_eyelids_upclamp_PXrange.opr" "c_Rt_up_eyelids_lfupmult.i2x"
		;
connectAttr "c_Rt_up_eyelids_lfclamp_PYrange.opr" "c_Rt_up_eyelids_rtdnmult.i1x"
		;
connectAttr "c_Rt_up_eyelids_upclamp_NXrange.opr" "c_Rt_up_eyelids_rtdnmult.i2x"
		;
connectAttr "c_Rt_up_eyelids_rtclamp_PXrange.opr" "c_Rt_up_eyelids_rtScale.i1x";
connectAttr "c_Rt_up_eyelids_lfreverse_Y.ox" "c_Rt_up_eyelids_rtScale.i2x";
connectAttr "c_Rt_up_eyelids_lfclamp_NYrange.opr" "c_Rt_up_eyelids_rtupmult.i1x"
		;
connectAttr "c_Rt_up_eyelids_upclamp_NXrange.opr" "c_Rt_up_eyelids_rtupmult.i2x"
		;
connectAttr "c_Rt_up_eyelids_CTRL.tx" "c_Rt_up_eyelids_upmult_Xinverse.i2x";
connectAttr "c_Rt_up_eyelids_upclamp_PYrange.opr" "c_Rt_up_eyelids_upScale.i1x";
connectAttr "c_Rt_up_eyelids_upreverse_X.ox" "c_Rt_up_eyelids_upScale.i2x";
connectAttr "c_up_mouthLip_CTRL.ty" "c_up_mouthLip_dnmult_Yinverse.i2x";
connectAttr "c_up_mouthLip_dnclamp_PYrange.opr" "c_up_mouthLip_dnScale.i1x";
connectAttr "c_up_mouthLip_upreverse_X.ox" "c_up_mouthLip_dnScale.i2x";
connectAttr "c_up_mouthLip_lfclamp_PYrange.opr" "c_up_mouthLip_lfdnmult.i1x";
connectAttr "c_up_mouthLip_upclamp_PXrange.opr" "c_up_mouthLip_lfdnmult.i2x";
connectAttr "c_up_mouthLip_CTRL.tx" "c_up_mouthLip_lfmult_Xinverse.i2x";
connectAttr "c_up_mouthLip_CTRL.ty" "c_up_mouthLip_lfmult_Yinverse.i2x";
connectAttr "c_up_mouthLip_lfclamp_PXrange.opr" "c_up_mouthLip_lfScale.i1x";
connectAttr "c_up_mouthLip_lfreverse_Y.ox" "c_up_mouthLip_lfScale.i2x";
connectAttr "c_up_mouthLip_lfclamp_NYrange.opr" "c_up_mouthLip_lfupmult.i1x";
connectAttr "c_up_mouthLip_upclamp_PXrange.opr" "c_up_mouthLip_lfupmult.i2x";
connectAttr "c_up_mouthLip_lfclamp_PYrange.opr" "c_up_mouthLip_rtdnmult.i1x";
connectAttr "c_up_mouthLip_upclamp_NXrange.opr" "c_up_mouthLip_rtdnmult.i2x";
connectAttr "c_up_mouthLip_rtclamp_PXrange.opr" "c_up_mouthLip_rtScale.i1x";
connectAttr "c_up_mouthLip_lfreverse_Y.ox" "c_up_mouthLip_rtScale.i2x";
connectAttr "c_up_mouthLip_lfclamp_NYrange.opr" "c_up_mouthLip_rtupmult.i1x";
connectAttr "c_up_mouthLip_upclamp_NXrange.opr" "c_up_mouthLip_rtupmult.i2x";
connectAttr "c_up_mouthLip_CTRL.tx" "c_up_mouthLip_upmult_Xinverse.i2x";
connectAttr "c_up_mouthLip_upclamp_PYrange.opr" "c_up_mouthLip_upScale.i1x";
connectAttr "c_up_mouthLip_upreverse_X.ox" "c_up_mouthLip_upScale.i2x";
connectAttr "c_uo_CTRL.ty" "E_dnmult_Yinverse.i2x";
connectAttr "E_dnclamp_PYrange.opr" "E_dnScale.i1x";
connectAttr "E_upreverse_X.ox" "E_dnScale.i2x";
connectAttr "E_lfclamp_PYrange.opr" "E_lfdnmult.i1x";
connectAttr "E_upclamp_PXrange.opr" "E_lfdnmult.i2x";
connectAttr "c_uo_CTRL.tx" "E_lfmult_Xinverse.i2x";
connectAttr "c_uo_CTRL.ty" "E_lfmult_Yinverse.i2x";
connectAttr "E_lfclamp_PXrange.opr" "E_lfScale.i1x";
connectAttr "E_lfreverse_Y.ox" "E_lfScale.i2x";
connectAttr "E_lfclamp_NYrange.opr" "E_lfupmult.i1x";
connectAttr "E_upclamp_PXrange.opr" "E_lfupmult.i2x";
connectAttr "E_lfclamp_PYrange.opr" "E_rtdnmult.i1x";
connectAttr "E_upclamp_NXrange.opr" "E_rtdnmult.i2x";
connectAttr "E_rtclamp_PXrange.opr" "E_rtScale.i1x";
connectAttr "E_lfreverse_Y.ox" "E_rtScale.i2x";
connectAttr "E_lfclamp_NYrange.opr" "E_rtupmult.i1x";
connectAttr "E_upclamp_NXrange.opr" "E_rtupmult.i2x";
connectAttr "c_uo_CTRL.tx" "E_upmult_Xinverse.i2x";
connectAttr "E_upclamp_PYrange.opr" "E_upScale.i1x";
connectAttr "E_upreverse_X.ox" "E_upScale.i2x";
connectAttr "c_mbp_CTRL.ty" "FV_dnmult_Yinverse.i2x";
connectAttr "FV_dnclamp_PYrange.opr" "FV_dnScale.i1x";
connectAttr "FV_upreverse_X.ox" "FV_dnScale.i2x";
connectAttr "FV_lfclamp_PYrange.opr" "FV_lfdnmult.i1x";
connectAttr "FV_upclamp_PXrange.opr" "FV_lfdnmult.i2x";
connectAttr "c_mbp_CTRL.tx" "FV_lfmult_Xinverse.i2x";
connectAttr "c_mbp_CTRL.ty" "FV_lfmult_Yinverse.i2x";
connectAttr "FV_lfclamp_PXrange.opr" "FV_lfScale.i1x";
connectAttr "FV_lfreverse_Y.ox" "FV_lfScale.i2x";
connectAttr "FV_lfclamp_NYrange.opr" "FV_lfupmult.i1x";
connectAttr "FV_upclamp_PXrange.opr" "FV_lfupmult.i2x";
connectAttr "FV_lfclamp_PYrange.opr" "FV_rtdnmult.i1x";
connectAttr "FV_upclamp_NXrange.opr" "FV_rtdnmult.i2x";
connectAttr "FV_rtclamp_PXrange.opr" "FV_rtScale.i1x";
connectAttr "FV_lfreverse_Y.ox" "FV_rtScale.i2x";
connectAttr "FV_lfclamp_NYrange.opr" "FV_rtupmult.i1x";
connectAttr "FV_upclamp_NXrange.opr" "FV_rtupmult.i2x";
connectAttr "c_mbp_CTRL.tx" "FV_upmult_Xinverse.i2x";
connectAttr "FV_upclamp_PYrange.opr" "FV_upScale.i1x";
connectAttr "FV_upreverse_X.ox" "FV_upScale.i2x";
connectAttr "c_fv_CTRL.ty" "I_dnmult_Yinverse.i2x";
connectAttr "I_dnclamp_PYrange.opr" "I_dnScale.i1x";
connectAttr "I_upreverse_X.ox" "I_dnScale.i2x";
connectAttr "I_lfclamp_PYrange.opr" "I_lfdnmult.i1x";
connectAttr "I_upclamp_PXrange.opr" "I_lfdnmult.i2x";
connectAttr "c_fv_CTRL.tx" "I_lfmult_Xinverse.i2x";
connectAttr "c_fv_CTRL.ty" "I_lfmult_Yinverse.i2x";
connectAttr "I_lfclamp_PXrange.opr" "I_lfScale.i1x";
connectAttr "I_lfreverse_Y.ox" "I_lfScale.i2x";
connectAttr "I_lfclamp_NYrange.opr" "I_lfupmult.i1x";
connectAttr "I_upclamp_PXrange.opr" "I_lfupmult.i2x";
connectAttr "I_lfclamp_PYrange.opr" "I_rtdnmult.i1x";
connectAttr "I_upclamp_NXrange.opr" "I_rtdnmult.i2x";
connectAttr "I_rtclamp_PXrange.opr" "I_rtScale.i1x";
connectAttr "I_lfreverse_Y.ox" "I_rtScale.i2x";
connectAttr "I_lfclamp_NYrange.opr" "I_rtupmult.i1x";
connectAttr "I_upclamp_NXrange.opr" "I_rtupmult.i2x";
connectAttr "c_fv_CTRL.tx" "I_upmult_Xinverse.i2x";
connectAttr "I_upclamp_PYrange.opr" "I_upScale.i1x";
connectAttr "I_upreverse_X.ox" "I_upScale.i2x";
connectAttr "c_the_CTRL.ty" "O_dnmult_Yinverse.i2x";
connectAttr "O_dnclamp_PYrange.opr" "O_dnScale.i1x";
connectAttr "O_upreverse_X.ox" "O_dnScale.i2x";
connectAttr "O_lfclamp_PYrange.opr" "O_lfdnmult.i1x";
connectAttr "O_upclamp_PXrange.opr" "O_lfdnmult.i2x";
connectAttr "c_the_CTRL.tx" "O_lfmult_Xinverse.i2x";
connectAttr "c_the_CTRL.ty" "O_lfmult_Yinverse.i2x";
connectAttr "O_lfclamp_PXrange.opr" "O_lfScale.i1x";
connectAttr "O_lfreverse_Y.ox" "O_lfScale.i2x";
connectAttr "O_lfclamp_NYrange.opr" "O_lfupmult.i1x";
connectAttr "O_upclamp_PXrange.opr" "O_lfupmult.i2x";
connectAttr "O_lfclamp_PYrange.opr" "O_rtdnmult.i1x";
connectAttr "O_upclamp_NXrange.opr" "O_rtdnmult.i2x";
connectAttr "O_rtclamp_PXrange.opr" "O_rtScale.i1x";
connectAttr "O_lfreverse_Y.ox" "O_rtScale.i2x";
connectAttr "O_lfclamp_NYrange.opr" "O_rtupmult.i1x";
connectAttr "O_upclamp_NXrange.opr" "O_rtupmult.i2x";
connectAttr "c_the_CTRL.tx" "O_upmult_Xinverse.i2x";
connectAttr "O_upclamp_PYrange.opr" "O_upScale.i1x";
connectAttr "O_upreverse_X.ox" "O_upScale.i2x";
connectAttr "c_OU_CTRL.ty" "OU_dnmult_Yinverse.i2x";
connectAttr "OU_dnclamp_PYrange.opr" "OU_dnScale.i1x";
connectAttr "OU_upreverse_X.ox" "OU_dnScale.i2x";
connectAttr "OU_lfclamp_PYrange.opr" "OU_lfdnmult.i1x";
connectAttr "OU_upclamp_PXrange.opr" "OU_lfdnmult.i2x";
connectAttr "c_OU_CTRL.tx" "OU_lfmult_Xinverse.i2x";
connectAttr "c_OU_CTRL.ty" "OU_lfmult_Yinverse.i2x";
connectAttr "OU_lfclamp_PXrange.opr" "OU_lfScale.i1x";
connectAttr "OU_lfreverse_Y.ox" "OU_lfScale.i2x";
connectAttr "OU_lfclamp_NYrange.opr" "OU_lfupmult.i1x";
connectAttr "OU_upclamp_PXrange.opr" "OU_lfupmult.i2x";
connectAttr "OU_lfclamp_PYrange.opr" "OU_rtdnmult.i1x";
connectAttr "OU_upclamp_NXrange.opr" "OU_rtdnmult.i2x";
connectAttr "OU_rtclamp_PXrange.opr" "OU_rtScale.i1x";
connectAttr "OU_lfreverse_Y.ox" "OU_rtScale.i2x";
connectAttr "OU_lfclamp_NYrange.opr" "OU_rtupmult.i1x";
connectAttr "OU_upclamp_NXrange.opr" "OU_rtupmult.i2x";
connectAttr "c_OU_CTRL.tx" "OU_upmult_Xinverse.i2x";
connectAttr "OU_upclamp_PYrange.opr" "OU_upScale.i1x";
connectAttr "OU_upreverse_X.ox" "OU_upScale.i2x";
connectAttr "c_tongue_CTRL.ty" "tongue_dnmult_Yinverse.i2x";
connectAttr "tongue_dnclamp_PYrange.opr" "tongue_dnScale.i1x";
connectAttr "tongue_upreverse_X.ox" "tongue_dnScale.i2x";
connectAttr "tongue_lfclamp_PYrange.opr" "tongue_lfdnmult.i1x";
connectAttr "tongue_upclamp_PXrange.opr" "tongue_lfdnmult.i2x";
connectAttr "c_tongue_CTRL.tx" "tongue_lfmult_Xinverse.i2x";
connectAttr "c_tongue_CTRL.ty" "tongue_lfmult_Yinverse.i2x";
connectAttr "tongue_lfclamp_PXrange.opr" "tongue_lfScale.i1x";
connectAttr "tongue_lfreverse_Y.ox" "tongue_lfScale.i2x";
connectAttr "tongue_lfclamp_NYrange.opr" "tongue_lfupmult.i1x";
connectAttr "tongue_upclamp_PXrange.opr" "tongue_lfupmult.i2x";
connectAttr "tongue_lfclamp_PYrange.opr" "tongue_rtdnmult.i1x";
connectAttr "tongue_upclamp_NXrange.opr" "tongue_rtdnmult.i2x";
connectAttr "tongue_rtclamp_PXrange.opr" "tongue_rtScale.i1x";
connectAttr "tongue_lfreverse_Y.ox" "tongue_rtScale.i2x";
connectAttr "tongue_lfclamp_NYrange.opr" "tongue_rtupmult.i1x";
connectAttr "tongue_upclamp_NXrange.opr" "tongue_rtupmult.i2x";
connectAttr "c_tongue_CTRL.tx" "tongue_upmult_Xinverse.i2x";
connectAttr "tongue_upclamp_PYrange.opr" "tongue_upScale.i1x";
connectAttr "tongue_upreverse_X.ox" "tongue_upScale.i2x";
connectAttr "c_eeesz_CTRL.ty" "U_dnmult_Yinverse.i2x";
connectAttr "U_dnclamp_PYrange.opr" "U_dnScale.i1x";
connectAttr "U_upreverse_X.ox" "U_dnScale.i2x";
connectAttr "U_lfclamp_PYrange.opr" "U_lfdnmult.i1x";
connectAttr "U_upclamp_PXrange.opr" "U_lfdnmult.i2x";
connectAttr "c_eeesz_CTRL.tx" "U_lfmult_Xinverse.i2x";
connectAttr "c_eeesz_CTRL.ty" "U_lfmult_Yinverse.i2x";
connectAttr "U_lfclamp_PXrange.opr" "U_lfScale.i1x";
connectAttr "U_lfreverse_Y.ox" "U_lfScale.i2x";
connectAttr "U_lfclamp_NYrange.opr" "U_lfupmult.i1x";
connectAttr "U_upclamp_PXrange.opr" "U_lfupmult.i2x";
connectAttr "U_lfclamp_PYrange.opr" "U_rtdnmult.i1x";
connectAttr "U_upclamp_NXrange.opr" "U_rtdnmult.i2x";
connectAttr "U_rtclamp_PXrange.opr" "U_rtScale.i1x";
connectAttr "U_lfreverse_Y.ox" "U_rtScale.i2x";
connectAttr "U_lfclamp_NYrange.opr" "U_rtupmult.i1x";
connectAttr "U_upclamp_NXrange.opr" "U_rtupmult.i2x";
connectAttr "c_eeesz_CTRL.tx" "U_upmult_Xinverse.i2x";
connectAttr "U_upclamp_PYrange.opr" "U_upScale.i1x";
connectAttr "U_upreverse_X.ox" "U_upScale.i2x";
connectAttr "A_lfclamp_NYrange.opr" "A_lfplus_Yplus.i1[0]";
connectAttr "A_lfclamp_PYrange.opr" "A_lfplus_Yplus.i1[1]";
connectAttr "A_upclamp_NXrange.opr" "A_upplus_Xplus.i1[0]";
connectAttr "A_upclamp_PXrange.opr" "A_upplus_Xplus.i1[1]";
connectAttr "c_dn_mouthLip_lfclamp_NYrange.opr" "c_dn_mouthLip_lfplus_Yplus.i1[0]"
		;
connectAttr "c_dn_mouthLip_lfclamp_PYrange.opr" "c_dn_mouthLip_lfplus_Yplus.i1[1]"
		;
connectAttr "c_dn_mouthLip_upclamp_NXrange.opr" "c_dn_mouthLip_upplus_Xplus.i1[0]"
		;
connectAttr "c_dn_mouthLip_upclamp_PXrange.opr" "c_dn_mouthLip_upplus_Xplus.i1[1]"
		;
connectAttr "c_jaw_dn_lfclamp_NYrange.opr" "c_jaw_dn_lfplus_Yplus.i1[0]";
connectAttr "c_jaw_dn_lfclamp_PYrange.opr" "c_jaw_dn_lfplus_Yplus.i1[1]";
connectAttr "c_jaw_dn_upclamp_NXrange.opr" "c_jaw_dn_upplus_Xplus.i1[0]";
connectAttr "c_jaw_dn_upclamp_PXrange.opr" "c_jaw_dn_upplus_Xplus.i1[1]";
connectAttr "c_jaw_up_lfclamp_NYrange.opr" "c_jaw_up_lfplus_Yplus.i1[0]";
connectAttr "c_jaw_up_lfclamp_PYrange.opr" "c_jaw_up_lfplus_Yplus.i1[1]";
connectAttr "c_jaw_up_upclamp_NXrange.opr" "c_jaw_up_upplus_Xplus.i1[0]";
connectAttr "c_jaw_up_upclamp_PXrange.opr" "c_jaw_up_upplus_Xplus.i1[1]";
connectAttr "c_Lf_dn_eyelids_lfclamp_NYrange.opr" "c_Lf_dn_eyelids_lfplus_Yplus.i1[0]"
		;
connectAttr "c_Lf_dn_eyelids_lfclamp_PYrange.opr" "c_Lf_dn_eyelids_lfplus_Yplus.i1[1]"
		;
connectAttr "c_Lf_dn_eyelids_upclamp_NXrange.opr" "c_Lf_dn_eyelids_upplus_Xplus.i1[0]"
		;
connectAttr "c_Lf_dn_eyelids_upclamp_PXrange.opr" "c_Lf_dn_eyelids_upplus_Xplus.i1[1]"
		;
connectAttr "c_Lf_eyebrows_01_lfclamp_NYrange.opr" "c_Lf_eyebrows_01_lfplus_Yplus.i1[0]"
		;
connectAttr "c_Lf_eyebrows_01_lfclamp_PYrange.opr" "c_Lf_eyebrows_01_lfplus_Yplus.i1[1]"
		;
connectAttr "c_Lf_eyebrows_CTRL.t" "c_Lf_eyebrows_01_plus.i3[0]";
connectAttr "c_Lf_eyebrows_01_CTRL.t" "c_Lf_eyebrows_01_plus.i3[1]";
connectAttr "c_Lf_eyebrows_01_upclamp_NXrange.opr" "c_Lf_eyebrows_01_upplus_Xplus.i1[0]"
		;
connectAttr "c_Lf_eyebrows_01_upclamp_PXrange.opr" "c_Lf_eyebrows_01_upplus_Xplus.i1[1]"
		;
connectAttr "c_Lf_eyebrows_02_lfclamp_NYrange.opr" "c_Lf_eyebrows_02_lfplus_Yplus.i1[0]"
		;
connectAttr "c_Lf_eyebrows_02_lfclamp_PYrange.opr" "c_Lf_eyebrows_02_lfplus_Yplus.i1[1]"
		;
connectAttr "c_Lf_eyebrows_CTRL.t" "c_Lf_eyebrows_02_plus.i3[0]";
connectAttr "c_Lf_eyebrows_02_CTRL.t" "c_Lf_eyebrows_02_plus.i3[1]";
connectAttr "c_Lf_eyebrows_02_upclamp_NXrange.opr" "c_Lf_eyebrows_02_upplus_Xplus.i1[0]"
		;
connectAttr "c_Lf_eyebrows_02_upclamp_PXrange.opr" "c_Lf_eyebrows_02_upplus_Xplus.i1[1]"
		;
connectAttr "c_Lf_eyebrows_03_lfclamp_NYrange.opr" "c_Lf_eyebrows_03_lfplus_Yplus.i1[0]"
		;
connectAttr "c_Lf_eyebrows_03_lfclamp_PYrange.opr" "c_Lf_eyebrows_03_lfplus_Yplus.i1[1]"
		;
connectAttr "c_Lf_eyebrows_CTRL.t" "c_Lf_eyebrows_03_plus.i3[0]";
connectAttr "c_Lf_eyebrows_03_CTRL.t" "c_Lf_eyebrows_03_plus.i3[1]";
connectAttr "c_Lf_eyebrows_03_upclamp_NXrange.opr" "c_Lf_eyebrows_03_upplus_Xplus.i1[0]"
		;
connectAttr "c_Lf_eyebrows_03_upclamp_PXrange.opr" "c_Lf_eyebrows_03_upplus_Xplus.i1[1]"
		;
connectAttr "c_Lf_eyeStretch_lfclamp_NYrange.opr" "c_Lf_eyeStretch_lfplus_Yplus.i1[0]"
		;
connectAttr "c_Lf_eyeStretch_lfclamp_PYrange.opr" "c_Lf_eyeStretch_lfplus_Yplus.i1[1]"
		;
connectAttr "c_Lf_eyeStretch_upclamp_NXrange.opr" "c_Lf_eyeStretch_upplus_Xplus.i1[0]"
		;
connectAttr "c_Lf_eyeStretch_upclamp_PXrange.opr" "c_Lf_eyeStretch_upplus_Xplus.i1[1]"
		;
connectAttr "c_Lf_mouthLip_lfclamp_NYrange.opr" "c_Lf_mouthLip_lfplus_Yplus.i1[0]"
		;
connectAttr "c_Lf_mouthLip_lfclamp_PYrange.opr" "c_Lf_mouthLip_lfplus_Yplus.i1[1]"
		;
connectAttr "c_Lf_mouthLip_upclamp_NXrange.opr" "c_Lf_mouthLip_upplus_Xplus.i1[0]"
		;
connectAttr "c_Lf_mouthLip_upclamp_PXrange.opr" "c_Lf_mouthLip_upplus_Xplus.i1[1]"
		;
connectAttr "c_Lf_up_eyelids_lfclamp_NYrange.opr" "c_Lf_up_eyelids_lfplus_Yplus.i1[0]"
		;
connectAttr "c_Lf_up_eyelids_lfclamp_PYrange.opr" "c_Lf_up_eyelids_lfplus_Yplus.i1[1]"
		;
connectAttr "c_Lf_up_eyelids_upclamp_NXrange.opr" "c_Lf_up_eyelids_upplus_Xplus.i1[0]"
		;
connectAttr "c_Lf_up_eyelids_upclamp_PXrange.opr" "c_Lf_up_eyelids_upplus_Xplus.i1[1]"
		;
connectAttr "c_nose_lfclamp_NYrange.opr" "c_nose_lfplus_Yplus.i1[0]";
connectAttr "c_nose_lfclamp_PYrange.opr" "c_nose_lfplus_Yplus.i1[1]";
connectAttr "c_nose_upclamp_NXrange.opr" "c_nose_upplus_Xplus.i1[0]";
connectAttr "c_nose_upclamp_PXrange.opr" "c_nose_upplus_Xplus.i1[1]";
connectAttr "c_Rt_dn_eyelids_lfclamp_NYrange.opr" "c_Rt_dn_eyelids_lfplus_Yplus.i1[0]"
		;
connectAttr "c_Rt_dn_eyelids_lfclamp_PYrange.opr" "c_Rt_dn_eyelids_lfplus_Yplus.i1[1]"
		;
connectAttr "c_Rt_dn_eyelids_upclamp_NXrange.opr" "c_Rt_dn_eyelids_upplus_Xplus.i1[0]"
		;
connectAttr "c_Rt_dn_eyelids_upclamp_PXrange.opr" "c_Rt_dn_eyelids_upplus_Xplus.i1[1]"
		;
connectAttr "c_Rt_eyebrows_01_lfclamp_NYrange.opr" "c_Rt_eyebrows_01_lfplus_Yplus.i1[0]"
		;
connectAttr "c_Rt_eyebrows_01_lfclamp_PYrange.opr" "c_Rt_eyebrows_01_lfplus_Yplus.i1[1]"
		;
connectAttr "c_Rt_eyebrows_CTRL.t" "c_Rt_eyebrows_01_plus.i3[0]";
connectAttr "c_Rt_eyebrows_01_CTRL.t" "c_Rt_eyebrows_01_plus.i3[1]";
connectAttr "c_Rt_eyebrows_01_upclamp_NXrange.opr" "c_Rt_eyebrows_01_upplus_Xplus.i1[0]"
		;
connectAttr "c_Rt_eyebrows_01_upclamp_PXrange.opr" "c_Rt_eyebrows_01_upplus_Xplus.i1[1]"
		;
connectAttr "c_Rt_eyebrows_02_lfclamp_NYrange.opr" "c_Rt_eyebrows_02_lfplus_Yplus.i1[0]"
		;
connectAttr "c_Rt_eyebrows_02_lfclamp_PYrange.opr" "c_Rt_eyebrows_02_lfplus_Yplus.i1[1]"
		;
connectAttr "c_Rt_eyebrows_CTRL.t" "c_Rt_eyebrows_02_plus.i3[0]";
connectAttr "c_Rt_eyebrows_02_CTRL.t" "c_Rt_eyebrows_02_plus.i3[1]";
connectAttr "c_Rt_eyebrows_02_upclamp_NXrange.opr" "c_Rt_eyebrows_02_upplus_Xplus.i1[0]"
		;
connectAttr "c_Rt_eyebrows_02_upclamp_PXrange.opr" "c_Rt_eyebrows_02_upplus_Xplus.i1[1]"
		;
connectAttr "c_Rt_eyebrows_03_lfclamp_NYrange.opr" "c_Rt_eyebrows_03_lfplus_Yplus.i1[0]"
		;
connectAttr "c_Rt_eyebrows_03_lfclamp_PYrange.opr" "c_Rt_eyebrows_03_lfplus_Yplus.i1[1]"
		;
connectAttr "c_Rt_eyebrows_CTRL.t" "c_Rt_eyebrows_03_plus.i3[0]";
connectAttr "c_Rt_eyebrows_03_CTRL.t" "c_Rt_eyebrows_03_plus.i3[1]";
connectAttr "c_Rt_eyebrows_03_upclamp_NXrange.opr" "c_Rt_eyebrows_03_upplus_Xplus.i1[0]"
		;
connectAttr "c_Rt_eyebrows_03_upclamp_PXrange.opr" "c_Rt_eyebrows_03_upplus_Xplus.i1[1]"
		;
connectAttr "c_Rt_eyeStretch_lfclamp_NYrange.opr" "c_Rt_eyeStretch_lfplus_Yplus.i1[0]"
		;
connectAttr "c_Rt_eyeStretch_lfclamp_PYrange.opr" "c_Rt_eyeStretch_lfplus_Yplus.i1[1]"
		;
connectAttr "c_Rt_eyeStretch_upclamp_NXrange.opr" "c_Rt_eyeStretch_upplus_Xplus.i1[0]"
		;
connectAttr "c_Rt_eyeStretch_upclamp_PXrange.opr" "c_Rt_eyeStretch_upplus_Xplus.i1[1]"
		;
connectAttr "c_Rt_mouthLip_lfclamp_NYrange.opr" "c_Rt_mouthLip_lfplus_Yplus.i1[0]"
		;
connectAttr "c_Rt_mouthLip_lfclamp_PYrange.opr" "c_Rt_mouthLip_lfplus_Yplus.i1[1]"
		;
connectAttr "c_Rt_mouthLip_upclamp_NXrange.opr" "c_Rt_mouthLip_upplus_Xplus.i1[0]"
		;
connectAttr "c_Rt_mouthLip_upclamp_PXrange.opr" "c_Rt_mouthLip_upplus_Xplus.i1[1]"
		;
connectAttr "c_Rt_up_eyelids_lfclamp_NYrange.opr" "c_Rt_up_eyelids_lfplus_Yplus.i1[0]"
		;
connectAttr "c_Rt_up_eyelids_lfclamp_PYrange.opr" "c_Rt_up_eyelids_lfplus_Yplus.i1[1]"
		;
connectAttr "c_Rt_up_eyelids_upclamp_NXrange.opr" "c_Rt_up_eyelids_upplus_Xplus.i1[0]"
		;
connectAttr "c_Rt_up_eyelids_upclamp_PXrange.opr" "c_Rt_up_eyelids_upplus_Xplus.i1[1]"
		;
connectAttr "c_up_mouthLip_lfclamp_NYrange.opr" "c_up_mouthLip_lfplus_Yplus.i1[0]"
		;
connectAttr "c_up_mouthLip_lfclamp_PYrange.opr" "c_up_mouthLip_lfplus_Yplus.i1[1]"
		;
connectAttr "c_up_mouthLip_upclamp_NXrange.opr" "c_up_mouthLip_upplus_Xplus.i1[0]"
		;
connectAttr "c_up_mouthLip_upclamp_PXrange.opr" "c_up_mouthLip_upplus_Xplus.i1[1]"
		;
connectAttr "E_lfclamp_NYrange.opr" "E_lfplus_Yplus.i1[0]";
connectAttr "E_lfclamp_PYrange.opr" "E_lfplus_Yplus.i1[1]";
connectAttr "E_upclamp_NXrange.opr" "E_upplus_Xplus.i1[0]";
connectAttr "E_upclamp_PXrange.opr" "E_upplus_Xplus.i1[1]";
connectAttr "FV_lfclamp_NYrange.opr" "FV_lfplus_Yplus.i1[0]";
connectAttr "FV_lfclamp_PYrange.opr" "FV_lfplus_Yplus.i1[1]";
connectAttr "FV_upclamp_NXrange.opr" "FV_upplus_Xplus.i1[0]";
connectAttr "FV_upclamp_PXrange.opr" "FV_upplus_Xplus.i1[1]";
connectAttr "I_lfclamp_NYrange.opr" "I_lfplus_Yplus.i1[0]";
connectAttr "I_lfclamp_PYrange.opr" "I_lfplus_Yplus.i1[1]";
connectAttr "I_upclamp_NXrange.opr" "I_upplus_Xplus.i1[0]";
connectAttr "I_upclamp_PXrange.opr" "I_upplus_Xplus.i1[1]";
connectAttr "O_lfclamp_NYrange.opr" "O_lfplus_Yplus.i1[0]";
connectAttr "O_lfclamp_PYrange.opr" "O_lfplus_Yplus.i1[1]";
connectAttr "O_upclamp_NXrange.opr" "O_upplus_Xplus.i1[0]";
connectAttr "O_upclamp_PXrange.opr" "O_upplus_Xplus.i1[1]";
connectAttr "OU_lfclamp_NYrange.opr" "OU_lfplus_Yplus.i1[0]";
connectAttr "OU_lfclamp_PYrange.opr" "OU_lfplus_Yplus.i1[1]";
connectAttr "OU_upclamp_NXrange.opr" "OU_upplus_Xplus.i1[0]";
connectAttr "OU_upclamp_PXrange.opr" "OU_upplus_Xplus.i1[1]";
connectAttr "tongue_lfclamp_NYrange.opr" "tongue_lfplus_Yplus.i1[0]";
connectAttr "tongue_lfclamp_PYrange.opr" "tongue_lfplus_Yplus.i1[1]";
connectAttr "tongue_upclamp_NXrange.opr" "tongue_upplus_Xplus.i1[0]";
connectAttr "tongue_upclamp_PXrange.opr" "tongue_upplus_Xplus.i1[1]";
connectAttr "U_lfclamp_NYrange.opr" "U_lfplus_Yplus.i1[0]";
connectAttr "U_lfclamp_PYrange.opr" "U_lfplus_Yplus.i1[1]";
connectAttr "U_upclamp_NXrange.opr" "U_upplus_Xplus.i1[0]";
connectAttr "U_upclamp_PXrange.opr" "U_upplus_Xplus.i1[1]";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "A_lfplus_Yplus.o1" "A_lfreverse_Y.ix";
connectAttr "A_upplus_Xplus.o1" "A_upreverse_X.ix";
connectAttr "c_dn_mouthLip_lfplus_Yplus.o1" "c_dn_mouthLip_lfreverse_Y.ix";
connectAttr "c_dn_mouthLip_upplus_Xplus.o1" "c_dn_mouthLip_upreverse_X.ix";
connectAttr "c_jaw_dn_lfplus_Yplus.o1" "c_jaw_dn_lfreverse_Y.ix";
connectAttr "c_jaw_dn_upplus_Xplus.o1" "c_jaw_dn_upreverse_X.ix";
connectAttr "c_jaw_up_lfplus_Yplus.o1" "c_jaw_up_lfreverse_Y.ix";
connectAttr "c_jaw_up_upplus_Xplus.o1" "c_jaw_up_upreverse_X.ix";
connectAttr "c_Lf_dn_eyelids_lfplus_Yplus.o1" "c_Lf_dn_eyelids_lfreverse_Y.ix";
connectAttr "c_Lf_dn_eyelids_upplus_Xplus.o1" "c_Lf_dn_eyelids_upreverse_X.ix";
connectAttr "c_Lf_eyebrows_01_lfplus_Yplus.o1" "c_Lf_eyebrows_01_lfreverse_Y.ix"
		;
connectAttr "c_Lf_eyebrows_01_upplus_Xplus.o1" "c_Lf_eyebrows_01_upreverse_X.ix"
		;
connectAttr "c_Lf_eyebrows_02_lfplus_Yplus.o1" "c_Lf_eyebrows_02_lfreverse_Y.ix"
		;
connectAttr "c_Lf_eyebrows_02_upplus_Xplus.o1" "c_Lf_eyebrows_02_upreverse_X.ix"
		;
connectAttr "c_Lf_eyebrows_03_lfplus_Yplus.o1" "c_Lf_eyebrows_03_lfreverse_Y.ix"
		;
connectAttr "c_Lf_eyebrows_03_upplus_Xplus.o1" "c_Lf_eyebrows_03_upreverse_X.ix"
		;
connectAttr "c_Lf_eyeStretch_lfplus_Yplus.o1" "c_Lf_eyeStretch_lfreverse_Y.ix";
connectAttr "c_Lf_eyeStretch_upplus_Xplus.o1" "c_Lf_eyeStretch_upreverse_X.ix";
connectAttr "c_Lf_mouthLip_lfplus_Yplus.o1" "c_Lf_mouthLip_lfreverse_Y.ix";
connectAttr "c_Lf_mouthLip_upplus_Xplus.o1" "c_Lf_mouthLip_upreverse_X.ix";
connectAttr "c_Lf_up_eyelids_lfplus_Yplus.o1" "c_Lf_up_eyelids_lfreverse_Y.ix";
connectAttr "c_Lf_up_eyelids_upplus_Xplus.o1" "c_Lf_up_eyelids_upreverse_X.ix";
connectAttr "c_nose_lfplus_Yplus.o1" "c_nose_lfreverse_Y.ix";
connectAttr "c_nose_upplus_Xplus.o1" "c_nose_upreverse_X.ix";
connectAttr "c_Rt_dn_eyelids_lfplus_Yplus.o1" "c_Rt_dn_eyelids_lfreverse_Y.ix";
connectAttr "c_Rt_dn_eyelids_upplus_Xplus.o1" "c_Rt_dn_eyelids_upreverse_X.ix";
connectAttr "c_Rt_eyebrows_01_lfplus_Yplus.o1" "c_Rt_eyebrows_01_lfreverse_Y.ix"
		;
connectAttr "c_Rt_eyebrows_01_upplus_Xplus.o1" "c_Rt_eyebrows_01_upreverse_X.ix"
		;
connectAttr "c_Rt_eyebrows_02_lfplus_Yplus.o1" "c_Rt_eyebrows_02_lfreverse_Y.ix"
		;
connectAttr "c_Rt_eyebrows_02_upplus_Xplus.o1" "c_Rt_eyebrows_02_upreverse_X.ix"
		;
connectAttr "c_Rt_eyebrows_03_lfplus_Yplus.o1" "c_Rt_eyebrows_03_lfreverse_Y.ix"
		;
connectAttr "c_Rt_eyebrows_03_upplus_Xplus.o1" "c_Rt_eyebrows_03_upreverse_X.ix"
		;
connectAttr "c_Rt_eyeStretch_lfplus_Yplus.o1" "c_Rt_eyeStretch_lfreverse_Y.ix";
connectAttr "c_Rt_eyeStretch_upplus_Xplus.o1" "c_Rt_eyeStretch_upreverse_X.ix";
connectAttr "c_Rt_mouthLip_lfplus_Yplus.o1" "c_Rt_mouthLip_lfreverse_Y.ix";
connectAttr "c_Rt_mouthLip_upplus_Xplus.o1" "c_Rt_mouthLip_upreverse_X.ix";
connectAttr "c_Rt_up_eyelids_lfplus_Yplus.o1" "c_Rt_up_eyelids_lfreverse_Y.ix";
connectAttr "c_Rt_up_eyelids_upplus_Xplus.o1" "c_Rt_up_eyelids_upreverse_X.ix";
connectAttr "c_up_mouthLip_lfplus_Yplus.o1" "c_up_mouthLip_lfreverse_Y.ix";
connectAttr "c_up_mouthLip_upplus_Xplus.o1" "c_up_mouthLip_upreverse_X.ix";
connectAttr "E_lfplus_Yplus.o1" "E_lfreverse_Y.ix";
connectAttr "E_upplus_Xplus.o1" "E_upreverse_X.ix";
connectAttr "FV_lfplus_Yplus.o1" "FV_lfreverse_Y.ix";
connectAttr "FV_upplus_Xplus.o1" "FV_upreverse_X.ix";
connectAttr "I_lfplus_Yplus.o1" "I_lfreverse_Y.ix";
connectAttr "I_upplus_Xplus.o1" "I_upreverse_X.ix";
connectAttr "O_lfplus_Yplus.o1" "O_lfreverse_Y.ix";
connectAttr "O_upplus_Xplus.o1" "O_upreverse_X.ix";
connectAttr "OU_lfplus_Yplus.o1" "OU_lfreverse_Y.ix";
connectAttr "OU_upplus_Xplus.o1" "OU_upreverse_X.ix";
connectAttr "tongue_lfplus_Yplus.o1" "tongue_lfreverse_Y.ix";
connectAttr "tongue_upplus_Xplus.o1" "tongue_upreverse_X.ix";
connectAttr "U_lfplus_Yplus.o1" "U_lfreverse_Y.ix";
connectAttr "U_upplus_Xplus.o1" "U_upreverse_X.ix";
connectAttr "c_tongue_CTRL.rx" "unitConversion1.i";
connectAttr "c_tongue_CTRL.ry" "unitConversion2.i";
connectAttr "c_tongue_CTRL.rz" "unitConversion3.i";
connectAttr "hyperView1.msg" "nodeEditorPanel2Info.b[0]";
connectAttr "hyperLayout1.msg" "hyperView1.hl";
connectAttr "hyperView2.msg" "nodeEditorPanel1Info.b[0]";
connectAttr "hyperLayout2.msg" "hyperView2.hl";
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
// End of High_pannel_rig.ma

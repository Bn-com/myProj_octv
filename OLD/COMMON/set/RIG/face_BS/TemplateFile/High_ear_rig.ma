//Maya ASCII 2014 scene
//Name: High_ear_rig.ma
//Last modified: Fri, Jul 31, 2015 03:14:23 PM
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
currentUnit -l centimeter -a degree -t pal;
fileInfo "application" "maya";
fileInfo "product" "Maya 2014";
fileInfo "version" "2014";
fileInfo "cutIdentifier" "201310090313-890429";
fileInfo "osv" "Microsoft Windows 7 Ultimate Edition, 64-bit Windows 7 Service Pack 1 (Build 7601)\n";
createNode transform -n "GRP_EAR_TEMPLATE";
createNode nurbsCurve -n "GRP_EAR_TEMPLATEShape" -p "GRP_EAR_TEMPLATE";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-3.0000000000000027 0 -2.0000000000000004
		-3.0000000000000027 0 2.0000000000000004
		3.0000000000000027 0 2.0000000000000004
		3.0000000000000027 0 -2.0000000000000004
		-3.0000000000000027 0 -2.0000000000000004
		;
createNode transform -n "Lf_ear_TEMPLATE" -p "GRP_EAR_TEMPLATE";
	setAttr ".t" -type "double3" 1.7760719757257193 0 0 ;
createNode nurbsCurve -n "Lf_ear_TEMPLATEShape" -p "Lf_ear_TEMPLATE";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.51798270322925499 0.39588198362064903 -9.3675067702747583e-017
		0.11570288517591698 0.41580680778465995 -9.3675067702747583e-017
		0.012718672618316162 0.2696804613791417 -6.591949208711867e-017
		-0.0043585436105586517 -0.095791089619662942 -3.4694469519536142e-018
		-0.038712450622192085 -0.46031569316304161 5.8980598183211441e-017
		-0.06666210691723462 -0.61055473586064912 8.6736173798840355e-017
		0.30587802314590085 -0.47920293704566197 6.591949208711867e-017
		0.54406847065351194 -0.12585075626382508 3.4694469519536142e-018
		0.51798270322925499 0.39588198362064903 -9.3675067702747583e-017
		0.11570288517591698 0.41580680778465995 -9.3675067702747583e-017
		0.012718672618316162 0.2696804613791417 -6.591949208711867e-017
		;
createNode transform -n "ear_L_joint0_GRP" -p "Lf_ear_TEMPLATE";
createNode joint -n "ear_L_joint0" -p "ear_L_joint0_GRP";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.72774759282211765 -0.24896477548320489 -0.63906179803694307 0
		 0.18707400114173467 0.96851254022268463 -0.16427652762407927 0 0.65983843419312538 -2.3037127760971998e-015 0.75140750645808996 0
		 0.88042611893070433 1.8924287444956307 -0.24426614000907937 1;
	setAttr ".radi" 0.2;
createNode joint -n "ear_L_joint1" -p "ear_L_joint0";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".t" -type "double3" 0.27397497111621683 4.9130118373207886e-017 -3.3406778380496223e-016 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.72774759282211765 -0.24896477548320489 -0.63906179803694307 0
		 0.17441843888766773 0.96833534564561108 -0.17861933419813122 0 0.66329604952660615 0.018525629327829734 0.74812776431596606 0
		 0.88042611893070433 1.8924287444956307 -0.24426614000907937 1;
	setAttr ".radi" 0.2;
createNode joint -n "ear_L_joint2" -p "ear_L_joint1";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.24830838789714288 8.3266726846886741e-017 5.5511151231257827e-017 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.72774759282211765 -0.24896477548320489 -0.63906179803694307 0
		 0.17441843888766773 0.96833534564561108 -0.17861933419813122 0 0.66329604952660615 0.018525629327829734 0.74812776431596606 0
		 1.0287221325187565 1.8416962046807883 -0.37449029742303092 1;
	setAttr ".radi" 0.2;
createNode transform -n "Rt_ear_TEMPLATE" -p "GRP_EAR_TEMPLATE";
	setAttr ".t" -type "double3" -1.7760719757257193 0 0 ;
createNode nurbsCurve -n "Rt_ear_TEMPLATEShape" -p "Rt_ear_TEMPLATE";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-0.51798270322925499 0.39588198362064903 -5.9161992021686092e-017
		-0.11570288517591698 0.41580680778465995 -5.7095602671295312e-018
		-0.012718672618316162 0.2696804613791417 -3.3362762749628263e-018
		0.0043585436105586517 -0.095791089619662942 -2.6931497209865109e-017
		0.038712450622192085 -0.46031569316304161 -5.0294782910717769e-017
		0.06666210691723462 -0.61055473586064912 -5.5867712892452755e-017
		-0.30587802314590085 -0.47920293704566197 -8.9615292983367197e-017
		-0.54406847065351194 -0.12585075626382508 -9.3274590300918483e-017
		-0.51798270322925499 0.39588198362064903 -5.9161992021686092e-017
		-0.11570288517591698 0.41580680778465995 -5.7095602671295312e-018
		-0.012718672618316162 0.2696804613791417 -3.3362762749628263e-018
		;
createNode transform -n "ear_R_joint0_GRP" -p "Rt_ear_TEMPLATE";
	setAttr ".r" -type "double3" -180 0 0 ;
createNode joint -n "ear_R_joint0" -p "ear_R_joint0_GRP";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.72774759282211765 -0.24896477548320489 -0.63906179803694307 0
		 0.18707400114173467 0.96851254022268463 -0.16427652762407927 0 0.65983843419312538 -2.3037127760971998e-015 0.75140750645808996 0
		 0.88042611893070433 1.8924287444956307 -0.24426614000907937 1;
	setAttr ".radi" 0.2;
createNode joint -n "ear_R_joint1" -p "ear_R_joint0";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".t" -type "double3" -0.27397000000000005 0 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.72774759282211765 -0.24896477548320489 -0.63906179803694307 0
		 0.17441843888766773 0.96833534564561108 -0.17861933419813122 0 0.66329604952660615 0.018525629327829734 0.74812776431596606 0
		 0.88042611893070433 1.8924287444956307 -0.24426614000907937 1;
	setAttr ".radi" 0.2;
createNode joint -n "ear_R_joint2" -p "ear_R_joint1";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -0.24831000000000003 0 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.72774759282211765 -0.24896477548320489 -0.63906179803694307 0
		 0.17441843888766773 0.96833534564561108 -0.17861933419813122 0 0.66329604952660615 0.018525629327829734 0.74812776431596606 0
		 1.0287221325187565 1.8416962046807883 -0.37449029742303092 1;
	setAttr ".radi" 0.2;
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
	setAttr -k on ".an" yes;
	setAttr -k on ".ar";
	setAttr -k on ".fs";
	setAttr -k on ".ef";
	setAttr -av -k on ".bfs";
	setAttr -cb on ".me";
	setAttr -cb on ".se";
	setAttr -av -k on ".be";
	setAttr -k on ".ep";
	setAttr -k on ".fec";
	setAttr -av -k on ".ofc";
	setAttr -cb on ".ofe";
	setAttr -cb on ".efe";
	setAttr -cb on ".oft";
	setAttr -cb on ".umfn";
	setAttr -cb on ".ufe";
	setAttr -k on ".pff" yes;
	setAttr -k on ".peie";
	setAttr -k on ".ifp" -type "string" "<RenderLayer>/<Scene>_<RenderLayer>";
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
select -ne :defaultRenderQuality;
	setAttr -k on ".cch";
	setAttr -k on ".nds";
	setAttr -k on ".rtb";
	setAttr ".eaa" 0;
	setAttr ".ufil" yes;
	setAttr -k on ".pft";
	setAttr -av -k on ".pfwx";
	setAttr -av -k on ".pfwy";
	setAttr -k on ".pifw";
	setAttr -av -k on ".ss" 2;
	setAttr -av -k on ".mss";
	setAttr -k on ".mvs";
	setAttr -k on ".mvm";
	setAttr -k on ".vs";
	setAttr -k on ".pss";
	setAttr -k on ".ert";
	setAttr -k on ".rct";
	setAttr -k on ".gct";
	setAttr -k on ".bct";
	setAttr -k on ".cct";
select -ne :defaultResolution;
	setAttr -av -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -k on ".bnm";
	setAttr -av -k on ".w" 1280;
	setAttr -av -k on ".h" 720;
	setAttr -av -k on ".pa" 1;
	setAttr -av -k on ".al";
	setAttr -av -k on ".dar" 1.7779999971389771;
	setAttr -av -k on ".ldar" yes;
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
connectAttr "ear_L_joint0.s" "ear_L_joint1.is";
connectAttr "ear_L_joint1.s" "ear_L_joint2.is";
connectAttr "ear_R_joint0.s" "ear_R_joint1.is";
connectAttr "ear_R_joint1.s" "ear_R_joint2.is";
// End of High_ear_rig.ma

//Maya ASCII 2014 scene
//Name: High_tongue_rig.ma
//Last modified: Fri, Jul 31, 2015 03:19:24 PM
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
createNode transform -n "GRP_TONGUE_TEMPLATE";
	setAttr ".t" -type "double3" 0 1.8136399665625667 0 ;
	setAttr ".rp" -type "double3" -7.7124598275076113e-016 3.7402844379854288 0.31744866979326941 ;
	setAttr ".sp" -type "double3" -7.7124598275076113e-016 3.7402844379854288 0.31744866979326941 ;
createNode transform -n "GRP_tongue_Rig_all" -p "GRP_TONGUE_TEMPLATE";
	setAttr ".rp" -type "double3" -7.7124598275075846e-016 3.7402844379854288 0.31744866979326941 ;
	setAttr ".sp" -type "double3" -7.7124598275075846e-016 3.7402844379854288 0.31744866979326941 ;
createNode transform -n "GRP_tongueRig" -p "GRP_tongue_Rig_all";
	setAttr ".t" -type "double3" -1.653664778101241e-016 0 6.6613381477509392e-016 ;
	setAttr ".s" -type "double3" 1.0000000000000004 1 1.0000000000000004 ;
	setAttr ".rp" -type "double3" -6.0587950494063702e-016 3.7402844379854288 0.31744866979326875 ;
	setAttr ".sp" -type "double3" -6.0587950494063426e-016 3.7402844379854288 0.31744866979326858 ;
	setAttr ".spt" -type "double3" -2.8103169748498546e-030 0 1.6653345369377454e-016 ;
createNode transform -n "GRP_tongue_move" -p "GRP_tongueRig";
createNode transform -n "GRP_tongue_joint1_move" -p "GRP_tongue_move";
	setAttr ".t" -type "double3" 6.0587950494063406e-016 0 0 ;
	setAttr ".rp" -type "double3" -6.0587950494063416e-016 3.7402844379854288 0.31744866979326858 ;
	setAttr ".sp" -type "double3" -6.0587950494063416e-016 3.7402844379854288 0.31744866979326858 ;
createNode transform -n "GRP_tongue_joint1" -p "GRP_tongue_joint1_move";
	setAttr ".t" -type "double3" -6.0587950494063416e-016 3.7402844379854288 0.31744866979326858 ;
createNode joint -n "c_tongue_joint1" -p "GRP_tongue_joint1";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
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
	addAttr -ci true -sn "driven_envelope" -ln "driven_envelope" -at "double";
	setAttr ".uoc" yes;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1.0000000000000004 0 0 0 0 1 0 0 0 0 1.0000000000000004 0
		 -7.7124598275076113e-016 3.7402844379854288 0.31744866979326941 1;
	setAttr ".radi" 0.1;
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
createNode transform -n "c_GRP_tongue_joint2__move" -p "c_tongue_joint1";
	setAttr ".rp" -type "double3" 0 8.8817841970012523e-016 0.094000000000000083 ;
	setAttr ".sp" -type "double3" 0 8.8817841970012523e-016 0.094000000000000083 ;
createNode transform -n "c_GRP_tongue_joint2" -p "c_GRP_tongue_joint2__move";
	setAttr ".t" -type "double3" 0 4.4408920985006262e-016 0.094 ;
createNode joint -n "c_tongue_joint2" -p "c_GRP_tongue_joint2";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 3;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1.0000000000000004 0 0 0 0 1 0 0 0 0 1.0000000000000004 0
		 -7.7124598275076113e-016 3.7402844379854292 0.41144866979326944 1;
	setAttr ".radi" 0.1;
createNode transform -n "c_GRP_tongue_joint3__move" -p "c_tongue_joint2";
	setAttr ".rp" -type "double3" 0 8.8817841970012523e-016 0.094000000000000083 ;
	setAttr ".sp" -type "double3" 0 8.8817841970012523e-016 0.094000000000000083 ;
createNode transform -n "c_GRP_tongue_joint3" -p "c_GRP_tongue_joint3__move";
	setAttr ".t" -type "double3" 0 4.4408920985006262e-016 0.094 ;
createNode joint -n "c_tongue_joint3" -p "c_GRP_tongue_joint3";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 6;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1.0000000000000004 0 0 0 0 1 0 0 0 0 1.0000000000000004 0
		 -7.7124598275076113e-016 3.7402844379854296 0.50544866979326952 1;
	setAttr ".radi" 0.1;
createNode transform -n "c_GRP_tongue_joint4__move" -p "c_tongue_joint3";
	setAttr ".rp" -type "double3" 0 0 0.093999999999999861 ;
	setAttr ".sp" -type "double3" 0 0 0.093999999999999861 ;
createNode transform -n "c_GRP_tongue_joint4" -p "c_GRP_tongue_joint4__move";
createNode joint -n "c_tongue_joint4" -p "c_GRP_tongue_joint4";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 1;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1.0000000000000004 0 0 0 0 1 0 0 0 0 1.0000000000000004 0
		 -7.7124598275076113e-016 3.7402844379854296 0.59944866979326961 1;
	setAttr ".radi" 0.1;
createNode transform -n "c_GRP_tongue_joint5__move" -p "c_tongue_joint4";
	setAttr ".rp" -type "double3" 0 0 0.094000000000000083 ;
	setAttr ".sp" -type "double3" 0 0 0.094000000000000083 ;
createNode transform -n "c_GRP_tongue_joint5" -p "c_GRP_tongue_joint5__move";
createNode joint -n "c_tongue_joint5" -p "c_GRP_tongue_joint5";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 4;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1.0000000000000004 0 0 0 0 1 0 0 0 0 1.0000000000000004 0
		 -7.7124598275076113e-016 3.7402844379854296 0.69344866979326969 1;
	setAttr ".radi" 0.1;
createNode transform -n "c_GRP_tongue_joint6__move" -p "c_tongue_joint5";
	setAttr ".rp" -type "double3" 0 4.4408920985006262e-016 0.094000000000000861 ;
	setAttr ".sp" -type "double3" 0 4.4408920985006262e-016 0.094000000000000861 ;
createNode transform -n "c_GRP_tongue_joint6" -p "c_GRP_tongue_joint6__move";
	setAttr ".t" -type "double3" 0 4.4408920985006262e-016 0.094 ;
createNode joint -n "c_tongue_joint6" -p "c_GRP_tongue_joint6";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" 0 0 8.8817841970012523e-016 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1.0000000000000004 0 0 0 0 1 0 0 0 0 1.0000000000000004 0
		 -7.7124598275076113e-016 3.7402844379854301 0.78744866979327066 1;
	setAttr ".radi" 0.1;
createNode transform -n "c_GRP_tongue_joint7__move" -p "c_tongue_joint6";
	setAttr ".rp" -type "double3" 0 4.4408920985006262e-016 0.093999999999999195 ;
	setAttr ".sp" -type "double3" 0 4.4408920985006262e-016 0.093999999999999195 ;
createNode transform -n "c_GRP_tongue_joint7" -p "c_GRP_tongue_joint7__move";
createNode joint -n "c_tongue_joint7" -p "c_GRP_tongue_joint7";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 0 0 -8.8817841970012523e-016 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1.0000000000000004 0 0 0 0 1 0 0 0 0 1.0000000000000004 0
		 -7.7124598275076113e-016 3.7402844379854301 0.88144866979326986 1;
	setAttr ".radi" 0.1;
createNode transform -n "c_GRP_tongue_joint8__move" -p "c_tongue_joint7";
	setAttr ".rp" -type "double3" 0 1.3322676295501878e-015 0.093999999999999861 ;
	setAttr ".sp" -type "double3" 0 1.3322676295501878e-015 0.093999999999999861 ;
createNode transform -n "c_GRP_tongue_joint8" -p "c_GRP_tongue_joint8__move";
	setAttr ".t" -type "double3" 0 8.8817841970012523e-016 0.094 ;
createNode joint -n "c_tongue_joint8" -p "c_GRP_tongue_joint8";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1.0000000000000004 0 0 0 0 1 0 0 0 0 1.0000000000000004 0
		 -7.7124598275076113e-016 3.740284437985431 0.97544866979326994 1;
	setAttr ".radi" 0.1;
createNode transform -n "c_GRP_tongue_joint9__move" -p "c_tongue_joint8";
	setAttr ".rp" -type "double3" 0 0 0.094000000000000861 ;
	setAttr ".sp" -type "double3" 0 0 0.094000000000000861 ;
createNode transform -n "c_GRP_tongue_joint9" -p "c_GRP_tongue_joint9__move";
createNode joint -n "c_tongue_joint9" -p "c_GRP_tongue_joint9";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".t" -type "double3" 0 0 8.8817841970012523e-016 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1.0000000000000004 0 0 0 0 1 0 0 0 0 1.0000000000000004 0
		 -7.7124598275076113e-016 3.740284437985431 1.0694486697932708 1;
	setAttr ".radi" 0.1;
createNode transform -n "c_GRP_tongue_joint10__move" -p "c_tongue_joint9";
	setAttr ".rp" -type "double3" 0 0 0.094000000000000195 ;
	setAttr ".sp" -type "double3" 0 0 0.094000000000000195 ;
createNode transform -n "c_GRP_tongue_joint10" -p "c_GRP_tongue_joint10__move";
createNode joint -n "c_tongue_joint10" -p "c_GRP_tongue_joint10";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 3;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1.0000000000000004 0 0 0 0 1 0 0 0 0 1.0000000000000004 0
		 -7.7124598275076113e-016 3.740284437985431 1.1634486697932709 1;
	setAttr ".radi" 0.1;
createNode transform -n "c_GRP_tongue_joint11__move" -p "c_tongue_joint10";
	setAttr ".rp" -type "double3" 0 1.3322676295501878e-015 0.093999999999999195 ;
	setAttr ".sp" -type "double3" 0 1.3322676295501878e-015 0.093999999999999195 ;
createNode transform -n "c_GRP_tongue_joint11" -p "c_GRP_tongue_joint11__move";
	setAttr ".t" -type "double3" 0 4.4408920985006262e-016 0.094 ;
createNode joint -n "c_tongue_joint11" -p "c_GRP_tongue_joint11";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 0 0 -8.8817841970012523e-016 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1.0000000000000004 0 0 0 0 1 0 0 0 0 1.0000000000000004 0
		 -7.7124598275076113e-016 3.7402844379854314 1.2574486697932701 1;
	setAttr ".radi" 0.1;
createNode transform -n "c_GRP_tongue_joint12" -p "c_tongue_joint11";
createNode joint -n "c_tongue_joint12" -p "c_GRP_tongue_joint12";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1.0000000000000004 0 0 0 0 1 0 0 0 0 1.0000000000000004 0
		 -7.7124598275076113e-016 3.7402844379854314 1.3514486697932702 1;
	setAttr ".radi" 0.1;
createNode nurbsCurve -n "nurbsCircleShape1" -p "c_tongue_joint12";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.10784282992813311 0.11060484006477474 7.3419665812928279e-007
		-7.3027598049356234e-018 0.15641862527749434 7.3419665812631172e-007
		-0.107842829928133 0.11060485250723417 7.3419665812928279e-007
		-0.15251279268906087 6.20941792774668e-007 7.3419665813645452e-007
		-0.107842829928133 -0.11060361062364878 7.3419665814362666e-007
		-2.2655136510439675e-017 -0.15641738339390932 7.3419665814659731e-007
		0.10784282992813292 -0.11060362306610819 7.3419665814362666e-007
		0.15251279268906087 6.0849933328552993e-007 7.3419665813645452e-007
		0.10784282992813311 0.11060484006477474 7.3419665812928279e-007
		-7.3027598049356234e-018 0.15641862527749434 7.3419665812631172e-007
		-0.107842829928133 0.11060485250723417 7.3419665812928279e-007
		;
createNode nurbsCurve -n "nurbsCircleShape1" -p "c_tongue_joint11";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.10784282992813311 0.11060484006477474 7.3419665812928279e-007
		-7.3027598049356234e-018 0.15641862527749434 7.3419665812631172e-007
		-0.107842829928133 0.11060485250723417 7.3419665812928279e-007
		-0.15251279268906087 6.20941792774668e-007 7.3419665813645452e-007
		-0.107842829928133 -0.11060361062364878 7.3419665814362666e-007
		-2.2655136510439675e-017 -0.15641738339390932 7.3419665814659731e-007
		0.10784282992813292 -0.11060362306610819 7.3419665814362666e-007
		0.15251279268906087 6.0849933328552993e-007 7.3419665813645452e-007
		0.10784282992813311 0.11060484006477474 7.3419665812928279e-007
		-7.3027598049356234e-018 0.15641862527749434 7.3419665812631172e-007
		-0.107842829928133 0.11060485250723417 7.3419665812928279e-007
		;
createNode nurbsCurve -n "nurbsCircleShape1" -p "c_tongue_joint10";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.10784282992813311 0.11060484006477474 7.3419665812928279e-007
		-7.3027598049356234e-018 0.15641862527749434 7.3419665812631172e-007
		-0.107842829928133 0.11060485250723417 7.3419665812928279e-007
		-0.15251279268906087 6.20941792774668e-007 7.3419665813645452e-007
		-0.107842829928133 -0.11060361062364878 7.3419665814362666e-007
		-2.2655136510439675e-017 -0.15641738339390932 7.3419665814659731e-007
		0.10784282992813292 -0.11060362306610819 7.3419665814362666e-007
		0.15251279268906087 6.0849933328552993e-007 7.3419665813645452e-007
		0.10784282992813311 0.11060484006477474 7.3419665812928279e-007
		-7.3027598049356234e-018 0.15641862527749434 7.3419665812631172e-007
		-0.107842829928133 0.11060485250723417 7.3419665812928279e-007
		;
createNode nurbsCurve -n "nurbsCircleShape1" -p "c_tongue_joint9";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.10784282992813311 0.11060484006477474 7.3419665812928279e-007
		-7.3027598049356234e-018 0.15641862527749434 7.3419665812631172e-007
		-0.107842829928133 0.11060485250723417 7.3419665812928279e-007
		-0.15251279268906087 6.20941792774668e-007 7.3419665813645452e-007
		-0.107842829928133 -0.11060361062364878 7.3419665814362666e-007
		-2.2655136510439675e-017 -0.15641738339390932 7.3419665814659731e-007
		0.10784282992813292 -0.11060362306610819 7.3419665814362666e-007
		0.15251279268906087 6.0849933328552993e-007 7.3419665813645452e-007
		0.10784282992813311 0.11060484006477474 7.3419665812928279e-007
		-7.3027598049356234e-018 0.15641862527749434 7.3419665812631172e-007
		-0.107842829928133 0.11060485250723417 7.3419665812928279e-007
		;
createNode nurbsCurve -n "nurbsCircleShape1" -p "c_tongue_joint8";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.10784282992813311 0.11060484006477474 7.3419665812928279e-007
		-7.3027598049356234e-018 0.15641862527749434 7.3419665812631172e-007
		-0.107842829928133 0.11060485250723417 7.3419665812928279e-007
		-0.15251279268906087 6.20941792774668e-007 7.3419665813645452e-007
		-0.107842829928133 -0.11060361062364878 7.3419665814362666e-007
		-2.2655136510439675e-017 -0.15641738339390932 7.3419665814659731e-007
		0.10784282992813292 -0.11060362306610819 7.3419665814362666e-007
		0.15251279268906087 6.0849933328552993e-007 7.3419665813645452e-007
		0.10784282992813311 0.11060484006477474 7.3419665812928279e-007
		-7.3027598049356234e-018 0.15641862527749434 7.3419665812631172e-007
		-0.107842829928133 0.11060485250723417 7.3419665812928279e-007
		;
createNode nurbsCurve -n "nurbsCircleShape1" -p "c_tongue_joint7";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.10784282992813311 0.11060484006477474 7.3419665812928279e-007
		-7.3027598049356234e-018 0.15641862527749434 7.3419665812631172e-007
		-0.107842829928133 0.11060485250723417 7.3419665812928279e-007
		-0.15251279268906087 6.20941792774668e-007 7.3419665813645452e-007
		-0.107842829928133 -0.11060361062364878 7.3419665814362666e-007
		-2.2655136510439675e-017 -0.15641738339390932 7.3419665814659731e-007
		0.10784282992813292 -0.11060362306610819 7.3419665814362666e-007
		0.15251279268906087 6.0849933328552993e-007 7.3419665813645452e-007
		0.10784282992813311 0.11060484006477474 7.3419665812928279e-007
		-7.3027598049356234e-018 0.15641862527749434 7.3419665812631172e-007
		-0.107842829928133 0.11060485250723417 7.3419665812928279e-007
		;
createNode nurbsCurve -n "nurbsCircleShape1" -p "c_tongue_joint6";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.10784282992813311 0.11060484006477474 7.3419665812928279e-007
		-7.3027598049356234e-018 0.15641862527749434 7.3419665812631172e-007
		-0.107842829928133 0.11060485250723417 7.3419665812928279e-007
		-0.15251279268906087 6.20941792774668e-007 7.3419665813645452e-007
		-0.107842829928133 -0.11060361062364878 7.3419665814362666e-007
		-2.2655136510439675e-017 -0.15641738339390932 7.3419665814659731e-007
		0.10784282992813292 -0.11060362306610819 7.3419665814362666e-007
		0.15251279268906087 6.0849933328552993e-007 7.3419665813645452e-007
		0.10784282992813311 0.11060484006477474 7.3419665812928279e-007
		-7.3027598049356234e-018 0.15641862527749434 7.3419665812631172e-007
		-0.107842829928133 0.11060485250723417 7.3419665812928279e-007
		;
createNode nurbsCurve -n "nurbsCircleShape1" -p "c_tongue_joint5";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.10784282992813311 0.11060484006477474 7.3419665812928279e-007
		-7.3027598049356234e-018 0.15641862527749434 7.3419665812631172e-007
		-0.107842829928133 0.11060485250723417 7.3419665812928279e-007
		-0.15251279268906087 6.20941792774668e-007 7.3419665813645452e-007
		-0.107842829928133 -0.11060361062364878 7.3419665814362666e-007
		-2.2655136510439675e-017 -0.15641738339390932 7.3419665814659731e-007
		0.10784282992813292 -0.11060362306610819 7.3419665814362666e-007
		0.15251279268906087 6.0849933328552993e-007 7.3419665813645452e-007
		0.10784282992813311 0.11060484006477474 7.3419665812928279e-007
		-7.3027598049356234e-018 0.15641862527749434 7.3419665812631172e-007
		-0.107842829928133 0.11060485250723417 7.3419665812928279e-007
		;
createNode nurbsCurve -n "nurbsCircleShape1" -p "c_tongue_joint4";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.10784282992813311 0.11060484006477474 7.3419665812928279e-007
		-7.3027598049356234e-018 0.15641862527749434 7.3419665812631172e-007
		-0.107842829928133 0.11060485250723417 7.3419665812928279e-007
		-0.15251279268906087 6.20941792774668e-007 7.3419665813645452e-007
		-0.107842829928133 -0.11060361062364878 7.3419665814362666e-007
		-2.2655136510439675e-017 -0.15641738339390932 7.3419665814659731e-007
		0.10784282992813292 -0.11060362306610819 7.3419665814362666e-007
		0.15251279268906087 6.0849933328552993e-007 7.3419665813645452e-007
		0.10784282992813311 0.11060484006477474 7.3419665812928279e-007
		-7.3027598049356234e-018 0.15641862527749434 7.3419665812631172e-007
		-0.107842829928133 0.11060485250723417 7.3419665812928279e-007
		;
createNode nurbsCurve -n "nurbsCircleShape1" -p "c_tongue_joint3";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.10784282992813311 0.11060484006477474 7.3419665812928279e-007
		-7.3027598049356234e-018 0.15641862527749434 7.3419665812631172e-007
		-0.107842829928133 0.11060485250723417 7.3419665812928279e-007
		-0.15251279268906087 6.20941792774668e-007 7.3419665813645452e-007
		-0.107842829928133 -0.11060361062364878 7.3419665814362666e-007
		-2.2655136510439675e-017 -0.15641738339390932 7.3419665814659731e-007
		0.10784282992813292 -0.11060362306610819 7.3419665814362666e-007
		0.15251279268906087 6.0849933328552993e-007 7.3419665813645452e-007
		0.10784282992813311 0.11060484006477474 7.3419665812928279e-007
		-7.3027598049356234e-018 0.15641862527749434 7.3419665812631172e-007
		-0.107842829928133 0.11060485250723417 7.3419665812928279e-007
		;
createNode nurbsCurve -n "nurbsCircleShape1" -p "c_tongue_joint2";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.10784282992813311 0.11060484006477474 7.3419665812928279e-007
		-7.3027598049356234e-018 0.15641862527749434 7.3419665812631172e-007
		-0.107842829928133 0.11060485250723417 7.3419665812928279e-007
		-0.15251279268906087 6.20941792774668e-007 7.3419665813645452e-007
		-0.107842829928133 -0.11060361062364878 7.3419665814362666e-007
		-2.2655136510439675e-017 -0.15641738339390932 7.3419665814659731e-007
		0.10784282992813292 -0.11060362306610819 7.3419665814362666e-007
		0.15251279268906087 6.0849933328552993e-007 7.3419665813645452e-007
		0.10784282992813311 0.11060484006477474 7.3419665812928279e-007
		-7.3027598049356234e-018 0.15641862527749434 7.3419665812631172e-007
		-0.107842829928133 0.11060485250723417 7.3419665812928279e-007
		;
createNode nurbsCurve -n "nurbsCircleShape1" -p "c_tongue_joint1";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.10784282992813311 0.11060484006477474 7.3419665812928279e-007
		-7.3027598049356234e-018 0.15641862527749434 7.3419665812631172e-007
		-0.107842829928133 0.11060485250723417 7.3419665812928279e-007
		-0.15251279268906087 6.20941792774668e-007 7.3419665813645452e-007
		-0.107842829928133 -0.11060361062364878 7.3419665814362666e-007
		-2.2655136510439675e-017 -0.15641738339390932 7.3419665814659731e-007
		0.10784282992813292 -0.11060362306610819 7.3419665814362666e-007
		0.15251279268906087 6.0849933328552993e-007 7.3419665813645452e-007
		0.10784282992813311 0.11060484006477474 7.3419665812928279e-007
		-7.3027598049356234e-018 0.15641862527749434 7.3419665812631172e-007
		-0.107842829928133 0.11060485250723417 7.3419665812928279e-007
		;
createNode transform -n "GRP_Tongue_M_move" -p "GRP_tongue_Rig_all";
	setAttr ".t" -type "double3" 1.9928598618145811e-028 0.36151246942582915 0.39267777591549513 ;
	setAttr ".rp" -type "double3" -7.7124598275096041e-016 3.3787719685596023 1.2258537058013363 ;
	setAttr ".sp" -type "double3" -7.7124598275096041e-016 3.3787719685596023 1.2258537058013363 ;
createNode transform -n "Tongue_M_GRPB" -p "GRP_Tongue_M_move";
	setAttr ".t" -type "double3" -1.6536647781032605e-016 -4.4408920985006262e-016 
		6.6613381477509392e-016 ;
	setAttr ".r" -type "double3" -1.0933156717530828e-014 1.8834753950676954e-014 -6.4884622438510203e-015 ;
	setAttr ".s" -type "double3" 1.0000000000000004 1 1.0000000000000004 ;
	setAttr ".rp" -type "double3" 0 3.3787719685596027 1.2258537058013357 ;
	setAttr ".sp" -type "double3" 0 3.3787719685596027 1.2258537058013352 ;
	setAttr ".spt" -type "double3" 0 0 4.4408920985006281e-016 ;
createNode transform -n "Tongue_M_GRPA" -p "Tongue_M_GRPB";
	setAttr ".rp" -type "double3" 0 3.3787719685596027 1.2258537058013352 ;
	setAttr ".sp" -type "double3" 0 3.3787719685596027 1.2258537058013352 ;
createNode transform -n "Tongue_M" -p "Tongue_M_GRPA";
	addAttr -ci true -sn "sign" -ln "sign" -dv 73 -at "long";
	addAttr -ci true -sn "vis_second" -ln "vis_second" -min 0 -max 1 -en "OFF:ON" -at "enum";
	addAttr -ci true -sn "Tongue_5" -ln "Tongue_5" -dv 1 -at "float";
	addAttr -ci true -sn "Tongue_4" -ln "Tongue_4" -dv 1 -at "float";
	addAttr -ci true -sn "Tongue_3" -ln "Tongue_3" -dv 1 -at "float";
	addAttr -ci true -sn "Tongue_2" -ln "Tongue_2" -dv 1 -at "float";
	addAttr -ci true -sn "rotateWeight" -ln "rotateWeight" -at "double";
	addAttr -ci true -sn "drivenJoint" -ln "drivenJoint" -min 1 -max 12 -at "double";
	addAttr -ci true -sn "tongue_boundMesh" -ln "tongue_boundMesh" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "tongue_skinMesh" -ln "tongue_skinMesh" -min 0 -max 1 -at "bool";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" -6.0587950494063406e-016 0 0 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 0 3.3787719685596027 1.2258537058013352 ;
	setAttr ".sp" -type "double3" 0 3.3787719685596027 1.2258537058013352 ;
	setAttr ".mntl" -type "double3" -0.31 -0.31 -1.24 ;
	setAttr ".mxtl" -type "double3" 0.31 0.31 1.24 ;
	setAttr -k on ".vis_second" 1;
	setAttr -k on ".rotateWeight" 0.3;
	setAttr -k on ".drivenJoint" 12;
	setAttr -cb on ".tongue_skinMesh";
createNode nurbsCurve -n "Tongue_MShape" -p "Tongue_M";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".cc" -type "nurbsCurve" 
		1 52 0 no 3
		53 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52
		53
		0 3.4432152565083083 1.2258537058013352
		0 3.4383098334296527 1.2505150565634098
		0 3.4243402685711484 1.2714220058128809
		0 3.4034333193216773 1.2853915706713857
		0 3.3787719685596027 1.290296993750041
		0 3.3541106177975282 1.2853915706713857
		0 3.3332036685480571 1.2714220058128809
		0 3.3192341036895519 1.2505150565634098
		0 3.3143286806108967 1.2258537058013352
		0 3.3192341036895519 1.2011923550392607
		0 3.3332036685480571 1.1802854057897896
		0 3.3541106177975282 1.1663158409312848
		0 3.3787719685596027 1.1614104178526294
		0 3.4034333193216773 1.1663158409312848
		0 3.4243402685711484 1.1802854057897896
		0 3.4383098334296527 1.2011923550392607
		0 3.4432152565083083 1.2258537058013352
		0.02466135076207461 3.4383098334296527 1.2258537058013352
		0.045568300011545569 3.4243402685711484 1.2258537058013352
		0.059537864870050389 3.4034333193216773 1.2258537058013352
		0.06444328794870588 3.3787719685596027 1.2258537058013352
		0.059537864870050389 3.3541106177975282 1.2258537058013352
		0.045568300011545569 3.3332036685480571 1.2258537058013352
		0.02466135076207461 3.3192341036895519 1.2258537058013352
		0 3.3143286806108967 1.2258537058013352
		-0.02466135076207461 3.3192341036895519 1.2258537058013352
		-0.045568300011545569 3.3332036685480571 1.2258537058013352
		-0.059537864870050389 3.3541106177975282 1.2258537058013352
		-0.06444328794870588 3.3787719685596027 1.2258537058013352
		-0.059537864870050389 3.4034333193216773 1.2258537058013352
		-0.045568300011545569 3.4243402685711484 1.2258537058013352
		-0.02466135076207461 3.4383098334296527 1.2258537058013352
		0 3.4432152565083083 1.2258537058013352
		0 3.4383098334296527 1.2011923550392607
		0 3.4243402685711484 1.1802854057897896
		0 3.4034333193216773 1.1663158409312848
		0 3.3787719685596027 1.1614104178526294
		-0.02466135076207461 3.3787719685596027 1.1663158409312848
		-0.045568300011545569 3.3787719685596027 1.1802854057897896
		-0.059537864870050389 3.3787719685596027 1.2011923550392607
		-0.06444328794870588 3.3787719685596027 1.2258537058013352
		-0.059537864870050389 3.3787719685596027 1.2505150565634098
		-0.045568300011545569 3.3787719685596027 1.2714220058128809
		-0.02466135076207461 3.3787719685596027 1.2853915706713857
		0 3.3787719685596027 1.290296993750041
		0.02466135076207461 3.3787719685596027 1.2853915706713857
		0.045568300011545569 3.3787719685596027 1.2714220058128809
		0.059537864870050389 3.3787719685596027 1.2505150565634098
		0.06444328794870588 3.3787719685596027 1.2258537058013352
		0.059537864870050389 3.3787719685596027 1.2011923550392607
		0.045568300011545569 3.3787719685596027 1.1802854057897896
		0.02466135076207461 3.3787719685596027 1.1663158409312848
		0 3.3787719685596027 1.1614104178526294
		;
createNode nurbsCurve -n "GRP_Tongue_M_moveShape" -p "GRP_Tongue_M_move";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.11243725680719596 3.3787719685596023 1.1133238102103258
		-7.9057798012613145e-016 3.3787719685596023 1.0667507735247583
		-0.11243725680719741 3.3787719685596023 1.1133238102103258
		-0.15901029349276496 3.3787719685596023 1.2257610670175225
		-0.11243725680719746 3.3787719685596023 1.3381983238247193
		-8.2034971162404152e-016 3.3787719685596023 1.3847713605102867
		0.11243725680719585 3.3787719685596023 1.3381983238247193
		0.15901029349276341 3.3787719685596023 1.2257610670175225
		0.11243725680719596 3.3787719685596023 1.1133238102103258
		-7.9057798012613145e-016 3.3787719685596023 1.0667507735247583
		-0.11243725680719741 3.3787719685596023 1.1133238102103258
		;
createNode transform -n "GRP_tongue_mesh_template" -p "GRP_tongue_Rig_all";
	setAttr ".it" no;
createNode transform -n "tongue_boundMesh" -p "GRP_tongue_mesh_template";
createNode mesh -n "tongue_boundMeshShape" -p "tongue_boundMesh";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".vnm" 0;
createNode transform -n "tongue_skinMesh" -p "GRP_tongue_mesh_template";
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode mesh -n "tongue_skinMeshShape" -p "tongue_skinMesh";
	setAttr -k off ".v";
	setAttr -s 6 ".iog[0].og";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".vnm" 0;
	setAttr ".vcs" 2;
createNode mesh -n "tongue_skinMeshShapeOrig" -p "tongue_skinMesh";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 108 ".uvst[0].uvsp[0:107]" -type "float2" 0 0 1 1 1 0.45454547
		 0.5 0 0.5 0.45454547 0.5 0.18181819 0 0.18181819 0.25 0 0.25 0.18181819 0.25 0.090909094
		 0 0.090909094 0.125 0 0.125 0.090909094 0.125 0.18181819 0.5 0.090909094 0.375 0
		 0.375 0.090909094 0.375 0.18181819 0.25 0.45454547 0 0.27272728 0.25 0.27272728 0.125
		 0.27272728 1 0.36363637 0.25 0.36363637 0.125 0.36363637 0.125 0.45454547 0.5 0.27272728
		 0.375 0.27272728 0.5 0.36363637 0.375 0.36363637 0.375 0.45454547 0.75 0 0.75 0.18181819
		 0.75 0.090909094 0.625 0 0.625 0.090909094 0.625 0.18181819 0.875 0 0.875 0.090909094
		 0.875 0.18181819 0.75 0.45454547 0.75 0.27272728 0.625 0.27272728 0.75 0.36363637
		 0.625 0.36363637 0.625 0.45454547 0.875 0.27272728 0.875 0.36363637 0.875 0.45454547
		 0.5 1 0 0.72727275 0.5 0.72727275 0.25 0.72727275 0 0.54545456 0.25 0.54545456 0.125
		 0.54545456 0 0.63636363 0.25 0.63636363 0.125 0.63636363 0.125 0.72727275 0.5 0.54545456
		 0.375 0.54545456 0.5 0.63636363 0.375 0.63636363 0.375 0.72727275 0.25 1 0 0.81818181
		 0.25 0.81818181 0.125 0.81818181 1 0.90909094 0.25 0.90909094 0.125 0.90909094 0.125
		 1 0.5 0.81818181 0.375 0.81818181 0.5 0.90909094 0.375 0.90909094 0.375 1 0.75 0.72727275
		 0.75 0.54545456 0.625 0.54545456 0.75 0.63636363 0.625 0.63636363 0.625 0.72727275
		 0.875 0.54545456 0.875 0.63636363 0.875 0.72727275 0.75 1 0.75 0.81818181 0.625 0.81818181
		 0.75 0.90909094 0.625 0.90909094 0.625 1 0.875 0.81818181 0.875 0.90909094 0.875
		 1 0 0.36363637 0 0.45454547 1 0.090909094 1 0.18181819 1 0 1 0.27272728 0 0.90909094
		 0 1 1 0.63636363 1 0.72727275 1 0.54545456 1 0.81818181;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 96 ".vt[0:95]"  -7.5633944e-016 3.88143182 0.31744939 -7.6327833e-016 3.88143182 1.35144937
		 -7.6616952e-016 3.88143182 0.78744942 -8.0491169e-016 3.59913826 0.31744939 -8.0317697e-016 3.59913826 0.78744942
		 -8.0259871e-016 3.59913826 0.50544941 -7.5691769e-016 3.88143182 0.50544941 -0.1376228 3.74028516 0.31744939
		 -0.1376228 3.74028516 0.50544941 -0.1376228 3.74028516 0.4114494 -7.5836326e-016 3.88143182 0.4114494
		 -0.097314015 3.84009099 0.31744939 -0.097314015 3.84009099 0.4114494 -0.097314015 3.84009099 0.50544941
		 -8.0433343e-016 3.59913826 0.4114494 -0.097314015 3.64047933 0.31744939 -0.097314015 3.64047933 0.4114494
		 -0.097314015 3.64047933 0.50544941 -0.1376228 3.74028516 0.78744942 -7.5691769e-016 3.88143182 0.5994494
		 -0.1376228 3.74028516 0.5994494 -0.097314015 3.84009099 0.5994494 -7.5923062e-016 3.88143182 0.69344938
		 -0.1376228 3.74028516 0.69344938 -0.097314015 3.84009099 0.69344938 -0.097314015 3.84009099 0.78744942
		 -8.0491169e-016 3.59913826 0.5994494 -0.097314015 3.64047933 0.5994494 -8.0664642e-016 3.59913826 0.69344938
		 -0.097314015 3.64047933 0.69344938 -0.097314015 3.64047933 0.78744942 0.1376228 3.74028516 0.31744939
		 0.1376228 3.74028516 0.50544941 0.1376228 3.74028516 0.4114494 0.097314015 3.64047933 0.31744939
		 0.097314015 3.64047933 0.4114494 0.097314015 3.64047933 0.50544941 0.097314015 3.84009075 0.31744939
		 0.097314015 3.84009075 0.4114494 0.097314015 3.84009075 0.50544941 0.1376228 3.74028516 0.78744942
		 0.1376228 3.74028516 0.5994494 0.097314015 3.64047933 0.5994494 0.1376228 3.74028516 0.69344938
		 0.097314015 3.64047933 0.69344938 0.097314015 3.64047933 0.78744942 0.097314015 3.84009075 0.5994494
		 0.097314015 3.84009075 0.69344938 0.097314015 3.84009075 0.78744942 -8.0491169e-016 3.59913826 1.35144937
		 -7.5460471e-016 3.88143182 1.069449425 -8.0433343e-016 3.59913826 1.069449425 -0.1376228 3.74028516 1.069449425
		 -7.574959e-016 3.88143182 0.8814494 -0.1376228 3.74028516 0.8814494 -0.097314015 3.84009099 0.8814494
		 -7.5807416e-016 3.88143182 0.97544938 -0.1376228 3.74028516 0.97544938 -0.097314015 3.84009099 0.97544938
		 -0.097314015 3.84009099 1.069449425 -8.0433343e-016 3.59913826 0.8814494 -0.097314015 3.64047933 0.8814494
		 -8.0491169e-016 3.59913826 0.97544938 -0.097314015 3.64047933 0.97544938 -0.097314015 3.64047933 1.069449425
		 -0.1376228 3.74028516 1.35144937 -7.5633944e-016 3.88143182 1.16344941 -0.1376228 3.74028516 1.16344941
		 -0.097314015 3.84009099 1.16344941 -7.5836326e-016 3.88143182 1.25744939 -0.1376228 3.74028516 1.25744939
		 -0.097314015 3.84009099 1.25744939 -0.097314015 3.84009099 1.35144937 -8.0317697e-016 3.59913826 1.16344941
		 -0.097314015 3.64047933 1.16344941 -8.0635731e-016 3.59913826 1.25744939 -0.097314015 3.64047933 1.25744939
		 -0.097314015 3.64047933 1.35144937 0.1376228 3.74028516 1.069449425 0.1376228 3.74028516 0.8814494
		 0.097314015 3.64047933 0.8814494 0.1376228 3.74028516 0.97544938 0.097314015 3.64047933 0.97544938
		 0.097314015 3.64047933 1.069449425 0.097314015 3.84009075 0.8814494 0.097314015 3.84009075 0.97544938
		 0.097314015 3.84009075 1.069449425 0.1376228 3.74028516 1.35144937 0.1376228 3.74028516 1.16344941
		 0.097314015 3.64047933 1.16344941 0.1376228 3.74028516 1.25744939 0.097314015 3.64047933 1.25744939
		 0.097314015 3.64047933 1.35144937 0.097314015 3.84009075 1.16344941 0.097314015 3.84009075 1.25744939
		 0.097314015 3.84009075 1.35144937;
	setAttr -s 184 ".ed";
	setAttr ".ed[0:165]"  69 1 1 1 95 0 95 94 1 94 69 1 22 2 1 2 48 1 48 47 1
		 47 22 1 28 4 1 4 30 1 30 29 1 29 28 1 14 5 1 5 17 1 17 16 1 16 14 1 9 8 1 8 13 1
		 13 12 1 12 9 1 11 7 0 7 9 1 12 11 1 0 11 0 12 10 1 10 0 1 13 6 1 6 10 1 15 3 0 3 14 1
		 16 15 1 7 15 0 16 9 1 17 8 1 18 25 1 25 24 1 24 23 1 23 18 1 8 20 1 20 21 1 21 13 1
		 19 6 1 21 19 1 20 23 1 24 21 1 22 19 1 24 22 1 25 2 1 5 26 1 26 27 1 27 17 1 27 20 1
		 26 28 1 29 27 1 29 23 1 30 18 1 6 39 1 39 38 1 38 10 1 33 32 1 32 36 1 36 35 1 35 33 1
		 34 31 0 31 33 1 35 34 1 3 34 0 35 14 1 36 5 1 37 0 0 38 37 1 31 37 0 38 33 1 39 32 1
		 40 45 1 45 44 1 44 43 1 43 40 1 32 41 1 41 42 1 42 36 1 42 26 1 41 43 1 44 42 1 44 28 1
		 45 4 1 19 46 1 46 39 1 46 41 1 47 46 1 47 43 1 48 40 1 49 77 0 77 76 1 76 75 1 75 49 1
		 62 51 1 51 64 1 64 63 1 63 62 1 58 57 1 57 52 1 52 59 1 59 58 1 18 54 1 54 55 1 55 25 1
		 53 2 1 55 53 1 54 57 1 58 55 1 56 53 1 58 56 1 50 56 1 59 50 1 4 60 1 60 61 1 61 30 1
		 61 54 1 60 62 1 63 61 1 63 57 1 64 52 1 65 72 0 72 71 1 71 70 1 70 65 1 52 67 1 67 68 1
		 68 59 1 66 50 1 68 66 1 67 70 1 71 68 1 69 66 1 71 69 1 72 1 0 51 73 1 73 74 1 74 64 1
		 74 67 1 73 75 1 76 74 1 76 70 1 77 65 0 50 86 1 86 85 1 85 56 1 78 83 1 83 82 1 82 81 1
		 81 78 1 40 79 1 79 80 1 80 45 1 80 60 1 79 81 1 82 80 1 82 62 1 83 51 1 53 84 1 84 48 1
		 84 79 1 85 84 1 85 81 1 86 78 1;
	setAttr ".ed[166:183]" 87 92 0 92 91 1 91 90 1 90 87 1 78 88 1 88 89 1 89 83 1
		 89 73 1 88 90 1 91 89 1 91 75 1 92 49 0 66 93 1 93 86 1 93 88 1 94 93 1 94 90 1 95 87 0;
	setAttr -s 88 -ch 352 ".fc[0:87]" -type "polyFaces" 
		f 4 0 1 2 3
		mu 0 4 69 1 95 94
		f 4 4 5 6 7
		mu 0 4 22 2 48 47
		f 4 8 9 10 11
		mu 0 4 28 4 30 29
		f 4 12 13 14 15
		mu 0 4 14 5 17 16
		f 4 16 17 18 19
		mu 0 4 9 8 13 12
		f 4 20 21 -20 22
		mu 0 4 11 7 9 12
		f 4 23 -23 24 25
		mu 0 4 0 11 12 10
		f 4 26 27 -25 -19
		mu 0 4 13 6 10 12
		f 4 28 29 -16 30
		mu 0 4 15 3 14 16
		f 4 31 -31 32 -22
		mu 0 4 7 15 16 9
		f 4 33 -17 -33 -15
		mu 0 4 17 8 9 16
		f 4 34 35 36 37
		mu 0 4 18 25 24 23
		f 4 -18 38 39 40
		mu 0 4 13 8 20 21
		f 4 41 -27 -41 42
		mu 0 4 19 6 13 21
		f 4 -40 43 -37 44
		mu 0 4 21 20 23 24
		f 4 45 -43 -45 46
		mu 0 4 96 19 21 24
		f 4 47 -5 -47 -36
		mu 0 4 25 97 96 24
		f 4 48 49 50 -14
		mu 0 4 5 26 27 17
		f 4 51 -39 -34 -51
		mu 0 4 27 20 8 17
		f 4 52 -12 53 -50
		mu 0 4 26 28 29 27
		f 4 54 -44 -52 -54
		mu 0 4 29 23 20 27
		f 4 55 -38 -55 -11
		mu 0 4 30 18 23 29
		f 4 -28 56 57 58
		mu 0 4 98 99 39 38
		f 4 59 60 61 62
		mu 0 4 33 32 36 35
		f 4 63 64 -63 65
		mu 0 4 34 31 33 35
		f 4 66 -66 67 -30
		mu 0 4 3 34 35 14
		f 4 68 -13 -68 -62
		mu 0 4 36 5 14 35
		f 4 69 -26 -59 70
		mu 0 4 37 100 98 38
		f 4 71 -71 72 -65
		mu 0 4 31 37 38 33
		f 4 73 -60 -73 -58
		mu 0 4 39 32 33 38
		f 4 74 75 76 77
		mu 0 4 40 45 44 43
		f 4 -61 78 79 80
		mu 0 4 36 32 41 42
		f 4 -49 -69 -81 81
		mu 0 4 26 5 36 42
		f 4 -80 82 -77 83
		mu 0 4 42 41 43 44
		f 4 -53 -82 -84 84
		mu 0 4 28 26 42 44
		f 4 85 -9 -85 -76
		mu 0 4 45 4 28 44
		f 4 -42 86 87 -57
		mu 0 4 99 101 46 39
		f 4 88 -79 -74 -88
		mu 0 4 46 41 32 39
		f 4 -46 -8 89 -87
		mu 0 4 101 22 47 46
		f 4 90 -83 -89 -90
		mu 0 4 47 43 41 46
		f 4 91 -78 -91 -7
		mu 0 4 48 40 43 47
		f 4 92 93 94 95
		mu 0 4 49 77 76 75
		f 4 96 97 98 99
		mu 0 4 62 51 64 63
		f 4 100 101 102 103
		mu 0 4 58 57 52 59
		f 4 -35 104 105 106
		mu 0 4 25 18 54 55
		f 4 107 -48 -107 108
		mu 0 4 53 97 25 55
		f 4 -106 109 -101 110
		mu 0 4 55 54 57 58
		f 4 111 -109 -111 112
		mu 0 4 56 53 55 58
		f 4 113 -113 -104 114
		mu 0 4 50 56 58 59
		f 4 -10 115 116 117
		mu 0 4 30 4 60 61
		f 4 -56 -118 118 -105
		mu 0 4 18 30 61 54
		f 4 119 -100 120 -117
		mu 0 4 60 62 63 61
		f 4 121 -110 -119 -121
		mu 0 4 63 57 54 61
		f 4 122 -102 -122 -99
		mu 0 4 64 52 57 63
		f 4 123 124 125 126
		mu 0 4 65 72 71 70
		f 4 -103 127 128 129
		mu 0 4 59 52 67 68
		f 4 130 -115 -130 131
		mu 0 4 66 50 59 68
		f 4 -129 132 -126 133
		mu 0 4 68 67 70 71
		f 4 134 -132 -134 135
		mu 0 4 102 66 68 71
		f 4 136 -1 -136 -125
		mu 0 4 72 103 102 71
		f 4 -98 137 138 139
		mu 0 4 64 51 73 74
		f 4 -128 -123 -140 140
		mu 0 4 67 52 64 74
		f 4 -139 141 -95 142
		mu 0 4 74 73 75 76
		f 4 -133 -141 -143 143
		mu 0 4 70 67 74 76
		f 4 144 -127 -144 -94
		mu 0 4 77 65 70 76
		f 4 -114 145 146 147
		mu 0 4 104 105 86 85
		f 4 148 149 150 151
		mu 0 4 78 83 82 81
		f 4 -75 152 153 154
		mu 0 4 45 40 79 80
		f 4 -116 -86 -155 155
		mu 0 4 60 4 45 80
		f 4 -154 156 -151 157
		mu 0 4 80 79 81 82
		f 4 -120 -156 -158 158
		mu 0 4 62 60 80 82
		f 4 159 -97 -159 -150
		mu 0 4 83 51 62 82
		f 4 -108 160 161 -6
		mu 0 4 2 106 84 48
		f 4 162 -153 -92 -162
		mu 0 4 84 79 40 48
		f 4 -112 -148 163 -161
		mu 0 4 106 104 85 84
		f 4 164 -157 -163 -164
		mu 0 4 85 81 79 84
		f 4 165 -152 -165 -147
		mu 0 4 86 78 81 85
		f 4 166 167 168 169
		mu 0 4 87 92 91 90
		f 4 -149 170 171 172
		mu 0 4 83 78 88 89
		f 4 -138 -160 -173 173
		mu 0 4 73 51 83 89
		f 4 -172 174 -169 175
		mu 0 4 89 88 90 91
		f 4 -142 -174 -176 176
		mu 0 4 75 73 89 91
		f 4 177 -96 -177 -168
		mu 0 4 92 49 75 91
		f 4 -131 178 179 -146
		mu 0 4 105 107 93 86
		f 4 180 -171 -166 -180
		mu 0 4 93 88 78 86
		f 4 -135 -4 181 -179
		mu 0 4 107 69 94 93
		f 4 182 -175 -181 -182
		mu 0 4 94 90 88 93
		f 4 183 -170 -183 -3
		mu 0 4 95 87 90 94;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".vnm" 0;
createNode nurbsCurve -n "curveShape1" -p "GRP_TONGUE_TEMPLATE";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.36141389314307837 3.7402844379854301 1.8322611185027022
		0.36141389314307704 3.7402844379854301 1.8322611185027022
		0.36141389314307704 3.7402844379854301 0.15862088350711409
		-0.36141389314307837 3.7402844379854301 0.15862088350711409
		-0.36141389314307837 3.7402844379854301 1.8322611185027022
		;
createNode objectSet -n "tongue_influence";
	setAttr ".ihi" 0;
	setAttr -s 12 ".dsm";
	setAttr ".an" -type "string" "gCharacterSet";
createNode unitConversion -n "unitConversion606";
	setAttr ".cf" 0.017453292519943295;
createNode expression -n "tongueRig_driven_ex";
	setAttr -k on ".nds";
	setAttr -s 11 ".in";
	setAttr -s 11 ".in";
	setAttr -s 3 ".out";
	setAttr ".ixp" -type "string" ".O[0]=(linstep(0,1,.I[0])*-.I[1] \n+linstep(0,1,.I[2])*.I[3])\n*.I[4];\n\n.O[1]=(linstep(0,1,.I[5])*.I[6]\n+linstep(0,1,.I[7])*-.I[8])\n*.I[4];\n\n.O[2]=.I[9]*.I[10]\n*.I[4];";
createNode unitConversion -n "unitConversion607";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion608";
	setAttr ".cf" 0.017453292519943295;
createNode expression -n "tongue_translate_ex";
	setAttr -k on ".nds";
	setAttr -s 3 ".in";
	setAttr -s 3 ".in";
	setAttr -s 13 ".out";
	setAttr ".ixp" -type "string" "//tongue_translate_ex\n.O[0]=.I[0];\n.O[1]=.I[1];\n\nfloat $orgJointDis=0.094;\nfloat $tongueStretchScale=0.08;\n.O[2]=$orgJointDis+(.I[2]*$tongueStretchScale);\n.O[3]=$orgJointDis+(.I[2]*$tongueStretchScale);\n.O[4]=$orgJointDis+(.I[2]*$tongueStretchScale);\n.O[5]=$orgJointDis+(.I[2]*$tongueStretchScale);\n.O[6]=$orgJointDis+(.I[2]*$tongueStretchScale);\n.O[7]=$orgJointDis+(.I[2]*$tongueStretchScale);\n.O[8]=$orgJointDis+(.I[2]*$tongueStretchScale);\n.O[9]=$orgJointDis+(.I[2]*$tongueStretchScale);\n.O[10]=$orgJointDis+(.I[2]*$tongueStretchScale);\n.O[11]=$orgJointDis+(.I[2]*$tongueStretchScale);\n.O[12]=$orgJointDis+(.I[2]*$tongueStretchScale);";
createNode unitConversion -n "unitConversion571";
	setAttr ".cf" 0.017453292519943295;
createNode expression -n "tongue_rotate_ex";
	setAttr -k on ".nds";
	setAttr -s 5 ".in";
	setAttr -s 5 ".in";
	setAttr -s 33 ".out";
	setAttr ".ixp" -type "string" (
		"//tongue_rotate_ex\n.O[0]=.I[0]*.I[1]*clamp(0,1,(.I[2]-11));\n.O[1]=.I[0]*.I[1]*clamp(0,1,(.I[2]-10));\n.O[2]=.I[0]*.I[1]*clamp(0,1,(.I[2]-9));\n.O[3]=.I[0]*.I[1]*clamp(0,1,(.I[2]-8));\n.O[4]=.I[0]*.I[1]*clamp(0,1,(.I[2]-7));\n.O[5]=.I[0]*.I[1]*clamp(0,1,(.I[2]-6));\n.O[6]=.I[0]*.I[1]*clamp(0,1,(.I[2]-5));\n.O[7]=.I[0]*.I[1]*clamp(0,1,(.I[2]-4));\n.O[8]=.I[0]*.I[1]*clamp(0,1,(.I[2]-3));\n.O[9]=.I[0]*.I[1]*clamp(0,1,(.I[2]-2));\n.O[10]=.I[0]*.I[1]*clamp(0,1,(.I[2]-1));\n\n.O[11]=.I[3]*.I[1]*clamp(0,1,(.I[2]-11));\n.O[12]=.I[3]*.I[1]*clamp(0,1,(.I[2]-10));\n.O[13]=.I[3]*.I[1]*clamp(0,1,(.I[2]-9));\n.O[14]=.I[3]*.I[1]*clamp(0,1,(.I[2]-8));\n.O[15]=.I[3]*.I[1]*clamp(0,1,(.I[2]-7));\n.O[16]=.I[3]*.I[1]*clamp(0,1,(.I[2]-6));\n.O[17]=.I[3]*.I[1]*clamp(0,1,(.I[2]-5));\n.O[18]=.I[3]*.I[1]*clamp(0,1,(.I[2]-4));\n.O[19]=.I[3]*.I[1]*clamp(0,1,(.I[2]-3));\n.O[20]=.I[3]*.I[1]*clamp(0,1,(.I[2]-2));\n.O[21]=.I[3]*.I[1]*clamp(0,1,(.I[2]-1));\n\n.O[22]=.I[4]*.I[1]*clamp(0,1,(.I[2]-11));\n.O[23]=.I[4]*.I[1]*clamp(0,1,(.I[2]-10));\n.O[24]=.I[4]*.I[1]*clamp(0,1,(.I[2]-9));\n"
		+ ".O[25]=.I[4]*.I[1]*clamp(0,1,(.I[2]-8));\n.O[26]=.I[4]*.I[1]*clamp(0,1,(.I[2]-7));\n.O[27]=.I[4]*.I[1]*clamp(0,1,(.I[2]-6));\n.O[28]=.I[4]*.I[1]*clamp(0,1,(.I[2]-5));\n.O[29]=.I[4]*.I[1]*clamp(0,1,(.I[2]-4));\n.O[30]=.I[4]*.I[1]*clamp(0,1,(.I[2]-3));\n.O[31]=.I[4]*.I[1]*clamp(0,1,(.I[2]-2));\n.O[32]=.I[4]*.I[1]*clamp(0,1,(.I[2]-1));");
createNode unitConversion -n "unitConversion570";
	setAttr ".cf" 57.295779513082323;
createNode unitConversion -n "unitConversion582";
	setAttr ".cf" 57.295779513082323;
createNode unitConversion -n "unitConversion594";
	setAttr ".cf" 57.295779513082323;
createNode unitConversion -n "unitConversion583";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion595";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion572";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion584";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion596";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion573";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion585";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion597";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion574";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion586";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion598";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion575";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion587";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion599";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion576";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion588";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion600";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion577";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion589";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion601";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion578";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion590";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion602";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion579";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion591";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion603";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion580";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion592";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion604";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion581";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion593";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion605";
	setAttr ".cf" 0.017453292519943295;
createNode nurbsTessellate -n "nurbsTessellate1";
	setAttr ".f" 2;
	setAttr ".pt" 1;
	setAttr ".chr" 0.9;
	setAttr ".un" 1;
	setAttr ".vn" 1;
	setAttr ".ucr" no;
	setAttr ".cht" 0.01;
createNode loft -n "loft1";
	setAttr -s 12 ".ic";
	setAttr ".u" yes;
	setAttr ".rsn" yes;
createNode groupId -n "blendShape1GroupId";
	setAttr ".ihi" 0;
createNode objectSet -n "blendShape1Set";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode blendShape -n "blendShape1";
	addAttr -ci true -h true -sn "aal" -ln "attributeAliasList" -dt "attributeAlias";
	setAttr ".tc" no;
	setAttr ".w[0]"  1;
	setAttr ".aal" -type "attributeAlias" {"tongue_boundMesh","weight[0]"} ;
createNode groupParts -n "blendShape1GroupParts";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "vtx[*]";
createNode tweak -n "tweak1";
createNode objectSet -n "tweakSet1";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId634";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts2";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "vtx[*]";
createNode groupId -n "skinCluster1GroupId";
	setAttr ".ihi" 0;
createNode objectSet -n "skinCluster1Set";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode skinCluster -n "skinCluster1";
	setAttr -s 96 ".wl";
	setAttr -s 3 ".wl[0].w[0:2]"  0.62117245334065829 0.29810729488432047 
		0.080720251775021276;
	setAttr -s 3 ".wl[1].w[9:11]"  0.06100892691528341 0.46949553654235826 
		0.46949553654235826;
	setAttr -s 3 ".wl[2].w[4:6]"  0.24487112829593605 0.51025294294977785 
		0.24487592875428607;
	setAttr -s 3 ".wl[3].w[0:2]"  0.62117548349128082 0.29810562929783113 
		0.080718887210888088;
	setAttr -s 3 ".wl[4].w[4:6]"  0.24486982065132798 0.51025555820799195 
		0.24487462114068009;
	setAttr -s 3 ".wl[5].w[1:3]"  0.24486983744415389 0.51025555820830215 
		0.24487460434754396;
	setAttr -s 3 ".wl[6].w[1:3]"  0.24487114508865016 0.51025294295009038 
		0.24487591196125952;
	setAttr -s 3 ".wl[7].w[0:2]"  0.63023602285951119 0.29304109611307355 
		0.076722881027415257;
	setAttr -s 3 ".wl[8].w[1:3]"  0.24092104942641968 0.51815304526605788 
		0.24092590530752248;
	setAttr -s 3 ".wl[9].w[0:2]"  0.24092108752674421 0.5181530452667944 
		0.24092586720646136;
	setAttr -s 3 ".wl[10].w[0:2]"  0.24487118249061454 0.51025294295077273 
		0.24487587455861279;
	setAttr -s 3 ".wl[11].w[0:2]"  0.62563033313309624 0.2956364192586195 
		0.078733247608284304;
	setAttr -s 3 ".wl[12].w[0:2]"  0.24293804693680265 0.51411917020618902 
		0.24294278285700838;
	setAttr -s 3 ".wl[13].w[1:3]"  0.24293800918528793 0.51411917020548081 
		0.24294282060923117;
	setAttr -s 3 ".wl[14].w[0:2]"  0.24486987484635656 0.51025555820899082 
		0.24487456694465254;
	setAttr -s 3 ".wl[15].w[0:2]"  0.6256329845956734 0.29563493749744552 
		0.078732077906881082;
	setAttr -s 3 ".wl[16].w[0:2]"  0.24293689156198359 0.51412148093018317 
		0.24294162750783324;
	setAttr -s 3 ".wl[17].w[1:3]"  0.2429368538102667 0.51412148092947052 
		0.24294166526026267;
	setAttr -s 3 ".wl[18].w[4:6]"  0.24092103232015386 0.51815304526572348 
		0.24092592241412264;
	setAttr -s 3 ".wl[19].w[2:4]"  0.2448712030998618 0.51025294295114842 
		0.24487585394898981;
	setAttr -s 3 ".wl[20].w[2:4]"  0.24092110852080326 0.51815304526719574 
		0.240925846212001;
	setAttr -s 3 ".wl[21].w[2:4]"  0.24293806773865934 0.51411917020657794 
		0.24294276205476273;
	setAttr -s 3 ".wl[22].w[3:5]"  0.24487126111108623 0.51025294295218282 
		0.24487579593673089;
	setAttr -s 3 ".wl[23].w[3:5]"  0.24092116761520219 0.51815304526830697 
		0.24092578711649082;
	setAttr -s 3 ".wl[24].w[3:5]"  0.24293812629204461 0.51411917020764963 
		0.24294270350030581;
	setAttr -s 3 ".wl[25].w[4:6]"  0.24293799223563214 0.51411917020515774 
		0.24294283755921009;
	setAttr -s 3 ".wl[26].w[2:4]"  0.24486989545573704 0.5102555582093623 
		0.24487454633490077;
	setAttr -s 3 ".wl[27].w[2:4]"  0.24293691236395304 0.5141214809305692 
		0.24294160670547785;
	setAttr -s 3 ".wl[28].w[3:5]"  0.24486995346733603 0.51025555821039681 
		0.24487448832226713;
	setAttr -s 3 ".wl[29].w[3:5]"  0.24293697091765531 0.5141214809316409 
		0.24294154815070382;
	setAttr -s 3 ".wl[30].w[4:6]"  0.24293683686051701 0.51412148092914867 
		0.24294168221033421;
	setAttr -s 3 ".wl[31].w[0:2]"  0.63023602285950708 0.29304109611307594 
		0.07672288102741702;
	setAttr -s 3 ".wl[32].w[1:3]"  0.24092104942642156 0.51815304526605432 
		0.24092590530752422;
	setAttr -s 3 ".wl[33].w[0:2]"  0.24092108752674599 0.51815304526679096 
		0.24092586720646314;
	setAttr -s 3 ".wl[34].w[0:2]"  0.62563298459567052 0.29563493749744718 
		0.078732077906882331;
	setAttr -s 3 ".wl[35].w[0:2]"  0.24293689156198475 0.51412148093018095 
		0.24294162750783435;
	setAttr -s 3 ".wl[36].w[1:3]"  0.24293685381026808 0.51412148092946808 
		0.24294166526026384;
	setAttr -s 3 ".wl[37].w[0:2]"  0.62563077202603679 0.29563617398572695 
		0.078733053988236198;
	setAttr -s 3 ".wl[38].w[0:2]"  0.24293785568966214 0.51411955269622456 
		0.2429425916141133;
	setAttr -s 3 ".wl[39].w[1:3]"  0.24293781793811364 0.51411955269551657 
		0.24294262936636984;
	setAttr -s 3 ".wl[40].w[4:6]"  0.24092103232015563 0.51815304526571981 
		0.24092592241412458;
	setAttr -s 3 ".wl[41].w[2:4]"  0.24092110852080501 0.5181530452671923 
		0.24092584621200278;
	setAttr -s 3 ".wl[42].w[2:4]"  0.24293691236395423 0.51412148093056653 
		0.24294160670547926;
	setAttr -s 3 ".wl[43].w[3:5]"  0.24092116761520388 0.51815304526830352 
		0.24092578711649257;
	setAttr -s 3 ".wl[44].w[3:5]"  0.24293697091765654 0.51412148093163845 
		0.24294154815070496;
	setAttr -s 3 ".wl[45].w[4:6]"  0.24293683686051831 0.51412148092914622 
		0.24294168221033535;
	setAttr -s 3 ".wl[46].w[2:4]"  0.24293787649153764 0.51411955269661336 
		0.24294257081184903;
	setAttr -s 3 ".wl[47].w[3:5]"  0.24293793504497516 0.51411955269768528 
		0.24294251225733957;
	setAttr -s 3 ".wl[48].w[4:6]"  0.24293780098844286 0.51411955269519316 
		0.24294264631636397;
	setAttr -s 3 ".wl[49].w[9:11]"  0.061007679035462878 0.46949616048226855 
		0.46949616048226855;
	setAttr -s 3 ".wl[50].w[7:9]"  0.24487111150322041 0.51025294294946877 
		0.24487594554731079;
	setAttr -s 3 ".wl[51].w[7:9]"  0.24486980385850768 0.51025555820767521 
		0.24487463793381714;
	setAttr -s 3 ".wl[52].w[7:9]"  0.24092101521389017 0.51815304526538708 
		0.24092593952072267;
	setAttr -s 3 ".wl[53].w[5:7]"  0.24487118630714277 0.51025294295083889 
		0.24487587074201836;
	setAttr -s 3 ".wl[54].w[5:7]"  0.24092109141453605 0.5181530452668679 
		0.24092586331859608;
	setAttr -s 3 ".wl[55].w[5:7]"  0.24293805078899969 0.51411917020625852 
		0.24294277900474176;
	setAttr -s 3 ".wl[56].w[6:8]"  0.24487124431835475 0.51025294295189472 
		0.24487581272975059;
	setAttr -s 3 ".wl[57].w[6:8]"  0.24092115050892846 0.51815304526798844 
		0.24092580422308299;
	setAttr -s 3 ".wl[58].w[6:8]"  0.24293810934237414 0.51411917020734843 
		0.24294272045027737;
	setAttr -s 3 ".wl[59].w[7:9]"  0.24293797528597619 0.51411917020483622 
		0.24294285450918768;
	setAttr -s 3 ".wl[60].w[5:7]"  0.24486987866291357 0.51025555820906154 
		0.24487456312802489;
	setAttr -s 3 ".wl[61].w[5:7]"  0.2429368954142046 0.51412148093025589 
		0.24294162365553956;
	setAttr -s 3 ".wl[62].w[6:8]"  0.24486993667451276 0.51025555821009239 
		0.24487450511539485;
	setAttr -s 3 ".wl[63].w[6:8]"  0.24293695396790507 0.51412148093132792 
		0.24294156510076709;
	setAttr -s 3 ".wl[64].w[7:9]"  0.24293681991077198 0.51412148092882171 
		0.24294169916040634;
	setAttr -s 3 ".wl[65].w[9:11]"  0.057374923556754838 0.47131253822162256 
		0.47131253822162256;
	setAttr -s 3 ".wl[66].w[8:10]"  0.2448711695144247 0.51025294295054124 
		0.24487588753503414;
	setAttr -s 3 ".wl[67].w[8:10]"  0.2409210743082677 0.51815304526653916 
		0.2409258804251932;
	setAttr -s 3 ".wl[68].w[8:10]"  0.24293803383934051 0.51411917020594733 
		0.24294279595471208;
	setAttr -s 3 ".wl[69].w[9:11]"  0.24487122751916104 0.51025294296454804 
		0.24487582951629089;
	setAttr -s 3 ".wl[70].w[9:11]"  0.2409211333958477 0.51815304528128436 
		0.24092582132286805;
	setAttr -s 3 ".wl[71].w[9:11]"  0.242938092386076 0.51411917022031484 
		0.24294273739360916;
	setAttr -s 3 ".wl[72].w[9:11]"  0.059197114401373062 0.47040144279931345 
		0.47040144279931345;
	setAttr -s 3 ".wl[73].w[8:10]"  0.2448698618700868 0.51025555820874746 
		0.24487457992116574;
	setAttr -s 3 ".wl[74].w[8:10]"  0.2429368784644535 0.51412148092993282 
		0.24294164060561371;
	setAttr -s 3 ".wl[75].w[9:11]"  0.24486991987519763 0.51025555822275448 
		0.24487452190204775;
	setAttr -s 3 ".wl[76].w[9:11]"  0.2429369370115059 0.51412148094430066 
		0.24294158204419347;
	setAttr -s 3 ".wl[77].w[9:11]"  0.059196050968186316 0.47040197451590687 
		0.47040197451590687;
	setAttr -s 3 ".wl[78].w[7:9]"  0.24092101521389206 0.51815304526538364 
		0.24092593952072439;
	setAttr -s 3 ".wl[79].w[5:7]"  0.24092109141453771 0.51815304526686434 
		0.24092586331859794;
	setAttr -s 3 ".wl[80].w[5:7]"  0.24293689541420574 0.51412148093025334 
		0.24294162365554087;
	setAttr -s 3 ".wl[81].w[6:8]"  0.24092115050893012 0.51815304526798511 
		0.24092580422308468;
	setAttr -s 3 ".wl[82].w[6:8]"  0.24293695396790643 0.51412148093132526 
		0.24294156510076828;
	setAttr -s 3 ".wl[83].w[7:9]"  0.24293681991077318 0.51412148092881926 
		0.24294169916040764;
	setAttr -s 3 ".wl[84].w[5:7]"  0.24293785954186281 0.51411955269629395 
		0.2429425877618433;
	setAttr -s 3 ".wl[85].w[6:8]"  0.2429379180952897 0.51411955269738407 
		0.24294252920732629;
	setAttr -s 3 ".wl[86].w[7:9]"  0.24293778403877136 0.51411955269487197 
		0.24294266326635677;
	setAttr -s 3 ".wl[87].w[9:11]"  0.057374923556756441 0.47131253822162178 
		0.47131253822162178;
	setAttr -s 3 ".wl[88].w[8:10]"  0.24092107430826942 0.51815304526653572 
		0.24092588042519489;
	setAttr -s 3 ".wl[89].w[8:10]"  0.24293687846445458 0.51412148092993049 
		0.24294164060561493;
	setAttr -s 3 ".wl[90].w[9:11]"  0.24092113339584958 0.51815304528128048 
		0.24092582132286994;
	setAttr -s 3 ".wl[91].w[9:11]"  0.24293693701150704 0.51412148094429833 
		0.24294158204419461;
	setAttr -s 3 ".wl[92].w[9:11]"  0.059196050968187433 0.47040197451590626 
		0.47040197451590626;
	setAttr -s 3 ".wl[93].w[8:10]"  0.24293784259218842 0.51411955269598286 
		0.24294260471182871;
	setAttr -s 3 ".wl[94].w[9:11]"  0.24293790113897623 0.51411955271035048 
		0.24294254615067332;
	setAttr -s 3 ".wl[95].w[9:11]"  0.059196938371588508 0.47040153081420577 
		0.47040153081420577;
	setAttr -s 12 ".pm";
	setAttr ".gm" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr -s 12 ".ma";
	setAttr -s 12 ".dpf[0:11]"  4 4 4 4 4 4 4 4 4 4 4 4;
	setAttr -s 12 ".lw";
	setAttr -s 12 ".lw";
	setAttr ".mmi" yes;
	setAttr ".mi" 3;
	setAttr ".ucm" yes;
createNode dagPose -n "bindPose45";
	setAttr -s 38 ".wm";
	setAttr ".wm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".wm[1]" -type "matrix" 1.0000000000000004 0 0 0 0 1 0 0 0 0 1.0000000000000004 0
		 -1.6536647781012667e-016 0 6.6613381477509392e-016 1;
	setAttr ".wm[2]" -type "matrix" 1.0000000000000004 0 0 0 0 1 0 0 0 0 1.0000000000000004 0
		 -7.7124598275076103e-016 0 6.6613381477509392e-016 1;
	setAttr ".wm[3]" -type "matrix" 1.0000000000000004 0 0 0 0 1 0 0 0 0 1.0000000000000004 0
		 -1.6536647781012667e-016 0 6.6613381477509392e-016 1;
	setAttr ".wm[4]" -type "matrix" 1.0000000000000004 0 0 0 0 1 0 0 0 0 1.0000000000000004 0
		 -7.7124598275076113e-016 3.7402844379854288 0.31744866979326941 1;
	setAttr ".wm[6]" -type "matrix" 1.0000000000000004 0 0 0 0 1 0 0 0 0 1.0000000000000004 0
		 -7.7124598275076113e-016 3.7402844379854288 0.31744866979326941 1;
	setAttr ".wm[7]" -type "matrix" 1.0000000000000004 0 0 0 0 1 0 0 0 0 1.0000000000000004 0
		 -7.7124598275076113e-016 3.7402844379854292 0.41144866979326944 1;
	setAttr ".wm[9]" -type "matrix" 1.0000000000000004 0 0 0 0 1 0 0 0 0 1.0000000000000004 0
		 -7.7124598275076113e-016 3.7402844379854292 0.41144866979326944 1;
	setAttr ".wm[10]" -type "matrix" 1.0000000000000004 0 0 0 0 1 0 0 0 0 1.0000000000000004 0
		 -7.7124598275076113e-016 3.7402844379854296 0.50544866979326952 1;
	setAttr ".wm[12]" -type "matrix" 1.0000000000000004 0 0 0 0 1 0 0 0 0 1.0000000000000004 0
		 -7.7124598275076113e-016 3.7402844379854296 0.50544866979326952 1;
	setAttr ".wm[13]" -type "matrix" 1.0000000000000004 0 0 0 0 1 0 0 0 0 1.0000000000000004 0
		 -7.7124598275076113e-016 3.7402844379854296 0.59944866979326961 1;
	setAttr ".wm[15]" -type "matrix" 1.0000000000000004 0 0 0 0 1 0 0 0 0 1.0000000000000004 0
		 -7.7124598275076113e-016 3.7402844379854296 0.59944866979326961 1;
	setAttr ".wm[16]" -type "matrix" 1.0000000000000004 0 0 0 0 1 0 0 0 0 1.0000000000000004 0
		 -7.7124598275076113e-016 3.7402844379854296 0.69344866979326969 1;
	setAttr ".wm[18]" -type "matrix" 1.0000000000000004 0 0 0 0 1 0 0 0 0 1.0000000000000004 0
		 -7.7124598275076113e-016 3.7402844379854296 0.69344866979326969 1;
	setAttr ".wm[19]" -type "matrix" 1.0000000000000004 0 0 0 0 1 0 0 0 0 1.0000000000000004 0
		 -7.7124598275076113e-016 3.7402844379854301 0.78744866979326977 1;
	setAttr ".wm[21]" -type "matrix" 1.0000000000000004 0 0 0 0 1 0 0 0 0 1.0000000000000004 0
		 -7.7124598275076113e-016 3.7402844379854301 0.78744866979327066 1;
	setAttr ".wm[22]" -type "matrix" 1.0000000000000004 0 0 0 0 1 0 0 0 0 1.0000000000000004 0
		 -7.7124598275076113e-016 3.7402844379854301 0.88144866979327074 1;
	setAttr ".wm[24]" -type "matrix" 1.0000000000000004 0 0 0 0 1 0 0 0 0 1.0000000000000004 0
		 -7.7124598275076113e-016 3.7402844379854301 0.88144866979326986 1;
	setAttr ".wm[25]" -type "matrix" 1.0000000000000004 0 0 0 0 1 0 0 0 0 1.0000000000000004 0
		 -7.7124598275076113e-016 3.740284437985431 0.97544866979326994 1;
	setAttr ".wm[27]" -type "matrix" 1.0000000000000004 0 0 0 0 1 0 0 0 0 1.0000000000000004 0
		 -7.7124598275076113e-016 3.740284437985431 0.97544866979326994 1;
	setAttr ".wm[28]" -type "matrix" 1.0000000000000004 0 0 0 0 1 0 0 0 0 1.0000000000000004 0
		 -7.7124598275076113e-016 3.740284437985431 1.0694486697932699 1;
	setAttr ".wm[30]" -type "matrix" 1.0000000000000004 0 0 0 0 1 0 0 0 0 1.0000000000000004 0
		 -7.7124598275076113e-016 3.740284437985431 1.0694486697932708 1;
	setAttr ".wm[31]" -type "matrix" 1.0000000000000004 0 0 0 0 1 0 0 0 0 1.0000000000000004 0
		 -7.7124598275076113e-016 3.740284437985431 1.1634486697932709 1;
	setAttr ".wm[33]" -type "matrix" 1.0000000000000004 0 0 0 0 1 0 0 0 0 1.0000000000000004 0
		 -7.7124598275076113e-016 3.740284437985431 1.1634486697932709 1;
	setAttr ".wm[34]" -type "matrix" 1.0000000000000004 0 0 0 0 1 0 0 0 0 1.0000000000000004 0
		 -7.7124598275076113e-016 3.7402844379854314 1.257448669793271 1;
	setAttr ".wm[36]" -type "matrix" 1.0000000000000004 0 0 0 0 1 0 0 0 0 1.0000000000000004 0
		 -7.7124598275076113e-016 3.7402844379854314 1.3514486697932702 1;
	setAttr -s 38 ".xm";
	setAttr ".xm[0]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 -7.7124598275075846e-016
		 3.7402844379854288 0.31744866979326941 0 0 0 -7.7124598275075846e-016 3.7402844379854288
		 0.31744866979326941 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[1]" -type "matrix" "xform" 1.0000000000000004 1 1.0000000000000004 -1.9081958235744858e-016
		 3.2872847024232254e-016 -1.132450295465395e-016 0 -1.653664778101241e-016 0
		 6.6613381477509392e-016 0 0 0 -6.0587950494063426e-016 3.7402844379854288 0.31744866979326858 -2.8103169748498546e-030
		 0 1.6653345369377454e-016 -6.0587950494063702e-016 3.7402844379854288 0.31744866979326875 0
		 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[2]" -type "matrix" "xform" 1 1 1 0 0 0 0 -6.0587950494063406e-016
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[3]" -type "matrix" "xform" 1 1 1 0 0 0 0 6.0587950494063406e-016
		 0 0 0 0 0 -6.0587950494063416e-016 3.7402844379854288 0.31744866979326858 0 0 0 -6.0587950494063416e-016
		 3.7402844379854288 0.31744866979326858 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[4]" -type "matrix" "xform" 1 1 1 0 0 0 0 -6.0587950494063416e-016
		 3.7402844379854288 0.31744866979326858 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1
		 1 1 yes;
	setAttr ".xm[5]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[6]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 8.8817841970012523e-016
		 0.094000000000000083 0 0 0 0 8.8817841970012523e-016 0.094000000000000083 0 0 0 
		0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[7]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 4.4408920985006262e-016
		 0.094 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[8]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[9]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 8.8817841970012523e-016
		 0.094000000000000083 0 0 0 0 8.8817841970012523e-016 0.094000000000000083 0 0 0 
		0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[10]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 4.4408920985006262e-016
		 0.094 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[11]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[12]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0.093999999999999861 0
		 0 0 0 0 0.093999999999999861 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[13]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0.094 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[14]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[15]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0.094000000000000083 0
		 0 0 0 0 0.094000000000000083 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[16]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0.094 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[17]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[18]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 4.4408920985006262e-016
		 0.094000000000000861 0 0 0 0 4.4408920985006262e-016 0.094000000000000861 0 0 0 
		0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[19]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 4.4408920985006262e-016
		 0.094 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[20]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 8.8817841970012523e-016 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[21]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 4.4408920985006262e-016
		 0.093999999999999195 0 0 0 0 4.4408920985006262e-016 0.093999999999999195 0 0 0 
		0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[22]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0.094 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[23]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 -8.8817841970012523e-016 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[24]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 1.3322676295501878e-015
		 0.093999999999999861 0 0 0 0 1.3322676295501878e-015 0.093999999999999861 0 0 0 
		0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[25]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 8.8817841970012523e-016
		 0.094 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[26]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[27]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0.094000000000000861 0
		 0 0 0 0 0.094000000000000861 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[28]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0.094 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[29]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 8.8817841970012523e-016 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[30]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0.094000000000000195 0
		 0 0 0 0 0.094000000000000195 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[31]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0.094 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[32]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[33]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 1.3322676295501878e-015
		 0.093999999999999195 0 0 0 0 1.3322676295501878e-015 0.093999999999999195 0 0 0 
		0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[34]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 4.4408920985006262e-016
		 0.094 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[35]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 -8.8817841970012523e-016 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[36]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0.094 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[37]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr -s 38 ".m";
	setAttr -s 38 ".p";
	setAttr -s 38 ".g[0:37]" yes yes yes yes yes no yes yes no yes yes 
		no yes yes no yes yes no yes yes no yes yes no yes yes no yes yes no yes yes no yes 
		yes no yes no;
	setAttr ".bp" yes;
createNode groupParts -n "skinCluster1GroupParts";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "vtx[*]";
select -ne :time1;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".o" 22;
	setAttr -av ".unw" 22;
	setAttr -k on ".etw";
	setAttr -k on ".tps";
	setAttr -k on ".tms";
lockNode -l 1 ;
select -ne :renderPartition;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 3 ".st";
	setAttr -cb on ".an";
	setAttr -cb on ".pt";
lockNode -l 1 ;
select -ne :initialShadingGroup;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".dsm";
	setAttr -k on ".mwc";
	setAttr -cb on ".an";
	setAttr -cb on ".il";
	setAttr -cb on ".vo";
	setAttr -cb on ".eo";
	setAttr -cb on ".fo";
	setAttr -cb on ".epo";
	setAttr -k on ".ro" yes;
	setAttr -s 20 ".gn";
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
	setAttr -s 3 ".s";
lockNode -l 1 ;
select -ne :defaultTextureList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
select -ne :postProcessList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".p";
lockNode -l 1 ;
select -ne :defaultRenderUtilityList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".u";
select -ne :defaultRenderingList1;
select -ne :renderGlobalsList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
lockNode -l 1 ;
select -ne :defaultRenderGlobals;
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
	setAttr -cb on ".ren" -type "string" "mentalRay";
	setAttr -av -k on ".esr";
	setAttr -k on ".ors";
	setAttr -cb on ".sdf";
	setAttr -av -k on ".outf";
	setAttr -cb on ".imfkey";
	setAttr -k on ".gama";
	setAttr -k on ".an" yes;
	setAttr -cb on ".ar";
	setAttr -k on ".fs";
	setAttr -k on ".ef";
	setAttr -av -k on ".bfs";
	setAttr -cb on ".me";
	setAttr -cb on ".se";
	setAttr -av -k on ".be";
	setAttr -cb on ".ep";
	setAttr -k on ".fec";
	setAttr -av -k on ".ofc";
	setAttr -cb on ".ofe";
	setAttr -cb on ".efe";
	setAttr -k on ".oft";
	setAttr -cb on ".umfn";
	setAttr -cb on ".ufe";
	setAttr -k on ".pff" yes;
	setAttr -cb on ".peie";
	setAttr -k on ".ifp" -type "string" "<Layer>/<Scene>_<Layer>";
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
	setAttr -cb on ".prm";
	setAttr -cb on ".pom";
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
connectAttr "unitConversion606.o" "GRP_tongueRig.rx";
connectAttr "unitConversion607.o" "GRP_tongueRig.ry";
connectAttr "unitConversion608.o" "GRP_tongueRig.rz";
connectAttr "tongue_translate_ex.out[0]" "GRP_tongue_move.tx";
connectAttr "tongue_translate_ex.out[1]" "GRP_tongue_move.ty";
connectAttr "tongue_translate_ex.out[2]" "c_GRP_tongue_joint2.tz";
connectAttr "unitConversion571.o" "c_GRP_tongue_joint2.rx";
connectAttr "unitConversion583.o" "c_GRP_tongue_joint2.ry";
connectAttr "unitConversion595.o" "c_GRP_tongue_joint2.rz";
connectAttr "c_tongue_joint1.s" "c_tongue_joint2.is";
connectAttr "tongue_translate_ex.out[3]" "c_GRP_tongue_joint3.tz";
connectAttr "unitConversion572.o" "c_GRP_tongue_joint3.rx";
connectAttr "unitConversion584.o" "c_GRP_tongue_joint3.ry";
connectAttr "unitConversion596.o" "c_GRP_tongue_joint3.rz";
connectAttr "c_tongue_joint2.s" "c_tongue_joint3.is";
connectAttr "tongue_translate_ex.out[4]" "c_GRP_tongue_joint4.tz";
connectAttr "unitConversion573.o" "c_GRP_tongue_joint4.rx";
connectAttr "unitConversion585.o" "c_GRP_tongue_joint4.ry";
connectAttr "unitConversion597.o" "c_GRP_tongue_joint4.rz";
connectAttr "c_tongue_joint3.s" "c_tongue_joint4.is";
connectAttr "tongue_translate_ex.out[5]" "c_GRP_tongue_joint5.tz";
connectAttr "unitConversion574.o" "c_GRP_tongue_joint5.rx";
connectAttr "unitConversion586.o" "c_GRP_tongue_joint5.ry";
connectAttr "unitConversion598.o" "c_GRP_tongue_joint5.rz";
connectAttr "c_tongue_joint4.s" "c_tongue_joint5.is";
connectAttr "tongue_translate_ex.out[6]" "c_GRP_tongue_joint6.tz";
connectAttr "unitConversion575.o" "c_GRP_tongue_joint6.rx";
connectAttr "unitConversion587.o" "c_GRP_tongue_joint6.ry";
connectAttr "unitConversion599.o" "c_GRP_tongue_joint6.rz";
connectAttr "c_tongue_joint5.s" "c_tongue_joint6.is";
connectAttr "tongue_translate_ex.out[7]" "c_GRP_tongue_joint7.tz";
connectAttr "unitConversion576.o" "c_GRP_tongue_joint7.rx";
connectAttr "unitConversion588.o" "c_GRP_tongue_joint7.ry";
connectAttr "unitConversion600.o" "c_GRP_tongue_joint7.rz";
connectAttr "c_tongue_joint6.s" "c_tongue_joint7.is";
connectAttr "tongue_translate_ex.out[8]" "c_GRP_tongue_joint8.tz";
connectAttr "unitConversion577.o" "c_GRP_tongue_joint8.rx";
connectAttr "unitConversion589.o" "c_GRP_tongue_joint8.ry";
connectAttr "unitConversion601.o" "c_GRP_tongue_joint8.rz";
connectAttr "c_tongue_joint7.s" "c_tongue_joint8.is";
connectAttr "tongue_translate_ex.out[9]" "c_GRP_tongue_joint9.tz";
connectAttr "unitConversion578.o" "c_GRP_tongue_joint9.rx";
connectAttr "unitConversion590.o" "c_GRP_tongue_joint9.ry";
connectAttr "unitConversion602.o" "c_GRP_tongue_joint9.rz";
connectAttr "c_tongue_joint8.s" "c_tongue_joint9.is";
connectAttr "tongue_translate_ex.out[10]" "c_GRP_tongue_joint10.tz";
connectAttr "unitConversion579.o" "c_GRP_tongue_joint10.rx";
connectAttr "unitConversion591.o" "c_GRP_tongue_joint10.ry";
connectAttr "unitConversion603.o" "c_GRP_tongue_joint10.rz";
connectAttr "c_tongue_joint9.s" "c_tongue_joint10.is";
connectAttr "tongue_translate_ex.out[11]" "c_GRP_tongue_joint11.tz";
connectAttr "unitConversion580.o" "c_GRP_tongue_joint11.rx";
connectAttr "unitConversion592.o" "c_GRP_tongue_joint11.ry";
connectAttr "unitConversion604.o" "c_GRP_tongue_joint11.rz";
connectAttr "c_tongue_joint10.s" "c_tongue_joint11.is";
connectAttr "tongue_translate_ex.out[12]" "c_GRP_tongue_joint12.tz";
connectAttr "unitConversion581.o" "c_GRP_tongue_joint12.rx";
connectAttr "unitConversion593.o" "c_GRP_tongue_joint12.ry";
connectAttr "unitConversion605.o" "c_GRP_tongue_joint12.rz";
connectAttr "c_tongue_joint11.s" "c_tongue_joint12.is";
connectAttr "Tongue_M.tongue_boundMesh" "tongue_boundMesh.v";
connectAttr "nurbsTessellate1.op" "tongue_boundMeshShape.i";
connectAttr "Tongue_M.tongue_skinMesh" "tongue_skinMesh.v";
connectAttr "blendShape1GroupId.id" "tongue_skinMeshShape.iog.og[0].gid";
connectAttr "blendShape1Set.mwc" "tongue_skinMeshShape.iog.og[0].gco";
connectAttr "groupId634.id" "tongue_skinMeshShape.iog.og[1].gid";
connectAttr "tweakSet1.mwc" "tongue_skinMeshShape.iog.og[1].gco";
connectAttr "skinCluster1GroupId.id" "tongue_skinMeshShape.iog.og[2].gid";
connectAttr "skinCluster1Set.mwc" "tongue_skinMeshShape.iog.og[2].gco";
connectAttr "skinCluster1.og[0]" "tongue_skinMeshShape.i";
connectAttr "tweak1.vl[0].vt[0]" "tongue_skinMeshShape.twl";
connectAttr "c_tongue_joint12.iog" "tongue_influence.dsm" -na;
connectAttr "c_tongue_joint11.iog" "tongue_influence.dsm" -na;
connectAttr "c_tongue_joint10.iog" "tongue_influence.dsm" -na;
connectAttr "c_tongue_joint9.iog" "tongue_influence.dsm" -na;
connectAttr "c_tongue_joint8.iog" "tongue_influence.dsm" -na;
connectAttr "c_tongue_joint7.iog" "tongue_influence.dsm" -na;
connectAttr "c_tongue_joint6.iog" "tongue_influence.dsm" -na;
connectAttr "c_tongue_joint5.iog" "tongue_influence.dsm" -na;
connectAttr "c_tongue_joint4.iog" "tongue_influence.dsm" -na;
connectAttr "c_tongue_joint3.iog" "tongue_influence.dsm" -na;
connectAttr "c_tongue_joint2.iog" "tongue_influence.dsm" -na;
connectAttr "c_tongue_joint1.iog" "tongue_influence.dsm" -na;
connectAttr "tongueRig_driven_ex.out[0]" "unitConversion606.i";
connectAttr "c_tongue_joint1.up_driven" "tongueRig_driven_ex.in[0]";
connectAttr "c_tongue_joint1.up_scale" "tongueRig_driven_ex.in[1]";
connectAttr "c_tongue_joint1.dn_driven" "tongueRig_driven_ex.in[2]";
connectAttr "c_tongue_joint1.dn_scale" "tongueRig_driven_ex.in[3]";
connectAttr "c_tongue_joint1.driven_envelope" "tongueRig_driven_ex.in[4]";
connectAttr "c_tongue_joint1.lf_driven" "tongueRig_driven_ex.in[5]";
connectAttr "c_tongue_joint1.lf_scale" "tongueRig_driven_ex.in[6]";
connectAttr "c_tongue_joint1.rt_driven" "tongueRig_driven_ex.in[7]";
connectAttr "c_tongue_joint1.rt_scale" "tongueRig_driven_ex.in[8]";
connectAttr "c_tongue_joint1.twist_driven" "tongueRig_driven_ex.in[9]";
connectAttr "c_tongue_joint1.twist_scale" "tongueRig_driven_ex.in[10]";
connectAttr ":time1.o" "tongueRig_driven_ex.tim";
connectAttr "tongueRig_driven_ex.out[1]" "unitConversion607.i";
connectAttr "tongueRig_driven_ex.out[2]" "unitConversion608.i";
connectAttr "Tongue_M.tx" "tongue_translate_ex.in[0]";
connectAttr "Tongue_M.ty" "tongue_translate_ex.in[1]";
connectAttr "Tongue_M.tz" "tongue_translate_ex.in[2]";
connectAttr ":time1.o" "tongue_translate_ex.tim";
connectAttr "tongue_rotate_ex.out[0]" "unitConversion571.i";
connectAttr ":time1.o" "tongue_rotate_ex.tim";
connectAttr "unitConversion570.o" "tongue_rotate_ex.in[0]";
connectAttr "Tongue_M.rotateWeight" "tongue_rotate_ex.in[1]";
connectAttr "Tongue_M.drivenJoint" "tongue_rotate_ex.in[2]";
connectAttr "unitConversion582.o" "tongue_rotate_ex.in[3]";
connectAttr "unitConversion594.o" "tongue_rotate_ex.in[4]";
connectAttr "Tongue_M.rx" "unitConversion570.i";
connectAttr "Tongue_M.ry" "unitConversion582.i";
connectAttr "Tongue_M.rz" "unitConversion594.i";
connectAttr "tongue_rotate_ex.out[11]" "unitConversion583.i";
connectAttr "tongue_rotate_ex.out[22]" "unitConversion595.i";
connectAttr "tongue_rotate_ex.out[1]" "unitConversion572.i";
connectAttr "tongue_rotate_ex.out[12]" "unitConversion584.i";
connectAttr "tongue_rotate_ex.out[23]" "unitConversion596.i";
connectAttr "tongue_rotate_ex.out[2]" "unitConversion573.i";
connectAttr "tongue_rotate_ex.out[13]" "unitConversion585.i";
connectAttr "tongue_rotate_ex.out[24]" "unitConversion597.i";
connectAttr "tongue_rotate_ex.out[3]" "unitConversion574.i";
connectAttr "tongue_rotate_ex.out[14]" "unitConversion586.i";
connectAttr "tongue_rotate_ex.out[25]" "unitConversion598.i";
connectAttr "tongue_rotate_ex.out[4]" "unitConversion575.i";
connectAttr "tongue_rotate_ex.out[15]" "unitConversion587.i";
connectAttr "tongue_rotate_ex.out[26]" "unitConversion599.i";
connectAttr "tongue_rotate_ex.out[5]" "unitConversion576.i";
connectAttr "tongue_rotate_ex.out[16]" "unitConversion588.i";
connectAttr "tongue_rotate_ex.out[27]" "unitConversion600.i";
connectAttr "tongue_rotate_ex.out[6]" "unitConversion577.i";
connectAttr "tongue_rotate_ex.out[17]" "unitConversion589.i";
connectAttr "tongue_rotate_ex.out[28]" "unitConversion601.i";
connectAttr "tongue_rotate_ex.out[7]" "unitConversion578.i";
connectAttr "tongue_rotate_ex.out[18]" "unitConversion590.i";
connectAttr "tongue_rotate_ex.out[29]" "unitConversion602.i";
connectAttr "tongue_rotate_ex.out[8]" "unitConversion579.i";
connectAttr "tongue_rotate_ex.out[19]" "unitConversion591.i";
connectAttr "tongue_rotate_ex.out[30]" "unitConversion603.i";
connectAttr "tongue_rotate_ex.out[9]" "unitConversion580.i";
connectAttr "tongue_rotate_ex.out[20]" "unitConversion592.i";
connectAttr "tongue_rotate_ex.out[31]" "unitConversion604.i";
connectAttr "tongue_rotate_ex.out[10]" "unitConversion581.i";
connectAttr "tongue_rotate_ex.out[21]" "unitConversion593.i";
connectAttr "tongue_rotate_ex.out[32]" "unitConversion605.i";
connectAttr "loft1.os" "nurbsTessellate1.is";
connectAttr "|GRP_TONGUE_TEMPLATE|GRP_tongue_Rig_all|GRP_tongueRig|GRP_tongue_move|GRP_tongue_joint1_move|GRP_tongue_joint1|c_tongue_joint1|nurbsCircleShape1.ws" "loft1.ic[0]"
		;
connectAttr "|GRP_TONGUE_TEMPLATE|GRP_tongue_Rig_all|GRP_tongueRig|GRP_tongue_move|GRP_tongue_joint1_move|GRP_tongue_joint1|c_tongue_joint1|c_GRP_tongue_joint2__move|c_GRP_tongue_joint2|c_tongue_joint2|nurbsCircleShape1.ws" "loft1.ic[1]"
		;
connectAttr "|GRP_TONGUE_TEMPLATE|GRP_tongue_Rig_all|GRP_tongueRig|GRP_tongue_move|GRP_tongue_joint1_move|GRP_tongue_joint1|c_tongue_joint1|c_GRP_tongue_joint2__move|c_GRP_tongue_joint2|c_tongue_joint2|c_GRP_tongue_joint3__move|c_GRP_tongue_joint3|c_tongue_joint3|nurbsCircleShape1.ws" "loft1.ic[2]"
		;
connectAttr "|GRP_TONGUE_TEMPLATE|GRP_tongue_Rig_all|GRP_tongueRig|GRP_tongue_move|GRP_tongue_joint1_move|GRP_tongue_joint1|c_tongue_joint1|c_GRP_tongue_joint2__move|c_GRP_tongue_joint2|c_tongue_joint2|c_GRP_tongue_joint3__move|c_GRP_tongue_joint3|c_tongue_joint3|c_GRP_tongue_joint4__move|c_GRP_tongue_joint4|c_tongue_joint4|nurbsCircleShape1.ws" "loft1.ic[3]"
		;
connectAttr "|GRP_TONGUE_TEMPLATE|GRP_tongue_Rig_all|GRP_tongueRig|GRP_tongue_move|GRP_tongue_joint1_move|GRP_tongue_joint1|c_tongue_joint1|c_GRP_tongue_joint2__move|c_GRP_tongue_joint2|c_tongue_joint2|c_GRP_tongue_joint3__move|c_GRP_tongue_joint3|c_tongue_joint3|c_GRP_tongue_joint4__move|c_GRP_tongue_joint4|c_tongue_joint4|c_GRP_tongue_joint5__move|c_GRP_tongue_joint5|c_tongue_joint5|nurbsCircleShape1.ws" "loft1.ic[4]"
		;
connectAttr "|GRP_TONGUE_TEMPLATE|GRP_tongue_Rig_all|GRP_tongueRig|GRP_tongue_move|GRP_tongue_joint1_move|GRP_tongue_joint1|c_tongue_joint1|c_GRP_tongue_joint2__move|c_GRP_tongue_joint2|c_tongue_joint2|c_GRP_tongue_joint3__move|c_GRP_tongue_joint3|c_tongue_joint3|c_GRP_tongue_joint4__move|c_GRP_tongue_joint4|c_tongue_joint4|c_GRP_tongue_joint5__move|c_GRP_tongue_joint5|c_tongue_joint5|c_GRP_tongue_joint6__move|c_GRP_tongue_joint6|c_tongue_joint6|nurbsCircleShape1.ws" "loft1.ic[5]"
		;
connectAttr "|GRP_TONGUE_TEMPLATE|GRP_tongue_Rig_all|GRP_tongueRig|GRP_tongue_move|GRP_tongue_joint1_move|GRP_tongue_joint1|c_tongue_joint1|c_GRP_tongue_joint2__move|c_GRP_tongue_joint2|c_tongue_joint2|c_GRP_tongue_joint3__move|c_GRP_tongue_joint3|c_tongue_joint3|c_GRP_tongue_joint4__move|c_GRP_tongue_joint4|c_tongue_joint4|c_GRP_tongue_joint5__move|c_GRP_tongue_joint5|c_tongue_joint5|c_GRP_tongue_joint6__move|c_GRP_tongue_joint6|c_tongue_joint6|c_GRP_tongue_joint7__move|c_GRP_tongue_joint7|c_tongue_joint7|nurbsCircleShape1.ws" "loft1.ic[6]"
		;
connectAttr "|GRP_TONGUE_TEMPLATE|GRP_tongue_Rig_all|GRP_tongueRig|GRP_tongue_move|GRP_tongue_joint1_move|GRP_tongue_joint1|c_tongue_joint1|c_GRP_tongue_joint2__move|c_GRP_tongue_joint2|c_tongue_joint2|c_GRP_tongue_joint3__move|c_GRP_tongue_joint3|c_tongue_joint3|c_GRP_tongue_joint4__move|c_GRP_tongue_joint4|c_tongue_joint4|c_GRP_tongue_joint5__move|c_GRP_tongue_joint5|c_tongue_joint5|c_GRP_tongue_joint6__move|c_GRP_tongue_joint6|c_tongue_joint6|c_GRP_tongue_joint7__move|c_GRP_tongue_joint7|c_tongue_joint7|c_GRP_tongue_joint8__move|c_GRP_tongue_joint8|c_tongue_joint8|nurbsCircleShape1.ws" "loft1.ic[7]"
		;
connectAttr "|GRP_TONGUE_TEMPLATE|GRP_tongue_Rig_all|GRP_tongueRig|GRP_tongue_move|GRP_tongue_joint1_move|GRP_tongue_joint1|c_tongue_joint1|c_GRP_tongue_joint2__move|c_GRP_tongue_joint2|c_tongue_joint2|c_GRP_tongue_joint3__move|c_GRP_tongue_joint3|c_tongue_joint3|c_GRP_tongue_joint4__move|c_GRP_tongue_joint4|c_tongue_joint4|c_GRP_tongue_joint5__move|c_GRP_tongue_joint5|c_tongue_joint5|c_GRP_tongue_joint6__move|c_GRP_tongue_joint6|c_tongue_joint6|c_GRP_tongue_joint7__move|c_GRP_tongue_joint7|c_tongue_joint7|c_GRP_tongue_joint8__move|c_GRP_tongue_joint8|c_tongue_joint8|c_GRP_tongue_joint9__move|c_GRP_tongue_joint9|c_tongue_joint9|nurbsCircleShape1.ws" "loft1.ic[8]"
		;
connectAttr "|GRP_TONGUE_TEMPLATE|GRP_tongue_Rig_all|GRP_tongueRig|GRP_tongue_move|GRP_tongue_joint1_move|GRP_tongue_joint1|c_tongue_joint1|c_GRP_tongue_joint2__move|c_GRP_tongue_joint2|c_tongue_joint2|c_GRP_tongue_joint3__move|c_GRP_tongue_joint3|c_tongue_joint3|c_GRP_tongue_joint4__move|c_GRP_tongue_joint4|c_tongue_joint4|c_GRP_tongue_joint5__move|c_GRP_tongue_joint5|c_tongue_joint5|c_GRP_tongue_joint6__move|c_GRP_tongue_joint6|c_tongue_joint6|c_GRP_tongue_joint7__move|c_GRP_tongue_joint7|c_tongue_joint7|c_GRP_tongue_joint8__move|c_GRP_tongue_joint8|c_tongue_joint8|c_GRP_tongue_joint9__move|c_GRP_tongue_joint9|c_tongue_joint9|c_GRP_tongue_joint10__move|c_GRP_tongue_joint10|c_tongue_joint10|nurbsCircleShape1.ws" "loft1.ic[9]"
		;
connectAttr "|GRP_TONGUE_TEMPLATE|GRP_tongue_Rig_all|GRP_tongueRig|GRP_tongue_move|GRP_tongue_joint1_move|GRP_tongue_joint1|c_tongue_joint1|c_GRP_tongue_joint2__move|c_GRP_tongue_joint2|c_tongue_joint2|c_GRP_tongue_joint3__move|c_GRP_tongue_joint3|c_tongue_joint3|c_GRP_tongue_joint4__move|c_GRP_tongue_joint4|c_tongue_joint4|c_GRP_tongue_joint5__move|c_GRP_tongue_joint5|c_tongue_joint5|c_GRP_tongue_joint6__move|c_GRP_tongue_joint6|c_tongue_joint6|c_GRP_tongue_joint7__move|c_GRP_tongue_joint7|c_tongue_joint7|c_GRP_tongue_joint8__move|c_GRP_tongue_joint8|c_tongue_joint8|c_GRP_tongue_joint9__move|c_GRP_tongue_joint9|c_tongue_joint9|c_GRP_tongue_joint10__move|c_GRP_tongue_joint10|c_tongue_joint10|c_GRP_tongue_joint11__move|c_GRP_tongue_joint11|c_tongue_joint11|nurbsCircleShape1.ws" "loft1.ic[10]"
		;
connectAttr "|GRP_TONGUE_TEMPLATE|GRP_tongue_Rig_all|GRP_tongueRig|GRP_tongue_move|GRP_tongue_joint1_move|GRP_tongue_joint1|c_tongue_joint1|c_GRP_tongue_joint2__move|c_GRP_tongue_joint2|c_tongue_joint2|c_GRP_tongue_joint3__move|c_GRP_tongue_joint3|c_tongue_joint3|c_GRP_tongue_joint4__move|c_GRP_tongue_joint4|c_tongue_joint4|c_GRP_tongue_joint5__move|c_GRP_tongue_joint5|c_tongue_joint5|c_GRP_tongue_joint6__move|c_GRP_tongue_joint6|c_tongue_joint6|c_GRP_tongue_joint7__move|c_GRP_tongue_joint7|c_tongue_joint7|c_GRP_tongue_joint8__move|c_GRP_tongue_joint8|c_tongue_joint8|c_GRP_tongue_joint9__move|c_GRP_tongue_joint9|c_tongue_joint9|c_GRP_tongue_joint10__move|c_GRP_tongue_joint10|c_tongue_joint10|c_GRP_tongue_joint11__move|c_GRP_tongue_joint11|c_tongue_joint11|c_GRP_tongue_joint12|c_tongue_joint12|nurbsCircleShape1.ws" "loft1.ic[11]"
		;
connectAttr "blendShape1GroupId.msg" "blendShape1Set.gn" -na;
connectAttr "tongue_skinMeshShape.iog.og[0]" "blendShape1Set.dsm" -na;
connectAttr "blendShape1.msg" "blendShape1Set.ub[0]";
connectAttr "blendShape1GroupParts.og" "blendShape1.ip[0].ig";
connectAttr "blendShape1GroupId.id" "blendShape1.ip[0].gi";
connectAttr "tongue_boundMeshShape.w" "blendShape1.it[0].itg[0].iti[6000].igt";
connectAttr "tweak1.og[0]" "blendShape1GroupParts.ig";
connectAttr "blendShape1GroupId.id" "blendShape1GroupParts.gi";
connectAttr "groupParts2.og" "tweak1.ip[0].ig";
connectAttr "groupId634.id" "tweak1.ip[0].gi";
connectAttr "groupId634.msg" "tweakSet1.gn" -na;
connectAttr "tongue_skinMeshShape.iog.og[1]" "tweakSet1.dsm" -na;
connectAttr "tweak1.msg" "tweakSet1.ub[0]";
connectAttr "tongue_skinMeshShapeOrig.w" "groupParts2.ig";
connectAttr "groupId634.id" "groupParts2.gi";
connectAttr "skinCluster1GroupId.msg" "skinCluster1Set.gn" -na;
connectAttr "tongue_skinMeshShape.iog.og[2]" "skinCluster1Set.dsm" -na;
connectAttr "skinCluster1.msg" "skinCluster1Set.ub[0]";
connectAttr "skinCluster1GroupParts.og" "skinCluster1.ip[0].ig";
connectAttr "skinCluster1GroupId.id" "skinCluster1.ip[0].gi";
connectAttr "bindPose45.msg" "skinCluster1.bp";
connectAttr "c_tongue_joint1.wm" "skinCluster1.ma[0]";
connectAttr "c_tongue_joint2.wm" "skinCluster1.ma[1]";
connectAttr "c_tongue_joint3.wm" "skinCluster1.ma[2]";
connectAttr "c_tongue_joint4.wm" "skinCluster1.ma[3]";
connectAttr "c_tongue_joint5.wm" "skinCluster1.ma[4]";
connectAttr "c_tongue_joint6.wm" "skinCluster1.ma[5]";
connectAttr "c_tongue_joint7.wm" "skinCluster1.ma[6]";
connectAttr "c_tongue_joint8.wm" "skinCluster1.ma[7]";
connectAttr "c_tongue_joint9.wm" "skinCluster1.ma[8]";
connectAttr "c_tongue_joint10.wm" "skinCluster1.ma[9]";
connectAttr "c_tongue_joint11.wm" "skinCluster1.ma[10]";
connectAttr "c_tongue_joint12.wm" "skinCluster1.ma[11]";
connectAttr "c_tongue_joint1.liw" "skinCluster1.lw[0]";
connectAttr "c_tongue_joint2.liw" "skinCluster1.lw[1]";
connectAttr "c_tongue_joint3.liw" "skinCluster1.lw[2]";
connectAttr "c_tongue_joint4.liw" "skinCluster1.lw[3]";
connectAttr "c_tongue_joint5.liw" "skinCluster1.lw[4]";
connectAttr "c_tongue_joint6.liw" "skinCluster1.lw[5]";
connectAttr "c_tongue_joint7.liw" "skinCluster1.lw[6]";
connectAttr "c_tongue_joint8.liw" "skinCluster1.lw[7]";
connectAttr "c_tongue_joint9.liw" "skinCluster1.lw[8]";
connectAttr "c_tongue_joint10.liw" "skinCluster1.lw[9]";
connectAttr "c_tongue_joint11.liw" "skinCluster1.lw[10]";
connectAttr "c_tongue_joint12.liw" "skinCluster1.lw[11]";
connectAttr "c_tongue_joint12.msg" "skinCluster1.ptt";
connectAttr "c_tongue_joint1.wim" "skinCluster1.pm[0]";
connectAttr "c_tongue_joint2.wim" "skinCluster1.pm[1]";
connectAttr "c_tongue_joint3.wim" "skinCluster1.pm[2]";
connectAttr "c_tongue_joint4.wim" "skinCluster1.pm[3]";
connectAttr "c_tongue_joint5.wim" "skinCluster1.pm[4]";
connectAttr "c_tongue_joint6.wim" "skinCluster1.pm[5]";
connectAttr "c_tongue_joint7.wim" "skinCluster1.pm[6]";
connectAttr "c_tongue_joint8.wim" "skinCluster1.pm[7]";
connectAttr "c_tongue_joint9.wim" "skinCluster1.pm[8]";
connectAttr "c_tongue_joint10.wim" "skinCluster1.pm[9]";
connectAttr "c_tongue_joint11.wim" "skinCluster1.pm[10]";
connectAttr "c_tongue_joint12.wim" "skinCluster1.pm[11]";
connectAttr "GRP_tongue_Rig_all.msg" "bindPose45.m[0]";
connectAttr "GRP_tongueRig.msg" "bindPose45.m[1]";
connectAttr "GRP_tongue_move.msg" "bindPose45.m[2]";
connectAttr "GRP_tongue_joint1_move.msg" "bindPose45.m[3]";
connectAttr "GRP_tongue_joint1.msg" "bindPose45.m[4]";
connectAttr "c_tongue_joint1.msg" "bindPose45.m[5]";
connectAttr "c_GRP_tongue_joint2__move.msg" "bindPose45.m[6]";
connectAttr "c_GRP_tongue_joint2.msg" "bindPose45.m[7]";
connectAttr "c_tongue_joint2.msg" "bindPose45.m[8]";
connectAttr "c_GRP_tongue_joint3__move.msg" "bindPose45.m[9]";
connectAttr "c_GRP_tongue_joint3.msg" "bindPose45.m[10]";
connectAttr "c_tongue_joint3.msg" "bindPose45.m[11]";
connectAttr "c_GRP_tongue_joint4__move.msg" "bindPose45.m[12]";
connectAttr "c_GRP_tongue_joint4.msg" "bindPose45.m[13]";
connectAttr "c_tongue_joint4.msg" "bindPose45.m[14]";
connectAttr "c_GRP_tongue_joint5__move.msg" "bindPose45.m[15]";
connectAttr "c_GRP_tongue_joint5.msg" "bindPose45.m[16]";
connectAttr "c_tongue_joint5.msg" "bindPose45.m[17]";
connectAttr "c_GRP_tongue_joint6__move.msg" "bindPose45.m[18]";
connectAttr "c_GRP_tongue_joint6.msg" "bindPose45.m[19]";
connectAttr "c_tongue_joint6.msg" "bindPose45.m[20]";
connectAttr "c_GRP_tongue_joint7__move.msg" "bindPose45.m[21]";
connectAttr "c_GRP_tongue_joint7.msg" "bindPose45.m[22]";
connectAttr "c_tongue_joint7.msg" "bindPose45.m[23]";
connectAttr "c_GRP_tongue_joint8__move.msg" "bindPose45.m[24]";
connectAttr "c_GRP_tongue_joint8.msg" "bindPose45.m[25]";
connectAttr "c_tongue_joint8.msg" "bindPose45.m[26]";
connectAttr "c_GRP_tongue_joint9__move.msg" "bindPose45.m[27]";
connectAttr "c_GRP_tongue_joint9.msg" "bindPose45.m[28]";
connectAttr "c_tongue_joint9.msg" "bindPose45.m[29]";
connectAttr "c_GRP_tongue_joint10__move.msg" "bindPose45.m[30]";
connectAttr "c_GRP_tongue_joint10.msg" "bindPose45.m[31]";
connectAttr "c_tongue_joint10.msg" "bindPose45.m[32]";
connectAttr "c_GRP_tongue_joint11__move.msg" "bindPose45.m[33]";
connectAttr "c_GRP_tongue_joint11.msg" "bindPose45.m[34]";
connectAttr "c_tongue_joint11.msg" "bindPose45.m[35]";
connectAttr "c_GRP_tongue_joint12.msg" "bindPose45.m[36]";
connectAttr "c_tongue_joint12.msg" "bindPose45.m[37]";
connectAttr "bindPose45.w" "bindPose45.p[0]";
connectAttr "bindPose45.m[0]" "bindPose45.p[1]";
connectAttr "bindPose45.m[1]" "bindPose45.p[2]";
connectAttr "bindPose45.m[2]" "bindPose45.p[3]";
connectAttr "bindPose45.m[3]" "bindPose45.p[4]";
connectAttr "bindPose45.m[4]" "bindPose45.p[5]";
connectAttr "bindPose45.m[5]" "bindPose45.p[6]";
connectAttr "bindPose45.m[6]" "bindPose45.p[7]";
connectAttr "bindPose45.m[7]" "bindPose45.p[8]";
connectAttr "bindPose45.m[8]" "bindPose45.p[9]";
connectAttr "bindPose45.m[9]" "bindPose45.p[10]";
connectAttr "bindPose45.m[10]" "bindPose45.p[11]";
connectAttr "bindPose45.m[11]" "bindPose45.p[12]";
connectAttr "bindPose45.m[12]" "bindPose45.p[13]";
connectAttr "bindPose45.m[13]" "bindPose45.p[14]";
connectAttr "bindPose45.m[14]" "bindPose45.p[15]";
connectAttr "bindPose45.m[15]" "bindPose45.p[16]";
connectAttr "bindPose45.m[16]" "bindPose45.p[17]";
connectAttr "bindPose45.m[17]" "bindPose45.p[18]";
connectAttr "bindPose45.m[18]" "bindPose45.p[19]";
connectAttr "bindPose45.m[19]" "bindPose45.p[20]";
connectAttr "bindPose45.m[20]" "bindPose45.p[21]";
connectAttr "bindPose45.m[21]" "bindPose45.p[22]";
connectAttr "bindPose45.m[22]" "bindPose45.p[23]";
connectAttr "bindPose45.m[23]" "bindPose45.p[24]";
connectAttr "bindPose45.m[24]" "bindPose45.p[25]";
connectAttr "bindPose45.m[25]" "bindPose45.p[26]";
connectAttr "bindPose45.m[26]" "bindPose45.p[27]";
connectAttr "bindPose45.m[27]" "bindPose45.p[28]";
connectAttr "bindPose45.m[28]" "bindPose45.p[29]";
connectAttr "bindPose45.m[29]" "bindPose45.p[30]";
connectAttr "bindPose45.m[30]" "bindPose45.p[31]";
connectAttr "bindPose45.m[31]" "bindPose45.p[32]";
connectAttr "bindPose45.m[32]" "bindPose45.p[33]";
connectAttr "bindPose45.m[33]" "bindPose45.p[34]";
connectAttr "bindPose45.m[34]" "bindPose45.p[35]";
connectAttr "bindPose45.m[35]" "bindPose45.p[36]";
connectAttr "bindPose45.m[36]" "bindPose45.p[37]";
connectAttr "c_tongue_joint1.bps" "bindPose45.wm[5]";
connectAttr "c_tongue_joint2.bps" "bindPose45.wm[8]";
connectAttr "c_tongue_joint3.bps" "bindPose45.wm[11]";
connectAttr "c_tongue_joint4.bps" "bindPose45.wm[14]";
connectAttr "c_tongue_joint5.bps" "bindPose45.wm[17]";
connectAttr "c_tongue_joint6.bps" "bindPose45.wm[20]";
connectAttr "c_tongue_joint7.bps" "bindPose45.wm[23]";
connectAttr "c_tongue_joint8.bps" "bindPose45.wm[26]";
connectAttr "c_tongue_joint9.bps" "bindPose45.wm[29]";
connectAttr "c_tongue_joint10.bps" "bindPose45.wm[32]";
connectAttr "c_tongue_joint11.bps" "bindPose45.wm[35]";
connectAttr "c_tongue_joint12.bps" "bindPose45.wm[37]";
connectAttr "blendShape1.og[0]" "skinCluster1GroupParts.ig";
connectAttr "skinCluster1GroupId.id" "skinCluster1GroupParts.gi";
connectAttr "tongue_boundMeshShape.iog" ":initialShadingGroup.dsm" -na;
connectAttr "tongue_skinMeshShape.iog" ":initialShadingGroup.dsm" -na;
// End of High_tongue_rig.ma

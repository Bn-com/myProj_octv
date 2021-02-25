//Maya ASCII 2014 scene
//Name: High_selectPannel_rig.ma
//Last modified: Mon, Aug 24, 2015 09:59:06 AM
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
createNode transform -n "FM_Caml_gui_guides_grp";
	setAttr ".t" -type "double3" 0 -1000 0 ;
	setAttr ".r" -type "double3" -90 0 0 ;
	setAttr ".s" -type "double3" 0.001 0.001 0.001 ;
createNode transform -n "FM_Cam_FACIAL_gui_guides_grp" -p "FM_Caml_gui_guides_grp";
	setAttr ".s" -type "double3" 1 1.0000000000000002 1.0000000000000002 ;
createNode transform -n "FM_Cam_FACIAL_backgroundColor_" -p "FM_Cam_FACIAL_gui_guides_grp";
	setAttr ".rp" -type "double3" 16.331151962280273 0 0 ;
	setAttr ".sp" -type "double3" 16.331151962280273 0 0 ;
createNode mesh -n "FM_Cam_FACIAL_backgroundColor_Shape" -p "FM_Cam_FACIAL_backgroundColor_";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 4 ".uvst[0].uvsp[0:3]" -type "float2" 0 0 1 0 0 1 1 1;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 4 ".pt[0:3]" -type "float3"  -8.9395771 -27.289501 -18.324989 
		8.9395771 -27.289501 -18.324989 -8.9395771 27.289501 18.324989 8.9395771 27.289501 
		18.324989;
	setAttr -s 4 ".vt[0:3]"  -18.10165596 -4.068965e-015 18.32498932 50.76396179 -4.068965e-015 18.32498932
		 -18.10165596 4.068965e-015 -18.32498932 50.76396179 4.068965e-015 -18.32498932;
	setAttr -s 4 ".ed[0:3]"  0 1 0 0 2 0 1 3 0 2 3 0;
	setAttr -ch 4 ".fc[0]" -type "polyFaces" 
		f 4 0 2 -4 -2
		mu 0 4 0 1 3 2;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_characters_FACIAL_backgroundColor_" -p "FM_Cam_FACIAL_gui_guides_grp";
	setAttr ".rp" -type "double3" -15.407978396417462 14.748403056154752 1.1475734710693357 ;
	setAttr ".sp" -type "double3" -15.407978396417462 14.748403056154752 1.1475734710693357 ;
createNode mesh -n "FM_Cam_characters_FACIAL_backgroundColor_Shape" -p "FM_Cam_characters_FACIAL_backgroundColor_";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.24935289472341537 0.77852830290794373 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 4 ".uvst[0].uvsp[0:3]" -type "float2" 0.04565233 0.98222882
		 0.45305347 0.98222882 0.45305347 0.57482779 0.04565233 0.57482779;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 4 ".pt[0:3]" -type "float3"  3.8890169 -6.42697 -2.220446e-016 
		3.8890169 -6.42697 -2.220446e-016 3.8890169 -6.42697 -2.220446e-016 3.8890169 -6.42697 
		-2.220446e-016;
	setAttr -s 4 ".vt[0:3]"  -23.10595703 24.98433685 1.14757347 -15.48803329 24.98433685 1.14757347
		 -23.10595703 17.3664093 1.14757347 -15.48803329 17.3664093 1.14757347;
	setAttr -s 4 ".ed[0:3]"  0 1 0 0 2 0 1 3 0 2 3 0;
	setAttr -ch 4 ".fc[0]" -type "polyFaces" 
		f 4 1 3 -3 -1
		mu 0 4 0 3 2 1;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_characters_FACIAL_backgroundColor_pPlane" -p "FM_Cam_FACIAL_gui_guides_grp";
	setAttr ".v" no;
	setAttr ".s" -type "double3" 1 0.99999999999999978 0.99999999999999978 ;
createNode mesh -n "FM_Cam_characters_FACIAL_backgroundColor_pPlaneShape" -p "FM_Cam_characters_FACIAL_backgroundColor_pPlane";
	setAttr -k off ".v" no;
	setAttr ".mb" no;
	setAttr ".csh" no;
	setAttr ".rcsh" no;
	setAttr ".vis" no;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 4 ".uvst[0].uvsp[0:3]" -type "float2" 0 0 1 0 0 1 1 1;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".ds" no;
	setAttr ".smo" no;
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 4 ".vt[0:3]"  -0.5 -0.5 0 0.5 -0.5 0 -0.5 0.5 0 0.5 0.5 0;
	setAttr -s 4 ".ed[0:3]"  0 1 0 0 2 0 1 3 0 2 3 0;
	setAttr -ch 4 ".fc[0]" -type "polyFaces" 
		f 4 0 2 -4 -2
		mu 0 4 0 1 3 2;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
	setAttr ".fgc" no;
	setAttr ".fge" no;
	setAttr ".tpc" no;
	setAttr ".tpr" no;
	setAttr ".rflr" no;
	setAttr ".rfrr" no;
createNode transform -n "FM_Cam_c_hi_face" -p "FM_Cam_FACIAL_gui_guides_grp";
	setAttr ".rp" -type "double3" -3.3778700828552246 -0.20063400268554651 1.648193359375 ;
	setAttr ".sp" -type "double3" -3.3778700828552246 -0.20063400268554651 1.648193359375 ;
createNode transform -n "FM_Cam_l_hi_eye" -p "FM_Cam_c_hi_face";
	setAttr ".rp" -type "double3" 5.2732334136962891 9.4398949146270752 1.1025676727294902 ;
	setAttr ".sp" -type "double3" 5.2732334136962891 9.4398949146270752 1.1025676727294902 ;
createNode transform -n "c_Lf_eye_CTRL_backgroundColor_" -p "FM_Cam_l_hi_eye";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 5.0389535427093506 9.4398949146270752 0.94457244873046664 ;
	setAttr ".sp" -type "double3" 5.0389535427093506 9.4398949146270752 0.94457244873046664 ;
createNode mesh -n "c_Lf_eye_CTRL_backgroundColor_Shape" -p "c_Lf_eye_CTRL_backgroundColor_";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.6486026 0.89203393
		 0.62640893 0.93559146 0.59184146 0.97015893 0.54828387 0.9923526 0.5 1 0.4517161
		 0.9923526 0.40815854 0.97015893 0.37359107 0.93559146 0.3513974 0.89203393 0.34374997
		 0.84375 0.3513974 0.79546607 0.37359107 0.75190854 0.40815851 0.71734107 0.45171607
		 0.69514734 0.5 0.68749994 0.54828393 0.69514734 0.59184152 0.71734101 0.62640899
		 0.75190848 0.64860266 0.79546607 0.65625 0.84375;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".vt[0:19]"  1.68362904 10.66845703 0.94457209 2.1847434 11.77675629 0.94457209
		 2.96524858 12.65631104 0.94457209 3.94874239 13.22101974 0.94457209 5.038952827 13.41560364 0.94457209
		 6.12916327 13.22101593 0.94457209 7.11265707 12.65631104 0.94457209 7.8931613 11.77675629 0.94457209
		 8.39427567 10.66845703 0.94457209 8.56694794 9.43989563 0.94457209 8.39427567 8.21133423 0.94457209
		 7.8931613 7.10303116 0.94457209 7.11265564 6.22348022 0.94457257 6.12916327 5.65877151 0.94457257
		 5.038952827 5.46418762 0.94457257 3.94874239 5.65877151 0.94457257 2.96525002 6.22348022 0.94457257
		 2.18474627 7.10303116 0.94457209 1.68363047 8.21133423 0.94457209 1.51095915 9.43989563 0.94457209;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 -19 -18 -17 -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 -20
		mu 0 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_l_hi_eye_2_guide" -p "FM_Cam_l_hi_eye";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 5.0611488819122314 12.39503002166748 0.9797782897949191 ;
	setAttr ".sp" -type "double3" 5.0611488819122314 12.39503002166748 0.9797782897949191 ;
createNode mesh -n "FM_Cam_l_hi_eye_2_guideShape" -p "FM_Cam_l_hi_eye_2_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 6 ".uvst[0].uvsp[0:5]" -type "float2" 0.43390542 0.98099685
		 0.43390542 0.98099685 0.44123089 0.94890189 0.44123089 0.94890189 0.43390542 0.98099685
		 0.44123089 0.94890189;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 6 ".vt[0:5]"  5.78819561 12.73447037 0.97977811 4.33410215 12.73447037 0.97977811
		 5.061148643 12.78588486 0.97977811 5.061148643 12.084621429 0.97977811 4.33410215 12.0041770935 0.97977811
		 5.78819561 12.0041770935 0.97977811;
	setAttr -s 6 ".ed[0:5]"  1 2 0 0 5 0 1 4 0 2 0 0 4 3 0 3 5 0;
	setAttr -ch 6 ".fc[0]" -type "polyFaces" 
		f 6 5 -2 -4 -1 2 4
		mu 0 6 2 5 4 1 0 3;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_l_hi_eye_3_guide" -p "FM_Cam_l_hi_eye";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 6.3610012531280518 12.009665489196777 0.97977828979491921 ;
	setAttr ".sp" -type "double3" 6.3610012531280518 12.009665489196777 0.97977828979491921 ;
createNode mesh -n "FM_Cam_l_hi_eye_3_guideShape" -p "FM_Cam_l_hi_eye_3_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 6 ".uvst[0].uvsp[0:5]" -type "float2" 0.44123089 0.94890189
		 0.43390542 0.98099685 0.41824257 0.973454 0.42537722 0.942195 0.40257972 0.96591115
		 0.40952355 0.93548816;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 6 ".vt[0:5]"  6.9338069 11.95444107 0.97977811 6.36100054 12.46500015 0.97977811
		 6.36100054 11.79443741 0.97977811 6.9338069 11.28486252 0.97977811 5.78819561 12.0041770935 0.97977811
		 5.78819561 12.73447037 0.97977811;
	setAttr -s 6 ".ed[0:5]"  0 3 0 5 1 0 1 0 0 2 4 0 3 2 0 5 4 0;
	setAttr -ch 6 ".fc[0]" -type "polyFaces" 
		f 6 -5 -1 -3 -2 5 -4
		mu 0 6 3 5 4 2 1 0;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_l_hi_eye_4_guide" -p "FM_Cam_l_hi_eye";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 3.7612969875335693 12.009665489196777 0.97977828979491921 ;
	setAttr ".sp" -type "double3" 3.7612969875335693 12.009665489196777 0.97977828979491921 ;
createNode mesh -n "FM_Cam_l_hi_eye_4_guideShape" -p "FM_Cam_l_hi_eye_4_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 6 ".uvst[0].uvsp[0:5]" -type "float2" 0.44123089 0.94890189
		 0.42537722 0.942195 0.41824257 0.973454 0.43390542 0.98099685 0.40952355 0.93548816
		 0.40257972 0.96591115;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 6 ".vt[0:5]"  3.76129723 12.46500015 0.97977811 3.18849182 11.95444107 0.97977811
		 3.76129723 11.79443741 0.97977811 3.18849182 11.28486252 0.97977811 4.33410215 12.73447037 0.97977811
		 4.33410215 12.0041770935 0.97977811;
	setAttr -s 6 ".ed[0:5]"  4 0 0 0 1 0 1 3 0 2 5 0 3 2 0 4 5 0;
	setAttr -ch 6 ".fc[0]" -type "polyFaces" 
		f 6 3 -6 0 1 2 4
		mu 0 6 1 0 3 2 5 4;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_l_hi_eye_5_guide" -p "FM_Cam_l_hi_eye";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 6.3610012531280518 6.8777859210968018 0.97977828979492032 ;
	setAttr ".sp" -type "double3" 6.3610012531280518 6.8777859210968018 0.97977828979492032 ;
createNode mesh -n "FM_Cam_l_hi_eye_5_guideShape" -p "FM_Cam_l_hi_eye_5_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 6 ".uvst[0].uvsp[0:5]" -type "float2" 0.48261556 0.69141757
		 0.47568756 0.72177106 0.45848843 0.72095931 0.46523112 0.69141757 0.5 0.69141757
		 0.49288672 0.72258282;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 6 ".vt[0:5]"  6.9338069 6.92534637 0.97977811 6.36100054 6.41478729 0.97977811
		 6.36100054 7.065929413 0.97977811 6.9338069 7.6102562 0.97977811 5.78819561 6.14531708 0.97977811
		 5.78819561 6.85445786 0.97977811;
	setAttr -s 6 ".ed[0:5]"  0 1 0 1 4 0 3 0 0 3 2 0 2 5 0 5 4 0;
	setAttr -ch 6 ".fc[0]" -type "polyFaces" 
		f 6 -1 -3 3 4 5 -2
		mu 0 6 0 3 2 1 5 4;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_l_hi_eye_6_guide" -p "FM_Cam_l_hi_eye";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 5.0611488819122314 6.4741816520690918 0.97977828979492043 ;
	setAttr ".sp" -type "double3" 5.0611488819122314 6.4741816520690918 0.97977828979492043 ;
createNode mesh -n "FM_Cam_l_hi_eye_6_guideShape" -p "FM_Cam_l_hi_eye_6_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 6 ".uvst[0].uvsp[0:5]" -type "float2" 0.49288672 0.72258282
		 0.5 0.69141757 0.5 0.69141757 0.49288672 0.72258282 0.49288672 0.72258282 0.5 0.69141757;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 6 ".vt[0:5]"  5.78819561 6.14531708 0.97977811 4.33410215 6.14531708 0.97977811
		 5.061148643 6.093906403 0.97977811 5.78819561 6.85445786 0.97977811 4.33410215 6.85445786 0.97977811
		 5.061148643 6.77368164 0.97977811;
	setAttr -s 6 ".ed[0:5]"  3 0 0 4 1 0 1 2 0 2 0 0 4 5 0 5 3 0;
	setAttr -ch 6 ".fc[0]" -type "polyFaces" 
		f 6 3 -1 -6 -5 1 2
		mu 0 6 1 5 4 0 3 2;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_l_hi_eye_7_guide" -p "FM_Cam_l_hi_eye";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 3.7612969875335693 6.8777859210968018 0.97977828979492032 ;
	setAttr ".sp" -type "double3" 3.7612969875335693 6.8777859210968018 0.97977828979492032 ;
createNode mesh -n "FM_Cam_l_hi_eye_7_guideShape" -p "FM_Cam_l_hi_eye_7_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 6 ".uvst[0].uvsp[0:5]" -type "float2" 0.48261556 0.69141757
		 0.46523112 0.69141757 0.45848843 0.72095931 0.47568756 0.72177106 0.5 0.69141757
		 0.49288672 0.72258282;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 6 ".vt[0:5]"  3.76129723 6.41478729 0.97977811 3.18849182 6.92534637 0.97977811
		 3.18849182 7.6102562 0.97977811 3.76129723 7.065929413 0.97977811 4.33410215 6.85445786 0.97977811
		 4.33410215 6.14531708 0.97977811;
	setAttr -s 6 ".ed[0:5]"  2 1 0 1 0 0 0 5 0 2 3 0 3 4 0 4 5 0;
	setAttr -ch 6 ".fc[0]" -type "polyFaces" 
		f 6 2 -6 -5 -4 0 1
		mu 0 6 0 4 5 3 2 1;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "c_Lf_pupil_M_guide" -p "FM_Cam_l_hi_eye";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 5.0389535427093506 9.4398937225341797 1.1875686645507793 ;
	setAttr ".sp" -type "double3" 5.0389535427093506 9.4398937225341797 1.1875686645507793 ;
createNode mesh -n "c_Lf_pupil_M_guideShape" -p "c_Lf_pupil_M_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.6486026 0.89203393
		 0.62640893 0.93559146 0.59184146 0.97015893 0.54828387 0.9923526 0.5 1 0.4517161
		 0.9923526 0.40815854 0.97015893 0.37359107 0.93559146 0.3513974 0.89203393 0.34374997
		 0.84375 0.3513974 0.79546607 0.37359107 0.75190854 0.40815851 0.71734107 0.45171607
		 0.69514734 0.5 0.68749994 0.54828393 0.69514734 0.59184152 0.71734101 0.62640899
		 0.75190848 0.64860266 0.79546607 0.65625 0.84375;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".vt[0:19]"  3.84246492 9.82865524 1.18756914 4.021159172 10.17936325 1.18756914
		 4.29948187 10.45768738 1.18756914 4.65019131 10.63638306 1.18756914 5.038952827 10.69795609 1.18756914
		 5.4277153 10.63638306 1.18756914 5.77842379 10.45768738 1.18756914 6.056746483 10.17936325 1.18756914
		 6.23544073 9.82865524 1.18756914 6.29701471 9.43989563 1.18756914 6.23544073 9.051132202 1.18756914
		 6.056746483 8.70042419 1.18756914 5.77842236 8.42210007 1.18756914 5.4277153 8.2434082 1.18756914
		 5.038952827 8.18183136 1.18756914 4.65019131 8.2434082 1.18756914 4.2994833 8.42210007 1.18756914
		 4.021159172 8.70042419 1.18756914 3.84246492 9.051132202 1.18756914 3.78089237 9.43989563 1.18756914;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 -19 -18 -17 -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 -20
		mu 0 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_l_hi_eye_9_guide" -p "FM_Cam_l_hi_eye";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 7.1958298683166504 9.4398946762084961 0.98765945434570102 ;
	setAttr ".sp" -type "double3" 7.1958298683166504 9.4398946762084961 0.98765945434570102 ;
createNode mesh -n "FM_Cam_l_hi_eye_9_guideShape" -p "FM_Cam_l_hi_eye_9_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 12 ".uvst[0].uvsp[0:11]" -type "float2" 0.5 1 0.4517161 0.9923526
		 0.5 0.83749998 0.40815854 0.97015893 0.37359107 0.93559146 0.3513974 0.89203393 0.34374997
		 0.84375 0.3513974 0.79546607 0.37359107 0.75190854 0.40815851 0.71734107 0.45171607
		 0.69514734 0.5 0.68749994;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 12 ".vt[0:11]"  6.76635933 10.29883575 0.98765916 7.031785965 10.25679398 0.98765916
		 7.27123213 10.13479233 0.98765916 7.46125698 9.944767 0.98765916 7.58326101 9.70532227 0.98765916
		 7.62530041 9.43989563 0.98765916 7.58326101 9.17446899 0.98765916 7.46125698 8.93502045 0.98765916
		 7.27123213 8.74499893 0.98765916 7.031785965 8.62299347 0.98765916 6.76635933 8.58095551 0.98765916
		 6.76635933 9.43989563 0.98765916;
	setAttr -s 12 ".ed[0:11]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 0 11 0 10 11 0;
	setAttr -ch 12 ".fc[0]" -type "polyFaces" 
		f 12 -12 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 10
		mu 0 12 2 11 10 9 8 7 6 5 4 3 1 0;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_l_hi_eye_10_guide" -p "FM_Cam_l_hi_eye";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 2.946425199508667 9.4398946762084961 0.98765945434570102 ;
	setAttr ".sp" -type "double3" 2.946425199508667 9.4398946762084961 0.98765945434570102 ;
createNode mesh -n "FM_Cam_l_hi_eye_10_guideShape" -p "FM_Cam_l_hi_eye_10_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 12 ".uvst[0].uvsp[0:11]" -type "float2" 0.6486026 0.89203393
		 0.62640893 0.93559146 0.5 0.83749998 0.59184146 0.97015893 0.54828387 0.9923526 0.5
		 1 0.5 0.68749994 0.54828393 0.69514734 0.59184152 0.71734101 0.62640899 0.75190848
		 0.64860266 0.79546607 0.65625 0.84375;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 12 ".vt[0:11]"  2.54926968 9.71198273 0.98765916 2.67433548 9.95743942 0.98765916
		 2.86913013 10.15223312 0.98765916 3.11458588 10.27730179 0.98765916 3.38667488 10.32039642 0.98765916
		 3.38667488 8.55939484 0.98765916 3.11458588 8.60248947 0.98765916 2.86913013 8.72755432 0.98765916
		 2.67433548 8.92234802 0.98765916 2.54926968 9.16780472 0.98765916 2.50617552 9.43989563 0.98765916
		 3.38667488 9.43989563 0.98765916;
	setAttr -s 12 ".ed[0:11]"  0 1 0 1 2 0 2 3 0 3 4 0 5 6 0 6 7 0 7 8 0
		 8 9 0 9 10 0 10 0 0 4 11 0 5 11 0;
	setAttr -ch 12 ".fc[0]" -type "polyFaces" 
		f 12 -11 -4 -3 -2 -1 -10 -9 -8 -7 -6 -5 11
		mu 0 12 2 5 4 3 1 0 11 10 9 8 7 6;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_l_hi_eye_11_guide" -p "FM_Cam_l_hi_eye";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 7.8467056751251221 7.9531514644622803 0.9506950378417951 ;
	setAttr ".sp" -type "double3" 7.8467056751251221 7.9531514644622803 0.9506950378417951 ;
createNode mesh -n "FM_Cam_l_hi_eye_11_guideShape" -p "FM_Cam_l_hi_eye_11_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 4 ".uvst[0].uvsp[0:3]" -type "float2" 0.375 0.25 0.625
		 0.25 0.625 0.5 0.375 0.5;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 4 ".pt[0:3]" -type "float3"  0 -27.812107 0 0 -27.812107 
		-9.5367432e-007 0 -27.812107 0 0 -27.812107 -9.5367432e-007;
	setAttr -s 4 ".vt[0:3]"  8.25075436 35.86001587 0.95069551 7.47817326 35.57442474 0.95069551
		 8.21523857 35.95609283 0.95069551 7.44265699 35.67050171 0.95069551;
	setAttr -s 4 ".ed[0:3]"  0 1 0 2 3 0 0 2 0 1 3 0;
	setAttr -ch 4 ".fc[0]" -type "polyFaces" 
		f 4 2 1 -4 -1
		mu 0 4 0 3 2 1;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "c_Lf_eyeStretch_CTRL_guide" -p "FM_Cam_l_hi_eye";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 8.0447254180908203 7.4407000541687012 0.95069503784179521 ;
	setAttr ".sp" -type "double3" 8.0447254180908203 7.4407000541687012 0.95069503784179521 ;
createNode mesh -n "c_Lf_eyeStretch_CTRL_guideShape" -p "c_Lf_eyeStretch_CTRL_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 7 ".uvst[0].uvsp[0:6]" -type "float2" 0.375 0.25 0.40625
		 0.25 0.875 1 0.375 0.25 0.53125 0.4375 0.875 1 0.875 0;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 7 ".vt[0:6]"  8.48777676 7.566082 0.95069456 7.88420868 7.89860916 0.95069456
		 8.38456154 7.12900162 0.95069456 8.26357651 7.49119186 0.95069456 7.60167408 7.2700882 0.95069456
		 7.82587624 7.34497833 0.95069456 7.94685936 6.9827919 0.95069504;
	setAttr -s 7 ".ed[0:6]"  0 3 0 0 1 0 2 6 0 2 3 0 4 5 0 4 1 0 6 5 0;
	setAttr -ch 7 ".fc[0]" -type "polyFaces" 
		f 7 -1 1 -6 4 -7 -3 3
		mu 0 7 1 0 4 3 6 5 2;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "c_Lf_eye_M_guide" -p "FM_Cam_l_hi_eye";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 5.0611493587493896 9.4019908905029297 1.0307197570800761 ;
	setAttr ".sp" -type "double3" 5.0611493587493896 9.4019908905029297 1.0307197570800761 ;
createNode mesh -n "c_Lf_eye_M_guideShape" -p "c_Lf_eye_M_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.47029039 0.74541754
		 0.43129694 0.91625899 0.41528496 0.91024578 0.45323563 0.74397337 0.48734522 0.7468617
		 0.4473089 0.92227226 0.4473089 0.92227226 0.48734522 0.7468617 0.4473089 0.92227226
		 0.48734522 0.7468617 0.47029039 0.74541754 0.43129694 0.91625899 0.45323563 0.74397337
		 0.41528496 0.91024578;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 14 ".vt[0:13]"  6.9338069 10.30266953 1.030719876 6.36099911 10.99899292 1.030719876
		 5.78819561 11.31653976 1.030719876 5.061148643 11.48084641 1.030719876 4.33410215 11.31653976 1.030719876
		 3.76129723 10.99899292 1.030719876 3.18849182 10.30266953 1.030719876 6.9338069 8.55427551 1.030719876
		 6.36100054 7.81225586 1.030719876 5.78819561 7.48860931 1.030719876 5.061148643 7.32313538 1.030719876
		 4.33410215 7.48860931 1.030719876 3.76129723 7.81225586 1.030719876 3.18849182 8.55427551 1.030719876;
	setAttr -s 14 ".ed[0:13]"  0 7 0 0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 6 13 0
		 5 6 0 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0;
	setAttr -ch 14 ".fc[0]" -type "polyFaces" 
		f 14 -13 -12 -11 -10 -9 -1 1 2 3 4 5 7 6 -14
		mu 0 14 10 9 7 4 0 3 2 1 5 6 8 11 13 12;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_l_hi_eye_14_guide" -p "FM_Cam_l_hi_eye";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr ".ove" yes;
	setAttr ".rp" -type "double3" 6.3610012531280518 7.7043659687042236 0.97977828979492021 ;
	setAttr ".sp" -type "double3" 6.3610012531280518 7.7043659687042236 0.97977828979492021 ;
createNode mesh -n "FM_Cam_l_hi_eye_14_guideShape" -p "FM_Cam_l_hi_eye_14_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 6 ".uvst[0].uvsp[0:5]" -type "float2" 0.47568756 0.72177106
		 0.47029039 0.74541754 0.45323563 0.74397337 0.45848843 0.72095931 0.49288672 0.72258282
		 0.48734522 0.7468617;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 6 ".vt[0:5]"  6.9338069 7.6102562 0.97977811 6.36100054 7.065929413 0.97977811
		 6.36100054 7.81225586 0.97977811 6.9338069 8.55427551 0.97977811 5.78819561 6.85445786 0.97977811
		 5.78819561 7.48860931 0.97977811;
	setAttr -s 6 ".ed[0:5]"  0 1 0 1 4 0 3 0 0 3 2 0 2 5 0 5 4 0;
	setAttr -ch 6 ".fc[0]" -type "polyFaces" 
		f 6 -1 -3 3 4 5 -2
		mu 0 6 0 3 2 1 5 4;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_l_hi_eye_15_guide" -p "FM_Cam_l_hi_eye";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr ".ove" yes;
	setAttr ".rp" -type "double3" 5.0611488819122314 7.1311447620391846 0.97977828979492032 ;
	setAttr ".sp" -type "double3" 5.0611488819122314 7.1311447620391846 0.97977828979492032 ;
createNode mesh -n "FM_Cam_l_hi_eye_15_guideShape" -p "FM_Cam_l_hi_eye_15_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 6 ".uvst[0].uvsp[0:5]" -type "float2" 0.48734522 0.7468617
		 0.48734522 0.7468617 0.49288672 0.72258282 0.49288672 0.72258282 0.48734522 0.7468617
		 0.49288672 0.72258282;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 6 ".vt[0:5]"  5.78819561 6.85445786 0.97977811 4.33410215 6.85445786 0.97977811
		 5.061148643 6.77368164 0.97977811 5.78819561 7.48860931 0.97977811 5.061148643 7.32313538 0.97977811
		 4.33410215 7.48860931 0.97977811;
	setAttr -s 6 ".ed[0:5]"  1 2 0 2 0 0 3 0 0 5 1 0 3 4 0 4 5 0;
	setAttr -ch 6 ".fc[0]" -type "polyFaces" 
		f 6 1 -3 4 5 3 0
		mu 0 6 3 2 1 0 4 5;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_l_hi_eye_16_guide" -p "FM_Cam_l_hi_eye";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr ".ove" yes;
	setAttr ".rp" -type "double3" 3.7612969875335693 7.7043659687042236 0.97977828979492021 ;
	setAttr ".sp" -type "double3" 3.7612969875335693 7.7043659687042236 0.97977828979492021 ;
createNode mesh -n "FM_Cam_l_hi_eye_16_guideShape" -p "FM_Cam_l_hi_eye_16_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 6 ".uvst[0].uvsp[0:5]" -type "float2" 0.49288672 0.72258282
		 0.47568756 0.72177106 0.47029039 0.74541754 0.48734522 0.7468617 0.45848843 0.72095931
		 0.45323563 0.74397337;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 6 ".vt[0:5]"  3.76129723 7.065929413 0.97977811 3.18849182 7.6102562 0.97977811
		 3.76129723 7.81225586 0.97977811 3.18849182 8.55427551 0.97977811 4.33410215 7.48860931 0.97977811
		 4.33410215 6.85445786 0.97977811;
	setAttr -s 6 ".ed[0:5]"  1 0 0 0 5 0 3 1 0 4 2 0 2 3 0 4 5 0;
	setAttr -ch 6 ".fc[0]" -type "polyFaces" 
		f 6 1 -6 3 4 2 0
		mu 0 6 1 0 3 2 5 4;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_l_hi_eye_17_guide" -p "FM_Cam_l_hi_eye";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr ".ove" yes;
	setAttr ".rp" -type "double3" 5.0611488819122314 11.700579643249512 0.97977828979491932 ;
	setAttr ".sp" -type "double3" 5.0611488819122314 11.700579643249512 0.97977828979491932 ;
createNode mesh -n "FM_Cam_l_hi_eye_17_guideShape" -p "FM_Cam_l_hi_eye_17_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 6 ".uvst[0].uvsp[0:5]" -type "float2" 0.44123089 0.94890189
		 0.4473089 0.92227226 0.4473089 0.92227226 0.44123089 0.94890189 0.44123089 0.94890189
		 0.4473089 0.92227226;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 6 ".vt[0:5]"  5.78819561 12.0041770935 0.97977811 4.33410215 12.0041770935 0.97977811
		 5.061148643 12.084621429 0.97977811 5.78819561 11.31653976 0.97977811 5.061148643 11.48084641 0.97977811
		 4.33410215 11.31653976 0.97977811;
	setAttr -s 6 ".ed[0:5]"  0 3 0 1 2 0 1 5 0 2 0 0 4 5 0 3 4 0;
	setAttr -ch 6 ".fc[0]" -type "polyFaces" 
		f 6 -6 -1 -4 -2 2 -5
		mu 0 6 1 5 4 0 3 2;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_l_hi_eye_18_guide" -p "FM_Cam_l_hi_eye";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr ".ove" yes;
	setAttr ".rp" -type "double3" 3.7612969875335693 11.153422355651855 0.97977828979491943 ;
	setAttr ".sp" -type "double3" 3.7612969875335693 11.153422355651855 0.97977828979491943 ;
createNode mesh -n "FM_Cam_l_hi_eye_18_guideShape" -p "FM_Cam_l_hi_eye_18_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 6 ".uvst[0].uvsp[0:5]" -type "float2" 0.43129694 0.91625899
		 0.41528496 0.91024578 0.40952355 0.93548816 0.42537722 0.942195 0.4473089 0.92227226
		 0.44123089 0.94890189;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 6 ".vt[0:5]"  3.76129723 11.79443741 0.97977811 3.18849182 11.28486252 0.97977811
		 3.76129723 10.99899292 0.97977811 3.18849182 10.30266953 0.97977811 4.33410215 12.0041770935 0.97977811
		 4.33410215 11.31653976 0.97977811;
	setAttr -s 6 ".ed[0:5]"  0 4 0 1 0 0 1 3 0 2 3 0 5 2 0 4 5 0;
	setAttr -ch 6 ".fc[0]" -type "polyFaces" 
		f 6 -5 -6 -1 -2 2 -4
		mu 0 6 0 4 5 3 2 1;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_l_hi_eye_19_guide" -p "FM_Cam_l_hi_eye";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr ".ove" yes;
	setAttr ".rp" -type "double3" 6.3610012531280518 11.153422355651855 0.97977828979491943 ;
	setAttr ".sp" -type "double3" 6.3610012531280518 11.153422355651855 0.97977828979491943 ;
createNode mesh -n "FM_Cam_l_hi_eye_19_guideShape" -p "FM_Cam_l_hi_eye_19_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 6 ".uvst[0].uvsp[0:5]" -type "float2" 0.43129694 0.91625899
		 0.42537722 0.942195 0.40952355 0.93548816 0.41528496 0.91024578 0.4473089 0.92227226
		 0.44123089 0.94890189;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 6 ".vt[0:5]"  6.9338069 11.28486252 0.97977811 6.36100054 11.79443741 0.97977811
		 6.9338069 10.30266953 0.97977811 6.36099911 10.99899292 0.97977811 5.78819561 11.31653976 0.97977811
		 5.78819561 12.0041770935 0.97977811;
	setAttr -s 6 ".ed[0:5]"  0 2 0 0 1 0 1 5 0 2 3 0 3 4 0 5 4 0;
	setAttr -ch 6 ".fc[0]" -type "polyFaces" 
		f 6 -4 -1 1 2 5 -5
		mu 0 6 0 3 2 1 5 4;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "c_Lf_spec_M_guide" -p "FM_Cam_l_hi_eye";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 5.0112409591674805 9.4121818542480469 1.2605628967285138 ;
	setAttr ".sp" -type "double3" 5.0112409591674805 9.4121818542480469 1.2605628967285138 ;
createNode mesh -n "c_Lf_spec_M_guideShape" -p "c_Lf_spec_M_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 34 ".uvst[0].uvsp[0:33]" -type "float2" 0.6486026 0.89203393
		 0.62640893 0.93559146 0.59184146 0.97015893 0.54828387 0.9923526 0.5 1 0.5 1 0.34374997
		 0.84375 0.3513974 0.79546607 0.34374997 0.84375 0.37359107 0.75190854 0.40815851
		 0.71734107 0.45171607 0.69514734 0.5 0.68749994 0.54828393 0.69514734 0.59184152
		 0.71734101 0.62640899 0.75190848 0.64860266 0.79546607 0.65625 0.84375 0.5 1 0.54828387
		 0.9923526 0.59184146 0.97015893 0.62640893 0.93559146 0.6486026 0.89203393 0.65625
		 0.84375 0.64860266 0.79546607 0.62640899 0.75190848 0.59184152 0.71734101 0.54828393
		 0.69514734 0.5 0.68749994 0.45171607 0.69514734 0.40815851 0.71734107 0.37359107
		 0.75190854 0.3513974 0.79546607 0.34374997 0.84375;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 34 ".pt[0:33]" -type "float3"  0.6876359 -1.4325733 0 0.20869045 
		-1.592223 0 0.087449558 -0.86265022 0 0.34687647 -0.77617615 0 -0.29614922 -1.5960592 
		0 -0.18600914 -0.86473221 0 -0.77747053 -1.443707 0 -0.446729 -0.7822082 0 -0.95625353 
		-1.1933335 0 -0.75505733 -0.749237 0 -0.99706507 1.2138668 0 -0.79932314 1.4317206 
		0 -0.45855939 0.77532691 0 -0.67321831 0.75446326 0 -0.32037532 1.5913757 0 -0.19913061 
		0.86180675 0 0.18446483 1.5952114 0 0.074325718 0.8638835 0 0.66578716 1.4428582 
		0 0.33504033 0.78135699 0 1.0764643 1.1492236 0 0.55749267 0.62230361 0 1.3763067 
		0.7430566 0 0.71990716 0.40229571 0 1.5359565 0.26410633 0 0.80638796 0.14286405 
		0 1.5397936 -0.24073333 0 0.80846614 -0.13059084 0 1.3874376 -0.72205371 0 0.72594112 
		-0.39130592 0 1.0938028 -1.1327308 0 0.56688577 -0.61376214 0 -0.94462264 -0.90281749 
		0 -0.91969335 0.895078 0;
	setAttr -s 34 ".vt[0:33]"  3.96194124 9.78983688 1.26056302 4.1227932 10.10552216 1.26056302
		 4.54269743 9.80044174 1.26056302 4.45556879 9.62944794 1.26056302 4.37332392 10.3560524 1.26056302
		 4.67840147 9.9361496 1.26056302 4.68901157 10.51690674 1.26056302 4.849401 10.023281097 1.26056302
		 4.90170145 10.47976303 1.26056302 5.019802094 10.15863419 1.26056302 6.10755157 9.29626083 1.26056302
		 6.11596441 9.089954376 1.26056302 5.62233639 9.25033951 1.26056302 5.71939135 9.36648178 1.26056302
		 5.95511389 8.77426529 1.26056302 5.53520966 9.079341888 1.26056302 5.70458269 8.52373505 1.26056302
		 5.39950418 8.94363785 1.26056302 5.38889408 8.36288071 1.26056302 5.22850609 8.85651016 1.26056302
		 5.038952827 8.30745697 1.26056302 5.038952827 8.82648849 1.26056302 4.68901157 8.36288071 1.26056302
		 4.849401 8.85651016 1.26056302 4.37332392 8.52373505 1.26056302 4.67840147 8.94363785 1.26056302
		 4.1227932 8.77426529 1.26056302 4.54269743 9.079341888 1.26056302 3.96194124 9.089954376 1.26056302
		 4.45556879 9.25033951 1.26056302 3.90651751 9.43989563 1.26056302 4.42554617 9.43989563 1.26056302
		 5.038952827 10.32877731 1.26056302 5.91187572 9.41755295 1.26056302;
	setAttr -s 34 ".ed[0:33]"  0 1 0 3 2 0 1 4 0 2 5 0 4 6 0 5 7 0 6 8 0
		 8 32 0 7 9 0 10 11 0 13 12 0 10 33 0 11 14 0 12 15 0 14 16 0 15 17 0 16 18 0 17 19 0
		 18 20 0 19 21 0 20 22 0 21 23 0 22 24 0 23 25 0 24 26 0 25 27 0 26 28 0 27 29 0 28 30 0
		 29 31 0 30 0 0 31 3 0 32 9 0 33 13 0;
	setAttr -ch 34 ".fc[0]" -type "polyFaces" 
		f 34 13 15 17 19 21 23 25 27 29 31 1 3 5 8 -33 -8 -7 -5 -3 -1 -31 -29 -27 -25 -23 -21
		 -19 -17 -15 -13 -10 11 33 10
		mu 0 34 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 5 4 3 2 1 0 17 16 15 14 13 12 11 10
		 9 7 6 8 33;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "c_Lf_dn_eyelids_CTRL_guide" -p "FM_Cam_l_hi_eye";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 1.9097495079040527 7.2884385585784912 1.0385551452636703 ;
	setAttr ".sp" -type "double3" 1.9097495079040527 7.2884385585784912 1.0385551452636703 ;
createNode mesh -n "c_Lf_dn_eyelids_CTRL_guideShape" -p "c_Lf_dn_eyelids_CTRL_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 12 ".uvst[0].uvsp[0:11]" -type "float2" 0.375 0.25 0.40625
		 0.25 0.38149059 0.25778872 0.875 1 0.75 1 0.51945782 0.42334932 0.53125 0.4375 0.875
		 1 0.875 0 0.51944202 0.42333046 0.38168237 0.25801882 0.375 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 12 ".vt[0:11]"  1.36498928 7.98371124 1.038554668 1.91345549 6.22903061 1.038555145
		 1.90922832 8.34727478 1.038555622 1.61483479 8.34670258 1.038555622 1.61553955 7.98419952 1.038554668
		 2.45488358 7.98583221 1.038554668 2.20433807 7.98534393 1.038554668 2.20363331 8.34784698 1.038555622
		 1.83147526 6.28778839 1.038555145 1.99512625 6.28793716 1.038555145 1.30371952 7.90819168 1.038554668
		 2.5157795 7.90831757 1.038554668;
	setAttr -s 12 ".ed[0:11]"  0 10 0 3 2 0 3 4 0 5 6 0 5 11 0 7 6 0 7 2 0
		 0 4 0 8 1 0 9 1 0 10 8 0 11 9 0;
	setAttr -ch 12 ".fc[0]" -type "polyFaces" 
		f 12 10 8 -10 -12 -5 3 -6 6 -2 2 -8 0
		mu 0 12 2 9 6 5 10 11 8 7 4 3 1 0;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "c_Lf_up_eyelids_CTRL_guide" -p "FM_Cam_l_hi_eye";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 1.9037876129150391 11.592889785766602 1.0385551452636692 ;
	setAttr ".sp" -type "double3" 1.9037876129150391 11.592889785766602 1.0385551452636692 ;
createNode mesh -n "c_Lf_up_eyelids_CTRL_guideShape" -p "c_Lf_up_eyelids_CTRL_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 12 ".uvst[0].uvsp[0:11]" -type "float2" 0.375 0.25 0.38149059
		 0.25778872 0.875 1 0.875 0 0.51945782 0.42334932 0.875 1 0.75 1 0.51944202 0.42333046
		 0.53125 0.4375 0.38168237 0.25801882 0.40625 0.25 0.375 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 12 ".vt[0:11]"  1.35932827 10.89549637 1.038555622 1.9009614 12.65229797 1.038555622
		 1.90497732 10.5340538 1.038555622 1.61058092 10.5334816 1.038555622 1.60987568 10.89598465 1.038555622
		 2.4492197 10.89761734 1.038555622 2.1986742 10.89712906 1.038555622 2.19937944 10.53462601 1.038555622
		 1.81921291 12.59321976 1.038555622 1.98286152 12.59371185 1.038555622 1.29776192 10.97077942 1.038555622
		 2.50981331 10.9753685 1.038555622;
	setAttr -s 12 ".ed[0:11]"  0 10 0 3 2 0 3 4 0 5 6 0 5 11 0 7 6 0 7 2 0
		 0 4 0 8 1 0 9 1 0 10 8 0 11 9 0;
	setAttr -ch 12 ".fc[0]" -type "polyFaces" 
		f 12 -1 7 -3 1 -7 5 -4 4 11 9 -9 -11
		mu 0 12 1 0 3 2 6 5 10 11 9 4 8 7;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "c_Lf_eyelids_CTRL_guide" -p "FM_Cam_l_hi_eye";
	setAttr ".s" -type "double3" 1 0.99999999999999956 0.99999999999999978 ;
	setAttr ".rp" -type "double3" 8.2756277827324496 10.717866897582988 1.0351848602294906 ;
	setAttr ".sp" -type "double3" 8.2756277827324496 10.717866897582994 1.0351848602294909 ;
	setAttr ".spt" -type "double3" 0 -5.329070518200749e-015 -2.2204460492503126e-016 ;
createNode mesh -n "c_Lf_eyelids_CTRL_guideShape" -p "c_Lf_eyelids_CTRL_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0 0 0.25 0 0.5 0
		 0.75 0 0 0.25 0 0.5 1 0.5 0 0.75 1 0.75 0 1 0.25 1 0.5 1 0.75 1 1 1;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 14 ".pt[0:13]" -type "float3"  18.416265 -1.4210855e-014 
		-1.3322676e-015 18.193634 -1.4210855e-014 -1.3322676e-015 17.462858 -1.4210855e-014 
		-1.3322676e-015 16.934574 -1.4210855e-014 -1.3322676e-015 18.367149 -1.4210855e-014 
		-1.3322676e-015 17.658102 -1.4210855e-014 -1.3322676e-015 17.012625 -1.4210855e-014 
		-1.3322676e-015 16.448761 -1.4210855e-014 -1.3322676e-015 16.837757 -1.4210855e-014 
		-1.3322676e-015 14.805871 -1.4210855e-014 -1.3322676e-015 14.58393 -1.4210855e-014 
		-1.3322676e-015 15.563691 -1.4210855e-014 -1.3322676e-015 16.228382 -1.4210855e-014 
		-1.3322676e-015 16.559992 -1.4210855e-014 -1.3322676e-015;
	setAttr -s 14 ".vt[0:13]"  -9.18255424 10.26820755 1.035186768 -9.071238518 9.49691772 1.035182953
		 -8.7058506 8.9657402 1.035186768 -8.44170856 8.88540649 1.035182953 -9.15799618 11.03950119 1.035186768
		 -8.80347252 11.73529434 1.035186768 -8.48073387 9.6998558 1.035186768 -8.19880199 12.26578903 1.035186768
		 -8.39330006 10.26377487 1.035186768 -7.37735701 12.5503273 1.035186768 -7.26638651 12.44075394 1.035186768
		 -7.75626707 11.83792496 1.035186768 -8.088612556 11.19745255 1.035186768 -8.25441742 10.75442123 1.035186768;
	setAttr -s 14 ".ed[0:13]"  0 1 0 0 4 0 1 2 0 2 3 0 4 5 0 3 6 0 5 7 0
		 6 8 0 7 9 0 8 13 0 9 10 0 10 11 0 11 12 0 12 13 0;
	setAttr -ch 14 ".fc[0]" -type "polyFaces" 
		f 14 -8 -6 -4 -3 -1 1 4 6 8 10 11 12 13 -10
		mu 0 14 8 6 3 2 1 0 4 5 7 9 10 11 12 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_r_hi_eye" -p "FM_Cam_c_hi_face";
	setAttr ".rp" -type "double3" -5.207082986831665 9.4398949146270752 1.1025676727294902 ;
	setAttr ".sp" -type "double3" -5.207082986831665 9.4398949146270752 1.1025676727294902 ;
createNode transform -n "FM_Cam_r_hi_eye_1_guide" -p "FM_Cam_r_hi_eye";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -4.9728034734725952 9.4398949146270752 0.94457244873046664 ;
	setAttr ".sp" -type "double3" -4.9728034734725952 9.4398949146270752 0.94457244873046664 ;
createNode mesh -n "FM_Cam_r_hi_eye_1_guideShape" -p "FM_Cam_r_hi_eye_1_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.6486026 0.89203393
		 0.62640893 0.93559146 0.59184146 0.97015893 0.54828387 0.9923526 0.5 1 0.4517161
		 0.9923526 0.40815854 0.97015893 0.37359107 0.93559146 0.3513974 0.89203393 0.34374997
		 0.84375 0.3513974 0.79546607 0.37359107 0.75190854 0.40815851 0.71734107 0.45171607
		 0.69514734 0.5 0.68749994 0.54828393 0.69514734 0.59184152 0.71734101 0.62640899
		 0.75190848 0.64860266 0.79546607 0.65625 0.84375;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".vt[0:19]"  -1.61747885 10.66845703 0.94457209 -2.11859322 11.77675629 0.94457209
		 -2.8990984 12.65631104 0.94457209 -3.8825922 13.22101974 0.94457209 -4.97280264 13.41560364 0.94457209
		 -6.063013077 13.22101593 0.94457209 -7.046506882 12.65631104 0.94457209 -7.82701111 11.77675629 0.94457209
		 -8.328125 10.66845703 0.94457209 -8.50079823 9.43989563 0.94457209 -8.328125 8.21133423 0.94457209
		 -7.82701111 7.10303116 0.94457209 -7.046505928 6.22348022 0.94457257 -6.063013077 5.65877151 0.94457257
		 -4.97280264 5.46418762 0.94457257 -3.8825922 5.65877151 0.94457257 -2.89909983 6.22348022 0.94457257
		 -2.11859584 7.10303116 0.94457209 -1.61748028 8.21133423 0.94457209 -1.44480872 9.43989563 0.94457209;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 19 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		mu 0 20 19 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_r_hi_eye_2_guide" -p "FM_Cam_r_hi_eye";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -4.9949986934661865 12.39503002166748 0.9797782897949191 ;
	setAttr ".sp" -type "double3" -4.9949986934661865 12.39503002166748 0.9797782897949191 ;
createNode mesh -n "FM_Cam_r_hi_eye_2_guideShape" -p "FM_Cam_r_hi_eye_2_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 6 ".uvst[0].uvsp[0:5]" -type "float2" 0.43390542 0.98099685
		 0.43390542 0.98099685 0.44123089 0.94890189 0.44123089 0.94890189 0.43390542 0.98099685
		 0.44123089 0.94890189;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 6 ".vt[0:5]"  -5.72204542 12.73447037 0.97977811 -4.26795197 12.73447037 0.97977811
		 -4.99499798 12.78588486 0.97977811 -4.99499798 12.084621429 0.97977811 -4.26795197 12.0041770935 0.97977811
		 -5.72204542 12.0041770935 0.97977811;
	setAttr -s 6 ".ed[0:5]"  1 2 0 0 5 0 1 4 0 2 0 0 4 3 0 3 5 0;
	setAttr -ch 6 ".fc[0]" -type "polyFaces" 
		f 6 -5 -3 0 3 1 -6
		mu 0 6 2 3 0 1 4 5;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_r_hi_eye_3_guide" -p "FM_Cam_r_hi_eye";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -6.2948510646820068 12.009665489196777 0.97977828979491921 ;
	setAttr ".sp" -type "double3" -6.2948510646820068 12.009665489196777 0.97977828979491921 ;
createNode mesh -n "FM_Cam_r_hi_eye_3_guideShape" -p "FM_Cam_r_hi_eye_3_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 6 ".uvst[0].uvsp[0:5]" -type "float2" 0.44123089 0.94890189
		 0.43390542 0.98099685 0.41824257 0.973454 0.42537722 0.942195 0.40257972 0.96591115
		 0.40952355 0.93548816;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 6 ".vt[0:5]"  -6.86765671 11.95444107 0.97977811 -6.29485035 12.46500015 0.97977811
		 -6.29485035 11.79443741 0.97977811 -6.86765671 11.28486252 0.97977811 -5.72204542 12.0041770935 0.97977811
		 -5.72204542 12.73447037 0.97977811;
	setAttr -s 6 ".ed[0:5]"  0 3 0 5 1 0 1 0 0 2 4 0 3 2 0 5 4 0;
	setAttr -ch 6 ".fc[0]" -type "polyFaces" 
		f 6 3 -6 1 2 0 4
		mu 0 6 3 0 1 2 4 5;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_r_hi_eye_4_guide" -p "FM_Cam_r_hi_eye";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -3.6951465606689453 12.009665489196777 0.97977828979491921 ;
	setAttr ".sp" -type "double3" -3.6951465606689453 12.009665489196777 0.97977828979491921 ;
createNode mesh -n "FM_Cam_r_hi_eye_4_guideShape" -p "FM_Cam_r_hi_eye_4_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 6 ".uvst[0].uvsp[0:5]" -type "float2" 0.44123089 0.94890189
		 0.42537722 0.942195 0.41824257 0.973454 0.43390542 0.98099685 0.40952355 0.93548816
		 0.40257972 0.96591115;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 6 ".vt[0:5]"  -3.69514728 12.46500015 0.97977811 -3.12234116 11.95444107 0.97977811
		 -3.69514728 11.79443741 0.97977811 -3.12234116 11.28486252 0.97977811 -4.26795197 12.73447037 0.97977811
		 -4.26795197 12.0041770935 0.97977811;
	setAttr -s 6 ".ed[0:5]"  4 0 0 0 1 0 1 3 0 2 5 0 3 2 0 4 5 0;
	setAttr -ch 6 ".fc[0]" -type "polyFaces" 
		f 6 -5 -3 -2 -1 5 -4
		mu 0 6 1 4 5 2 3 0;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_r_hi_eye_5_guide" -p "FM_Cam_r_hi_eye";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -6.2948510646820068 6.8777859210968018 0.97977828979492032 ;
	setAttr ".sp" -type "double3" -6.2948510646820068 6.8777859210968018 0.97977828979492032 ;
createNode mesh -n "FM_Cam_r_hi_eye_5_guideShape" -p "FM_Cam_r_hi_eye_5_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 6 ".uvst[0].uvsp[0:5]" -type "float2" 0.48261556 0.69141757
		 0.47568756 0.72177106 0.45848843 0.72095931 0.46523112 0.69141757 0.5 0.69141757
		 0.49288672 0.72258282;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 6 ".vt[0:5]"  -6.86765671 6.92534637 0.97977811 -6.29485035 6.41478729 0.97977811
		 -6.29485035 7.065929413 0.97977811 -6.86765671 7.6102562 0.97977811 -5.72204542 6.14531708 0.97977811
		 -5.72204542 6.85445786 0.97977811;
	setAttr -s 6 ".ed[0:5]"  0 1 0 1 4 0 3 0 0 3 2 0 2 5 0 5 4 0;
	setAttr -ch 6 ".fc[0]" -type "polyFaces" 
		f 6 1 -6 -5 -4 2 0
		mu 0 6 0 4 5 1 2 3;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_r_hi_eye_6_guide" -p "FM_Cam_r_hi_eye";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -4.9949986934661865 6.4741816520690918 0.97977828979492043 ;
	setAttr ".sp" -type "double3" -4.9949986934661865 6.4741816520690918 0.97977828979492043 ;
createNode mesh -n "FM_Cam_r_hi_eye_6_guideShape" -p "FM_Cam_r_hi_eye_6_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 6 ".uvst[0].uvsp[0:5]" -type "float2" 0.49288672 0.72258282
		 0.5 0.69141757 0.5 0.69141757 0.49288672 0.72258282 0.49288672 0.72258282 0.5 0.69141757;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 6 ".vt[0:5]"  -5.72204542 6.14531708 0.97977811 -4.26795197 6.14531708 0.97977811
		 -4.99499798 6.093906403 0.97977811 -5.72204542 6.85445786 0.97977811 -4.26795197 6.85445786 0.97977811
		 -4.99499798 6.77368164 0.97977811;
	setAttr -s 6 ".ed[0:5]"  3 0 0 4 1 0 1 2 0 2 0 0 4 5 0 5 3 0;
	setAttr -ch 6 ".fc[0]" -type "polyFaces" 
		f 6 -3 -2 4 5 0 -4
		mu 0 6 1 2 3 0 4 5;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_r_hi_eye_7_guide" -p "FM_Cam_r_hi_eye";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -3.6951465606689453 6.8777859210968018 0.97977828979492032 ;
	setAttr ".sp" -type "double3" -3.6951465606689453 6.8777859210968018 0.97977828979492032 ;
createNode mesh -n "FM_Cam_r_hi_eye_7_guideShape" -p "FM_Cam_r_hi_eye_7_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 6 ".uvst[0].uvsp[0:5]" -type "float2" 0.48261556 0.69141757
		 0.46523112 0.69141757 0.45848843 0.72095931 0.47568756 0.72177106 0.5 0.69141757
		 0.49288672 0.72258282;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 6 ".vt[0:5]"  -3.69514728 6.41478729 0.97977811 -3.12234116 6.92534637 0.97977811
		 -3.12234116 7.6102562 0.97977811 -3.69514728 7.065929413 0.97977811 -4.26795197 6.85445786 0.97977811
		 -4.26795197 6.14531708 0.97977811;
	setAttr -s 6 ".ed[0:5]"  2 1 0 1 0 0 0 5 0 2 3 0 3 4 0 4 5 0;
	setAttr -ch 6 ".fc[0]" -type "polyFaces" 
		f 6 -2 -1 3 4 5 -3
		mu 0 6 0 1 2 3 5 4;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "c_Rt_pupil_M_guide" -p "FM_Cam_r_hi_eye";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -4.9728034734725952 9.4398937225341797 1.1875686645507793 ;
	setAttr ".sp" -type "double3" -4.9728034734725952 9.4398937225341797 1.1875686645507793 ;
createNode mesh -n "c_Rt_pupil_M_guideShape" -p "c_Rt_pupil_M_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.6486026 0.89203393
		 0.62640893 0.93559146 0.59184146 0.97015893 0.54828387 0.9923526 0.5 1 0.4517161
		 0.9923526 0.40815854 0.97015893 0.37359107 0.93559146 0.3513974 0.89203393 0.34374997
		 0.84375 0.3513974 0.79546607 0.37359107 0.75190854 0.40815851 0.71734107 0.45171607
		 0.69514734 0.5 0.68749994 0.54828393 0.69514734 0.59184152 0.71734101 0.62640899
		 0.75190848 0.64860266 0.79546607 0.65625 0.84375;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".vt[0:19]"  -3.77631474 9.82865524 1.18756914 -3.95500898 10.17936325 1.18756914
		 -4.23333168 10.45768738 1.18756914 -4.58404064 10.63638306 1.18756914 -4.97280264 10.69795609 1.18756914
		 -5.36156464 10.63638306 1.18756914 -5.7122736 10.45768738 1.18756914 -5.99059629 10.17936325 1.18756914
		 -6.16929054 9.82865524 1.18756914 -6.230865 9.43989563 1.18756914 -6.16929054 9.051132202 1.18756914
		 -5.99059629 8.70042419 1.18756914 -5.71227217 8.42210007 1.18756914 -5.36156464 8.2434082 1.18756914
		 -4.97280264 8.18183136 1.18756914 -4.58404064 8.2434082 1.18756914 -4.23333311 8.42210007 1.18756914
		 -3.95500898 8.70042419 1.18756914 -3.77631474 9.051132202 1.18756914 -3.71474195 9.43989563 1.18756914;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 19 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		mu 0 20 19 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_r_hi_eye_9_guide" -p "FM_Cam_r_hi_eye";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -7.1296799182891846 9.4398946762084961 0.98765945434570102 ;
	setAttr ".sp" -type "double3" -7.1296799182891846 9.4398946762084961 0.98765945434570102 ;
createNode mesh -n "FM_Cam_r_hi_eye_9_guideShape" -p "FM_Cam_r_hi_eye_9_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 12 ".uvst[0].uvsp[0:11]" -type "float2" 0.5 1 0.4517161 0.9923526
		 0.5 0.83749998 0.40815854 0.97015893 0.37359107 0.93559146 0.3513974 0.89203393 0.34374997
		 0.84375 0.3513974 0.79546607 0.37359107 0.75190854 0.40815851 0.71734107 0.45171607
		 0.69514734 0.5 0.68749994;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 12 ".vt[0:11]"  -6.70020962 10.29883575 0.98765916 -6.96563625 10.25679398 0.98765916
		 -7.20508194 10.13479233 0.98765916 -7.39510632 9.944767 0.98765916 -7.51711082 9.70532227 0.98765916
		 -7.55915022 9.43989563 0.98765916 -7.51711082 9.17446899 0.98765916 -7.39510632 8.93502045 0.98765916
		 -7.20508194 8.74499893 0.98765916 -6.96563625 8.62299347 0.98765916 -6.70020962 8.58095551 0.98765916
		 -6.70020962 9.43989563 0.98765916;
	setAttr -s 12 ".ed[0:11]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 0 11 0 10 11 0;
	setAttr -ch 12 ".fc[0]" -type "polyFaces" 
		f 12 -11 0 1 2 3 4 5 6 7 8 9 11
		mu 0 12 2 0 1 3 4 5 6 7 8 9 10 11;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_r_hi_eye_10_guide" -p "FM_Cam_r_hi_eye";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -2.8802748918533325 9.4398946762084961 0.98765945434570102 ;
	setAttr ".sp" -type "double3" -2.8802748918533325 9.4398946762084961 0.98765945434570102 ;
createNode mesh -n "FM_Cam_r_hi_eye_10_guideShape" -p "FM_Cam_r_hi_eye_10_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 12 ".uvst[0].uvsp[0:11]" -type "float2" 0.6486026 0.89203393
		 0.62640893 0.93559146 0.5 0.83749998 0.59184146 0.97015893 0.54828387 0.9923526 0.5
		 1 0.5 0.68749994 0.54828393 0.69514734 0.59184152 0.71734101 0.62640899 0.75190848
		 0.64860266 0.79546607 0.65625 0.84375;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 12 ".vt[0:11]"  -2.48311949 9.71198273 0.98765916 -2.60818529 9.95743942 0.98765916
		 -2.80297995 10.15223312 0.98765916 -3.048435688 10.27730179 0.98765916 -3.32052469 10.32039642 0.98765916
		 -3.32052469 8.55939484 0.98765916 -3.048435688 8.60248947 0.98765916 -2.80297995 8.72755432 0.98765916
		 -2.60818529 8.92234802 0.98765916 -2.48311949 9.16780472 0.98765916 -2.44002509 9.43989563 0.98765916
		 -3.32052469 9.43989563 0.98765916;
	setAttr -s 12 ".ed[0:11]"  0 1 0 1 2 0 2 3 0 3 4 0 5 6 0 6 7 0 7 8 0
		 8 9 0 9 10 0 10 0 0 4 11 0 5 11 0;
	setAttr -ch 12 ".fc[0]" -type "polyFaces" 
		f 12 -12 4 5 6 7 8 9 0 1 2 3 10
		mu 0 12 2 6 7 8 9 10 11 0 1 3 4 5;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_r_hi_eye_11_guide" -p "FM_Cam_r_hi_eye";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -7.780555248260498 7.9531514644622803 0.9506950378417951 ;
	setAttr ".sp" -type "double3" -7.780555248260498 7.9531514644622803 0.9506950378417951 ;
createNode mesh -n "FM_Cam_r_hi_eye_11_guideShape" -p "FM_Cam_r_hi_eye_11_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 4 ".uvst[0].uvsp[0:3]" -type "float2" 0.375 0.25 0.625
		 0.25 0.625 0.5 0.375 0.5;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 4 ".pt[0:3]" -type "float3"  0 -27.812107 0 0 -27.812107 
		-9.5367432e-007 0 -27.812107 0 0 -27.812107 -9.5367432e-007;
	setAttr -s 4 ".vt[0:3]"  -8.18460369 35.86001587 0.95069551 -7.41202259 35.57442474 0.95069551
		 -8.14908791 35.95609283 0.95069551 -7.37650681 35.67050171 0.95069551;
	setAttr -s 4 ".ed[0:3]"  0 1 0 2 3 0 0 2 0 1 3 0;
	setAttr -ch 4 ".fc[0]" -type "polyFaces" 
		f 4 0 3 -2 -3
		mu 0 4 0 1 2 3;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "c_Rt_eyeStretch_CTRL_guide" -p "FM_Cam_r_hi_eye";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -7.9785752296447754 7.4407000541687012 0.95069503784179521 ;
	setAttr ".sp" -type "double3" -7.9785752296447754 7.4407000541687012 0.95069503784179521 ;
createNode mesh -n "c_Rt_eyeStretch_CTRL_guideShape" -p "c_Rt_eyeStretch_CTRL_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 7 ".uvst[0].uvsp[0:6]" -type "float2" 0.375 0.25 0.53125
		 0.4375 0.875 0 0.875 1 0.375 0.25 0.40625 0.25 0.875 1;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 7 ".vt[0:6]"  -8.42162704 7.566082 0.95069456 -7.81805897 7.89860916 0.95069456
		 -8.31841183 7.12900162 0.95069456 -8.1974268 7.49119186 0.95069456 -7.53552341 7.2700882 0.95069456
		 -7.75972652 7.34497833 0.95069456 -7.88070917 6.9827919 0.95069504;
	setAttr -s 7 ".ed[0:6]"  0 3 0 0 1 0 2 3 0 4 5 0 4 1 0 6 5 0 6 2 0;
	setAttr -ch 7 ".fc[0]" -type "polyFaces" 
		f 7 -2 0 -3 -7 5 -4 4
		mu 0 7 1 0 2 3 6 5 4;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "c_Rt_eye_M_guide" -p "FM_Cam_r_hi_eye";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -4.9949989318847656 9.4019908905029297 1.0307197570800761 ;
	setAttr ".sp" -type "double3" -4.9949989318847656 9.4019908905029297 1.0307197570800761 ;
createNode mesh -n "c_Rt_eye_M_guideShape" -p "c_Rt_eye_M_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.47029039 0.74541754
		 0.43129694 0.91625899 0.41528496 0.91024578 0.45323563 0.74397337 0.48734522 0.7468617
		 0.4473089 0.92227226 0.4473089 0.92227226 0.48734522 0.7468617 0.4473089 0.92227226
		 0.48734522 0.7468617 0.47029039 0.74541754 0.43129694 0.91625899 0.45323563 0.74397337
		 0.41528496 0.91024578;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 3 ".pt";
	setAttr ".pt[3]" -type "float3" 1.4156103e-007 -4.7683716e-007 -4.7683716e-007 ;
	setAttr -s 14 ".vt[0:13]"  -6.86765671 10.30266953 1.030719876 -6.29484892 10.99899292 1.030719876
		 -5.72204542 11.31653976 1.030719876 -4.99499798 11.48084641 1.030719876 -4.26795197 11.31653976 1.030719876
		 -3.69514728 10.99899292 1.030719876 -3.12234116 10.30266953 1.030719876 -6.86765671 8.55427551 1.030719876
		 -6.29485035 7.81225586 1.030719876 -5.72204542 7.48860931 1.030719876 -4.99499798 7.32313538 1.030719876
		 -4.26795197 7.48860931 1.030719876 -3.69514728 7.81225586 1.030719876 -3.12234116 8.55427551 1.030719876;
	setAttr -s 14 ".ed[0:13]"  0 7 0 0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 6 13 0
		 5 6 0 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0;
	setAttr -ch 14 ".fc[0]" -type "polyFaces" 
		f 14 13 -7 -8 -6 -5 -4 -3 -2 0 8 9 10 11 12
		mu 0 14 10 12 13 11 8 6 5 1 2 3 0 4 7 9;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_r_hi_eye_14_guide" -p "FM_Cam_r_hi_eye";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -6.2948510646820068 7.7043659687042236 0.97977828979492021 ;
	setAttr ".sp" -type "double3" -6.2948510646820068 7.7043659687042236 0.97977828979492021 ;
createNode mesh -n "FM_Cam_r_hi_eye_14_guideShape" -p "FM_Cam_r_hi_eye_14_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 6 ".uvst[0].uvsp[0:5]" -type "float2" 0.47568756 0.72177106
		 0.47029039 0.74541754 0.45323563 0.74397337 0.45848843 0.72095931 0.49288672 0.72258282
		 0.48734522 0.7468617;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 6 ".vt[0:5]"  -6.86765671 7.6102562 0.97977811 -6.29485035 7.065929413 0.97977811
		 -6.29485035 7.81225586 0.97977811 -6.86765671 8.55427551 0.97977811 -5.72204542 6.85445786 0.97977811
		 -5.72204542 7.48860931 0.97977811;
	setAttr -s 6 ".ed[0:5]"  0 1 0 1 4 0 3 0 0 3 2 0 2 5 0 5 4 0;
	setAttr -ch 6 ".fc[0]" -type "polyFaces" 
		f 6 1 -6 -5 -4 2 0
		mu 0 6 0 4 5 1 2 3;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_r_hi_eye_15_guide" -p "FM_Cam_r_hi_eye";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -4.9949986934661865 7.1311447620391846 0.97977828979492032 ;
	setAttr ".sp" -type "double3" -4.9949986934661865 7.1311447620391846 0.97977828979492032 ;
createNode mesh -n "FM_Cam_r_hi_eye_15_guideShape" -p "FM_Cam_r_hi_eye_15_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 6 ".uvst[0].uvsp[0:5]" -type "float2" 0.48734522 0.7468617
		 0.48734522 0.7468617 0.49288672 0.72258282 0.49288672 0.72258282 0.48734522 0.7468617
		 0.49288672 0.72258282;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 6 ".vt[0:5]"  -5.72204542 6.85445786 0.97977811 -4.26795197 6.85445786 0.97977811
		 -4.99499798 6.77368164 0.97977811 -5.72204542 7.48860931 0.97977811 -4.99499798 7.32313538 0.97977811
		 -4.26795197 7.48860931 0.97977811;
	setAttr -s 6 ".ed[0:5]"  1 2 0 2 0 0 3 0 0 5 1 0 3 4 0 4 5 0;
	setAttr -ch 6 ".fc[0]" -type "polyFaces" 
		f 6 -1 -4 -6 -5 2 -2
		mu 0 6 3 5 4 0 1 2;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_r_hi_eye_16_guide" -p "FM_Cam_r_hi_eye";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -3.6951465606689453 7.7043659687042236 0.97977828979492021 ;
	setAttr ".sp" -type "double3" -3.6951465606689453 7.7043659687042236 0.97977828979492021 ;
createNode mesh -n "FM_Cam_r_hi_eye_16_guideShape" -p "FM_Cam_r_hi_eye_16_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 6 ".uvst[0].uvsp[0:5]" -type "float2" 0.49288672 0.72258282
		 0.47568756 0.72177106 0.47029039 0.74541754 0.48734522 0.7468617 0.45848843 0.72095931
		 0.45323563 0.74397337;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 6 ".vt[0:5]"  -3.69514728 7.065929413 0.97977811 -3.12234116 7.6102562 0.97977811
		 -3.69514728 7.81225586 0.97977811 -3.12234116 8.55427551 0.97977811 -4.26795197 7.48860931 0.97977811
		 -4.26795197 6.85445786 0.97977811;
	setAttr -s 6 ".ed[0:5]"  1 0 0 0 5 0 3 1 0 4 2 0 2 3 0 4 5 0;
	setAttr -ch 6 ".fc[0]" -type "polyFaces" 
		f 6 -1 -3 -5 -4 5 -2
		mu 0 6 1 4 5 2 3 0;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_r_hi_eye_17_guide" -p "FM_Cam_r_hi_eye";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -4.9949986934661865 11.700579643249512 0.97977828979491932 ;
	setAttr ".sp" -type "double3" -4.9949986934661865 11.700579643249512 0.97977828979491932 ;
createNode mesh -n "FM_Cam_r_hi_eye_17_guideShape" -p "FM_Cam_r_hi_eye_17_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 6 ".uvst[0].uvsp[0:5]" -type "float2" 0.44123089 0.94890189
		 0.4473089 0.92227226 0.4473089 0.92227226 0.44123089 0.94890189 0.44123089 0.94890189
		 0.4473089 0.92227226;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 6 ".vt[0:5]"  -5.72204542 12.0041770935 0.97977811 -4.26795197 12.0041770935 0.97977811
		 -4.99499798 12.084621429 0.97977811 -5.72204542 11.31653976 0.97977811 -4.99499798 11.48084641 0.97977811
		 -4.26795197 11.31653976 0.97977811;
	setAttr -s 6 ".ed[0:5]"  0 3 0 1 2 0 1 5 0 2 0 0 4 5 0 3 4 0;
	setAttr -ch 6 ".fc[0]" -type "polyFaces" 
		f 6 4 -3 1 3 0 5
		mu 0 6 1 2 3 0 4 5;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_r_hi_eye_18_guide" -p "FM_Cam_r_hi_eye";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -3.6951465606689453 11.153422355651855 0.97977828979491943 ;
	setAttr ".sp" -type "double3" -3.6951465606689453 11.153422355651855 0.97977828979491943 ;
createNode mesh -n "FM_Cam_r_hi_eye_18_guideShape" -p "FM_Cam_r_hi_eye_18_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 6 ".uvst[0].uvsp[0:5]" -type "float2" 0.43129694 0.91625899
		 0.41528496 0.91024578 0.40952355 0.93548816 0.42537722 0.942195 0.4473089 0.92227226
		 0.44123089 0.94890189;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 6 ".vt[0:5]"  -3.69514728 11.79443741 0.97977811 -3.12234116 11.28486252 0.97977811
		 -3.69514728 10.99899292 0.97977811 -3.12234116 10.30266953 0.97977811 -4.26795197 12.0041770935 0.97977811
		 -4.26795197 11.31653976 0.97977811;
	setAttr -s 6 ".ed[0:5]"  0 4 0 1 0 0 1 3 0 2 3 0 5 2 0 4 5 0;
	setAttr -ch 6 ".fc[0]" -type "polyFaces" 
		f 6 3 -3 1 0 5 4
		mu 0 6 0 1 2 3 5 4;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_r_hi_eye_19_guide" -p "FM_Cam_r_hi_eye";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -6.2948510646820068 11.153422355651855 0.97977828979491943 ;
	setAttr ".sp" -type "double3" -6.2948510646820068 11.153422355651855 0.97977828979491943 ;
createNode mesh -n "FM_Cam_r_hi_eye_19_guideShape" -p "FM_Cam_r_hi_eye_19_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 6 ".uvst[0].uvsp[0:5]" -type "float2" 0.43129694 0.91625899
		 0.42537722 0.942195 0.40952355 0.93548816 0.41528496 0.91024578 0.4473089 0.92227226
		 0.44123089 0.94890189;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 6 ".vt[0:5]"  -6.86765671 11.28486252 0.97977811 -6.29485035 11.79443741 0.97977811
		 -6.86765671 10.30266953 0.97977811 -6.29484892 10.99899292 0.97977811 -5.72204542 11.31653976 0.97977811
		 -5.72204542 12.0041770935 0.97977811;
	setAttr -s 6 ".ed[0:5]"  0 2 0 0 1 0 1 5 0 2 3 0 3 4 0 5 4 0;
	setAttr -ch 6 ".fc[0]" -type "polyFaces" 
		f 6 4 -6 -3 -2 0 3
		mu 0 6 0 4 5 1 2 3;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "c_Rt_spec_M_guide" -p "FM_Cam_r_hi_eye";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -4.9450905323028564 9.4121818542480469 1.2605628967285136 ;
	setAttr ".sp" -type "double3" -4.9450905323028564 9.4121818542480469 1.2605628967285136 ;
createNode mesh -n "c_Rt_spec_M_guideShape" -p "c_Rt_spec_M_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 34 ".uvst[0].uvsp[0:33]" -type "float2" 0.6486026 0.89203393
		 0.62640893 0.93559146 0.59184146 0.97015893 0.54828387 0.9923526 0.5 1 0.5 1 0.34374997
		 0.84375 0.3513974 0.79546607 0.34374997 0.84375 0.37359107 0.75190854 0.40815851
		 0.71734107 0.45171607 0.69514734 0.5 0.68749994 0.54828393 0.69514734 0.59184152
		 0.71734101 0.62640899 0.75190848 0.64860266 0.79546607 0.65625 0.84375 0.5 1 0.54828387
		 0.9923526 0.59184146 0.97015893 0.62640893 0.93559146 0.6486026 0.89203393 0.65625
		 0.84375 0.64860266 0.79546607 0.62640899 0.75190848 0.59184152 0.71734101 0.54828393
		 0.69514734 0.5 0.68749994 0.45171607 0.69514734 0.40815851 0.71734107 0.37359107
		 0.75190854 0.3513974 0.79546607 0.34374997 0.84375;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 34 ".vt[0:33]"  -3.89579153 9.78983688 1.26056302 -4.056643009 10.10552216 1.26056302
		 -4.47654724 9.80044174 1.26056302 -4.38941813 9.62944794 1.26056302 -4.30717325 10.3560524 1.26056302
		 -4.61225128 9.9361496 1.26056302 -4.62286139 10.51690674 1.26056302 -4.78325081 10.023281097 1.26056302
		 -4.83555126 10.47976303 1.26056302 -4.95365143 10.15863419 1.26056302 -6.041401386 9.29626083 1.26056302
		 -6.049814224 9.089954376 1.26056302 -5.55618572 9.25033951 1.26056302 -5.65324163 9.36648178 1.26056302
		 -5.8889637 8.77426529 1.26056302 -5.46905994 9.079341888 1.26056302 -5.63843203 8.52373505 1.26056302
		 -5.33335447 8.94363785 1.26056302 -5.32274389 8.36288071 1.26056302 -5.1623559 8.85651016 1.26056302
		 -4.97280264 8.30745697 1.26056302 -4.97280264 8.82648849 1.26056302 -4.62286139 8.36288071 1.26056302
		 -4.78325081 8.85651016 1.26056302 -4.30717325 8.52373505 1.26056302 -4.61225128 8.94363785 1.26056302
		 -4.056643009 8.77426529 1.26056302 -4.47654724 9.079341888 1.26056302 -3.89579153 9.089954376 1.26056302
		 -4.38941813 9.25033951 1.26056302 -3.84036684 9.43989563 1.26056302 -4.35939598 9.43989563 1.26056302
		 -4.97280264 10.32877731 1.26056302 -5.84572506 9.41755295 1.26056302;
	setAttr -s 34 ".ed[0:33]"  0 1 0 3 2 0 1 4 0 2 5 0 4 6 0 5 7 0 6 8 0
		 8 32 0 7 9 0 10 11 0 13 12 0 10 33 0 11 14 0 12 15 0 14 16 0 15 17 0 16 18 0 17 19 0
		 18 20 0 19 21 0 20 22 0 21 23 0 22 24 0 23 25 0 24 26 0 25 27 0 26 28 0 27 29 0 28 30 0
		 29 31 0 30 0 0 31 3 0 32 9 0 33 13 0;
	setAttr -ch 34 ".fc[0]" -type "polyFaces" 
		f 34 -11 -34 -12 9 12 14 16 18 20 22 24 26 28 30 0 2 4 6 7 32 -9 -6 -4 -2 -32 -30 -28
		 -26 -24 -22 -20 -18 -16 -14
		mu 0 34 32 33 8 6 7 9 10 11 12 13 14 15 16 17 0 1 2 3 4 5 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "c_Rt_dn_eyelids_CTRL_guide" -p "FM_Cam_r_hi_eye";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -1.8435989618301392 7.2884385585784912 1.0385551452636703 ;
	setAttr ".sp" -type "double3" -1.8435989618301392 7.2884385585784912 1.0385551452636703 ;
createNode mesh -n "c_Rt_dn_eyelids_CTRL_guideShape" -p "c_Rt_dn_eyelids_CTRL_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 12 ".uvst[0].uvsp[0:11]" -type "float2" 0.375 0.25 0.38149059
		 0.25778872 0.875 0 0.875 1 0.51945782 0.42334932 0.75 1 0.875 1 0.51944202 0.42333046
		 0.53125 0.4375 0.38168237 0.25801882 0.40625 0.25 0.375 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 12 ".vt[0:11]"  -1.29883885 7.98371124 1.038554668 -1.8473053 6.22903061 1.038555145
		 -1.84307814 8.34727478 1.038555622 -1.54868436 8.34670258 1.038555622 -1.54938936 7.98419952 1.038554668
		 -2.38873291 7.98583221 1.038554668 -2.13818789 7.98534393 1.038554668 -2.13748288 8.34784698 1.038555622
		 -1.76532483 6.28778839 1.038555145 -1.92897606 6.28793716 1.038555145 -1.23756909 7.90819168 1.038554668
		 -2.44962883 7.90831757 1.038554668;
	setAttr -s 12 ".ed[0:11]"  0 10 0 3 2 0 3 4 0 5 6 0 5 11 0 7 6 0 7 2 0
		 0 4 0 8 1 0 9 1 0 10 8 0 11 9 0;
	setAttr -ch 12 ".fc[0]" -type "polyFaces" 
		f 12 -1 7 -3 1 -7 5 -4 4 11 9 -9 -11
		mu 0 12 1 0 2 3 5 6 10 11 9 4 8 7;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "c_Rt_up_eyelids_CTRL_guide" -p "FM_Cam_r_hi_eye";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -1.8376375436782837 11.592889785766602 1.0385551452636692 ;
	setAttr ".sp" -type "double3" -1.8376375436782837 11.592889785766602 1.0385551452636692 ;
createNode mesh -n "c_Rt_up_eyelids_CTRL_guideShape" -p "c_Rt_up_eyelids_CTRL_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 12 ".uvst[0].uvsp[0:11]" -type "float2" 0.375 0.25 0.38149059
		 0.25778872 0.40625 0.25 0.75 1 0.875 1 0.51945782 0.42334932 0.53125 0.4375 0.875
		 0 0.875 1 0.51944202 0.42333046 0.38168237 0.25801882 0.375 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 12 ".vt[0:11]"  -1.29317784 10.89549637 1.038555622 -1.83481097 12.65229797 1.038555622
		 -1.83882713 10.5340538 1.038555622 -1.54443049 10.5334816 1.038555622 -1.54372549 10.89598465 1.038555622
		 -2.38306928 10.89761734 1.038555622 -2.13252401 10.89712906 1.038555622 -2.13322902 10.53462601 1.038555622
		 -1.75306273 12.59321976 1.038555622 -1.91671133 12.59371185 1.038555622 -1.23161173 10.97077942 1.038555622
		 -2.44366336 10.9753685 1.038555622;
	setAttr -s 12 ".ed[0:11]"  0 10 0 3 2 0 3 4 0 5 6 0 5 11 0 7 6 0 7 2 0
		 0 4 0 8 1 0 9 1 0 10 8 0 11 9 0;
	setAttr -ch 12 ".fc[0]" -type "polyFaces" 
		f 12 10 8 -10 -12 -5 3 -6 6 -2 2 -8 0
		mu 0 12 1 9 6 5 10 11 7 8 3 4 2 0;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "c_Rt_eyelids_CTRL_guide" -p "FM_Cam_r_hi_eye";
	setAttr ".s" -type "double3" 1 0.99999999999999956 0.99999999999999978 ;
	setAttr ".rp" -type "double3" -8.2244703769683838 10.717866897583002 1.035184860229492 ;
	setAttr ".sp" -type "double3" -8.2244703769683838 10.717866897583008 1.0351848602294922 ;
	setAttr ".spt" -type "double3" 0 -5.329070518200749e-015 -2.2204460492503126e-016 ;
createNode mesh -n "c_Rt_eyelids_CTRL_guideShape" -p "c_Rt_eyelids_CTRL_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0 0 0.25 0 0.5 0
		 0.75 0 0 0.25 0 0.5 1 0.5 0 0.75 1 0.75 0 1 0.25 1 0.5 1 0.75 1 1 1;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 14 ".vt[0:13]"  -9.18255424 10.26820755 1.035186768 -9.071238518 9.49691772 1.035182953
		 -8.7058506 8.9657402 1.035186768 -8.44170856 8.88540649 1.035182953 -9.15799618 11.03950119 1.035186768
		 -8.80347252 11.73529434 1.035186768 -8.48073387 9.6998558 1.035186768 -8.19880199 12.26578903 1.035186768
		 -8.39330006 10.26377487 1.035186768 -7.37735701 12.5503273 1.035186768 -7.26638651 12.44075394 1.035186768
		 -7.75626707 11.83792496 1.035186768 -8.088612556 11.19745255 1.035186768 -8.25441742 10.75442123 1.035186768;
	setAttr -s 14 ".ed[0:13]"  0 1 0 0 4 0 1 2 0 2 3 0 4 5 0 3 6 0 5 7 0
		 6 8 0 7 9 0 8 13 0 9 10 0 10 11 0 11 12 0 12 13 0;
	setAttr -ch 14 ".fc[0]" -type "polyFaces" 
		f 14 9 -14 -13 -12 -11 -9 -7 -5 -2 0 2 3 5 7
		mu 0 14 8 13 12 11 10 9 7 5 4 0 1 2 3 6;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_hi_eye" -p "FM_Cam_c_hi_face";
	setAttr ".rp" -type "double3" 0.069305896759033203 9.5477485656738281 1.1787338256835937 ;
	setAttr ".sp" -type "double3" 0.069305896759033203 9.5477485656738281 1.1787338256835937 ;
createNode transform -n "c_eye_M_guide" -p "FM_Cam_hi_eye";
createNode mesh -n "c_eye_M_guideShape" -p "c_eye_M_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.71472525596618652 0.17261371109634638 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.94922078 0.17261374
		 0.93774378 0.21810468 0.90443617 0.25914261 0.85255831 0.2917105 0.78718829 0.3126204
		 0.71472526 0.31982541 0.64226222 0.3126204 0.5768922 0.2917105 0.52501434 0.25914261
		 0.49170673 0.21810468 0.48022974 0.17261374 0.49170673 0.1271228 0.52501434 0.086084872
		 0.5768922 0.053516973 0.6422621 0.032607038 0.71472526 0.025402011 0.78718841 0.032607038
		 0.85255837 0.053516913 0.90443629 0.08608482 0.9377439 0.1271228;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 20 ".vt[0:19]"  1.1424365 9.77432632 1.1008873 0.9821651 9.97872925 1.1008873
		 0.73253715 10.14094162 1.1008873 0.41798711 10.24509048 1.1008873 0.069305874 10.28097534 1.1008873
		 -0.27937534 10.24509048 1.1008873 -0.5939253 10.14094162 1.1008873 -0.84355307 9.97872925 1.1008873
		 -1.0038241148 9.77432632 1.1008873 -1.059049368 9.54774857 1.1008873 -1.0038241148 9.32116699 1.1008873
		 -0.84355283 9.11676788 1.1008873 -0.59392524 8.95455551 1.1008873 -0.27937523 8.85040665 1.1008873
		 0.069305837 8.81452179 1.1008873 0.41798687 8.85040665 1.1008873 0.73253649 8.95455551 1.1008873
		 0.98216438 9.11676788 1.1008873 1.14243555 9.32116699 1.1008873 1.19766116 9.54774857 1.1008873;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 19 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_r_hi_brow" -p "FM_Cam_c_hi_face";
	setAttr ".rp" -type "double3" -5.21343994140625 15.377712249755859 1.018184661865231 ;
	setAttr ".sp" -type "double3" -5.21343994140625 15.377712249755859 1.018184661865231 ;
createNode transform -n "c_Rt_eyebrows_CTRL_backgroundColor_" -p "FM_Cam_r_hi_brow";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr ".ove" yes;
	setAttr ".rp" -type "double3" -4.4629273414611816 15.377712249755859 0.94457244873046531 ;
	setAttr ".sp" -type "double3" -4.4629273414611816 15.377712249755859 0.94457244873046531 ;
createNode mesh -n "c_Rt_eyebrows_CTRL_backgroundColor_Shape" -p "c_Rt_eyebrows_CTRL_backgroundColor_";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 8 ".uvst[0].uvsp[0:7]" -type "float2" 0.375 0.22500245
		 0.625 0.22500245 0.61284238 0.25 0.38715762 0.24999999 0.375 0.024997517 0.625 0.024997562
		 0.38715762 -7.4505806e-009 0.61284238 0;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 8 ".vt[0:7]"  -7.69092655 16.73395157 0.94457269 -7.55321693 16.91597366 0.94457269
		 -1.37263751 16.91597366 0.94457269 -1.23492813 16.73395157 0.94457269 -7.55321693 13.83945084 0.94457269
		 -7.69092655 14.021476746 0.94457269 -1.23492813 14.021476746 0.94457269 -1.37263751 13.83945084 0.94457269;
	setAttr -s 8 ".ed[0:7]"  1 2 0 1 0 0 3 2 0 4 7 0 5 0 0 4 5 0 6 3 0
		 7 6 0;
	setAttr -ch 8 ".fc[0]" -type "polyFaces" 
		f 8 2 -1 1 -5 -6 3 7 6
		mu 0 8 1 2 3 0 4 6 7 5;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "c_Rt_eyebrows_01_CTRL_guide" -p "FM_Cam_r_hi_brow";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -2.5988919734954834 15.499760150909424 1.0917968749999967 ;
	setAttr ".sp" -type "double3" -2.5988919734954834 15.499760150909424 1.0917968749999967 ;
createNode mesh -n "c_Rt_eyebrows_01_CTRL_guideShape" -p "c_Rt_eyebrows_01_CTRL_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 8 ".uvst[0].uvsp[0:7]" -type "float2" 0.5625 0.024997551
		 0.55642116 -1.8626451e-009 0.61284238 0 0.625 0.024997562 0.5625 0.22500245 0.625
		 0.22500245 0.55642116 0.25 0.61284238 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 8 ".vt[0:7]"  -2.015808582 15.95059967 1.091796041 -1.94069338 15.89101791 1.091796041
		 -1.94069338 15.0031166077 1.091796041 -2.015808582 14.94353485 1.091796041 -3.25709057 15.048923492 1.091796041
		 -3.21953297 15.10850525 1.091796041 -3.21953297 15.99640274 1.091796041 -3.25709057 16.055986404 1.091796041;
	setAttr -s 8 ".ed[0:7]"  1 0 0 2 1 0 3 2 0 4 3 0 4 5 0 5 6 0 7 0 0
		 6 7 0;
	setAttr -ch 8 ".fc[0]" -type "polyFaces" 
		f 8 0 -7 -8 -6 -5 3 2 1
		mu 0 8 5 7 6 4 0 1 2 3;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "c_Rt_eyebrows_02_CTRL_guide" -p "FM_Cam_r_hi_brow";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -3.8589527606964111 15.700954914093018 1.0917968749999964 ;
	setAttr ".sp" -type "double3" -3.8589527606964111 15.700954914093018 1.0917968749999964 ;
createNode mesh -n "c_Rt_eyebrows_02_CTRL_guideShape" -p "c_Rt_eyebrows_02_CTRL_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 8 ".uvst[0].uvsp[0:7]" -type "float2" 0.5 0.22500245 0.5625
		 0.22500245 0.55642116 0.25 0.5 0.25 0.5 0.02499754 0.5625 0.024997551 0.5 -3.7252903e-009
		 0.55642116 -1.8626451e-009;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 8 ".vt[0:7]"  -4.49837255 16.35298729 1.091796041 -4.49837255 16.29340553 1.091796041
		 -4.49837255 15.40550613 1.091796041 -4.49837255 15.34592056 1.091796041 -3.21953297 15.99640274 1.091796041
		 -3.25709057 16.055986404 1.091796041 -3.21953297 15.10850525 1.091796041 -3.25709057 15.048923492 1.091796041;
	setAttr -s 8 ".ed[0:7]"  0 5 0 0 1 0 1 2 0 3 7 0 2 3 0 4 5 0 6 4 0
		 7 6 0;
	setAttr -ch 8 ".fc[0]" -type "polyFaces" 
		f 8 6 5 -1 1 2 4 3 7
		mu 0 8 5 1 2 3 0 4 6 7;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "c_Rt_eyebrows_03_CTRL_guide" -p "FM_Cam_r_hi_brow";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -5.777212381362915 15.902149677276611 1.0917968749999964 ;
	setAttr ".sp" -type "double3" -5.777212381362915 15.902149677276611 1.0917968749999964 ;
createNode mesh -n "c_Rt_eyebrows_03_CTRL_guideShape" -p "c_Rt_eyebrows_03_CTRL_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 10 ".uvst[0].uvsp[0:9]" -type "float2" 0.5 0.22500245 0.5
		 0.25 0.44357881 0.25 0.5 0.02499754 0.44357881 -5.5879354e-009 0.5 -3.7252903e-009
		 0.375 0.22500245 0.38715762 0.24999999 0.375 0.024997517 0.38715762 -7.4505806e-009;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 10 ".vt[0:9]"  -7.056052208 16.29340553 1.091796041 -6.98093939 16.35298729 1.091796041
		 -6.98093939 15.34592056 1.091796041 -7.056052208 15.40550613 1.091796041 -5.73965597 16.45837975 1.091796041
		 -5.73965597 15.4513092 1.091796041 -4.49837255 16.29340553 1.091796041 -4.49837255 16.35298729 1.091796041
		 -4.49837255 15.40550613 1.091796041 -4.49837255 15.34592056 1.091796041;
	setAttr -s 10 ".ed[0:9]"  1 4 0 1 0 0 2 5 0 3 0 0 2 3 0 4 7 0 5 9 0
		 7 6 0 6 8 0 8 9 0;
	setAttr -ch 10 ".fc[0]" -type "polyFaces" 
		f 10 -9 -8 -6 -1 1 -4 -5 2 6 -10
		mu 0 10 3 0 1 2 7 6 8 9 4 5;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "c_Rt_eyebrows_CTRL_guide" -p "FM_Cam_r_hi_brow";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -8.5859255790710449 15.336277961730957 1.0385551452636685 ;
	setAttr ".sp" -type "double3" -8.5859255790710449 15.336277961730957 1.0385551452636685 ;
createNode mesh -n "c_Rt_eyebrows_CTRL_guideShape" -p "c_Rt_eyebrows_CTRL_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 12 ".uvst[0].uvsp[0:11]" -type "float2" 0.375 0.25 0.38149059
		 0.25778872 0.40625 0.25 0.75 1 0.875 1 0.51945782 0.42334932 0.53125 0.4375 0.875
		 0 0.875 1 0.51944202 0.42333046 0.38168237 0.25801882 0.375 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 12 ".vt[0:11]"  -8.041464806 14.6388855 1.038555622 -8.58309937 16.3956852 1.038554668
		 -8.58711338 14.27744675 1.038555622 -8.29271889 14.27687073 1.038555622 -8.29201317 14.63937759 1.038555622
		 -9.13135719 14.64100647 1.038555622 -8.88081169 14.640522 1.038555622 -8.88151741 14.27801514 1.038555622
		 -8.50134945 16.33660316 1.038554668 -8.66499901 16.33709908 1.038554668 -7.97989941 14.71416855 1.038555622
		 -9.19195175 14.71875381 1.038555622;
	setAttr -s 12 ".ed[0:11]"  0 10 0 3 2 0 3 4 0 5 6 0 5 11 0 7 6 0 7 2 0
		 0 4 0 8 1 0 9 1 0 10 8 0 11 9 0;
	setAttr -ch 12 ".fc[0]" -type "polyFaces" 
		f 12 10 8 -10 -12 -5 3 -6 6 -2 2 -8 0
		mu 0 12 1 9 6 5 10 11 7 8 3 4 2 0;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "c_Rt_brows_01_CTRL_guide" -p "FM_Cam_r_hi_brow";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -2.8428341150283813 14.391452789306641 0.99995803833007491 ;
	setAttr ".sp" -type "double3" -2.8428341150283813 14.391452789306641 0.99995803833007491 ;
createNode mesh -n "c_Rt_brows_01_CTRL_guideShape" -p "c_Rt_brows_01_CTRL_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 4 ".uvst[0].uvsp[0:3]" -type "float2" 0.375 0 0.625 0 0.625
		 0.25 0.375 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 4 ".pt[0:3]" -type "float3"  0 -27.812107 9.5367432e-007 
		0 -27.812107 9.5367432e-007 0 -27.812107 9.5367432e-007 0 -27.812107 9.5367432e-007;
	setAttr -s 4 ".vt[0:3]"  -3.09482789 41.88209534 0.99995744 -2.59084034 41.88209534 0.99995744
		 -3.09482789 42.52502441 0.99995744 -2.59084034 42.52502441 0.99995744;
	setAttr -s 4 ".ed[0:3]"  0 1 0 2 3 0 0 2 0 1 3 0;
	setAttr -ch 4 ".fc[0]" -type "polyFaces" 
		f 4 0 3 -2 -3
		mu 0 4 0 1 2 3;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "c_Rt_brows_02_CTRL_guide" -p "FM_Cam_r_hi_brow";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -3.668975830078125 14.391452789306641 0.99995803833007491 ;
	setAttr ".sp" -type "double3" -3.668975830078125 14.391452789306641 0.99995803833007491 ;
createNode mesh -n "c_Rt_brows_02_CTRL_guideShape" -p "c_Rt_brows_02_CTRL_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 4 ".uvst[0].uvsp[0:3]" -type "float2" 0.375 0 0.625 0 0.625
		 0.25 0.375 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 4 ".pt[0:3]" -type "float3"  0 -27.812107 9.5367432e-007 
		0 -27.812107 9.5367432e-007 0 -27.812107 9.5367432e-007 0 -27.812107 9.5367432e-007;
	setAttr -s 4 ".vt[0:3]"  -3.92096949 41.88209534 0.99995744 -3.41698217 41.88209534 0.99995744
		 -3.92096949 42.52502441 0.99995744 -3.41698217 42.52502441 0.99995744;
	setAttr -s 4 ".ed[0:3]"  0 1 0 2 3 0 0 2 0 1 3 0;
	setAttr -ch 4 ".fc[0]" -type "polyFaces" 
		f 4 0 3 -2 -3
		mu 0 4 0 1 2 3;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "c_Rt_brows_03_CTRL_guide" -p "FM_Cam_r_hi_brow";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -4.4870972633361816 14.391452789306641 0.99995803833007491 ;
	setAttr ".sp" -type "double3" -4.4870972633361816 14.391452789306641 0.99995803833007491 ;
createNode mesh -n "c_Rt_brows_03_CTRL_guideShape" -p "c_Rt_brows_03_CTRL_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 4 ".uvst[0].uvsp[0:3]" -type "float2" 0.375 0 0.625 0 0.625
		 0.25 0.375 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 4 ".pt[0:3]" -type "float3"  0 -27.812107 9.5367432e-007 
		0 -27.812107 9.5367432e-007 0 -27.812107 9.5367432e-007 0 -27.812107 9.5367432e-007;
	setAttr -s 4 ".vt[0:3]"  -4.73909092 41.88209534 0.99995744 -4.23510361 41.88209534 0.99995744
		 -4.73909092 42.52502441 0.99995744 -4.23510361 42.52502441 0.99995744;
	setAttr -s 4 ".ed[0:3]"  0 1 0 2 3 0 0 2 0 1 3 0;
	setAttr -ch 4 ".fc[0]" -type "polyFaces" 
		f 4 0 3 -2 -3
		mu 0 4 0 1 2 3;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "c_Rt_brows_04_CTRL_guide" -p "FM_Cam_r_hi_brow";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -5.2570936679840088 14.391452789306641 0.99995803833007491 ;
	setAttr ".sp" -type "double3" -5.2570936679840088 14.391452789306641 0.99995803833007491 ;
createNode mesh -n "c_Rt_brows_04_CTRL_guideShape" -p "c_Rt_brows_04_CTRL_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 4 ".uvst[0].uvsp[0:3]" -type "float2" 0.375 0 0.625 0 0.625
		 0.25 0.375 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 4 ".pt[0:3]" -type "float3"  0 -27.812107 9.5367432e-007 
		0 -27.812107 9.5367432e-007 0 -27.812107 9.5367432e-007 0 -27.812107 9.5367432e-007;
	setAttr -s 4 ".vt[0:3]"  -5.50908756 41.88209534 0.99995744 -5.0050997734 41.88209534 0.99995744
		 -5.50908756 42.52502441 0.99995744 -5.0050997734 42.52502441 0.99995744;
	setAttr -s 4 ".ed[0:3]"  0 1 0 2 3 0 0 2 0 1 3 0;
	setAttr -ch 4 ".fc[0]" -type "polyFaces" 
		f 4 0 3 -2 -3
		mu 0 4 0 1 2 3;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "c_Rt_brows_05_CTRL_guide" -p "FM_Cam_r_hi_brow";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -6.0270898342132568 14.391452789306641 0.99995803833007491 ;
	setAttr ".sp" -type "double3" -6.0270898342132568 14.391452789306641 0.99995803833007491 ;
createNode mesh -n "c_Rt_brows_05_CTRL_guideShape" -p "c_Rt_brows_05_CTRL_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 4 ".uvst[0].uvsp[0:3]" -type "float2" 0.375 0 0.625 0 0.625
		 0.25 0.375 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 4 ".pt[0:3]" -type "float3"  0 -27.812107 9.5367432e-007 
		0 -27.812107 9.5367432e-007 0 -27.812107 9.5367432e-007 0 -27.812107 9.5367432e-007;
	setAttr -s 4 ".vt[0:3]"  -6.27908373 41.88209534 0.99995744 -5.77509594 41.88209534 0.99995744
		 -6.27908373 42.52502441 0.99995744 -5.77509594 42.52502441 0.99995744;
	setAttr -s 4 ".ed[0:3]"  0 1 0 2 3 0 0 2 0 1 3 0;
	setAttr -ch 4 ".fc[0]" -type "polyFaces" 
		f 4 0 3 -2 -3
		mu 0 4 0 1 2 3;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_l_hi_brow" -p "FM_Cam_c_hi_face";
	setAttr ".rp" -type "double3" 5.296299934387207 15.377712249755859 1.018184661865231 ;
	setAttr ".sp" -type "double3" 5.296299934387207 15.377712249755859 1.018184661865231 ;
createNode transform -n "c_Lf_eyebrows_CTRL_backgroundColor_" -p "FM_Cam_l_hi_brow";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr ".ove" yes;
	setAttr ".rp" -type "double3" 4.5457873344421387 15.377712249755859 0.94457244873046531 ;
	setAttr ".sp" -type "double3" 4.5457873344421387 15.377712249755859 0.94457244873046531 ;
createNode mesh -n "c_Lf_eyebrows_CTRL_backgroundColor_Shape" -p "c_Lf_eyebrows_CTRL_backgroundColor_";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 8 ".uvst[0].uvsp[0:7]" -type "float2" 0.375 0.22500245
		 0.625 0.22500245 0.61284238 0.25 0.38715762 0.24999999 0.375 0.024997517 0.625 0.024997562
		 0.38715762 -7.4505806e-009 0.61284238 0;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 8 ".vt[0:7]"  7.77378654 16.73395157 0.94457269 7.63607693 16.91597366 0.94457269
		 1.45549774 16.91597366 0.94457269 1.31778812 16.73395157 0.94457269 7.63607693 13.83945084 0.94457269
		 7.77378654 14.021476746 0.94457269 1.31778812 14.021476746 0.94457269 1.45549774 13.83945084 0.94457269;
	setAttr -s 8 ".ed[0:7]"  1 2 0 1 0 0 3 2 0 4 7 0 5 0 0 4 5 0 6 3 0
		 7 6 0;
	setAttr -ch 8 ".fc[0]" -type "polyFaces" 
		f 8 -8 -4 5 4 -2 0 -3 -7
		mu 0 8 5 7 6 4 0 3 2 1;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "c_Lf_eyebrows_01_CTRL_guide" -p "FM_Cam_l_hi_brow";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 2.6817522048950195 15.499760150909424 1.0917968749999967 ;
	setAttr ".sp" -type "double3" 2.6817522048950195 15.499760150909424 1.0917968749999967 ;
createNode mesh -n "c_Lf_eyebrows_01_CTRL_guideShape" -p "c_Lf_eyebrows_01_CTRL_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 8 ".uvst[0].uvsp[0:7]" -type "float2" 0.5625 0.024997551
		 0.55642116 -1.8626451e-009 0.61284238 0 0.625 0.024997562 0.5625 0.22500245 0.625
		 0.22500245 0.55642116 0.25 0.61284238 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 8 ".vt[0:7]"  2.098668575 15.95059967 1.091796041 2.023553371 15.89101791 1.091796041
		 2.023553371 15.0031166077 1.091796041 2.098668575 14.94353485 1.091796041 3.33995104 15.048923492 1.091796041
		 3.30239344 15.10850525 1.091796041 3.30239344 15.99640274 1.091796041 3.33995104 16.055986404 1.091796041;
	setAttr -s 8 ".ed[0:7]"  1 0 0 2 1 0 3 2 0 4 3 0 4 5 0 5 6 0 7 0 0
		 6 7 0;
	setAttr -ch 8 ".fc[0]" -type "polyFaces" 
		f 8 -2 -3 -4 4 5 7 6 -1
		mu 0 8 5 3 2 1 0 4 6 7;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "c_Lf_eyebrows_02_CTRL_guide" -p "FM_Cam_l_hi_brow";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 3.9418132305145264 15.700954914093018 1.0917968749999964 ;
	setAttr ".sp" -type "double3" 3.9418132305145264 15.700954914093018 1.0917968749999964 ;
createNode mesh -n "c_Lf_eyebrows_02_CTRL_guideShape" -p "c_Lf_eyebrows_02_CTRL_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 8 ".uvst[0].uvsp[0:7]" -type "float2" 0.5 0.22500245 0.5625
		 0.22500245 0.55642116 0.25 0.5 0.25 0.5 0.02499754 0.5625 0.024997551 0.5 -3.7252903e-009
		 0.55642116 -1.8626451e-009;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 8 ".vt[0:7]"  4.58123302 16.35298729 1.091796041 4.58123302 16.29340553 1.091796041
		 4.58123302 15.40550613 1.091796041 4.58123302 15.34592056 1.091796041 3.30239344 15.99640274 1.091796041
		 3.33995104 16.055986404 1.091796041 3.30239344 15.10850525 1.091796041 3.33995104 15.048923492 1.091796041;
	setAttr -s 8 ".ed[0:7]"  0 5 0 0 1 0 1 2 0 3 7 0 2 3 0 4 5 0 6 4 0
		 7 6 0;
	setAttr -ch 8 ".fc[0]" -type "polyFaces" 
		f 8 -8 -4 -5 -3 -2 0 -6 -7
		mu 0 8 5 7 6 4 0 3 2 1;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "c_Lf_eyebrows_03_CTRL_guide" -p "FM_Cam_l_hi_brow";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 5.8600726127624512 15.902149677276611 1.0917968749999964 ;
	setAttr ".sp" -type "double3" 5.8600726127624512 15.902149677276611 1.0917968749999964 ;
createNode mesh -n "c_Lf_eyebrows_03_CTRL_guideShape" -p "c_Lf_eyebrows_03_CTRL_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 10 ".uvst[0].uvsp[0:9]" -type "float2" 0.5 0.22500245 0.5
		 0.25 0.44357881 0.25 0.5 0.02499754 0.44357881 -5.5879354e-009 0.5 -3.7252903e-009
		 0.375 0.22500245 0.38715762 0.24999999 0.375 0.024997517 0.38715762 -7.4505806e-009;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 10 ".vt[0:9]"  7.1389122 16.29340553 1.091796041 7.063799858 16.35298729 1.091796041
		 7.063799858 15.34592056 1.091796041 7.1389122 15.40550613 1.091796041 5.82251644 16.45837975 1.091796041
		 5.82251644 15.4513092 1.091796041 4.58123302 16.29340553 1.091796041 4.58123302 16.35298729 1.091796041
		 4.58123302 15.40550613 1.091796041 4.58123302 15.34592056 1.091796041;
	setAttr -s 10 ".ed[0:9]"  1 4 0 1 0 0 2 5 0 3 0 0 2 3 0 4 7 0 5 9 0
		 7 6 0 6 8 0 8 9 0;
	setAttr -ch 10 ".fc[0]" -type "polyFaces" 
		f 10 9 -7 -3 4 3 -2 0 5 7 8
		mu 0 10 3 5 4 9 8 6 7 2 1 0;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "c_Lf_eyebrows_CTRL_guide" -p "FM_Cam_l_hi_brow";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 8.668785572052002 15.336277961730957 1.0385551452636685 ;
	setAttr ".sp" -type "double3" 8.668785572052002 15.336277961730957 1.0385551452636685 ;
createNode mesh -n "c_Lf_eyebrows_CTRL_guideShape" -p "c_Lf_eyebrows_CTRL_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 12 ".uvst[0].uvsp[0:11]" -type "float2" 0.375 0.25 0.38149059
		 0.25778872 0.875 1 0.875 0 0.51945782 0.42334932 0.875 1 0.75 1 0.51944202 0.42333046
		 0.53125 0.4375 0.38168237 0.25801882 0.40625 0.25 0.375 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 12 ".vt[0:11]"  8.1243248 14.6388855 1.038555622 8.66595936 16.3956852 1.038554668
		 8.66997337 14.27744675 1.038555622 8.37557793 14.27687073 1.038555622 8.37487411 14.63937759 1.038555622
		 9.21421719 14.64100647 1.038555622 8.96367264 14.640522 1.038555622 8.96437645 14.27801514 1.038555622
		 8.58420944 16.33660316 1.038554668 8.74785995 16.33709908 1.038554668 8.062759399 14.71416855 1.038555622
		 9.27481174 14.71875381 1.038555622;
	setAttr -s 12 ".ed[0:11]"  0 10 0 3 2 0 3 4 0 5 6 0 5 11 0 7 6 0 7 2 0
		 0 4 0 8 1 0 9 1 0 10 8 0 11 9 0;
	setAttr -ch 12 ".fc[0]" -type "polyFaces" 
		f 12 -1 7 -3 1 -7 5 -4 4 11 9 -9 -11
		mu 0 12 1 0 3 2 6 5 10 11 9 4 8 7;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "c_Lf_brows_01_CTRL_guide" -p "FM_Cam_l_hi_brow";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 2.925694465637207 14.391452789306641 0.99995803833007491 ;
	setAttr ".sp" -type "double3" 2.925694465637207 14.391452789306641 0.99995803833007491 ;
createNode mesh -n "c_Lf_brows_01_CTRL_guideShape" -p "c_Lf_brows_01_CTRL_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 4 ".uvst[0].uvsp[0:3]" -type "float2" 0.375 0 0.625 0 0.625
		 0.25 0.375 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 4 ".pt[0:3]" -type "float3"  0 -27.812107 9.5367432e-007 
		0 -27.812107 9.5367432e-007 0 -27.812107 9.5367432e-007 0 -27.812107 9.5367432e-007;
	setAttr -s 4 ".vt[0:3]"  3.17768812 41.88209534 0.99995744 2.67370081 41.88209534 0.99995744
		 3.17768812 42.52502441 0.99995744 2.67370081 42.52502441 0.99995744;
	setAttr -s 4 ".ed[0:3]"  0 1 0 2 3 0 0 2 0 1 3 0;
	setAttr -ch 4 ".fc[0]" -type "polyFaces" 
		f 4 2 1 -4 -1
		mu 0 4 0 3 2 1;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "c_Lf_brows_02_CTRL_guide" -p "FM_Cam_l_hi_brow";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 3.751835823059082 14.391452789306641 0.99995803833007491 ;
	setAttr ".sp" -type "double3" 3.751835823059082 14.391452789306641 0.99995803833007491 ;
createNode mesh -n "c_Lf_brows_02_CTRL_guideShape" -p "c_Lf_brows_02_CTRL_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 4 ".uvst[0].uvsp[0:3]" -type "float2" 0.375 0 0.625 0 0.625
		 0.25 0.375 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 4 ".pt[0:3]" -type "float3"  0 -27.812107 9.5367432e-007 
		0 -27.812107 9.5367432e-007 0 -27.812107 9.5367432e-007 0 -27.812107 9.5367432e-007;
	setAttr -s 4 ".vt[0:3]"  4.0038294792 41.88209534 0.99995744 3.49984217 41.88209534 0.99995744
		 4.0038294792 42.52502441 0.99995744 3.49984217 42.52502441 0.99995744;
	setAttr -s 4 ".ed[0:3]"  0 1 0 2 3 0 0 2 0 1 3 0;
	setAttr -ch 4 ".fc[0]" -type "polyFaces" 
		f 4 2 1 -4 -1
		mu 0 4 0 3 2 1;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "c_Lf_brows_03_CTRL_guide" -p "FM_Cam_l_hi_brow";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 4.5699572563171387 14.391452789306641 0.99995803833007491 ;
	setAttr ".sp" -type "double3" 4.5699572563171387 14.391452789306641 0.99995803833007491 ;
createNode mesh -n "c_Lf_brows_03_CTRL_guideShape" -p "c_Lf_brows_03_CTRL_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 4 ".uvst[0].uvsp[0:3]" -type "float2" 0.375 0 0.625 0 0.625
		 0.25 0.375 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 4 ".pt[0:3]" -type "float3"  0 -27.812107 9.5367432e-007 
		0 -27.812107 9.5367432e-007 0 -27.812107 9.5367432e-007 0 -27.812107 9.5367432e-007;
	setAttr -s 4 ".vt[0:3]"  4.82195091 41.88209534 0.99995744 4.3179636 41.88209534 0.99995744
		 4.82195091 42.52502441 0.99995744 4.3179636 42.52502441 0.99995744;
	setAttr -s 4 ".ed[0:3]"  0 1 0 2 3 0 0 2 0 1 3 0;
	setAttr -ch 4 ".fc[0]" -type "polyFaces" 
		f 4 2 1 -4 -1
		mu 0 4 0 3 2 1;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "c_Lf_brows_04_CTRL_guide" -p "FM_Cam_l_hi_brow";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 5.3399538993835449 14.391452789306641 0.99995803833007491 ;
	setAttr ".sp" -type "double3" 5.3399538993835449 14.391452789306641 0.99995803833007491 ;
createNode mesh -n "c_Lf_brows_04_CTRL_guideShape" -p "c_Lf_brows_04_CTRL_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 4 ".uvst[0].uvsp[0:3]" -type "float2" 0.375 0 0.625 0 0.625
		 0.25 0.375 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 4 ".pt[0:3]" -type "float3"  0 -27.812107 9.5367432e-007 
		0 -27.812107 9.5367432e-007 0 -27.812107 9.5367432e-007 0 -27.812107 9.5367432e-007;
	setAttr -s 4 ".vt[0:3]"  5.59194756 41.88209534 0.99995744 5.087960243 41.88209534 0.99995744
		 5.59194756 42.52502441 0.99995744 5.087960243 42.52502441 0.99995744;
	setAttr -s 4 ".ed[0:3]"  0 1 0 2 3 0 0 2 0 1 3 0;
	setAttr -ch 4 ".fc[0]" -type "polyFaces" 
		f 4 2 1 -4 -1
		mu 0 4 0 3 2 1;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "c_Lf_brows_05_CTRL_guide" -p "FM_Cam_l_hi_brow";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 6.1099495887756348 14.391452789306641 0.99995803833007491 ;
	setAttr ".sp" -type "double3" 6.1099495887756348 14.391452789306641 0.99995803833007491 ;
createNode mesh -n "c_Lf_brows_05_CTRL_guideShape" -p "c_Lf_brows_05_CTRL_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 4 ".uvst[0].uvsp[0:3]" -type "float2" 0.375 0 0.625 0 0.625
		 0.25 0.375 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 4 ".pt[0:3]" -type "float3"  0 -27.812107 9.5367432e-007 
		0 -27.812107 9.5367432e-007 0 -27.812107 9.5367432e-007 0 -27.812107 9.5367432e-007;
	setAttr -s 4 ".vt[0:3]"  6.36194324 41.88209534 0.99995744 5.85795593 41.88209534 0.99995744
		 6.36194324 42.52502441 0.99995744 5.85795593 42.52502441 0.99995744;
	setAttr -s 4 ".ed[0:3]"  0 1 0 2 3 0 0 2 0 1 3 0;
	setAttr -ch 4 ".fc[0]" -type "polyFaces" 
		f 4 2 1 -4 -1
		mu 0 4 0 3 2 1;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_c_hi_cover" -p "FM_Cam_c_hi_face";
	setAttr ".rp" -type "double3" 0.048093318939208984 0.46844458580017118 1.168736457824707 ;
	setAttr ".sp" -type "double3" 0.048093318939208984 0.46844458580017118 1.168736457824707 ;
createNode transform -n "FM_Cam_c_hi_mouth_backgroundColor_" -p "FM_Cam_c_hi_cover";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 0 0.69603633880615257 0.97840797901153553 ;
	setAttr ".sp" -type "double3" 0 0.69603633880615257 0.97840797901153553 ;
createNode mesh -n "FM_Cam_c_hi_mouth_backgroundColor_Shape" -p "FM_Cam_c_hi_mouth_backgroundColor_";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 24 ".uvst[0].uvsp[0:23]" -type "float2" 0.375 0.25 0.625
		 0.25 0.55361432 0.25 0.55361432 0 0.47506088 0.25 0.47506088 0.02527169 0.375 0.18943125
		 0.375 0.10483883 0.58930719 0.25 0.58930719 0 0.57246578 0.25 0.57246578 0 0.58930719
		 0 0.625 0 0.58930719 0.25 0.55361432 0.25 0.47506088 0.25 0.47506088 0.02527169 0.55361432
		 0 0.375 0.18943125 0.375 0.25 0.375 0.10483883 0.57246578 0.25 0.57246578 0;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".rsl" 0;
	setAttr -s 24 ".pt[0:23]" -type "float3"  0 -5.6989489 -3.7421329 0 
		3.5766802 5.5334959 0 5.1342058 7.0910215 0 3.7983866 5.7552023 0 -5.3689528 -3.4121368 
		0 3.7244844 5.6813002 0 -4.1434412 -2.1866252 0 1.6579045 3.6147203 0 -1.331565 0.62525094 
		0 4.9992304 6.9560461 0 -5.6709204 -3.7141044 0 4.5105982 6.4674139 0 -5.5436182 
		-3.5868022 0 -5.6709204 -3.7141044 0 4.9992304 6.9560461 0 3.7983866 5.7552023 0 
		3.7244844 5.6813002 0 -4.1434412 -2.1866252 0 -5.3689528 -3.4121368 0 1.6579045 3.6147203 
		0 3.5766802 5.5334959 0 -1.331565 0.62525094 0 4.5105982 6.4674139 0 -5.5436182 -3.5868022;
	setAttr -s 24 ".vt[0:23]"  0 0.97840798 4.720541 -6.68814898 0.97840798 -4.55508804
		 0 0.97840798 -6.11261368 -1.90975261 0.97840798 -4.77679443 -1.90975261 0.97840798 4.39054489
		 -4.011260033 0.97840798 -4.7028923 -4.12965536 0.97840798 3.16503334 -6.68814898 0.97840798 -2.63631248
		 -6.27376699 0.97840798 0.35315704 -0.78209114 0.97840798 -5.97763824 -0.78209114 0.97840798 4.69251251
		 -1.40542603 0.97840798 -5.48900604 -1.40542603 0.97840798 4.56521034 0.78209114 0.97840798 4.69251251
		 0.78209114 0.97840798 -5.97763824 1.90975285 0.97840798 -4.77679443 4.011260033 0.97840798 -4.7028923
		 4.12965536 0.97840798 3.16503334 1.90975285 0.97840798 4.39054489 6.68814898 0.97840798 -2.63631248
		 6.68814898 0.97840798 -4.55508804 6.27376747 0.97840798 0.35315704 1.40542603 0.97840798 -5.48900604
		 1.40542603 0.97840798 4.56521034;
	setAttr -s 24 ".ed[0:23]"  1 5 0 3 11 0 4 12 0 5 3 0 7 1 0 8 7 0 6 8 0
		 6 4 0 9 2 0 10 0 0 11 9 0 12 10 0 13 0 0 14 2 0 16 15 0 17 18 0 20 16 0 19 20 0 21 19 0
		 17 21 0 22 14 0 23 13 0 15 22 0 18 23 0;
	setAttr -ch 24 ".fc[0]" -type "polyFaces" 
		f 24 -1 -5 -6 -7 7 2 11 9 -13 -22 -24 -16 19 18 17 16 14 22 20 13 -9 -11 -2 -4
		mu 0 24 4 0 6 7 5 3 11 9 13 12 23 18 17 21 19 20 16 15 22 14 1 8 10 2;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "c_mouthLip_CTRL_guide" -p "FM_Cam_c_hi_cover";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -2.384185791015625e-007 0.18789240717887903 1.1199684143066406 ;
	setAttr ".sp" -type "double3" -2.384185791015625e-007 0.18789240717887903 1.1199684143066406 ;
createNode mesh -n "c_mouthLip_CTRL_guideShape" -p "c_mouthLip_CTRL_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.64860266 0.79546607
		 0.62640899 0.75190848 0.59184152 0.71734101 0.54828393 0.69514734 0.5 0.68749994
		 0.45171607 0.69514734 0.40815851 0.71734107 0.37359107 0.75190854 0.3513974 0.79546607
		 0.34374997 0.84375 0.3513974 0.89203393 0.37359107 0.93559146 0.40815854 0.97015893
		 0.4517161 0.9923526 0.5 1 0.54828387 0.9923526 0.59184146 0.97015893 0.62640893 0.93559146
		 0.6486026 0.89203393 0.65625 0.84375;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".vt[0:19]"  1.49516368 0.34028053 1.11996841 1.27186227 0.47774887 1.11996841
		 0.92406195 0.58684731 1.11996841 0.48580807 0.65689087 1.11996841 0 0.68102646 1.11996841
		 -0.48580807 0.65689087 1.11996841 -0.92406178 0.58684731 1.11996841 -1.27186179 0.47774887 1.11996841
		 -1.4951632 0.34027863 1.11996841 -1.57210755 0.18789291 1.11996841 -1.4951632 0.035507202 1.11996841
		 -1.27186167 -0.10196304 1.11996841 -0.92406154 -0.21105957 1.11996841 -0.48580796 -0.28110504 1.11996841
		 -4.6852442e-008 -0.30524063 1.11996841 0.48580778 -0.28110504 1.11996841 0.92406142 -0.21105957 1.11996841
		 1.27186143 -0.10196304 1.11996841 1.49516273 0.035507202 1.11996841 1.57210708 0.18789291 1.11996841;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 19 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		mu 0 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "c_Rt_mouthLip_CTRL_guide" -p "FM_Cam_c_hi_cover";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -4.3422551155090332 0.21513506770133997 1.1673240661621094 ;
	setAttr ".sp" -type "double3" -4.3422551155090332 0.21513506770133997 1.1673240661621094 ;
createNode mesh -n "c_Rt_mouthLip_CTRL_guideShape" -p "c_Rt_mouthLip_CTRL_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.64860266 0.79546607
		 0.62640899 0.75190848 0.59184152 0.71734101 0.54828393 0.69514734 0.5 0.68749994
		 0.45171607 0.69514734 0.40815851 0.71734107 0.37359107 0.75190854 0.3513974 0.79546607
		 0.34374997 0.84375 0.3513974 0.89203393 0.37359107 0.93559146 0.40815854 0.97015893
		 0.4517161 0.9923526 0.5 1 0.54828387 0.9923526 0.59184146 0.97015893 0.62640893 0.93559146
		 0.6486026 0.89203393 0.65625 0.84375;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".vt[0:19]"  -3.63740945 0.44415474 1.16732407 -3.74267769 0.65075493 1.16732407
		 -3.90663671 0.81471252 1.16732407 -4.1132369 0.919981 1.16732407 -4.34225512 0.95625305 1.16732407
		 -4.57127285 0.919981 1.16732407 -4.77787304 0.81471252 1.16732407 -4.94183207 0.65075302 1.16732407
		 -5.047100067 0.44415283 1.16732407 -5.08337307 0.21513557 1.16732407 -5.047100067 -0.013881683 1.16732407
		 -4.94183207 -0.22048187 1.16732407 -4.77787304 -0.38444138 1.16732407 -4.57127285 -0.48970985 1.16732407
		 -4.34225512 -0.5259819 1.16732407 -4.1132369 -0.48970985 1.16732407 -3.90663671 -0.38444138 1.16732407
		 -3.7426784 -0.22048187 1.16732407 -3.63741016 -0.013881683 1.16732407 -3.60113716 0.21513557 1.16732407;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 19 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		mu 0 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "c_muothLip_01_second_CTRL_guide" -p "FM_Cam_c_hi_cover";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 0.051511287689208984 1.4209636449813845 1.1058864593505857 ;
	setAttr ".sp" -type "double3" 0.051511287689208984 1.4209636449813845 1.1058864593505857 ;
createNode mesh -n "c_muothLip_01_second_CTRL_guideShape" -p "c_muothLip_01_second_CTRL_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 4 ".uvst[0].uvsp[0:3]" -type "float2" 0.58443815 0.25 0.58443815
		 0.25 0.58443815 0 0.58443815 0;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 4 ".pt[0:3]" -type "float3"  0 -27.812107 -4.7683716e-007 
		0 -27.812107 -2.3841858e-007 0 -27.812107 -2.3841858e-007 0 -27.812107 -4.7683716e-007;
	setAttr -s 4 ".vt[0:3]"  -0.58110666 29.72270203 1.10588682 -0.54546642 28.74344063 1.10588682
		 0.648489 28.74344063 1.10588682 0.68412924 29.72270203 1.10588682;
	setAttr -s 4 ".ed[0:3]"  0 3 0 2 1 0 0 1 0 3 2 0;
	setAttr -ch 4 ".fc[0]" -type "polyFaces" 
		f 4 -1 2 -2 -4
		mu 0 4 0 1 2 3;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "c_muothLip_14_second_CTRL_guide" -p "FM_Cam_c_hi_cover";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -1.1648871898651123 1.3918032050132754 1.1058864593505857 ;
	setAttr ".sp" -type "double3" -1.1648871898651123 1.3918032050132754 1.1058864593505857 ;
createNode mesh -n "c_muothLip_14_second_CTRL_guideShape" -p "c_muothLip_14_second_CTRL_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 4 ".uvst[0].uvsp[0:3]" -type "float2" 0.54387629 0 0.58443815
		 0 0.58443815 0.25 0.54387629 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 4 ".pt[0:3]" -type "float3"  0 -27.812107 -4.7683716e-007 
		0 -27.812107 -2.3841858e-007 0 -27.812107 -4.7683716e-007 0 -27.812107 -3.5762787e-007;
	setAttr -s 4 ".vt[0:3]"  -0.58110666 29.72270203 1.10588682 -0.54546642 28.74344063 1.10588682
		 -1.78430796 29.63197899 1.10588682 -1.71302581 28.68511963 1.10588682;
	setAttr -s 4 ".ed[0:3]"  2 0 0 3 1 0 0 1 0 2 3 0;
	setAttr -ch 4 ".fc[0]" -type "polyFaces" 
		f 4 1 -3 -1 3
		mu 0 4 0 1 2 3;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "c_muothLip_02_second_CTRL_guide" -p "FM_Cam_c_hi_cover";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 1.274348258972168 1.3918032050132754 1.1058864593505857 ;
	setAttr ".sp" -type "double3" 1.274348258972168 1.3918032050132754 1.1058864593505857 ;
createNode mesh -n "c_muothLip_02_second_CTRL_guideShape" -p "c_muothLip_02_second_CTRL_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 4 ".uvst[0].uvsp[0:3]" -type "float2" 0.54387629 0 0.54387629
		 0.25 0.58443815 0.25 0.58443815 0;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 4 ".pt[0:3]" -type "float3"  0 -27.812107 -2.3841858e-007 
		0 -27.812107 -4.7683716e-007 0 -27.812107 -3.5762787e-007 0 -27.812107 -4.7683716e-007;
	setAttr -s 4 ".vt[0:3]"  0.648489 28.74344063 1.10588682 0.68412924 29.72270203 1.10588682
		 1.82892561 28.68511963 1.10588682 1.90020752 29.63197899 1.10588682;
	setAttr -s 4 ".ed[0:3]"  1 0 0 2 0 0 3 1 0 3 2 0;
	setAttr -ch 4 ".fc[0]" -type "polyFaces" 
		f 4 -4 2 0 -2
		mu 0 4 0 1 2 3;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "c_muothLip_13_second_CTRL_guide" -p "FM_Cam_c_hi_cover";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -2.355694055557251 1.1973976492881777 1.1058864593505857 ;
	setAttr ".sp" -type "double3" -2.355694055557251 1.1973976492881777 1.1058864593505857 ;
createNode mesh -n "c_muothLip_13_second_CTRL_guideShape" -p "c_muothLip_13_second_CTRL_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 4 ".uvst[0].uvsp[0:3]" -type "float2" 0.46275258 0 0.54387629
		 0 0.54387629 0.25 0.46275258 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 4 ".pt[0:3]" -type "float3"  0 -27.812107 -4.7683716e-007 
		0 -27.812107 -3.5762787e-007 0 -27.812107 -4.7683716e-007 0 -27.812107 -3.5762787e-007;
	setAttr -s 4 ".vt[0:3]"  -1.78430796 29.63197899 1.10588682 -1.71302581 28.68511963 1.10588682
		 -2.9983623 29.32093239 1.10588682 -2.72619724 28.38703156 1.10588682;
	setAttr -s 4 ".ed[0:3]"  2 0 0 3 1 0 0 1 0 2 3 0;
	setAttr -ch 4 ".fc[0]" -type "polyFaces" 
		f 4 1 -3 -1 3
		mu 0 4 0 1 2 3;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "c_muothLip_03_second_CTRL_guide" -p "FM_Cam_c_hi_cover";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 2.484471321105957 1.1973976492881777 1.1058864593505857 ;
	setAttr ".sp" -type "double3" 2.484471321105957 1.1973976492881777 1.1058864593505857 ;
createNode mesh -n "c_muothLip_03_second_CTRL_guideShape" -p "c_muothLip_03_second_CTRL_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 4 ".uvst[0].uvsp[0:3]" -type "float2" 0.46275258 0 0.46275258
		 0.25 0.54387629 0.25 0.54387629 0;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 4 ".pt[0:3]" -type "float3"  0 -27.812107 -3.5762787e-007 
		0 -27.812107 -4.7683716e-007 0 -27.812107 -3.5762787e-007 0 -27.812107 -4.7683716e-007;
	setAttr -s 4 ".vt[0:3]"  1.82892561 28.68511963 1.10588682 1.90020752 29.63197899 1.10588682
		 2.86785221 28.38703156 1.10588682 3.14001703 29.32093239 1.10588682;
	setAttr -s 4 ".ed[0:3]"  2 0 0 1 0 0 3 1 0 3 2 0;
	setAttr -ch 4 ".fc[0]" -type "polyFaces" 
		f 4 -4 2 1 -1
		mu 0 4 0 1 2 3;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "c_muothLip_12_second_CTRL_guide" -p "FM_Cam_c_hi_cover";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -3.5533030033111572 0.70490783452987693 1.1058864593505857 ;
	setAttr ".sp" -type "double3" -3.5533030033111572 0.70490783452987693 1.1058864593505857 ;
createNode mesh -n "c_muothLip_12_second_CTRL_guideShape" -p "c_muothLip_12_second_CTRL_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 4 ".uvst[0].uvsp[0:3]" -type "float2" 0.375 0 0.46275258
		 0 0.46275258 0.25 0.375 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 4 ".pt[0:3]" -type "float3"  0 -27.812107 -3.5762787e-007 
		0 -27.812107 -2.3841858e-007 0 -27.812107 -4.7683716e-007 0 -27.812107 -3.5762787e-007;
	setAttr -s 4 ".vt[0:3]"  -4.22488594 27.71309853 1.10588682 -4.38040876 28.73772049 1.10588682
		 -2.9983623 29.32093239 1.10588682 -2.72619724 28.38703156 1.10588682;
	setAttr -s 4 ".ed[0:3]"  0 3 0 1 2 0 0 1 0 2 3 0;
	setAttr -ch 4 ".fc[0]" -type "polyFaces" 
		f 4 0 -4 -2 -3
		mu 0 4 0 1 2 3;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "c_muothLip_04_second_CTRL_guide" -p "FM_Cam_c_hi_cover";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 3.5726194381713867 0.74997943639755271 1.1058864593505857 ;
	setAttr ".sp" -type "double3" 3.5726194381713867 0.74997943639755271 1.1058864593505857 ;
createNode mesh -n "c_muothLip_04_second_CTRL_guideShape" -p "c_muothLip_04_second_CTRL_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 4 ".uvst[0].uvsp[0:3]" -type "float2" 0.375 0 0.375 0.25
		 0.46275258 0.25 0.46275258 0;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 4 ".pt[0:3]" -type "float3"  0 -27.812107 -3.5762787e-007 
		0 -27.812107 -3.5762787e-007 0 -27.812107 -4.7683716e-007 0 -27.812107 -2.3841858e-007;
	setAttr -s 4 ".vt[0:3]"  4.13474178 27.80324173 1.10588682 2.86785221 28.38703156 1.10588682
		 3.14001703 29.32093239 1.10588682 4.27738667 28.85362053 1.10588682;
	setAttr -s 4 ".ed[0:3]"  0 1 0 2 1 0 3 2 0 0 3 0;
	setAttr -ch 4 ".fc[0]" -type "polyFaces" 
		f 4 3 2 1 -1
		mu 0 4 0 1 2 3;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "c_muothLip_08_second_CTRL_guide" -p "FM_Cam_c_hi_cover";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 0.038058996200561523 -1.0458522140979765 1.1058864593505862 ;
	setAttr ".sp" -type "double3" 0.038058996200561523 -1.0458522140979765 1.1058864593505862 ;
createNode mesh -n "c_muothLip_08_second_CTRL_guideShape" -p "c_muothLip_08_second_CTRL_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 4 ".uvst[0].uvsp[0:3]" -type "float2" 0.58443815 0.25 0.58443815
		 0.25 0.58443815 0 0.58443815 0;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 4 ".pt[0:3]" -type "float3"  0 -27.812107 -2.9802322e-007 
		0 -27.812107 -3.5762787e-007 0 -27.812107 -3.5762787e-007 0 -27.812107 -2.9802322e-007;
	setAttr -s 4 ".vt[0:3]"  0.65722466 26.27635574 1.10588682 0.62158442 27.25615501 1.10588682
		 -0.54546642 27.25615501 1.10588682 -0.58110666 26.27635574 1.10588682;
	setAttr -s 4 ".ed[0:3]"  2 1 0 0 3 0 0 1 0 3 2 0;
	setAttr -ch 4 ".fc[0]" -type "polyFaces" 
		f 4 -2 2 -1 -4
		mu 0 4 0 1 2 3;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "c_muothLip_09_second_CTRL_guide" -p "FM_Cam_c_hi_cover";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -1.1648871898651123 -1.0166764557361601 1.1058864593505862 ;
	setAttr ".sp" -type "double3" -1.1648871898651123 -1.0166764557361601 1.1058864593505862 ;
createNode mesh -n "c_muothLip_09_second_CTRL_guideShape" -p "c_muothLip_09_second_CTRL_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 4 ".uvst[0].uvsp[0:3]" -type "float2" 0.54387629 0 0.54387629
		 0.25 0.58443815 0.25 0.58443815 0;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 4 ".pt[0:3]" -type "float3"  0 -27.812107 -2.9802322e-007 
		0 -27.812107 -3.5762787e-007 0 -27.812107 -3.5762787e-007 0 -27.812107 -2.9802322e-007;
	setAttr -s 4 ".vt[0:3]"  -0.58110666 26.27635574 1.10588682 -0.54546642 27.25615501 1.10588682
		 -1.71302581 27.31450653 1.10588682 -1.78430796 26.36712837 1.10588682;
	setAttr -s 4 ".ed[0:3]"  3 0 0 2 1 0 0 1 0 3 2 0;
	setAttr -ch 4 ".fc[0]" -type "polyFaces" 
		f 4 -4 0 2 -2
		mu 0 4 0 1 2 3;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "c_muothLip_07_second_CTRL_guide" -p "FM_Cam_c_hi_cover";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 1.2647919654846191 -1.0166764557361601 1.1058864593505862 ;
	setAttr ".sp" -type "double3" 1.2647919654846191 -1.0166764557361601 1.1058864593505862 ;
createNode mesh -n "c_muothLip_07_second_CTRL_guideShape" -p "c_muothLip_07_second_CTRL_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 4 ".uvst[0].uvsp[0:3]" -type "float2" 0.54387629 0 0.58443815
		 0 0.58443815 0.25 0.54387629 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 4 ".pt[0:3]" -type "float3"  0 -27.812107 -3.5762787e-007 
		0 -27.812107 -2.9802322e-007 0 -27.812107 -2.9802322e-007 0 -27.812107 -3.5762787e-007;
	setAttr -s 4 ".vt[0:3]"  0.62158442 27.25615501 1.10588682 0.65722466 26.27635574 1.10588682
		 1.90799952 26.36712837 1.10588682 1.83671761 27.31450653 1.10588682;
	setAttr -s 4 ".ed[0:3]"  1 0 0 2 1 0 3 0 0 2 3 0;
	setAttr -ch 4 ".fc[0]" -type "polyFaces" 
		f 4 2 -1 -2 3
		mu 0 4 0 1 2 3;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "c_muothLip_10_second_CTRL_guide" -p "FM_Cam_c_hi_cover";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -2.355694055557251 -0.82216504216194131 1.1058864593505862 ;
	setAttr ".sp" -type "double3" -2.355694055557251 -0.82216504216194131 1.1058864593505862 ;
createNode mesh -n "c_muothLip_10_second_CTRL_guideShape" -p "c_muothLip_10_second_CTRL_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 4 ".uvst[0].uvsp[0:3]" -type "float2" 0.46275258 0 0.46275258
		 0.25 0.54387629 0.25 0.54387629 0;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 4 ".pt[0:3]" -type "float3"  0 -27.812107 -2.9802322e-007 
		0 -27.812107 -3.5762787e-007 0 -27.812107 -3.5762787e-007 0 -27.812107 -3.0174851e-007;
	setAttr -s 4 ".vt[0:3]"  -1.78430796 26.36712837 1.10588682 -1.71302581 27.31450653 1.10588682
		 -2.72619724 27.61275673 1.10588682 -2.9983623 26.67834473 1.10588682;
	setAttr -s 4 ".ed[0:3]"  3 0 0 2 1 0 0 1 0 3 2 0;
	setAttr -ch 4 ".fc[0]" -type "polyFaces" 
		f 4 -4 0 2 -2
		mu 0 4 0 1 2 3;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "c_muothLip_06_second_CTRL_guide" -p "FM_Cam_c_hi_cover";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 2.4793858528137207 -0.82216504216194131 1.1058864593505862 ;
	setAttr ".sp" -type "double3" 2.4793858528137207 -0.82216504216194131 1.1058864593505862 ;
createNode mesh -n "c_muothLip_06_second_CTRL_guideShape" -p "c_muothLip_06_second_CTRL_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 4 ".uvst[0].uvsp[0:3]" -type "float2" 0.46275258 0 0.54387629
		 0 0.54387629 0.25 0.46275258 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 4 ".pt[0:3]" -type "float3"  0 -27.812107 -2.9802322e-007 
		0 -27.812107 -3.5762787e-007 0 -27.812107 -3.0174851e-007 0 -27.812107 -3.5762787e-007;
	setAttr -s 4 ".vt[0:3]"  1.90799952 26.36712837 1.10588682 1.83671761 27.31450653 1.10588682
		 3.1220541 26.67834473 1.10588682 2.8498888 27.61275673 1.10588682;
	setAttr -s 4 ".ed[0:3]"  2 0 0 0 1 0 3 1 0 2 3 0;
	setAttr -ch 4 ".fc[0]" -type "polyFaces" 
		f 4 2 -2 -1 3
		mu 0 4 0 1 2 3;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "c_muothLip_11_second_CTRL_guide" -p "FM_Cam_c_hi_cover";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -3.5533030033111572 -0.32940530776977517 1.1058864593505859 ;
	setAttr ".sp" -type "double3" -3.5533030033111572 -0.32940530776977517 1.1058864593505859 ;
createNode mesh -n "c_muothLip_11_second_CTRL_guideShape" -p "c_muothLip_11_second_CTRL_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 4 ".uvst[0].uvsp[0:3]" -type "float2" 0.375 0 0.375 0.25
		 0.46275258 0.25 0.46275258 0;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 4 ".pt[0:3]" -type "float3"  0 -27.812107 -3.5762787e-007 
		0 -27.812107 -3.5762787e-007 0 -27.812107 -3.0174851e-007 0 -27.812107 -3.5762787e-007;
	setAttr -s 4 ".vt[0:3]"  -4.22488594 28.28705978 1.10588682 -4.38040876 27.26187515 1.10588682
		 -2.9983623 26.67834473 1.10588682 -2.72619724 27.61275673 1.10588682;
	setAttr -s 4 ".ed[0:3]"  0 3 0 1 2 0 0 1 0 2 3 0;
	setAttr -ch 4 ".fc[0]" -type "polyFaces" 
		f 4 2 1 3 -1
		mu 0 4 0 1 2 3;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "c_muothLip_05_second_CTRL_guide" -p "FM_Cam_c_hi_cover";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 3.5628175735473633 -0.38649415969848611 1.1058864593505859 ;
	setAttr ".sp" -type "double3" 3.5628175735473633 -0.38649415969848611 1.1058864593505859 ;
createNode mesh -n "c_muothLip_05_second_CTRL_guideShape" -p "c_muothLip_05_second_CTRL_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 4 ".uvst[0].uvsp[0:3]" -type "float2" 0.375 0 0.46275258
		 0 0.46275258 0.25 0.375 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 4 ".pt[0:3]" -type "float3"  0 -27.812107 -3.5762787e-007 
		0 -27.812107 -3.5762787e-007 0 -27.812107 -3.0174851e-007 0 -27.812107 -3.5762787e-007;
	setAttr -s 4 ".vt[0:3]"  4.12022305 28.17288208 1.10588682 4.27574635 27.14769936 1.10588682
		 3.1220541 26.67834473 1.10588682 2.8498888 27.61275673 1.10588682;
	setAttr -s 4 ".ed[0:3]"  0 1 0 1 2 0 2 3 0 0 3 0;
	setAttr -ch 4 ".fc[0]" -type "polyFaces" 
		f 4 3 -3 -2 -1
		mu 0 4 0 1 2 3;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "c_Lf_mouthLip_CTRL_guide" -p "FM_Cam_c_hi_cover";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 4.4065219163894653 0.21513506770133997 1.1673240661621094 ;
	setAttr ".sp" -type "double3" 4.4065219163894653 0.21513506770133997 1.1673240661621094 ;
createNode mesh -n "c_Lf_mouthLip_CTRL_guideShape" -p "c_Lf_mouthLip_CTRL_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.64860266 0.79546607
		 0.62640899 0.75190848 0.59184152 0.71734101 0.54828393 0.69514734 0.5 0.68749994
		 0.45171607 0.69514734 0.40815851 0.71734107 0.37359107 0.75190854 0.3513974 0.79546607
		 0.34374997 0.84375 0.3513974 0.89203393 0.37359107 0.93559146 0.40815854 0.97015893
		 0.4517161 0.9923526 0.5 1 0.54828387 0.9923526 0.59184146 0.97015893 0.62640893 0.93559146
		 0.6486026 0.89203393 0.65625 0.84375;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".vt[0:19]"  5.11136723 0.44415474 1.16732407 5.0060992241 0.65075493 1.16732407
		 4.84214067 0.81471252 1.16732407 4.63554001 0.919981 1.16732407 4.40652227 0.95625305 1.16732407
		 4.17750406 0.919981 1.16732407 3.97090411 0.81471252 1.16732407 3.80694532 0.65075302 1.16732407
		 3.70167708 0.44415283 1.16732407 3.66540408 0.21513557 1.16732407 3.70167708 -0.013881683 1.16732407
		 3.80694532 -0.22048187 1.16732407 3.97090435 -0.38444138 1.16732407 4.17750406 -0.48970985 1.16732407
		 4.40652227 -0.5259819 1.16732407 4.63554049 -0.48970985 1.16732407 4.8421402 -0.38444138 1.16732407
		 5.0060992241 -0.22048187 1.16732407 5.11136675 -0.013881683 1.16732407 5.14763975 0.21513557 1.16732407;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 19 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		mu 0 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "c_Lf_nosewing_CTRL_guide" -p "FM_Cam_c_hi_cover";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 0.78313446044921875 4.7665503025054932 1.0669164657592762 ;
	setAttr ".sp" -type "double3" 0.78313446044921875 4.7665503025054932 1.0669164657592762 ;
createNode mesh -n "c_Lf_nosewing_CTRL_guideShape" -p "c_Lf_nosewing_CTRL_guide";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 15 ".uvst[0].uvsp[0:14]" -type "float2" 0.375 0.019314488
		 0.375 0.10036689 0.375 0 0.40518284 0 0.40518284 0.1750624 0.48571217 0.25 0.52727604
		 0.25 0.52727604 0.23260936 0.48554382 0.21759836 0.45843607 0.18315665 0.45843607
		 0.23545432 0.44340986 0.14214885 0.43938816 0.10036689 0.44778165 0.019314487 0.45843607
		 0;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 15 ".vt[0:14]"  1.51817989 4.25870895 1.066915274 1.51817989 4.57220078 1.066915274
		 1.51817989 4.056171417 1.066915274 1.22678661 3.8429966 1.066915631 0.89656544 4.57220078 1.066915631
		 0.81553364 3.96027565 1.066915631 0.71267414 3.78028679 1.066915631 1.22678661 5.16155624 1.066915631
		 0.71267414 5.22541428 1.066915631 0.85773945 4.90186691 1.066915631 0.44935226 5.75281525 1.066917181
		 0.45097637 5.49716568 1.066917181 0.71267414 5.63804626 1.066917539 0.048089027 5.75281525 1.066917181
		 0.048089027 5.6156044 1.066917181;
	setAttr -s 15 ".ed[0:14]"  0 1 0 2 3 0 2 0 0 4 5 0 5 6 0 1 7 0 8 9 0
		 9 4 0 11 14 0 10 13 0 11 8 0 12 10 0 7 12 0 3 6 0 13 14 0;
	setAttr -ch 15 ".fc[0]" -type "polyFaces" 
		f 15 12 11 9 14 -9 10 6 7 3 4 -14 -2 2 0 5
		mu 0 15 4 10 5 6 7 8 9 11 12 13 14 3 2 0 1;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "c_Rt_nosewing_CTRL_guide" -p "FM_Cam_c_hi_cover";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -0.68695640563964844 4.7665503025054932 1.0669164657592762 ;
	setAttr ".sp" -type "double3" -0.68695640563964844 4.7665503025054932 1.0669164657592762 ;
createNode mesh -n "c_Rt_nosewing_CTRL_guideShape" -p "c_Rt_nosewing_CTRL_guide";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 15 ".uvst[0].uvsp[0:14]" -type "float2" 0.375 0.019314488
		 0.375 0.10036689 0.375 0 0.40518284 0 0.40518284 0.1750624 0.48571217 0.25 0.48554382
		 0.21759836 0.52727604 0.23260936 0.52727604 0.25 0.45843607 0.23545432 0.45843607
		 0.18315665 0.44340986 0.14214885 0.44778165 0.019314487 0.43938816 0.10036689 0.45843607
		 0;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 15 ".vt[0:14]"  -1.42200184 4.056171417 1.066915274 0.048089027 5.75281525 1.066917181
		 -1.42200184 4.57220078 1.066915274 -1.42200184 4.25870895 1.066915274 -1.13060856 3.8429966 1.066915631
		 -0.61649609 3.78028679 1.066915631 -1.13060856 5.16155624 1.066915631 -0.61649609 5.63804626 1.066917539
		 -0.35317421 5.75281525 1.066917181 -0.35479832 5.49716568 1.066917181 -0.61649609 5.22541428 1.066915631
		 -0.80038738 4.57220078 1.066915631 -0.76156139 4.90186691 1.066915631 -0.71935558 3.96027565 1.066915631
		 0.048089027 5.6156044 1.066917181;
	setAttr -s 15 ".ed[0:14]"  0 4 0 0 3 0 1 14 0 3 2 0 4 5 0 2 6 0 6 7 0
		 8 1 0 7 8 0 9 10 0 10 12 0 12 11 0 11 13 0 13 5 0 9 14 0;
	setAttr -ch 15 ".fc[0]" -type "polyFaces" 
		f 15 -11 -10 14 -3 -8 -9 -7 -6 -4 -2 0 4 -14 -13 -12
		mu 0 15 11 10 6 7 8 5 9 4 1 0 2 3 14 12 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "c_nose_CTRL_guide" -p "FM_Cam_c_hi_cover";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 0.048089265823364258 4.6979457139968872 1.0669164657592762 ;
	setAttr ".sp" -type "double3" 0.048089265823364258 4.6979457139968872 1.0669164657592762 ;
createNode mesh -n "c_nose_CTRL_guideShape" -p "c_nose_CTRL_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 16 ".uvst[0].uvsp[0:15]" -type "float2" 0.48441321 0 0.43938816
		 0.10036689 0.44778165 0.019314487 0.45843607 0 0.45843607 0.18315665 0.44340986 0.14214885
		 0.48554382 0.21759836 0.52727604 0.23260936 0.48441321 0 0.52727604 0 0.43938816
		 0.10036689 0.44778165 0.019314487 0.45843607 0 0.45843607 0.18315665 0.44340986 0.14214885
		 0.48554382 0.21759836;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 16 ".vt[0:15]"  0.048089027 3.78030014 1.066915274 -0.36571217 3.7802887 1.066915274
		 0.46189022 3.7802887 1.066915274 -0.80038691 4.57220459 1.066915274 -0.71935558 3.96027374 1.066915274
		 -0.61649609 3.7802887 1.066915274 -0.61649609 5.22541809 1.066915274 -0.76156092 4.9018631 1.066915274
		 -0.35479832 5.49716568 1.066917181 0.048089027 5.6156044 1.066917181 0.81553411 3.96027374 1.066915274
		 0.89656544 4.57220459 1.066915274 0.71267462 3.7802887 1.066915274 0.85773945 4.9018631 1.066915274
		 0.71267462 5.22541809 1.066915274 0.45097685 5.49716568 1.066917181;
	setAttr -s 16 ".ed[0:15]"  5 1 0 1 0 0 2 0 0 12 2 0 3 4 0 4 5 0 6 7 0
		 7 3 0 8 6 0 8 9 0 11 10 0 10 12 0 13 11 0 14 13 0 15 14 0 15 9 0;
	setAttr -ch 16 ".fc[0]" -type "polyFaces" 
		f 16 15 -10 8 6 7 4 5 0 1 -3 -4 -12 -11 -13 -14 -15
		mu 0 16 15 7 6 4 5 1 2 3 0 9 8 12 11 10 14 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "c_up_mouthLip_CTRL_guide" -p "FM_Cam_c_hi_cover";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 0.089311122894287109 2.5752511024475102 1.0669155120849603 ;
	setAttr ".sp" -type "double3" 0.089311122894287109 2.5752511024475102 1.0669155120849603 ;
createNode mesh -n "c_up_mouthLip_CTRL_guideShape" -p "c_up_mouthLip_CTRL_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.375 0 0.52727604
		 0.25 0.375 0.10036689 0.375 0.019314488 0.40518284 0 0.45843607 0 0.40518284 0.1750624
		 0.45843607 0.23545432 0.48571217 0.25 0.48441321 0 0.375 0.019314488 0.375 0.10036689
		 0.375 0 0.40518284 0 0.48441321 0 0.52727604 0 0.45843607 0 0.40518284 0.1750624
		 0.45843607 0.23545432 0.48571217 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".vt[0:19]"  -1.083952904 2.23743629 1.066915512 0.096180916 2.9314003 1.066915512
		 0.096180916 2.23215103 1.066915512 -1.096357346 2.4186039 1.066915512 -1.12090969 2.30923843 1.066915512
		 -0.82822037 2.21910286 1.066915512 -0.45951653 2.23214722 1.066915512 -0.84341431 2.64641571 1.066915512
		 -0.4596405 2.86604691 1.066915512 -0.25846767 2.91906738 1.066915512 -0.26804638 2.23214722 1.066915512
		 1.29953194 2.30923843 1.066915512 1.27497959 2.4186039 1.066915512 1.26257515 2.23743629 1.066915512
		 1.0068426132 2.21910286 1.066915512 0.44666862 2.23214722 1.066915512 0.63813877 2.23214722 1.066915512
		 1.022036552 2.64641571 1.066915512 0.63826275 2.86604691 1.066915512 0.43708992 2.91906738 1.066915512;
	setAttr -s 20 ".ed[0:19]"  0 5 0 0 4 0 4 3 0 5 6 0 6 10 0 3 7 0 7 8 0
		 9 1 0 8 9 0 10 2 0 11 12 0 13 14 0 13 11 0 15 2 0 14 16 0 12 17 0 17 18 0 19 1 0
		 18 19 0 16 15 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 16 18 17 -8 -9 -7 -6 -3 -2 0 3 4 9 -14 -20 -15 -12 12 10 15
		mu 0 20 17 18 19 1 8 7 6 2 3 0 4 5 9 15 14 16 13 12 10 11;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "c_dn_mouthLip_CTRL_guide" -p "FM_Cam_c_hi_cover";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 0.089311122894287109 -2.2421011924743648 1.0669155120849614 ;
	setAttr ".sp" -type "double3" 0.089311122894287109 -2.2421011924743648 1.0669155120849614 ;
createNode mesh -n "c_dn_mouthLip_CTRL_guideShape" -p "c_dn_mouthLip_CTRL_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.375 0 0.52727604
		 0 0.375 0.10036689 0.375 0.019314488 0.40518284 0 0.45843607 0 0.40518284 0.1750624
		 0.45843607 0.23545432 0.48571217 0.25 0.48441321 0 0.375 0.019314488 0.375 0.10036689
		 0.375 0 0.40518284 0 0.48441321 0 0.45843607 0 0.40518284 0.1750624 0.45843607 0.23545432
		 0.48571217 0.25 0.52727604 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".vt[0:19]"  -1.083952904 -1.90428734 1.066915512 0.096180916 -2.59824944 1.066915512
		 0.096180916 -1.89900208 1.066915512 -1.096357346 -2.085453033 1.066915512 -1.12090969 -1.97608566 1.066915512
		 -0.82822037 -1.885952 1.066915512 -0.45951653 -1.89899635 1.066915512 -0.84341431 -2.31326294 1.066915512
		 -0.4596405 -2.53289604 1.066915512 -0.25846767 -2.58591461 1.066915512 -0.26804638 -1.89899635 1.066915512
		 1.29953194 -1.97608566 1.066915512 1.27497959 -2.085453033 1.066915512 1.26257515 -1.90428734 1.066915512
		 1.0068426132 -1.885952 1.066915512 0.44666862 -1.89899635 1.066915512 0.63813877 -1.89899635 1.066915512
		 1.022036552 -2.31326294 1.066915512 0.63826275 -2.53289604 1.066915512 0.43708992 -2.58591461 1.066915512;
	setAttr -s 20 ".ed[0:19]"  0 5 0 0 4 0 4 3 0 5 6 0 6 10 0 3 7 0 7 8 0
		 9 1 0 8 9 0 10 2 0 11 12 0 13 14 0 13 11 0 15 2 0 14 16 0 12 17 0 17 18 0 19 1 0
		 18 19 0 16 15 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 -16 -11 -13 11 14 19 13 -10 -5 -4 -1 1 2 5 6 8 7 -18 -19 -17
		mu 0 20 16 11 10 12 13 15 14 1 9 5 4 0 3 2 6 7 8 19 18 17;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "c_jaw_dn_CTRL_guide" -p "FM_Cam_c_hi_cover";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 0.0039539337158203125 -3.7886366844177242 1.0669155120849618 ;
	setAttr ".sp" -type "double3" 0.0039539337158203125 -3.7886366844177242 1.0669155120849618 ;
createNode mesh -n "c_jaw_dn_CTRL_guideShape" -p "c_jaw_dn_CTRL_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.375 0 0.375 0.10036689
		 0.375 0.019314488 0.40518284 0 0.45843607 0 0.40518284 0.1750624 0.45843607 0.23545432
		 0.48571217 0.25 0.48441321 0 0.375 0.019314488 0.375 0.10036689 0.375 0 0.40518284
		 0 0.48441321 0 0.45843607 0 0.40518284 0.1750624 0.45843607 0.23545432 0.48571217
		 0.25 0.48571217 0.25 0.48441321 0;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".op" yes;
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".vt[0:19]"  -1.79042554 -3.35025978 1.066915512 -1.8068223 -3.65427017 1.066915512
		 -1.83927584 -3.44516563 1.066915512 -1.45239496 -3.32602501 1.066915512 -0.96503687 -3.34326744 1.066915512
		 -1.47247839 -3.97959518 1.066915512 -0.9652009 -4.18116379 1.066915512 -0.56213951 -4.25124741 1.066915512
		 -0.57480097 -3.34326744 1.066915512 1.8471837 -3.44516563 1.066915512 1.81473064 -3.65427017 1.066915512
		 1.79833364 -3.35025978 1.066915512 1.46030331 -3.32602501 1.066915512 0.58270884 -3.34326744 1.066915512
		 0.97294474 -3.34326744 1.066915512 1.48038626 -3.97959518 1.066915512 0.97310925 -4.18116379 1.066915512
		 0.57004786 -4.25124741 1.066915512 0.0039548874 -4.25124741 1.066915512 0.0039548874 -3.34326744 1.066915512;
	setAttr -s 20 ".ed[0:19]"  0 3 0 0 2 0 2 1 0 3 4 0 4 8 0 1 5 0 5 6 0
		 7 18 0 6 7 0 9 10 0 11 12 0 11 9 0 13 19 0 12 14 0 10 15 0 15 16 0 16 17 0 14 13 0
		 18 17 0 19 8 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 19 -5 -4 -1 1 2 5 6 8 7 18 -17 -16 -15 -10 -12 10 13 17 12
		mu 0 20 19 8 4 3 0 2 1 5 6 7 18 17 16 15 10 9 11 12 14 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "c_Rt_cheek_CTRL_guide" -p "FM_Cam_c_hi_cover";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -6.0758411884307861 -0.018381595611571957 1.3867778778076172 ;
	setAttr ".sp" -type "double3" -6.0758411884307861 -0.018381595611571957 1.3867778778076172 ;
createNode mesh -n "c_Rt_cheek_CTRL_guideShape" -p "c_Rt_cheek_CTRL_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.64860266 0.79546607
		 0.62640899 0.75190848 0.59184152 0.71734101 0.54828393 0.69514734 0.5 0.68749994
		 0.45171607 0.69514734 0.40815851 0.71734107 0.37359107 0.75190854 0.3513974 0.79546607
		 0.34374997 0.84375 0.3513974 0.89203393 0.37359107 0.93559146 0.40815854 0.97015893
		 0.4517161 0.9923526 0.5 1 0.54828387 0.9923526 0.59184146 0.97015893 0.62640893 0.93559146
		 0.6486026 0.89203393 0.65625 0.84375;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".vt[0:19]"  -5.56480837 0.16148758 1.38677788 -5.72630167 0.54398727 1.38677788
		 -5.88512564 0.82707787 1.38677788 -6.060809612 1.061096191 1.38677788 -6.2638216 1.23441505 1.38677788
		 -6.45094109 1.30453682 1.38677788 -6.57421398 1.24172783 1.386778 -6.63942719 1.052131653 1.38677788
		 -6.64045286 0.77718353 1.386778 -6.62198734 0.46932602 1.38677788 -6.5776639 0.12983704 1.38677788
		 -6.38706303 -0.40145302 1.38677788 -6.20919991 -0.77683449 1.38677788 -6.0059022903 -1.10395432 1.38677788
		 -5.81130743 -1.3014183 1.38677788 -5.69648981 -1.34129906 1.38677788 -5.5762949 -1.24277306 1.38677788
		 -5.52689362 -1.0073471069 1.38677788 -5.51180077 -0.69867325 1.38677788 -5.51122952 -0.26986504 1.38677788;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 19 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		mu 0 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "c_Lf_cheek_CTRL_guide" -p "FM_Cam_c_hi_cover";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 6.252208948135376 -0.018381595611571957 1.3867778778076172 ;
	setAttr ".sp" -type "double3" 6.252208948135376 -0.018381595611571957 1.3867778778076172 ;
createNode mesh -n "c_Lf_cheek_CTRL_guideShape" -p "c_Lf_cheek_CTRL_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.64860266 0.79546607
		 0.62640899 0.75190848 0.59184152 0.71734101 0.54828393 0.69514734 0.5 0.68749994
		 0.45171607 0.69514734 0.40815851 0.71734107 0.37359107 0.75190854 0.3513974 0.79546607
		 0.34374997 0.84375 0.3513974 0.89203393 0.37359107 0.93559146 0.40815854 0.97015893
		 0.4517161 0.9923526 0.5 1 0.54828387 0.9923526 0.59184146 0.97015893 0.62640893 0.93559146
		 0.6486026 0.89203393 0.65625 0.84375;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".vt[0:19]"  5.74095011 0.16148758 1.38677788 5.90251541 0.54398727 1.38677788
		 6.06140995 0.82707787 1.38677788 6.2371707 1.061096191 1.38677788 6.44027233 1.23441505 1.38677788
		 6.62747431 1.30453682 1.38677788 6.75080109 1.24172783 1.386778 6.81604338 1.052131653 1.38677788
		 6.81707001 0.77718353 1.386778 6.79859638 0.46932602 1.38677788 6.75425243 0.12983704 1.38677788
		 6.56356812 -0.40145302 1.38677788 6.38562679 -0.77683449 1.38677788 6.18223906 -1.10395432 1.38677788
		 5.98755884 -1.3014183 1.38677788 5.8726902 -1.34129906 1.38677788 5.75244188 -1.24277306 1.38677788
		 5.70301914 -1.0073471069 1.38677788 5.68791962 -0.69867325 1.38677788 5.68734789 -0.26986504 1.38677788;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 -19 -18 -17 -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 -20
		mu 0 20 19 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_c_hi_cover_27_guide" -p "FM_Cam_c_hi_cover";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -3.15692138671875 3.3982357978820805 1.2755050659179681 ;
	setAttr ".sp" -type "double3" -3.15692138671875 3.3982357978820805 1.2755050659179681 ;
createNode mesh -n "FM_Cam_c_hi_cover_27_guideShape" -p "FM_Cam_c_hi_cover_27_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 4 ".uvst[0].uvsp[0:3]" -type "float2" 0.375 0.082979284
		 0.625 0.082979284 0.625 0.16385521 0.375 0.16385521;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 4 ".pt[0:3]" -type "float3"  0 -27.812107 4.7683716e-007 
		0 -27.812107 4.7683716e-007 0 -27.812107 4.7683716e-007 0 -27.812107 4.7683716e-007;
	setAttr -s 4 ".vt[0:3]"  -3.58365345 30.82577324 1.27550447 -2.96618676 30.82577324 1.27550447
		 -2.73018932 31.59491348 1.27550447 -3.34765482 31.59491348 1.27550447;
	setAttr -s 4 ".ed[0:3]"  1 2 0 0 3 0 1 0 0 2 3 0;
	setAttr -ch 4 ".fc[0]" -type "polyFaces" 
		f 4 -3 0 3 -2
		mu 0 4 0 1 2 3;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_c_hi_cover_28_guide" -p "FM_Cam_c_hi_cover";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -2.9132356643676758 4.1924300193786621 1.2755050659179679 ;
	setAttr ".sp" -type "double3" -2.9132356643676758 4.1924300193786621 1.2755050659179679 ;
createNode mesh -n "FM_Cam_c_hi_cover_28_guideShape" -p "FM_Cam_c_hi_cover_28_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 4 ".uvst[0].uvsp[0:3]" -type "float2" 0.375 0.16385521
		 0.625 0.16385521 0.625 0.25 0.375 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 4 ".pt[0:3]" -type "float3"  0 -27.812107 4.7683716e-007 
		0 -27.812107 4.7683716e-007 0 -27.812107 4.7683716e-007 0 -27.812107 4.7683716e-007;
	setAttr -s 4 ".vt[0:3]"  -3.096281767 32.41416168 1.27550447 -2.47881651 32.41416168 1.27550447
		 -2.73018932 31.59491348 1.27550447 -3.34765482 31.59491348 1.27550447;
	setAttr -s 4 ".ed[0:3]"  0 1 0 2 1 0 3 0 0 2 3 0;
	setAttr -ch 4 ".fc[0]" -type "polyFaces" 
		f 4 -4 1 -1 -3
		mu 0 4 0 1 2 3;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_c_hi_cover_29_guide" -p "FM_Cam_c_hi_cover";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -3.3959883451461792 2.6190934181213383 1.2755050659179681 ;
	setAttr ".sp" -type "double3" -3.3959883451461792 2.6190934181213383 1.2755050659179681 ;
createNode mesh -n "FM_Cam_c_hi_cover_29_guideShape" -p "FM_Cam_c_hi_cover_29_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 4 ".uvst[0].uvsp[0:3]" -type "float2" 0.375 0 0.625 0 0.625
		 0.082979284 0.375 0.082979284;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 4 ".pt[0:3]" -type "float3"  0 -27.812107 7.1525574e-007 
		0 -27.812107 7.1525574e-007 0 -27.812107 4.7683716e-007 0 -27.812107 4.7683716e-007;
	setAttr -s 4 ".vt[0:3]"  -3.82578993 30.036628723 1.27550447 -3.208323 30.036628723 1.27550447
		 -2.96618676 30.82577324 1.27550447 -3.58365345 30.82577324 1.27550447;
	setAttr -s 4 ".ed[0:3]"  0 1 0 0 3 0 1 2 0 2 3 0;
	setAttr -ch 4 ".fc[0]" -type "polyFaces" 
		f 4 0 2 3 -2
		mu 0 4 0 1 2 3;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_c_hi_cover_30_guide" -p "FM_Cam_c_hi_cover";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 2.9252302646636963 4.1924300193786621 1.2755050659179679 ;
	setAttr ".sp" -type "double3" 2.9252302646636963 4.1924300193786621 1.2755050659179679 ;
createNode mesh -n "FM_Cam_c_hi_cover_30_guideShape" -p "FM_Cam_c_hi_cover_30_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 4 ".uvst[0].uvsp[0:3]" -type "float2" 0.375 0.16385521
		 0.625 0.16385521 0.625 0.25 0.375 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 4 ".pt[0:3]" -type "float3"  0 -27.812107 4.7683716e-007 
		0 -27.812107 4.7683716e-007 0 -27.812107 4.7683716e-007 0 -27.812107 4.7683716e-007;
	setAttr -s 4 ".vt[0:3]"  3.10827637 32.41416168 1.27550447 2.49081087 32.41416168 1.27550447
		 2.74218416 31.59491348 1.27550447 3.35964966 31.59491348 1.27550447;
	setAttr -s 4 ".ed[0:3]"  0 1 0 2 1 0 3 0 0 2 3 0;
	setAttr -ch 4 ".fc[0]" -type "polyFaces" 
		f 4 2 0 -2 3
		mu 0 4 0 3 2 1;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_c_hi_cover_31_guide" -p "FM_Cam_c_hi_cover";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 3.1689162254333496 3.3982357978820805 1.2755050659179681 ;
	setAttr ".sp" -type "double3" 3.1689162254333496 3.3982357978820805 1.2755050659179681 ;
createNode mesh -n "FM_Cam_c_hi_cover_31_guideShape" -p "FM_Cam_c_hi_cover_31_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 4 ".uvst[0].uvsp[0:3]" -type "float2" 0.375 0.082979284
		 0.625 0.082979284 0.625 0.16385521 0.375 0.16385521;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 4 ".pt[0:3]" -type "float3"  0 -27.812107 4.7683716e-007 
		0 -27.812107 4.7683716e-007 0 -27.812107 4.7683716e-007 0 -27.812107 4.7683716e-007;
	setAttr -s 4 ".vt[0:3]"  3.59564829 30.82577324 1.27550447 2.97818136 30.82577324 1.27550447
		 2.74218416 31.59491348 1.27550447 3.35964966 31.59491348 1.27550447;
	setAttr -s 4 ".ed[0:3]"  1 2 0 0 3 0 1 0 0 2 3 0;
	setAttr -ch 4 ".fc[0]" -type "polyFaces" 
		f 4 1 -4 -1 2
		mu 0 4 0 3 2 1;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_c_hi_cover_32_guide" -p "FM_Cam_c_hi_cover";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 3.4079828262329102 2.6190934181213383 1.2755050659179681 ;
	setAttr ".sp" -type "double3" 3.4079828262329102 2.6190934181213383 1.2755050659179681 ;
createNode mesh -n "FM_Cam_c_hi_cover_32_guideShape" -p "FM_Cam_c_hi_cover_32_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 4 ".uvst[0].uvsp[0:3]" -type "float2" 0.375 0 0.625 0 0.625
		 0.082979284 0.375 0.082979284;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 4 ".pt[0:3]" -type "float3"  0 -27.812107 7.1525574e-007 
		0 -27.812107 7.1525574e-007 0 -27.812107 4.7683716e-007 0 -27.812107 4.7683716e-007;
	setAttr -s 4 ".vt[0:3]"  3.83778429 30.036628723 1.27550447 3.22031832 30.036628723 1.27550447
		 2.97818136 30.82577324 1.27550447 3.59564829 30.82577324 1.27550447;
	setAttr -s 4 ".ed[0:3]"  0 1 0 0 3 0 1 2 0 2 3 0;
	setAttr -ch 4 ".fc[0]" -type "polyFaces" 
		f 4 1 -4 -3 -1
		mu 0 4 0 3 2 1;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "c_nose_fold_CTRL_guide" -p "FM_Cam_c_hi_cover";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 0.04808923602104187 5.5883383750915527 1.1075878143310534 ;
	setAttr ".sp" -type "double3" 0.04808923602104187 5.5883383750915527 1.1075878143310534 ;
createNode mesh -n "c_nose_fold_CTRL_guideShape" -p "c_nose_fold_CTRL_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.64860266 0.79546607
		 0.62640899 0.75190848 0.59184152 0.71734101 0.54828393 0.69514734 0.5 0.68749994
		 0.45171607 0.69514734 0.40815851 0.71734107 0.37359107 0.75190854 0.3513974 0.79546607
		 0.34374997 0.84375 0.3513974 0.89203393 0.37359107 0.93559146 0.40815854 0.97015893
		 0.4517161 0.9923526 0.5 1 0.54828387 0.9923526 0.59184146 0.97015893 0.62640893 0.93559146
		 0.6486026 0.89203393 0.65625 0.84375;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".vt[0:19]"  0.54030162 5.71023178 1.10758972 0.4549531 5.81807709 1.10758579
		 0.34221596 5.90017319 1.10758972 0.20272081 5.95226288 1.10758591 0.048089277 5.97021103 1.10758972
		 -0.10654226 5.95226288 1.10758591 -0.24603733 5.90017319 1.10758972 -0.35877439 5.81807709 1.10758591
		 -0.44412285 5.71023178 1.10758972 -0.49369591 5.58760071 1.10758591 -0.49139708 5.46450424 1.10758972
		 -0.42059326 5.3576355 1.10758591 -0.29242849 5.27650452 1.10758781 -0.13093151 5.22441483 1.10758781
		 0.04808927 5.20646667 1.10758781 0.22711003 5.22441483 1.10758781 0.388607 5.27650452 1.10758781
		 0.51677167 5.3576355 1.10758591 0.5875755 5.46450424 1.10758972 0.58987439 5.58760071 1.10758591;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 19 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		mu 0 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "c_Rt_nostril_CTRL_guide" -p "FM_Cam_c_hi_cover";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -0.7522580623626709 3.8536543846130376 1.1075878143310538 ;
	setAttr ".sp" -type "double3" -0.7522580623626709 3.8536543846130376 1.1075878143310538 ;
createNode mesh -n "c_Rt_nostril_CTRL_guideShape" -p "c_Rt_nostril_CTRL_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.64860266 0.79546607
		 0.62640899 0.75190848 0.59184152 0.71734101 0.54828393 0.69514734 0.5 0.68749994
		 0.45171607 0.69514734 0.40815851 0.71734107 0.37359107 0.75190854 0.3513974 0.79546607
		 0.34374997 0.84375 0.3513974 0.89203393 0.37359107 0.93559146 0.40815854 0.97015893
		 0.4517161 0.9923526 0.5 1 0.54828387 0.9923526 0.59184146 0.97015893 0.62640893 0.93559146
		 0.6486026 0.89203393 0.65625 0.84375;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".vt[0:19]"  -0.20368272 3.79422379 1.10758781 -0.25721419 3.93020058 1.10758781
		 -0.3437115 4.051223755 1.10758758 -0.45776466 4.15066528 1.10758758 -0.59575987 4.22271347 1.10758781
		 -0.74657917 4.26124191 1.10758781 -0.89768147 4.26331711 1.10758781 -1.042046547 4.23067856 1.10758781
		 -1.17170739 4.16483688 1.10758781 -1.26666951 4.069885254 1.10758781 -1.30852509 3.95410156 1.10758781
		 -1.27607465 3.82724571 1.10758781 -1.17312038 3.70095444 1.10758781 -1.030433536 3.59054947 1.10758758
		 -0.86883307 3.50945854 1.10758758 -0.68709493 3.45909691 1.10758781 -0.50195408 3.44399261 1.10758781
		 -0.34648627 3.47134399 1.10758758 -0.24215215 3.54582977 1.10758781 -0.19599104 3.65996742 1.10758781;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 19 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		mu 0 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "c_Lf_nostril_CTRL_guide" -p "FM_Cam_c_hi_cover";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 0.90432083606719971 3.8536543846130376 1.1075878143310538 ;
	setAttr ".sp" -type "double3" 0.90432083606719971 3.8536543846130376 1.1075878143310538 ;
createNode mesh -n "c_Lf_nostril_CTRL_guideShape" -p "c_Lf_nostril_CTRL_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.64860266 0.79546607
		 0.62640899 0.75190848 0.59184152 0.71734101 0.54828393 0.69514734 0.5 0.68749994
		 0.45171607 0.69514734 0.40815851 0.71734107 0.37359107 0.75190854 0.3513974 0.79546607
		 0.34374997 0.84375 0.3513974 0.89203393 0.37359107 0.93559146 0.40815854 0.97015893
		 0.4517161 0.9923526 0.5 1 0.54828387 0.9923526 0.59184146 0.97015893 0.62640893 0.93559146
		 0.6486026 0.89203393 0.65625 0.84375;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".vt[0:19]"  0.35574549 3.79422379 1.10758781 0.40927637 3.93020058 1.10758781
		 0.49577367 4.051223755 1.10758758 0.60982752 4.15066528 1.10758758 0.74782228 4.22271347 1.10758781
		 0.89864159 4.26124191 1.10758781 1.049743891 4.26331711 1.10758781 1.19410896 4.23067856 1.10758781
		 1.32377028 4.16483688 1.10758781 1.4187324 4.069885254 1.10758781 1.46058822 3.95410156 1.10758781
		 1.4281373 3.82724571 1.10758781 1.3251828 3.70095444 1.10758781 1.18249619 3.59054947 1.10758758
		 1.020895481 3.50945854 1.10758758 0.83915687 3.45909691 1.10758781 0.65401649 3.44399261 1.10758781
		 0.49854833 3.47134399 1.10758758 0.39421517 3.54582977 1.10758781 0.34805346 3.65996742 1.10758781;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 -19 -18 -17 -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 -20
		mu 0 20 19 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_c_hi_cover_36_guide" -p "FM_Cam_c_hi_cover";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 6.7820096015930176 4.0422520637512207 1.1623191833496085 ;
	setAttr ".sp" -type "double3" 6.7820096015930176 4.0422520637512207 1.1623191833496085 ;
createNode mesh -n "FM_Cam_c_hi_cover_36_guideShape" -p "FM_Cam_c_hi_cover_36_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 21 ".uvst[0].uvsp[0:20]" -type "float2" 0.54828387 0.9923526
		 0.5 1 0.4517161 0.9923526 0.40815854 0.97015893 0.37359107 0.93559146 0.3513974 0.89203393
		 0.34374997 0.84375 0.3513974 0.79546607 0.37359107 0.75190854 0.40815851 0.71734107
		 0.45171607 0.69514734 0.5 0.68749994 0.57182235 0.94124269 0.58500743 0.90346456
		 0.57894909 0.8664726 0.57195091 0.84037805 0.56486845 0.81915122 0.55610275 0.7995128
		 0.55394828 0.76691782 0.54535681 0.70377725 0.541076 0.69400573;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 21 ".vt[0:20]"  6.33654785 5.29383469 1.16231918 6.90059376 5.28092575 1.16231918
		 7.39377117 5.095825195 1.16231918 7.84090376 4.78455734 1.16231918 8.03213501 4.43730927 1.16231918
		 8.064083099 4.051282883 1.16231918 7.95860529 3.66057205 1.16231918 7.65637589 3.30895996 1.16231918
		 7.14904404 3.010503769 1.16231918 6.70032549 2.85878944 1.16231918 6.25623894 2.79067039 1.16231918
		 5.66213369 4.87984848 1.16231918 5.94794655 5.23235703 1.16231918 5.55447531 4.59379196 1.16231918
		 5.5206604 4.29946136 1.16231918 5.5015974 4.059747696 1.16231918 5.4999361 3.84762573 1.16231918
		 5.51520538 3.63450813 1.16231918 5.5702672 3.41260147 1.16231918 5.760427 2.89800072 1.16231918
		 5.80585861 2.81955338 1.16231918;
	setAttr -s 21 ".ed[0:20]"  12 0 0 0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0
		 6 7 0 7 8 0 8 9 0 9 10 0 10 20 0 12 11 0 11 13 0 13 14 0 14 15 0 15 16 0 16 17 0
		 17 18 0 18 19 0 19 20 0;
	setAttr -ch 21 ".fc[0]" -type "polyFaces" 
		f 21 20 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 12 13 14 15 16 17 18 19
		mu 0 21 19 20 11 10 9 8 7 6 5 4 3 2 1 0 12 13 14 15 16 17 18;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_c_hi_cover_37_guide" -p "FM_Cam_c_hi_cover";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 5.2197883129119873 4.0259547233581543 1.1623191833496085 ;
	setAttr ".sp" -type "double3" 5.2197883129119873 4.0259547233581543 1.1623191833496085 ;
createNode mesh -n "FM_Cam_c_hi_cover_37_guideShape" -p "FM_Cam_c_hi_cover_37_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 18 ".uvst[0].uvsp[0:17]" -type "float2" 0.6486026 0.89203393
		 0.57894909 0.8664726 0.58500743 0.90346456 0.62640893 0.93559146 0.57182235 0.94124269
		 0.59184146 0.97015893 0.54828387 0.9923526 0.541076 0.69400573 0.54535681 0.70377725
		 0.54828393 0.69514734 0.55394828 0.76691782 0.59184152 0.71734101 0.55610275 0.7995128
		 0.62640899 0.75190848 0.56486845 0.81915122 0.64860266 0.79546607 0.57195091 0.84037805
		 0.65625 0.84375;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 18 ".vt[0:17]"  4.84978962 4.53275299 1.16231918 5.20060253 4.86592865 1.16231918
		 5.52908993 5.095592499 1.16231918 5.94794655 5.23235703 1.16231918 5.72682762 2.8246212 1.16231918
		 5.071004868 2.97540092 1.16231918 4.66765833 3.25413513 1.16231918 4.49163008 3.60571289 1.16231918
		 4.58835888 4.088697433 1.16231918 5.66213369 4.87984848 1.16231918 5.55447531 4.59379196 1.16231918
		 5.5206604 4.29946136 1.16231918 5.5015974 4.059747696 1.16231918 5.4999361 3.84762573 1.16231918
		 5.51520538 3.63450813 1.16231918 5.5702672 3.41260147 1.16231918 5.760427 2.89800072 1.16231918
		 5.80585861 2.81955338 1.16231918;
	setAttr -s 18 ".ed[0:17]"  0 1 0 1 2 0 2 3 0 4 5 0 5 6 0 6 7 0 7 8 0
		 8 0 0 3 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 17 4 0 16 17 0;
	setAttr -ch 18 ".fc[0]" -type "polyFaces" 
		f 18 -16 -15 -14 -13 -12 -11 -10 -9 -3 -2 -1 -8 -7 -6 -5 -4 -17 -18
		mu 0 18 8 10 12 14 16 1 2 4 6 5 3 0 17 15 13 11 9 7;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_c_hi_cover_38_guide" -p "FM_Cam_c_hi_cover";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -6.6858258247375488 4.0422520637512207 1.1623191833496085 ;
	setAttr ".sp" -type "double3" -6.6858258247375488 4.0422520637512207 1.1623191833496085 ;
createNode mesh -n "FM_Cam_c_hi_cover_38_guideShape" -p "FM_Cam_c_hi_cover_38_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 21 ".uvst[0].uvsp[0:20]" -type "float2" 0.54828387 0.9923526
		 0.5 1 0.4517161 0.9923526 0.40815854 0.97015893 0.37359107 0.93559146 0.3513974 0.89203393
		 0.34374997 0.84375 0.3513974 0.79546607 0.37359107 0.75190854 0.40815851 0.71734107
		 0.45171607 0.69514734 0.5 0.68749994 0.57182235 0.94124269 0.58500743 0.90346456
		 0.57894909 0.8664726 0.57195091 0.84037805 0.56486845 0.81915122 0.55610275 0.7995128
		 0.55394828 0.76691782 0.54535681 0.70377725 0.541076 0.69400573;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 21 ".pt[0:20]" -type "float3"  0 4.131515 6.4561534 0 4.1186061 
		6.4432445 0 3.9335055 6.2581439 0 3.6222377 5.946876 0 3.2749896 5.599628 0 2.8889632 
		5.2136016 0 2.4982524 4.8228908 0 2.1466403 4.4712787 0 1.8481841 4.1728225 0 1.6964698 
		4.0211082 0 1.6283507 3.9529891 0 3.7175288 6.0421672 0 4.0700374 6.3946757 0 3.4314723 
		5.7561107 0 3.1371417 5.4617801 0 2.897428 5.2220664 0 2.6853061 5.0099444 0 2.4721885 
		4.7968268 0 2.2502818 4.5749202 0 1.7356811 4.0603194 0 1.6572337 3.9818721;
	setAttr -s 21 ".vt[0:20]"  -6.24037647 1.16231918 -5.29383421 -6.80440426 1.16231918 -5.28092527
		 -7.29758072 1.16231918 -5.095824718 -7.74471521 1.16231918 -4.78455687 -7.93593979 1.16231918 -4.43730879
		 -7.96789646 1.16231918 -4.051282406 -7.86244154 1.16231918 -3.66057158 -7.56020784 1.16231918 -3.30895948
		 -7.052863598 1.16231918 -3.010503292 -6.60416031 1.16231918 -2.85878897 -6.16005802 1.16231918 -2.79066992
		 -5.56595373 1.16231918 -4.879848 -5.85176277 1.16231918 -5.23235655 -5.45829964 1.16231918 -4.59379148
		 -5.42447948 1.16231918 -4.29946089 -5.4054203 1.16231918 -4.059747219 -5.40375519 1.16231918 -3.84762526
		 -5.41903067 1.16231918 -3.63450766 -5.47408915 1.16231918 -3.41260099 -5.66424465 1.16231918 -2.89800024
		 -5.7096796 1.16231918 -2.8195529;
	setAttr -s 21 ".ed[0:20]"  12 0 0 0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0
		 6 7 0 7 8 0 8 9 0 9 10 0 10 20 0 12 11 0 11 13 0 13 14 0 14 15 0 15 16 0 16 17 0
		 17 18 0 18 19 0 19 20 0;
	setAttr -ch 21 ".fc[0]" -type "polyFaces" 
		f 21 -20 -19 -18 -17 -16 -15 -14 -13 0 1 2 3 4 5 6 7 8 9 10 11 -21
		mu 0 21 19 18 17 16 15 14 13 12 0 1 2 3 4 5 6 7 8 9 10 11 20;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_c_hi_cover_39_guide" -p "FM_Cam_c_hi_cover";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -5.1236059665679932 4.0259547233581543 1.1623191833496085 ;
	setAttr ".sp" -type "double3" -5.1236059665679932 4.0259547233581543 1.1623191833496085 ;
createNode mesh -n "FM_Cam_c_hi_cover_39_guideShape" -p "FM_Cam_c_hi_cover_39_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 18 ".uvst[0].uvsp[0:17]" -type "float2" 0.6486026 0.89203393
		 0.57894909 0.8664726 0.58500743 0.90346456 0.62640893 0.93559146 0.57182235 0.94124269
		 0.59184146 0.97015893 0.54828387 0.9923526 0.541076 0.69400573 0.54535681 0.70377725
		 0.54828393 0.69514734 0.55394828 0.76691782 0.59184152 0.71734101 0.55610275 0.7995128
		 0.62640899 0.75190848 0.56486845 0.81915122 0.64860266 0.79546607 0.57195091 0.84037805
		 0.65625 0.84375;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 18 ".vt[0:17]"  -4.7536068 4.53275299 1.16231918 -5.10441875 4.86592865 1.16231918
		 -5.43290949 5.095592499 1.16231918 -5.85176277 5.23235703 1.16231918 -5.63064671 2.8246212 1.16231918
		 -4.97482395 2.97540092 1.16231918 -4.57147694 3.25413513 1.16231918 -4.39544916 3.60571289 1.16231918
		 -4.49218035 4.088697433 1.16231918 -5.56595373 4.87984848 1.16231918 -5.45829964 4.59379196 1.16231918
		 -5.42447948 4.29946136 1.16231918 -5.4054203 4.059747696 1.16231918 -5.40375519 3.84762573 1.16231918
		 -5.41903067 3.63450813 1.16231918 -5.47408915 3.41260147 1.16231918 -5.66424465 2.89800072 1.16231918
		 -5.7096796 2.81955338 1.16231918;
	setAttr -s 18 ".ed[0:17]"  0 1 0 1 2 0 2 3 0 4 5 0 5 6 0 6 7 0 7 8 0
		 8 0 0 3 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 17 4 0 16 17 0;
	setAttr -ch 18 ".fc[0]" -type "polyFaces" 
		f 18 17 16 3 4 5 6 7 0 1 2 8 9 10 11 12 13 14 15
		mu 0 18 8 7 9 11 13 15 17 0 3 5 6 4 2 1 16 14 12 10;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_c_hi_cover_40_guide" -p "FM_Cam_c_hi_cover";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 0.047238826751708984 -4.8434662818908691 1.1075878143310558 ;
	setAttr ".sp" -type "double3" 0.047238826751708984 -4.8434662818908691 1.1075878143310558 ;
createNode mesh -n "FM_Cam_c_hi_cover_40_guideShape" -p "FM_Cam_c_hi_cover_40_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.5 0.68749994 0.45171607
		 0.69514734 0.40815851 0.71734107 0.37359107 0.75190854 0.3513974 0.79546607 0.34374997
		 0.84375 0.3513974 0.89203393 0.37359107 0.93559146 0.40815854 0.97015893 0.4517161
		 0.9923526 0.5 1 0.4517161 0.9923526 0.40815854 0.97015893 0.37359107 0.93559146 0.3513974
		 0.89203393 0.34374997 0.84375 0.3513974 0.79546607 0.37359107 0.75190854 0.40815851
		 0.71734107 0.45171607 0.69514734;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".vt[0:19]"  0.048089027 -4.51120758 1.10758781 0.18220329 -4.51317596 1.10758781
		 0.30349302 -4.53395462 1.10758781 0.4227972 -4.57479668 1.10758781 0.52835655 -4.6391964 1.10758781
		 0.58179855 -4.7465744 1.10758781 0.55965519 -4.89016151 1.10758781 0.46024132 -5.036691666 1.10758781
		 0.34342289 -5.11478615 1.10758781 0.20335579 -5.16010666 1.10758781 0.048089027 -5.17572403 1.10758781
		 -0.086452007 -4.51317596 1.10758781 -0.20812893 -4.53395462 1.10758781 -0.3278141 -4.57479668 1.10758781
		 -0.43370819 -4.6391964 1.10758781 -0.4873209 -4.7465744 1.10758781 -0.46510696 -4.89016151 1.10758781
		 -0.36537838 -5.036691666 1.10758781 -0.24818707 -5.11478615 1.10758781 -0.10767269 -5.16010666 1.10758781;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 0 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 10 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 19 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 10 11 12 13 14 15 16 17 18
		mu 0 20 19 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "c_Rt_nosewing_CTRL_guide1" -p "FM_Cam_c_hi_cover";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -2.4150632619857788 5.1716933250427246 0.95069503784179576 ;
	setAttr ".sp" -type "double3" -2.4150632619857788 5.1716933250427246 0.95069503784179576 ;
createNode mesh -n "c_Rt_nosewing_CTRL_guide1Shape" -p "c_Rt_nosewing_CTRL_guide1";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 7 ".uvst[0].uvsp[0:6]" -type "float2" 0.375 0.25 0.53125
		 0.4375 0.875 0 0.875 1 0.375 0.25 0.40625 0.25 0.875 1;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 7 ".vt[0:6]"  -2.52392697 5.62794495 0.95069504 -1.96543074 5.24072647 0.95069504
		 -2.86469579 5.34503174 0.95069504 -2.49171519 5.39706802 0.95069504 -2.39662361 4.71544266 0.95069504
		 -2.42883539 4.94632339 0.95069504 -2.8018105 4.89428711 0.95069504;
	setAttr -s 7 ".ed[0:6]"  0 3 0 0 1 0 2 3 0 4 5 0 4 1 0 6 5 0 6 2 0;
	setAttr -ch 7 ".fc[0]" -type "polyFaces" 
		f 7 -2 0 -3 -7 5 -4 4
		mu 0 7 1 0 2 3 6 5 4;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_c_hi_cover_42_guide" -p "FM_Cam_c_hi_cover";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -1.9007757902145386 5.242957592010498 0.95069503784179576 ;
	setAttr ".sp" -type "double3" -1.9007757902145386 5.242957592010498 0.95069503784179576 ;
createNode mesh -n "FM_Cam_c_hi_cover_42_guideShape" -p "FM_Cam_c_hi_cover_42_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 4 ".uvst[0].uvsp[0:3]" -type "float2" 0.375 0.25 0.625
		 0.25 0.625 0.5 0.375 0.5;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 4 ".pt[0:3]" -type "float3"  0 -27.812107 -4.7683716e-007 
		0 -27.812107 -4.7683716e-007 0 -27.812107 -4.7683716e-007 0 -27.812107 -4.7683716e-007;
	setAttr -s 4 ".vt[0:3]"  -1.99820328 33.45847702 0.95069551 -1.90512514 32.64007568 0.95069551
		 -1.89642668 33.47005463 0.95069551 -1.8033483 32.65165329 0.95069551;
	setAttr -s 4 ".ed[0:3]"  0 1 0 2 3 0 0 2 0 1 3 0;
	setAttr -ch 4 ".fc[0]" -type "polyFaces" 
		f 4 0 3 -2 -3
		mu 0 4 0 1 2 3;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "c_Lf_nosewing_CTRL_guide1" -p "FM_Cam_c_hi_cover";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 2.410304069519043 5.1716933250427246 0.95069503784179576 ;
	setAttr ".sp" -type "double3" 2.410304069519043 5.1716933250427246 0.95069503784179576 ;
createNode mesh -n "c_Lf_nosewing_CTRL_guide1Shape" -p "c_Lf_nosewing_CTRL_guide1";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 7 ".uvst[0].uvsp[0:6]" -type "float2" 0.375 0.25 0.40625
		 0.25 0.875 1 0.375 0.25 0.53125 0.4375 0.875 1 0.875 0;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 7 ".vt[0:6]"  2.5191679 5.62794495 0.95069504 1.96067142 5.24072647 0.95069504
		 2.85993671 5.34503174 0.95069504 2.48695564 5.39706802 0.95069504 2.3918643 4.71544266 0.95069504
		 2.42407608 4.94632339 0.95069504 2.79705143 4.89428711 0.95069504;
	setAttr -s 7 ".ed[0:6]"  0 3 0 0 1 0 2 6 0 2 3 0 4 5 0 4 1 0 6 5 0;
	setAttr -ch 7 ".fc[0]" -type "polyFaces" 
		f 7 -1 1 -6 4 -7 -3 3
		mu 0 7 1 0 4 3 6 5 2;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_c_hi_cover_44_guide" -p "FM_Cam_c_hi_cover";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 1.8960165977478027 5.242957592010498 0.95069503784179576 ;
	setAttr ".sp" -type "double3" 1.8960165977478027 5.242957592010498 0.95069503784179576 ;
createNode mesh -n "FM_Cam_c_hi_cover_44_guideShape" -p "FM_Cam_c_hi_cover_44_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 4 ".uvst[0].uvsp[0:3]" -type "float2" 0.375 0.25 0.625
		 0.25 0.625 0.5 0.375 0.5;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 4 ".pt[0:3]" -type "float3"  0 -27.812107 -4.7683716e-007 
		0 -27.812107 -4.7683716e-007 0 -27.812107 -4.7683716e-007 0 -27.812107 -4.7683716e-007;
	setAttr -s 4 ".vt[0:3]"  1.99344397 33.45847702 0.95069551 1.90036583 32.64007568 0.95069551
		 1.89166737 33.47005463 0.95069551 1.79858923 32.65165329 0.95069551;
	setAttr -s 4 ".ed[0:3]"  0 1 0 2 3 0 0 2 0 1 3 0;
	setAttr -ch 4 ".fc[0]" -type "polyFaces" 
		f 4 2 1 -4 -1
		mu 0 4 0 3 2 1;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_c_hi_tooth" -p "FM_Cam_c_hi_face";
	setAttr ".rp" -type "double3" -4.8461991548538208 -11.422832489013672 2.3481931686401394 ;
	setAttr ".sp" -type "double3" -4.8461991548538208 -11.422832489013672 2.3481931686401394 ;
createNode transform -n "UpperTooth_Ctrl_guide" -p "FM_Cam_c_hi_tooth";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -4.843996524810791 -8.853764533996582 2.344572067260744 ;
	setAttr ".sp" -type "double3" -4.843996524810791 -8.853764533996582 2.344572067260744 ;
createNode mesh -n "UpperTooth_Ctrl_guideShape" -p "UpperTooth_Ctrl_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 16 ".uvst[0].uvsp[0:15]" -type "float2" 0.4740586 0.18274811
		 0.4740586 0.25 0.4481172 0.18274811 0.4481172 0.25 0.48702931 0.25 0.48702931 0.18274811
		 0.48702931 0.18274811 0.48702931 0.25 0.4481172 0.18274811 0.4740586 0.18274811 0.4740586
		 0.25 0.4481172 0.25 0.48702931 0.25 0.48702931 0.18274811 0.4481172 0.21637405 0.4481172
		 0.21637405;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 16 ".vt[0:15]"  -3.8023181 -8.74126244 2.34457254 -3.78235769 -9.17807388 2.34457254
		 -3.40144157 -9.17215729 2.34457254 -3.42856312 -9.009098053 2.34457254 -4.29641485 -8.57593918 2.34457254
		 -4.285923 -9.17765236 2.34457254 -5.88567448 -8.74126244 2.34457254 -5.90563488 -9.17807388 2.34457254
		 -6.286551 -9.17215729 2.34457254 -6.25942898 -9.009098053 2.34457254 -5.39157772 -8.57593918 2.34457254
		 -5.40206957 -9.17765236 2.34457254 -4.84399509 -8.52945518 2.34457254 -4.84399509 -9.17765236 2.34457254
		 -3.35426044 -9.09062767 2.34457254 -6.3337326 -9.09062767 2.34457254;
	setAttr -s 16 ".ed[0:15]"  3 0 0 0 4 0 11 13 0 1 2 0 3 14 0 5 1 0 9 6 0
		 6 10 0 7 8 0 9 15 0 10 12 0 11 7 0 12 4 0 13 5 0 14 2 0 15 8 0;
	setAttr -ch 16 ".fc[0]" -type "polyFaces" 
		f 16 3 -15 -5 0 1 -13 -11 -8 -7 9 15 -9 -12 2 13 5
		mu 0 16 0 2 14 3 1 4 12 7 10 11 15 8 9 6 13 5;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "LowerTooth_Ctrl_guide" -p "FM_Cam_c_hi_tooth";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -4.8439962863922119 -13.99261474609375 2.3445720672607453 ;
	setAttr ".sp" -type "double3" -4.8439962863922119 -13.99261474609375 2.3445720672607453 ;
createNode mesh -n "LowerTooth_Ctrl_guideShape" -p "LowerTooth_Ctrl_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 16 ".uvst[0].uvsp[0:15]" -type "float2" 0.4740586 0.18274811
		 0.4740586 0.25 0.4481172 0.18274811 0.4481172 0.25 0.48702931 0.25 0.48702931 0.18274811
		 0.48702931 0.18274811 0.48702931 0.25 0.4481172 0.18274811 0.4740586 0.18274811 0.4740586
		 0.25 0.4481172 0.25 0.48702931 0.25 0.48702931 0.18274811 0.4481172 0.21637405 0.4481172
		 0.21637405;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 16 ".vt[0:15]"  -3.8023181 -14.10513878 2.34457254 -3.78235769 -13.6690197 2.34457254
		 -3.4014411 -13.67495728 2.34457254 -3.42856312 -13.83768463 2.34457254 -4.29641485 -14.27020454 2.34457254
		 -4.28592348 -13.66943932 2.34457254 -5.88567448 -14.10513878 2.34457254 -5.90563488 -13.6690197 2.34457254
		 -6.28655148 -13.67495728 2.34457254 -6.25942898 -13.83768463 2.34457254 -5.39157772 -14.27020454 2.34457254
		 -5.40206909 -13.66943932 2.34457254 -4.84399509 -14.31620979 2.34457254 -4.84399509 -13.66943932 2.34457254
		 -3.35425997 -13.75635147 2.34457254 -6.3337326 -13.75635147 2.34457254;
	setAttr -s 16 ".ed[0:15]"  3 0 0 0 4 0 11 13 0 1 2 0 3 14 0 5 1 0 9 6 0
		 6 10 0 7 8 0 9 15 0 10 12 0 11 7 0 12 4 0 13 5 0 14 2 0 15 8 0;
	setAttr -ch 16 ".fc[0]" -type "polyFaces" 
		f 16 -6 -14 -3 11 8 -16 -10 6 7 10 12 -2 -1 4 14 -4
		mu 0 16 0 5 13 6 9 8 15 11 10 7 12 4 1 3 14 2;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "LowerTooth_second01_Ctrl_guide" -p "FM_Cam_c_hi_tooth";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr ".ove" yes;
	setAttr ".rp" -type "double3" -8.2334909439086914 -12.489205837249756 2.3518142700195312 ;
	setAttr ".sp" -type "double3" -8.2334909439086914 -12.489205837249756 2.3518142700195312 ;
createNode mesh -n "LowerTooth_second01_Ctrl_guideShape" -p "LowerTooth_second01_Ctrl_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 12 ".uvst[0].uvsp[0:11]" -type "float2" 0.50156593 0.045372829
		 0.50156593 0.18823496 0.50156593 0.11680389 0.4924826 0.25 0.4337413 0.25 0.4337413
		 0 0.4924826 0 0.375 0.18823496 0.375 0.25 0.375 0.11680389 0.375 0.045372833 0.375
		 0;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 12 ".pt[0:11]" -type "float3"  -1.054827 0 0 -1.054827 0 
		0 -1.054827 0 0 -1.054827 0 0 -1.054827 0 0 -1.054827 0 0 -1.054827 0 0 -1.054827 
		0 0 -1.054827 0 0 -1.054827 0 0 -1.054827 0 0 -1.054827 0 0;
	setAttr -s 12 ".vt[0:11]"  -7.53511238 -13.19222069 2.35181475 -7.50499296 -11.60804176 2.35181475
		 -7.85496092 -11.79451752 2.35181475 -7.75681019 -12.86434364 2.35181475 -7.94773865 -12.34043694 2.35181475
		 -6.697052 -11.6819725 2.35181475 -6.49370146 -12.030701637 2.35181379 -6.41035891 -12.5580616 2.35181475
		 -6.40958977 -12.86752987 2.35181379 -6.5607481 -13.25699329 2.35181379 -7.10596371 -11.59059525 2.35181475
		 -7.12211895 -13.38781643 2.35181379;
	setAttr -s 12 ".ed[0:11]"  0 11 0 1 10 0 0 3 0 2 1 0 3 4 0 4 2 0 5 6 0
		 6 7 0 7 8 0 8 9 0 10 5 0 11 9 0;
	setAttr -ch 12 ".fc[0]" -type "polyFaces" 
		f 12 -3 0 11 -10 -9 -8 -7 -11 -2 -4 -6 -5
		mu 0 12 10 11 5 6 0 2 1 3 4 8 7 9;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "UpperTooth_second01_Ctrl_guide" -p "FM_Cam_c_hi_tooth";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr ".ove" yes;
	setAttr ".rp" -type "double3" -8.0604498386383057 -10.372311592102051 2.3518147468566895 ;
	setAttr ".sp" -type "double3" -8.0604498386383057 -10.372311592102051 2.3518147468566895 ;
createNode mesh -n "UpperTooth_second01_Ctrl_guideShape" -p "UpperTooth_second01_Ctrl_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 12 ".uvst[0].uvsp[0:11]" -type "float2" 0.50156593 0.045372829
		 0.50156593 0.18823496 0.50156593 0.11680389 0.4924826 0.25 0.4337413 0.25 0.4337413
		 0 0.4924826 0 0.375 0.18823496 0.375 0.25 0.375 0.11680389 0.375 0.045372833 0.375
		 0;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 12 ".pt[0:11]" -type "float3"  -0.81499976 0 0 -0.81499976 
		0 0 -0.81499976 0 0 -0.81499976 0 0 -0.81499976 0 0 -0.81499976 0 0 -0.81499976 0 
		0 -0.81499976 0 0 -0.81499976 0 0 -0.81499976 0 0 -0.81499976 0 0 -0.81499976 0 0;
	setAttr -s 12 ".vt[0:11]"  -7.71317005 -11.22370529 2.35181475 -7.42585754 -9.5801754 2.35181475
		 -7.73625708 -9.81611061 2.35181475 -7.98432684 -10.95518112 2.35181475 -8.026875496 -10.40159798 2.35181475
		 -6.76629639 -9.52550888 2.35181475 -6.46402502 -9.87423897 2.35181475 -6.47960377 -10.40159798 2.35181475
		 -6.557971 -10.85944557 2.35181475 -6.8080492 -11.18955803 2.35181475 -7.13564014 -9.51326942 2.35181475
		 -7.19136333 -11.23135376 2.35181475;
	setAttr -s 12 ".ed[0:11]"  0 11 0 1 10 0 0 3 0 2 1 0 3 4 0 4 2 0 5 6 0
		 6 7 0 7 8 0 8 9 0 10 5 0 11 9 0;
	setAttr -ch 12 ".fc[0]" -type "polyFaces" 
		f 12 -3 0 11 -10 -9 -8 -7 -11 -2 -4 -6 -5
		mu 0 12 10 11 5 6 0 2 1 3 4 8 7 9;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "UpperTooth_second02_Ctrl_guide" -p "FM_Cam_c_hi_tooth";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr ".ove" yes;
	setAttr ".rp" -type "double3" -6.4895238876342773 -10.310423851013184 2.3518147468566895 ;
	setAttr ".sp" -type "double3" -6.4895238876342773 -10.310423851013184 2.3518147468566895 ;
createNode mesh -n "UpperTooth_second02_Ctrl_guideShape" -p "UpperTooth_second02_Ctrl_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 12 ".uvst[0].uvsp[0:11]" -type "float2" 0.51064932 0 0.56782466
		 0 0.50156593 0.045372829 0.50156593 0.18823496 0.56782466 0.25 0.51064932 0.25 0.50156593
		 0.11680389 0.625 0 0.625 0.045372833 0.625 0.11680389 0.625 0.18823496 0.625 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 12 ".pt[0:11]" -type "float3"  -0.78743887 0 0 -0.78743887 
		0 0 -0.78743887 0 0 -0.78743887 0 0 -0.78743887 0 0 -0.78743887 0 0 -0.78743887 0 
		0 -0.78743887 0 0 -0.78743887 0 0 -0.78743887 0 0 -0.78743887 0 0 -0.78743887 0 0;
	setAttr -s 12 ".vt[0:11]"  -4.84619904 -9.81611061 2.35181475 -4.84619904 -10.98709679 2.35181475
		 -4.84619904 -10.40159798 2.35181475 -5.24939632 -11.33772659 2.35181475 -5.1749382 -9.34176064 2.35181475
		 -6.46402502 -9.87423897 2.35181475 -6.47960377 -10.40159798 2.35181475 -6.557971 -10.85944557 2.35181475
		 -6.11737919 -9.42658043 2.35181475 -6.37008953 -11.22071457 2.35181475 -5.80974579 -11.35368347 2.35181475
		 -5.6461587 -9.26716423 2.35181475;
	setAttr -s 12 ".ed[0:11]"  1 2 0 2 0 0 3 1 0 0 4 0 5 6 0 6 7 0 8 11 0
		 8 5 0 9 10 0 7 9 0 10 3 0 11 4 0;
	setAttr -ch 12 ".fc[0]" -type "polyFaces" 
		f 12 9 8 10 2 0 1 3 -12 -7 7 4 5
		mu 0 12 2 0 1 7 8 9 10 11 4 5 3 6;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "UpperTooth_second04_Ctrl_guide" -p "FM_Cam_c_hi_tooth";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr ".ove" yes;
	setAttr ".rp" -type "double3" -3.2134793996810913 -10.310423851013184 2.3518147468566895 ;
	setAttr ".sp" -type "double3" -3.2134793996810913 -10.310423851013184 2.3518147468566895 ;
createNode mesh -n "UpperTooth_second04_Ctrl_guideShape" -p "UpperTooth_second04_Ctrl_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 12 ".uvst[0].uvsp[0:11]" -type "float2" 0.625 0 0.625 0.25
		 0.625 0.18823496 0.625 0.045372833 0.625 0.11680389 0.50156593 0.18823496 0.50156593
		 0.11680389 0.50156593 0.045372829 0.51064932 0.25 0.51064932 0 0.56782466 0 0.56782466
		 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 12 ".pt[0:11]" -type "float3"  0.77683353 0 0 0.77683353 
		0 0 0.77683353 0 0 0.77683353 0 0 0.77683353 0 0 0.77683353 0 0 0.77683353 0 0 0.77683353 
		0 0 0.77683353 0 0 0.77683353 0 0 0.77683353 0 0 0.77683353 0 0;
	setAttr -s 12 ".vt[0:11]"  -4.44300175 -11.33772659 2.35181475 -4.51745987 -9.34176064 2.35181475
		 -4.84619904 -9.81611061 2.35181475 -4.84619904 -10.98709679 2.35181475 -4.84619904 -10.40159798 2.35181475
		 -3.22837305 -9.87423897 2.35181475 -3.21279454 -10.40159798 2.35181475 -3.13442683 -10.85944557 2.35181475
		 -3.57501912 -9.42658043 2.35181475 -3.3223083 -11.22071457 2.35181475 -3.88265228 -11.35368347 2.35181475
		 -4.046239376 -9.26716423 2.35181475;
	setAttr -s 12 ".ed[0:11]"  0 3 0 2 1 0 3 4 0 4 2 0 5 6 0 6 7 0 8 11 0
		 8 5 0 9 10 0 7 9 0 10 0 0 11 1 0;
	setAttr -ch 12 ".fc[0]" -type "polyFaces" 
		f 12 -3 -1 -11 -9 -10 -6 -5 -8 6 11 -2 -4
		mu 0 12 4 3 0 10 9 7 6 5 8 11 1 2;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "UpperTooth_second05_Ctrl_guide" -p "FM_Cam_c_hi_tooth";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr ".ove" yes;
	setAttr ".rp" -type "double3" -1.6449926495552063 -10.372311592102051 2.3518147468566895 ;
	setAttr ".sp" -type "double3" -1.6449926495552063 -10.372311592102051 2.3518147468566895 ;
createNode mesh -n "UpperTooth_second05_Ctrl_guideShape" -p "UpperTooth_second05_Ctrl_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 12 ".uvst[0].uvsp[0:11]" -type "float2" 0.375 0 0.375 0.25
		 0.375 0.18823496 0.375 0.045372833 0.375 0.11680389 0.4924826 0.25 0.50156593 0.18823496
		 0.50156593 0.11680389 0.50156593 0.045372829 0.4924826 0 0.4337413 0.25 0.4337413
		 0;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 12 ".pt[0:11]" -type "float3"  0.80195534 0 0 0.80195534 
		0 0 0.80195534 0 0 0.80195534 0 0 0.80195534 0 0 0.80195534 0 0 0.80195534 0 0 0.80195534 
		0 0 0.80195534 0 0 0.80195534 0 0 0.80195534 0 0 0.80195534 0 0;
	setAttr -s 12 ".vt[0:11]"  -1.97922826 -11.22370529 2.35181475 -2.26654053 -9.5801754 2.35181475
		 -1.956141 -9.81611061 2.35181475 -1.70807123 -10.95518112 2.35181475 -1.66552281 -10.40159798 2.35181475
		 -2.92610168 -9.52550888 2.35181475 -3.22837305 -9.87423897 2.35181475 -3.21279454 -10.40159798 2.35181475
		 -3.13442683 -10.85944557 2.35181475 -2.88434911 -11.18955803 2.35181475 -2.55675817 -9.51326942 2.35181475
		 -2.5010345 -11.23135376 2.35181475;
	setAttr -s 12 ".ed[0:11]"  0 11 0 1 10 0 0 3 0 2 1 0 3 4 0 4 2 0 5 6 0
		 6 7 0 7 8 0 8 9 0 10 5 0 11 9 0;
	setAttr -ch 12 ".fc[0]" -type "polyFaces" 
		f 12 -1 2 4 5 3 1 10 6 7 8 9 -12
		mu 0 12 11 0 3 4 2 1 10 5 6 7 8 9;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "UpperTooth_second03_Ctrl_guide" -p "FM_Cam_c_hi_tooth";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr ".ove" yes;
	setAttr ".rp" -type "double3" -4.8461990356445313 -10.34017276763916 2.3587198257446289 ;
	setAttr ".sp" -type "double3" -4.8461990356445313 -10.34017276763916 2.3587198257446289 ;
createNode mesh -n "UpperTooth_second03_Ctrl_guideShape" -p "UpperTooth_second03_Ctrl_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 12 ".uvst[0].uvsp[0:11]" -type "float2" 0.51064932 0 0.56782466
		 0 0.50156593 0.045372829 0.50156593 0.18823496 0.56782466 0.25 0.51064932 0.25 0.50156593
		 0.11680389 0.625 0 0.625 0.045372833 0.625 0.11680389 0.625 0.18823496 0.625 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 12 ".pt[0:11]" -type "float3"  0.75 0 0 0.75 0 0 0.75 0 
		0 0.89633441 0.027967328 0 0.85791928 -0.092848994 0.014124068 0.86782598 0.058128357 
		0 0.88340473 0 0 0.96177208 -0.12765121 0 0.82175487 0 0 0.98598987 -0.070190936 
		0.0018144785 0.93061006 -0.085818 0 0.80788237 0.0263202 -0.00031411339;
	setAttr -s 12 ".vt[0:11]"  -4.84619904 -9.81611061 2.35181475 -4.84619904 -10.98709679 2.35181475
		 -4.84619904 -10.40159798 2.35181475 -5.24939632 -11.33772659 2.35181475 -5.1749382 -9.34176064 2.35181475
		 -6.46402502 -9.87423897 2.35181475 -6.47960377 -10.40159798 2.35181475 -6.557971 -10.85944557 2.35181475
		 -6.11737919 -9.42658043 2.35181475 -6.37008953 -11.22071457 2.35181475 -5.80974579 -11.35368347 2.35181475
		 -5.6461587 -9.26716423 2.35181475;
	setAttr -s 12 ".ed[0:11]"  1 2 0 2 0 0 3 1 0 0 4 0 5 6 0 6 7 0 8 11 0
		 8 5 0 9 10 0 7 9 0 10 3 0 11 4 0;
	setAttr -ch 12 ".fc[0]" -type "polyFaces" 
		f 12 9 8 10 2 0 1 3 -12 -7 7 4 5
		mu 0 12 2 0 1 7 8 9 10 11 4 5 3 6;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "LowerTooth_second02_Ctrl_guide" -p "FM_Cam_c_hi_tooth";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr ".ove" yes;
	setAttr ".rp" -type "double3" -6.6487135887145996 -12.536131858825684 2.3518142700195312 ;
	setAttr ".sp" -type "double3" -6.6487135887145996 -12.536131858825684 2.3518142700195312 ;
createNode mesh -n "LowerTooth_second02_Ctrl_guideShape" -p "LowerTooth_second02_Ctrl_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 12 ".uvst[0].uvsp[0:11]" -type "float2" 0.51064932 0 0.56782466
		 0 0.50156593 0.045372829 0.50156593 0.18823496 0.56782466 0.25 0.51064932 0.25 0.50156593
		 0.11680389 0.625 0 0.625 0.045372833 0.625 0.11680389 0.625 0.18823496 0.625 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 12 ".pt[0:11]" -type "float3"  -0.99854755 0 0 -0.99854755 
		0 0 -0.99854755 0 0 -0.99854755 0 0 -0.99854755 0 0 -0.99854755 0 0 -0.99854755 0 
		0 -0.99854755 0 0 -0.99854755 0 0 -0.99854755 0 0 -0.99854755 0 0 -0.99854755 0 0;
	setAttr -s 12 ".vt[0:11]"  -4.80663061 -11.97257423 2.35181475 -4.80663061 -13.074316025 2.35181475
		 -4.80663061 -12.5580616 2.35181475 -5.05155611 -13.43483829 2.35181379 -5.085909367 -11.62682152 2.35181475
		 -6.49370146 -12.030701637 2.35181379 -6.41035891 -12.5580616 2.35181475 -6.40958977 -12.86752987 2.35181379
		 -6.3152194 -11.65228844 2.35181475 -6.21181631 -13.33761024 2.35181475 -5.71082497 -13.56949997 2.35181475
		 -5.66594267 -11.50276375 2.35181475;
	setAttr -s 12 ".ed[0:11]"  1 2 0 2 0 0 3 1 0 0 4 0 5 6 0 6 7 0 8 11 0
		 8 5 0 9 10 0 7 9 0 10 3 0 11 4 0;
	setAttr -ch 12 ".fc[0]" -type "polyFaces" 
		f 12 4 5 9 8 10 2 0 1 3 -12 -7 7
		mu 0 12 3 6 2 0 1 7 8 9 10 11 4 5;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "LowerTooth_second04_Ctrlguide" -p "FM_Cam_c_hi_tooth";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr ".ove" yes;
	setAttr ".rp" -type "double3" -3.2360996007919312 -12.536131858825684 2.3518142700195312 ;
	setAttr ".sp" -type "double3" -3.2360996007919312 -12.536131858825684 2.3518142700195312 ;
createNode mesh -n "LowerTooth_second04_CtrlguideShape" -p "LowerTooth_second04_Ctrlguide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 12 ".uvst[0].uvsp[0:11]" -type "float2" 0.51064932 0 0.56782466
		 0 0.50156593 0.045372829 0.50156593 0.18823496 0.56782466 0.25 0.51064932 0.25 0.50156593
		 0.11680389 0.625 0 0.625 0.045372833 0.625 0.11680389 0.625 0.18823496 0.625 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 12 ".pt[0:11]" -type "float3"  0.72699636 0 0 0.72699636 
		0 0 0.72699636 0 0 0.72699636 0 0 0.72699636 0 0 0.72699636 0 0 0.72699636 0 0 0.72699636 
		0 0 0.72699636 0 0 0.72699636 0 0 0.72699636 0 0 0.72699636 0 0;
	setAttr -s 12 ".vt[0:11]"  -4.80663061 -11.97257423 2.35181475 -4.80663061 -13.074316025 2.35181475
		 -4.80663061 -12.5580616 2.35181475 -4.56170654 -13.43483829 2.35181379 -4.52735329 -11.62682152 2.35181475
		 -3.11956143 -12.030701637 2.35181379 -3.20290375 -12.5580616 2.35181475 -3.20367289 -12.86752987 2.35181379
		 -3.29804349 -11.65228844 2.35181475 -3.40144634 -13.33761024 2.35181475 -3.90243769 -13.56949997 2.35181475
		 -3.94731998 -11.50276375 2.35181475;
	setAttr -s 12 ".ed[0:11]"  1 2 0 2 0 0 3 1 0 0 4 0 5 6 0 6 7 0 8 11 0
		 8 5 0 9 10 0 7 9 0 10 3 0 11 4 0;
	setAttr -ch 12 ".fc[0]" -type "polyFaces" 
		f 12 -8 6 11 -4 -2 -1 -3 -11 -9 -10 -6 -5
		mu 0 12 3 5 4 11 10 9 8 7 1 0 2 6;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "LowerTooth_second05_Ctrl_guide" -p "FM_Cam_c_hi_tooth";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr ".ove" yes;
	setAttr ".rp" -type "double3" -1.6617548763751984 -12.489205837249756 2.3518142700195312 ;
	setAttr ".sp" -type "double3" -1.6617548763751984 -12.489205837249756 2.3518142700195312 ;
createNode mesh -n "LowerTooth_second05_Ctrl_guideShape" -p "LowerTooth_second05_Ctrl_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 12 ".uvst[0].uvsp[0:11]" -type "float2" 0.50156593 0.045372829
		 0.50156593 0.18823496 0.50156593 0.11680389 0.4924826 0.25 0.4337413 0.25 0.4337413
		 0 0.4924826 0 0.375 0.18823496 0.375 0.25 0.375 0.11680389 0.375 0.045372833 0.375
		 0;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 12 ".pt[0:11]" -type "float3"  0.77284354 0 0 0.77284354 
		0 0 0.77284354 0 0 0.77284354 0 0 0.77284354 0 0 0.77284354 0 0 0.77284354 0 0 0.77284354 
		0 0 0.77284354 0 0 0.77284354 0 0 0.77284354 0 0 0.77284354 0 0;
	setAttr -s 12 ".vt[0:11]"  -2.078150272 -13.19222069 2.35181475 -2.10826993 -11.60804176 2.35181475
		 -1.75830197 -11.79451752 2.35181475 -1.85645366 -12.86434364 2.35181475 -1.66552401 -12.34043694 2.35181475
		 -2.91621089 -11.6819725 2.35181475 -3.11956143 -12.030701637 2.35181379 -3.20290375 -12.5580616 2.35181475
		 -3.20367289 -12.86752987 2.35181379 -3.052514553 -13.25699329 2.35181379 -2.50729895 -11.59059525 2.35181475
		 -2.4911437 -13.38781643 2.35181379;
	setAttr -s 12 ".ed[0:11]"  0 11 0 1 10 0 0 3 0 2 1 0 3 4 0 4 2 0 5 6 0
		 6 7 0 7 8 0 8 9 0 10 5 0 11 9 0;
	setAttr -ch 12 ".fc[0]" -type "polyFaces" 
		f 12 4 5 3 1 10 6 7 8 9 -12 -1 2
		mu 0 12 10 9 7 8 4 3 1 2 0 6 5 11;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "LowerTooth_second03_Ctrl_guide" -p "FM_Cam_c_hi_tooth";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr ".ove" yes;
	setAttr ".rp" -type "double3" -4.9319713115692139 -12.543268203735352 2.3518142700195312 ;
	setAttr ".sp" -type "double3" -4.9319713115692139 -12.543268203735352 2.3518142700195312 ;
createNode mesh -n "LowerTooth_second03_Ctrl_guideShape" -p "LowerTooth_second03_Ctrl_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 12 ".uvst[0].uvsp[0:11]" -type "float2" 0.51064932 0 0.56782466
		 0 0.50156593 0.045372829 0.50156593 0.18823496 0.56782466 0.25 0.51064932 0.25 0.50156593
		 0.11680389 0.625 0 0.625 0.045372833 0.625 0.11680389 0.625 0.18823496 0.625 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 12 ".pt[0:11]" -type "float3"  -0.92950112 0 0 -0.92950112 
		0 0 -0.92950112 0 0 -0.92950112 0 0 -0.92950112 0 0 -1.0276171 0.071362995 0 -0.92490727 
		0.042817798 0 -0.93842942 -0.17840749 0 -1.0793631 0.057090398 0 -1.0151365 -0.099908195 
		0 -1.0365455 -0.035681497 0 -0.97945511 0.021408899 0;
	setAttr -s 12 ".vt[0:11]"  -4.80663061 -11.97257423 2.35181475 -4.80663061 -13.074316025 2.35181475
		 -4.80663061 -12.5580616 2.35181475 -4.56170654 -13.43483829 2.35181379 -4.52735329 -11.62682152 2.35181475
		 -3.11956143 -12.030701637 2.35181379 -3.20290375 -12.5580616 2.35181475 -3.20367289 -12.86752987 2.35181379
		 -3.29804349 -11.65228844 2.35181475 -3.40144634 -13.33761024 2.35181475 -3.90243769 -13.56949997 2.35181475
		 -3.94731998 -11.50276375 2.35181475;
	setAttr -s 12 ".ed[0:11]"  1 2 0 2 0 0 3 1 0 0 4 0 5 6 0 6 7 0 8 11 0
		 8 5 0 9 10 0 7 9 0 10 3 0 11 4 0;
	setAttr -ch 12 ".fc[0]" -type "polyFaces" 
		f 12 -8 6 11 -4 -2 -1 -3 -11 -9 -10 -6 -5
		mu 0 12 3 5 4 11 10 9 8 7 1 0 2 6;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_c_hi_tongue" -p "FM_Cam_c_hi_face";
	setAttr ".rp" -type "double3" -13.511857032775879 -10.758709192276001 2.3445720672607444 ;
	setAttr ".sp" -type "double3" -13.511857032775879 -10.758709192276001 2.3445720672607444 ;
createNode transform -n "FM_Cam_c_hi_tongue_1_guide" -p "FM_Cam_c_hi_tongue";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -11.729801177978516 -8.6704714298248291 2.344572067260744 ;
	setAttr ".sp" -type "double3" -11.729801177978516 -8.6704714298248291 2.344572067260744 ;
createNode mesh -n "FM_Cam_c_hi_tongue_1_guideShape" -p "FM_Cam_c_hi_tongue_1_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode mesh -n "polySurfaceShape3" -p "FM_Cam_c_hi_tongue_1_guide";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 6 ".uvst[0].uvsp[0:5]" -type "float2" 0.4115586 0.18274811
		 0.4115586 0.25 0.4481172 0.25 0.4481172 0.18274811 0.375 0.18274811 0.375 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 6 ".vt[0:5]"  -11.41718006 -8.48535347 2.34457254 -12.4664402 -7.69257927 2.34457207
		 -11.88123322 -7.98057175 2.34457207 -12.4664402 -9.64836311 2.34457254 -11.72980118 -9.64836311 2.34457254
		 -10.99316216 -9.64836311 2.34457254;
	setAttr -s 6 ".ed[0:5]"  0 2 0 5 0 0 1 3 0 2 1 0 3 4 0 4 5 0;
	setAttr -ch 6 ".fc[0]" -type "polyFaces" 
		f 6 5 1 0 3 2 4
		mu 0 6 0 4 5 1 2 3;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 3;
	setAttr ".dsm" 2;
createNode transform -n "FM_Cam_c_hi_tongue_2_guide" -p "FM_Cam_c_hi_tongue";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -15.293912410736084 -8.6704714298248291 2.344572067260744 ;
	setAttr ".sp" -type "double3" -15.293912410736084 -8.6704714298248291 2.344572067260744 ;
createNode mesh -n "FM_Cam_c_hi_tongue_2_guideShape" -p "FM_Cam_c_hi_tongue_2_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode mesh -n "polySurfaceShape1" -p "FM_Cam_c_hi_tongue_2_guide";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 6 ".uvst[0].uvsp[0:5]" -type "float2" 0.4115586 0.18274811
		 0.4481172 0.18274811 0.4481172 0.25 0.4115586 0.25 0.375 0.18274811 0.375 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 6 ".vt[0:5]"  -15.60653305 -8.48535347 2.34457254 -14.55727291 -7.69257927 2.34457207
		 -15.14247704 -7.98057175 2.34457207 -15.29390907 -9.64836311 2.34457254 -14.55727291 -9.64836311 2.34457254
		 -16.03055191 -9.64836311 2.34457254;
	setAttr -s 6 ".ed[0:5]"  0 2 0 5 0 0 1 4 0 2 1 0 4 3 0 3 5 0;
	setAttr -ch 6 ".fc[0]" -type "polyFaces" 
		f 6 -5 -3 -4 -1 -2 -6
		mu 0 6 0 1 2 3 5 4;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 3;
	setAttr ".dsm" 2;
createNode transform -n "FM_Cam_c_hi_tongue_4_guide" -p "FM_Cam_c_hi_tongue";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -11.729801177978516 -10.650235176086426 2.3445720672607444 ;
	setAttr ".sp" -type "double3" -11.729801177978516 -10.650235176086426 2.3445720672607444 ;
createNode mesh -n "FM_Cam_c_hi_tongue_4_guideShape" -p "FM_Cam_c_hi_tongue_4_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode mesh -n "polySurfaceShape6" -p "FM_Cam_c_hi_tongue_4_guide";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 6 ".uvst[0].uvsp[0:5]" -type "float2" 0.4115586 0.11944372
		 0.4115586 0.18274811 0.4481172 0.18274811 0.4481172 0.11944372 0.375 0.11944372 0.375
		 0.18274811;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 6 ".vt[0:5]"  -10.99316216 -9.64836311 2.34457254 -10.99316216 -11.50335312 2.34457254
		 -12.4664402 -9.64836311 2.34457254 -12.4664402 -11.65210724 2.34457254 -11.72980118 -9.64836311 2.34457254
		 -11.72980118 -11.56285477 2.34457254;
	setAttr -s 6 ".ed[0:5]"  1 0 0 2 4 0 3 5 0 2 3 0 4 0 0 5 1 0;
	setAttr -ch 6 ".fc[0]" -type "polyFaces" 
		f 6 5 0 -5 -2 3 2
		mu 0 6 0 4 5 1 2 3;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 3;
	setAttr ".dsm" 2;
createNode transform -n "FM_Cam_c_hi_tongue_5_guide" -p "FM_Cam_c_hi_tongue";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -15.293912410736084 -10.650235176086426 2.3445720672607444 ;
	setAttr ".sp" -type "double3" -15.293912410736084 -10.650235176086426 2.3445720672607444 ;
createNode mesh -n "FM_Cam_c_hi_tongue_5_guideShape" -p "FM_Cam_c_hi_tongue_5_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode mesh -n "polySurfaceShape4" -p "FM_Cam_c_hi_tongue_5_guide";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 6 ".uvst[0].uvsp[0:5]" -type "float2" 0.4115586 0.11944372
		 0.4481172 0.11944372 0.4481172 0.18274811 0.4115586 0.18274811 0.375 0.11944372 0.375
		 0.18274811;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 6 ".vt[0:5]"  -16.03055191 -9.64836311 2.34457254 -16.03055191 -11.50335312 2.34457254
		 -14.55727291 -9.64836311 2.34457254 -14.55727291 -11.65210724 2.34457254 -15.29390907 -9.64836311 2.34457254
		 -15.29390907 -11.56285477 2.34457254;
	setAttr -s 6 ".ed[0:5]"  1 0 0 2 4 0 3 5 0 2 3 0 4 0 0 5 1 0;
	setAttr -ch 6 ".fc[0]" -type "polyFaces" 
		f 6 -3 -4 1 4 -1 -6
		mu 0 6 0 1 2 3 5 4;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 3;
	setAttr ".dsm" 2;
createNode transform -n "c_tongue_CTRL_guide" -p "FM_Cam_c_hi_tongue";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -13.458370685577393 -6.9701056480407706 2.3445720672607435 ;
	setAttr ".sp" -type "double3" -13.458370685577393 -6.9701056480407706 2.3445720672607435 ;
createNode mesh -n "c_tongue_CTRL_guideShape" -p "c_tongue_CTRL_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 16 ".uvst[0].uvsp[0:15]" -type "float2" 0.4740586 0.18274811
		 0.4740586 0.25 0.4481172 0.18274811 0.4481172 0.25 0.48702931 0.25 0.48702931 0.18274811
		 0.48702931 0.18274811 0.48702931 0.25 0.4481172 0.18274811 0.4740586 0.18274811 0.4740586
		 0.25 0.4481172 0.25 0.48702931 0.25 0.48702931 0.18274811 0.4481172 0.21637405 0.4481172
		 0.21637405;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 16 ".vt[0:15]"  -12.41669273 -6.81189919 2.34457207 -12.39673233 -7.42616653 2.34457207
		 -12.015815735 -7.41784477 2.34457207 -12.042938232 -7.18854332 2.34457207 -12.91078949 -6.57941246 2.34457207
		 -12.90029716 -7.42557335 2.34457207 -14.50004864 -6.81189919 2.34457207 -14.52000904 -7.42616653 2.34457207
		 -14.90092468 -7.41784477 2.34457207 -14.87380409 -7.18854332 2.34457207 -14.0059518814 -6.57941246 2.34457207
		 -14.016444206 -7.42557335 2.34457207 -13.45836926 -6.51404381 2.34457207 -13.45836926 -7.42557335 2.34457207
		 -11.96863461 -7.30319405 2.34457207 -14.94810677 -7.30319405 2.34457207;
	setAttr -s 16 ".ed[0:15]"  3 0 0 0 4 0 11 13 0 1 2 0 3 14 0 5 1 0 9 6 0
		 6 10 0 7 8 0 9 15 0 10 12 0 11 7 0 12 4 0 13 5 0 14 2 0 15 8 0;
	setAttr -ch 16 ".fc[0]" -type "polyFaces" 
		f 16 -8 -7 9 15 -9 -12 2 13 5 3 -15 -5 0 1 -13 -11
		mu 0 16 7 10 11 15 8 9 6 13 5 0 2 14 3 1 4 12;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_c_hi_tongue_10_guide" -p "FM_Cam_c_hi_tongue";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -15.293912410736084 -12.979033470153809 2.3445720672607449 ;
	setAttr ".sp" -type "double3" -15.293912410736084 -12.979033470153809 2.3445720672607449 ;
createNode mesh -n "FM_Cam_c_hi_tongue_10_guideShape" -p "FM_Cam_c_hi_tongue_10_guide";
	setAttr -k off ".v";
	setAttr -s 2 ".iog[0].og";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode mesh -n "polySurfaceShape7" -p "FM_Cam_c_hi_tongue_10_guide";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0:1]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 12 ".uvst[0].uvsp[0:11]" -type "float2" 0.4115586 0 0.4481172
		 0 0.4481172 0.048114859 0.4115586 0.048114859 0.375 0 0.375 0.048114855 0.4115586
		 0.048114859 0.4481172 0.048114859 0.4481172 0.11944372 0.4115586 0.11944372 0.375
		 0.048114855 0.375 0.11944372;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 9 ".pt[0:8]" -type "float3"  0 0 0.014545794 0 0 0.014546755 
		0 0 0.014545794 0 0 0.014546755 0 0 0.014545794 0 0.22949089 0.014545794 0 0 0.014545794 
		0 0 0.014545794 0 0 0.014545794;
	setAttr -s 9 ".vt[0:8]"  -15.22787285 -13.76747894 2.34457254 -15.66477776 -12.75742817 2.34457159
		 -15.11102676 -13.17545319 2.34457254 -14.86282349 -14.19344807 2.34457159 -14.55727291 -14.45471382 2.34457254
		 -14.55727291 -13.59347916 2.34457254 -14.55727291 -11.65210724 2.34457254 -15.29390907 -11.56285477 2.34457254
		 -16.03055191 -11.50335312 2.34457254;
	setAttr -s 10 ".ed[0:9]"  0 3 0 0 1 0 5 2 0 2 1 0 3 4 0 5 4 0 1 8 0
		 6 5 0 6 7 0 7 8 0;
	setAttr -s 2 -ch 12 ".fc[0:1]" -type "polyFaces" 
		f 6 4 -6 2 3 -2 0
		mu 0 6 0 1 2 3 5 4
		f 6 -3 -8 8 9 -7 -4
		mu 0 6 6 7 8 9 11 10;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 3;
	setAttr ".dsm" 2;
createNode transform -n "FM_Cam_c_hi_tongue_11_guide" -p "FM_Cam_c_hi_tongue";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -11.729801177978516 -12.979033470153809 2.3445720672607449 ;
	setAttr ".sp" -type "double3" -11.729801177978516 -12.979033470153809 2.3445720672607449 ;
createNode mesh -n "FM_Cam_c_hi_tongue_11_guideShape" -p "FM_Cam_c_hi_tongue_11_guide";
	setAttr -k off ".v";
	setAttr -s 2 ".iog[0].og";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode mesh -n "polySurfaceShape9" -p "FM_Cam_c_hi_tongue_11_guide";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0:1]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 12 ".uvst[0].uvsp[0:11]" -type "float2" 0.4115586 0.048114859
		 0.4115586 0.11944372 0.4481172 0.11944372 0.4481172 0.048114859 0.375 0.048114855
		 0.375 0.11944372 0.4115586 0 0.4115586 0.048114859 0.4481172 0.048114859 0.4481172
		 0 0.375 0 0.375 0.048114855;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 9 ".pt[0:8]" -type "float3"  0 0 0.014545794 0 0 0.014545794 
		0 0.22949089 0.014545794 0 0 0.014545794 0 0 0.014545794 0 0 0.014546755 0 0 0.014545794 
		0 0 0.014546755 0 0 0.014545794;
	setAttr -s 9 ".vt[0:8]"  -11.72980118 -11.56285477 2.34457254 -12.4664402 -11.65210724 2.34457254
		 -12.4664402 -13.59347916 2.34457254 -11.91268635 -13.17545319 2.34457254 -10.99316216 -11.50335312 2.34457254
		 -11.35893536 -12.75742817 2.34457159 -11.7958374 -13.76747894 2.34457254 -12.16089249 -14.19344807 2.34457159
		 -12.4664402 -14.45471382 2.34457254;
	setAttr -s 10 ".ed[0:9]"  5 4 0 1 2 0 1 0 0 2 3 0 0 4 0 3 5 0 6 7 0
		 6 5 0 7 8 0 2 8 0;
	setAttr -s 2 -ch 12 ".fc[0:1]" -type "polyFaces" 
		f 6 5 0 -5 -3 1 3
		mu 0 6 0 4 5 1 2 3
		f 6 -7 7 -6 -4 9 -9
		mu 0 6 6 10 11 7 8 9;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 3;
	setAttr ".dsm" 2;
createNode transform -n "c_tongue_joint2_guide" -p "FM_Cam_c_hi_tongue";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" 1 0.99999999999999978 0.99999999999999978 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -13.511855125427246 -9.0473773238570363 2.3591182231903072 ;
	setAttr ".sp" -type "double3" -13.511855125427246 -9.0473773238570381 2.3591182231903076 ;
	setAttr ".spt" -type "double3" 0 1.7763568394002501e-015 -4.4408920985006252e-016 ;
createNode mesh -n "c_tongue_joint2_guideShape" -p "c_tongue_joint2_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".dr" 1;
createNode mesh -n "polySurfaceShape11" -p "c_tongue_joint2_guide";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 4 ".uvst[0].uvsp[0:3]" -type "float2" 0 0 1 0 0 1 1 1;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 4 ".pt[0:3]" -type "float3"  -0.54541779 -0.70640182 4.4408921e-016 
		0.54541492 -0.69839478 -7.4505806e-009 -0.54541779 -1.0213614 1.6670674e-007 0.54541588 
		-1.0613956 4.4408921e-016;
	setAttr -s 4 ".vt[0:3]"  -14.011855125 -8.17770386 2.35911822 -13.011855125 -8.17770386 2.35911822
		 -14.011855125 -7.17770386 2.35911822 -13.011855125 -7.17770386 2.35911822;
	setAttr -s 4 ".ed[0:3]"  0 1 0 0 2 0 1 3 0 2 3 0;
	setAttr -ch 4 ".fc[0]" -type "polyFaces" 
		f 4 0 2 -4 -2
		mu 0 4 0 1 3 2;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode transform -n "c_tongue_joint5_guide" -p "FM_Cam_c_hi_tongue";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" 1 0.99999999999999978 0.99999999999999978 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -13.511856555938721 -10.592145442962645 2.3591182231903072 ;
	setAttr ".sp" -type "double3" -13.511856555938721 -10.592145442962646 2.3591182231903076 ;
	setAttr ".spt" -type "double3" 0 1.7763568394002501e-015 -4.4408920985006252e-016 ;
createNode mesh -n "c_tongue_joint5_guideShape" -p "c_tongue_joint5_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 6 ".uvst[0].uvsp[0:5]" -type "float2" 0 0 1 0 0 1 1 1 0.5
		 0 0.52860308 1;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 6 ".pt[0:5]" -type "float3"  0 -0.65719509 4.4408921e-016 
		0 -0.68543816 4.4408921e-016 0 -0.72766399 4.4408921e-016 0 -0.66398525 4.4408921e-016 
		0 -0.70739746 4.4408921e-016 -9.5367432e-007 -0.75395012 4.4408921e-016;
	setAttr -s 6 ".vt[0:5]"  -14.55727291 -10.19959641 2.35911822 -12.4664402 -10.14659882 2.35911822
		 -14.55727291 -9.47193146 2.35911822 -12.4664402 -9.48261261 2.35911822 -13.51185608 -10.33029556 2.35911822
		 -13.51185513 -9.57634544 2.35911822;
	setAttr -s 6 ".ed[0:5]"  0 4 0 0 2 0 1 3 0 2 5 0 4 1 0 5 3 0;
	setAttr -ch 6 ".fc[0]" -type "polyFaces" 
		f 6 0 4 2 -6 -4 -2
		mu 0 6 0 4 1 3 5 2;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode mesh -n "polySurfaceShape11" -p "c_tongue_joint5_guide";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 4 ".uvst[0].uvsp[0:3]" -type "float2" 0 0 1 0 0 1 1 1;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 4 ".pt[0:3]" -type "float3"  -0.54541779 -0.70640182 4.4408921e-016 
		0.54541492 -0.69839478 -7.4505806e-009 -0.54541779 -1.0213614 1.6670674e-007 0.54541588 
		-1.0613956 4.4408921e-016;
	setAttr -s 4 ".vt[0:3]"  -14.011855125 -8.17770386 2.35911822 -13.011855125 -8.17770386 2.35911822
		 -14.011855125 -7.17770386 2.35911822 -13.011855125 -7.17770386 2.35911822;
	setAttr -s 4 ".ed[0:3]"  0 1 0 0 2 0 1 3 0 2 3 0;
	setAttr -ch 4 ".fc[0]" -type "polyFaces" 
		f 4 0 2 -4 -2
		mu 0 4 0 1 3 2;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode transform -n "c_tongue_joint3_guide" -p "FM_Cam_c_hi_tongue";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 0 -0.67517270374469252 0 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" 1 0.99999999999999978 0.99999999999999978 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -13.511855125427246 -9.0473773238570363 2.3591182231903072 ;
	setAttr ".sp" -type "double3" -13.511855125427246 -9.0473773238570381 2.3591182231903076 ;
	setAttr ".spt" -type "double3" 0 1.7763568394002501e-015 -4.4408920985006252e-016 ;
createNode mesh -n "c_tongue_joint3_guideShape" -p "c_tongue_joint3_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 5 ".uvst[0].uvsp[0:4]" -type "float2" 0 0 1 0 0 1 1 1 0.5
		 0;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 5 ".pt[0:4]" -type "float3"  0 0.087345958 0 0 0.068659663 
		0 0 -0.0098677874 0 0 0.038173556 0 0 -0.0210706 0;
	setAttr -s 5 ".vt[0:4]"  -14.55727291 -8.88410568 2.35911822 -12.4664402 -8.87609863 2.35911822
		 -14.55727291 -8.19906521 2.35911846 -12.46643925 -8.2390995 2.35911822 -13.51185608 -8.88010216 2.35911822;
	setAttr -s 5 ".ed[0:4]"  0 4 0 0 2 0 1 3 0 2 3 0 4 1 0;
	setAttr -ch 5 ".fc[0]" -type "polyFaces" 
		f 5 0 4 2 -4 -2
		mu 0 5 0 4 1 3 2;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode mesh -n "polySurfaceShape11" -p "c_tongue_joint3_guide";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 4 ".uvst[0].uvsp[0:3]" -type "float2" 0 0 1 0 0 1 1 1;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 4 ".pt[0:3]" -type "float3"  -0.54541779 -0.70640182 4.4408921e-016 
		0.54541492 -0.69839478 -7.4505806e-009 -0.54541779 -1.0213614 1.6670674e-007 0.54541588 
		-1.0613956 4.4408921e-016;
	setAttr -s 4 ".vt[0:3]"  -14.011855125 -8.17770386 2.35911822 -13.011855125 -8.17770386 2.35911822
		 -14.011855125 -7.17770386 2.35911822 -13.011855125 -7.17770386 2.35911822;
	setAttr -s 4 ".ed[0:3]"  0 1 0 0 2 0 1 3 0 2 3 0;
	setAttr -ch 4 ".fc[0]" -type "polyFaces" 
		f 4 0 2 -4 -2
		mu 0 4 0 1 3 2;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode transform -n "c_tongue_joint4_guide" -p "FM_Cam_c_hi_tongue";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" 1 0.99999999999999978 0.99999999999999978 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -13.511856079101562 -10.330295562744139 2.3591182231903072 ;
	setAttr ".sp" -type "double3" -13.511856079101562 -10.330295562744141 2.3591182231903076 ;
	setAttr ".spt" -type "double3" 0 1.7763568394002501e-015 -4.4408920985006252e-016 ;
createNode mesh -n "c_tongue_joint4_guideShape" -p "c_tongue_joint4_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 6 ".uvst[0].uvsp[0:5]" -type "float2" 0 0 1 0 0 1 1 1 0.5
		 0 0.52860308 1;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 6 ".vt[0:5]"  -14.55727291 -10.19959641 2.35911822 -12.4664402 -10.14659882 2.35911822
		 -14.55727291 -9.47193146 2.35911822 -12.4664402 -9.48261261 2.35911822 -13.51185608 -10.33029556 2.35911822
		 -13.51185513 -9.57634544 2.35911822;
	setAttr -s 6 ".ed[0:5]"  0 4 0 0 2 0 1 3 0 2 5 0 4 1 0 5 3 0;
	setAttr -ch 6 ".fc[0]" -type "polyFaces" 
		f 6 0 4 2 -6 -4 -2
		mu 0 6 0 4 1 3 5 2;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode mesh -n "polySurfaceShape11" -p "c_tongue_joint4_guide";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 4 ".uvst[0].uvsp[0:3]" -type "float2" 0 0 1 0 0 1 1 1;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 4 ".pt[0:3]" -type "float3"  -0.54541779 -0.70640182 4.4408921e-016 
		0.54541492 -0.69839478 -7.4505806e-009 -0.54541779 -1.0213614 1.6670674e-007 0.54541588 
		-1.0613956 4.4408921e-016;
	setAttr -s 4 ".vt[0:3]"  -14.011855125 -8.17770386 2.35911822 -13.011855125 -8.17770386 2.35911822
		 -14.011855125 -7.17770386 2.35911822 -13.011855125 -7.17770386 2.35911822;
	setAttr -s 4 ".ed[0:3]"  0 1 0 0 2 0 1 3 0 2 3 0;
	setAttr -ch 4 ".fc[0]" -type "polyFaces" 
		f 4 0 2 -4 -2
		mu 0 4 0 1 3 2;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode transform -n "c_tongue_joint12_guide" -p "FM_Cam_c_hi_tongue";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" 1 0.99999999999999978 0.99999999999999978 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -13.511856555938721 -14.5829963684082 2.3591183423995967 ;
	setAttr ".sp" -type "double3" -13.511856555938721 -14.582996368408203 2.3591183423995972 ;
	setAttr ".spt" -type "double3" 0 3.5527136788005001e-015 -4.4408920985006252e-016 ;
createNode mesh -n "c_tongue_joint12_guideShape" -p "c_tongue_joint12_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 8 ".uvst[0].uvsp[0:7]" -type "float2" 0 0 1 0 0 1 1 1 0.5
		 0 0.52860308 1 0.27854645 1 0.75222301 1;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  0.5227077 -3.42307 0 -0.52270722 
		-3.4078512 4.7683716e-007 -1.2218952e-006 -3.6131897 0 -1.2218952e-006 -3.6131897 
		0 -2.682209e-007 -3.3404903 2.3841858e-007 -2.1755695e-006 -3.4227858 0 -0.52271008 
		-3.3219986 0 0.52270484 -3.2610569 0;
	setAttr -s 8 ".vt[0:7]"  -14.55727196 -11.44847679 2.35911846 -12.46643925 -11.46369553 2.35911798
		 -14.55727196 -10.84152412 2.35911822 -12.46643925 -10.84152412 2.35911822 -13.51185513 -11.6628828 2.35911822
		 -13.51185417 -11.035443306 2.35911822 -14.034563065 -10.90156269 2.35911822 -12.98914528 -10.90156269 2.35911822;
	setAttr -s 8 ".ed[0:7]"  0 2 0 1 3 0 2 6 0 5 7 0 0 4 0 4 1 0 6 5 0
		 7 3 0;
	setAttr -ch 8 ".fc[0]" -type "polyFaces" 
		f 8 4 5 1 -8 -4 -7 -3 -1
		mu 0 8 0 4 1 3 7 5 6 2;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode mesh -n "polySurfaceShape11" -p "c_tongue_joint12_guide";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 4 ".uvst[0].uvsp[0:3]" -type "float2" 0 0 1 0 0 1 1 1;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 4 ".pt[0:3]" -type "float3"  -0.54541779 -0.70640182 4.4408921e-016 
		0.54541492 -0.69839478 -7.4505806e-009 -0.54541779 -1.0213614 1.6670674e-007 0.54541588 
		-1.0613956 4.4408921e-016;
	setAttr -s 4 ".vt[0:3]"  -14.011855125 -8.17770386 2.35911822 -13.011855125 -8.17770386 2.35911822
		 -14.011855125 -7.17770386 2.35911822 -13.011855125 -7.17770386 2.35911822;
	setAttr -s 4 ".ed[0:3]"  0 1 0 0 2 0 1 3 0 2 3 0;
	setAttr -ch 4 ".fc[0]" -type "polyFaces" 
		f 4 0 2 -4 -2
		mu 0 4 0 1 3 2;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode transform -n "c_tongue_joint9_guide" -p "FM_Cam_c_hi_tongue";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" 1 0.99999999999999978 0.99999999999999978 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -13.511856555938721 -13.042253494262692 2.3591182231903072 ;
	setAttr ".sp" -type "double3" -13.511856555938721 -13.042253494262695 2.3591182231903076 ;
	setAttr ".spt" -type "double3" 0 3.5527136788005001e-015 -4.4408920985006252e-016 ;
createNode mesh -n "c_tongue_joint9_guideShape" -p "c_tongue_joint9_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 6 ".uvst[0].uvsp[0:5]" -type "float2" 0 0 1 0 0 1 1 1 0.5
		 0 0.52860308 1;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 7 ".pt[0:6]" -type "float3"  0 -1.3508062 -2.3841858e-007 
		0 -1.3747978 2.3841858e-007 0 -1.3507633 2.3841858e-007 0 -1.311553 -2.3841858e-007 
		9.5367432e-007 -1.3726912 4.4408921e-016 -9.5367432e-007 -1.3311586 4.4408921e-016 
		0 0 0;
	setAttr -s 6 ".vt[0:5]"  -14.55727291 -11.88511086 2.35911846 -12.4664402 -11.86111927 2.35911798
		 -14.55727291 -11.30513191 2.35911822 -12.4664402 -11.32035065 2.35911822 -13.51185608 -12.079912186 2.35911822
		 -13.51185513 -11.51953793 2.35911822;
	setAttr -s 6 ".ed[0:5]"  0 2 0 1 3 0 2 5 0 5 3 0 0 4 0 4 1 0;
	setAttr -ch 6 ".fc[0]" -type "polyFaces" 
		f 6 4 5 1 -4 -3 -1
		mu 0 6 0 4 1 3 5 2;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode mesh -n "polySurfaceShape11" -p "c_tongue_joint9_guide";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 4 ".uvst[0].uvsp[0:3]" -type "float2" 0 0 1 0 0 1 1 1;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 4 ".pt[0:3]" -type "float3"  -0.54541779 -0.70640182 4.4408921e-016 
		0.54541492 -0.69839478 -7.4505806e-009 -0.54541779 -1.0213614 1.6670674e-007 0.54541588 
		-1.0613956 4.4408921e-016;
	setAttr -s 4 ".vt[0:3]"  -14.011855125 -8.17770386 2.35911822 -13.011855125 -8.17770386 2.35911822
		 -14.011855125 -7.17770386 2.35911822 -13.011855125 -7.17770386 2.35911822;
	setAttr -s 4 ".ed[0:3]"  0 1 0 0 2 0 1 3 0 2 3 0;
	setAttr -ch 4 ".fc[0]" -type "polyFaces" 
		f 4 0 2 -4 -2
		mu 0 4 0 1 3 2;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode transform -n "c_tongue_joint1_guide" -p "FM_Cam_c_hi_tongue";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" 1 0.99999999999999978 0.99999999999999978 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -13.51237154006958 -7.9286458492279035 2.3591182231903072 ;
	setAttr ".sp" -type "double3" -13.51237154006958 -7.9286458492279053 2.3591182231903076 ;
	setAttr ".spt" -type "double3" 0 1.7763568394002501e-015 -4.4408920985006252e-016 ;
createNode mesh -n "c_tongue_joint1_guideShape" -p "c_tongue_joint1_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 7 ".uvst[0].uvsp[0:6]" -type "float2" 0 0 1 0 0 1 1 1 0.5
		 0 0.27854645 1 0.75222301 1;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 7 ".pt[0:6]" -type "float3"  1.0131226 6.3931413 0 -1.0762144 
		6.3371983 0 2.0908325 6.2724638 0 -2.0908329 6.1605797 0 -0.028362356 6.2462511 0 
		2.0906565 5.1802158 0 -2.0918629 5.1483889 0;
	setAttr -s 7 ".vt[0:6]"  -14.0022687912 -14.011343002 2.35911822 -12.95834923 -13.95540047 2.35911822
		 -14.55727291 -13.96504307 2.35911822 -12.4664402 -13.85315895 2.35911822 -13.48349285 -13.92395496 2.35911822
		 -14.55727386 -13.4193058 2.35911822 -12.4664402 -13.34739876 2.35911822;
	setAttr -s 7 ".ed[0:6]"  0 2 0 1 3 0 2 5 0 0 4 0 4 1 0 5 6 0 6 3 0;
	setAttr -ch 7 ".fc[0]" -type "polyFaces" 
		f 7 3 4 1 -7 -6 -3 -1
		mu 0 7 0 4 1 3 6 5 2;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode mesh -n "polySurfaceShape11" -p "c_tongue_joint1_guide";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 4 ".uvst[0].uvsp[0:3]" -type "float2" 0 0 1 0 0 1 1 1;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 4 ".pt[0:3]" -type "float3"  -0.54541779 -0.70640182 4.4408921e-016 
		0.54541492 -0.69839478 -7.4505806e-009 -0.54541779 -1.0213614 1.6670674e-007 0.54541588 
		-1.0613956 4.4408921e-016;
	setAttr -s 4 ".vt[0:3]"  -14.011855125 -8.17770386 2.35911822 -13.011855125 -8.17770386 2.35911822
		 -14.011855125 -7.17770386 2.35911822 -13.011855125 -7.17770386 2.35911822;
	setAttr -s 4 ".ed[0:3]"  0 1 0 0 2 0 1 3 0 2 3 0;
	setAttr -ch 4 ".fc[0]" -type "polyFaces" 
		f 4 0 2 -4 -2
		mu 0 4 0 1 3 2;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode transform -n "c_tongue_joint6_guide" -p "FM_Cam_c_hi_tongue";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" 1 0.99999999999999978 0.99999999999999978 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -13.511856555938721 -11.248456001281737 2.3591182231903072 ;
	setAttr ".sp" -type "double3" -13.511856555938721 -11.248456001281738 2.3591182231903076 ;
	setAttr ".spt" -type "double3" 0 1.7763568394002501e-015 -4.4408920985006252e-016 ;
createNode mesh -n "c_tongue_joint6_guideShape" -p "c_tongue_joint6_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 8 ".uvst[0].uvsp[0:7]" -type "float2" 0 0 1 0 0 1 1 1 0.5
		 0 0.52860308 1 0.25 0 0.73203826 0;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".vt[0:7]"  -14.55727196 -11.46896362 2.35911822 -12.4664402 -11.46896362 2.35911822
		 -14.55727291 -10.85878277 2.35911822 -12.4664402 -10.8340292 2.35911822 -13.51185513 -11.6628828 2.35911822
		 -13.51185608 -11.039685249 2.35911822 -14.034564018 -11.52900219 2.35911822 -12.98914623 -11.52900219 2.35911822;
	setAttr -s 8 ".ed[0:7]"  0 6 0 0 2 0 1 3 0 2 5 0 4 7 0 5 3 0 6 4 0
		 7 1 0;
	setAttr -ch 8 ".fc[0]" -type "polyFaces" 
		f 8 0 6 4 7 2 -6 -4 -2
		mu 0 8 0 6 4 7 1 3 5 2;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode mesh -n "polySurfaceShape11" -p "c_tongue_joint6_guide";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 4 ".uvst[0].uvsp[0:3]" -type "float2" 0 0 1 0 0 1 1 1;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 4 ".pt[0:3]" -type "float3"  -0.54541779 -0.70640182 4.4408921e-016 
		0.54541492 -0.69839478 -7.4505806e-009 -0.54541779 -1.0213614 1.6670674e-007 0.54541588 
		-1.0613956 4.4408921e-016;
	setAttr -s 4 ".vt[0:3]"  -14.011855125 -8.17770386 2.35911822 -13.011855125 -8.17770386 2.35911822
		 -14.011855125 -7.17770386 2.35911822 -13.011855125 -7.17770386 2.35911822;
	setAttr -s 4 ".ed[0:3]"  0 1 0 0 2 0 1 3 0 2 3 0;
	setAttr -ch 4 ".fc[0]" -type "polyFaces" 
		f 4 0 2 -4 -2
		mu 0 4 0 1 3 2;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode transform -n "c_tongue_joint11_guide" -p "FM_Cam_c_hi_tongue";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" 1 0.99999999999999978 0.99999999999999978 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -13.511856555938721 -14.085227012634274 2.3591182231903072 ;
	setAttr ".sp" -type "double3" -13.511856555938721 -14.085227012634277 2.3591182231903076 ;
	setAttr ".spt" -type "double3" 0 3.5527136788005001e-015 -4.4408920985006252e-016 ;
createNode mesh -n "c_tongue_joint11_guideShape" -p "c_tongue_joint11_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 6 ".uvst[0].uvsp[0:5]" -type "float2" 0 0 1 0 0 1 1 1 0.5
		 0 0.52860308 1;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 7 ".pt[0:6]" -type "float3"  0 -2.3384504 -2.3841858e-007 
		0 -2.3015003 2.3841858e-007 0 -2.4410477 4.4408921e-016 0 -2.3918743 4.4408921e-016 
		0 -2.3783169 4.4408921e-016 -9.5367432e-007 -2.474206 4.4408921e-016 0 0 0;
	setAttr -s 6 ".vt[0:5]"  -14.55727291 -11.88511086 2.35911846 -12.4664402 -11.86111927 2.35911798
		 -14.55727291 -11.30513191 2.35911822 -12.4664402 -11.32035065 2.35911822 -13.51185608 -12.079912186 2.35911822
		 -13.51185513 -11.51953793 2.35911822;
	setAttr -s 6 ".ed[0:5]"  0 2 0 1 3 0 2 5 0 5 3 0 0 4 0 4 1 0;
	setAttr -ch 6 ".fc[0]" -type "polyFaces" 
		f 6 4 5 1 -4 -3 -1
		mu 0 6 0 4 1 3 5 2;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode mesh -n "polySurfaceShape11" -p "c_tongue_joint11_guide";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 4 ".uvst[0].uvsp[0:3]" -type "float2" 0 0 1 0 0 1 1 1;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 4 ".pt[0:3]" -type "float3"  -0.54541779 -0.70640182 4.4408921e-016 
		0.54541492 -0.69839478 -7.4505806e-009 -0.54541779 -1.0213614 1.6670674e-007 0.54541588 
		-1.0613956 4.4408921e-016;
	setAttr -s 4 ".vt[0:3]"  -14.011855125 -8.17770386 2.35911822 -13.011855125 -8.17770386 2.35911822
		 -14.011855125 -7.17770386 2.35911822 -13.011855125 -7.17770386 2.35911822;
	setAttr -s 4 ".ed[0:3]"  0 1 0 0 2 0 1 3 0 2 3 0;
	setAttr -ch 4 ".fc[0]" -type "polyFaces" 
		f 4 0 2 -4 -2
		mu 0 4 0 1 3 2;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode transform -n "c_tongue_joint7_guide" -p "FM_Cam_c_hi_tongue";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" 1 0.99999999999999978 0.99999999999999978 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -13.511856079101562 -12.290322303771973 2.3591182231903076 ;
	setAttr ".sp" -type "double3" -13.511856079101562 -12.290322303771976 2.3591182231903081 ;
	setAttr ".spt" -type "double3" 0 3.5527136788005001e-015 -4.4408920985006252e-016 ;
createNode mesh -n "c_tongue_joint7_guideShape" -p "c_tongue_joint7_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 8 ".uvst[0].uvsp[0:7]" -type "float2" 0 0 1 0 0 1 1 1 0.5
		 0 0.52860308 1 0.27854645 1 0.75222301 1;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  -9.5367432e-007 -0.6274395 
		4.4408921e-016 -9.5367432e-007 -0.6274395 4.4408921e-016 -9.5367432e-007 -0.6274395 
		4.4408921e-016 -9.5367432e-007 -0.6274395 4.4408921e-016 -9.5367432e-007 -0.6274395 
		4.4408921e-016 -9.5367432e-007 -0.6274395 4.4408921e-016 -9.5367432e-007 -0.6274395 
		4.4408921e-016 -9.5367432e-007 -0.6274395 4.4408921e-016;
	setAttr -s 8 ".vt[0:7]"  -14.55727196 -11.44847679 2.35911846 -12.46643925 -11.46369553 2.35911798
		 -14.55727196 -10.84152412 2.35911822 -12.46643925 -10.84152412 2.35911822 -13.51185513 -11.6628828 2.35911822
		 -13.51185417 -11.035443306 2.35911822 -14.034563065 -10.90156269 2.35911822 -12.98914528 -10.90156269 2.35911822;
	setAttr -s 8 ".ed[0:7]"  0 2 0 1 3 0 2 6 0 5 7 0 0 4 0 4 1 0 6 5 0
		 7 3 0;
	setAttr -ch 8 ".fc[0]" -type "polyFaces" 
		f 8 4 5 1 -8 -4 -7 -3 -1
		mu 0 8 0 4 1 3 7 5 6 2;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode mesh -n "polySurfaceShape11" -p "c_tongue_joint7_guide";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 4 ".uvst[0].uvsp[0:3]" -type "float2" 0 0 1 0 0 1 1 1;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 4 ".pt[0:3]" -type "float3"  -0.54541779 -0.70640182 4.4408921e-016 
		0.54541492 -0.69839478 -7.4505806e-009 -0.54541779 -1.0213614 1.6670674e-007 0.54541588 
		-1.0613956 4.4408921e-016;
	setAttr -s 4 ".vt[0:3]"  -14.011855125 -8.17770386 2.35911822 -13.011855125 -8.17770386 2.35911822
		 -14.011855125 -7.17770386 2.35911822 -13.011855125 -7.17770386 2.35911822;
	setAttr -s 4 ".ed[0:3]"  0 1 0 0 2 0 1 3 0 2 3 0;
	setAttr -ch 4 ".fc[0]" -type "polyFaces" 
		f 4 0 2 -4 -2
		mu 0 4 0 1 3 2;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode transform -n "c_tongue_joint10_guide" -p "FM_Cam_c_hi_tongue";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" 1 0.99999999999999978 0.99999999999999978 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -13.511856555938721 -13.614830493926998 2.3591183423995967 ;
	setAttr ".sp" -type "double3" -13.511856555938721 -13.614830493927002 2.3591183423995972 ;
	setAttr ".spt" -type "double3" 0 3.5527136788005001e-015 -4.4408920985006252e-016 ;
createNode mesh -n "c_tongue_joint10_guideShape" -p "c_tongue_joint10_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 6 ".uvst[0].uvsp[0:5]" -type "float2" 0 0 1 0 0 1 1 1 0.5
		 0 0.52860308 1;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 7 ".pt[0:6]" -type "float3"  0 -1.8610691 -2.3841858e-007 
		0 -1.851106 2.3841858e-007 0 -1.9307852 2.3841858e-007 0 -1.9155668 4.4408921e-016 
		0 -1.9138321 4.4408921e-016 0 -1.9330658 4.4408921e-016 0 0 0;
	setAttr -s 6 ".vt[0:5]"  -14.55727291 -11.88511086 2.35911846 -12.4664402 -11.86111927 2.35911798
		 -14.55727291 -11.30513191 2.35911822 -12.4664402 -11.32035065 2.35911822 -13.51185608 -12.079912186 2.35911822
		 -13.51185513 -11.51953793 2.35911822;
	setAttr -s 6 ".ed[0:5]"  0 2 0 1 3 0 2 5 0 5 3 0 0 4 0 4 1 0;
	setAttr -ch 6 ".fc[0]" -type "polyFaces" 
		f 6 4 5 1 -4 -3 -1
		mu 0 6 0 4 1 3 5 2;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode mesh -n "polySurfaceShape11" -p "c_tongue_joint10_guide";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 4 ".uvst[0].uvsp[0:3]" -type "float2" 0 0 1 0 0 1 1 1;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 4 ".pt[0:3]" -type "float3"  -0.54541779 -0.70640182 4.4408921e-016 
		0.54541492 -0.69839478 -7.4505806e-009 -0.54541779 -1.0213614 1.6670674e-007 0.54541588 
		-1.0613956 4.4408921e-016;
	setAttr -s 4 ".vt[0:3]"  -14.011855125 -8.17770386 2.35911822 -13.011855125 -8.17770386 2.35911822
		 -14.011855125 -7.17770386 2.35911822 -13.011855125 -7.17770386 2.35911822;
	setAttr -s 4 ".ed[0:3]"  0 1 0 0 2 0 1 3 0 2 3 0;
	setAttr -ch 4 ".fc[0]" -type "polyFaces" 
		f 4 0 2 -4 -2
		mu 0 4 0 1 3 2;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode transform -n "c_tongue_joint8_guide" -p "FM_Cam_c_hi_tongue";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" 1 0.99999999999999978 0.99999999999999978 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -13.511856555938721 -12.46330642700195 2.3591182231903072 ;
	setAttr ".sp" -type "double3" -13.511856555938721 -12.463306427001953 2.3591182231903076 ;
	setAttr ".spt" -type "double3" 0 3.5527136788005001e-015 -4.4408920985006252e-016 ;
createNode mesh -n "c_tongue_joint8_guideShape" -p "c_tongue_joint8_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 6 ".uvst[0].uvsp[0:5]" -type "float2" 0 0 1 0 0 1 1 1 0.5
		 0 0.52860308 1;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 7 ".pt[0:6]" -type "float3"  0 -0.77078438 0 0 -0.77078438 
		0 0 -0.77078438 0 0 -0.77078438 0 0 -0.77078438 0 0 -0.77078438 0 0 0 0;
	setAttr -s 6 ".vt[0:5]"  -14.55727291 -11.88511086 2.35911846 -12.4664402 -11.86111927 2.35911798
		 -14.55727291 -11.30513191 2.35911822 -12.4664402 -11.32035065 2.35911822 -13.51185608 -12.079912186 2.35911822
		 -13.51185513 -11.51953793 2.35911822;
	setAttr -s 6 ".ed[0:5]"  0 2 0 1 3 0 2 5 0 5 3 0 0 4 0 4 1 0;
	setAttr -ch 6 ".fc[0]" -type "polyFaces" 
		f 6 4 5 1 -4 -3 -1
		mu 0 6 0 4 1 3 5 2;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode mesh -n "polySurfaceShape11" -p "c_tongue_joint8_guide";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 4 ".uvst[0].uvsp[0:3]" -type "float2" 0 0 1 0 0 1 1 1;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 4 ".pt[0:3]" -type "float3"  -0.54541779 -0.70640182 4.4408921e-016 
		0.54541492 -0.69839478 -7.4505806e-009 -0.54541779 -1.0213614 1.6670674e-007 0.54541588 
		-1.0613956 4.4408921e-016;
	setAttr -s 4 ".vt[0:3]"  -14.011855125 -8.17770386 2.35911822 -13.011855125 -8.17770386 2.35911822
		 -14.011855125 -7.17770386 2.35911822 -13.011855125 -7.17770386 2.35911822;
	setAttr -s 4 ".ed[0:3]"  0 1 0 0 2 0 1 3 0 2 3 0;
	setAttr -ch 4 ".fc[0]" -type "polyFaces" 
		f 4 0 2 -4 -2
		mu 0 4 0 1 3 2;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode transform -n "FM_Cam_c_hi_side" -p "FM_Cam_c_hi_face";
	setAttr ".rp" -type "double3" 5.2996270656585693 -11.588359117507935 2.3445720672607449 ;
	setAttr ".sp" -type "double3" 5.2996270656585693 -11.588359117507935 2.3445720672607449 ;
createNode transform -n "head_stretch_bottom_Ctrl2_guide" -p "FM_Cam_c_hi_side";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 5.4188346862792969 -16.846231460571289 2.3445720672607457 ;
	setAttr ".sp" -type "double3" 5.4188346862792969 -16.846231460571289 2.3445720672607457 ;
createNode mesh -n "head_stretch_bottom_Ctrl2_guideShape" -p "head_stretch_bottom_Ctrl2_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 16 ".uvst[0].uvsp[0:15]" -type "float2" 0.4740586 0.18274811
		 0.4740586 0.25 0.4481172 0.18274811 0.4481172 0.25 0.48702931 0.25 0.48702931 0.18274811
		 0.48702931 0.18274811 0.48702931 0.25 0.4481172 0.18274811 0.4740586 0.18274811 0.4740586
		 0.25 0.4481172 0.25 0.48702931 0.25 0.48702931 0.18274811 0.4481172 0.21637405 0.4481172
		 0.21637405;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 16 ".vt[0:15]"  6.36792088 -17.010015488 2.34457254 6.38610554 -16.37522125 2.34457254
		 6.73316288 -16.38386154 2.34457159 6.70845222 -16.62072182 2.34457254 5.91774273 -17.25027847 2.34457254
		 5.92730236 -16.3758316 2.34457159 4.46974945 -17.010015488 2.34457254 4.45156479 -16.37522125 2.34457254
		 4.10450745 -16.38386154 2.34457159 4.1292181 -16.62072182 2.34457254 4.9199276 -17.25027847 2.34457254
		 4.91036797 -16.3758316 2.34457159 5.41883659 -17.31724167 2.34457159 5.41883659 -16.3758316 2.34457159
		 6.7761488 -16.5023365 2.34457254 4.061520576 -16.5023365 2.34457254;
	setAttr -s 16 ".ed[0:15]"  3 0 0 0 4 0 11 13 0 1 2 0 3 14 0 5 1 0 9 6 0
		 6 10 0 7 8 0 9 15 0 10 12 0 11 7 0 12 4 0 13 5 0 14 2 0 15 8 0;
	setAttr -ch 16 ".fc[0]" -type "polyFaces" 
		f 16 -6 -14 -3 11 8 -16 -10 6 7 10 12 -2 -1 4 14 -4
		mu 0 16 0 5 13 6 9 8 15 11 10 7 12 4 1 3 14 2;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "head_stretch_Ctrl_guide" -p "FM_Cam_c_hi_side";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 5.2749075889587402 -6.4981436729431143 2.3445720672607435 ;
	setAttr ".sp" -type "double3" 5.2749075889587402 -6.4981436729431143 2.3445720672607435 ;
createNode mesh -n "head_stretch_Ctrl_guideShape" -p "head_stretch_Ctrl_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 16 ".uvst[0].uvsp[0:15]" -type "float2" 0.4740586 0.18274811
		 0.4740586 0.25 0.4481172 0.18274811 0.4481172 0.25 0.48702931 0.25 0.48702931 0.18274811
		 0.48702931 0.18274811 0.48702931 0.25 0.4481172 0.18274811 0.4740586 0.18274811 0.4740586
		 0.25 0.4481172 0.25 0.48702931 0.25 0.48702931 0.18274811 0.4481172 0.21637405 0.4481172
		 0.21637405;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 16 ".vt[0:15]"  6.72512722 -6.27609825 2.34457207 6.75291729 -7.1368103 2.34457207
		 7.28322506 -7.12459373 2.34457207 7.24546719 -6.80433273 2.34457207 6.037247658 -5.95046234 2.34457207
		 6.051856995 -7.13530159 2.34457207 3.82468987 -6.27609825 2.34457207 3.7968998 -7.1368103 2.34457207
		 3.26659107 -7.12459373 2.34457207 3.30434895 -6.80433273 2.34457207 4.51256943 -5.95046234 2.34457207
		 4.49796009 -7.13530159 2.34457207 5.27490997 -5.85947609 2.34457207 5.27490997 -7.13530159 2.34457207
		 7.34891033 -6.96405602 2.34457207 3.20090485 -6.96405602 2.34457207;
	setAttr -s 16 ".ed[0:15]"  3 0 0 0 4 0 11 13 0 1 2 0 3 14 0 5 1 0 9 6 0
		 6 10 0 7 8 0 9 15 0 10 12 0 11 7 0 12 4 0 13 5 0 14 2 0 15 8 0;
	setAttr -ch 16 ".fc[0]" -type "polyFaces" 
		f 16 -12 2 13 5 3 -15 -5 0 1 -13 -11 -8 -7 9 15 -9
		mu 0 16 9 6 13 5 0 2 14 3 1 4 12 7 10 11 15 8;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "head_stretch_top_Ctrl_guide" -p "FM_Cam_c_hi_side";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 5.2996270656585693 -9.6800787448883057 2.3445720672607444 ;
	setAttr ".sp" -type "double3" 5.2996270656585693 -9.6800787448883057 2.3445720672607444 ;
createNode mesh -n "head_stretch_top_Ctrl_guideShape" -p "head_stretch_top_Ctrl_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 30 ".uvst[0].uvsp[0:29]" -type "float2" 0.56212866 0.1379988
		 0.59921068 0.1379988 0.56212866 0.25 0.59921068 0.25 0.375 0.17923957 0.375 0.25
		 0.48106802 0.25 0.375 0.1379988 0.48106799 0.1379988 0.625 0.11978726 0.59921062
		 0.11978726 0.5418635 0.25 0.5418635 0.1379988 0.52159834 0.25 0.52159834 0.1379988
		 0.56212866 0.1379988 0.59921068 0.1379988 0.59921068 0.25 0.56212866 0.25 0.375 0.17923957
		 0.48106802 0.25 0.375 0.25 0.375 0.1379988 0.48106799 0.1379988 0.625 0.25 0.59921062
		 0.11978726 0.5418635 0.25 0.5418635 0.1379988 0.52159834 0.25 0.52159834 0.1379988;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 30 ".vt[0:29]"  8.34272766 -8.97937584 2.34457254 5.35837936 -7.73671341 2.34457207
		 8.82847404 -10.00078964233 2.34457254 7.4238596 -8.25417519 2.34457254 8.29927444 -11.14211655 2.34457254
		 7.55729389 -11.14211655 2.34457254 5.77060699 -11.14211655 2.34457254 5.72846508 -7.73763657 2.34457207
		 5.35837936 -11.6234436 2.34457254 5.66606379 -11.6234436 2.34457254 6.1548214 -7.80007935 2.34457207
		 6.05586195 -10.52715111 2.34457254 6.84223366 -7.97952461 2.34457207 7.29663754 -10.42465591 2.34457254
		 6.55142021 -7.88980103 2.34457207 6.72713232 -10.213974 2.34457254 2.37402916 -8.97937584 2.34457254
		 1.77078009 -10.00078964233 2.34457254 3.2928977 -8.25417519 2.34457254 2.29997993 -11.14211655 2.34457254
		 3.057698011 -11.14211655 2.34457254 4.94614983 -11.14211655 2.34457254 4.98829269 -7.73763657 2.34457207
		 5.050692558 -11.6234436 2.34457254 4.56193495 -7.80007935 2.34457207 4.66089535 -10.52715111 2.34457254
		 3.87452412 -7.97952461 2.34457207 3.31835508 -10.42465591 2.34457254 4.16533709 -7.88980103 2.34457207
		 3.98962474 -10.213974 2.34457254;
	setAttr -s 30 ".ed[0:29]"  0 3 0 2 0 0 3 12 0 4 2 0 4 5 0 5 13 0 7 1 0
		 9 6 0 8 9 0 10 7 0 11 6 0 12 14 0 13 15 0 14 10 0 15 11 0 16 18 0 17 16 0 18 26 0
		 19 17 0 19 20 0 20 27 0 22 1 0 23 21 0 8 23 0 24 22 0 25 21 0 26 28 0 27 29 0 28 24 0
		 29 25 0;
	setAttr -ch 30 ".fc[0]" -type "polyFaces" 
		f 30 -23 -24 8 7 -11 -15 -13 -6 -5 3 1 0 2 11 13 9 6 -22 -25 -29 -27 -18 -16 -17 -19
		 19 20 27 29 25
		mu 0 30 16 25 9 10 1 0 12 14 8 7 4 5 6 13 11 2 3 24 17 18 26 28 20 21 19 22 23 29 27 15;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "head_stretch_bottom_Ctrl_guide" -p "FM_Cam_c_hi_side";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 5.4092611074447632 -13.830033302307129 2.3445720672607453 ;
	setAttr ".sp" -type "double3" 5.4092611074447632 -13.830033302307129 2.3445720672607453 ;
createNode mesh -n "head_stretch_bottom_Ctrl_guideShape" -p "head_stretch_bottom_Ctrl_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 28 ".uvst[0].uvsp[0:27]" -type "float2" 0.375 0 0.375 0.054321218
		 0.48106802 0 0.56936634 0 0.59921068 0 0.625 0 0.51029497 0 0.53952193 0 0.59921068
		 0.10864244 0.56936634 0.10864244 0.53952193 0.10864244 0.51029497 0.10864244 0.48106802
		 0.10864244 0.375 0.10864244 0.375 0 0.48106802 0 0.375 0.054321218 0.56936634 0 0.59921068
		 0 0.51029497 0 0.53952193 0 0.625 0.10864244 0.59921068 0.10864244 0.56936634 0.10864244
		 0.53952193 0.10864244 0.51029497 0.10864244 0.48106802 0.10864244 0.375 0.10864244;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 28 ".vt[0:27]"  8.45974255 -13.51154423 2.34457159 5.35837936 -15.81248951 2.34457159
		 7.4238596 -14.66794205 2.34457254 8.34214306 -11.91799927 2.34457254 7.51775694 -11.91799927 2.34457254
		 5.35837936 -11.84757614 2.34457254 5.72846508 -15.76840782 2.34457254 5.64630508 -11.84757614 2.34457254
		 6.70239449 -12.70475388 2.34457254 6.58502245 -15.34844303 2.34457159 6.156744 -12.54025078 2.34457254
		 6.156744 -15.61124229 2.34457254 7.22744656 -12.46982765 2.34457254 7.0044412613 -15.0081920624 2.34457254
		 8.4009428 -12.71477127 2.34457254 2.35877967 -13.51154423 2.34457159 3.2928977 -14.66794205 2.34457254
		 2.47637987 -11.91799927 2.34457254 3.19900131 -11.91799927 2.34457254 4.98829269 -15.76840782 2.34457254
		 5.07045269 -11.84757614 2.34457254 4.014362812 -12.70475388 2.34457254 4.13173389 -15.34844303 2.34457159
		 4.56001377 -12.54025078 2.34457254 4.56001377 -15.61124229 2.34457254 3.48931074 -12.46982765 2.34457254
		 3.71231604 -15.0081920624 2.34457254 2.41758013 -12.71477127 2.34457254;
	setAttr -s 28 ".ed[0:27]"  0 2 0 0 14 0 2 13 0 3 4 0 4 12 0 6 1 0 7 5 0
		 8 10 0 9 11 0 10 7 0 11 6 0 12 8 0 13 9 0 14 3 0 15 16 0 15 27 0 16 26 0 17 18 0
		 18 25 0 19 1 0 20 5 0 21 23 0 22 24 0 23 20 0 24 19 0 25 21 0 26 22 0 27 17 0;
	setAttr -ch 28 ".fc[0]" -type "polyFaces" 
		f 28 -1 1 13 3 4 11 7 9 6 -21 -24 -22 -26 -19 -18 -28 -16 14 16 26 22 24 19 -6 -11 -9
		 -13 -3
		mu 0 28 2 0 1 13 12 11 10 9 8 21 22 23 24 25 26 27 16 14 15 19 20 17 18 5 4 3 7 6;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_c_hi_hand" -p "FM_Cam_FACIAL_gui_guides_grp";
	setAttr ".rp" -type "double3" 4.5967197418212891 5.4068996906280518 1.1149044036865223 ;
	setAttr ".sp" -type "double3" 4.5967197418212891 5.4068996906280518 1.1149044036865223 ;
createNode transform -n "FM_Cam_c_hi_hand_1_guide" -p "FM_Cam_c_hi_hand";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr ".v" no;
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" 4.0681415023862151 0 0 ;
	setAttr ".rp" -type "double3" 17.550102233886719 6.5370230674743652 0.99995803833007668 ;
	setAttr ".sp" -type "double3" 17.550102233886719 6.5370230674743652 0.99995803833007668 ;
createNode mesh -n "FM_Cam_c_hi_hand_1_guideShape" -p "FM_Cam_c_hi_hand_1_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.27687995135784149 1.0749086439609528 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 4 ".uvst[0].uvsp[0:3]" -type "float2" 0.40217707 0.8175559
		 0.011079311 0.8175559 0.011079311 0.98703283 0.40217707 0.98703283;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 4 ".pt[0:3]" -type "float3"  0 -27.812107 4.7683716e-007 
		0 -27.812107 4.7683716e-007 0 -27.812107 9.5367432e-007 0 -27.812107 9.5367432e-007;
	setAttr -s 4 ".vt[0:3]"  19.26084137 33.61230469 0.99995732 15.8393631 33.61230469 0.99995732
		 19.26084137 35.085956573 0.99995732 15.8393631 35.085956573 0.99995732;
	setAttr -s 4 ".ed[0:3]"  0 1 0 2 3 0 0 2 0 1 3 0;
	setAttr -ch 4 ".fc[0]" -type "polyFaces" 
		f 4 2 1 -4 -1
		mu 0 4 0 3 2 1;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_c_hi_hand_2_guide" -p "FM_Cam_c_hi_hand";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr ".v" no;
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" 4.0681415023862151 0 0 ;
	setAttr ".rp" -type "double3" 17.550102233886719 4.736396312713623 0.99995803833007713 ;
	setAttr ".sp" -type "double3" 17.550102233886719 4.736396312713623 0.99995803833007713 ;
createNode mesh -n "FM_Cam_c_hi_hand_2_guideShape" -p "FM_Cam_c_hi_hand_2_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.0096197724342346191 0.79064017534255981 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 4 ".uvst[0].uvsp[0:3]" -type "float2" 0.40072051 0.62112725
		 0.0096197128 0.62112713 0.0096197128 0.79064023 0.40072045 0.79064023;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 4 ".pt[0:3]" -type "float3"  0 -27.812107 4.7683716e-007 
		0 -27.812107 4.7683716e-007 0 -27.812107 4.7683716e-007 0 -27.812107 4.7683716e-007;
	setAttr -s 4 ".vt[0:3]"  19.26084137 31.81167984 0.99995756 15.8393631 31.81167984 0.99995756
		 19.26084137 33.28532791 0.99995756 15.8393631 33.28532791 0.99995756;
	setAttr -s 4 ".ed[0:3]"  0 1 0 2 3 0 0 2 0 1 3 0;
	setAttr -ch 4 ".fc[0]" -type "polyFaces" 
		f 4 2 1 -4 -1
		mu 0 4 0 3 2 1;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_c_hi_hand_3_guide" -p "FM_Cam_c_hi_hand";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr ".v" no;
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" 4.0681415023862151 0 0 ;
	setAttr ".rp" -type "double3" 17.550092697143555 3.0289111137390137 0.99995803833007746 ;
	setAttr ".sp" -type "double3" 17.550092697143555 3.0289111137390137 0.99995803833007746 ;
createNode mesh -n "FM_Cam_c_hi_hand_3_guideShape" -p "FM_Cam_c_hi_hand_3_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.20700191771067045 0.52140985270148343 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 4 ".uvst[0].uvsp[0:3]" -type "float2" 0.40252852 0.43667597
		 0.011475325 0.43667597 0.011475325 0.60614377 0.40252852 0.60614377;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 4 ".pt[0:3]" -type "float3"  0 -27.812107 7.1525574e-007 
		0 -27.812107 7.1525574e-007 0 -27.812107 4.7683716e-007 0 -27.812107 4.7683716e-007;
	setAttr -s 4 ".vt[0:3]"  19.26083183 30.10419464 0.99995744 15.83935356 30.10419464 0.99995744
		 19.26083183 31.57784271 0.99995744 15.83935356 31.57784271 0.99995744;
	setAttr -s 4 ".ed[0:3]"  0 1 0 2 3 0 0 2 0 1 3 0;
	setAttr -ch 4 ".fc[0]" -type "polyFaces" 
		f 4 2 1 -4 -1
		mu 0 4 0 3 2 1;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_c_hi_hand_4_guide" -p "FM_Cam_c_hi_hand";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr ".v" no;
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" 4.0681415023862151 0 0 ;
	setAttr ".rp" -type "double3" 17.55009651184082 1.2282909750938418 0.9999580383300779 ;
	setAttr ".sp" -type "double3" 17.55009651184082 1.2282909750938418 0.9999580383300779 ;
createNode mesh -n "FM_Cam_c_hi_hand_4_guideShape" -p "FM_Cam_c_hi_hand_4_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.20642390667128729 0.34144139434527432 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 4 ".uvst[0].uvsp[0:3]" -type "float2" 0.40196183 0.25669599
		 0.010886014 0.25669599 0.010886014 0.4261868 0.40196183 0.4261868;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 4 ".pt[0:3]" -type "float3"  0 -27.812107 5.9604645e-007 
		0 -27.812107 5.9604645e-007 0 -27.812107 4.7683716e-007 0 -27.812107 4.7683716e-007;
	setAttr -s 4 ".vt[0:3]"  19.26083565 28.30357361 0.99995744 15.83935738 28.30357361 0.99995744
		 19.26083565 29.77722359 0.99995744 15.83935738 29.77722359 0.99995744;
	setAttr -s 4 ".ed[0:3]"  0 1 0 2 3 0 0 2 0 1 3 0;
	setAttr -ch 4 ".fc[0]" -type "polyFaces" 
		f 4 2 1 -4 -1
		mu 0 4 0 3 2 1;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_c_hi_hand_5_guide" -p "FM_Cam_c_hi_hand";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr ".v" no;
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" 4.0681415023862151 0 0 ;
	setAttr ".rp" -type "double3" 20.15789794921875 1.2282938659191134 0.9999580383300779 ;
	setAttr ".sp" -type "double3" 20.15789794921875 1.2282938659191134 0.9999580383300779 ;
createNode mesh -n "FM_Cam_c_hi_hand_5_guideShape" -p "FM_Cam_c_hi_hand_5_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.46883939206600189 0.43126866490878513 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 4 ".uvst[0].uvsp[0:3]" -type "float2" 0.52729177 0.37036031
		 0.41038701 0.37036031 0.41038701 0.49217701 0.52729177 0.49217701;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 4 ".pt[0:3]" -type "float3"  0 -27.812107 7.1525574e-007 
		0 -27.812107 7.1525574e-007 0 -27.812107 7.1525574e-007 0 -27.812107 7.1525574e-007;
	setAttr -s 4 ".vt[0:3]"  20.68892288 28.36566734 0.99995738 19.62687302 28.36566734 0.99995738
		 20.68892288 29.71513557 0.99995738 19.62687302 29.71513557 0.99995738;
	setAttr -s 4 ".ed[0:3]"  0 1 0 2 3 0 0 2 0 1 3 0;
	setAttr -ch 4 ".fc[0]" -type "polyFaces" 
		f 4 2 1 -4 -1
		mu 0 4 0 3 2 1;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_c_hi_hand_6_guide" -p "FM_Cam_c_hi_hand";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr ".v" no;
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" 4.0681415023862151 0 0 ;
	setAttr ".rp" -type "double3" 20.157891273498535 3.0289111137390137 0.99995803833007746 ;
	setAttr ".sp" -type "double3" 20.157891273498535 3.0289111137390137 0.99995803833007746 ;
createNode mesh -n "FM_Cam_c_hi_hand_6_guideShape" -p "FM_Cam_c_hi_hand_6_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.46883939206600189 0.59407404506380124 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 4 ".uvst[0].uvsp[0:3]" -type "float2" 0.52728534 0.53316987
		 0.41039345 0.53316987 0.41039345 0.65497828 0.52728534 0.65497828;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 4 ".pt[0:3]" -type "float3"  0 -27.812107 7.1525574e-007 
		0 -27.812107 7.1525574e-007 0 -27.812107 4.7683716e-007 0 -27.812107 4.7683716e-007;
	setAttr -s 4 ".vt[0:3]"  20.68891525 30.16628647 0.99995744 19.62686729 30.16628647 0.99995744
		 20.68891525 31.51575089 0.99995744 19.62686729 31.51575089 0.99995744;
	setAttr -s 4 ".ed[0:3]"  0 1 0 2 3 0 0 2 0 1 3 0;
	setAttr -ch 4 ".fc[0]" -type "polyFaces" 
		f 4 2 1 -4 -1
		mu 0 4 0 3 2 1;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_c_hi_hand_7_guide" -p "FM_Cam_c_hi_hand";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr ".v" no;
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" 4.0681415023862151 0 0 ;
	setAttr ".rp" -type "double3" 20.157894134521484 4.7674446105957031 0.99995803833007701 ;
	setAttr ".sp" -type "double3" 20.157894134521484 4.7674446105957031 0.99995803833007701 ;
createNode mesh -n "FM_Cam_c_hi_hand_7_guideShape" -p "FM_Cam_c_hi_hand_7_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.4688393771648407 0.75497266346389813 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 4 ".uvst[0].uvsp[0:3]" -type "float2" 0.52729619 0.69406533
		 0.4103826 0.69406533 0.4103826 0.81587994 0.52729619 0.81587994;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 4 ".pt[0:3]" -type "float3"  0 -27.812107 4.7683716e-007 
		0 -27.812107 4.7683716e-007 0 -27.812107 4.7683716e-007 0 -27.812107 4.7683716e-007;
	setAttr -s 4 ".vt[0:3]"  20.68891907 31.90481758 0.99995732 19.6268692 31.90481758 0.99995732
		 20.68891907 33.25428772 0.99995732 19.6268692 33.25428772 0.99995732;
	setAttr -s 4 ".ed[0:3]"  0 1 0 2 3 0 0 2 0 1 3 0;
	setAttr -ch 4 ".fc[0]" -type "polyFaces" 
		f 4 2 1 -4 -1
		mu 0 4 0 3 2 1;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_c_hi_hand_8_guide" -p "FM_Cam_c_hi_hand";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr ".v" no;
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" 4.0681415023862151 0 0 ;
	setAttr ".rp" -type "double3" 20.157894134521484 6.5059752464294434 0.99995803833007668 ;
	setAttr ".sp" -type "double3" 20.157894134521484 6.5059752464294434 0.99995803833007668 ;
createNode mesh -n "FM_Cam_c_hi_hand_8_guideShape" -p "FM_Cam_c_hi_hand_8_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.4688393771648407 0.64494945340364884 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 4 ".uvst[0].uvsp[0:3]" -type "float2" 0.52729142 0.84147209
		 0.41038731 0.84147209 0.41038731 0.96329647 0.52729142 0.96329647;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 4 ".pt[0:3]" -type "float3"  0 -27.812107 4.7683716e-007 
		0 -27.812107 4.7683716e-007 0 -27.812107 0 0 -27.812107 0;
	setAttr -s 4 ".vt[0:3]"  20.68891907 33.64334869 0.99995756 19.6268692 33.64334869 0.99995756
		 20.68891907 34.99281693 0.99995756 19.6268692 34.99281693 0.99995756;
	setAttr -s 4 ".ed[0:3]"  0 1 0 2 3 0 0 2 0 1 3 0;
	setAttr -ch 4 ".fc[0]" -type "polyFaces" 
		f 4 2 1 -4 -1
		mu 0 4 0 3 2 1;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_c_hi_hand_9_guide" -p "FM_Cam_c_hi_hand";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr ".v" no;
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" 4.0681415023862151 0 0 ;
	setAttr ".rp" -type "double3" 17.517709732055664 9.0924806594848633 1.2298488616943339 ;
	setAttr ".sp" -type "double3" 17.517709732055664 9.0924806594848633 1.2298488616943339 ;
createNode mesh -n "FM_Cam_c_hi_hand_9_guideShape" -p "FM_Cam_c_hi_hand_9_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.3227277398109436 0.1715925931930542 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.38978302 0.19339633
		 0.37979788 0.21308833 0.36418012 0.22865242 0.3444995 0.23868215 0.32273543 0.24219
		 0.30094251 0.23867762 0.28128654 0.22865987 0.26565161 0.21308029 0.25567514 0.19340175
		 0.25224587 0.1715914 0.25567526 0.14978492 0.26564926 0.13010788 0.28129151 0.11452222
		 0.30093837 0.10450989 0.32273474 0.10099518 0.34450495 0.10450584 0.36417413 0.11452895
		 0.37980089 0.13010061 0.38978267 0.14978939 0.39320961 0.17159182;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".vt[0:19]"  18.68736649 9.47252274 1.22985077 18.51267624 9.81536865 1.22984695
		 18.24059677 10.087451935 1.22985077 17.89775467 10.26213455 1.22985077 17.51770973 10.32233429 1.22984695
		 17.13766479 10.26213455 1.22985077 16.79482269 10.087451935 1.22985077 16.52274132 9.81536865 1.22984695
		 16.34805298 9.47252274 1.22985077 16.28786087 9.092483521 1.22984695 16.34805298 8.71243668 1.22985077
		 16.52274132 8.36959076 1.22984695 16.79482269 8.097511292 1.22984695 17.13766479 7.92282867 1.22984695
		 17.51770973 7.86262894 1.22985077 17.89775467 7.92282867 1.22984695 18.24059677 8.097511292 1.22984695
		 18.51267624 8.36959076 1.22984695 18.68736649 8.71243668 1.22985077 18.74755859 9.092483521 1.22984695;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 19 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		mu 0 20 19 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "c_Lf_ear_CTRL_guide" -p "FM_Cam_c_hi_hand";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 10.333439826965332 5.5952966213226318 0.9999580383300769 ;
	setAttr ".sp" -type "double3" 10.333439826965332 5.5952966213226318 0.9999580383300769 ;
createNode mesh -n "c_Lf_ear_CTRL_guideShape" -p "c_Lf_ear_CTRL_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.71047544479370117 0.70226572453975677 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 8 ".uvst[0].uvsp[0:7]" -type "float2" 0.82008278 0.41775134
		 0.84974939 0.42819163 0.84869128 0.96735531 0.81896621 0.98678011 0.57207745 0.52041483
		 0.61088336 0.48693022 0.60990334 0.98636991 0.5712015 0.96681064;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 8 ".vt[0:7]"  11.56163406 3.83209419 0.9999581 9.10524559 3.11645126 0.9999581
		 11.56163406 7.97000885 0.99995804 9.10524559 8.0014953613 0.9999581 11.24908257 8.2219162 0.99995804
		 11.24908257 3.49158096 0.9999581 9.34402561 8.2219162 0.9999581 9.34402561 2.96867752 0.9999581;
	setAttr -s 8 ".ed[0:7]"  0 5 0 2 4 0 0 2 0 1 3 0 4 6 0 5 7 0 6 3 0
		 7 1 0;
	setAttr -ch 8 ".fc[0]" -type "polyFaces" 
		f 8 -1 2 1 4 6 -4 -8 -6
		mu 0 8 5 4 7 6 3 2 1 0;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "c_Rt_ear_CTRL_guide" -p "FM_Cam_c_hi_hand";
	addAttr -ci true -sn "CloseSmooth" -ln "CloseSmooth" -dv 2 -at "long";
	addAttr -ci true -sn "MediumSmooth" -ln "MediumSmooth" -dv 1 -at "long";
	addAttr -ci true -sn "FarSmooth" -ln "FarSmooth" -at "long";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -10.267289638519287 5.5952966213226318 0.9999580383300769 ;
	setAttr ".sp" -type "double3" -10.267289638519287 5.5952966213226318 0.9999580383300769 ;
createNode mesh -n "c_Rt_ear_CTRL_guideShape" -p "c_Rt_ear_CTRL_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.71752327680587769 0.70499110221862793 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 8 ".uvst[0].uvsp[0:7]" -type "float2" 0.83265257 0.42094386
		 0.86246204 0.4317663 0.86246204 0.97155964 0.83265257 0.98903835 0.57258451 0.50255901
		 0.6152178 0.4732174 0.6152178 0.98903835 0.57258451 0.97155964;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 8 ".vt[0:7]"  -11.4954834 3.83209229 0.9999578 -9.039095879 3.11645126 0.9999578
		 -11.4954834 7.97000504 0.99995828 -9.039095879 8.0014953613 0.99995828 -11.1829319 8.2219162 0.99995828
		 -11.1829319 3.49157906 0.9999578 -9.2778759 8.2219162 0.99995828 -9.2778759 2.96867752 0.99995804;
	setAttr -s 8 ".ed[0:7]"  0 5 0 2 4 0 0 2 0 1 3 0 4 6 0 5 7 0 6 3 0
		 7 1 0;
	setAttr -ch 8 ".fc[0]" -type "polyFaces" 
		f 8 7 3 -7 -5 -2 -3 0 5
		mu 0 8 0 1 2 3 6 7 4 5;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
	setAttr ".dr" 1;
createNode transform -n "FM_FACIAL_CAM_GRP" -p "FM_Cam_FACIAL_gui_guides_grp";
	setAttr ".v" no;
createNode transform -n "FM_FACIAL_CAM" -p "FM_FACIAL_CAM_GRP";
	setAttr ".t" -type "double3" -3.5871072381341125 1.3901088640419246 13.591253403945952 ;
	setAttr ".r" -type "double3" -2.8249000307521008e-030 0 0 ;
	setAttr ".s" -type "double3" 1 1.0000000000000002 1.0000000000000002 ;
	setAttr ".rp" -type "double3" 4.4408920985006262e-016 0 -0.160097165219419 ;
	setAttr ".sp" -type "double3" 4.4408920985006262e-016 0 -0.16009716521941897 ;
	setAttr ".spt" -type "double3" 0 0 -2.775557561562892e-017 ;
createNode camera -n "FM_FACIAL_CAMShape" -p "FM_FACIAL_CAM";
	setAttr -k off ".v";
	setAttr ".rnd" no;
	setAttr ".cap" -type "double2" 1.4173 0.9449 ;
	setAttr -l on ".ff";
	setAttr ".ow" 33.880276198608634;
	setAttr ".imn" -type "string" "camera1";
	setAttr ".den" -type "string" "camera1_depth";
	setAttr ".man" -type "string" "camera1_mask";
	setAttr ".o" yes;
	setAttr ".dgc" -type "float3" 0.45967802 0.45967802 0.45967802 ;
createNode transform -n "FM_Cam_BODY_gui_guides_grp" -p "FM_Caml_gui_guides_grp";
	setAttr ".t" -type "double3" 0 -58.319041567875125 0 ;
	setAttr ".rp" -type "double3" 15.749060374460042 0 3.15544362088405e-030 ;
	setAttr ".sp" -type "double3" 15.749060374460042 0 3.15544362088405e-030 ;
createNode transform -n "FM_Cam_BODY_backgroundColor_" -p "FM_Cam_BODY_gui_guides_grp";
createNode mesh -n "FM_Cam_BODY_backgroundColor_Shape" -p "FM_Cam_BODY_backgroundColor_";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 4 ".uvst[0].uvsp[0:3]" -type "float2" 0.036344428 0.56462276
		 0.036344428 0.0072618332 0.54268235 0.0072618332 0.54268235 0.56462276;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 4 ".vt[0:3]"  -27.041564941 -27.289505 3.1554436e-030 -27.041564941 27.28950119 3.1554436e-030
		 22.54107857 27.28950119 3.1554436e-030 22.54107857 -27.289505 3.1554436e-030;
	setAttr -s 4 ".ed[0:3]"  0 3 0 0 1 0 1 2 0 3 2 0;
	setAttr -ch 4 ".fc[0]" -type "polyFaces" 
		f 4 -2 0 3 -3
		mu 0 4 0 1 2 3;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_characters_BODY_picture_" -p "FM_Cam_BODY_gui_guides_grp";
	setAttr ".rp" -type "double3" -21.858963039335563 22.74263552232965 2.1393923759460445 ;
	setAttr ".sp" -type "double3" -21.858963039335563 22.74263552232965 2.1393923759460445 ;
createNode mesh -n "FM_Cam_characters_BODY_picture_Shape" -p "FM_Cam_characters_BODY_picture_";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.24935289472341537 0.77852830290794373 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 4 ".uvst[0].uvsp[0:3]" -type "float2" 0.04565233 0.98222882
		 0.45305347 0.98222882 0.45305347 0.57482779 0.04565233 0.57482779;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 4 ".pt[0:3]" -type "float3"  15.277567 60.843781 -4.4408921e-016 
		15.277567 60.843781 -4.4408921e-016 15.277567 60.843781 -4.4408921e-016 15.277567 
		60.843781 -4.4408921e-016;
	setAttr -s 4 ".vt[0:3]"  -40.94549179 -34.29218292 2.13939238 -33.32756805 -34.29218292 2.13939238
		 -40.94549179 -41.91011047 2.13939238 -33.32756805 -41.91011047 2.13939238;
	setAttr -s 4 ".ed[0:3]"  0 1 0 0 2 0 1 3 0 2 3 0;
	setAttr -ch 4 ".fc[0]" -type "polyFaces" 
		f 4 1 3 -3 -1
		mu 0 4 0 3 2 1;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_l_hi_arm1_" -p "FM_Cam_BODY_gui_guides_grp";
	setAttr ".v" no;
	setAttr ".rp" -type "double3" 18.974245071411133 20.184394836425781 2.1393923759460449 ;
	setAttr ".sp" -type "double3" 18.974245071411133 20.184394836425781 2.1393923759460449 ;
createNode mesh -n "FM_Cam_l_hi_arm1_Shape" -p "FM_Cam_l_hi_arm1_";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.39320961 0.17159182
		 0.38978302 0.19339633 0.37979788 0.21308833 0.36418012 0.22865242 0.3444995 0.23868215
		 0.32273543 0.24219 0.30094251 0.23867762 0.28128654 0.22865987 0.26565161 0.21308029
		 0.25567514 0.19340175 0.25224587 0.1715914 0.25567526 0.14978492 0.26564926 0.13010788
		 0.28129151 0.11452222 0.30093837 0.10450989 0.32273474 0.10099518 0.34450495 0.10450584
		 0.36417413 0.11452895 0.37980089 0.13010061 0.38978267 0.14978939;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  4.9500351 -40.36045837 2.13939238 4.69242287 -39.85487747 2.13939238
		 4.29119873 -39.45363998 2.13939238 3.78561974 -39.19604492 2.13939238 3.22518539 -39.10726929 2.13939238
		 2.66474342 -39.19604492 2.13939238 2.15916443 -39.45363998 2.13939238 1.75793457 -39.85487747 2.13939238
		 1.50032806 -40.36045837 2.13939238 1.41156769 -40.92089081 2.13939238 1.50032806 -41.48133087 2.13939238
		 1.75793457 -41.98691559 2.13939238 2.15916443 -42.38814163 2.13939238 2.66474342 -42.64573669 2.13939238
		 3.22518539 -42.73451233 2.13939238 3.78561974 -42.64573669 2.13939238 4.29119873 -42.38814163 2.13939238
		 4.69242287 -41.98691559 2.13939238 4.9500351 -41.48133087 2.13939238 5.038801193 -40.92089081 2.13939238;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 19 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_c_body_letter_" -p "FM_Cam_BODY_gui_guides_grp";
	setAttr ".rp" -type "double3" -1.7564988136291504 25.267999649047852 1.9510667324066162 ;
	setAttr ".sp" -type "double3" -1.7564988136291504 25.267999649047852 1.9510667324066162 ;
createNode transform -n "FM_Cam_r_body_letter_" -p "FM_Cam_c_body_letter_";
	setAttr ".rp" -type "double3" -7.6894187927246094 23.988329820386511 1.9510667324066162 ;
	setAttr ".sp" -type "double3" -7.6894187927246094 23.988329820386511 1.9510667324066162 ;
createNode mesh -n "FM_Cam_r_body_letter_Shape" -p "FM_Cam_r_body_letter_";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 101 ".uvst[0].uvsp[0:100]" -type "float2" 1 0.038455497 0.54151595
		 0.46987823 0 0.99984294 0.3590056 1 0.80872452 0.73451346 1.666336e-016 0.9613874
		 1.666336e-016 0.038455497 0.1540312 0.77917445 0.031440504 0.96170139 0.15405272
		 0.7983349 0.15405536 0.20055065 0.031642232 0.038119152 1.666336e-016 0 0.4235858
		 0 0.4235858 0.038455497 0.26955459 0.46146595 0.39080861 0.038099431 0.26953366 0.28134853
		 0.40373051 0.46146595 0.32551831 0.45943969 0.73706347 0 1 0 0.26955459 0.92293191
		 0.26955459 0.49992147 0.67871976 0.73470306 0.41893503 0.96154845 0.32166064 0.49932066
		 0.68926436 0.52494109 0.1540312 0.52494109 0.53310204 0.52494109 0.26955459 0.52494109
		 0.5 0.32819051 0.5 0.51576537 0.15384752 0.17541298 0.26964888 0.17541298 0.2 0 0.14547107
		 0.1 0.1 0.04978269 0.1 0 0.30000001 0 0.30000001 0.063421443 0.27812865 0.1 0.40000001
		 0 0.40000001 0.038167618 0.1540312 0.30000001 0.1540312 0.40000001 0.26953429 0.30000001
		 0.30000001 0.45981407 0.30000001 0.49955657 0.2695488 0.40000001 0.4481295 0.40000001
		 0.40000001 0.46132591 0.40000001 0.50188506 0.75738466 0.17541298 0.61035651 0.17541298
		 0.69999999 0.05131061 0.66482997 0.1 0.80000001 0.12881656 0.80000001 0 0.83133042
		 0.1 0.89999998 0.059741359 0.89999998 0 0.69999999 0.25237489 0.66529793 0.30000001
		 0.52036297 0.30000001 0.60000002 0.18975057 0.5924328 0.40000001 0.60000002 0.38961479
		 0.60000002 0.4850809 0.5 0.99569982 0.5 0.95174384 0.1540312 0.69999999 0.26955459
		 0.69999999 0.1540312 0.60000002 0.26955459 0.60000002 0.2 0.99984294 0.15405221 0.80000001
		 0.14536174 0.89999998 0.1 0.99984294 0.1 0.95057118 0.26955459 0.80000001 0.30000001
		 0.99985504 0.30000001 0.93526042 0.26955459 0.89999998 0.40000001 0.99978334 0.40000001
		 0.96082532 0.80643284 0.69999999 0.67644393 0.69999999 0.69999999 0.53190386 0.63792074
		 0.60000002 0.60000002 0.55925995 0.80000001 0.6681686 0.76843858 0.60000002 0.69999999
		 0.93739253 0.67002332 0.80000001 0.60438091 0.89999998 0.60000002 0.98126453 0.60000002
		 0.90360987 0.80030262 0.80000001 0.80000001 0.80111051 0.74274004 0.89999998;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 101 ".pt[0:100]" -type "float3"  -46.659966 59.419518 0 -47.062809 
		59.799095 0 -47.538605 60.265373 0 -47.223167 60.265545 0 -46.827965 60.031929 0 
		-47.538605 60.231541 0 -47.538605 59.419518 0 -47.403263 60.071224 0 -47.510979 60.231819 
		0 -47.403233 60.088081 0 -47.403244 59.562138 0 -47.510799 59.41927 0 -47.538605 
		59.385685 0 -47.166424 59.385685 0 -47.166424 59.419518 0 -47.301762 59.791698 0 
		-47.195225 59.419205 0 -47.301781 59.633224 0 -47.183868 59.791698 0 -47.25259 59.789913 
		0 -46.890991 59.385685 0 -46.659966 59.385685 0 -47.301762 60.197708 0 -47.301762 
		59.825531 0 -46.942257 60.032097 0 -47.170513 60.231712 0 -47.255978 59.825138 0 
		-46.932991 59.847538 0 -47.403255 59.847546 0 -47.070202 59.847546 0 -47.301762 59.847546 
		0 -47.099285 59.674435 0 -47.099285 59.83947 0 -47.403427 59.54002 0 -47.301678 59.54002 
		0 -47.362877 59.385685 0 -47.410789 59.473671 0 -47.450623 59.429226 0 -47.450737 
		59.385685 0 -47.275009 59.385685 0 -47.275009 59.441486 0 -47.294384 59.473625 0 
		-47.187149 59.385685 0 -47.187149 59.419254 0 -47.403324 59.649632 0 -47.403297 59.737617 
		0 -47.301781 59.649632 0 -47.275009 59.790245 0 -47.275009 59.825371 0 -47.301765 
		59.737617 0 -47.144859 59.737617 0 -47.187149 59.791573 0 -47.187149 59.827255 0 
		-46.873226 59.539944 0 -47.002319 59.54002 0 -46.923561 59.430828 0 -46.95446 59.473667 
		0 -46.835648 59.499069 0 -46.835693 59.385685 0 -46.808128 59.473713 0 -46.747818 
		59.438286 0 -46.747833 59.385685 0 -46.923325 59.607903 0 -46.953949 59.649708 0 
		-47.081394 59.649632 0 -47.011421 59.552631 0 -47.01807 59.737617 0 -47.011421 59.728477 
		0 -47.011421 59.812473 0 -47.099274 60.261879 0 -47.099304 60.222973 0 -47.403305 
		60.001564 0 -47.301762 60.001564 0 -47.403278 59.913582 0 -47.301762 59.913582 0 
		-47.362877 60.265381 0 -47.403225 60.089546 0 -47.411171 60.177448 0 -47.450737 60.265369 
		0 -47.450745 60.222012 0 -47.301762 60.089546 0 -47.275009 60.265427 0 -47.275009 
		60.208553 0 -47.301762 60.177528 0 -47.187149 60.265442 0 -47.187149 60.231049 0 
		-46.830029 60.001564 0 -46.944199 60.00156 0 -46.923557 59.853668 0 -46.978104 59.913582 
		0 -47.011398 59.877708 0 -46.835716 59.973564 0 -46.863422 59.913582 0 -46.923599 
		60.210369 0 -46.950134 60.089481 0 -47.007423 60.177708 0 -47.011482 60.248783 0 
		-47.01128 60.180885 0 -46.835503 60.089527 0 -46.83577 60.090504 0 -46.885849 60.177677 
		0;
	setAttr -s 101 ".vt[0:100]"  40.28850174 -36.64947891 1.95106673 39.4828186 -35.89032364 1.95106673
		 38.53123093 -34.95776749 1.95106673 39.16210175 -34.95742798 1.95106673 39.95251083 -35.42465591 1.95106673
		 38.53123093 -35.025432587 1.95106673 38.53123093 -36.64947891 1.95106673 38.8019104 -35.34606552 1.95106673
		 38.58647919 -35.024879456 1.95106673 38.80197144 -35.31235123 1.95106673 38.80194855 -36.36424255 1.95106673
		 38.58683777 -36.64997864 1.95106673 38.53123093 -36.71714401 1.95106673 39.27558899 -36.71714401 1.95106673
		 39.27558899 -36.64947891 1.95106673 39.0049133301 -35.90512085 1.95106673 39.21798706 -36.65010834 1.95106673
		 39.0048751831 -36.22206879 1.95106673 39.24069595 -35.90512085 1.95106673 39.10325623 -35.90868759 1.95106673
		 39.82645035 -36.71714401 1.95106673 40.28850174 -36.71714401 1.95106673 39.0049133301 -35.093101501 1.95106673
		 39.0049133301 -35.83745575 1.95106673 39.72392273 -35.42432022 1.95106673 39.26741028 -35.025093079 1.95106673
		 39.096481323 -35.83823776 1.95106673 39.74245834 -35.79343796 1.95106673 38.80192566 -35.79342651 1.95106673
		 39.46803284 -35.79342651 1.95106673 39.0049133301 -35.79342651 1.95106673 39.40986633 -36.13964462 1.95106673
		 39.40986633 -35.80957413 1.95106673 38.80158615 -36.40847778 1.95106673 39.0050811768 -36.40847778 1.95106673
		 38.88268661 -36.71714401 1.95106673 38.7868576 -36.54117584 1.95106673 38.70719147 -36.6300621 1.95106673
		 38.70696259 -36.71714401 1.95106673 39.058414459 -36.71714401 1.95106673 39.058414459 -36.60554504 1.95106673
		 39.019668579 -36.5412674 1.95106673 39.23413849 -36.71714401 1.95106673 39.23413849 -36.65000534 1.95106673
		 38.80178833 -36.18925095 1.95106673 38.80184174 -36.013282776 1.95106673 39.0048751831 -36.18925095 1.95106673
		 39.058414459 -35.90802765 1.95106673 39.058414459 -35.83777618 1.95106673 39.004901886 -36.013282776 1.95106673
		 39.31871796 -36.013282776 1.95106673 39.23413849 -35.90537262 1.95106673 39.23413849 -35.83400345 1.95106673
		 39.86198425 -36.40862656 1.95106673 39.6037941 -36.40847778 1.95106673 39.76131821 -36.62685776 1.95106673
		 39.6995163 -36.54117966 1.95106673 39.93714523 -36.49037552 1.95106673 39.93704987 -36.71714401 1.95106673
		 39.99217987 -36.5410881 1.95106673 40.11280441 -36.61194229 1.95106673 40.1127739 -36.71714401 1.95106673
		 39.76179123 -36.27271271 1.95106673 39.70053864 -36.18909836 1.95106673 39.44564819 -36.18925095 1.95106673
		 39.58559418 -36.38325119 1.95106673 39.57229614 -36.013282776 1.95106673 39.58559418 -36.03155899 1.95106673
		 39.58559036 -35.86356735 1.95106673 39.40988922 -34.96475601 1.95106673 39.40982437 -35.042572021 1.95106673
		 38.80183029 -35.48538589 1.95106673 39.0049133301 -35.48538589 1.95106673 38.80187988 -35.66135025 1.95106673
		 39.0049133301 -35.66135025 1.95106673 38.88268661 -34.95775604 1.95106673 38.80198669 -35.30942154 1.95106673
		 38.78609467 -35.13362122 1.95106673 38.70696259 -34.95777512 1.95106673 38.70694733 -35.044494629 1.95106673
		 39.0049133301 -35.30942154 1.95106673 39.058414459 -34.95766449 1.95106673 39.058414459 -35.071411133 1.95106673
		 39.0049133301 -35.13345718 1.95106673 39.2341423 -34.95763016 1.95106673 39.23413849 -35.026420593 1.95106673
		 39.94837952 -35.48538589 1.95106673 39.72003555 -35.48539734 1.95106673 39.76132202 -35.78117752 1.95106673
		 39.65222931 -35.66135025 1.95106673 39.58564377 -35.73310089 1.95106673 39.93700027 -35.54138565 1.95106673
		 39.8815918 -35.66135406 1.95106673 39.76123428 -35.067779541 1.95106673 39.70816422 -35.30955505 1.95106673
		 39.5935936 -35.13310242 1.95106673 39.58547211 -34.99095154 1.95106673 39.58587646 -35.12674713 1.95106673
		 39.93743134 -35.3094635 1.95106673 39.93689728 -35.30750656 1.95106673 39.83673477 -35.13315964 1.95106673;
	setAttr -s 101 ".ed[0:100]"  98 99 0 53 62 0 51 18 0 18 50 0 32 52 0 42 13 0
		 13 14 0 14 43 0 33 36 0 36 37 0 38 35 0 37 11 0 11 6 0 6 12 0 12 38 0 41 34 0 35 39 0
		 40 41 0 39 42 0 43 16 0 16 40 0 28 45 0 44 10 0 10 33 0 45 44 0 34 17 0 17 46 0 49 15 0
		 15 47 0 48 23 0 23 30 0 46 49 0 50 31 0 47 19 0 19 51 0 52 26 0 26 48 0 59 57 0 54 56 0
		 56 55 0 57 53 0 55 20 0 20 58 0 0 60 0 61 21 0 21 0 0 60 59 0 58 61 0 68 27 0 62 63 0
		 65 54 0 64 65 0 63 67 0 67 66 0 31 64 0 66 1 0 1 68 0 29 32 0 69 84 0 85 25 0 25 70 0
		 74 72 0 71 73 0 73 28 0 30 74 0 75 78 0 79 77 0 76 9 0 9 7 0 7 71 0 77 76 0 78 2 0
		 2 5 0 5 8 0 8 79 0 72 80 0 81 75 0 83 22 0 22 82 0 80 83 0 84 3 0 3 81 0 82 85 0
		 91 86 0 87 89 0 27 88 0 89 90 0 90 29 0 92 91 0 88 92 0 93 96 0 97 95 0 94 24 0 24 87 0
		 95 94 0 96 69 0 70 97 0 86 4 0 4 98 0 100 93 0 99 100 0;
	setAttr -ch 101 ".fc[0]" -type "polyFaces" 
		f 78 90 95 58 80 81 76 65 71 72 73 74 66 70 67 68 69 62 63 21 24 22 23 8 9 11 12 13
		 14 10 16 18 5 6 7 19 20 17 15 25 26 31 27 28 33 34 2 3 32 54 51 50 38 39 41 42 47
		 44 45 43 46 37 40 1 49 52 53 55 56 48 85 89 88 83 97 98 0 100 99
		mu 0 78 93 96 69 84 3 81 75 78 2 5 8 79 77 76 9 7 71 73 28 45 44 10 33 36 37 11 6 12 38
		 35 39 42 13 14 43 16 40 41 34 17 46 49 15 47 19 51 18 50 31 64 65 54 56 55 20 58
		 61 21 0 60 59 57 53 62 63 67 66 1 68 27 88 92 91 86 4 98 99 100
		h 23 92 93 84 86 87 57 4 35 36 29 30 64 61 75 79 77 78 82 59 60 96 91 94
		mu 0 23 94 24 87 89 90 29 32 52 26 48 23 30 74 72 80 83 22 82 85 25 70 97 95;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_l_body_letter_" -p "FM_Cam_c_body_letter_";
	setAttr ".rp" -type "double3" 4.3107032775878906 23.988160066358191 1.9510667324066162 ;
	setAttr ".sp" -type "double3" 4.3107032775878906 23.988160066358191 1.9510667324066162 ;
createNode mesh -n "FM_Cam_l_body_letter_Shape" -p "FM_Cam_l_body_letter_";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 65 ".uvst[0].uvsp[0:64]" -type "float2" 0.5 0.96153843 0.5
		 1 0 1 0 0.96153843 0 0.03846154 0.18181819 0.77929688 0.037112322 0.96185249 0.18184367
		 0.79841685 0.18199997 0.18732584 0.03735061 0.038129896 0 0 0.90909094 0 1 0.26442358
		 0.95454544 0.26923078 0.31818181 0.26183149 0.53582644 0.03818519 0.31797534 0.1892273
		 0.31817323 0.799263 0.49106994 0.96157098 0.18181819 0.45454547 0.31818181 0.45454547
		 0.44444445 0 0.44444445 0.038968313 0.18198383 0.18181819 0.31798223 0.18181819 0.22222222
		 0 0.16807985 0.090909094 0.11111111 0.047184724 0.11111111 0 0.32395512 0.090909094
		 0.33333334 0 0.33333334 0.068046808 0.18181819 0.27272728 0.18181819 0.36363637 0.31818181
		 0.27272728 0.31818181 0.36363637 0.97160017 0.18181819 0.91021633 0.18181819 0.66666669
		 0 0.66666669 0.040785223 0.55555558 0 0.55555558 0.038219575 0.77777779 0 0.77777779
		 0.060597908 0.94034553 0.090909094 0.83155572 0.090909094 0.8888889 0 0.8888889 0.14959854
		 0.44444445 1 0.44444445 0.96017241 0.18181819 0.72727275 0.31818181 0.72727275 0.18181819
		 0.54545456 0.18181819 0.63636363 0.31818181 0.54545456 0.31818181 0.63636363 0.22222222
		 1 0.18170518 0.81818181 0.16815327 0.90909094 0.11111111 1 0.11111111 0.95306927
		 0.31825608 0.81818181 0.32946685 0.90909094 0.33333334 1 0.33333334 0.91575831;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 65 ".pt[0:64]" -type "float3"  -8.1345062 60.231628 0 -8.1345062 
		60.265461 0 -8.5066833 60.265461 0 -8.5066833 60.231628 0 -8.5066833 59.419605 0 
		-8.3713436 60.071312 0 -8.4790592 60.231903 0 -8.3713188 60.088131 0 -8.3711109 59.55056 
		0 -8.4788818 59.419312 0 -8.5066833 59.385773 0 -7.829999 59.385773 0 -7.7623305 
		59.618382 0 -7.796165 59.622612 0 -8.2698736 59.616104 0 -8.1078396 59.41925 0 -8.2699966 
		59.552231 0 -8.2698669 60.088875 0 -8.1411543 60.231655 0 -8.371336 59.785633 0 -8.2698441 
		59.785633 0 -8.1758604 59.385773 0 -8.1758633 59.419964 0 -8.3711157 59.545715 0 
		-8.2699986 59.545715 0 -8.3412724 59.385773 0 -8.3818321 59.465847 0 -8.423996 59.427326 
		0 -8.4239769 59.385773 0 -8.2655354 59.465744 0 -8.2585659 59.385773 0 -8.2587299 
		59.445541 0 -8.3714714 59.625687 0 -8.3714609 59.705658 0 -8.2698555 59.625687 0 
		-8.2698441 59.705658 0 -7.7834697 59.545715 0 -7.8290701 59.545666 0 -8.0104485 59.385773 
		0 -8.0104351 59.421455 0 -8.093154 59.385773 0 -8.093154 59.41935 0 -7.9277425 59.385773 
		0 -7.9277411 59.439075 0 -7.8067346 59.465744 0 -7.8877172 59.465748 0 -7.8450365 
		59.385773 0 -7.8451295 59.517429 0 -8.1758604 60.265461 0 -8.1758604 60.230431 0 
		-8.3713589 60.025543 0 -8.2698441 60.025543 0 -8.3712711 59.865601 0 -8.3713131 59.945572 
		0 -8.2698441 59.865601 0 -8.2698441 59.945572 0 -8.3412724 60.265461 0 -8.3713455 
		60.105518 0 -8.3818331 60.185371 0 -8.4239769 60.265461 0 -8.423995 60.224129 0 -8.2697945 
		60.105518 0 -8.2613316 60.185444 0 -8.2585659 60.265461 0 -8.2584944 60.191315 0;
	setAttr -s 65 ".vt[0:64]"  12.44521141 -35.025432587 1.95106673 12.44521141 -34.95776749 1.95106673
		 11.70085716 -34.95776749 1.95106673 11.70085716 -35.025432587 1.95106673 11.70085716 -36.64947891 1.95106673
		 11.97153664 -35.34606552 1.95106673 11.75610638 -35.024879456 1.95106673 11.97158623 -35.31242371 1.95106673
		 11.97200298 -36.38756561 1.95106673 11.7564621 -36.65006256 1.95106673 11.70085716 -36.71714401 1.95106673
		 13.054226875 -36.71714401 1.95106673 13.18956375 -36.25192642 1.95106673 13.12189484 -36.24346542 1.95106673
		 12.17447758 -36.25648117 1.95106673 12.4985466 -36.65018845 1.95106673 12.17423153 -36.38422394 1.95106673
		 12.17449188 -35.31093979 1.95106673 12.43191624 -35.025375366 1.95106673 11.9715538 -35.91742325 1.95106673
		 12.17453671 -35.91742325 1.95106673 12.36250401 -36.71714401 1.95106673 12.36249828 -36.64876175 1.95106673
		 11.97199345 -36.39725876 1.95106673 12.17422867 -36.39725494 1.95106673 12.031681061 -36.71714401 1.95106673
		 11.95056057 -36.55699158 1.95106673 11.86623287 -36.63403702 1.95106673 11.86627007 -36.71714401 1.95106673
		 12.18315411 -36.55719757 1.95106673 12.19709301 -36.71714401 1.95106673 12.19676495 -36.59760284 1.95106673
		 11.97128201 -36.23731232 1.95106673 11.97130299 -36.07736969 1.95106673 12.17451286 -36.23731232 1.95106673
		 12.17453671 -36.07736969 1.95106673 13.14728546 -36.39725494 1.95106673 13.056084633 -36.39735413 1.95106673
		 12.69332886 -36.71714401 1.95106673 12.69335556 -36.64577484 1.95106673 12.52791691 -36.71714401 1.95106673
		 12.52791691 -36.64998627 1.95106673 12.85873985 -36.71714401 1.95106673 12.85874271 -36.61053467 1.95106673
		 13.10075569 -36.55720139 1.95106673 12.93879032 -36.55719376 1.95106673 13.024151802 -36.71714401 1.95106673
		 13.023965836 -36.4538269 1.95106673 12.36250401 -34.95776749 1.95106673 12.36250401 -35.027824402 1.95106673
		 11.97150612 -35.43759918 1.95106673 12.17453671 -35.43759918 1.95106673 11.97168159 -35.75748444 1.95106673
		 11.97159767 -35.59754181 1.95106673 12.17453671 -35.75748444 1.95106673 12.17453671 -35.59754181 1.95106673
		 12.031681061 -34.95776749 1.95106673 11.97153473 -35.27764893 1.95106673 11.95055866 -35.11794281 1.95106673
		 11.86627007 -34.95776749 1.95106673 11.86623478 -35.040428162 1.95106673 12.17463684 -35.27765274 1.95106673
		 12.19156265 -35.11780167 1.95106673 12.19709301 -34.95776749 1.95106673 12.19723606 -35.10606003 1.95106673;
	setAttr -s 65 ".ed[0:64]"  0 1 0 1 48 0 49 18 0 18 0 0 36 12 0 12 13 0
		 13 37 0 35 20 0 29 24 0 23 26 0 26 27 0 28 25 0 27 9 0 9 4 0 4 10 0 10 28 0 30 21 0
		 22 31 0 25 30 0 31 29 0 19 33 0 32 8 0 8 23 0 33 32 0 24 16 0 16 14 0 14 34 0 34 35 0
		 44 36 0 37 47 0 40 38 0 39 41 0 21 40 0 41 15 0 15 22 0 38 42 0 43 39 0 46 11 0 11 44 0
		 42 46 0 45 43 0 47 45 0 48 63 0 64 49 0 55 51 0 50 53 0 52 19 0 53 52 0 20 54 0 54 55 0
		 56 59 0 60 58 0 57 7 0 7 5 0 5 50 0 58 57 0 59 2 0 2 3 0 3 6 0 6 60 0 51 17 0 17 61 0
		 61 62 0 63 56 0 62 64 0;
	setAttr -ch 65 ".fc[0]" -type "polyFaces" 
		f 65 64 43 2 3 0 1 42 63 50 56 57 58 59 51 55 52 53 54 45 47 46 20 23 21 22 9 10 12
		 13 14 15 11 18 16 32 30 35 39 37 38 28 4 5 6 29 41 40 36 31 33 34 17 19 8 24 25 26
		 27 7 48 49 44 60 61 62
		mu 0 65 62 64 49 18 0 1 48 63 56 59 2 3 6 60 58 57 7 5 50 53 52 19 33 32 8 23 26 27 9 4
		 10 28 25 30 21 40 38 42 46 11 44 36 12 13 37 47 45 43 39 41 15 22 31 29 24 16 14
		 34 35 20 54 55 51 17 61;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_HANDS_gui_guides_grp" -p "FM_Cam_BODY_gui_guides_grp";
	setAttr ".rp" -type "double3" 41.490046501159668 13.781185150146484 3.1554436208840472e-030 ;
	setAttr ".sp" -type "double3" 41.490046501159668 13.781185150146484 3.1554436208840472e-030 ;
createNode transform -n "FM_Cam_HANDS_backgroundColor_" -p "FM_Cam_HANDS_gui_guides_grp";
	setAttr ".rp" -type "double3" 41.490046501159668 13.781185150146484 3.1554436208840472e-030 ;
	setAttr ".sp" -type "double3" 41.490046501159668 13.781185150146484 3.1554436208840472e-030 ;
createNode mesh -n "FM_Cam_HANDS_backgroundColor_Shape" -p "FM_Cam_HANDS_backgroundColor_";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 4 ".uvst[0].uvsp[0:3]" -type "float2" 0.59756726 0.5698818
		 0.59756726 0.29184556 0.9724412 0.29184556 0.9724412 0.5698818;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 4 ".vt[0:3]"  59.70320511 27.28950119 3.1554436e-030 23.27688789 27.28950119 3.1554436e-030
		 59.70320511 0.27286911 3.1554436e-030 23.27688789 0.27286911 3.1554436e-030;
	setAttr -s 4 ".ed[0:3]"  1 0 0 1 3 0 2 0 0 3 2 0;
	setAttr -ch 4 ".fc[0]" -type "polyFaces" 
		f 4 1 3 2 -1
		mu 0 4 0 1 2 3;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_characters_hands_picture_" -p "FM_Cam_HANDS_gui_guides_grp";
	setAttr ".t" -type "double3" 40.115631323849534 8.5327581385441444 0.80267380134854993 ;
	setAttr ".s" -type "double3" 0.62481225493121351 0.62481225493121351 0.62481225493121351 ;
	setAttr ".rp" -type "double3" -13.657747987065303 14.209877383785503 1.3367185745974945 ;
	setAttr ".sp" -type "double3" -21.858963039335563 22.74263552232965 2.1393923759460445 ;
	setAttr ".spt" -type "double3" 8.2012150522702605 -8.5327581385441462 -0.80267380134854993 ;
createNode mesh -n "FM_Cam_characters_hands_picture_Shape" -p "FM_Cam_characters_hands_picture_";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.24935289472341537 0.77852830290794373 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 4 ".uvst[0].uvsp[0:3]" -type "float2" 0.04565233 0.98222882
		 0.45305347 0.98222882 0.45305347 0.57482779 0.04565233 0.57482779;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 4 ".pt[0:3]" -type "float3"  15.277567 60.843781 -4.4408921e-016 
		15.277567 60.843781 -4.4408921e-016 15.277567 60.843781 -4.4408921e-016 15.277567 
		60.843781 -4.4408921e-016;
	setAttr -s 4 ".vt[0:3]"  -40.94549179 -34.29218292 2.13939238 -33.32756805 -34.29218292 2.13939238
		 -40.94549179 -41.91011047 2.13939238 -33.32756805 -41.91011047 2.13939238;
	setAttr -s 4 ".ed[0:3]"  0 1 0 0 2 0 1 3 0 2 3 0;
	setAttr -ch 4 ".fc[0]" -type "polyFaces" 
		f 4 1 3 -3 -1
		mu 0 4 0 3 2 1;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_l_hi_hand_" -p "FM_Cam_HANDS_gui_guides_grp";
	setAttr ".rp" -type "double3" 35.029745101928711 15.591230392456055 2.1393921375274658 ;
	setAttr ".sp" -type "double3" 35.029745101928711 15.591230392456055 2.1393921375274658 ;
createNode transform -n "Lf_thumb3_guide" -p "FM_Cam_l_hi_hand_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 39.979299545288086 13.060630798339844 2.1393921375274658 ;
	setAttr ".sp" -type "double3" 39.979299545288086 13.060630798339844 2.1393921375274658 ;
createNode mesh -n "Lf_thumb3_guideShape" -p "Lf_thumb3_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193001 0.61471206 0.80727184 0.7219848 0.7221396 0.80711704 0.61486673 0.86177522
		 0.49595416 0.8806091 0.3770414 0.86177522 0.2697686 0.80711704 0.18463637 0.7219848
		 0.12997819 0.61471206 0.11114423 0.49579921 0.12997819 0.37688643 0.18463637 0.26961371
		 0.26976854 0.1844815 0.37704134 0.12982315 0.49595416 0.11098927 0.61486691 0.12982315
		 0.72213972 0.18448138 0.80727196 0.26961353 0.86193019 0.37688643;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  23.69987869 -47.87233353 2.13939214 23.77909088 -47.71687317 2.13939214
		 23.90245819 -47.59350586 2.13939214 24.057914734 -47.51429749 2.13939214 24.23023605 -47.48700714 2.13939214
		 24.40256119 -47.51429749 2.13939214 24.5580101 -47.59350586 2.13939214 24.68138504 -47.71687317 2.13939214
		 24.76059341 -47.87233353 2.13939214 24.78788757 -48.044654846 2.13939214 24.76059341 -48.21697617 2.13939214
		 24.68138504 -48.37242889 2.13939214 24.5580101 -48.49580002 2.13939214 24.40256119 -48.57500839 2.13939214
		 24.23023605 -48.60230255 2.13939214 24.057914734 -48.57500839 2.13939214 23.90245819 -48.49580002 2.13939214
		 23.77909088 -48.37242889 2.13939214 23.69987869 -48.21697617 2.13939214 23.67258835 -48.044654846 2.13939214;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 -19 -18 -17 -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 -20
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "Lf_thumb2_guide" -p "FM_Cam_l_hi_hand_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 39.110956192016602 10.405982971191406 2.1393921375274658 ;
	setAttr ".sp" -type "double3" 39.110956192016602 10.405982971191406 2.1393921375274658 ;
createNode mesh -n "Lf_thumb2_guideShape" -p "Lf_thumb2_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193001 0.61471206 0.80727184 0.7219848 0.7221396 0.80711704 0.61486673 0.86177522
		 0.49595416 0.8806091 0.3770414 0.86177522 0.2697686 0.80711704 0.18463637 0.7219848
		 0.12997819 0.61471206 0.11114423 0.49579921 0.12997819 0.37688643 0.18463637 0.26961371
		 0.26976854 0.1844815 0.37704134 0.12982315 0.49595416 0.11098927 0.61486691 0.12982315
		 0.72213972 0.18448138 0.80727196 0.26961353 0.86193019 0.37688643;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  22.83153534 -50.52698135 2.13939214 22.91074753 -50.371521 2.13939214
		 23.034114838 -50.24815369 2.13939214 23.18957138 -50.16894531 2.13939214 23.3618927 -50.14165497 2.13939214
		 23.53421783 -50.16894531 2.13939214 23.68966675 -50.24815369 2.13939214 23.81304169 -50.371521 2.13939214
		 23.89225006 -50.52698135 2.13939214 23.91954422 -50.69930267 2.13939214 23.89225006 -50.87162399 2.13939214
		 23.81304169 -51.027076721 2.13939214 23.68966675 -51.15044785 2.13939214 23.53421783 -51.22965622 2.13939214
		 23.3618927 -51.25695038 2.13939214 23.18957138 -51.22965622 2.13939214 23.034114838 -51.15044785 2.13939214
		 22.91074753 -51.027076721 2.13939214 22.83153534 -50.87162399 2.13939214 22.804245 -50.69930267 2.13939214;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 -19 -18 -17 -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 -20
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "Lf_thumb1_guide" -p "FM_Cam_l_hi_hand_";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" -1.87531726048406 -1.8742162880367079 0.10928710177038425 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 39.110956192016602 10.405982971191406 2.1393921375274658 ;
	setAttr ".sp" -type "double3" 39.110956192016602 10.405982971191406 2.1393921375274658 ;
createNode mesh -n "Lf_thumb1_guideShape" -p "Lf_thumb1_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193001 0.61471206 0.80727184 0.7219848 0.7221396 0.80711704 0.61486673 0.86177522
		 0.49595416 0.8806091 0.3770414 0.86177522 0.2697686 0.80711704 0.18463637 0.7219848
		 0.12997819 0.61471206 0.11114423 0.49579921 0.12997819 0.37688643 0.18463637 0.26961371
		 0.26976854 0.1844815 0.37704134 0.12982315 0.49595416 0.11098927 0.61486691 0.12982315
		 0.72213972 0.18448138 0.80727196 0.26961353 0.86193019 0.37688643;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  22.83153534 -50.52698135 2.13939214 22.91074753 -50.371521 2.13939214
		 23.034114838 -50.24815369 2.13939214 23.18957138 -50.16894531 2.13939214 23.3618927 -50.14165497 2.13939214
		 23.53421783 -50.16894531 2.13939214 23.68966675 -50.24815369 2.13939214 23.81304169 -50.371521 2.13939214
		 23.89225006 -50.52698135 2.13939214 23.91954422 -50.69930267 2.13939214 23.89225006 -50.87162399 2.13939214
		 23.81304169 -51.027076721 2.13939214 23.68966675 -51.15044785 2.13939214 23.53421783 -51.22965622 2.13939214
		 23.3618927 -51.25695038 2.13939214 23.18957138 -51.22965622 2.13939214 23.034114838 -51.15044785 2.13939214
		 22.91074753 -51.027076721 2.13939214 22.83153534 -50.87162399 2.13939214 22.804245 -50.69930267 2.13939214;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 -19 -18 -17 -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 -20
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "Lf_index3_guide" -p "FM_Cam_l_hi_hand_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 38.788431167602539 20.056991577148437 2.1393921375274658 ;
	setAttr ".sp" -type "double3" 38.788431167602539 20.056991577148437 2.1393921375274658 ;
createNode mesh -n "Lf_index3_guideShape" -p "Lf_index3_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193001 0.61471206 0.80727184 0.7219848 0.7221396 0.80711704 0.61486673 0.86177522
		 0.49595416 0.8806091 0.3770414 0.86177522 0.2697686 0.80711704 0.18463637 0.7219848
		 0.12997819 0.61471206 0.11114423 0.49579921 0.12997819 0.37688643 0.18463637 0.26961371
		 0.26976854 0.1844815 0.37704134 0.12982315 0.49595416 0.11098927 0.61486691 0.12982315
		 0.72213972 0.18448138 0.80727196 0.26961353 0.86193019 0.37688643;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  22.50901031 -40.87597275 2.13939214 22.5882225 -40.72051239 2.13939214
		 22.71158981 -40.59714508 2.13939214 22.86704636 -40.51793671 2.13939214 23.039367676 -40.49064636 2.13939214
		 23.21169281 -40.51793671 2.13939214 23.36714172 -40.59714508 2.13939214 23.49051666 -40.72051239 2.13939214
		 23.56972504 -40.87597275 2.13939214 23.5970192 -41.048294067 2.13939214 23.56972504 -41.22061539 2.13939214
		 23.49051666 -41.37606812 2.13939214 23.36714172 -41.49943924 2.13939214 23.21169281 -41.57864761 2.13939214
		 23.039367676 -41.60594177 2.13939214 22.86704636 -41.57864761 2.13939214 22.71158981 -41.49943924 2.13939214
		 22.5882225 -41.37606812 2.13939214 22.50901031 -41.22061539 2.13939214 22.48171997 -41.048294067 2.13939214;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 -19 -18 -17 -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 -20
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "Lf_index2_guide" -p "FM_Cam_l_hi_hand_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 38.068944931030273 17.675251007080078 2.1393921375274658 ;
	setAttr ".sp" -type "double3" 38.068944931030273 17.675251007080078 2.1393921375274658 ;
createNode mesh -n "Lf_index2_guideShape" -p "Lf_index2_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193001 0.61471206 0.80727184 0.7219848 0.7221396 0.80711704 0.61486673 0.86177522
		 0.49595416 0.8806091 0.3770414 0.86177522 0.2697686 0.80711704 0.18463637 0.7219848
		 0.12997819 0.61471206 0.11114423 0.49579921 0.12997819 0.37688643 0.18463637 0.26961371
		 0.26976854 0.1844815 0.37704134 0.12982315 0.49595416 0.11098927 0.61486691 0.12982315
		 0.72213972 0.18448138 0.80727196 0.26961353 0.86193019 0.37688643;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  21.78952408 -43.25771332 2.13939214 21.86873627 -43.10225296 2.13939214
		 21.99210358 -42.97888565 2.13939214 22.14756012 -42.89967728 2.13939214 22.31988144 -42.87238693 2.13939214
		 22.49220657 -42.89967728 2.13939214 22.64765549 -42.97888565 2.13939214 22.77103043 -43.10225296 2.13939214
		 22.8502388 -43.25771332 2.13939214 22.87753296 -43.43003464 2.13939214 22.8502388 -43.60235596 2.13939214
		 22.77103043 -43.75780869 2.13939214 22.64765549 -43.88117981 2.13939214 22.49220657 -43.96038818 2.13939214
		 22.31988144 -43.98768234 2.13939214 22.14756012 -43.96038818 2.13939214 21.99210358 -43.88117981 2.13939214
		 21.86873627 -43.75780869 2.13939214 21.78952408 -43.60235596 2.13939214 21.76223373 -43.43003464 2.13939214;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 -19 -18 -17 -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 -20
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "Lf_index1_guide" -p "FM_Cam_l_hi_hand_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 37.250223159790039 15.219081878662109 2.1393921375274658 ;
	setAttr ".sp" -type "double3" 37.250223159790039 15.219081878662109 2.1393921375274658 ;
createNode mesh -n "Lf_index1_guideShape" -p "Lf_index1_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193001 0.61471206 0.80727184 0.7219848 0.7221396 0.80711704 0.61486673 0.86177522
		 0.49595416 0.8806091 0.3770414 0.86177522 0.2697686 0.80711704 0.18463637 0.7219848
		 0.12997819 0.61471206 0.11114423 0.49579921 0.12997819 0.37688643 0.18463637 0.26961371
		 0.26976854 0.1844815 0.37704134 0.12982315 0.49595416 0.11098927 0.61486691 0.12982315
		 0.72213972 0.18448138 0.80727196 0.26961353 0.86193019 0.37688643;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  20.97080231 -45.71388245 2.13939214 21.050014496 -45.55842209 2.13939214
		 21.17338181 -45.43505478 2.13939214 21.32883835 -45.35584641 2.13939214 21.50115967 -45.32855606 2.13939214
		 21.6734848 -45.35584641 2.13939214 21.82893372 -45.43505478 2.13939214 21.95230865 -45.55842209 2.13939214
		 22.031517029 -45.71388245 2.13939214 22.058811188 -45.88620377 2.13939214 22.031517029 -46.058525085 2.13939214
		 21.95230865 -46.21397781 2.13939214 21.82893372 -46.33734894 2.13939214 21.6734848 -46.41655731 2.13939214
		 21.50115967 -46.44385147 2.13939214 21.32883835 -46.41655731 2.13939214 21.17338181 -46.33734894 2.13939214
		 21.050014496 -46.21397781 2.13939214 20.97080231 -46.058525085 2.13939214 20.94351196 -45.88620377 2.13939214;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 -19 -18 -17 -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 -20
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "Lf_mid3_guide" -p "FM_Cam_l_hi_hand_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 35.389486312866211 20.776477813720703 2.1393921375274658 ;
	setAttr ".sp" -type "double3" 35.389486312866211 20.776477813720703 2.1393921375274658 ;
createNode mesh -n "Lf_mid3_guideShape" -p "Lf_mid3_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193001 0.61471206 0.80727184 0.7219848 0.7221396 0.80711704 0.61486673 0.86177522
		 0.49595416 0.8806091 0.3770414 0.86177522 0.2697686 0.80711704 0.18463637 0.7219848
		 0.12997819 0.61471206 0.11114423 0.49579921 0.12997819 0.37688643 0.18463637 0.26961371
		 0.26976854 0.1844815 0.37704134 0.12982315 0.49595416 0.11098927 0.61486691 0.12982315
		 0.72213972 0.18448138 0.80727196 0.26961353 0.86193019 0.37688643;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  19.11006546 -40.15648651 2.13939214 19.18927765 -40.0010261536 2.13939214
		 19.31264496 -39.87765884 2.13939214 19.4681015 -39.79845047 2.13939214 19.64042282 -39.77116013 2.13939214
		 19.81274796 -39.79845047 2.13939214 19.96819687 -39.87765884 2.13939214 20.091571808 -40.0010261536 2.13939214
		 20.17078018 -40.15648651 2.13939214 20.19807434 -40.32880783 2.13939214 20.17078018 -40.50112915 2.13939214
		 20.091571808 -40.65658188 2.13939214 19.96819687 -40.779953 2.13939214 19.81274796 -40.85916138 2.13939214
		 19.64042282 -40.88645554 2.13939214 19.4681015 -40.85916138 2.13939214 19.31264496 -40.779953 2.13939214
		 19.18927765 -40.65658188 2.13939214 19.11006546 -40.50112915 2.13939214 19.082775116 -40.32880783 2.13939214;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 -19 -18 -17 -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 -20
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "Lf_mid2_guide" -p "FM_Cam_l_hi_hand_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 35.240629196166992 18.270687103271484 2.1393921375274658 ;
	setAttr ".sp" -type "double3" 35.240629196166992 18.270687103271484 2.1393921375274658 ;
createNode mesh -n "Lf_mid2_guideShape" -p "Lf_mid2_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193001 0.61471206 0.80727184 0.7219848 0.7221396 0.80711704 0.61486673 0.86177522
		 0.49595416 0.8806091 0.3770414 0.86177522 0.2697686 0.80711704 0.18463637 0.7219848
		 0.12997819 0.61471206 0.11114423 0.49579921 0.12997819 0.37688643 0.18463637 0.26961371
		 0.26976854 0.1844815 0.37704134 0.12982315 0.49595416 0.11098927 0.61486691 0.12982315
		 0.72213972 0.18448138 0.80727196 0.26961353 0.86193019 0.37688643;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  18.96120834 -42.66227722 2.13939214 19.040420532 -42.50681686 2.13939214
		 19.16378784 -42.38344955 2.13939214 19.31924438 -42.30424118 2.13939214 19.4915657 -42.27695084 2.13939214
		 19.66389084 -42.30424118 2.13939214 19.81933975 -42.38344955 2.13939214 19.94271469 -42.50681686 2.13939214
		 20.021923065 -42.66227722 2.13939214 20.049217224 -42.83459854 2.13939214 20.021923065 -43.0069198608 2.13939214
		 19.94271469 -43.16237259 2.13939214 19.81933975 -43.28574371 2.13939214 19.66389084 -43.36495209 2.13939214
		 19.4915657 -43.39224625 2.13939214 19.31924438 -43.36495209 2.13939214 19.16378784 -43.28574371 2.13939214
		 19.040420532 -43.16237259 2.13939214 18.96120834 -43.0069198608 2.13939214 18.933918 -42.83459854 2.13939214;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 -19 -18 -17 -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 -20
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "Lf_mid1_guide" -p "FM_Cam_l_hi_hand_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 35.116579055786133 15.591228485107422 2.1393921375274658 ;
	setAttr ".sp" -type "double3" 35.116579055786133 15.591228485107422 2.1393921375274658 ;
createNode mesh -n "Lf_mid1_guideShape" -p "Lf_mid1_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193001 0.61471206 0.80727184 0.7219848 0.7221396 0.80711704 0.61486673 0.86177522
		 0.49595416 0.8806091 0.3770414 0.86177522 0.2697686 0.80711704 0.18463637 0.7219848
		 0.12997819 0.61471206 0.11114423 0.49579921 0.12997819 0.37688643 0.18463637 0.26961371
		 0.26976854 0.1844815 0.37704134 0.12982315 0.49595416 0.11098927 0.61486691 0.12982315
		 0.72213972 0.18448138 0.80727196 0.26961353 0.86193019 0.37688643;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  18.8371582 -45.34173584 2.13939214 18.91637039 -45.18627548 2.13939214
		 19.039737701 -45.062908173 2.13939214 19.19519424 -44.9836998 2.13939214 19.36751556 -44.95640945 2.13939214
		 19.5398407 -44.9836998 2.13939214 19.69528961 -45.062908173 2.13939214 19.81866455 -45.18627548 2.13939214
		 19.89787292 -45.34173584 2.13939214 19.92516708 -45.51405716 2.13939214 19.89787292 -45.68637848 2.13939214
		 19.81866455 -45.84183121 2.13939214 19.69528961 -45.96520233 2.13939214 19.5398407 -46.044410706 2.13939214
		 19.36751556 -46.071704865 2.13939214 19.19519424 -46.044410706 2.13939214 19.039737701 -45.96520233 2.13939214
		 18.91637039 -45.84183121 2.13939214 18.8371582 -45.68637848 2.13939214 18.80986786 -45.51405716 2.13939214;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 -19 -18 -17 -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 -20
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "Lf_ring3_guide" -p "FM_Cam_l_hi_hand_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 32.337884902954102 20.156230926513672 2.1393921375274658 ;
	setAttr ".sp" -type "double3" 32.337884902954102 20.156230926513672 2.1393921375274658 ;
createNode mesh -n "Lf_ring3_guideShape" -p "Lf_ring3_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193001 0.61471206 0.80727184 0.7219848 0.7221396 0.80711704 0.61486673 0.86177522
		 0.49595416 0.8806091 0.3770414 0.86177522 0.2697686 0.80711704 0.18463637 0.7219848
		 0.12997819 0.61471206 0.11114423 0.49579921 0.12997819 0.37688643 0.18463637 0.26961371
		 0.26976854 0.1844815 0.37704134 0.12982315 0.49595416 0.11098927 0.61486691 0.12982315
		 0.72213972 0.18448138 0.80727196 0.26961353 0.86193019 0.37688643;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  16.05846405 -40.7767334 2.13939214 16.13767624 -40.62127304 2.13939214
		 16.26104355 -40.49790573 2.13939214 16.41650009 -40.41869736 2.13939214 16.58882141 -40.39140701 2.13939214
		 16.76114655 -40.41869736 2.13939214 16.91659546 -40.49790573 2.13939214 17.039970398 -40.62127304 2.13939214
		 17.11917877 -40.7767334 2.13939214 17.14647293 -40.94905472 2.13939214 17.11917877 -41.12137604 2.13939214
		 17.039970398 -41.27682877 2.13939214 16.91659546 -41.40019989 2.13939214 16.76114655 -41.47940826 2.13939214
		 16.58882141 -41.50670242 2.13939214 16.41650009 -41.47940826 2.13939214 16.26104355 -41.40019989 2.13939214
		 16.13767624 -41.27682877 2.13939214 16.05846405 -41.12137604 2.13939214 16.031173706 -40.94905472 2.13939214;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 -19 -18 -17 -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 -20
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "Lf_ring2_guide" -p "FM_Cam_l_hi_hand_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 32.660409927368164 17.799301147460938 2.1393921375274658 ;
	setAttr ".sp" -type "double3" 32.660409927368164 17.799301147460938 2.1393921375274658 ;
createNode mesh -n "Lf_ring2_guideShape" -p "Lf_ring2_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193001 0.61471206 0.80727184 0.7219848 0.7221396 0.80711704 0.61486673 0.86177522
		 0.49595416 0.8806091 0.3770414 0.86177522 0.2697686 0.80711704 0.18463637 0.7219848
		 0.12997819 0.61471206 0.11114423 0.49579921 0.12997819 0.37688643 0.18463637 0.26961371
		 0.26976854 0.1844815 0.37704134 0.12982315 0.49595416 0.11098927 0.61486691 0.12982315
		 0.72213972 0.18448138 0.80727196 0.26961353 0.86193019 0.37688643;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  16.38098907 -43.13366318 2.13939214 16.46020126 -42.97820282 2.13939214
		 16.58356857 -42.85483551 2.13939214 16.73902512 -42.77562714 2.13939214 16.91134644 -42.74833679 2.13939214
		 17.08367157 -42.77562714 2.13939214 17.23912048 -42.85483551 2.13939214 17.36249542 -42.97820282 2.13939214
		 17.4417038 -43.13366318 2.13939214 17.46899796 -43.3059845 2.13939214 17.4417038 -43.47830582 2.13939214
		 17.36249542 -43.63375854 2.13939214 17.23912048 -43.75712967 2.13939214 17.08367157 -43.83633804 2.13939214
		 16.91134644 -43.8636322 2.13939214 16.73902512 -43.83633804 2.13939214 16.58356857 -43.75712967 2.13939214
		 16.46020126 -43.63375854 2.13939214 16.38098907 -43.47830582 2.13939214 16.35369873 -43.3059845 2.13939214;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 -19 -18 -17 -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 -20
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "Lf_ring1_guide" -p "FM_Cam_l_hi_hand_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 33.106988906860352 15.591228485107422 2.1393921375274658 ;
	setAttr ".sp" -type "double3" 33.106988906860352 15.591228485107422 2.1393921375274658 ;
createNode mesh -n "Lf_ring1_guideShape" -p "Lf_ring1_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193001 0.61471206 0.80727184 0.7219848 0.7221396 0.80711704 0.61486673 0.86177522
		 0.49595416 0.8806091 0.3770414 0.86177522 0.2697686 0.80711704 0.18463637 0.7219848
		 0.12997819 0.61471206 0.11114423 0.49579921 0.12997819 0.37688643 0.18463637 0.26961371
		 0.26976854 0.1844815 0.37704134 0.12982315 0.49595416 0.11098927 0.61486691 0.12982315
		 0.72213972 0.18448138 0.80727196 0.26961353 0.86193019 0.37688643;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  16.82756805 -45.34173584 2.13939214 16.90678024 -45.18627548 2.13939214
		 17.030147552 -45.062908173 2.13939214 17.1856041 -44.9836998 2.13939214 17.35792542 -44.95640945 2.13939214
		 17.53025055 -44.9836998 2.13939214 17.68569946 -45.062908173 2.13939214 17.8090744 -45.18627548 2.13939214
		 17.88828278 -45.34173584 2.13939214 17.91557693 -45.51405716 2.13939214 17.88828278 -45.68637848 2.13939214
		 17.8090744 -45.84183121 2.13939214 17.68569946 -45.96520233 2.13939214 17.53025055 -46.044410706 2.13939214
		 17.35792542 -46.071704865 2.13939214 17.1856041 -46.044410706 2.13939214 17.030147552 -45.96520233 2.13939214
		 16.90678024 -45.84183121 2.13939214 16.82756805 -45.68637848 2.13939214 16.80027771 -45.51405716 2.13939214;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 -19 -18 -17 -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 -20
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "Lf_pinky3_guide" -p "FM_Cam_l_hi_hand_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 30.080191612243652 18.89093017578125 2.1393921375274658 ;
	setAttr ".sp" -type "double3" 30.080191612243652 18.89093017578125 2.1393921375274658 ;
createNode mesh -n "Lf_pinky3_guideShape" -p "Lf_pinky3_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193001 0.61471206 0.80727184 0.7219848 0.7221396 0.80711704 0.61486673 0.86177522
		 0.49595416 0.8806091 0.3770414 0.86177522 0.2697686 0.80711704 0.18463637 0.7219848
		 0.12997819 0.61471206 0.11114423 0.49579921 0.12997819 0.37688643 0.18463637 0.26961371
		 0.26976854 0.1844815 0.37704134 0.12982315 0.49595416 0.11098927 0.61486691 0.12982315
		 0.72213972 0.18448138 0.80727196 0.26961353 0.86193019 0.37688643;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  13.80077267 -42.042030334 2.13939214 13.87998486 -41.88657379 2.13939214
		 14.0033521652 -41.76320648 2.13939214 14.15880871 -41.68399811 2.13939214 14.33113003 -41.65670776 2.13939214
		 14.50345516 -41.68399811 2.13939214 14.65890408 -41.76320648 2.13939214 14.78227901 -41.88657379 2.13939214
		 14.86148548 -42.042030334 2.13939214 14.88878155 -42.21435547 2.13939214 14.86148548 -42.38667297 2.13939214
		 14.78227901 -42.54212952 2.13939214 14.65890408 -42.66549683 2.13939214 14.50345516 -42.7447052 2.13939214
		 14.33113003 -42.77200317 2.13939214 14.15880871 -42.7447052 2.13939214 14.0033521652 -42.66549683 2.13939214
		 13.87998486 -42.54212952 2.13939214 13.80077267 -42.38667297 2.13939214 13.77348042 -42.21435547 2.13939214;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 -19 -18 -17 -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 -20
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "Lf_pinky2_guide" -p "FM_Cam_l_hi_hand_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 30.452338218688965 17.179054260253906 2.1393921375274658 ;
	setAttr ".sp" -type "double3" 30.452338218688965 17.179054260253906 2.1393921375274658 ;
createNode mesh -n "Lf_pinky2_guideShape" -p "Lf_pinky2_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193001 0.61471206 0.80727184 0.7219848 0.7221396 0.80711704 0.61486673 0.86177522
		 0.49595416 0.8806091 0.3770414 0.86177522 0.2697686 0.80711704 0.18463637 0.7219848
		 0.12997819 0.61471206 0.11114423 0.49579921 0.12997819 0.37688643 0.18463637 0.26961371
		 0.26976854 0.1844815 0.37704134 0.12982315 0.49595416 0.11098927 0.61486691 0.12982315
		 0.72213972 0.18448138 0.80727196 0.26961353 0.86193019 0.37688643;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  14.17291927 -43.75390625 2.13939214 14.25213146 -43.59844971 2.13939214
		 14.37549877 -43.4750824 2.13939214 14.53095531 -43.39587402 2.13939214 14.70327663 -43.36858368 2.13939214
		 14.87560177 -43.39587402 2.13939214 15.031050682 -43.4750824 2.13939214 15.15442562 -43.59844971 2.13939214
		 15.23363209 -43.75390625 2.13939214 15.26092815 -43.92623138 2.13939214 15.23363209 -44.098548889 2.13939214
		 15.15442562 -44.25400543 2.13939214 15.031050682 -44.37737274 2.13939214 14.87560177 -44.45658112 2.13939214
		 14.70327663 -44.48387909 2.13939214 14.53095531 -44.45658112 2.13939214 14.37549877 -44.37737274 2.13939214
		 14.25213146 -44.25400543 2.13939214 14.17291927 -44.098548889 2.13939214 14.14562702 -43.92623138 2.13939214;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 -19 -18 -17 -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 -20
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "Lf_pinky1_guide" -p "FM_Cam_l_hi_hand_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 31.171822547912598 15.070224761962891 2.1393921375274658 ;
	setAttr ".sp" -type "double3" 31.171822547912598 15.070224761962891 2.1393921375274658 ;
createNode mesh -n "Lf_pinky1_guideShape" -p "Lf_pinky1_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193001 0.61471206 0.80727184 0.7219848 0.7221396 0.80711704 0.61486673 0.86177522
		 0.49595416 0.8806091 0.3770414 0.86177522 0.2697686 0.80711704 0.18463637 0.7219848
		 0.12997819 0.61471206 0.11114423 0.49579921 0.12997819 0.37688643 0.18463637 0.26961371
		 0.26976854 0.1844815 0.37704134 0.12982315 0.49595416 0.11098927 0.61486691 0.12982315
		 0.72213972 0.18448138 0.80727196 0.26961353 0.86193019 0.37688643;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  14.8924036 -45.86273956 2.13939214 14.97161579 -45.70727921 2.13939214
		 15.094983101 -45.5839119 2.13939214 15.25043964 -45.50470352 2.13939214 15.42276096 -45.47741318 2.13939214
		 15.5950861 -45.50470352 2.13939214 15.75053501 -45.5839119 2.13939214 15.87390995 -45.70727921 2.13939214
		 15.95311642 -45.86273956 2.13939214 15.98041248 -46.035060883 2.13939214 15.95311642 -46.2073822 2.13939214
		 15.87390995 -46.36283493 2.13939214 15.75053501 -46.48620605 2.13939214 15.5950861 -46.56541443 2.13939214
		 15.42276096 -46.59270859 2.13939214 15.25043964 -46.56541443 2.13939214 15.094983101 -46.48620605 2.13939214
		 14.97161579 -46.36283493 2.13939214 14.8924036 -46.2073822 2.13939214 14.86511135 -46.035060883 2.13939214;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 -19 -18 -17 -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 -20
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_r_hi_hand_" -p "FM_Cam_HANDS_gui_guides_grp";
	setAttr ".rp" -type "double3" 47.961444854736328 15.591230392456055 2.1393921375274658 ;
	setAttr ".sp" -type "double3" 47.961444854736328 15.591230392456055 2.1393921375274658 ;
createNode transform -n "Rt_thumb3_guide" -p "FM_Cam_r_hi_hand_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 43.01188850402832 13.060630798339844 2.1393921375274658 ;
	setAttr ".sp" -type "double3" 43.01188850402832 13.060630798339844 2.1393921375274658 ;
createNode mesh -n "Rt_thumb3_guideShape" -p "Rt_thumb3_guide";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193019 0.37688643 0.80727196 0.26961353 0.72213972 0.18448138 0.61486691 0.12982315
		 0.49595416 0.11098927 0.37704134 0.12982315 0.26976854 0.1844815 0.18463637 0.26961371
		 0.12997819 0.37688643 0.11114423 0.49579921 0.12997819 0.61471206 0.18463637 0.7219848
		 0.2697686 0.80711704 0.3770414 0.86177522 0.49595416 0.8806091 0.61486673 0.86177522
		 0.7221396 0.80711704 0.80727184 0.7219848 0.86193001 0.61471206;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  27.7931881 -47.87233353 2.13939214 27.71397591 -47.71687317 2.13939214
		 27.5906086 -47.59350586 2.13939214 27.43515205 -47.51429749 2.13939214 27.26283073 -47.48700714 2.13939214
		 27.0905056 -47.51429749 2.13939214 26.93505669 -47.59350586 2.13939214 26.81168175 -47.71687317 2.13939214
		 26.73247337 -47.87233353 2.13939214 26.70517921 -48.044654846 2.13939214 26.73247337 -48.21697617 2.13939214
		 26.81168175 -48.37242889 2.13939214 26.93505669 -48.49580002 2.13939214 27.0905056 -48.57500839 2.13939214
		 27.26283073 -48.60230255 2.13939214 27.43515205 -48.57500839 2.13939214 27.5906086 -48.49580002 2.13939214
		 27.71397591 -48.37242889 2.13939214 27.7931881 -48.21697617 2.13939214 27.82047844 -48.044654846 2.13939214;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 19 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "Rt_thumb2_guide" -p "FM_Cam_r_hi_hand_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 43.880231857299805 10.405982971191406 2.1393921375274658 ;
	setAttr ".sp" -type "double3" 43.880231857299805 10.405982971191406 2.1393921375274658 ;
createNode mesh -n "Rt_thumb2_guideShape" -p "Rt_thumb2_guide";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193019 0.37688643 0.80727196 0.26961353 0.72213972 0.18448138 0.61486691 0.12982315
		 0.49595416 0.11098927 0.37704134 0.12982315 0.26976854 0.1844815 0.18463637 0.26961371
		 0.12997819 0.37688643 0.11114423 0.49579921 0.12997819 0.61471206 0.18463637 0.7219848
		 0.2697686 0.80711704 0.3770414 0.86177522 0.49595416 0.8806091 0.61486673 0.86177522
		 0.7221396 0.80711704 0.80727184 0.7219848 0.86193001 0.61471206;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  28.66153145 -50.52698135 2.13939214 28.58231926 -50.371521 2.13939214
		 28.45895195 -50.24815369 2.13939214 28.30349541 -50.16894531 2.13939214 28.13117409 -50.14165497 2.13939214
		 27.95884895 -50.16894531 2.13939214 27.80340004 -50.24815369 2.13939214 27.6800251 -50.371521 2.13939214
		 27.60081673 -50.52698135 2.13939214 27.57352257 -50.69930267 2.13939214 27.60081673 -50.87162399 2.13939214
		 27.6800251 -51.027076721 2.13939214 27.80340004 -51.15044785 2.13939214 27.95884895 -51.22965622 2.13939214
		 28.13117409 -51.25695038 2.13939214 28.30349541 -51.22965622 2.13939214 28.45895195 -51.15044785 2.13939214
		 28.58231926 -51.027076721 2.13939214 28.66153145 -50.87162399 2.13939214 28.68882179 -50.69930267 2.13939214;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 19 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "Rt_thumb1_guide" -p "FM_Cam_r_hi_hand_";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 1.649103159589707 -2.1660877249674897 0.086338995321817436 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 43.880231857299805 10.405982971191406 2.1393921375274658 ;
	setAttr ".sp" -type "double3" 43.880231857299805 10.405982971191406 2.1393921375274658 ;
createNode mesh -n "Rt_thumb1_guideShape" -p "Rt_thumb1_guide";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193019 0.37688643 0.80727196 0.26961353 0.72213972 0.18448138 0.61486691 0.12982315
		 0.49595416 0.11098927 0.37704134 0.12982315 0.26976854 0.1844815 0.18463637 0.26961371
		 0.12997819 0.37688643 0.11114423 0.49579921 0.12997819 0.61471206 0.18463637 0.7219848
		 0.2697686 0.80711704 0.3770414 0.86177522 0.49595416 0.8806091 0.61486673 0.86177522
		 0.7221396 0.80711704 0.80727184 0.7219848 0.86193001 0.61471206;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  28.66153145 -50.52698135 2.13939214 28.58231926 -50.371521 2.13939214
		 28.45895195 -50.24815369 2.13939214 28.30349541 -50.16894531 2.13939214 28.13117409 -50.14165497 2.13939214
		 27.95884895 -50.16894531 2.13939214 27.80340004 -50.24815369 2.13939214 27.6800251 -50.371521 2.13939214
		 27.60081673 -50.52698135 2.13939214 27.57352257 -50.69930267 2.13939214 27.60081673 -50.87162399 2.13939214
		 27.6800251 -51.027076721 2.13939214 27.80340004 -51.15044785 2.13939214 27.95884895 -51.22965622 2.13939214
		 28.13117409 -51.25695038 2.13939214 28.30349541 -51.22965622 2.13939214 28.45895195 -51.15044785 2.13939214
		 28.58231926 -51.027076721 2.13939214 28.66153145 -50.87162399 2.13939214 28.68882179 -50.69930267 2.13939214;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 19 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "Rt_index3_guide" -p "FM_Cam_r_hi_hand_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 44.202756881713867 20.056991577148437 2.1393921375274658 ;
	setAttr ".sp" -type "double3" 44.202756881713867 20.056991577148437 2.1393921375274658 ;
createNode mesh -n "Rt_index3_guideShape" -p "Rt_index3_guide";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193019 0.37688643 0.80727196 0.26961353 0.72213972 0.18448138 0.61486691 0.12982315
		 0.49595416 0.11098927 0.37704134 0.12982315 0.26976854 0.1844815 0.18463637 0.26961371
		 0.12997819 0.37688643 0.11114423 0.49579921 0.12997819 0.61471206 0.18463637 0.7219848
		 0.2697686 0.80711704 0.3770414 0.86177522 0.49595416 0.8806091 0.61486673 0.86177522
		 0.7221396 0.80711704 0.80727184 0.7219848 0.86193001 0.61471206;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  28.98405647 -40.87597275 2.13939214 28.90484428 -40.72051239 2.13939214
		 28.78147697 -40.59714508 2.13939214 28.62602043 -40.51793671 2.13939214 28.45369911 -40.49064636 2.13939214
		 28.28137398 -40.51793671 2.13939214 28.12592506 -40.59714508 2.13939214 28.0025501251 -40.72051239 2.13939214
		 27.92334175 -40.87597275 2.13939214 27.89604759 -41.048294067 2.13939214 27.92334175 -41.22061539 2.13939214
		 28.0025501251 -41.37606812 2.13939214 28.12592506 -41.49943924 2.13939214 28.28137398 -41.57864761 2.13939214
		 28.45369911 -41.60594177 2.13939214 28.62602043 -41.57864761 2.13939214 28.78147697 -41.49943924 2.13939214
		 28.90484428 -41.37606812 2.13939214 28.98405647 -41.22061539 2.13939214 29.011346817 -41.048294067 2.13939214;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 19 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "Rt_index2_guide" -p "FM_Cam_r_hi_hand_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 44.922243118286133 17.675251007080078 2.1393921375274658 ;
	setAttr ".sp" -type "double3" 44.922243118286133 17.675251007080078 2.1393921375274658 ;
createNode mesh -n "Rt_index2_guideShape" -p "Rt_index2_guide";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193019 0.37688643 0.80727196 0.26961353 0.72213972 0.18448138 0.61486691 0.12982315
		 0.49595416 0.11098927 0.37704134 0.12982315 0.26976854 0.1844815 0.18463637 0.26961371
		 0.12997819 0.37688643 0.11114423 0.49579921 0.12997819 0.61471206 0.18463637 0.7219848
		 0.2697686 0.80711704 0.3770414 0.86177522 0.49595416 0.8806091 0.61486673 0.86177522
		 0.7221396 0.80711704 0.80727184 0.7219848 0.86193001 0.61471206;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  29.70354271 -43.25771332 2.13939214 29.62433052 -43.10225296 2.13939214
		 29.50096321 -42.97888565 2.13939214 29.34550667 -42.89967728 2.13939214 29.17318535 -42.87238693 2.13939214
		 29.00086021423 -42.89967728 2.13939214 28.8454113 -42.97888565 2.13939214 28.72203636 -43.10225296 2.13939214
		 28.64282799 -43.25771332 2.13939214 28.61553383 -43.43003464 2.13939214 28.64282799 -43.60235596 2.13939214
		 28.72203636 -43.75780869 2.13939214 28.8454113 -43.88117981 2.13939214 29.00086021423 -43.96038818 2.13939214
		 29.17318535 -43.98768234 2.13939214 29.34550667 -43.96038818 2.13939214 29.50096321 -43.88117981 2.13939214
		 29.62433052 -43.75780869 2.13939214 29.70354271 -43.60235596 2.13939214 29.73083305 -43.43003464 2.13939214;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 19 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "Rt_index1_guide" -p "FM_Cam_r_hi_hand_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 45.740964889526367 15.219081878662109 2.1393921375274658 ;
	setAttr ".sp" -type "double3" 45.740964889526367 15.219081878662109 2.1393921375274658 ;
createNode mesh -n "Rt_index1_guideShape" -p "Rt_index1_guide";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193019 0.37688643 0.80727196 0.26961353 0.72213972 0.18448138 0.61486691 0.12982315
		 0.49595416 0.11098927 0.37704134 0.12982315 0.26976854 0.1844815 0.18463637 0.26961371
		 0.12997819 0.37688643 0.11114423 0.49579921 0.12997819 0.61471206 0.18463637 0.7219848
		 0.2697686 0.80711704 0.3770414 0.86177522 0.49595416 0.8806091 0.61486673 0.86177522
		 0.7221396 0.80711704 0.80727184 0.7219848 0.86193001 0.61471206;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  30.52226448 -45.71388245 2.13939214 30.44305229 -45.55842209 2.13939214
		 30.31968498 -45.43505478 2.13939214 30.16422844 -45.35584641 2.13939214 29.99190712 -45.32855606 2.13939214
		 29.81958199 -45.35584641 2.13939214 29.66413307 -45.43505478 2.13939214 29.54075813 -45.55842209 2.13939214
		 29.46154976 -45.71388245 2.13939214 29.4342556 -45.88620377 2.13939214 29.46154976 -46.058525085 2.13939214
		 29.54075813 -46.21397781 2.13939214 29.66413307 -46.33734894 2.13939214 29.81958199 -46.41655731 2.13939214
		 29.99190712 -46.44385147 2.13939214 30.16422844 -46.41655731 2.13939214 30.31968498 -46.33734894 2.13939214
		 30.44305229 -46.21397781 2.13939214 30.52226448 -46.058525085 2.13939214 30.54955482 -45.88620377 2.13939214;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 19 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "Rt_mid3_guide" -p "FM_Cam_r_hi_hand_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 47.601703643798828 20.776477813720703 2.1393921375274658 ;
	setAttr ".sp" -type "double3" 47.601703643798828 20.776477813720703 2.1393921375274658 ;
createNode mesh -n "Rt_mid3_guideShape" -p "Rt_mid3_guide";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193019 0.37688643 0.80727196 0.26961353 0.72213972 0.18448138 0.61486691 0.12982315
		 0.49595416 0.11098927 0.37704134 0.12982315 0.26976854 0.1844815 0.18463637 0.26961371
		 0.12997819 0.37688643 0.11114423 0.49579921 0.12997819 0.61471206 0.18463637 0.7219848
		 0.2697686 0.80711704 0.3770414 0.86177522 0.49595416 0.8806091 0.61486673 0.86177522
		 0.7221396 0.80711704 0.80727184 0.7219848 0.86193001 0.61471206;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  32.38300323 -40.15648651 2.13939214 32.30378723 -40.0010261536 2.13939214
		 32.18041992 -39.87765884 2.13939214 32.024963379 -39.79845047 2.13939214 31.85264397 -39.77116013 2.13939214
		 31.68031883 -39.79845047 2.13939214 31.52486992 -39.87765884 2.13939214 31.40149498 -40.0010261536 2.13939214
		 31.32228661 -40.15648651 2.13939214 31.29499245 -40.32880783 2.13939214 31.32228661 -40.50112915 2.13939214
		 31.40149498 -40.65658188 2.13939214 31.52486992 -40.779953 2.13939214 31.68031883 -40.85916138 2.13939214
		 31.85264397 -40.88645554 2.13939214 32.024963379 -40.85916138 2.13939214 32.18041992 -40.779953 2.13939214
		 32.30378723 -40.65658188 2.13939214 32.38300323 -40.50112915 2.13939214 32.41029358 -40.32880783 2.13939214;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 19 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "Rt_mid2_guide" -p "FM_Cam_r_hi_hand_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 47.750556945800781 18.270687103271484 2.1393921375274658 ;
	setAttr ".sp" -type "double3" 47.750556945800781 18.270687103271484 2.1393921375274658 ;
createNode mesh -n "Rt_mid2_guideShape" -p "Rt_mid2_guide";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193019 0.37688643 0.80727196 0.26961353 0.72213972 0.18448138 0.61486691 0.12982315
		 0.49595416 0.11098927 0.37704134 0.12982315 0.26976854 0.1844815 0.18463637 0.26961371
		 0.12997819 0.37688643 0.11114423 0.49579921 0.12997819 0.61471206 0.18463637 0.7219848
		 0.2697686 0.80711704 0.3770414 0.86177522 0.49595416 0.8806091 0.61486673 0.86177522
		 0.7221396 0.80711704 0.80727184 0.7219848 0.86193001 0.61471206;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  32.53186035 -42.66227722 2.13939214 32.45264435 -42.50681686 2.13939214
		 32.32927704 -42.38344955 2.13939214 32.1738205 -42.30424118 2.13939214 32.0015029907 -42.27695084 2.13939214
		 31.82917595 -42.30424118 2.13939214 31.67372704 -42.38344955 2.13939214 31.5503521 -42.50681686 2.13939214
		 31.47114372 -42.66227722 2.13939214 31.44384956 -42.83459854 2.13939214 31.47114372 -43.0069198608 2.13939214
		 31.5503521 -43.16237259 2.13939214 31.67372704 -43.28574371 2.13939214 31.82917595 -43.36495209 2.13939214
		 32.0015029907 -43.39224625 2.13939214 32.1738205 -43.36495209 2.13939214 32.32927704 -43.28574371 2.13939214
		 32.45264435 -43.16237259 2.13939214 32.53186035 -43.0069198608 2.13939214 32.55914307 -42.83459854 2.13939214;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 19 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "Rt_mid1_guide" -p "FM_Cam_r_hi_hand_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 47.874608993530273 15.591228485107422 2.1393921375274658 ;
	setAttr ".sp" -type "double3" 47.874608993530273 15.591228485107422 2.1393921375274658 ;
createNode mesh -n "Rt_mid1_guideShape" -p "Rt_mid1_guide";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193019 0.37688643 0.80727196 0.26961353 0.72213972 0.18448138 0.61486691 0.12982315
		 0.49595416 0.11098927 0.37704134 0.12982315 0.26976854 0.1844815 0.18463637 0.26961371
		 0.12997819 0.37688643 0.11114423 0.49579921 0.12997819 0.61471206 0.18463637 0.7219848
		 0.2697686 0.80711704 0.3770414 0.86177522 0.49595416 0.8806091 0.61486673 0.86177522
		 0.7221396 0.80711704 0.80727184 0.7219848 0.86193001 0.61471206;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  32.65590668 -45.34173584 2.13939214 32.57669067 -45.18627548 2.13939214
		 32.45333099 -45.062908173 2.13939214 32.29787445 -44.9836998 2.13939214 32.12554932 -44.95640945 2.13939214
		 31.95322609 -44.9836998 2.13939214 31.79777718 -45.062908173 2.13939214 31.67440224 -45.18627548 2.13939214
		 31.59519386 -45.34173584 2.13939214 31.5678997 -45.51405716 2.13939214 31.59519386 -45.68637848 2.13939214
		 31.67440224 -45.84183121 2.13939214 31.79777718 -45.96520233 2.13939214 31.95322609 -46.044410706 2.13939214
		 32.12554932 -46.071704865 2.13939214 32.29787445 -46.044410706 2.13939214 32.45333099 -45.96520233 2.13939214
		 32.57669067 -45.84183121 2.13939214 32.65590668 -45.68637848 2.13939214 32.68319702 -45.51405716 2.13939214;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 19 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "Rt_ring3_guide" -p "FM_Cam_r_hi_hand_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 50.653305053710937 20.156230926513672 2.1393921375274658 ;
	setAttr ".sp" -type "double3" 50.653305053710937 20.156230926513672 2.1393921375274658 ;
createNode mesh -n "Rt_ring3_guideShape" -p "Rt_ring3_guide";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193019 0.37688643 0.80727196 0.26961353 0.72213972 0.18448138 0.61486691 0.12982315
		 0.49595416 0.11098927 0.37704134 0.12982315 0.26976854 0.1844815 0.18463637 0.26961371
		 0.12997819 0.37688643 0.11114423 0.49579921 0.12997819 0.61471206 0.18463637 0.7219848
		 0.2697686 0.80711704 0.3770414 0.86177522 0.49595416 0.8806091 0.61486673 0.86177522
		 0.7221396 0.80711704 0.80727184 0.7219848 0.86193001 0.61471206;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  35.43460083 -40.7767334 2.13939214 35.35539246 -40.62127304 2.13939214
		 35.23202515 -40.49790573 2.13939214 35.076568604 -40.41869736 2.13939214 34.90424347 -40.39140701 2.13939214
		 34.73191833 -40.41869736 2.13939214 34.57646942 -40.49790573 2.13939214 34.45309448 -40.62127304 2.13939214
		 34.37388611 -40.7767334 2.13939214 34.34658813 -40.94905472 2.13939214 34.37388611 -41.12137604 2.13939214
		 34.45309448 -41.27682877 2.13939214 34.57646942 -41.40019989 2.13939214 34.73191833 -41.47940826 2.13939214
		 34.90424347 -41.50670242 2.13939214 35.076568604 -41.47940826 2.13939214 35.23202515 -41.40019989 2.13939214
		 35.35539246 -41.27682877 2.13939214 35.43460083 -41.12137604 2.13939214 35.4618988 -40.94905472 2.13939214;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 19 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "Rt_ring2_guide" -p "FM_Cam_r_hi_hand_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 50.330776214599609 17.799301147460938 2.1393921375274658 ;
	setAttr ".sp" -type "double3" 50.330776214599609 17.799301147460938 2.1393921375274658 ;
createNode mesh -n "Rt_ring2_guideShape" -p "Rt_ring2_guide";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193019 0.37688643 0.80727196 0.26961353 0.72213972 0.18448138 0.61486691 0.12982315
		 0.49595416 0.11098927 0.37704134 0.12982315 0.26976854 0.1844815 0.18463637 0.26961371
		 0.12997819 0.37688643 0.11114423 0.49579921 0.12997819 0.61471206 0.18463637 0.7219848
		 0.2697686 0.80711704 0.3770414 0.86177522 0.49595416 0.8806091 0.61486673 0.86177522
		 0.7221396 0.80711704 0.80727184 0.7219848 0.86193001 0.61471206;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  35.11207581 -43.13366318 2.13939214 35.032867432 -42.97820282 2.13939214
		 34.90950012 -42.85483551 2.13939214 34.75404358 -42.77562714 2.13939214 34.58171844 -42.74833679 2.13939214
		 34.40939331 -42.77562714 2.13939214 34.2539444 -42.85483551 2.13939214 34.13056946 -42.97820282 2.13939214
		 34.051361084 -43.13366318 2.13939214 34.02406311 -43.3059845 2.13939214 34.051361084 -43.47830582 2.13939214
		 34.13056946 -43.63375854 2.13939214 34.2539444 -43.75712967 2.13939214 34.40939331 -43.83633804 2.13939214
		 34.58171844 -43.8636322 2.13939214 34.75404358 -43.83633804 2.13939214 34.90950012 -43.75712967 2.13939214
		 35.032867432 -43.63375854 2.13939214 35.11207581 -43.47830582 2.13939214 35.13936615 -43.3059845 2.13939214;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 19 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "Rt_ring1_guide" -p "FM_Cam_r_hi_hand_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 49.884197235107422 15.591228485107422 2.1393921375274658 ;
	setAttr ".sp" -type "double3" 49.884197235107422 15.591228485107422 2.1393921375274658 ;
createNode mesh -n "Rt_ring1_guideShape" -p "Rt_ring1_guide";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193019 0.37688643 0.80727196 0.26961353 0.72213972 0.18448138 0.61486691 0.12982315
		 0.49595416 0.11098927 0.37704134 0.12982315 0.26976854 0.1844815 0.18463637 0.26961371
		 0.12997819 0.37688643 0.11114423 0.49579921 0.12997819 0.61471206 0.18463637 0.7219848
		 0.2697686 0.80711704 0.3770414 0.86177522 0.49595416 0.8806091 0.61486673 0.86177522
		 0.7221396 0.80711704 0.80727184 0.7219848 0.86193001 0.61471206;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  34.66549683 -45.34173584 2.13939214 34.58628845 -45.18627548 2.13939214
		 34.46292114 -45.062908173 2.13939214 34.3074646 -44.9836998 2.13939214 34.13513947 -44.95640945 2.13939214
		 33.96281433 -44.9836998 2.13939214 33.80736542 -45.062908173 2.13939214 33.68399048 -45.18627548 2.13939214
		 33.6047821 -45.34173584 2.13939214 33.57748413 -45.51405716 2.13939214 33.6047821 -45.68637848 2.13939214
		 33.68399048 -45.84183121 2.13939214 33.80736542 -45.96520233 2.13939214 33.96281433 -46.044410706 2.13939214
		 34.13513947 -46.071704865 2.13939214 34.3074646 -46.044410706 2.13939214 34.46292114 -45.96520233 2.13939214
		 34.58628845 -45.84183121 2.13939214 34.66549683 -45.68637848 2.13939214 34.69278717 -45.51405716 2.13939214;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 19 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "Rt_pinky3_guide" -p "FM_Cam_r_hi_hand_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 52.910999298095703 18.89093017578125 2.1393921375274658 ;
	setAttr ".sp" -type "double3" 52.910999298095703 18.89093017578125 2.1393921375274658 ;
createNode mesh -n "Rt_pinky3_guideShape" -p "Rt_pinky3_guide";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193019 0.37688643 0.80727196 0.26961353 0.72213972 0.18448138 0.61486691 0.12982315
		 0.49595416 0.11098927 0.37704134 0.12982315 0.26976854 0.1844815 0.18463637 0.26961371
		 0.12997819 0.37688643 0.11114423 0.49579921 0.12997819 0.61471206 0.18463637 0.7219848
		 0.2697686 0.80711704 0.3770414 0.86177522 0.49595416 0.8806091 0.61486673 0.86177522
		 0.7221396 0.80711704 0.80727184 0.7219848 0.86193001 0.61471206;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  37.69229126 -42.042030334 2.13939214 37.61308289 -41.88657379 2.13939214
		 37.48971558 -41.76320648 2.13939214 37.33425903 -41.68399811 2.13939214 37.16194153 -41.65670776 2.13939214
		 36.98960876 -41.68399811 2.13939214 36.83416748 -41.76320648 2.13939214 36.71078491 -41.88657379 2.13939214
		 36.63158417 -42.042030334 2.13939214 36.60428619 -42.21435547 2.13939214 36.63158417 -42.38667297 2.13939214
		 36.71078491 -42.54212952 2.13939214 36.83416748 -42.66549683 2.13939214 36.98960876 -42.7447052 2.13939214
		 37.16194153 -42.77200317 2.13939214 37.33425903 -42.7447052 2.13939214 37.48971558 -42.66549683 2.13939214
		 37.61308289 -42.54212952 2.13939214 37.69229126 -42.38667297 2.13939214 37.71958923 -42.21435547 2.13939214;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 19 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "Rt_pinky2_guide" -p "FM_Cam_r_hi_hand_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 52.538852691650391 17.179054260253906 2.1393921375274658 ;
	setAttr ".sp" -type "double3" 52.538852691650391 17.179054260253906 2.1393921375274658 ;
createNode mesh -n "Rt_pinky2_guideShape" -p "Rt_pinky2_guide";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193019 0.37688643 0.80727196 0.26961353 0.72213972 0.18448138 0.61486691 0.12982315
		 0.49595416 0.11098927 0.37704134 0.12982315 0.26976854 0.1844815 0.18463637 0.26961371
		 0.12997819 0.37688643 0.11114423 0.49579921 0.12997819 0.61471206 0.18463637 0.7219848
		 0.2697686 0.80711704 0.3770414 0.86177522 0.49595416 0.8806091 0.61486673 0.86177522
		 0.7221396 0.80711704 0.80727184 0.7219848 0.86193001 0.61471206;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  37.32014465 -43.75390625 2.13939214 37.24093628 -43.59844971 2.13939214
		 37.11756897 -43.4750824 2.13939214 36.96211243 -43.39587402 2.13939214 36.78979492 -43.36858368 2.13939214
		 36.61746216 -43.39587402 2.13939214 36.46202087 -43.4750824 2.13939214 36.33863831 -43.59844971 2.13939214
		 36.25943756 -43.75390625 2.13939214 36.23213959 -43.92623138 2.13939214 36.25943756 -44.098548889 2.13939214
		 36.33863831 -44.25400543 2.13939214 36.46202087 -44.37737274 2.13939214 36.61746216 -44.45658112 2.13939214
		 36.78979492 -44.48387909 2.13939214 36.96211243 -44.45658112 2.13939214 37.11756897 -44.37737274 2.13939214
		 37.24093628 -44.25400543 2.13939214 37.32014465 -44.098548889 2.13939214 37.34744263 -43.92623138 2.13939214;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 19 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "Rt_pinky1_guide" -p "FM_Cam_r_hi_hand_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 51.819366455078125 15.070224761962891 2.1393921375274658 ;
	setAttr ".sp" -type "double3" 51.819366455078125 15.070224761962891 2.1393921375274658 ;
createNode mesh -n "Rt_pinky1_guideShape" -p "Rt_pinky1_guide";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193019 0.37688643 0.80727196 0.26961353 0.72213972 0.18448138 0.61486691 0.12982315
		 0.49595416 0.11098927 0.37704134 0.12982315 0.26976854 0.1844815 0.18463637 0.26961371
		 0.12997819 0.37688643 0.11114423 0.49579921 0.12997819 0.61471206 0.18463637 0.7219848
		 0.2697686 0.80711704 0.3770414 0.86177522 0.49595416 0.8806091 0.61486673 0.86177522
		 0.7221396 0.80711704 0.80727184 0.7219848 0.86193001 0.61471206;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  36.60066223 -45.86273956 2.13939214 36.52145386 -45.70727921 2.13939214
		 36.39808655 -45.5839119 2.13939214 36.24263 -45.50470352 2.13939214 36.070304871 -45.47741318 2.13939214
		 35.89797974 -45.50470352 2.13939214 35.74253082 -45.5839119 2.13939214 35.61915588 -45.70727921 2.13939214
		 35.53994751 -45.86273956 2.13939214 35.51264954 -46.035060883 2.13939214 35.53994751 -46.2073822 2.13939214
		 35.61915588 -46.36283493 2.13939214 35.74253082 -46.48620605 2.13939214 35.89797974 -46.56541443 2.13939214
		 36.070304871 -46.59270859 2.13939214 36.24263 -46.56541443 2.13939214 36.39808655 -46.48620605 2.13939214
		 36.52145386 -46.36283493 2.13939214 36.60066223 -46.2073822 2.13939214 36.62796021 -46.035060883 2.13939214;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 19 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_c_hands_letter_" -p "FM_Cam_HANDS_gui_guides_grp";
	setAttr ".rp" -type "double3" 41.266054491436449 25.267999649047852 1.9510667324066162 ;
	setAttr ".sp" -type "double3" 41.266054491436449 25.267999649047852 1.9510667324066162 ;
createNode transform -n "FM_Cam_r_hands_letter_" -p "FM_Cam_c_hands_letter_";
	setAttr ".rp" -type "double3" 50.924000466613187 24.309625948058439 1.9510667324066158 ;
	setAttr ".sp" -type "double3" 50.924000466613187 24.309625948058439 1.9510667324066158 ;
createNode mesh -n "FM_Cam_r_hands_letter_Shape" -p "FM_Cam_r_hands_letter_";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 101 ".uvst[0].uvsp[0:100]" -type "float2" 1 0.038455497 0.54151595
		 0.46987823 0 0.99984294 0.3590056 1 0.80872452 0.73451346 1.666336e-016 0.9613874
		 1.666336e-016 0.038455497 0.1540312 0.77917445 0.031440504 0.96170139 0.15405272
		 0.7983349 0.15405536 0.20055065 0.031642232 0.038119152 1.666336e-016 0 0.4235858
		 0 0.4235858 0.038455497 0.26955459 0.46146595 0.39080861 0.038099431 0.26953366 0.28134853
		 0.40373051 0.46146595 0.32551831 0.45943969 0.73706347 0 1 0 0.26955459 0.92293191
		 0.26955459 0.49992147 0.67871976 0.73470306 0.41893503 0.96154845 0.32166064 0.49932066
		 0.68926436 0.52494109 0.1540312 0.52494109 0.53310204 0.52494109 0.26955459 0.52494109
		 0.5 0.32819051 0.5 0.51576537 0.15384752 0.17541298 0.26964888 0.17541298 0.2 0 0.14547107
		 0.1 0.1 0.04978269 0.1 0 0.30000001 0 0.30000001 0.063421443 0.27812865 0.1 0.40000001
		 0 0.40000001 0.038167618 0.1540312 0.30000001 0.1540312 0.40000001 0.26953429 0.30000001
		 0.30000001 0.45981407 0.30000001 0.49955657 0.2695488 0.40000001 0.4481295 0.40000001
		 0.40000001 0.46132591 0.40000001 0.50188506 0.75738466 0.17541298 0.61035651 0.17541298
		 0.69999999 0.05131061 0.66482997 0.1 0.80000001 0.12881656 0.80000001 0 0.83133042
		 0.1 0.89999998 0.059741359 0.89999998 0 0.69999999 0.25237489 0.66529793 0.30000001
		 0.52036297 0.30000001 0.60000002 0.18975057 0.5924328 0.40000001 0.60000002 0.38961479
		 0.60000002 0.4850809 0.5 0.99569982 0.5 0.95174384 0.1540312 0.69999999 0.26955459
		 0.69999999 0.1540312 0.60000002 0.26955459 0.60000002 0.2 0.99984294 0.15405221 0.80000001
		 0.14536174 0.89999998 0.1 0.99984294 0.1 0.95057118 0.26955459 0.80000001 0.30000001
		 0.99985504 0.30000001 0.93526042 0.26955459 0.89999998 0.40000001 0.99978334 0.40000001
		 0.96082532 0.80643284 0.69999999 0.67644393 0.69999999 0.69999999 0.53190386 0.63792074
		 0.60000002 0.60000002 0.55925995 0.80000001 0.6681686 0.76843858 0.60000002 0.69999999
		 0.93739253 0.67002332 0.80000001 0.60438091 0.89999998 0.60000002 0.98126453 0.60000002
		 0.90360987 0.80030262 0.80000001 0.80000001 0.80111051 0.74274004 0.89999998;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 101 ".pt[0:100]" -type "float3"  11.953451 59.740814 -6.6613381e-016 
		11.55061 60.120392 -6.6613381e-016 11.074816 60.58667 -6.6613381e-016 11.390251 60.586842 
		-6.6613381e-016 11.785456 60.353226 -6.6613381e-016 11.074816 60.552837 -6.6613381e-016 
		11.074816 59.740814 -6.6613381e-016 11.210155 60.392521 -6.6613381e-016 11.10244 
		60.553116 -6.6613381e-016 11.210186 60.409378 -6.6613381e-016 11.210175 59.883434 
		-6.6613381e-016 11.102619 59.740566 -6.6613381e-016 11.074816 59.706982 -6.6613381e-016 
		11.446995 59.706982 -6.6613381e-016 11.446995 59.740814 -6.6613381e-016 11.311657 
		60.112995 -6.6613381e-016 11.418194 59.740501 -6.6613381e-016 11.311638 59.954521 
		-6.6613381e-016 11.429548 60.112995 -6.6613381e-016 11.360828 60.11121 -6.6613381e-016 
		11.722425 59.706982 -6.6613381e-016 11.953451 59.706982 -6.6613381e-016 11.311657 
		60.519005 -6.6613381e-016 11.311657 60.146828 -6.6613381e-016 11.671162 60.353394 
		-6.6613381e-016 11.442905 60.553009 -6.6613381e-016 11.357441 60.146435 -6.6613381e-016 
		11.680429 60.168835 -6.6613381e-016 11.210163 60.168842 -6.6613381e-016 11.543217 
		60.168842 -6.6613381e-016 11.311657 60.168842 -6.6613381e-016 11.514133 59.995731 
		-6.6613381e-016 11.514133 60.160767 -6.6613381e-016 11.209993 59.861317 -6.6613381e-016 
		11.311741 59.861317 -6.6613381e-016 11.250544 59.706982 -6.6613381e-016 11.202629 
		59.794968 -6.6613381e-016 11.162796 59.750523 -6.6613381e-016 11.162682 59.706982 
		-6.6613381e-016 11.338408 59.706982 -6.6613381e-016 11.338408 59.762783 -6.6613381e-016 
		11.319035 59.794922 -6.6613381e-016 11.42627 59.706982 -6.6613381e-016 11.42627 59.740551 
		-6.6613381e-016 11.210094 59.970928 -6.6613381e-016 11.210121 60.058914 -6.6613381e-016 
		11.311638 59.970928 -6.6613381e-016 11.338408 60.111542 -6.6613381e-016 11.338408 
		60.146667 -6.6613381e-016 11.311651 60.058914 -6.6613381e-016 11.468559 60.058914 
		-6.6613381e-016 11.42627 60.112869 -6.6613381e-016 11.42627 60.148552 -6.6613381e-016 
		11.740192 59.86124 -6.6613381e-016 11.611097 59.861317 -6.6613381e-016 11.689859 
		59.752125 -6.6613381e-016 11.658958 59.794964 -6.6613381e-016 11.777773 59.820366 
		-6.6613381e-016 11.777725 59.706982 -6.6613381e-016 11.80529 59.79501 -6.6613381e-016 
		11.865602 59.759583 -6.6613381e-016 11.865587 59.706982 -6.6613381e-016 11.690096 
		59.929199 -6.6613381e-016 11.65947 59.971004 -6.6613381e-016 11.532024 59.970928 
		-6.6613381e-016 11.601997 59.873928 -6.6613381e-016 11.595348 60.058914 -6.6613381e-016 
		11.601997 60.049774 -6.6613381e-016 11.601995 60.13377 -6.6613381e-016 11.514145 
		60.583176 -6.6613381e-016 11.514112 60.54427 -6.6613381e-016 11.210115 60.322861 
		-6.6613381e-016 11.311657 60.322861 -6.6613381e-016 11.21014 60.234879 -6.6613381e-016 
		11.311657 60.234879 -6.6613381e-016 11.250544 60.586678 -6.6613381e-016 11.210194 
		60.410843 -6.6613381e-016 11.202248 60.498745 -6.6613381e-016 11.162682 60.586666 
		-6.6613381e-016 11.162674 60.543308 -6.6613381e-016 11.311657 60.410843 -6.6613381e-016 
		11.338408 60.586723 -6.6613381e-016 11.338408 60.52985 -6.6613381e-016 11.311657 
		60.498825 -6.6613381e-016 11.426271 60.586739 -6.6613381e-016 11.42627 60.552345 
		-6.6613381e-016 11.78339 60.322861 -6.6613381e-016 11.669218 60.322857 -6.6613381e-016 
		11.689861 60.174965 -6.6613381e-016 11.635315 60.234879 -6.6613381e-016 11.602022 
		60.199005 -6.6613381e-016 11.7777 60.294861 -6.6613381e-016 11.749996 60.234879 -6.6613381e-016 
		11.689817 60.531666 -6.6613381e-016 11.663282 60.410778 -6.6613381e-016 11.605997 
		60.499004 -6.6613381e-016 11.601936 60.57008 -6.6613381e-016 11.602139 60.502182 
		-6.6613381e-016 11.777916 60.410824 -6.6613381e-016 11.777649 60.4118 -6.6613381e-016 
		11.727568 60.498974 -6.6613381e-016;
	setAttr -s 101 ".vt[0:100]"  40.28850174 -36.64947891 1.95106673 39.4828186 -35.89032364 1.95106673
		 38.53123093 -34.95776749 1.95106673 39.16210175 -34.95742798 1.95106673 39.95251083 -35.42465591 1.95106673
		 38.53123093 -35.025432587 1.95106673 38.53123093 -36.64947891 1.95106673 38.8019104 -35.34606552 1.95106673
		 38.58647919 -35.024879456 1.95106673 38.80197144 -35.31235123 1.95106673 38.80194855 -36.36424255 1.95106673
		 38.58683777 -36.64997864 1.95106673 38.53123093 -36.71714401 1.95106673 39.27558899 -36.71714401 1.95106673
		 39.27558899 -36.64947891 1.95106673 39.0049133301 -35.90512085 1.95106673 39.21798706 -36.65010834 1.95106673
		 39.0048751831 -36.22206879 1.95106673 39.24069595 -35.90512085 1.95106673 39.10325623 -35.90868759 1.95106673
		 39.82645035 -36.71714401 1.95106673 40.28850174 -36.71714401 1.95106673 39.0049133301 -35.093101501 1.95106673
		 39.0049133301 -35.83745575 1.95106673 39.72392273 -35.42432022 1.95106673 39.26741028 -35.025093079 1.95106673
		 39.096481323 -35.83823776 1.95106673 39.74245834 -35.79343796 1.95106673 38.80192566 -35.79342651 1.95106673
		 39.46803284 -35.79342651 1.95106673 39.0049133301 -35.79342651 1.95106673 39.40986633 -36.13964462 1.95106673
		 39.40986633 -35.80957413 1.95106673 38.80158615 -36.40847778 1.95106673 39.0050811768 -36.40847778 1.95106673
		 38.88268661 -36.71714401 1.95106673 38.7868576 -36.54117584 1.95106673 38.70719147 -36.6300621 1.95106673
		 38.70696259 -36.71714401 1.95106673 39.058414459 -36.71714401 1.95106673 39.058414459 -36.60554504 1.95106673
		 39.019668579 -36.5412674 1.95106673 39.23413849 -36.71714401 1.95106673 39.23413849 -36.65000534 1.95106673
		 38.80178833 -36.18925095 1.95106673 38.80184174 -36.013282776 1.95106673 39.0048751831 -36.18925095 1.95106673
		 39.058414459 -35.90802765 1.95106673 39.058414459 -35.83777618 1.95106673 39.004901886 -36.013282776 1.95106673
		 39.31871796 -36.013282776 1.95106673 39.23413849 -35.90537262 1.95106673 39.23413849 -35.83400345 1.95106673
		 39.86198425 -36.40862656 1.95106673 39.6037941 -36.40847778 1.95106673 39.76131821 -36.62685776 1.95106673
		 39.6995163 -36.54117966 1.95106673 39.93714523 -36.49037552 1.95106673 39.93704987 -36.71714401 1.95106673
		 39.99217987 -36.5410881 1.95106673 40.11280441 -36.61194229 1.95106673 40.1127739 -36.71714401 1.95106673
		 39.76179123 -36.27271271 1.95106673 39.70053864 -36.18909836 1.95106673 39.44564819 -36.18925095 1.95106673
		 39.58559418 -36.38325119 1.95106673 39.57229614 -36.013282776 1.95106673 39.58559418 -36.03155899 1.95106673
		 39.58559036 -35.86356735 1.95106673 39.40988922 -34.96475601 1.95106673 39.40982437 -35.042572021 1.95106673
		 38.80183029 -35.48538589 1.95106673 39.0049133301 -35.48538589 1.95106673 38.80187988 -35.66135025 1.95106673
		 39.0049133301 -35.66135025 1.95106673 38.88268661 -34.95775604 1.95106673 38.80198669 -35.30942154 1.95106673
		 38.78609467 -35.13362122 1.95106673 38.70696259 -34.95777512 1.95106673 38.70694733 -35.044494629 1.95106673
		 39.0049133301 -35.30942154 1.95106673 39.058414459 -34.95766449 1.95106673 39.058414459 -35.071411133 1.95106673
		 39.0049133301 -35.13345718 1.95106673 39.2341423 -34.95763016 1.95106673 39.23413849 -35.026420593 1.95106673
		 39.94837952 -35.48538589 1.95106673 39.72003555 -35.48539734 1.95106673 39.76132202 -35.78117752 1.95106673
		 39.65222931 -35.66135025 1.95106673 39.58564377 -35.73310089 1.95106673 39.93700027 -35.54138565 1.95106673
		 39.8815918 -35.66135406 1.95106673 39.76123428 -35.067779541 1.95106673 39.70816422 -35.30955505 1.95106673
		 39.5935936 -35.13310242 1.95106673 39.58547211 -34.99095154 1.95106673 39.58587646 -35.12674713 1.95106673
		 39.93743134 -35.3094635 1.95106673 39.93689728 -35.30750656 1.95106673 39.83673477 -35.13315964 1.95106673;
	setAttr -s 101 ".ed[0:100]"  98 99 0 53 62 0 51 18 0 18 50 0 32 52 0 42 13 0
		 13 14 0 14 43 0 33 36 0 36 37 0 38 35 0 37 11 0 11 6 0 6 12 0 12 38 0 41 34 0 35 39 0
		 40 41 0 39 42 0 43 16 0 16 40 0 28 45 0 44 10 0 10 33 0 45 44 0 34 17 0 17 46 0 49 15 0
		 15 47 0 48 23 0 23 30 0 46 49 0 50 31 0 47 19 0 19 51 0 52 26 0 26 48 0 59 57 0 54 56 0
		 56 55 0 57 53 0 55 20 0 20 58 0 0 60 0 61 21 0 21 0 0 60 59 0 58 61 0 68 27 0 62 63 0
		 65 54 0 64 65 0 63 67 0 67 66 0 31 64 0 66 1 0 1 68 0 29 32 0 69 84 0 85 25 0 25 70 0
		 74 72 0 71 73 0 73 28 0 30 74 0 75 78 0 79 77 0 76 9 0 9 7 0 7 71 0 77 76 0 78 2 0
		 2 5 0 5 8 0 8 79 0 72 80 0 81 75 0 83 22 0 22 82 0 80 83 0 84 3 0 3 81 0 82 85 0
		 91 86 0 87 89 0 27 88 0 89 90 0 90 29 0 92 91 0 88 92 0 93 96 0 97 95 0 94 24 0 24 87 0
		 95 94 0 96 69 0 70 97 0 86 4 0 4 98 0 100 93 0 99 100 0;
	setAttr -ch 101 ".fc[0]" -type "polyFaces" 
		f 78 90 95 58 80 81 76 65 71 72 73 74 66 70 67 68 69 62 63 21 24 22 23 8 9 11 12 13
		 14 10 16 18 5 6 7 19 20 17 15 25 26 31 27 28 33 34 2 3 32 54 51 50 38 39 41 42 47
		 44 45 43 46 37 40 1 49 52 53 55 56 48 85 89 88 83 97 98 0 100 99
		mu 0 78 93 96 69 84 3 81 75 78 2 5 8 79 77 76 9 7 71 73 28 45 44 10 33 36 37 11 6 12 38
		 35 39 42 13 14 43 16 40 41 34 17 46 49 15 47 19 51 18 50 31 64 65 54 56 55 20 58
		 61 21 0 60 59 57 53 62 63 67 66 1 68 27 88 92 91 86 4 98 99 100
		h 23 92 93 84 86 87 57 4 35 36 29 30 64 61 75 79 77 78 82 59 60 96 91 94
		mu 0 23 94 24 87 89 90 29 32 52 26 48 23 30 74 72 80 83 22 82 85 25 70 97 95;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_l_hands_letter_" -p "FM_Cam_c_hands_letter_";
	setAttr ".rp" -type "double3" 31.473827357812446 24.309456194030119 1.9510667324066158 ;
	setAttr ".sp" -type "double3" 31.473827357812446 24.309456194030119 1.9510667324066158 ;
createNode mesh -n "FM_Cam_l_hands_letter_Shape" -p "FM_Cam_l_hands_letter_";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 65 ".uvst[0].uvsp[0:64]" -type "float2" 0.5 0.96153843 0.5
		 1 0 1 0 0.96153843 0 0.03846154 0.18181819 0.77929688 0.037112322 0.96185249 0.18184367
		 0.79841685 0.18199997 0.18732584 0.03735061 0.038129896 0 0 0.90909094 0 1 0.26442358
		 0.95454544 0.26923078 0.31818181 0.26183149 0.53582644 0.03818519 0.31797534 0.1892273
		 0.31817323 0.799263 0.49106994 0.96157098 0.18181819 0.45454547 0.31818181 0.45454547
		 0.44444445 0 0.44444445 0.038968313 0.18198383 0.18181819 0.31798223 0.18181819 0.22222222
		 0 0.16807985 0.090909094 0.11111111 0.047184724 0.11111111 0 0.32395512 0.090909094
		 0.33333334 0 0.33333334 0.068046808 0.18181819 0.27272728 0.18181819 0.36363637 0.31818181
		 0.27272728 0.31818181 0.36363637 0.97160017 0.18181819 0.91021633 0.18181819 0.66666669
		 0 0.66666669 0.040785223 0.55555558 0 0.55555558 0.038219575 0.77777779 0 0.77777779
		 0.060597908 0.94034553 0.090909094 0.83155572 0.090909094 0.8888889 0 0.8888889 0.14959854
		 0.44444445 1 0.44444445 0.96017241 0.18181819 0.72727275 0.31818181 0.72727275 0.18181819
		 0.54545456 0.18181819 0.63636363 0.31818181 0.54545456 0.31818181 0.63636363 0.22222222
		 1 0.18170518 0.81818181 0.16815327 0.90909094 0.11111111 1 0.11111111 0.95306927
		 0.31825608 0.81818181 0.32946685 0.90909094 0.33333334 1 0.33333334 0.91575831;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 65 ".pt[0:64]" -type "float3"  19.028618 60.552925 -6.6613381e-016 
		19.028618 60.586758 -6.6613381e-016 18.656441 60.586758 -6.6613381e-016 18.656441 
		60.552925 -6.6613381e-016 18.656441 59.740902 -6.6613381e-016 18.791779 60.392609 
		-6.6613381e-016 18.684065 60.5532 -6.6613381e-016 18.791805 60.409428 -6.6613381e-016 
		18.792013 59.871857 -6.6613381e-016 18.684242 59.740608 -6.6613381e-016 18.656441 
		59.707069 -6.6613381e-016 19.333126 59.707069 -6.6613381e-016 19.400795 59.939678 
		-6.6613381e-016 19.366959 59.943909 -6.6613381e-016 18.89325 59.937401 -6.6613381e-016 
		19.055286 59.740547 -6.6613381e-016 18.893127 59.873528 -6.6613381e-016 18.893257 
		60.410172 -6.6613381e-016 19.021969 60.552952 -6.6613381e-016 18.79179 60.10693 -6.6613381e-016 
		18.89328 60.10693 -6.6613381e-016 18.987263 59.707069 -6.6613381e-016 18.987261 59.741261 
		-6.6613381e-016 18.792007 59.867012 -6.6613381e-016 18.893127 59.867012 -6.6613381e-016 
		18.821854 59.707069 -6.6613381e-016 18.781292 59.787144 -6.6613381e-016 18.739128 
		59.748623 -6.6613381e-016 18.739147 59.707069 -6.6613381e-016 18.897589 59.787041 
		-6.6613381e-016 18.904558 59.707069 -6.6613381e-016 18.904394 59.766838 -6.6613381e-016 
		18.791653 59.946983 -6.6613381e-016 18.791664 60.026955 -6.6613381e-016 18.893269 
		59.946983 -6.6613381e-016 18.89328 60.026955 -6.6613381e-016 19.379654 59.867012 
		-6.6613381e-016 19.334053 59.866962 -6.6613381e-016 19.152676 59.707069 -6.6613381e-016 
		19.152691 59.742752 -6.6613381e-016 19.069969 59.707069 -6.6613381e-016 19.069969 
		59.740646 -6.6613381e-016 19.235382 59.707069 -6.6613381e-016 19.235382 59.760372 
		-6.6613381e-016 19.356388 59.787041 -6.6613381e-016 19.275406 59.787045 -6.6613381e-016 
		19.318089 59.707069 -6.6613381e-016 19.317993 59.838726 -6.6613381e-016 18.987263 
		60.586758 -6.6613381e-016 18.987263 60.551727 -6.6613381e-016 18.791763 60.34684 
		-6.6613381e-016 18.89328 60.34684 -6.6613381e-016 18.791851 60.186897 -6.6613381e-016 
		18.791809 60.266869 -6.6613381e-016 18.89328 60.186897 -6.6613381e-016 18.89328 60.266869 
		-6.6613381e-016 18.821854 60.586758 -6.6613381e-016 18.791779 60.426815 -6.6613381e-016 
		18.781292 60.506668 -6.6613381e-016 18.739147 60.586758 -6.6613381e-016 18.739128 
		60.545425 -6.6613381e-016 18.89333 60.426815 -6.6613381e-016 18.901794 60.506741 
		-6.6613381e-016 18.904558 60.586758 -6.6613381e-016 18.904629 60.512611 -6.6613381e-016;
	setAttr -s 65 ".vt[0:64]"  12.44521141 -35.025432587 1.95106673 12.44521141 -34.95776749 1.95106673
		 11.70085716 -34.95776749 1.95106673 11.70085716 -35.025432587 1.95106673 11.70085716 -36.64947891 1.95106673
		 11.97153664 -35.34606552 1.95106673 11.75610638 -35.024879456 1.95106673 11.97158623 -35.31242371 1.95106673
		 11.97200298 -36.38756561 1.95106673 11.7564621 -36.65006256 1.95106673 11.70085716 -36.71714401 1.95106673
		 13.054226875 -36.71714401 1.95106673 13.18956375 -36.25192642 1.95106673 13.12189484 -36.24346542 1.95106673
		 12.17447758 -36.25648117 1.95106673 12.4985466 -36.65018845 1.95106673 12.17423153 -36.38422394 1.95106673
		 12.17449188 -35.31093979 1.95106673 12.43191624 -35.025375366 1.95106673 11.9715538 -35.91742325 1.95106673
		 12.17453671 -35.91742325 1.95106673 12.36250401 -36.71714401 1.95106673 12.36249828 -36.64876175 1.95106673
		 11.97199345 -36.39725876 1.95106673 12.17422867 -36.39725494 1.95106673 12.031681061 -36.71714401 1.95106673
		 11.95056057 -36.55699158 1.95106673 11.86623287 -36.63403702 1.95106673 11.86627007 -36.71714401 1.95106673
		 12.18315411 -36.55719757 1.95106673 12.19709301 -36.71714401 1.95106673 12.19676495 -36.59760284 1.95106673
		 11.97128201 -36.23731232 1.95106673 11.97130299 -36.07736969 1.95106673 12.17451286 -36.23731232 1.95106673
		 12.17453671 -36.07736969 1.95106673 13.14728546 -36.39725494 1.95106673 13.056084633 -36.39735413 1.95106673
		 12.69332886 -36.71714401 1.95106673 12.69335556 -36.64577484 1.95106673 12.52791691 -36.71714401 1.95106673
		 12.52791691 -36.64998627 1.95106673 12.85873985 -36.71714401 1.95106673 12.85874271 -36.61053467 1.95106673
		 13.10075569 -36.55720139 1.95106673 12.93879032 -36.55719376 1.95106673 13.024151802 -36.71714401 1.95106673
		 13.023965836 -36.4538269 1.95106673 12.36250401 -34.95776749 1.95106673 12.36250401 -35.027824402 1.95106673
		 11.97150612 -35.43759918 1.95106673 12.17453671 -35.43759918 1.95106673 11.97168159 -35.75748444 1.95106673
		 11.97159767 -35.59754181 1.95106673 12.17453671 -35.75748444 1.95106673 12.17453671 -35.59754181 1.95106673
		 12.031681061 -34.95776749 1.95106673 11.97153473 -35.27764893 1.95106673 11.95055866 -35.11794281 1.95106673
		 11.86627007 -34.95776749 1.95106673 11.86623478 -35.040428162 1.95106673 12.17463684 -35.27765274 1.95106673
		 12.19156265 -35.11780167 1.95106673 12.19709301 -34.95776749 1.95106673 12.19723606 -35.10606003 1.95106673;
	setAttr -s 65 ".ed[0:64]"  0 1 0 1 48 0 49 18 0 18 0 0 36 12 0 12 13 0
		 13 37 0 35 20 0 29 24 0 23 26 0 26 27 0 28 25 0 27 9 0 9 4 0 4 10 0 10 28 0 30 21 0
		 22 31 0 25 30 0 31 29 0 19 33 0 32 8 0 8 23 0 33 32 0 24 16 0 16 14 0 14 34 0 34 35 0
		 44 36 0 37 47 0 40 38 0 39 41 0 21 40 0 41 15 0 15 22 0 38 42 0 43 39 0 46 11 0 11 44 0
		 42 46 0 45 43 0 47 45 0 48 63 0 64 49 0 55 51 0 50 53 0 52 19 0 53 52 0 20 54 0 54 55 0
		 56 59 0 60 58 0 57 7 0 7 5 0 5 50 0 58 57 0 59 2 0 2 3 0 3 6 0 6 60 0 51 17 0 17 61 0
		 61 62 0 63 56 0 62 64 0;
	setAttr -ch 65 ".fc[0]" -type "polyFaces" 
		f 65 64 43 2 3 0 1 42 63 50 56 57 58 59 51 55 52 53 54 45 47 46 20 23 21 22 9 10 12
		 13 14 15 11 18 16 32 30 35 39 37 38 28 4 5 6 29 41 40 36 31 33 34 17 19 8 24 25 26
		 27 7 48 49 44 60 61 62
		mu 0 65 62 64 49 18 0 1 48 63 56 59 2 3 6 60 58 57 7 5 50 53 52 19 33 32 8 23 26 27 9 4
		 10 28 25 30 21 40 38 42 46 11 44 36 12 13 37 47 45 43 39 41 15 22 31 29 24 16 14
		 34 35 20 54 55 51 17 61;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_FEET_gui_guides_grp" -p "FM_Cam_BODY_gui_guides_grp";
	setAttr ".rp" -type "double3" 41.490046501159668 -13.781187057495117 3.1554436208840472e-030 ;
	setAttr ".sp" -type "double3" 41.490046501159668 -13.781187057495117 3.1554436208840472e-030 ;
createNode transform -n "FM_Cam_FEET_backgroundColor_" -p "FM_Cam_FEET_gui_guides_grp";
	setAttr ".rp" -type "double3" 41.490046501159668 -13.781187057495117 3.1554436208840472e-030 ;
	setAttr ".sp" -type "double3" 41.490046501159668 -13.781187057495117 3.1554436208840472e-030 ;
createNode mesh -n "FM_Cam_FEET_backgroundColor_Shape" -p "FM_Cam_FEET_backgroundColor_";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 4 ".uvst[0].uvsp[0:3]" -type "float2" 0.97244126 0.28292441
		 0.5975672 0.28292441 0.5975672 0.0048881508 0.97244126 0.0048881508;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 4 ".vt[0:3]"  59.70320511 -27.289505 3.1554436e-030 23.27688789 -27.289505 3.1554436e-030
		 59.70320511 -0.27286911 3.1554436e-030 23.27688789 -0.27286911 3.1554436e-030;
	setAttr -s 4 ".ed[0:3]"  0 2 0 1 0 0 3 1 0 2 3 0;
	setAttr -ch 4 ".fc[0]" -type "polyFaces" 
		f 4 3 2 1 0
		mu 0 4 0 1 2 3;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_characters_feet_picture_" -p "FM_Cam_FEET_gui_guides_grp";
	setAttr ".t" -type "double3" 40.115631323849534 -17.971989125631723 0.80267380134855038 ;
	setAttr ".s" -type "double3" 0.62481225493121351 0.62481225493121351 0.62481225493121351 ;
	setAttr ".rp" -type "double3" -13.657747987065303 14.209877383785503 1.3367185745974945 ;
	setAttr ".sp" -type "double3" -21.858963039335563 22.74263552232965 2.1393923759460445 ;
	setAttr ".spt" -type "double3" 8.2012150522702605 -8.5327581385441462 -0.80267380134854993 ;
createNode mesh -n "FM_Cam_characters_feet_picture_Shape" -p "FM_Cam_characters_feet_picture_";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.24935289472341537 0.77852830290794373 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 4 ".uvst[0].uvsp[0:3]" -type "float2" 0.04565233 0.98222882
		 0.45305347 0.98222882 0.45305347 0.57482779 0.04565233 0.57482779;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 4 ".pt[0:3]" -type "float3"  15.277567 60.843781 -4.4408921e-016 
		15.277567 60.843781 -4.4408921e-016 15.277567 60.843781 -4.4408921e-016 15.277567 
		60.843781 -4.4408921e-016;
	setAttr -s 4 ".vt[0:3]"  -40.94549179 -34.29218292 2.13939238 -33.32756805 -34.29218292 2.13939238
		 -40.94549179 -41.91011047 2.13939238 -33.32756805 -41.91011047 2.13939238;
	setAttr -s 4 ".ed[0:3]"  0 1 0 0 2 0 1 3 0 2 3 0;
	setAttr -ch 4 ".fc[0]" -type "polyFaces" 
		f 4 1 3 -3 -1
		mu 0 4 0 3 2 1;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_l_hi_feet_" -p "FM_Cam_FEET_gui_guides_grp";
	setAttr ".rp" -type "double3" 33.455117225646973 -7.1997222900390625 2.1393921375274658 ;
	setAttr ".sp" -type "double3" 33.455117225646973 -7.1997222900390625 2.1393921375274658 ;
createNode transform -n "Lf_Toe_thumb3_guide" -p "FM_Cam_l_hi_feet_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 37.542081832885742 -4.178924560546875 2.1393921375274658 ;
	setAttr ".sp" -type "double3" 37.542081832885742 -4.178924560546875 2.1393921375274658 ;
createNode mesh -n "Lf_Toe_thumb3_guideShape" -p "Lf_Toe_thumb3_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193001 0.61471206 0.80727184 0.7219848 0.7221396 0.80711704 0.61486673 0.86177522
		 0.49595416 0.8806091 0.3770414 0.86177522 0.2697686 0.80711704 0.18463637 0.7219848
		 0.12997819 0.61471206 0.11114423 0.49579921 0.12997819 0.37688643 0.18463637 0.26961371
		 0.26976854 0.1844815 0.37704134 0.12982315 0.49595416 0.11098927 0.61486691 0.12982315
		 0.72213972 0.18448138 0.80727196 0.26961353 0.86193019 0.37688643;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  21.26266098 -65.1118927 2.13939214 21.34187317 -64.95642853 2.13939214
		 21.46524048 -64.83306122 2.13939214 21.62069702 -64.75385284 2.13939214 21.79301834 -64.7265625 2.13939214
		 21.96534348 -64.75385284 2.13939214 22.12079239 -64.83306122 2.13939214 22.24416733 -64.95642853 2.13939214
		 22.3233757 -65.1118927 2.13939214 22.35066986 -65.28421021 2.13939214 22.3233757 -65.45653534 2.13939214
		 22.24416733 -65.61198425 2.13939214 22.12079239 -65.73535919 2.13939214 21.96534348 -65.81456757 2.13939214
		 21.79301834 -65.84185791 2.13939214 21.62069702 -65.81456757 2.13939214 21.46524048 -65.73535919 2.13939214
		 21.34187317 -65.61198425 2.13939214 21.26266098 -65.45653534 2.13939214 21.23537064 -65.28421021 2.13939214;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 -19 -18 -17 -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 -20
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "Lf_Toe_thumb2_guide" -p "FM_Cam_l_hi_feet_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 37.636850357055664 -6.1217117309570313 2.1393921375274658 ;
	setAttr ".sp" -type "double3" 37.636850357055664 -6.1217117309570313 2.1393921375274658 ;
createNode mesh -n "Lf_Toe_thumb2_guideShape" -p "Lf_Toe_thumb2_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193001 0.61471206 0.80727184 0.7219848 0.7221396 0.80711704 0.61486673 0.86177522
		 0.49595416 0.8806091 0.3770414 0.86177522 0.2697686 0.80711704 0.18463637 0.7219848
		 0.12997819 0.61471206 0.11114423 0.49579921 0.12997819 0.37688643 0.18463637 0.26961371
		 0.26976854 0.1844815 0.37704134 0.12982315 0.49595416 0.11098927 0.61486691 0.12982315
		 0.72213972 0.18448138 0.80727196 0.26961353 0.86193019 0.37688643;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  21.3574295 -67.054679871 2.13939214 21.43664169 -66.8992157 2.13939214
		 21.560009 -66.77584839 2.13939214 21.71546555 -66.69664001 2.13939214 21.88778687 -66.66934967 2.13939214
		 22.060112 -66.69664001 2.13939214 22.21556091 -66.77584839 2.13939214 22.33893585 -66.8992157 2.13939214
		 22.41814423 -67.054679871 2.13939214 22.44543839 -67.22699738 2.13939214 22.41814423 -67.39932251 2.13939214
		 22.33893585 -67.55477142 2.13939214 22.21556091 -67.67814636 2.13939214 22.060112 -67.75735474 2.13939214
		 21.88778687 -67.78464508 2.13939214 21.71546555 -67.75735474 2.13939214 21.560009 -67.67814636 2.13939214
		 21.43664169 -67.55477142 2.13939214 21.3574295 -67.39932251 2.13939214 21.33013916 -67.22699738 2.13939214;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 -19 -18 -17 -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 -20
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "Lf_Toe_thumb1_guide" -p "FM_Cam_l_hi_feet_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 37.589468002319336 -7.6854248046875 2.1393921375274658 ;
	setAttr ".sp" -type "double3" 37.589468002319336 -7.6854248046875 2.1393921375274658 ;
createNode mesh -n "Lf_Toe_thumb1_guideShape" -p "Lf_Toe_thumb1_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193001 0.61471206 0.80727184 0.7219848 0.7221396 0.80711704 0.61486673 0.86177522
		 0.49595416 0.8806091 0.3770414 0.86177522 0.2697686 0.80711704 0.18463637 0.7219848
		 0.12997819 0.61471206 0.11114423 0.49579921 0.12997819 0.37688643 0.18463637 0.26961371
		 0.26976854 0.1844815 0.37704134 0.12982315 0.49595416 0.11098927 0.61486691 0.12982315
		 0.72213972 0.18448138 0.80727196 0.26961353 0.86193019 0.37688643;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  21.31004715 -68.61838531 2.13939214 21.38925934 -68.46292114 2.13939214
		 21.51262665 -68.33955383 2.13939214 21.66808319 -68.26034546 2.13939214 21.84040451 -68.23306274 2.13939214
		 22.012729645 -68.26034546 2.13939214 22.16817856 -68.33955383 2.13939214 22.2915535 -68.46292114 2.13939214
		 22.37076187 -68.61838531 2.13939214 22.39805603 -68.79071045 2.13939214 22.37076187 -68.96302795 2.13939214
		 22.2915535 -69.1184845 2.13939214 22.16817856 -69.24185181 2.13939214 22.012729645 -69.32106018 2.13939214
		 21.84040451 -69.34835815 2.13939214 21.66808319 -69.32106018 2.13939214 21.51262665 -69.24185181 2.13939214
		 21.38925934 -69.1184845 2.13939214 21.31004715 -68.96302795 2.13939214 21.28275681 -68.79071045 2.13939214;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 -19 -18 -17 -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 -20
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "Lf_Toe_index3_guide" -p "FM_Cam_l_hi_feet_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 34.53312873840332 -4.0130767822265625 2.1393921375274658 ;
	setAttr ".sp" -type "double3" 34.53312873840332 -4.0130767822265625 2.1393921375274658 ;
createNode mesh -n "Lf_Toe_index3_guideShape" -p "Lf_Toe_index3_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193001 0.61471206 0.80727184 0.7219848 0.7221396 0.80711704 0.61486673 0.86177522
		 0.49595416 0.8806091 0.3770414 0.86177522 0.2697686 0.80711704 0.18463637 0.7219848
		 0.12997819 0.61471206 0.11114423 0.49579921 0.12997819 0.37688643 0.18463637 0.26961371
		 0.26976854 0.1844815 0.37704134 0.12982315 0.49595416 0.11098927 0.61486691 0.12982315
		 0.72213972 0.18448138 0.80727196 0.26961353 0.86193019 0.37688643;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  18.25370789 -64.94604492 2.13939214 18.33292007 -64.79058075 2.13939214
		 18.45628738 -64.66721344 2.13939214 18.61174393 -64.58800507 2.13939214 18.78406525 -64.56071472 2.13939214
		 18.95639038 -64.58800507 2.13939214 19.11183929 -64.66721344 2.13939214 19.23521423 -64.79058075 2.13939214
		 19.31442261 -64.94604492 2.13939214 19.34171677 -65.11836243 2.13939214 19.31442261 -65.29068756 2.13939214
		 19.23521423 -65.44613647 2.13939214 19.11183929 -65.56951141 2.13939214 18.95639038 -65.64871979 2.13939214
		 18.78406525 -65.67601013 2.13939214 18.61174393 -65.64871979 2.13939214 18.45628738 -65.56951141 2.13939214
		 18.33292007 -65.44613647 2.13939214 18.25370789 -65.29068756 2.13939214 18.22641754 -65.11836243 2.13939214;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 -19 -18 -17 -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 -20
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "Lf_Toe_index2_guide" -p "FM_Cam_l_hi_feet_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 34.675283432006836 -5.363555908203125 2.1393921375274658 ;
	setAttr ".sp" -type "double3" 34.675283432006836 -5.363555908203125 2.1393921375274658 ;
createNode mesh -n "Lf_Toe_index2_guideShape" -p "Lf_Toe_index2_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193001 0.61471206 0.80727184 0.7219848 0.7221396 0.80711704 0.61486673 0.86177522
		 0.49595416 0.8806091 0.3770414 0.86177522 0.2697686 0.80711704 0.18463637 0.7219848
		 0.12997819 0.61471206 0.11114423 0.49579921 0.12997819 0.37688643 0.18463637 0.26961371
		 0.26976854 0.1844815 0.37704134 0.12982315 0.49595416 0.11098927 0.61486691 0.12982315
		 0.72213972 0.18448138 0.80727196 0.26961353 0.86193019 0.37688643;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  18.39586258 -66.29651642 2.13939214 18.47507477 -66.14105225 2.13939214
		 18.59844208 -66.017684937 2.13939214 18.75389862 -65.93847656 2.13939214 18.92621994 -65.91119385 2.13939214
		 19.098545074 -65.93847656 2.13939214 19.25399399 -66.017684937 2.13939214 19.37736893 -66.14105225 2.13939214
		 19.4565773 -66.29651642 2.13939214 19.48387146 -66.46884155 2.13939214 19.4565773 -66.64115906 2.13939214
		 19.37736893 -66.7966156 2.13939214 19.25399399 -66.91998291 2.13939214 19.098545074 -66.99919128 2.13939214
		 18.92621994 -67.026489258 2.13939214 18.75389862 -66.99919128 2.13939214 18.59844208 -66.91998291 2.13939214
		 18.47507477 -66.7966156 2.13939214 18.39586258 -66.64115906 2.13939214 18.36857224 -66.46884155 2.13939214;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 -19 -18 -17 -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 -20
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "Lf_Toe_index1_guide" -p "FM_Cam_l_hi_feet_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 34.841131210327148 -6.7140274047851563 2.1393921375274658 ;
	setAttr ".sp" -type "double3" 34.841131210327148 -6.7140274047851563 2.1393921375274658 ;
createNode mesh -n "Lf_Toe_index1_guideShape" -p "Lf_Toe_index1_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193001 0.61471206 0.80727184 0.7219848 0.7221396 0.80711704 0.61486673 0.86177522
		 0.49595416 0.8806091 0.3770414 0.86177522 0.2697686 0.80711704 0.18463637 0.7219848
		 0.12997819 0.61471206 0.11114423 0.49579921 0.12997819 0.37688643 0.18463637 0.26961371
		 0.26976854 0.1844815 0.37704134 0.12982315 0.49595416 0.11098927 0.61486691 0.12982315
		 0.72213972 0.18448138 0.80727196 0.26961353 0.86193019 0.37688643;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  18.56171036 -67.64698792 2.13939214 18.64092255 -67.49153137 2.13939214
		 18.76428986 -67.36816406 2.13939214 18.9197464 -67.28895569 2.13939214 19.092067719 -67.26166534 2.13939214
		 19.26439285 -67.28895569 2.13939214 19.41984177 -67.36816406 2.13939214 19.54321671 -67.49153137 2.13939214
		 19.62242508 -67.64698792 2.13939214 19.64971924 -67.81931305 2.13939214 19.62242508 -67.99163818 2.13939214
		 19.54321671 -68.1470871 2.13939214 19.41984177 -68.27046204 2.13939214 19.26439285 -68.34967041 2.13939214
		 19.092067719 -68.37696075 2.13939214 18.9197464 -68.34967041 2.13939214 18.76428986 -68.27046204 2.13939214
		 18.64092255 -68.1470871 2.13939214 18.56171036 -67.99163818 2.13939214 18.53442001 -67.81931305 2.13939214;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 -19 -18 -17 -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 -20
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "Lf_Toe_mid3_guide" -p "FM_Cam_l_hi_feet_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 32.163872718811035 -5.1977081298828125 2.1393921375274658 ;
	setAttr ".sp" -type "double3" 32.163872718811035 -5.1977081298828125 2.1393921375274658 ;
createNode mesh -n "Lf_Toe_mid3_guideShape" -p "Lf_Toe_mid3_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193001 0.61471206 0.80727184 0.7219848 0.7221396 0.80711704 0.61486673 0.86177522
		 0.49595416 0.8806091 0.3770414 0.86177522 0.2697686 0.80711704 0.18463637 0.7219848
		 0.12997819 0.61471206 0.11114423 0.49579921 0.12997819 0.37688643 0.18463637 0.26961371
		 0.26976854 0.1844815 0.37704134 0.12982315 0.49595416 0.11098927 0.61486691 0.12982315
		 0.72213972 0.18448138 0.80727196 0.26961353 0.86193019 0.37688643;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  15.88445377 -66.13066864 2.13939214 15.96366596 -65.97520447 2.13939214
		 16.087032318 -65.85183716 2.13939214 16.24248886 -65.77262878 2.13939214 16.41481018 -65.74534607 2.13939214
		 16.58713531 -65.77262878 2.13939214 16.74258423 -65.85183716 2.13939214 16.86595917 -65.97520447 2.13939214
		 16.94516754 -66.13066864 2.13939214 16.9724617 -66.30299377 2.13939214 16.94516754 -66.47531128 2.13939214
		 16.86595917 -66.63076782 2.13939214 16.74258423 -66.75413513 2.13939214 16.58713531 -66.83334351 2.13939214
		 16.41481018 -66.86064148 2.13939214 16.24248886 -66.83334351 2.13939214 16.087032318 -66.75413513 2.13939214
		 15.96366596 -66.63076782 2.13939214 15.88445377 -66.47531128 2.13939214 15.85716152 -66.30299377 2.13939214;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 -19 -18 -17 -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 -20
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "Lf_Toe_mid2_guide" -p "FM_Cam_l_hi_feet_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 32.685110092163086 -6.429718017578125 2.1393921375274658 ;
	setAttr ".sp" -type "double3" 32.685110092163086 -6.429718017578125 2.1393921375274658 ;
createNode mesh -n "Lf_Toe_mid2_guideShape" -p "Lf_Toe_mid2_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193001 0.61471206 0.80727184 0.7219848 0.7221396 0.80711704 0.61486673 0.86177522
		 0.49595416 0.8806091 0.3770414 0.86177522 0.2697686 0.80711704 0.18463637 0.7219848
		 0.12997819 0.61471206 0.11114423 0.49579921 0.12997819 0.37688643 0.18463637 0.26961371
		 0.26976854 0.1844815 0.37704134 0.12982315 0.49595416 0.11098927 0.61486691 0.12982315
		 0.72213972 0.18448138 0.80727196 0.26961353 0.86193019 0.37688643;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  16.40568924 -67.36267853 2.13939214 16.48490143 -67.20722198 2.13939214
		 16.60826874 -67.083854675 2.13939214 16.76372528 -67.0046463013 2.13939214 16.9360466 -66.97735596 2.13939214
		 17.10837173 -67.0046463013 2.13939214 17.26382065 -67.083854675 2.13939214 17.38719559 -67.20722198 2.13939214
		 17.46640396 -67.36267853 2.13939214 17.49369812 -67.53500366 2.13939214 17.46640396 -67.70732117 2.13939214
		 17.38719559 -67.86277771 2.13939214 17.26382065 -67.98614502 2.13939214 17.10837173 -68.065353394 2.13939214
		 16.9360466 -68.092651367 2.13939214 16.76372528 -68.065353394 2.13939214 16.60826874 -67.98614502 2.13939214
		 16.48490143 -67.86277771 2.13939214 16.40568924 -67.70732117 2.13939214 16.3783989 -67.53500366 2.13939214;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 -19 -18 -17 -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 -20
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "Lf_Toe_mid1_guide" -p "FM_Cam_l_hi_feet_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 33.087884902954102 -7.7801971435546875 2.1393921375274658 ;
	setAttr ".sp" -type "double3" 33.087884902954102 -7.7801971435546875 2.1393921375274658 ;
createNode mesh -n "Lf_Toe_mid1_guideShape" -p "Lf_Toe_mid1_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193001 0.61471206 0.80727184 0.7219848 0.7221396 0.80711704 0.61486673 0.86177522
		 0.49595416 0.8806091 0.3770414 0.86177522 0.2697686 0.80711704 0.18463637 0.7219848
		 0.12997819 0.61471206 0.11114423 0.49579921 0.12997819 0.37688643 0.18463637 0.26961371
		 0.26976854 0.1844815 0.37704134 0.12982315 0.49595416 0.11098927 0.61486691 0.12982315
		 0.72213972 0.18448138 0.80727196 0.26961353 0.86193019 0.37688643;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  16.80846405 -68.71315765 2.13939214 16.88767624 -68.55769348 2.13939214
		 17.011043549 -68.43432617 2.13939214 17.16650009 -68.3551178 2.13939214 17.33882141 -68.32783508 2.13939214
		 17.51114655 -68.3551178 2.13939214 17.66659546 -68.43432617 2.13939214 17.7899704 -68.55769348 2.13939214
		 17.86917877 -68.71315765 2.13939214 17.89647293 -68.88548279 2.13939214 17.86917877 -69.057800293 2.13939214
		 17.7899704 -69.21325684 2.13939214 17.66659546 -69.33662415 2.13939214 17.51114655 -69.41583252 2.13939214
		 17.33882141 -69.44313049 2.13939214 17.16650009 -69.41583252 2.13939214 17.011043549 -69.33662415 2.13939214
		 16.88767624 -69.21325684 2.13939214 16.80846405 -69.057800293 2.13939214 16.78117371 -68.88548279 2.13939214;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 -19 -18 -17 -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 -20
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "Lf_Toe_ring3_guide" -p "FM_Cam_l_hi_feet_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 30.647551536560059 -6.8087921142578125 2.1393921375274658 ;
	setAttr ".sp" -type "double3" 30.647551536560059 -6.8087921142578125 2.1393921375274658 ;
createNode mesh -n "Lf_Toe_ring3_guideShape" -p "Lf_Toe_ring3_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193001 0.61471206 0.80727184 0.7219848 0.7221396 0.80711704 0.61486673 0.86177522
		 0.49595416 0.8806091 0.3770414 0.86177522 0.2697686 0.80711704 0.18463637 0.7219848
		 0.12997819 0.61471206 0.11114423 0.49579921 0.12997819 0.37688643 0.18463637 0.26961371
		 0.26976854 0.1844815 0.37704134 0.12982315 0.49595416 0.11098927 0.61486691 0.12982315
		 0.72213972 0.18448138 0.80727196 0.26961353 0.86193019 0.37688643;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  14.36813259 -67.74176025 2.13939214 14.44734478 -67.58630371 2.13939214
		 14.57071209 -67.4629364 2.13939214 14.72616863 -67.38372803 2.13939214 14.89848995 -67.35643005 2.13939214
		 15.070815086 -67.38372803 2.13939214 15.226264 -67.4629364 2.13939214 15.34963894 -67.58630371 2.13939214
		 15.42884541 -67.74176025 2.13939214 15.45614147 -67.91407776 2.13939214 15.42884541 -68.086402893 2.13939214
		 15.34963894 -68.24185181 2.13939214 15.226264 -68.36522675 2.13939214 15.070815086 -68.44443512 2.13939214
		 14.89848995 -68.47172546 2.13939214 14.72616863 -68.44443512 2.13939214 14.57071209 -68.36522675 2.13939214
		 14.44734478 -68.24185181 2.13939214 14.36813259 -68.086402893 2.13939214 14.34084034 -67.91407776 2.13939214;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 -19 -18 -17 -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 -20
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "Lf_Toe_ring2_guide" -p "FM_Cam_l_hi_feet_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 31.263558387756348 -7.8749618530273437 2.1393921375274658 ;
	setAttr ".sp" -type "double3" 31.263558387756348 -7.8749618530273437 2.1393921375274658 ;
createNode mesh -n "Lf_Toe_ring2_guideShape" -p "Lf_Toe_ring2_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193001 0.61471206 0.80727184 0.7219848 0.7221396 0.80711704 0.61486673 0.86177522
		 0.49595416 0.8806091 0.3770414 0.86177522 0.2697686 0.80711704 0.18463637 0.7219848
		 0.12997819 0.61471206 0.11114423 0.49579921 0.12997819 0.37688643 0.18463637 0.26961371
		 0.26976854 0.1844815 0.37704134 0.12982315 0.49595416 0.11098927 0.61486691 0.12982315
		 0.72213972 0.18448138 0.80727196 0.26961353 0.86193019 0.37688643;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  14.98413944 -68.80792236 2.13939214 15.063351631 -68.65246582 2.13939214
		 15.18671894 -68.52909851 2.13939214 15.34217548 -68.44989014 2.13939214 15.5144968 -68.42259979 2.13939214
		 15.68682194 -68.44989014 2.13939214 15.84227085 -68.52909851 2.13939214 15.96564579 -68.65246582 2.13939214
		 16.04485321 -68.80792236 2.13939214 16.072147369 -68.9802475 2.13939214 16.04485321 -69.15257263 2.13939214
		 15.96564579 -69.30802155 2.13939214 15.84227085 -69.43139648 2.13939214 15.68682194 -69.51060486 2.13939214
		 15.5144968 -69.5378952 2.13939214 15.34217548 -69.51060486 2.13939214 15.18671894 -69.43139648 2.13939214
		 15.063351631 -69.30802155 2.13939214 14.98413944 -69.15257263 2.13939214 14.95684719 -68.9802475 2.13939214;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 -19 -18 -17 -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 -20
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "Lf_Toe_ring1_guide" -p "FM_Cam_l_hi_feet_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 31.832180023193359 -8.964813232421875 2.1393921375274658 ;
	setAttr ".sp" -type "double3" 31.832180023193359 -8.964813232421875 2.1393921375274658 ;
createNode mesh -n "Lf_Toe_ring1_guideShape" -p "Lf_Toe_ring1_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193001 0.61471206 0.80727184 0.7219848 0.7221396 0.80711704 0.61486673 0.86177522
		 0.49595416 0.8806091 0.3770414 0.86177522 0.2697686 0.80711704 0.18463637 0.7219848
		 0.12997819 0.61471206 0.11114423 0.49579921 0.12997819 0.37688643 0.18463637 0.26961371
		 0.26976854 0.1844815 0.37704134 0.12982315 0.49595416 0.11098927 0.61486691 0.12982315
		 0.72213972 0.18448138 0.80727196 0.26961353 0.86193019 0.37688643;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  15.55276012 -69.89778137 2.13939214 15.63197231 -69.74232483 2.13939214
		 15.75533962 -69.61895752 2.13939214 15.91079617 -69.53974915 2.13939214 16.083118439 -69.51245117 2.13939214
		 16.25544357 -69.53974915 2.13939214 16.41089249 -69.61895752 2.13939214 16.53426743 -69.74232483 2.13939214
		 16.61347198 -69.89778137 2.13939214 16.64076996 -70.070098877 2.13939214 16.61347198 -70.24242401 2.13939214
		 16.53426743 -70.39787292 2.13939214 16.41089249 -70.52124786 2.13939214 16.25544357 -70.60045624 2.13939214
		 16.083118439 -70.62774658 2.13939214 15.91079617 -70.60045624 2.13939214 15.75533962 -70.52124786 2.13939214
		 15.63197231 -70.39787292 2.13939214 15.55276012 -70.24242401 2.13939214 15.52546787 -70.070098877 2.13939214;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 -19 -18 -17 -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 -20
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "Lf_Toe_pinky3_guide" -p "FM_Cam_l_hi_feet_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 29.273385047912598 -8.1829681396484375 2.1393921375274658 ;
	setAttr ".sp" -type "double3" 29.273385047912598 -8.1829681396484375 2.1393921375274658 ;
createNode mesh -n "Lf_Toe_pinky3_guideShape" -p "Lf_Toe_pinky3_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193001 0.61471206 0.80727184 0.7219848 0.7221396 0.80711704 0.61486673 0.86177522
		 0.49595416 0.8806091 0.3770414 0.86177522 0.2697686 0.80711704 0.18463637 0.7219848
		 0.12997819 0.61471206 0.11114423 0.49579921 0.12997819 0.37688643 0.18463637 0.26961371
		 0.26976854 0.1844815 0.37704134 0.12982315 0.49595416 0.11098927 0.61486691 0.12982315
		 0.72213972 0.18448138 0.80727196 0.26961353 0.86193019 0.37688643;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  12.9939661 -69.11592865 2.13939214 13.073178291 -68.96046448 2.13939214
		 13.1965456 -68.83709717 2.13939214 13.35200214 -68.75788879 2.13939214 13.52432346 -68.73060608 2.13939214
		 13.6966486 -68.75788879 2.13939214 13.85209751 -68.83709717 2.13939214 13.97547245 -68.96046448 2.13939214
		 14.054678917 -69.11592865 2.13939214 14.081974983 -69.28825378 2.13939214 14.054678917 -69.46057129 2.13939214
		 13.97547245 -69.61602783 2.13939214 13.85209751 -69.73939514 2.13939214 13.6966486 -69.81860352 2.13939214
		 13.52432346 -69.84590149 2.13939214 13.35200214 -69.81860352 2.13939214 13.1965456 -69.73939514 2.13939214
		 13.073178291 -69.61602783 2.13939214 12.9939661 -69.46057129 2.13939214 12.96667385 -69.28825378 2.13939214;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 -19 -18 -17 -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 -20
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "Lf_Toe_pinky2_guide" -p "FM_Cam_l_hi_feet_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 29.794619560241699 -9.2491302490234375 2.1393921375274658 ;
	setAttr ".sp" -type "double3" 29.794619560241699 -9.2491302490234375 2.1393921375274658 ;
createNode mesh -n "Lf_Toe_pinky2_guideShape" -p "Lf_Toe_pinky2_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193001 0.61471206 0.80727184 0.7219848 0.7221396 0.80711704 0.61486673 0.86177522
		 0.49595416 0.8806091 0.3770414 0.86177522 0.2697686 0.80711704 0.18463637 0.7219848
		 0.12997819 0.61471206 0.11114423 0.49579921 0.12997819 0.37688643 0.18463637 0.26961371
		 0.26976854 0.1844815 0.37704134 0.12982315 0.49595416 0.11098927 0.61486691 0.12982315
		 0.72213972 0.18448138 0.80727196 0.26961353 0.86193019 0.37688643;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  13.51520061 -70.18209839 2.13939214 13.5944128 -70.026634216 2.13939214
		 13.71778011 -69.90326691 2.13939214 13.87323666 -69.82405853 2.13939214 14.045557976 -69.79676819 2.13939214
		 14.21788311 -69.82405853 2.13939214 14.37333202 -69.90326691 2.13939214 14.49670696 -70.026634216 2.13939214
		 14.57591343 -70.18209839 2.13939214 14.6032095 -70.35441589 2.13939214 14.57591343 -70.5267334 2.13939214
		 14.49670696 -70.68218994 2.13939214 14.37333202 -70.80555725 2.13939214 14.21788311 -70.88476563 2.13939214
		 14.045557976 -70.9120636 2.13939214 13.87323666 -70.88476563 2.13939214 13.71778011 -70.80555725 2.13939214
		 13.5944128 -70.68218994 2.13939214 13.51520061 -70.5267334 2.13939214 13.48790836 -70.35441589 2.13939214;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 -19 -18 -17 -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 -20
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "Lf_Toe_pinky1_guide" -p "FM_Cam_l_hi_feet_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 30.363240242004395 -10.386367797851562 2.1393921375274658 ;
	setAttr ".sp" -type "double3" 30.363240242004395 -10.386367797851562 2.1393921375274658 ;
createNode mesh -n "Lf_Toe_pinky1_guideShape" -p "Lf_Toe_pinky1_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193001 0.61471206 0.80727184 0.7219848 0.7221396 0.80711704 0.61486673 0.86177522
		 0.49595416 0.8806091 0.3770414 0.86177522 0.2697686 0.80711704 0.18463637 0.7219848
		 0.12997819 0.61471206 0.11114423 0.49579921 0.12997819 0.37688643 0.18463637 0.26961371
		 0.26976854 0.1844815 0.37704134 0.12982315 0.49595416 0.11098927 0.61486691 0.12982315
		 0.72213972 0.18448138 0.80727196 0.26961353 0.86193019 0.37688643;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  14.083821297 -71.31933594 2.13939214 14.16303349 -71.16387939 2.13939214
		 14.28640079 -71.040512085 2.13939214 14.44185734 -70.96130371 2.13939214 14.61417866 -70.93400574 2.13939214
		 14.78650379 -70.96130371 2.13939214 14.94195271 -71.040512085 2.13939214 15.065327644 -71.16387939 2.13939214
		 15.14453411 -71.31933594 2.13939214 15.17183018 -71.49165344 2.13939214 15.14453411 -71.66397858 2.13939214
		 15.065327644 -71.81942749 2.13939214 14.94195271 -71.94280243 2.13939214 14.78650379 -72.022010803 2.13939214
		 14.61417866 -72.049301147 2.13939214 14.44185734 -72.022010803 2.13939214 14.28640079 -71.94280243 2.13939214
		 14.16303349 -71.81942749 2.13939214 14.083821297 -71.66397858 2.13939214 14.056529045 -71.49165344 2.13939214;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 -19 -18 -17 -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 -20
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_r_hi_feet_" -p "FM_Cam_FEET_gui_guides_grp";
	setAttr ".rp" -type "double3" 49.889011383056641 -7.1997222900390625 2.1393921375274658 ;
	setAttr ".sp" -type "double3" 49.889011383056641 -7.1997222900390625 2.1393921375274658 ;
createNode transform -n "Rt_Toe_thumb3_guide" -p "FM_Cam_r_hi_feet_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 45.802045822143555 -4.178924560546875 2.1393921375274658 ;
	setAttr ".sp" -type "double3" 45.802045822143555 -4.178924560546875 2.1393921375274658 ;
createNode mesh -n "Rt_Toe_thumb3_guideShape" -p "Rt_Toe_thumb3_guide";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193019 0.37688643 0.80727196 0.26961353 0.72213972 0.18448138 0.61486691 0.12982315
		 0.49595416 0.11098927 0.37704134 0.12982315 0.26976854 0.1844815 0.18463637 0.26961371
		 0.12997819 0.37688643 0.11114423 0.49579921 0.12997819 0.61471206 0.18463637 0.7219848
		 0.2697686 0.80711704 0.3770414 0.86177522 0.49595416 0.8806091 0.61486673 0.86177522
		 0.7221396 0.80711704 0.80727184 0.7219848 0.86193001 0.61471206;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  30.58334541 -65.1118927 2.13939214 30.50413322 -64.95642853 2.13939214
		 30.38076591 -64.83306122 2.13939214 30.22530937 -64.75385284 2.13939214 30.052988052 -64.7265625 2.13939214
		 29.88066292 -64.75385284 2.13939214 29.725214 -64.83306122 2.13939214 29.60183907 -64.95642853 2.13939214
		 29.52263069 -65.1118927 2.13939214 29.49533653 -65.28421021 2.13939214 29.52263069 -65.45653534 2.13939214
		 29.60183907 -65.61198425 2.13939214 29.725214 -65.73535919 2.13939214 29.88066292 -65.81456757 2.13939214
		 30.052988052 -65.84185791 2.13939214 30.22530937 -65.81456757 2.13939214 30.38076591 -65.73535919 2.13939214
		 30.50413322 -65.61198425 2.13939214 30.58334541 -65.45653534 2.13939214 30.61063576 -65.28421021 2.13939214;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 19 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "Rt_Toe_thumb2_guide" -p "FM_Cam_r_hi_feet_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 45.707277297973633 -6.1217117309570313 2.1393921375274658 ;
	setAttr ".sp" -type "double3" 45.707277297973633 -6.1217117309570313 2.1393921375274658 ;
createNode mesh -n "Rt_Toe_thumb2_guideShape" -p "Rt_Toe_thumb2_guide";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193019 0.37688643 0.80727196 0.26961353 0.72213972 0.18448138 0.61486691 0.12982315
		 0.49595416 0.11098927 0.37704134 0.12982315 0.26976854 0.1844815 0.18463637 0.26961371
		 0.12997819 0.37688643 0.11114423 0.49579921 0.12997819 0.61471206 0.18463637 0.7219848
		 0.2697686 0.80711704 0.3770414 0.86177522 0.49595416 0.8806091 0.61486673 0.86177522
		 0.7221396 0.80711704 0.80727184 0.7219848 0.86193001 0.61471206;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  30.48857689 -67.054679871 2.13939214 30.4093647 -66.8992157 2.13939214
		 30.28599739 -66.77584839 2.13939214 30.13054085 -66.69664001 2.13939214 29.95821953 -66.66934967 2.13939214
		 29.78589439 -66.69664001 2.13939214 29.63044548 -66.77584839 2.13939214 29.50707054 -66.8992157 2.13939214
		 29.42786217 -67.054679871 2.13939214 29.40056801 -67.22699738 2.13939214 29.42786217 -67.39932251 2.13939214
		 29.50707054 -67.55477142 2.13939214 29.63044548 -67.67814636 2.13939214 29.78589439 -67.75735474 2.13939214
		 29.95821953 -67.78464508 2.13939214 30.13054085 -67.75735474 2.13939214 30.28599739 -67.67814636 2.13939214
		 30.4093647 -67.55477142 2.13939214 30.48857689 -67.39932251 2.13939214 30.51586723 -67.22699738 2.13939214;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 19 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "Rt_Toe_thumb1_guide" -p "FM_Cam_r_hi_feet_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 45.754659652709961 -7.6854248046875 2.1393921375274658 ;
	setAttr ".sp" -type "double3" 45.754659652709961 -7.6854248046875 2.1393921375274658 ;
createNode mesh -n "Rt_Toe_thumb1_guideShape" -p "Rt_Toe_thumb1_guide";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193019 0.37688643 0.80727196 0.26961353 0.72213972 0.18448138 0.61486691 0.12982315
		 0.49595416 0.11098927 0.37704134 0.12982315 0.26976854 0.1844815 0.18463637 0.26961371
		 0.12997819 0.37688643 0.11114423 0.49579921 0.12997819 0.61471206 0.18463637 0.7219848
		 0.2697686 0.80711704 0.3770414 0.86177522 0.49595416 0.8806091 0.61486673 0.86177522
		 0.7221396 0.80711704 0.80727184 0.7219848 0.86193001 0.61471206;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  30.53595924 -68.61838531 2.13939214 30.45674706 -68.46292114 2.13939214
		 30.33337975 -68.33955383 2.13939214 30.1779232 -68.26034546 2.13939214 30.0056018829 -68.23306274 2.13939214
		 29.83327675 -68.26034546 2.13939214 29.67782784 -68.33955383 2.13939214 29.5544529 -68.46292114 2.13939214
		 29.47524452 -68.61838531 2.13939214 29.44795036 -68.79071045 2.13939214 29.47524452 -68.96302795 2.13939214
		 29.5544529 -69.1184845 2.13939214 29.67782784 -69.24185181 2.13939214 29.83327675 -69.32106018 2.13939214
		 30.0056018829 -69.34835815 2.13939214 30.1779232 -69.32106018 2.13939214 30.33337975 -69.24185181 2.13939214
		 30.45674706 -69.1184845 2.13939214 30.53595924 -68.96302795 2.13939214 30.56324959 -68.79071045 2.13939214;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 19 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "Rt_Toe_index3_guide" -p "FM_Cam_r_hi_feet_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 48.810997009277344 -4.0130767822265625 2.1393921375274658 ;
	setAttr ".sp" -type "double3" 48.810997009277344 -4.0130767822265625 2.1393921375274658 ;
createNode mesh -n "Rt_Toe_index3_guideShape" -p "Rt_Toe_index3_guide";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193019 0.37688643 0.80727196 0.26961353 0.72213972 0.18448138 0.61486691 0.12982315
		 0.49595416 0.11098927 0.37704134 0.12982315 0.26976854 0.1844815 0.18463637 0.26961371
		 0.12997819 0.37688643 0.11114423 0.49579921 0.12997819 0.61471206 0.18463637 0.7219848
		 0.2697686 0.80711704 0.3770414 0.86177522 0.49595416 0.8806091 0.61486673 0.86177522
		 0.7221396 0.80711704 0.80727184 0.7219848 0.86193001 0.61471206;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  33.59230042 -64.94604492 2.13939214 33.51308441 -64.79058075 2.13939214
		 33.3897171 -64.66721344 2.13939214 33.23426056 -64.58800507 2.13939214 33.061935425 -64.56071472 2.13939214
		 32.88961792 -64.58800507 2.13939214 32.73416138 -64.66721344 2.13939214 32.61079407 -64.79058075 2.13939214
		 32.53158569 -64.94604492 2.13939214 32.50428772 -65.11836243 2.13939214 32.53158569 -65.29068756 2.13939214
		 32.61079407 -65.44613647 2.13939214 32.73416138 -65.56951141 2.13939214 32.88961792 -65.64871979 2.13939214
		 33.061935425 -65.67601013 2.13939214 33.23426056 -65.64871979 2.13939214 33.3897171 -65.56951141 2.13939214
		 33.51308441 -65.44613647 2.13939214 33.59230042 -65.29068756 2.13939214 33.61958313 -65.11836243 2.13939214;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 19 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "Rt_Toe_index2_guide" -p "FM_Cam_r_hi_feet_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 48.668846130371094 -5.363555908203125 2.1393921375274658 ;
	setAttr ".sp" -type "double3" 48.668846130371094 -5.363555908203125 2.1393921375274658 ;
createNode mesh -n "Rt_Toe_index2_guideShape" -p "Rt_Toe_index2_guide";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193019 0.37688643 0.80727196 0.26961353 0.72213972 0.18448138 0.61486691 0.12982315
		 0.49595416 0.11098927 0.37704134 0.12982315 0.26976854 0.1844815 0.18463637 0.26961371
		 0.12997819 0.37688643 0.11114423 0.49579921 0.12997819 0.61471206 0.18463637 0.7219848
		 0.2697686 0.80711704 0.3770414 0.86177522 0.49595416 0.8806091 0.61486673 0.86177522
		 0.7221396 0.80711704 0.80727184 0.7219848 0.86193001 0.61471206;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  33.45014191 -66.29651642 2.13939214 33.3709259 -66.14105225 2.13939214
		 33.24755859 -66.017684937 2.13939214 33.092102051 -65.93847656 2.13939214 32.91978455 -65.91119385 2.13939214
		 32.74745941 -65.93847656 2.13939214 32.5920105 -66.017684937 2.13939214 32.46863556 -66.14105225 2.13939214
		 32.38942719 -66.29651642 2.13939214 32.36213684 -66.46884155 2.13939214 32.38942719 -66.64115906 2.13939214
		 32.46863556 -66.7966156 2.13939214 32.5920105 -66.91998291 2.13939214 32.74745941 -66.99919128 2.13939214
		 32.91978455 -67.026489258 2.13939214 33.092102051 -66.99919128 2.13939214 33.24755859 -66.91998291 2.13939214
		 33.3709259 -66.7966156 2.13939214 33.45014191 -66.64115906 2.13939214 33.47743225 -66.46884155 2.13939214;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 19 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "Rt_Toe_index1_guide" -p "FM_Cam_r_hi_feet_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 48.502998352050781 -6.7140274047851563 2.1393921375274658 ;
	setAttr ".sp" -type "double3" 48.502998352050781 -6.7140274047851563 2.1393921375274658 ;
createNode mesh -n "Rt_Toe_index1_guideShape" -p "Rt_Toe_index1_guide";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193019 0.37688643 0.80727196 0.26961353 0.72213972 0.18448138 0.61486691 0.12982315
		 0.49595416 0.11098927 0.37704134 0.12982315 0.26976854 0.1844815 0.18463637 0.26961371
		 0.12997819 0.37688643 0.11114423 0.49579921 0.12997819 0.61471206 0.18463637 0.7219848
		 0.2697686 0.80711704 0.3770414 0.86177522 0.49595416 0.8806091 0.61486673 0.86177522
		 0.7221396 0.80711704 0.80727184 0.7219848 0.86193001 0.61471206;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  33.28429413 -67.64698792 2.13939214 33.20507813 -67.49153137 2.13939214
		 33.081710815 -67.36816406 2.13939214 32.92625427 -67.28895569 2.13939214 32.75393677 -67.26166534 2.13939214
		 32.58161163 -67.28895569 2.13939214 32.42616272 -67.36816406 2.13939214 32.30278778 -67.49153137 2.13939214
		 32.22357941 -67.64698792 2.13939214 32.19628906 -67.81931305 2.13939214 32.22357941 -67.99163818 2.13939214
		 32.30278778 -68.1470871 2.13939214 32.42616272 -68.27046204 2.13939214 32.58161163 -68.34967041 2.13939214
		 32.75393677 -68.37696075 2.13939214 32.92625427 -68.34967041 2.13939214 33.081710815 -68.27046204 2.13939214
		 33.20507813 -68.1470871 2.13939214 33.28429413 -67.99163818 2.13939214 33.31158447 -67.81931305 2.13939214;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 19 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "Rt_Toe_mid3_guide" -p "FM_Cam_r_hi_feet_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 51.180255889892578 -5.1977081298828125 2.1393921375274658 ;
	setAttr ".sp" -type "double3" 51.180255889892578 -5.1977081298828125 2.1393921375274658 ;
createNode mesh -n "Rt_Toe_mid3_guideShape" -p "Rt_Toe_mid3_guide";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193019 0.37688643 0.80727196 0.26961353 0.72213972 0.18448138 0.61486691 0.12982315
		 0.49595416 0.11098927 0.37704134 0.12982315 0.26976854 0.1844815 0.18463637 0.26961371
		 0.12997819 0.37688643 0.11114423 0.49579921 0.12997819 0.61471206 0.18463637 0.7219848
		 0.2697686 0.80711704 0.3770414 0.86177522 0.49595416 0.8806091 0.61486673 0.86177522
		 0.7221396 0.80711704 0.80727184 0.7219848 0.86193001 0.61471206;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  35.96154785 -66.13066864 2.13939214 35.88233948 -65.97520447 2.13939214
		 35.75897217 -65.85183716 2.13939214 35.60351563 -65.77262878 2.13939214 35.43119812 -65.74534607 2.13939214
		 35.25886536 -65.77262878 2.13939214 35.10342407 -65.85183716 2.13939214 34.9800415 -65.97520447 2.13939214
		 34.90083313 -66.13066864 2.13939214 34.87354279 -66.30299377 2.13939214 34.90083313 -66.47531128 2.13939214
		 34.9800415 -66.63076782 2.13939214 35.10342407 -66.75413513 2.13939214 35.25886536 -66.83334351 2.13939214
		 35.43119812 -66.86064148 2.13939214 35.60351563 -66.83334351 2.13939214 35.75897217 -66.75413513 2.13939214
		 35.88233948 -66.63076782 2.13939214 35.96154785 -66.47531128 2.13939214 35.98884583 -66.30299377 2.13939214;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 19 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "Rt_Toe_mid2_guide" -p "FM_Cam_r_hi_feet_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 50.659019470214844 -6.429718017578125 2.1393921375274658 ;
	setAttr ".sp" -type "double3" 50.659019470214844 -6.429718017578125 2.1393921375274658 ;
createNode mesh -n "Rt_Toe_mid2_guideShape" -p "Rt_Toe_mid2_guide";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193019 0.37688643 0.80727196 0.26961353 0.72213972 0.18448138 0.61486691 0.12982315
		 0.49595416 0.11098927 0.37704134 0.12982315 0.26976854 0.1844815 0.18463637 0.26961371
		 0.12997819 0.37688643 0.11114423 0.49579921 0.12997819 0.61471206 0.18463637 0.7219848
		 0.2697686 0.80711704 0.3770414 0.86177522 0.49595416 0.8806091 0.61486673 0.86177522
		 0.7221396 0.80711704 0.80727184 0.7219848 0.86193001 0.61471206;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  35.44031525 -67.36267853 2.13939214 35.36109924 -67.20722198 2.13939214
		 35.23773193 -67.083854675 2.13939214 35.082275391 -67.0046463013 2.13939214 34.90995789 -66.97735596 2.13939214
		 34.73763275 -67.0046463013 2.13939214 34.58218384 -67.083854675 2.13939214 34.4588089 -67.20722198 2.13939214
		 34.37960052 -67.36267853 2.13939214 34.35231018 -67.53500366 2.13939214 34.37960052 -67.70732117 2.13939214
		 34.4588089 -67.86277771 2.13939214 34.58218384 -67.98614502 2.13939214 34.73763275 -68.065353394 2.13939214
		 34.90995789 -68.092651367 2.13939214 35.082275391 -68.065353394 2.13939214 35.23773193 -67.98614502 2.13939214
		 35.36109924 -67.86277771 2.13939214 35.44031525 -67.70732117 2.13939214 35.46760559 -67.53500366 2.13939214;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 19 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "Rt_Toe_mid1_guide" -p "FM_Cam_r_hi_feet_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 50.256244659423828 -7.7801971435546875 2.1393921375274658 ;
	setAttr ".sp" -type "double3" 50.256244659423828 -7.7801971435546875 2.1393921375274658 ;
createNode mesh -n "Rt_Toe_mid1_guideShape" -p "Rt_Toe_mid1_guide";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193019 0.37688643 0.80727196 0.26961353 0.72213972 0.18448138 0.61486691 0.12982315
		 0.49595416 0.11098927 0.37704134 0.12982315 0.26976854 0.1844815 0.18463637 0.26961371
		 0.12997819 0.37688643 0.11114423 0.49579921 0.12997819 0.61471206 0.18463637 0.7219848
		 0.2697686 0.80711704 0.3770414 0.86177522 0.49595416 0.8806091 0.61486673 0.86177522
		 0.7221396 0.80711704 0.80727184 0.7219848 0.86193001 0.61471206;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  35.037536621 -68.71315765 2.13939214 34.95832825 -68.55769348 2.13939214
		 34.83496094 -68.43432617 2.13939214 34.67950439 -68.3551178 2.13939214 34.50718689 -68.32783508 2.13939214
		 34.33485413 -68.3551178 2.13939214 34.17941284 -68.43432617 2.13939214 34.056030273 -68.55769348 2.13939214
		 33.9768219 -68.71315765 2.13939214 33.94953156 -68.88548279 2.13939214 33.9768219 -69.057800293 2.13939214
		 34.056030273 -69.21325684 2.13939214 34.17941284 -69.33662415 2.13939214 34.33485413 -69.41583252 2.13939214
		 34.50718689 -69.44313049 2.13939214 34.67950439 -69.41583252 2.13939214 34.83496094 -69.33662415 2.13939214
		 34.95832825 -69.21325684 2.13939214 35.037536621 -69.057800293 2.13939214 35.064834595 -68.88548279 2.13939214;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 19 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "Rt_Toe_ring3_guide" -p "FM_Cam_r_hi_feet_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 52.696575164794922 -6.8087921142578125 2.1393921375274658 ;
	setAttr ".sp" -type "double3" 52.696575164794922 -6.8087921142578125 2.1393921375274658 ;
createNode mesh -n "Rt_Toe_ring3_guideShape" -p "Rt_Toe_ring3_guide";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193019 0.37688643 0.80727196 0.26961353 0.72213972 0.18448138 0.61486691 0.12982315
		 0.49595416 0.11098927 0.37704134 0.12982315 0.26976854 0.1844815 0.18463637 0.26961371
		 0.12997819 0.37688643 0.11114423 0.49579921 0.12997819 0.61471206 0.18463637 0.7219848
		 0.2697686 0.80711704 0.3770414 0.86177522 0.49595416 0.8806091 0.61486673 0.86177522
		 0.7221396 0.80711704 0.80727184 0.7219848 0.86193001 0.61471206;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  37.47787476 -67.74176025 2.13939214 37.39865875 -67.58630371 2.13939214
		 37.27529144 -67.4629364 2.13939214 37.1198349 -67.38372803 2.13939214 36.9475174 -67.35643005 2.13939214
		 36.77519226 -67.38372803 2.13939214 36.61974335 -67.4629364 2.13939214 36.49636841 -67.58630371 2.13939214
		 36.41716003 -67.74176025 2.13939214 36.38986206 -67.91407776 2.13939214 36.41716003 -68.086402893 2.13939214
		 36.49636841 -68.24185181 2.13939214 36.61974335 -68.36522675 2.13939214 36.77519226 -68.44443512 2.13939214
		 36.9475174 -68.47172546 2.13939214 37.1198349 -68.44443512 2.13939214 37.27529144 -68.36522675 2.13939214
		 37.39865875 -68.24185181 2.13939214 37.47787476 -68.086402893 2.13939214 37.5051651 -67.91407776 2.13939214;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 19 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "Rt_Toe_ring2_guide" -p "FM_Cam_r_hi_feet_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 52.080570220947266 -7.8749618530273437 2.1393921375274658 ;
	setAttr ".sp" -type "double3" 52.080570220947266 -7.8749618530273437 2.1393921375274658 ;
createNode mesh -n "Rt_Toe_ring2_guideShape" -p "Rt_Toe_ring2_guide";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193019 0.37688643 0.80727196 0.26961353 0.72213972 0.18448138 0.61486691 0.12982315
		 0.49595416 0.11098927 0.37704134 0.12982315 0.26976854 0.1844815 0.18463637 0.26961371
		 0.12997819 0.37688643 0.11114423 0.49579921 0.12997819 0.61471206 0.18463637 0.7219848
		 0.2697686 0.80711704 0.3770414 0.86177522 0.49595416 0.8806091 0.61486673 0.86177522
		 0.7221396 0.80711704 0.80727184 0.7219848 0.86193001 0.61471206;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  36.86186218 -68.80792236 2.13939214 36.78265381 -68.65246582 2.13939214
		 36.6592865 -68.52909851 2.13939214 36.50382996 -68.44989014 2.13939214 36.33151245 -68.42259979 2.13939214
		 36.15917969 -68.44989014 2.13939214 36.0037384033 -68.52909851 2.13939214 35.88035583 -68.65246582 2.13939214
		 35.80115509 -68.80792236 2.13939214 35.77385712 -68.9802475 2.13939214 35.80115509 -69.15257263 2.13939214
		 35.88035583 -69.30802155 2.13939214 36.0037384033 -69.43139648 2.13939214 36.15917969 -69.51060486 2.13939214
		 36.33151245 -69.5378952 2.13939214 36.50382996 -69.51060486 2.13939214 36.6592865 -69.43139648 2.13939214
		 36.78265381 -69.30802155 2.13939214 36.86186218 -69.15257263 2.13939214 36.88916016 -68.9802475 2.13939214;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 19 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "Rt_Toe_ring1_guide" -p "FM_Cam_r_hi_feet_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 51.511947631835938 -8.964813232421875 2.1393921375274658 ;
	setAttr ".sp" -type "double3" 51.511947631835938 -8.964813232421875 2.1393921375274658 ;
createNode mesh -n "Rt_Toe_ring1_guideShape" -p "Rt_Toe_ring1_guide";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193019 0.37688643 0.80727196 0.26961353 0.72213972 0.18448138 0.61486691 0.12982315
		 0.49595416 0.11098927 0.37704134 0.12982315 0.26976854 0.1844815 0.18463637 0.26961371
		 0.12997819 0.37688643 0.11114423 0.49579921 0.12997819 0.61471206 0.18463637 0.7219848
		 0.2697686 0.80711704 0.3770414 0.86177522 0.49595416 0.8806091 0.61486673 0.86177522
		 0.7221396 0.80711704 0.80727184 0.7219848 0.86193001 0.61471206;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  36.29324341 -69.89778137 2.13939214 36.21403503 -69.74232483 2.13939214
		 36.090667725 -69.61895752 2.13939214 35.93521118 -69.53974915 2.13939214 35.76288605 -69.51245117 2.13939214
		 35.59056091 -69.53974915 2.13939214 35.435112 -69.61895752 2.13939214 35.31173706 -69.74232483 2.13939214
		 35.23252869 -69.89778137 2.13939214 35.20523071 -70.070098877 2.13939214 35.23252869 -70.24242401 2.13939214
		 35.31173706 -70.39787292 2.13939214 35.435112 -70.52124786 2.13939214 35.59056091 -70.60045624 2.13939214
		 35.76288605 -70.62774658 2.13939214 35.93521118 -70.60045624 2.13939214 36.090667725 -70.52124786 2.13939214
		 36.21403503 -70.39787292 2.13939214 36.29324341 -70.24242401 2.13939214 36.32054138 -70.070098877 2.13939214;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 19 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "Rt_Toe_pinky3_guide" -p "FM_Cam_r_hi_feet_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 54.070743560791016 -8.1829681396484375 2.1393921375274658 ;
	setAttr ".sp" -type "double3" 54.070743560791016 -8.1829681396484375 2.1393921375274658 ;
createNode mesh -n "Rt_Toe_pinky3_guideShape" -p "Rt_Toe_pinky3_guide";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193019 0.37688643 0.80727196 0.26961353 0.72213972 0.18448138 0.61486691 0.12982315
		 0.49595416 0.11098927 0.37704134 0.12982315 0.26976854 0.1844815 0.18463637 0.26961371
		 0.12997819 0.37688643 0.11114423 0.49579921 0.12997819 0.61471206 0.18463637 0.7219848
		 0.2697686 0.80711704 0.3770414 0.86177522 0.49595416 0.8806091 0.61486673 0.86177522
		 0.7221396 0.80711704 0.80727184 0.7219848 0.86193001 0.61471206;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  38.85203552 -69.11592865 2.13939214 38.77282715 -68.96046448 2.13939214
		 38.64945984 -68.83709717 2.13939214 38.4940033 -68.75788879 2.13939214 38.32168579 -68.73060608 2.13939214
		 38.14935303 -68.75788879 2.13939214 37.99391174 -68.83709717 2.13939214 37.87052917 -68.96046448 2.13939214
		 37.79132843 -69.11592865 2.13939214 37.76403046 -69.28825378 2.13939214 37.79132843 -69.46057129 2.13939214
		 37.87052917 -69.61602783 2.13939214 37.99391174 -69.73939514 2.13939214 38.14935303 -69.81860352 2.13939214
		 38.32168579 -69.84590149 2.13939214 38.4940033 -69.81860352 2.13939214 38.64945984 -69.73939514 2.13939214
		 38.77282715 -69.61602783 2.13939214 38.85203552 -69.46057129 2.13939214 38.8793335 -69.28825378 2.13939214;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 19 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "Rt_Toe_pinky2_guide" -p "FM_Cam_r_hi_feet_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 53.549507141113281 -9.2491302490234375 2.1393921375274658 ;
	setAttr ".sp" -type "double3" 53.549507141113281 -9.2491302490234375 2.1393921375274658 ;
createNode mesh -n "Rt_Toe_pinky2_guideShape" -p "Rt_Toe_pinky2_guide";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193019 0.37688643 0.80727196 0.26961353 0.72213972 0.18448138 0.61486691 0.12982315
		 0.49595416 0.11098927 0.37704134 0.12982315 0.26976854 0.1844815 0.18463637 0.26961371
		 0.12997819 0.37688643 0.11114423 0.49579921 0.12997819 0.61471206 0.18463637 0.7219848
		 0.2697686 0.80711704 0.3770414 0.86177522 0.49595416 0.8806091 0.61486673 0.86177522
		 0.7221396 0.80711704 0.80727184 0.7219848 0.86193001 0.61471206;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  38.33080292 -70.18209839 2.13939214 38.25159454 -70.026634216 2.13939214
		 38.12822723 -69.90326691 2.13939214 37.97277069 -69.82405853 2.13939214 37.80044556 -69.79676819 2.13939214
		 37.62812042 -69.82405853 2.13939214 37.47267151 -69.90326691 2.13939214 37.34929657 -70.026634216 2.13939214
		 37.27009583 -70.18209839 2.13939214 37.24279785 -70.35441589 2.13939214 37.27009583 -70.5267334 2.13939214
		 37.34929657 -70.68218994 2.13939214 37.47267151 -70.80555725 2.13939214 37.62812042 -70.88476563 2.13939214
		 37.80044556 -70.9120636 2.13939214 37.97277069 -70.88476563 2.13939214 38.12822723 -70.80555725 2.13939214
		 38.25159454 -70.68218994 2.13939214 38.33080292 -70.5267334 2.13939214 38.35809326 -70.35441589 2.13939214;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 19 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "Rt_Toe_pinky1_guide" -p "FM_Cam_r_hi_feet_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 52.980888366699219 -10.386367797851562 2.1393921375274658 ;
	setAttr ".sp" -type "double3" 52.980888366699219 -10.386367797851562 2.1393921375274658 ;
createNode mesh -n "Rt_Toe_pinky1_guideShape" -p "Rt_Toe_pinky1_guide";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193019 0.37688643 0.80727196 0.26961353 0.72213972 0.18448138 0.61486691 0.12982315
		 0.49595416 0.11098927 0.37704134 0.12982315 0.26976854 0.1844815 0.18463637 0.26961371
		 0.12997819 0.37688643 0.11114423 0.49579921 0.12997819 0.61471206 0.18463637 0.7219848
		 0.2697686 0.80711704 0.3770414 0.86177522 0.49595416 0.8806091 0.61486673 0.86177522
		 0.7221396 0.80711704 0.80727184 0.7219848 0.86193001 0.61471206;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  37.76218414 -71.31933594 2.13939214 37.68296814 -71.16387939 2.13939214
		 37.55960083 -71.040512085 2.13939214 37.40414429 -70.96130371 2.13939214 37.23182678 -70.93400574 2.13939214
		 37.059501648 -70.96130371 2.13939214 36.90405273 -71.040512085 2.13939214 36.7806778 -71.16387939 2.13939214
		 36.70146942 -71.31933594 2.13939214 36.67417908 -71.49165344 2.13939214 36.70146942 -71.66397858 2.13939214
		 36.7806778 -71.81942749 2.13939214 36.90405273 -71.94280243 2.13939214 37.059501648 -72.022010803 2.13939214
		 37.23182678 -72.049301147 2.13939214 37.40414429 -72.022010803 2.13939214 37.55960083 -71.94280243 2.13939214
		 37.68296814 -71.81942749 2.13939214 37.76218414 -71.66397858 2.13939214 37.78947449 -71.49165344 2.13939214;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 19 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_c_feet_letter_" -p "FM_Cam_FEET_gui_guides_grp";
createNode transform -n "FM_Cam_r_feet_letter_" -p "FM_Cam_c_feet_letter_";
	setAttr ".t" -type "double3" -2.8605762924782638 -0.38296284901079347 0 ;
	setAttr ".s" -type "double3" 1.5 1.5 1.5 ;
	setAttr ".rp" -type "double3" 55.158927917480469 -1.9728488922119141 1.9510667324066162 ;
	setAttr ".sp" -type "double3" 55.158927917480469 -1.9728488922119141 1.9510667324066162 ;
createNode mesh -n "FM_Cam_r_feet_letter_Shape" -p "FM_Cam_r_feet_letter_";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 101 ".uvst[0].uvsp[0:100]" -type "float2" 1 0.038455497 0.54151595
		 0.46987823 0 0.99984294 0.3590056 1 0.80872452 0.73451346 1.666336e-016 0.9613874
		 1.666336e-016 0.038455497 0.1540312 0.77917445 0.031440504 0.96170139 0.15405272
		 0.7983349 0.15405536 0.20055065 0.031642232 0.038119152 1.666336e-016 0 0.4235858
		 0 0.4235858 0.038455497 0.26955459 0.46146595 0.39080861 0.038099431 0.26953366 0.28134853
		 0.40373051 0.46146595 0.32551831 0.45943969 0.73706347 0 1 0 0.26955459 0.92293191
		 0.26955459 0.49992147 0.67871976 0.73470306 0.41893503 0.96154845 0.32166064 0.49932066
		 0.68926436 0.52494109 0.1540312 0.52494109 0.53310204 0.52494109 0.26955459 0.52494109
		 0.5 0.32819051 0.5 0.51576537 0.15384752 0.17541298 0.26964888 0.17541298 0.2 0 0.14547107
		 0.1 0.1 0.04978269 0.1 0 0.30000001 0 0.30000001 0.063421443 0.27812865 0.1 0.40000001
		 0 0.40000001 0.038167618 0.1540312 0.30000001 0.1540312 0.40000001 0.26953429 0.30000001
		 0.30000001 0.45981407 0.30000001 0.49955657 0.2695488 0.40000001 0.4481295 0.40000001
		 0.40000001 0.46132591 0.40000001 0.50188506 0.75738466 0.17541298 0.61035651 0.17541298
		 0.69999999 0.05131061 0.66482997 0.1 0.80000001 0.12881656 0.80000001 0 0.83133042
		 0.1 0.89999998 0.059741359 0.89999998 0 0.69999999 0.25237489 0.66529793 0.30000001
		 0.52036297 0.30000001 0.60000002 0.18975057 0.5924328 0.40000001 0.60000002 0.38961479
		 0.60000002 0.4850809 0.5 0.99569982 0.5 0.95174384 0.1540312 0.69999999 0.26955459
		 0.69999999 0.1540312 0.60000002 0.26955459 0.60000002 0.2 0.99984294 0.15405221 0.80000001
		 0.14536174 0.89999998 0.1 0.99984294 0.1 0.95057118 0.26955459 0.80000001 0.30000001
		 0.99985504 0.30000001 0.93526042 0.26955459 0.89999998 0.40000001 0.99978334 0.40000001
		 0.96082532 0.80643284 0.69999999 0.67644393 0.69999999 0.69999999 0.53190386 0.63792074
		 0.60000002 0.60000002 0.55925995 0.80000001 0.6681686 0.76843858 0.60000002 0.69999999
		 0.93739253 0.67002332 0.80000001 0.60438091 0.89999998 0.60000002 0.98126453 0.60000002
		 0.90360987 0.80030262 0.80000001 0.80000001 0.80111051 0.74274004 0.89999998;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 101 ".pt[0:100]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 101 ".vt[0:100]"  40.28850174 -63.89032364 1.95106673 39.4828186 -63.13116837 1.95106673
		 38.53123093 -62.19861603 1.95106673 39.16210175 -62.19827652 1.95106673 39.95251083 -62.66549683 1.95106673
		 38.53123093 -62.26628113 1.95106673 38.53123093 -63.89032364 1.95106673 38.8019104 -62.58691025 1.95106673
		 38.58647919 -62.26572418 1.95106673 38.80197144 -62.55319977 1.95106673 38.80194855 -63.60508728 1.95106673
		 38.58683777 -63.89082336 1.95106673 38.53123093 -63.95799255 1.95106673 39.27558899 -63.95799255 1.95106673
		 39.27558899 -63.89032364 1.95106673 39.0049133301 -63.14596939 1.95106673 39.21798706 -63.89095306 1.95106673
		 39.0048751831 -63.46291351 1.95106673 39.24069595 -63.14596939 1.95106673 39.10325623 -63.14953613 1.95106673
		 39.82645035 -63.95799255 1.95106673 40.28850174 -63.95799255 1.95106673 39.0049133301 -62.33394623 1.95106673
		 39.0049133301 -63.078304291 1.95106673 39.72392273 -62.66516495 1.95106673 39.26741028 -62.26593781 1.95106673
		 39.096481323 -63.079086304 1.95106673 39.74245834 -63.03427887 1.95106673 38.80192566 -63.034275055 1.95106673
		 39.46803284 -63.034275055 1.95106673 39.0049133301 -63.034275055 1.95106673 39.40986633 -63.38048935 1.95106673
		 39.40986633 -63.050422668 1.95106673 38.80158615 -63.64932251 1.95106673 39.0050811768 -63.64932251 1.95106673
		 38.88268661 -63.95799255 1.95106673 38.7868576 -63.78202438 1.95106673 38.70719147 -63.87090683 1.95106673
		 38.70696259 -63.95799255 1.95106673 39.058414459 -63.95799255 1.95106673 39.058414459 -63.84639359 1.95106673
		 39.019668579 -63.78211212 1.95106673 39.23413849 -63.95799255 1.95106673 39.23413849 -63.89085007 1.95106673
		 38.80178833 -63.43009949 1.95106673 38.80184174 -63.25412369 1.95106673 39.0048751831 -63.43009949 1.95106673
		 39.058414459 -63.14887619 1.95106673 39.058414459 -63.078624725 1.95106673 39.004901886 -63.25412369 1.95106673
		 39.31871796 -63.25412369 1.95106673 39.23413849 -63.14621353 1.95106673 39.23413849 -63.074848175 1.95106673
		 39.86198425 -63.64947128 1.95106673 39.6037941 -63.64932251 1.95106673 39.76131821 -63.86770248 1.95106673
		 39.6995163 -63.7820282 1.95106673 39.93714523 -63.73121643 1.95106673 39.93704987 -63.95799255 1.95106673
		 39.99217987 -63.78192902 1.95106673 40.11280441 -63.85278702 1.95106673 40.1127739 -63.95799255 1.95106673
		 39.76179123 -63.51356125 1.95106673 39.70053864 -63.4299469 1.95106673 39.44564819 -63.43009949 1.95106673
		 39.58559418 -63.62409592 1.95106673 39.57229614 -63.25412369 1.95106673 39.58559418 -63.27240372 1.95106673
		 39.58559036 -63.10441208 1.95106673 39.40988922 -62.20560455 1.95106673 39.40982437 -62.28342056 1.95106673
		 38.80183029 -62.72623062 1.95106673 39.0049133301 -62.72623062 1.95106673 38.80187988 -62.90219498 1.95106673
		 39.0049133301 -62.90219498 1.95106673 38.88268661 -62.19860077 1.95106673 38.80198669 -62.55026627 1.95106673
		 38.78609467 -62.37446976 1.95106673 38.70696259 -62.19861984 1.95106673 38.70694733 -62.28533936 1.95106673
		 39.0049133301 -62.55026627 1.95106673 39.058414459 -62.19850922 1.95106673 39.058414459 -62.31225967 1.95106673
		 39.0049133301 -62.37430191 1.95106673 39.2341423 -62.1984787 1.95106673 39.23413849 -62.26726913 1.95106673
		 39.94837952 -62.72623444 1.95106673 39.72003555 -62.72624207 1.95106673 39.76132202 -63.022026062 1.95106673
		 39.65222931 -62.90219498 1.95106673 39.58564377 -62.97394943 1.95106673 39.93700027 -62.78223038 1.95106673
		 39.8815918 -62.90219879 1.95106673 39.76123428 -62.30862808 1.95106673 39.70816422 -62.55039978 1.95106673
		 39.5935936 -62.37394714 1.95106673 39.58547211 -62.23179626 1.95106673 39.58587646 -62.36759186 1.95106673
		 39.93743134 -62.55030441 1.95106673 39.93689728 -62.5483551 1.95106673 39.83673477 -62.37400436 1.95106673;
	setAttr -s 101 ".ed[0:100]"  98 99 0 53 62 0 51 18 0 18 50 0 32 52 0 42 13 0
		 13 14 0 14 43 0 33 36 0 36 37 0 38 35 0 37 11 0 11 6 0 6 12 0 12 38 0 41 34 0 35 39 0
		 40 41 0 39 42 0 43 16 0 16 40 0 28 45 0 44 10 0 10 33 0 45 44 0 34 17 0 17 46 0 49 15 0
		 15 47 0 48 23 0 23 30 0 46 49 0 50 31 0 47 19 0 19 51 0 52 26 0 26 48 0 59 57 0 54 56 0
		 56 55 0 57 53 0 55 20 0 20 58 0 0 60 0 61 21 0 21 0 0 60 59 0 58 61 0 68 27 0 62 63 0
		 65 54 0 64 65 0 63 67 0 67 66 0 31 64 0 66 1 0 1 68 0 29 32 0 69 84 0 85 25 0 25 70 0
		 74 72 0 71 73 0 73 28 0 30 74 0 75 78 0 79 77 0 76 9 0 9 7 0 7 71 0 77 76 0 78 2 0
		 2 5 0 5 8 0 8 79 0 72 80 0 81 75 0 83 22 0 22 82 0 80 83 0 84 3 0 3 81 0 82 85 0
		 91 86 0 87 89 0 27 88 0 89 90 0 90 29 0 92 91 0 88 92 0 93 96 0 97 95 0 94 24 0 24 87 0
		 95 94 0 96 69 0 70 97 0 86 4 0 4 98 0 100 93 0 99 100 0;
	setAttr -ch 101 ".fc[0]" -type "polyFaces" 
		f 78 90 95 58 80 81 76 65 71 72 73 74 66 70 67 68 69 62 63 21 24 22 23 8 9 11 12 13
		 14 10 16 18 5 6 7 19 20 17 15 25 26 31 27 28 33 34 2 3 32 54 51 50 38 39 41 42 47
		 44 45 43 46 37 40 1 49 52 53 55 56 48 85 89 88 83 97 98 0 100 99
		mu 0 78 93 96 69 84 3 81 75 78 2 5 8 79 77 76 9 7 71 73 28 45 44 10 33 36 37 11 6 12 38
		 35 39 42 13 14 43 16 40 41 34 17 46 49 15 47 19 51 18 50 31 64 65 54 56 55 20 58
		 61 21 0 60 59 57 53 62 63 67 66 1 68 27 88 92 91 86 4 98 99 100
		h 23 92 93 84 86 87 57 4 35 36 29 30 64 61 75 79 77 78 82 59 60 96 91 94
		mu 0 23 94 24 87 89 90 29 32 52 26 48 23 30 74 72 80 83 22 82 85 25 70 97 95;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_l_feet_letter_" -p "FM_Cam_c_feet_letter_";
	setAttr ".t" -type "double3" 2.8227822324329139 -0.38296284901079347 0 ;
	setAttr ".s" -type "double3" 1.5 1.5 1.5 ;
	setAttr ".rp" -type "double3" 28.194271087646484 -1.8220958709716797 1.9510667324066162 ;
	setAttr ".sp" -type "double3" 28.194271087646484 -1.8220958709716797 1.9510667324066162 ;
createNode mesh -n "FM_Cam_l_feet_letter_Shape" -p "FM_Cam_l_feet_letter_";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 65 ".uvst[0].uvsp[0:64]" -type "float2" 0.5 0.96153843 0.5
		 1 0 1 0 0.96153843 0 0.03846154 0.18181819 0.77929688 0.037112322 0.96185249 0.18184367
		 0.79841685 0.18199997 0.18732584 0.03735061 0.038129896 0 0 0.90909094 0 1 0.26442358
		 0.95454544 0.26923078 0.31818181 0.26183149 0.53582644 0.03818519 0.31797534 0.1892273
		 0.31817323 0.799263 0.49106994 0.96157098 0.18181819 0.45454547 0.31818181 0.45454547
		 0.44444445 0 0.44444445 0.038968313 0.18198383 0.18181819 0.31798223 0.18181819 0.22222222
		 0 0.16807985 0.090909094 0.11111111 0.047184724 0.11111111 0 0.32395512 0.090909094
		 0.33333334 0 0.33333334 0.068046808 0.18181819 0.27272728 0.18181819 0.36363637 0.31818181
		 0.27272728 0.31818181 0.36363637 0.97160017 0.18181819 0.91021633 0.18181819 0.66666669
		 0 0.66666669 0.040785223 0.55555558 0 0.55555558 0.038219575 0.77777779 0 0.77777779
		 0.060597908 0.94034553 0.090909094 0.83155572 0.090909094 0.8888889 0 0.8888889 0.14959854
		 0.44444445 1 0.44444445 0.96017241 0.18181819 0.72727275 0.31818181 0.72727275 0.18181819
		 0.54545456 0.18181819 0.63636363 0.31818181 0.54545456 0.31818181 0.63636363 0.22222222
		 1 0.18170518 0.81818181 0.16815327 0.90909094 0.11111111 1 0.11111111 0.95306927
		 0.31825608 0.81818181 0.32946685 0.90909094 0.33333334 1 0.33333334 0.91575831;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 65 ".pt[0:64]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 65 ".vt[0:64]"  12.44521141 -62.11536407 1.95106673 12.44521141 -62.047691345 1.95106673
		 11.70085716 -62.047691345 1.95106673 11.70085716 -62.11536407 1.95106673 11.70085716 -63.73940659 1.95106673
		 11.97153664 -62.43599319 1.95106673 11.75610638 -62.11480713 1.95106673 11.97158623 -62.40235901 1.95106673
		 11.97200298 -63.47749329 1.95106673 11.7564621 -63.73999023 1.95106673 11.70085716 -63.80707169 1.95106673
		 13.054226875 -63.80707169 1.95106673 13.18956375 -63.34185028 1.95106673 13.12189484 -63.3333931 1.95106673
		 12.17447758 -63.34641266 1.95106673 12.4985466 -63.74011612 1.95106673 12.17423153 -63.47415161 1.95106673
		 12.17449188 -62.40086746 1.95106673 12.43191624 -62.11530304 1.95106673 11.9715538 -63.0073509216 1.95106673
		 12.17453671 -63.0073509216 1.95106673 12.36250401 -63.80707169 1.95106673 12.36249828 -63.73868561 1.95106673
		 11.97199345 -63.48718643 1.95106673 12.17422867 -63.48718262 1.95106673 12.031681061 -63.80707169 1.95106673
		 11.95056057 -63.64691925 1.95106673 11.86623287 -63.72396469 1.95106673 11.86627007 -63.80707169 1.95106673
		 12.18315411 -63.64712524 1.95106673 12.19709301 -63.80707169 1.95106673 12.19676495 -63.68753052 1.95106673
		 11.97128201 -63.32723999 1.95106673 11.97130299 -63.16730118 1.95106673 12.17451286 -63.32723999 1.95106673
		 12.17453671 -63.16730118 1.95106673 13.14728546 -63.48718262 1.95106673 13.056084633 -63.48727798 1.95106673
		 12.69332886 -63.80707169 1.95106673 12.69335556 -63.73570251 1.95106673 12.52791691 -63.80707169 1.95106673
		 12.52791691 -63.73991394 1.95106673 12.85873985 -63.80707169 1.95106673 12.85874271 -63.70046234 1.95106673
		 13.10075569 -63.64712906 1.95106673 12.93879032 -63.64712143 1.95106673 13.024151802 -63.80707169 1.95106673
		 13.023965836 -63.54375458 1.95106673 12.36250401 -62.047691345 1.95106673 12.36250401 -62.11775589 1.95106673
		 11.97150612 -62.52752686 1.95106673 12.17453671 -62.52752686 1.95106673 11.97168159 -62.84741211 1.95106673
		 11.97159767 -62.68746567 1.95106673 12.17453671 -62.84741211 1.95106673 12.17453671 -62.68746567 1.95106673
		 12.031681061 -62.047691345 1.95106673 11.97153473 -62.3675766 1.95106673 11.95055866 -62.20786667 1.95106673
		 11.86627007 -62.047691345 1.95106673 11.86623478 -62.13035202 1.95106673 12.17463684 -62.3675766 1.95106673
		 12.19156265 -62.20772934 1.95106673 12.19709301 -62.047691345 1.95106673 12.19723606 -62.19598389 1.95106673;
	setAttr -s 65 ".ed[0:64]"  0 1 0 1 48 0 49 18 0 18 0 0 36 12 0 12 13 0
		 13 37 0 35 20 0 29 24 0 23 26 0 26 27 0 28 25 0 27 9 0 9 4 0 4 10 0 10 28 0 30 21 0
		 22 31 0 25 30 0 31 29 0 19 33 0 32 8 0 8 23 0 33 32 0 24 16 0 16 14 0 14 34 0 34 35 0
		 44 36 0 37 47 0 40 38 0 39 41 0 21 40 0 41 15 0 15 22 0 38 42 0 43 39 0 46 11 0 11 44 0
		 42 46 0 45 43 0 47 45 0 48 63 0 64 49 0 55 51 0 50 53 0 52 19 0 53 52 0 20 54 0 54 55 0
		 56 59 0 60 58 0 57 7 0 7 5 0 5 50 0 58 57 0 59 2 0 2 3 0 3 6 0 6 60 0 51 17 0 17 61 0
		 61 62 0 63 56 0 62 64 0;
	setAttr -ch 65 ".fc[0]" -type "polyFaces" 
		f 65 64 43 2 3 0 1 42 63 50 56 57 58 59 51 55 52 53 54 45 47 46 20 23 21 22 9 10 12
		 13 14 15 11 18 16 32 30 35 39 37 38 28 4 5 6 29 41 40 36 31 33 34 17 19 8 24 25 26
		 27 7 48 49 44 60 61 62
		mu 0 65 62 64 49 18 0 1 48 63 56 59 2 3 6 60 58 57 7 5 50 53 52 19 33 32 8 23 26 27 9 4
		 10 28 25 30 21 40 38 42 46 11 44 36 12 13 37 47 45 43 39 41 15 22 31 29 24 16 14
		 34 35 20 54 55 51 17 61;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_c_hi_body_" -p "FM_Cam_BODY_gui_guides_grp";
	setAttr ".rp" -type "double3" -2.1876144409179687 -2.3728256225585937 2.3219918012619019 ;
	setAttr ".sp" -type "double3" -2.1876144409179687 -2.3728256225585937 2.3219918012619019 ;
createNode transform -n "FM_Cam_r_hi_arm_" -p "FM_Cam_c_hi_body_";
	setAttr ".rp" -type "double3" -16.671303272247314 16.457347869873047 2.1393922567367554 ;
	setAttr ".sp" -type "double3" -16.671303272247314 16.457347869873047 2.1393922567367554 ;
createNode transform -n "Rt_shoulder_guide" -p "FM_Cam_r_hi_arm_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -8.142979621887207 18.17857551574707 2.1393923759460449 ;
	setAttr ".sp" -type "double3" -8.142979621887207 18.17857551574707 2.1393923759460449 ;
createNode mesh -n "Rt_shoulder_guideShape" -p "Rt_shoulder_guide";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 21 ".uvst[0].uvsp[0:20]" -type "float2" 0.4224298 0.032137346
		 0.52869076 0.066693999 0.47019911 0.078049056 0.49323919 0.10221282 0.52869076 0.11912756
		 0.55576003 0.1155033 0.58412218 0.094964311 0.59959215 0.066693999 0.625 0 0.625
		 0.066693999 0.6148358 0.10255056 0.60732722 0.12903883 0.58541125 0.16383144 0.55576026
		 0.18042409 0.52869076 0.18042409 0.48090714 0.16020662 0.44391629 0.12903883 0.41062218
		 0.097380474 0.375 0.12903883 0.375 0.066693999 0.375 0;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 21 ".pt[0:20]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 21 ".vt[0:20]"  -25.066921234 -44.034187317 2.13939238 -22.59849548 -44.034187317 2.13939238
		 -25.18558502 -42.45005035 2.13939238 -22.59849548 -43.21542358 2.13939238 -23.70656586 -43.21542358 2.13939238
		 -24.99275589 -43.21542358 2.13939238 -23.70656586 -41.81923294 2.13939238 -24.6113739 -43.63965607 2.13939238
		 -24.19606781 -43.076026917 2.13939238 -24.0032501221 -42.77937698 2.13939238 -23.70656586 -42.57171631 2.13939238
		 -22.89081955 -43.21542358 2.13939238 -23.39511871 -42.61621857 2.13939238 -23.068809509 -42.86836624 2.13939238
		 -24.7448616 -42.83870697 2.13939238 -24.52237701 -42.45005035 2.13939238 -24.16640472 -42.067420959 2.13939238
		 -23.3951149 -41.81923294 2.13939238 -22.80181885 -42.45005035 2.13939238 -23.053974152 -42.022918701 2.13939238
		 -22.71543884 -42.77522278 2.13939238;
	setAttr -s 21 ".ed[0:20]"  0 5 0 1 3 0 5 2 0 0 7 0 7 4 0 4 8 0 8 9 0
		 9 10 0 10 12 0 12 13 0 13 11 0 11 1 0 2 14 0 14 15 0 15 16 0 16 6 0 17 6 0 17 19 0
		 19 18 0 18 20 0 20 3 0;
	setAttr -ch 21 ".fc[0]" -type "polyFaces" 
		f 21 4 5 6 7 8 9 10 11 1 -21 -20 -19 -18 16 -16 -15 -14 -13 -3 -1 3
		mu 0 21 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "RtArm_Wrist_IK_guide" -p "FM_Cam_r_hi_arm_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -21.643396377563477 15.227508544921875 2.1393922567367554 ;
	setAttr ".sp" -type "double3" -21.643396377563477 15.227508544921875 2.1393922567367554 ;
createNode mesh -n "RtArm_Wrist_IK_guideShape" -p "RtArm_Wrist_IK_guide";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 6 ".uvst[0].uvsp[0:5]" -type "float2" 0.26224762 0.11706195
		 0.19908482 0.22638434 0.072875679 0.22638434 0.0097126365 0.11706183 0.072875321
		 0.0077396352 0.19908494 0.0077396948;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 6 ".pt[0:5]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0;
	setAttr -s 6 ".vt[0:5]"  -36.55337524 -44.42444992 2.13939238 -38.23154068 -44.42444992 2.13939238
		 -39.070617676 -45.87778091 2.13939238 -38.23154449 -47.33110428 2.13939214 -36.55338287 -47.33110428 2.13939214
		 -35.71429825 -45.87778091 2.13939238;
	setAttr -s 6 ".ed[0:5]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 0 0;
	setAttr -ch 6 ".fc[0]" -type "polyFaces" 
		f 6 5 0 1 2 3 4
		mu 0 6 0 1 2 3 4 5;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "RtArm_Wrist_FK_guide" -p "FM_Cam_r_hi_arm_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -18.865621566772461 15.110755920410156 2.1393923759460449 ;
	setAttr ".sp" -type "double3" -18.865621566772461 15.110755920410156 2.1393923759460449 ;
createNode mesh -n "RtArm_Wrist_FK_guideShape" -p "RtArm_Wrist_FK_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193001 0.61471206 0.80727184 0.7219848 0.7221396 0.80711704 0.61486673 0.86177522
		 0.49595416 0.8806091 0.3770414 0.86177522 0.2697686 0.80711704 0.18463637 0.7219848
		 0.12997819 0.61471206 0.11114423 0.49579921 0.12997819 0.37688643 0.18463637 0.26961371
		 0.26976854 0.1844815 0.37704134 0.12982315 0.49595416 0.11098927 0.61486691 0.12982315
		 0.72213972 0.18448138 0.80727196 0.26961353 0.86193019 0.37688643;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  -33.91712189 -45.7678833 2.13939238 -34.021305084 -45.56341171 2.13939238
		 -34.18356705 -45.40114975 2.13939238 -34.38803101 -45.29697037 2.13939238 -34.61468124 -45.26107407 2.13939238
		 -34.8413353 -45.29697037 2.13939238 -35.045791626 -45.40114975 2.13939238 -35.20806122 -45.56341171 2.13939238
		 -35.3122406 -45.7678833 2.13939238 -35.34814072 -45.99452972 2.13939238 -35.3122406 -46.22117615 2.13939238
		 -35.20806122 -46.42564011 2.13939238 -35.045791626 -46.58790588 2.13939238 -34.8413353 -46.69208908 2.13939238
		 -34.61468124 -46.72798538 2.13939238 -34.38803101 -46.69208908 2.13939238 -34.18356705 -46.58790588 2.13939238
		 -34.021305084 -46.42564011 2.13939238 -33.91712189 -46.22117615 2.13939238 -33.88122559 -45.99452972 2.13939238;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 19 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "Rtelbow1_bend_guide" -p "FM_Cam_r_hi_arm_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -15.939283847808838 14.699977874755859 2.1393923759460449 ;
	setAttr ".sp" -type "double3" -15.939283847808838 14.699977874755859 2.1393923759460449 ;
createNode mesh -n "Rtelbow1_bend_guideShape" -p "Rtelbow1_bend_guide";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.65625 0.84375 0.6486026
		 0.89203393 0.62640893 0.93559146 0.59184146 0.97015893 0.54828387 0.9923526 0.5 1
		 0.4517161 0.9923526 0.40815854 0.97015893 0.37359107 0.93559146 0.3513974 0.89203393
		 0.34374997 0.84375 0.3513974 0.79546607 0.37359107 0.75190854 0.40815851 0.71734107
		 0.45171607 0.69514734 0.5 0.68749994 0.54828393 0.69514734 0.59184152 0.71734101
		 0.62640899 0.75190848 0.64860266 0.79546607;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  -31.31370163 -46.28357697 2.13939238 -31.36965179 -46.17376328 2.13939238
		 -31.45679855 -46.086608887 2.13939238 -31.56661224 -46.030654907 2.13939238 -31.68834686 -46.011375427 2.13939238
		 -31.81008148 -46.030654907 2.13939238 -31.91989517 -46.086608887 2.13939238 -32.0070457458 -46.17376328 2.13939238
		 -32.062999725 -46.28357697 2.13939238 -32.082275391 -46.40530777 2.13939238 -32.062999725 -46.52703857 2.13939238
		 -32.0070457458 -46.63685608 2.13939238 -31.91989517 -46.72400665 2.13939238 -31.81008148 -46.77995682 2.13939238
		 -31.68834686 -46.79924011 2.13939238 -31.56661224 -46.77995682 2.13939238 -31.45679855 -46.72400665 2.13939238
		 -31.36965179 -46.63685608 2.13939238 -31.31370163 -46.52703857 2.13939238 -31.29441452 -46.40530777 2.13939238;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 19 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "RtArm_Switch_guide" -p "FM_Cam_r_hi_arm_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -19.31829833984375 17.579324722290039 2.1393923759460449 ;
	setAttr ".sp" -type "double3" -19.31829833984375 17.579324722290039 2.1393923759460449 ;
createNode mesh -n "RtArm_Switch_guideShape" -p "RtArm_Switch_guide";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 8 ".uvst[0].uvsp[0:7]" -type "float2" 0.625 0.083988376
		 0.625 0.25 0.5 0.25 0.625 0.25 0 0 0 1 1 0.5 0 1;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 8 ".pt[0:7]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 8 ".vt[0:7]"  -35.067432404 -44.5607605 2.13939238 -35.56148529 -42.49116135 2.13939238
		 -35.56148529 -43.15410995 2.13939238 -36.0587883 -43.15410995 2.13939238 -35.067432404 -42.49116135 2.13939238
		 -34.5733223 -42.49116135 2.13939238 -34.5733223 -43.15410995 2.13939238 -34.075931549 -43.15410995 2.13939238;
	setAttr -s 8 ".ed[0:7]"  2 1 0 2 3 0 0 3 0 4 1 0 6 5 0 6 7 0 0 7 0
		 4 5 0;
	setAttr -ch 8 ".fc[0]" -type "polyFaces" 
		f 8 4 -8 3 -1 1 -3 6 -6
		mu 0 8 0 1 2 3 4 5 6 7;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "RtArm_Elbow_FK_guide" -p "FM_Cam_r_hi_arm_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -12.974963188171387 14.603614807128906 2.1393923759460449 ;
	setAttr ".sp" -type "double3" -12.974963188171387 14.603614807128906 2.1393923759460449 ;
createNode mesh -n "RtArm_Elbow_FK_guideShape" -p "RtArm_Elbow_FK_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193001 0.61471206 0.80727184 0.7219848 0.7221396 0.80711704 0.61486673 0.86177522
		 0.49595416 0.8806091 0.3770414 0.86177522 0.2697686 0.80711704 0.18463637 0.7219848
		 0.12997819 0.61471206 0.11114423 0.49579921 0.12997819 0.37688643 0.18463637 0.26961371
		 0.26976854 0.1844815 0.37704134 0.12982315 0.49595416 0.11098927 0.61486691 0.12982315
		 0.72213972 0.18448138 0.80727196 0.26961353 0.86193019 0.37688643;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  -28.026462555 -46.27502441 2.13939238 -28.13064575 -46.070552826 2.13939238
		 -28.29290771 -45.90829086 2.13939238 -28.49737167 -45.80411148 2.13939238 -28.72402191 -45.76821518 2.13939238
		 -28.95067596 -45.80411148 2.13939238 -29.15513229 -45.90829086 2.13939238 -29.31740189 -46.070552826 2.13939238
		 -29.42158127 -46.27502441 2.13939238 -29.45748138 -46.50167084 2.13939238 -29.42158127 -46.72831726 2.13939238
		 -29.31740189 -46.93278122 2.13939238 -29.15513229 -47.095046997 2.13939238 -28.95067596 -47.19923019 2.13939238
		 -28.72402191 -47.2351265 2.13939238 -28.49737167 -47.19923019 2.13939238 -28.29290771 -47.095046997 2.13939238
		 -28.13064575 -46.93278122 2.13939238 -28.026462555 -46.72831726 2.13939238 -27.99056625 -46.50167084 2.13939238;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 19 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "RtArm_UpArm_FK_guide" -p "FM_Cam_r_hi_arm_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -7.5712919235229492 14.388404846191406 2.1393923759460449 ;
	setAttr ".sp" -type "double3" -7.5712919235229492 14.388404846191406 2.1393923759460449 ;
createNode mesh -n "RtArm_UpArm_FK_guideShape" -p "RtArm_UpArm_FK_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193001 0.61471206 0.80727184 0.7219848 0.7221396 0.80711704 0.61486673 0.86177522
		 0.49595416 0.8806091 0.3770414 0.86177522 0.2697686 0.80711704 0.18463637 0.7219848
		 0.12997819 0.61471206 0.11114423 0.49579921 0.12997819 0.37688643 0.18463637 0.26961371
		 0.26976854 0.1844815 0.37704134 0.12982315 0.49595416 0.11098927 0.61486691 0.12982315
		 0.72213972 0.18448138 0.80727196 0.26961353 0.86193019 0.37688643;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  -22.62279129 -46.49023438 2.13939238 -22.72697449 -46.28576279 2.13939238
		 -22.88923645 -46.12350082 2.13939238 -23.093700409 -46.019321442 2.13939238 -23.32035065 -45.98342514 2.13939238
		 -23.5470047 -46.019321442 2.13939238 -23.75146103 -46.12350082 2.13939238 -23.91373062 -46.28576279 2.13939238
		 -24.017910004 -46.49023438 2.13939238 -24.05381012 -46.7168808 2.13939238 -24.017910004 -46.94352722 2.13939238
		 -23.91373062 -47.14799118 2.13939238 -23.75146103 -47.31025696 2.13939238 -23.5470047 -47.41444016 2.13939238
		 -23.32035065 -47.45033646 2.13939238 -23.093700409 -47.41444016 2.13939238 -22.88923645 -47.31025696 2.13939238
		 -22.72697449 -47.14799118 2.13939238 -22.62279129 -46.94352722 2.13939238 -22.58689499 -46.7168808 2.13939238;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 19 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "RtupArm1_bend_guide" -p "FM_Cam_r_hi_arm_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -10.174860954284668 14.251388549804688 2.1393923759460449 ;
	setAttr ".sp" -type "double3" -10.174860954284668 14.251388549804688 2.1393923759460449 ;
createNode mesh -n "RtupArm1_bend_guideShape" -p "RtupArm1_bend_guide";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.65625 0.84375 0.6486026
		 0.89203393 0.62640893 0.93559146 0.59184146 0.97015893 0.54828387 0.9923526 0.5 1
		 0.4517161 0.9923526 0.40815854 0.97015893 0.37359107 0.93559146 0.3513974 0.89203393
		 0.34374997 0.84375 0.3513974 0.79546607 0.37359107 0.75190854 0.40815851 0.71734107
		 0.45171607 0.69514734 0.5 0.68749994 0.54828393 0.69514734 0.59184152 0.71734101
		 0.62640899 0.75190848 0.64860266 0.79546607;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  -25.54927826 -46.73216629 2.13939238 -25.60522842 -46.6223526 2.13939238
		 -25.69237518 -46.53519821 2.13939238 -25.80218887 -46.47924423 2.13939238 -25.92392349 -46.45996475 2.13939238
		 -26.045658112 -46.47924423 2.13939238 -26.1554718 -46.53519821 2.13939238 -26.24262238 -46.6223526 2.13939238
		 -26.29857635 -46.73216629 2.13939238 -26.31785202 -46.85389709 2.13939238 -26.29857635 -46.9756279 2.13939238
		 -26.24262238 -47.085445404 2.13939238 -26.1554718 -47.17259598 2.13939238 -26.045658112 -47.22854614 2.13939238
		 -25.92392349 -47.24782944 2.13939238 -25.80218887 -47.22854614 2.13939238 -25.69237518 -47.17259598 2.13939238
		 -25.60522842 -47.085445404 2.13939238 -25.54927826 -46.9756279 2.13939238 -25.52999115 -46.85389709 2.13939238;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 19 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "RtArm_Pole_ctrl_guide" -p "FM_Cam_r_hi_arm_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -13.049493789672852 17.957038879394531 2.1393922567367554 ;
	setAttr ".sp" -type "double3" -13.049493789672852 17.957038879394531 2.1393922567367554 ;
createNode mesh -n "RtArm_Pole_ctrl_guideShape" -p "RtArm_Pole_ctrl_guide";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 6 ".uvst[0].uvsp[0:5]" -type "float2" 0.26224762 0.11706195
		 0.19908482 0.22638434 0.072875679 0.22638434 0.0097126365 0.11706183 0.072875321
		 0.0077396352 0.19908494 0.0077396948;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 6 ".pt[0:5]" -type "float3"  24.078302 63.376411 -3.7600614e-008 
		24.607624 63.376411 -3.7600614e-008 24.872284 63.834816 -3.7600614e-008 24.607626 
		64.293221 3.7600614e-008 24.078304 64.293221 3.7600614e-008 23.813644 63.834816 -3.7600614e-008;
	setAttr -s 6 ".vt[0:5]"  -36.55337524 -44.42444992 2.13939238 -38.23154068 -44.42444992 2.13939238
		 -39.070617676 -45.87778091 2.13939238 -38.23154449 -47.33110428 2.13939214 -36.55338287 -47.33110428 2.13939214
		 -35.71429825 -45.87778091 2.13939238;
	setAttr -s 6 ".ed[0:5]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 0 0;
	setAttr -ch 6 ".fc[0]" -type "polyFaces" 
		f 6 5 0 1 2 3 4
		mu 0 6 0 1 2 3 4 5;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "To_Hands_View" -p "FM_Cam_r_hi_arm_";
	setAttr ".v" no;
	setAttr ".rp" -type "double3" -25.131332397460937 15.002086639404297 2.1393922567367554 ;
	setAttr ".sp" -type "double3" -25.131332397460937 15.002086639404297 2.1393922567367554 ;
createNode mesh -n "To_Hands_ViewShape" -p "|FM_Caml_gui_guides_grp|FM_Cam_BODY_gui_guides_grp|FM_Cam_c_hi_body_|FM_Cam_r_hi_arm_|To_Hands_View";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0:1]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 46 ".uvst[0].uvsp[0:45]" -type "float2" 0.625 0.083988376
		 0.5 0.083988376 0 0 0 1 1 0.5 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
		 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr -s 46 ".vt[0:45]"  -25.11658096 14.37480545 2.13939214 -25.11658096 15.27653122 2.13939238
		 -25.57693863 15.27653122 2.13939238 -26.040328979 15.27653122 2.13939238 -24.65616608 15.27653122 2.13939238
		 -24.19269943 15.27653122 2.13939238 -24.068218231 15.34751511 2.13939238 -24.22699356 15.65912247 2.13939238
		 -24.47429276 15.90642166 2.13939238 -24.78590775 16.065196991 2.13939238 -25.13132858 16.11990738 2.13939238
		 -25.47675323 16.065196991 2.13939238 -25.78837585 15.90642166 2.13939238 -26.035667419 15.65912247 2.13939238
		 -26.19444656 15.34751511 2.13939238 -26.24915314 15.00207901 2.13939214 -26.19444656 14.65665817 2.13939214
		 -26.035667419 14.34504318 2.13939214 -25.78837585 14.097743988 2.13939214 -25.47675323 13.93896866 2.13939214
		 -25.13132858 13.88425827 2.13939214 -24.78590775 13.93896866 2.13939214 -24.47429276 14.097743988 2.13939214
		 -24.22699356 14.34504318 2.13939214 -24.068218231 14.65665817 2.13939238 -24.013507843 15.00207901 2.13939238
		 -23.82510376 15.4264946 2.13939238 -24.020191193 15.80937576 2.13939238 -24.32404327 16.11322403 2.13939238
		 -24.70691681 16.30830765 2.13939238 -25.13132858 16.37553024 2.13939238 -25.55574417 16.30830765 2.13939238
		 -25.93862534 16.11322403 2.13939238 -26.24246979 15.80937576 2.13939238 -26.43754959 15.4264946 2.13939238
		 -26.50477219 15.00207901 2.13939214 -26.43754959 14.57767105 2.13939214 -26.24246979 14.19479752 2.13939214
		 -25.93862534 13.89094162 2.13939214 -25.55574417 13.69586563 2.13939214 -25.13132858 13.62864304 2.13939214
		 -24.70691681 13.69586563 2.13939214 -24.32404327 13.89094162 2.13939214 -24.020191193 14.19479752 2.13939214
		 -23.82511139 14.57767105 2.13939238 -23.75789261 15.00207901 2.13939238;
	setAttr -s 46 ".ed[0:45]"  2 1 0 2 3 0 0 3 0 4 1 0 0 5 0 4 5 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 20 0 20 21 0 21 22 0 22 23 0 23 24 0 24 25 0 25 6 0 26 27 0 27 28 0 28 29 0
		 29 30 0 30 31 0 31 32 0 32 33 0 33 34 0 34 35 0 35 36 0 36 37 0 37 38 0 38 39 0 39 40 0
		 40 41 0 41 42 0 42 43 0 43 44 0 44 45 0 45 26 0;
	setAttr -s 2 -ch 46 ".fc[0:1]" -type "polyFaces" 
		f 6 3 -1 1 -3 4 -6
		mu 0 6 0 1 2 3 4 5
		f 20 44 45 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43
		mu 0 20 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
		h 20 -25 -24 -23 -22 -21 -20 -19 -18 -17 -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -26
		mu 0 20 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_l_hi_arm_" -p "FM_Cam_c_hi_body_";
	setAttr ".rp" -type "double3" 12.296071529388428 17.813329696655273 2.1393922567367554 ;
	setAttr ".sp" -type "double3" 12.296071529388428 17.813329696655273 2.1393922567367554 ;
createNode transform -n "Lf_shoulder_guide" -p "FM_Cam_l_hi_arm_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 3.7677478790283203 18.17857551574707 2.1393923759460449 ;
	setAttr ".sp" -type "double3" 3.7677478790283203 18.17857551574707 2.1393923759460449 ;
createNode mesh -n "Lf_shoulder_guideShape" -p "Lf_shoulder_guide";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 21 ".uvst[0].uvsp[0:20]" -type "float2" 0.4224298 0.032137346
		 0.375 0 0.375 0.066693999 0.375 0.12903883 0.41062218 0.097380474 0.44391629 0.12903883
		 0.48090714 0.16020662 0.52869076 0.18042409 0.55576026 0.18042409 0.58541125 0.16383144
		 0.60732722 0.12903883 0.6148358 0.10255056 0.625 0.066693999 0.625 0 0.59959215 0.066693999
		 0.58412218 0.094964311 0.55576003 0.1155033 0.52869076 0.11912756 0.49323919 0.10221282
		 0.47019911 0.078049056 0.52869076 0.066693999;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 21 ".pt[0:20]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 21 ".vt[0:20]"  -10.80643272 -44.034187317 2.13939238 -13.27485657 -44.034187317 2.13939238
		 -10.68776894 -42.45005035 2.13939238 -13.27485657 -43.21542358 2.13939238 -12.16678619 -43.21542358 2.13939238
		 -10.88059807 -43.21542358 2.13939238 -12.16678619 -41.81923294 2.13939238 -11.26198006 -43.63965607 2.13939238
		 -11.67728615 -43.076026917 2.13939238 -11.87010574 -42.77937698 2.13939238 -12.16678619 -42.57171631 2.13939238
		 -12.98253536 -43.21542358 2.13939238 -12.47823715 -42.61621857 2.13939238 -12.80454445 -42.86836624 2.13939238
		 -11.12849045 -42.83870697 2.13939238 -11.35097885 -42.45005035 2.13939238 -11.70694733 -42.067420959 2.13939238
		 -12.47824001 -41.81923294 2.13939238 -13.071534157 -42.45005035 2.13939238 -12.81937885 -42.022918701 2.13939238
		 -13.15791321 -42.77522278 2.13939238;
	setAttr -s 21 ".ed[0:20]"  0 5 0 1 3 0 5 2 0 0 7 0 7 4 0 4 8 0 8 9 0
		 9 10 0 10 12 0 12 13 0 13 11 0 11 1 0 2 14 0 14 15 0 15 16 0 16 6 0 17 6 0 17 19 0
		 19 18 0 18 20 0 20 3 0;
	setAttr -ch 21 ".fc[0]" -type "polyFaces" 
		f 21 -4 0 2 12 13 14 15 -17 17 18 19 20 -2 -12 -11 -10 -9 -8 -7 -6 -5
		mu 0 21 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "LfArm_Wrist_IK_guide" -p "FM_Cam_l_hi_arm_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 17.26816987991333 15.227508544921875 2.1393923759460449 ;
	setAttr ".sp" -type "double3" 17.26816987991333 15.227508544921875 2.1393923759460449 ;
createNode mesh -n "LfArm_Wrist_IK_guideShape" -p "LfArm_Wrist_IK_guide";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 6 ".uvst[0].uvsp[0:5]" -type "float2" 0.26224762 0.11706195
		 0.19908494 0.0077396948 0.072875321 0.0077396352 0.0097126365 0.11706183 0.072875679
		 0.22638434 0.19908482 0.22638434;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 6 ".pt[0:5]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0;
	setAttr -s 6 ".vt[0:5]"  2.3581934 -44.42444992 2.13939238 0.6800251 -44.42444992 2.13939238
		 -0.1590519 -45.87778091 2.13939238 0.68002129 -47.33110428 2.13939238 2.35818386 -47.33110428 2.13939238
		 3.19727039 -45.87778091 2.13939238;
	setAttr -s 6 ".ed[0:5]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 0 0;
	setAttr -ch 6 ".fc[0]" -type "polyFaces" 
		f 6 5 0 1 2 3 4
		mu 0 6 0 5 4 3 2 1;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "LfArm_Wrist_FK_guide" -p "FM_Cam_l_hi_arm_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 14.490392684936523 15.110755920410156 2.1393923759460449 ;
	setAttr ".sp" -type "double3" 14.490392684936523 15.110755920410156 2.1393923759460449 ;
createNode mesh -n "LfArm_Wrist_FK_guideShape" -p "LfArm_Wrist_FK_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193001 0.61471206 0.80727184 0.7219848 0.7221396 0.80711704 0.61486673 0.86177522
		 0.49595416 0.8806091 0.3770414 0.86177522 0.2697686 0.80711704 0.18463637 0.7219848
		 0.12997819 0.61471206 0.11114423 0.49579921 0.12997819 0.37688643 0.18463637 0.26961371
		 0.26976854 0.1844815 0.37704134 0.12982315 0.49595416 0.11098927 0.61486691 0.12982315
		 0.72213972 0.18448138 0.80727196 0.26961353 0.86193019 0.37688643;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  -1.95623493 -45.7678833 2.13939238 -1.85204792 -45.56341171 2.13939238
		 -1.68978977 -45.40114975 2.13939238 -1.48531818 -45.29697037 2.13939238 -1.25867367 -45.26107407 2.13939238
		 -1.032019615 -45.29697037 2.13939238 -0.8275671 -45.40114975 2.13939238 -0.66528988 -45.56341171 2.13939238
		 -0.56111813 -45.7678833 2.13939238 -0.52520847 -45.99452972 2.13939238 -0.56111813 -46.22117615 2.13939238
		 -0.66528988 -46.42564011 2.13939238 -0.8275671 -46.58790588 2.13939238 -1.032019615 -46.69208908 2.13939238
		 -1.25867367 -46.72798538 2.13939238 -1.48531818 -46.69208908 2.13939238 -1.68978977 -46.58790588 2.13939238
		 -1.85204792 -46.42564011 2.13939238 -1.95623493 -46.22117615 2.13939238 -1.99212742 -45.99452972 2.13939238;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 -19 -18 -17 -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 -20
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "Lfelbow1_bend_guide" -p "FM_Cam_l_hi_arm_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 11.564051628112793 14.699977874755859 2.1393923759460449 ;
	setAttr ".sp" -type "double3" 11.564051628112793 14.699977874755859 2.1393923759460449 ;
createNode mesh -n "Lfelbow1_bend_guideShape" -p "Lfelbow1_bend_guide";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.65625 0.84375 0.64860266
		 0.79546607 0.62640899 0.75190848 0.59184152 0.71734101 0.54828393 0.69514734 0.5
		 0.68749994 0.45171607 0.69514734 0.40815851 0.71734107 0.37359107 0.75190854 0.3513974
		 0.79546607 0.34374997 0.84375 0.3513974 0.89203393 0.37359107 0.93559146 0.40815854
		 0.97015893 0.4517161 0.9923526 0.5 1 0.54828387 0.9923526 0.59184146 0.97015893 0.62640893
		 0.93559146 0.6486026 0.89203393;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  -4.55964947 -46.28357697 2.13939238 -4.50370121 -46.17376328 2.13939238
		 -4.41655827 -46.086608887 2.13939238 -4.30673885 -46.030654907 2.13939238 -4.18500805 -46.011375427 2.13939238
		 -4.063275337 -46.030654907 2.13939238 -3.95345783 -46.086608887 2.13939238 -3.86630726 -46.17376328 2.13939238
		 -3.81035328 -46.28357697 2.13939238 -3.7910738 -46.40530777 2.13939238 -3.81035328 -46.52703857 2.13939238
		 -3.86630726 -46.63685608 2.13939238 -3.95345783 -46.72400665 2.13939238 -4.063275337 -46.77995682 2.13939238
		 -4.18500805 -46.79924011 2.13939238 -4.30673885 -46.77995682 2.13939238 -4.41655827 -46.72400665 2.13939238
		 -4.50370121 -46.63685608 2.13939238 -4.55964947 -46.52703857 2.13939238 -4.57894421 -46.40530777 2.13939238;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 -19 -18 -17 -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 -20
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "LfArm_Switch_guide" -p "FM_Cam_l_hi_arm_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 14.943061828613281 17.579324722290039 2.1393923759460449 ;
	setAttr ".sp" -type "double3" 14.943061828613281 17.579324722290039 2.1393923759460449 ;
createNode mesh -n "LfArm_Switch_guideShape" -p "LfArm_Switch_guide";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 8 ".uvst[0].uvsp[0:7]" -type "float2" 0.625 0.083988376
		 0 1 1 0.5 0 1 0 0 0.625 0.25 0.5 0.25 0.625 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 8 ".pt[0:7]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 8 ".vt[0:7]"  -0.80592442 -44.5607605 2.13939238 -0.31187153 -42.49116135 2.13939238
		 -0.31187153 -43.15410995 2.13939238 0.18542957 -43.15410995 2.13939238 -0.80592442 -42.49116135 2.13939238
		 -1.30003643 -42.49116135 2.13939238 -1.30003643 -43.15410995 2.13939238 -1.79742718 -43.15410995 2.13939238;
	setAttr -s 8 ".ed[0:7]"  2 1 0 2 3 0 0 3 0 4 1 0 6 5 0 6 7 0 0 7 0
		 4 5 0;
	setAttr -ch 8 ".fc[0]" -type "polyFaces" 
		f 8 5 -7 2 -2 0 -4 7 -5
		mu 0 8 0 1 2 3 4 5 6 7;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "LfArm_Elbow_FK_guide" -p "FM_Cam_l_hi_arm_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 8.5997326374053955 14.603614807128906 2.1393923759460449 ;
	setAttr ".sp" -type "double3" 8.5997326374053955 14.603614807128906 2.1393923759460449 ;
createNode mesh -n "LfArm_Elbow_FK_guideShape" -p "LfArm_Elbow_FK_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193001 0.61471206 0.80727184 0.7219848 0.7221396 0.80711704 0.61486673 0.86177522
		 0.49595416 0.8806091 0.3770414 0.86177522 0.2697686 0.80711704 0.18463637 0.7219848
		 0.12997819 0.61471206 0.11114423 0.49579921 0.12997819 0.37688643 0.18463637 0.26961371
		 0.26976854 0.1844815 0.37704134 0.12982315 0.49595416 0.11098927 0.61486691 0.12982315
		 0.72213972 0.18448138 0.80727196 0.26961353 0.86193019 0.37688643;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  -7.84688997 -46.27502441 2.13939238 -7.74270916 -46.070552826 2.13939238
		 -7.5804491 -45.90829086 2.13939238 -7.37598133 -45.80411148 2.13939238 -7.14933109 -45.76821518 2.13939238
		 -6.92267895 -45.80411148 2.13939238 -6.71822262 -45.90829086 2.13939238 -6.5559473 -46.070552826 2.13939238
		 -6.45177555 -46.27502441 2.13939238 -6.41586781 -46.50167084 2.13939238 -6.45177555 -46.72831726 2.13939238
		 -6.5559473 -46.93278122 2.13939238 -6.71822262 -47.095046997 2.13939238 -6.92267895 -47.19923019 2.13939238
		 -7.14933109 -47.2351265 2.13939238 -7.37598133 -47.19923019 2.13939238 -7.5804491 -47.095046997 2.13939238
		 -7.74270916 -46.93278122 2.13939238 -7.84688997 -46.72831726 2.13939238 -7.88278818 -46.50167084 2.13939238;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 -19 -18 -17 -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 -20
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "LfArm_UpArm_FK_guide" -p "FM_Cam_l_hi_arm_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 3.1960582733154297 14.388404846191406 2.1393923759460449 ;
	setAttr ".sp" -type "double3" 3.1960582733154297 14.388404846191406 2.1393923759460449 ;
createNode mesh -n "LfArm_UpArm_FK_guideShape" -p "LfArm_UpArm_FK_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193001 0.61471206 0.80727184 0.7219848 0.7221396 0.80711704 0.61486673 0.86177522
		 0.49595416 0.8806091 0.3770414 0.86177522 0.2697686 0.80711704 0.18463637 0.7219848
		 0.12997819 0.61471206 0.11114423 0.49579921 0.12997819 0.37688643 0.18463637 0.26961371
		 0.26976854 0.1844815 0.37704134 0.12982315 0.49595416 0.11098927 0.61486691 0.12982315
		 0.72213972 0.18448138 0.80727196 0.26961353 0.86193019 0.37688643;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  -13.25056171 -46.49023438 2.13939238 -13.14637852 -46.28576279 2.13939238
		 -12.98411751 -46.12350082 2.13939238 -12.77965355 -46.019321442 2.13939238 -12.55300236 -45.98342514 2.13939238
		 -12.3263464 -46.019321442 2.13939238 -12.12189293 -46.12350082 2.13939238 -11.95962524 -46.28576279 2.13939238
		 -11.85544586 -46.49023438 2.13939238 -11.81954384 -46.7168808 2.13939238 -11.85544586 -46.94352722 2.13939238
		 -11.95962524 -47.14799118 2.13939238 -12.12189293 -47.31025696 2.13939238 -12.3263464 -47.41444016 2.13939238
		 -12.55300236 -47.45033646 2.13939238 -12.77965355 -47.41444016 2.13939238 -12.98411751 -47.31025696 2.13939238
		 -13.14637852 -47.14799118 2.13939238 -13.25056171 -46.94352722 2.13939238 -13.28646088 -46.7168808 2.13939238;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 -19 -18 -17 -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 -20
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "LfupArm1_bend_guide" -p "FM_Cam_l_hi_arm_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 5.7996292114257812 14.251388549804688 2.1393923759460449 ;
	setAttr ".sp" -type "double3" 5.7996292114257812 14.251388549804688 2.1393923759460449 ;
createNode mesh -n "LfupArm1_bend_guideShape" -p "LfupArm1_bend_guide";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.65625 0.84375 0.64860266
		 0.79546607 0.62640899 0.75190848 0.59184152 0.71734101 0.54828393 0.69514734 0.5
		 0.68749994 0.45171607 0.69514734 0.40815851 0.71734107 0.37359107 0.75190854 0.3513974
		 0.79546607 0.34374997 0.84375 0.3513974 0.89203393 0.37359107 0.93559146 0.40815854
		 0.97015893 0.4517161 0.9923526 0.5 1 0.54828387 0.9923526 0.59184146 0.97015893 0.62640893
		 0.93559146 0.6486026 0.89203393;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  -10.3240757 -46.73216629 2.13939238 -10.26812363 -46.6223526 2.13939238
		 -10.18098068 -46.53519821 2.13939238 -10.071166992 -46.47924423 2.13939238 -9.94942856 -46.45996475 2.13939238
		 -9.82769775 -46.47924423 2.13939238 -9.71788216 -46.53519821 2.13939238 -9.63073158 -46.6223526 2.13939238
		 -9.57477379 -46.73216629 2.13939238 -9.55550194 -46.85389709 2.13939238 -9.57477379 -46.9756279 2.13939238
		 -9.63073158 -47.085445404 2.13939238 -9.71788216 -47.17259598 2.13939238 -9.82769775 -47.22854614 2.13939238
		 -9.94942856 -47.24782944 2.13939238 -10.071166992 -47.22854614 2.13939238 -10.18098068 -47.17259598 2.13939238
		 -10.26812363 -47.085445404 2.13939238 -10.3240757 -46.9756279 2.13939238 -10.3433609 -46.85389709 2.13939238;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 -19 -18 -17 -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 -20
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "LfArm_Pole_ctrl_guide" -p "FM_Cam_l_hi_arm_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 8.6804599761962891 17.957036972045898 2.1393922567367554 ;
	setAttr ".sp" -type "double3" 8.6804599761962891 17.957036972045898 2.1393922567367554 ;
createNode mesh -n "LfArm_Pole_ctrl_guideShape" -p "LfArm_Pole_ctrl_guide";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 6 ".uvst[0].uvsp[0:5]" -type "float2" 0.26224762 0.11706195
		 0.19908482 0.22638434 0.072875679 0.22638434 0.0097126365 0.11706183 0.072875321
		 0.0077396352 0.19908494 0.0077396948;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 6 ".pt[0:5]" -type "float3"  16.90045 61.105286 0 14.601362 
		61.105286 0 13.449148 61.105286 0 14.601358 61.105286 0 16.900438 61.105286 0 18.047308 
		61.105286 0;
	setAttr -s 6 ".vt[0:5]"  -7.64387894 -42.15332413 2.13939238 -6.49433517 -42.15332413 2.13939238
		 -5.91822815 -43.14825058 2.13939238 -6.49433327 -44.14317322 2.13939214 -7.64387321 -44.14317322 2.13939214
		 -8.21730804 -43.14825058 2.13939238;
	setAttr -s 6 ".ed[0:5]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 0 0;
	setAttr -ch 6 ".fc[0]" -type "polyFaces" 
		f 6 5 0 1 2 3 4
		mu 0 6 0 1 2 3 4 5;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "To_Hands_View" -p "FM_Cam_l_hi_arm_";
	setAttr ".v" no;
	setAttr ".rp" -type "double3" 20.756097793579102 15.002086639404297 2.1393923759460449 ;
	setAttr ".sp" -type "double3" 20.756097793579102 15.002086639404297 2.1393923759460449 ;
createNode mesh -n "To_Hands_ViewShape" -p "|FM_Caml_gui_guides_grp|FM_Cam_BODY_gui_guides_grp|FM_Cam_c_hi_body_|FM_Cam_l_hi_arm_|To_Hands_View";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0:1]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 46 ".uvst[0].uvsp[0:45]" -type "float2" 0.625 0.083988376
		 0 1 1 0.5 0 1 0 0 0.5 0.083988376 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
		 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr -s 46 ".vt[0:45]"  20.74134254 14.37480545 2.13939238 20.74134254 15.27653122 2.13939238
		 21.20170975 15.27653122 2.13939238 21.66510582 15.27653122 2.13939238 20.28092957 15.27653122 2.13939238
		 19.81745911 15.27653122 2.13939238 19.69298744 15.34751511 2.13939238 19.85176659 15.65912247 2.13939238
		 20.099060059 15.90642166 2.13939238 20.41067886 16.065196991 2.13939238 20.75609016 16.11990738 2.13939238
		 21.10153389 16.065196991 2.13939238 21.41314125 15.90642166 2.13939238 21.66042709 15.65912247 2.13939238
		 21.81920433 15.34751511 2.13939238 21.87392807 15.00207901 2.13939238 21.81920433 14.65665817 2.13939238
		 21.66042709 14.34504318 2.13939238 21.41314125 14.097743988 2.13939238 21.10153389 13.93896866 2.13939238
		 20.75609016 13.88425827 2.13939238 20.41067886 13.93896866 2.13939238 20.099060059 14.097743988 2.13939238
		 19.85176659 14.34504318 2.13939238 19.69298744 14.65665817 2.13939238 19.63828659 15.00207901 2.13939238
		 19.44987106 15.4264946 2.13939238 19.64494896 15.80937576 2.13939238 19.94882011 16.11322403 2.13939238
		 20.3316803 16.30830765 2.13939238 20.75609016 16.37553024 2.13939238 21.1805191 16.30830765 2.13939238
		 21.56339645 16.11322403 2.13939238 21.86724091 15.80937576 2.13939238 22.062328339 15.4264946 2.13939238
		 22.1295433 15.00207901 2.13939238 22.062328339 14.57767105 2.13939238 21.86724091 14.19479752 2.13939238
		 21.56339645 13.89094162 2.13939238 21.1805191 13.69586563 2.13939238 20.75609016 13.62864304 2.13939238
		 20.3316803 13.69586563 2.13939238 19.94882011 13.89094162 2.13939238 19.64494896 14.19479752 2.13939238
		 19.44988441 14.57767105 2.13939238 19.38265228 15.00207901 2.13939238;
	setAttr -s 46 ".ed[0:45]"  2 1 0 2 3 0 0 3 0 4 1 0 0 5 0 4 5 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 20 0 20 21 0 21 22 0 22 23 0 23 24 0 24 25 0 25 6 0 26 27 0 27 28 0 28 29 0
		 29 30 0 30 31 0 31 32 0 32 33 0 33 34 0 34 35 0 35 36 0 36 37 0 37 38 0 38 39 0 39 40 0
		 40 41 0 41 42 0 42 43 0 43 44 0 44 45 0 45 26 0;
	setAttr -s 2 -ch 46 ".fc[0:1]" -type "polyFaces" 
		f 6 5 -5 2 -2 0 -4
		mu 0 6 0 1 2 3 4 5
		f 20 -44 -43 -42 -41 -40 -39 -38 -37 -36 -35 -34 -33 -32 -31 -30 -29 -28 -27 -46 -45
		mu 0 20 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
		h 20 25 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
		mu 0 20 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_r_hi_crura_" -p "FM_Cam_c_hi_body_";
	setAttr ".rp" -type "double3" -7.052342414855957 -10.605884552001953 2.1393920183181763 ;
	setAttr ".sp" -type "double3" -7.052342414855957 -10.605884552001953 2.1393920183181763 ;
createNode transform -n "RtLeg_hip_ctrl_guide" -p "FM_Cam_r_hi_crura_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -9.2157735824584961 0.99640846252441406 2.1393921375274658 ;
	setAttr ".sp" -type "double3" -9.2157735824584961 0.99640846252441406 2.1393921375274658 ;
createNode mesh -n "RtLeg_hip_ctrl_guideShape" -p "RtLeg_hip_ctrl_guide";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 21 ".uvst[0].uvsp[0:20]" -type "float2" 0.4224298 0.032137346
		 0.52869076 0.066693999 0.47019911 0.078049056 0.49323919 0.10221282 0.52869076 0.11912756
		 0.55576003 0.1155033 0.58412218 0.094964311 0.59959215 0.066693999 0.625 0 0.625
		 0.066693999 0.6148358 0.10255056 0.60732722 0.12903883 0.58541125 0.16383144 0.55576026
		 0.18042409 0.52869076 0.18042409 0.48090714 0.16020662 0.44391629 0.12903883 0.41062218
		 0.097380474 0.375 0.12903883 0.375 0.066693999 0.375 0;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 21 ".pt[0:20]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 21 ".vt[0:20]"  -24.14310455 -61.41454697 2.13939214 -23.76460266 -58.92876053 2.13939214
		 -25.75659943 -61.29114532 2.13939214 -24.5891304 -58.8032074 2.13939214 -24.75902939 -59.91906738 2.13939214
		 -24.95626068 -61.21432114 2.13939214 -26.16506577 -59.70497894 2.13939214 -24.47055817 -60.89530182 2.13939214
		 -24.97447968 -60.39064407 2.13939214 -25.2436409 -60.15098572 2.13939214 -25.40727997 -59.82036972 2.13939214
		 -24.63394928 -59.097587585 2.13939214 -25.3147049 -59.51356125 2.13939214 -25.010753632 -59.22360992 2.13939214
		 -25.29761887 -60.90692139 2.13939214 -25.6548996 -60.62327194 2.13939214 -25.98563385 -60.20611954 2.13939214
		 -26.11730576 -59.39134598 2.13939214 -25.39107895 -58.89060211 2.13939214 -25.85986328 -59.079040527 2.13939214
		 -25.050365448 -58.85346985 2.13939214;
	setAttr -s 21 ".ed[0:20]"  0 5 0 1 3 0 5 2 0 0 7 0 7 4 0 4 8 0 8 9 0
		 9 10 0 10 12 0 12 13 0 13 11 0 11 1 0 2 14 0 14 15 0 15 16 0 16 6 0 17 6 0 17 19 0
		 19 18 0 18 20 0 20 3 0;
	setAttr -ch 21 ".fc[0]" -type "polyFaces" 
		f 21 4 5 6 7 8 9 10 11 1 -21 -20 -19 -18 16 -16 -15 -14 -13 -3 -1 3
		mu 0 21 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "RtLeg_Pole_ctrl_guide" -p "FM_Cam_r_hi_crura_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -9.6201314926147461 -8.9782676696777344 2.1393920183181763 ;
	setAttr ".sp" -type "double3" -9.6201314926147461 -8.9782676696777344 2.1393920183181763 ;
createNode mesh -n "RtLeg_Pole_ctrl_guideShape" -p "RtLeg_Pole_ctrl_guide";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 6 ".uvst[0].uvsp[0:5]" -type "float2" 0.26224762 0.11706195
		 0.19908482 0.22638434 0.072875679 0.22638434 0.0097126365 0.11706183 0.072875321
		 0.0077396352 0.19908494 0.0077396948;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 6 ".pt[0:5]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0;
	setAttr -s 6 ".vt[0:5]"  -24.53010941 -68.63022614 2.13939214 -26.20827484 -68.63022614 2.13939214
		 -27.047351837 -70.083557129 2.1393919 -26.20827866 -71.53688049 2.1393919 -24.53011703 -71.53688049 2.1393919
		 -23.69103241 -70.083557129 2.1393919;
	setAttr -s 6 ".ed[0:5]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 0 0;
	setAttr -ch 6 ".fc[0]" -type "polyFaces" 
		f 6 5 0 1 2 3 4
		mu 0 6 0 1 2 3 4 5;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "RtLeg_Switch_guide" -p "FM_Cam_r_hi_crura_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -9.6044712066650391 -18.490982055664063 2.1393918991088867 ;
	setAttr ".sp" -type "double3" -9.6044712066650391 -18.490982055664063 2.1393918991088867 ;
createNode mesh -n "RtLeg_Switch_guideShape" -p "RtLeg_Switch_guide";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 8 ".uvst[0].uvsp[0:7]" -type "float2" 0.625 0.083988376
		 0.625 0.25 0.5 0.25 0.625 0.25 0 0 0 1 1 0.5 0 1;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 8 ".pt[0:7]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 8 ".vt[0:7]"  -24.17120743 -79.59444427 2.1393919 -26.5345192 -80.16157532 2.1393919
		 -25.77727127 -80.16067505 2.1393919 -25.77659607 -80.72871399 2.1393919 -26.53518677 -79.59724426 2.1393919
		 -26.53585625 -79.032852173 2.1393919 -25.77860641 -79.031951904 2.1393919 -25.77928162 -78.46382141 2.1393919;
	setAttr -s 8 ".ed[0:7]"  2 1 0 2 3 0 0 3 0 4 1 0 6 5 0 6 7 0 0 7 0
		 4 5 0;
	setAttr -ch 8 ".fc[0]" -type "polyFaces" 
		f 8 4 -8 3 -1 1 -3 6 -6
		mu 0 8 0 1 2 3 4 5 6 7;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "RtLeg_Leg_FK_guide" -p "FM_Cam_r_hi_crura_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -4.3959531784057617 0.58365058898925781 2.1393921375274658 ;
	setAttr ".sp" -type "double3" -4.3959531784057617 0.58365058898925781 2.1393921375274658 ;
createNode mesh -n "RtLeg_Leg_FK_guideShape" -p "RtLeg_Leg_FK_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193001 0.61471206 0.80727184 0.7219848 0.7221396 0.80711704 0.61486673 0.86177522
		 0.49595416 0.8806091 0.3770414 0.86177522 0.2697686 0.80711704 0.18463637 0.7219848
		 0.12997819 0.61471206 0.11114423 0.49579921 0.12997819 0.37688643 0.18463637 0.26961371
		 0.26976854 0.1844815 0.37704134 0.12982315 0.49595416 0.11098927 0.61486691 0.12982315
		 0.72213972 0.18448138 0.80727196 0.26961353 0.86193019 0.37688643;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  -19.24759293 -60.23004913 2.13939214 -19.38162613 -59.96699524 2.13939214
		 -19.59037781 -59.75824356 2.13939214 -19.85342407 -59.62421417 2.13939214 -20.1450119 -59.57803726 2.13939214
		 -20.43660355 -59.62421417 2.13939214 -20.69963837 -59.75824356 2.13939214 -20.90840149 -59.96699524 2.13939214
		 -21.042427063 -60.23004913 2.13939214 -21.088615417 -60.52163315 2.13939214 -21.042427063 -60.81321716 2.13939214
		 -20.90840149 -61.076263428 2.13939214 -20.69963837 -61.28501892 2.13939214 -20.43660355 -61.41904831 2.13939214
		 -20.1450119 -61.46523285 2.13939214 -19.85342407 -61.41904831 2.13939214 -19.59037781 -61.28501892 2.13939214
		 -19.38162613 -61.076263428 2.13939214 -19.24759293 -60.81321716 2.13939214 -19.2014122 -60.52163315 2.13939214;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 19 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "RtLeg_Knee_FK_guide" -p "FM_Cam_r_hi_crura_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -5.6526250839233398 -8.5901298522949219 2.1393920183181763 ;
	setAttr ".sp" -type "double3" -5.6526250839233398 -8.5901298522949219 2.1393920183181763 ;
createNode mesh -n "RtLeg_Knee_FK_guideShape" -p "RtLeg_Knee_FK_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193001 0.61471206 0.80727184 0.7219848 0.7221396 0.80711704 0.61486673 0.86177522
		 0.49595416 0.8806091 0.3770414 0.86177522 0.2697686 0.80711704 0.18463637 0.7219848
		 0.12997819 0.61471206 0.11114423 0.49579921 0.12997819 0.37688643 0.18463637 0.26961371
		 0.26976854 0.1844815 0.37704134 0.12982315 0.49595416 0.11098927 0.61486691 0.12982315
		 0.72213972 0.18448138 0.80727196 0.26961353 0.86193019 0.37688643;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  -20.70412445 -69.46876526 2.13939214 -20.80830765 -69.26429749 2.13939214
		 -20.97056961 -69.10203552 2.13939214 -21.17503357 -68.99785614 2.13939214 -21.40168381 -68.96195984 2.13939214
		 -21.62833786 -68.99785614 2.13939214 -21.83279419 -69.10203552 2.13939214 -21.99506378 -69.26429749 2.13939214
		 -22.099243164 -69.46876526 2.13939214 -22.13514328 -69.69541931 2.13939214 -22.099243164 -69.92206573 2.1393919
		 -21.99506378 -70.12652588 2.1393919 -21.83279419 -70.28878784 2.1393919 -21.62833786 -70.39297485 2.1393919
		 -21.40168381 -70.42887115 2.1393919 -21.17503357 -70.39297485 2.1393919 -20.97056961 -70.28878784 2.1393919
		 -20.80830765 -70.12652588 2.1393919 -20.70412445 -69.92206573 2.13939214 -20.66822815 -69.69541931 2.13939214;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 19 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "RtLeg_Ankle_FK_guide" -p "FM_Cam_r_hi_crura_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -6.3084707260131836 -19.083629608154297 2.1393918991088867 ;
	setAttr ".sp" -type "double3" -6.3084707260131836 -19.083629608154297 2.1393918991088867 ;
createNode mesh -n "RtLeg_Ankle_FK_guideShape" -p "RtLeg_Ankle_FK_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193001 0.61471206 0.80727184 0.7219848 0.7221396 0.80711704 0.61486673 0.86177522
		 0.49595416 0.8806091 0.3770414 0.86177522 0.2697686 0.80711704 0.18463637 0.7219848
		 0.12997819 0.61471206 0.11114423 0.49579921 0.12997819 0.37688643 0.18463637 0.26961371
		 0.26976854 0.1844815 0.37704134 0.12982315 0.49595416 0.11098927 0.61486691 0.12982315
		 0.72213972 0.18448138 0.80727196 0.26961353 0.86193019 0.37688643;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  -21.35997009 -79.96226501 2.1393919 -21.46415329 -79.75779724 2.1393919
		 -21.62641525 -79.59553528 2.1393919 -21.83087921 -79.4913559 2.1393919 -22.057529449 -79.45545959 2.1393919
		 -22.2841835 -79.4913559 2.1393919 -22.48863983 -79.59553528 2.1393919 -22.65090942 -79.75779724 2.1393919
		 -22.75508881 -79.96226501 2.1393919 -22.79098892 -80.18891907 2.1393919 -22.75508881 -80.41556549 2.1393919
		 -22.65090942 -80.62002563 2.1393919 -22.48863983 -80.7822876 2.1393919 -22.2841835 -80.88647461 2.1393919
		 -22.057529449 -80.92237091 2.1393919 -21.83087921 -80.88647461 2.1393919 -21.62641525 -80.7822876 2.1393919
		 -21.46415329 -80.62002563 2.1393919 -21.35997009 -80.41556549 2.1393919 -21.32407379 -80.18891907 2.1393919;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 19 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "RtLegLeg_ball_FK_guide" -p "FM_Cam_r_hi_crura_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -7.1100568771362305 -21.561260223388672 2.1393918991088867 ;
	setAttr ".sp" -type "double3" -7.1100568771362305 -21.561260223388672 2.1393918991088867 ;
createNode mesh -n "RtLegLeg_ball_FK_guideShape" -p "RtLegLeg_ball_FK_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193001 0.61471206 0.80727184 0.7219848 0.7221396 0.80711704 0.61486673 0.86177522
		 0.49595416 0.8806091 0.3770414 0.86177522 0.2697686 0.80711704 0.18463637 0.7219848
		 0.12997819 0.61471206 0.11114423 0.49579921 0.12997819 0.37688643 0.18463637 0.26961371
		 0.26976854 0.1844815 0.37704134 0.12982315 0.49595416 0.11098927 0.61486691 0.12982315
		 0.72213972 0.18448138 0.80727196 0.26961353 0.86193019 0.37688643;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  -22.16155624 -82.43989563 2.1393919 -22.26573944 -82.23542786 2.1393919
		 -22.4280014 -82.073165894 2.1393919 -22.63246536 -81.96898651 2.1393919 -22.8591156 -81.93309021 2.1393919
		 -23.085769653 -81.96898651 2.1393919 -23.29022598 -82.073165894 2.1393919 -23.45249557 -82.23542786 2.1393919
		 -23.55667496 -82.43989563 2.1393919 -23.59257507 -82.66654968 2.1393919 -23.55667496 -82.89319611 2.1393919
		 -23.45249557 -83.09765625 2.1393919 -23.29022598 -83.25991821 2.1393919 -23.085769653 -83.36410522 2.1393919
		 -22.8591156 -83.40000153 2.1393919 -22.63246536 -83.36410522 2.1393919 -22.4280014 -83.25991821 2.1393919
		 -22.26573944 -83.09765625 2.1393919 -22.16155624 -82.89319611 2.1393919 -22.12565994 -82.66654968 2.1393919;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 19 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "RtLeg_Leg_IK_guide" -p "FM_Cam_r_hi_crura_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -4.1547689437866211 -21.074939727783203 2.1393918991088867 ;
	setAttr ".sp" -type "double3" -4.1547689437866211 -21.074939727783203 2.1393918991088867 ;
createNode mesh -n "RtLeg_Leg_IK_guideShape" -p "RtLeg_Leg_IK_guide";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 6 ".uvst[0].uvsp[0:5]" -type "float2" 0.26224762 0.11706195
		 0.19908482 0.22638434 0.072875679 0.22638434 0.0097126365 0.11706183 0.072875321
		 0.0077396352 0.19908494 0.0077396948;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 6 ".pt[0:5]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0;
	setAttr -s 6 ".vt[0:5]"  -19.064746857 -80.72689819 2.1393919 -20.74291229 -80.72689819 2.1393919
		 -21.58198929 -82.18022919 2.1393919 -20.74291611 -83.63355255 2.1393919 -19.064754486 -83.63355255 2.1393919
		 -18.22566986 -82.18022919 2.1393919;
	setAttr -s 6 ".ed[0:5]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 0 0;
	setAttr -ch 6 ".fc[0]" -type "polyFaces" 
		f 6 5 0 1 2 3 4
		mu 0 6 0 1 2 3 4 5;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "Rtleg1_bend_guide" -p "FM_Cam_r_hi_crura_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -5.2089300155639648 -3.4773902893066406 2.1393921375274658 ;
	setAttr ".sp" -type "double3" -5.2089300155639648 -3.4773902893066406 2.1393921375274658 ;
createNode mesh -n "Rtleg1_bend_guideShape" -p "Rtleg1_bend_guide";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.65625 0.84375 0.6486026
		 0.89203393 0.62640893 0.93559146 0.59184146 0.97015893 0.54828387 0.9923526 0.5 1
		 0.4517161 0.9923526 0.40815854 0.97015893 0.37359107 0.93559146 0.3513974 0.89203393
		 0.34374997 0.84375 0.3513974 0.79546607 0.37359107 0.75190854 0.40815851 0.71734107
		 0.45171607 0.69514734 0.5 0.68749994 0.54828393 0.69514734 0.59184152 0.71734101
		 0.62640899 0.75190848 0.64860266 0.79546607;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  -20.58334732 -64.46094513 2.13939214 -20.63929749 -64.35112762 2.13939214
		 -20.72644424 -64.26397705 2.13939214 -20.83625793 -64.20802307 2.13939214 -20.95799255 -64.18874359 2.13939214
		 -21.079727173 -64.20802307 2.13939214 -21.18954086 -64.26397705 2.13939214 -21.27669144 -64.35112762 2.13939214
		 -21.33264542 -64.46094513 2.13939214 -21.35192108 -64.58267212 2.13939214 -21.33264542 -64.70440674 2.13939214
		 -21.27669144 -64.81421661 2.13939214 -21.18954086 -64.90136719 2.13939214 -21.079727173 -64.95732117 2.13939214
		 -20.95799255 -64.97660828 2.13939214 -20.83625793 -64.95732117 2.13939214 -20.72644424 -64.90136719 2.13939214
		 -20.63929749 -64.81421661 2.13939214 -20.58334732 -64.70440674 2.13939214 -20.56406021 -64.58267212 2.13939214;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 19 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "Rtknee1_bend_guide" -p "FM_Cam_r_hi_crura_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -6.1717100143432617 -13.763965606689453 2.1393918991088867 ;
	setAttr ".sp" -type "double3" -6.1717100143432617 -13.763965606689453 2.1393918991088867 ;
createNode mesh -n "Rtknee1_bend_guideShape" -p "Rtknee1_bend_guide";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.65625 0.84375 0.6486026
		 0.89203393 0.62640893 0.93559146 0.59184146 0.97015893 0.54828387 0.9923526 0.5 1
		 0.4517161 0.9923526 0.40815854 0.97015893 0.37359107 0.93559146 0.3513974 0.89203393
		 0.34374997 0.84375 0.3513974 0.79546607 0.37359107 0.75190854 0.40815851 0.71734107
		 0.45171607 0.69514734 0.5 0.68749994 0.54828393 0.69514734 0.59184152 0.71734101
		 0.62640899 0.75190848 0.64860266 0.79546607;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  -21.54612732 -74.74752045 2.1393919 -21.60207748 -74.63770294 2.1393919
		 -21.68922424 -74.55055237 2.1393919 -21.79903793 -74.49459839 2.1393919 -21.92077255 -74.47531891 2.1393919
		 -22.042507172 -74.49459839 2.1393919 -22.15232086 -74.55055237 2.1393919 -22.23947144 -74.63770294 2.1393919
		 -22.29542542 -74.74752045 2.1393919 -22.31470108 -74.86924744 2.1393919 -22.29542542 -74.99098206 2.1393919
		 -22.23947144 -75.10079193 2.1393919 -22.15232086 -75.1879425 2.1393919 -22.042507172 -75.24389648 2.1393919
		 -21.92077255 -75.26318359 2.1393919 -21.79903793 -75.24389648 2.1393919 -21.68922424 -75.1879425 2.1393919
		 -21.60207748 -75.10079193 2.1393919 -21.54612732 -74.99098206 2.1393919 -21.52684021 -74.86924744 2.1393919;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 19 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "To_Feet_View" -p "FM_Cam_r_hi_crura_";
	setAttr ".v" no;
	setAttr ".rp" -type "double3" -10.254635810852051 -22.140403747558594 2.1393918991088867 ;
	setAttr ".sp" -type "double3" -10.254635810852051 -22.140403747558594 2.1393918991088867 ;
createNode mesh -n "To_Feet_ViewShape" -p "|FM_Caml_gui_guides_grp|FM_Cam_BODY_gui_guides_grp|FM_Cam_c_hi_body_|FM_Cam_r_hi_crura_|To_Feet_View";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0:1]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 46 ".uvst[0].uvsp[0:45]" -type "float2" 0.625 0.083988376
		 0.5 0.083988376 0 0 0 1 1 0.5 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
		 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr -s 46 ".vt[0:45]"  -10.23988438 -22.76768494 2.1393919 -10.23988438 -21.86595917 2.1393919
		 -10.70024204 -21.86595917 2.1393919 -11.16363239 -21.86595917 2.1393919 -9.77946949 -21.86595917 2.1393919
		 -9.31600285 -21.86595917 2.1393919 -9.19152164 -21.79497528 2.1393919 -9.35029697 -21.48336792 2.1393919
		 -9.59759617 -21.23606873 2.1393919 -9.90921116 -21.077293396 2.1393919 -10.254632 -21.022583008 2.1393919
		 -10.60005665 -21.077293396 2.1393919 -10.91167927 -21.23606873 2.1393919 -11.15897083 -21.48336792 2.1393919
		 -11.31774998 -21.79497528 2.1393919 -11.37245655 -22.14041138 2.1393919 -11.31774998 -22.48583221 2.1393919
		 -11.15897083 -22.7974472 2.1393919 -10.91167927 -23.044746399 2.1393919 -10.60005665 -23.20352173 2.1393919
		 -10.254632 -23.25823212 2.1393919 -9.90921116 -23.20352173 2.1393919 -9.59759617 -23.044746399 2.1393919
		 -9.35029697 -22.7974472 2.1393919 -9.19152164 -22.48583221 2.1393919 -9.13681126 -22.14041138 2.1393919
		 -8.94840717 -21.71599579 2.1393919 -9.14349461 -21.33311462 2.1393919 -9.44734669 -21.029266357 2.1393919
		 -9.83022022 -20.83418274 2.1393919 -10.254632 -20.76696014 2.1393919 -10.67904758 -20.83418274 2.1393919
		 -11.061928749 -21.029266357 2.1393919 -11.3657732 -21.33311462 2.1393919 -11.560853 -21.71599579 2.1393919
		 -11.6280756 -22.14041138 2.1393919 -11.560853 -22.56481934 2.1393919 -11.3657732 -22.94769287 2.1393919
		 -11.061928749 -23.25154877 2.1393919 -10.67904758 -23.44662476 2.1393919 -10.254632 -23.51384735 2.1393919
		 -9.83022022 -23.44662476 2.1393919 -9.44734669 -23.25154877 2.1393919 -9.14349461 -22.94769287 2.1393919
		 -8.9484148 -22.56481934 2.1393919 -8.88119602 -22.14041138 2.1393919;
	setAttr -s 46 ".ed[0:45]"  2 1 0 2 3 0 0 3 0 4 1 0 0 5 0 4 5 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 20 0 20 21 0 21 22 0 22 23 0 23 24 0 24 25 0 25 6 0 26 27 0 27 28 0 28 29 0
		 29 30 0 30 31 0 31 32 0 32 33 0 33 34 0 34 35 0 35 36 0 36 37 0 37 38 0 38 39 0 39 40 0
		 40 41 0 41 42 0 42 43 0 43 44 0 44 45 0 45 26 0;
	setAttr -s 2 -ch 46 ".fc[0:1]" -type "polyFaces" 
		f 6 3 -1 1 -3 4 -6
		mu 0 6 0 1 2 3 4 5
		f 20 44 45 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43
		mu 0 20 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
		h 20 -25 -24 -23 -22 -21 -20 -19 -18 -17 -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -26
		mu 0 20 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_l_hi_crura_" -p "FM_Cam_c_hi_body_";
	setAttr ".rp" -type "double3" 2.6771097183227539 -10.605884552001953 2.1393920183181763 ;
	setAttr ".sp" -type "double3" 2.6771097183227539 -10.605884552001953 2.1393920183181763 ;
createNode transform -n "LfLeg_hip_ctrl_guide" -p "FM_Cam_l_hi_crura_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 4.8405427932739258 0.99640846252441406 2.1393921375274658 ;
	setAttr ".sp" -type "double3" 4.8405427932739258 0.99640846252441406 2.1393921375274658 ;
createNode mesh -n "LfLeg_hip_ctrl_guideShape" -p "LfLeg_hip_ctrl_guide";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 21 ".uvst[0].uvsp[0:20]" -type "float2" 0.4224298 0.032137346
		 0.375 0 0.375 0.066693999 0.375 0.12903883 0.41062218 0.097380474 0.44391629 0.12903883
		 0.48090714 0.16020662 0.52869076 0.18042409 0.55576026 0.18042409 0.58541125 0.16383144
		 0.60732722 0.12903883 0.6148358 0.10255056 0.625 0.066693999 0.625 0 0.59959215 0.066693999
		 0.58412218 0.094964311 0.55576003 0.1155033 0.52869076 0.11912756 0.49323919 0.10221282
		 0.47019911 0.078049056 0.52869076 0.066693999;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 21 ".pt[0:20]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 21 ".vt[0:20]"  -11.7302475 -61.41454697 2.13939214 -12.1087513 -58.92876053 2.13939214
		 -10.11675262 -61.29114532 2.13939214 -11.28422546 -58.8032074 2.13939214 -11.11432457 -59.91906738 2.13939214
		 -10.91709137 -61.21432114 2.13939214 -9.70828438 -59.70497894 2.13939214 -11.40279579 -60.89530182 2.13939214
		 -10.89887428 -60.39064407 2.13939214 -10.62971306 -60.15098572 2.13939214 -10.4660759 -59.82036972 2.13939214
		 -11.23940468 -59.097587585 2.13939214 -10.55864906 -59.51356125 2.13939214 -10.86260223 -59.22360992 2.13939214
		 -10.57573509 -60.90692139 2.13939214 -10.21845627 -60.62327194 2.13939214 -9.8877182 -60.20611954 2.13939214
		 -9.7560463 -59.39134598 2.13939214 -10.4822731 -58.89060211 2.13939214 -10.013492584 -59.079040527 2.13939214
		 -10.82299042 -58.85346985 2.13939214;
	setAttr -s 21 ".ed[0:20]"  0 5 0 1 3 0 5 2 0 0 7 0 7 4 0 4 8 0 8 9 0
		 9 10 0 10 12 0 12 13 0 13 11 0 11 1 0 2 14 0 14 15 0 15 16 0 16 6 0 17 6 0 17 19 0
		 19 18 0 18 20 0 20 3 0;
	setAttr -ch 21 ".fc[0]" -type "polyFaces" 
		f 21 -4 0 2 12 13 14 15 -17 17 18 19 20 -2 -12 -11 -10 -9 -8 -7 -6 -5
		mu 0 21 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "LfLeg_Pole_ctrl_guide" -p "FM_Cam_l_hi_crura_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 5.2449016571044922 -8.9782676696777344 2.1393921375274658 ;
	setAttr ".sp" -type "double3" 5.2449016571044922 -8.9782676696777344 2.1393921375274658 ;
createNode mesh -n "LfLeg_Pole_ctrl_guideShape" -p "LfLeg_Pole_ctrl_guide";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 6 ".uvst[0].uvsp[0:5]" -type "float2" 0.26224762 0.11706195
		 0.19908494 0.0077396948 0.072875321 0.0077396352 0.0097126365 0.11706183 0.072875679
		 0.22638434 0.19908482 0.22638434;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 6 ".pt[0:5]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0;
	setAttr -s 6 ".vt[0:5]"  -9.6650753 -68.63022614 2.13939214 -11.34324074 -68.63022614 2.13939214
		 -12.18231964 -70.083557129 2.13939214 -11.34324455 -71.53688049 2.13939214 -9.66508102 -71.53688049 2.13939214
		 -8.82599831 -70.083557129 2.13939214;
	setAttr -s 6 ".ed[0:5]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 0 0;
	setAttr -ch 6 ".fc[0]" -type "polyFaces" 
		f 6 5 0 1 2 3 4
		mu 0 6 0 5 4 3 2 1;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "LfLeg_Switch_guide" -p "FM_Cam_l_hi_crura_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 5.2292413711547852 -18.490982055664063 2.1393918991088867 ;
	setAttr ".sp" -type "double3" 5.2292413711547852 -18.490982055664063 2.1393918991088867 ;
createNode mesh -n "LfLeg_Switch_guideShape" -p "LfLeg_Switch_guide";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 8 ".uvst[0].uvsp[0:7]" -type "float2" 0.625 0.083988376
		 0 1 1 0.5 0 1 0 0 0.625 0.25 0.5 0.25 0.625 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 8 ".pt[0:7]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 8 ".vt[0:7]"  -11.70214272 -79.59444427 2.1393919 -9.33883095 -80.16157532 2.1393919
		 -10.096078873 -80.16067505 2.1393919 -10.096754074 -80.72871399 2.1393919 -9.33816528 -79.59724426 2.1393919
		 -9.3374958 -79.032852173 2.1393919 -10.094743729 -79.031951904 2.1393919 -10.094074249 -78.46382141 2.1393919;
	setAttr -s 8 ".ed[0:7]"  2 1 0 2 3 0 0 3 0 4 1 0 6 5 0 6 7 0 0 7 0
		 4 5 0;
	setAttr -ch 8 ".fc[0]" -type "polyFaces" 
		f 8 5 -7 2 -2 0 -4 7 -5
		mu 0 8 0 1 2 3 4 5 6 7;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "LfLeg_Leg_FK_guide" -p "FM_Cam_l_hi_crura_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 0.020720005035400391 0.58365058898925781 2.1393921375274658 ;
	setAttr ".sp" -type "double3" 0.020720005035400391 0.58365058898925781 2.1393921375274658 ;
createNode mesh -n "LfLeg_Leg_FK_guideShape" -p "LfLeg_Leg_FK_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193001 0.61471206 0.80727184 0.7219848 0.7221396 0.80711704 0.61486673 0.86177522
		 0.49595416 0.8806091 0.3770414 0.86177522 0.2697686 0.80711704 0.18463637 0.7219848
		 0.12997819 0.61471206 0.11114423 0.49579921 0.12997819 0.37688643 0.18463637 0.26961371
		 0.26976854 0.1844815 0.37704134 0.12982315 0.49595416 0.11098927 0.61486691 0.12982315
		 0.72213972 0.18448138 0.80727196 0.26961353 0.86193019 0.37688643;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  -16.62575912 -60.23004913 2.13939214 -16.49172783 -59.96699524 2.13939214
		 -16.28297424 -59.75824356 2.13939214 -16.019929886 -59.62421417 2.13939214 -15.72834206 -59.57803726 2.13939214
		 -15.43675041 -59.62421417 2.13939214 -15.17371559 -59.75824356 2.13939214 -14.96495247 -59.96699524 2.13939214
		 -14.8309269 -60.23004913 2.13939214 -14.78473949 -60.52163315 2.13939214 -14.8309269 -60.81321716 2.13939214
		 -14.96495247 -61.076263428 2.13939214 -15.17371559 -61.28501892 2.13939214 -15.43675041 -61.41904831 2.13939214
		 -15.72834206 -61.46523285 2.13939214 -16.019929886 -61.41904831 2.13939214 -16.28297424 -61.28501892 2.13939214
		 -16.49172783 -61.076263428 2.13939214 -16.62575912 -60.81321716 2.13939214 -16.67194176 -60.52163315 2.13939214;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 -19 -18 -17 -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 -20
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "LfLeg_Knee_FK_guide" -p "FM_Cam_l_hi_crura_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 1.2773923873901367 -8.5901298522949219 2.1393921375274658 ;
	setAttr ".sp" -type "double3" 1.2773923873901367 -8.5901298522949219 2.1393921375274658 ;
createNode mesh -n "LfLeg_Knee_FK_guideShape" -p "LfLeg_Knee_FK_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193001 0.61471206 0.80727184 0.7219848 0.7221396 0.80711704 0.61486673 0.86177522
		 0.49595416 0.8806091 0.3770414 0.86177522 0.2697686 0.80711704 0.18463637 0.7219848
		 0.12997819 0.61471206 0.11114423 0.49579921 0.12997819 0.37688643 0.18463637 0.26961371
		 0.26976854 0.1844815 0.37704134 0.12982315 0.49595416 0.11098927 0.61486691 0.12982315
		 0.72213972 0.18448138 0.80727196 0.26961353 0.86193019 0.37688643;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  -15.16922951 -69.46876526 2.13939214 -15.065045357 -69.26429749 2.13939214
		 -14.90278339 -69.10203552 2.13939214 -14.69832039 -68.99785614 2.13939214 -14.47167015 -68.96195984 2.13939214
		 -14.2450161 -68.99785614 2.13939214 -14.040558815 -69.10203552 2.13939214 -13.87829018 -69.26429749 2.13939214
		 -13.77411175 -69.46876526 2.13939214 -13.73821068 -69.69541931 2.13939214 -13.77411175 -69.92206573 2.13939214
		 -13.87829018 -70.12652588 2.13939214 -14.040558815 -70.28878784 2.13939214 -14.2450161 -70.39297485 2.13939214
		 -14.47167015 -70.42887115 2.13939214 -14.69832039 -70.39297485 2.13939214 -14.90278339 -70.28878784 2.13939214
		 -15.065045357 -70.12652588 2.13939214 -15.16922951 -69.92206573 2.13939214 -15.20512581 -69.69541931 2.13939214;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 -19 -18 -17 -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 -20
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "LfLeg_Ankle_FK_guide" -p "FM_Cam_l_hi_crura_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 1.9332394599914551 -19.083629608154297 2.1393918991088867 ;
	setAttr ".sp" -type "double3" 1.9332394599914551 -19.083629608154297 2.1393918991088867 ;
createNode mesh -n "LfLeg_Ankle_FK_guideShape" -p "LfLeg_Ankle_FK_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193001 0.61471206 0.80727184 0.7219848 0.7221396 0.80711704 0.61486673 0.86177522
		 0.49595416 0.8806091 0.3770414 0.86177522 0.2697686 0.80711704 0.18463637 0.7219848
		 0.12997819 0.61471206 0.11114423 0.49579921 0.12997819 0.37688643 0.18463637 0.26961371
		 0.26976854 0.1844815 0.37704134 0.12982315 0.49595416 0.11098927 0.61486691 0.12982315
		 0.72213972 0.18448138 0.80727196 0.26961353 0.86193019 0.37688643;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  -14.51338387 -79.96226501 2.1393919 -14.40920067 -79.75779724 2.1393919
		 -14.24693775 -79.59553528 2.1393919 -14.0424757 -79.4913559 2.1393919 -13.81582546 -79.45545959 2.1393919
		 -13.58916855 -79.4913559 2.1393919 -13.38471413 -79.59553528 2.1393919 -13.22244263 -79.75779724 2.1393919
		 -13.11826324 -79.96226501 2.1393919 -13.082364082 -80.18891907 2.1393919 -13.11826324 -80.41556549 2.1393919
		 -13.22244263 -80.62002563 2.1393919 -13.38471413 -80.7822876 2.1393919 -13.58916855 -80.88647461 2.1393919
		 -13.81582546 -80.92237091 2.1393919 -14.0424757 -80.88647461 2.1393919 -14.24693775 -80.7822876 2.1393919
		 -14.40920067 -80.62002563 2.1393919 -14.51338387 -80.41556549 2.1393919 -14.54927826 -80.18891907 2.1393919;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 -19 -18 -17 -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 -20
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "LfLegLeg_ball_FK_guide" -p "FM_Cam_l_hi_crura_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 2.7348232269287109 -21.561260223388672 2.1393918991088867 ;
	setAttr ".sp" -type "double3" 2.7348232269287109 -21.561260223388672 2.1393918991088867 ;
createNode mesh -n "LfLegLeg_ball_FK_guideShape" -p "LfLegLeg_ball_FK_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193001 0.61471206 0.80727184 0.7219848 0.7221396 0.80711704 0.61486673 0.86177522
		 0.49595416 0.8806091 0.3770414 0.86177522 0.2697686 0.80711704 0.18463637 0.7219848
		 0.12997819 0.61471206 0.11114423 0.49579921 0.12997819 0.37688643 0.18463637 0.26961371
		 0.26976854 0.1844815 0.37704134 0.12982315 0.49595416 0.11098927 0.61486691 0.12982315
		 0.72213972 0.18448138 0.80727196 0.26961353 0.86193019 0.37688643;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  -13.71179867 -82.43989563 2.1393919 -13.60761452 -82.23542786 2.1393919
		 -13.44535255 -82.073165894 2.1393919 -13.2408886 -81.96898651 2.1393919 -13.01423645 -81.93309021 2.1393919
		 -12.7875824 -81.96898651 2.1393919 -12.58312798 -82.073165894 2.1393919 -12.42085934 -82.23542786 2.1393919
		 -12.316679 -82.43989563 2.1393919 -12.28078079 -82.66654968 2.1393919 -12.316679 -82.89319611 2.1393919
		 -12.42085934 -83.09765625 2.1393919 -12.58312798 -83.25991821 2.1393919 -12.7875824 -83.36410522 2.1393919
		 -13.01423645 -83.40000153 2.1393919 -13.2408886 -83.36410522 2.1393919 -13.44535255 -83.25991821 2.1393919
		 -13.60761452 -83.09765625 2.1393919 -13.71179867 -82.89319611 2.1393919 -13.74769402 -82.66654968 2.1393919;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 -19 -18 -17 -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 -20
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "LfLeg_Leg_IK_guide" -p "FM_Cam_l_hi_crura_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -0.22046375274658203 -21.074939727783203 2.1393918991088867 ;
	setAttr ".sp" -type "double3" -0.22046375274658203 -21.074939727783203 2.1393918991088867 ;
createNode mesh -n "LfLeg_Leg_IK_guideShape" -p "LfLeg_Leg_IK_guide";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 6 ".uvst[0].uvsp[0:5]" -type "float2" 0.26224762 0.11706195
		 0.19908494 0.0077396948 0.072875321 0.0077396352 0.0097126365 0.11706183 0.072875679
		 0.22638434 0.19908482 0.22638434;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 6 ".pt[0:5]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0;
	setAttr -s 6 ".vt[0:5]"  -15.13044167 -80.72689819 2.1393919 -16.80860901 -80.72689819 2.1393919
		 -17.6476841 -82.18022919 2.1393919 -16.80861282 -83.63355255 2.1393919 -15.13045025 -83.63355255 2.1393919
		 -14.29136467 -82.18022919 2.1393919;
	setAttr -s 6 ".ed[0:5]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 0 0;
	setAttr -ch 6 ".fc[0]" -type "polyFaces" 
		f 6 5 0 1 2 3 4
		mu 0 6 0 5 4 3 2 1;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "Lfleg1_bend_guide" -p "FM_Cam_l_hi_crura_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 0.83369731903076172 -3.4773902893066406 2.1393921375274658 ;
	setAttr ".sp" -type "double3" 0.83369731903076172 -3.4773902893066406 2.1393921375274658 ;
createNode mesh -n "Lfleg1_bend_guideShape" -p "Lfleg1_bend_guide";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.65625 0.84375 0.64860266
		 0.79546607 0.62640899 0.75190848 0.59184152 0.71734101 0.54828393 0.69514734 0.5
		 0.68749994 0.45171607 0.69514734 0.40815851 0.71734107 0.37359107 0.75190854 0.3513974
		 0.79546607 0.34374997 0.84375 0.3513974 0.89203393 0.37359107 0.93559146 0.40815854
		 0.97015893 0.4517161 0.9923526 0.5 1 0.54828387 0.9923526 0.59184146 0.97015893 0.62640893
		 0.93559146 0.6486026 0.89203393;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  -15.29000664 -64.46094513 2.13939214 -15.23405647 -64.35112762 2.13939214
		 -15.14690971 -64.26397705 2.13939214 -15.037096024 -64.20802307 2.13939214 -14.9153614 -64.18874359 2.13939214
		 -14.79362679 -64.20802307 2.13939214 -14.6838131 -64.26397705 2.13939214 -14.59666348 -64.35112762 2.13939214
		 -14.54070759 -64.46094513 2.13939214 -14.52143288 -64.58267212 2.13939214 -14.54070759 -64.70440674 2.13939214
		 -14.59666348 -64.81421661 2.13939214 -14.6838131 -64.90136719 2.13939214 -14.79362679 -64.95732117 2.13939214
		 -14.9153614 -64.97660828 2.13939214 -15.037096024 -64.95732117 2.13939214 -15.14690971 -64.90136719 2.13939214
		 -15.23405647 -64.81421661 2.13939214 -15.29000664 -64.70440674 2.13939214 -15.30929375 -64.58267212 2.13939214;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 -19 -18 -17 -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 -20
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "Lfknee1_bend_guide" -p "FM_Cam_l_hi_crura_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 1.7964773178100586 -13.763965606689453 2.1393918991088867 ;
	setAttr ".sp" -type "double3" 1.7964773178100586 -13.763965606689453 2.1393918991088867 ;
createNode mesh -n "Lfknee1_bend_guideShape" -p "Lfknee1_bend_guide";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.65625 0.84375 0.64860266
		 0.79546607 0.62640899 0.75190848 0.59184152 0.71734101 0.54828393 0.69514734 0.5
		 0.68749994 0.45171607 0.69514734 0.40815851 0.71734107 0.37359107 0.75190854 0.3513974
		 0.79546607 0.34374997 0.84375 0.3513974 0.89203393 0.37359107 0.93559146 0.40815854
		 0.97015893 0.4517161 0.9923526 0.5 1 0.54828387 0.9923526 0.59184146 0.97015893 0.62640893
		 0.93559146 0.6486026 0.89203393;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  -14.32722664 -74.74752045 2.1393919 -14.27127457 -74.63770294 2.1393919
		 -14.18412781 -74.55055237 2.1393919 -14.074314117 -74.49459839 2.1393919 -13.95258045 -74.47531891 2.1393919
		 -13.83084679 -74.49459839 2.1393919 -13.7210331 -74.55055237 2.1393919 -13.63388252 -74.63770294 2.1393919
		 -13.57792664 -74.74752045 2.1393919 -13.55865288 -74.86924744 2.1393919 -13.57792664 -74.99098206 2.1393919
		 -13.63388252 -75.10079193 2.1393919 -13.7210331 -75.1879425 2.1393919 -13.83084679 -75.24389648 2.1393919
		 -13.95258045 -75.26318359 2.1393919 -14.074314117 -75.24389648 2.1393919 -14.18412781 -75.1879425 2.1393919
		 -14.27127457 -75.10079193 2.1393919 -14.32722664 -74.99098206 2.1393919 -14.34651375 -74.86924744 2.1393919;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 -19 -18 -17 -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 -20
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "LfLeg_foot_guide" -p "FM_Cam_l_hi_crura_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -0.21780538558959961 -18.837909698486328 2.1393918991088867 ;
	setAttr ".sp" -type "double3" -0.21780538558959961 -18.837909698486328 2.1393918991088867 ;
createNode mesh -n "LfLeg_foot_guideShape" -p "LfLeg_foot_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.13084226846694946 0.18921643011594957 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.093077615 0.18921643
		 0.094925962 0.20088637 0.10029005 0.21141392 0.10864477 0.2197687 0.11917239 0.22513276
		 0.13084228 0.22698107 0.14251217 0.22513276 0.15303977 0.2197687 0.16139452 0.21141392
		 0.16675858 0.20088637 0.16860692 0.18921643 0.16675858 0.1775465 0.16139452 0.16701895
		 0.15303977 0.1586642 0.14251222 0.15330011 0.13084228 0.1514518 0.11917234 0.15330011
		 0.10864477 0.1586642 0.10029005 0.16701892 0.094925962 0.1775465;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  13.848919 61.269482 0 13.811446 
		61.195938 0 13.753082 61.137577 0 13.679541 61.100105 0 13.598018 61.087193 0 13.516493 
		61.100105 0 13.442953 61.137577 0 13.384586 61.195938 0 13.347115 61.269482 0 13.334202 
		61.351006 0 13.347115 61.432529 0 13.384586 61.506069 0 13.442953 61.564434 0 13.516493 
		61.601906 0 13.598018 61.614819 0 13.679541 61.601906 0 13.753082 61.564434 0 13.811446 
		61.506069 0 13.848919 61.432529 0 13.86183 61.351006 0;
	setAttr -s 20 ".vt[0:19]"  -14.51338387 -79.96226501 2.1393919 -14.40920067 -79.75779724 2.1393919
		 -14.24693775 -79.59553528 2.1393919 -14.0424757 -79.4913559 2.1393919 -13.81582546 -79.45545959 2.1393919
		 -13.58916855 -79.4913559 2.1393919 -13.38471413 -79.59553528 2.1393919 -13.22244263 -79.75779724 2.1393919
		 -13.11826324 -79.96226501 2.1393919 -13.082364082 -80.18891907 2.1393919 -13.11826324 -80.41556549 2.1393919
		 -13.22244263 -80.62002563 2.1393919 -13.38471413 -80.7822876 2.1393919 -13.58916855 -80.88647461 2.1393919
		 -13.81582546 -80.92237091 2.1393919 -14.0424757 -80.88647461 2.1393919 -14.24693775 -80.7822876 2.1393919
		 -14.40920067 -80.62002563 2.1393919 -14.51338387 -80.41556549 2.1393919 -14.54927826 -80.18891907 2.1393919;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 -19 -18 -17 -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 -20
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "RtLeg_foot_guide" -p "FM_Cam_l_hi_crura_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -4.1881980895996094 -18.837909698486328 2.1393918991088867 ;
	setAttr ".sp" -type "double3" -4.1881980895996094 -18.837909698486328 2.1393918991088867 ;
createNode mesh -n "RtLeg_foot_guideShape" -p "RtLeg_foot_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.13088877871632576 0.19243142008781433 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.16162516 0.19243142
		 0.1601208 0.20192949 0.15575503 0.21049784 0.14895517 0.2172977 0.14038683 0.22166346
		 0.13088877 0.22316782 0.12139072 0.22166346 0.11282238 0.2172977 0.10602251 0.21049784
		 0.10165673 0.20192949 0.1001524 0.19243142 0.10165673 0.18293336 0.10602251 0.17436503
		 0.11282238 0.16756517 0.12139072 0.16319938 0.13088877 0.16169502 0.14038683 0.16319938
		 0.14895517 0.16756517 0.15575503 0.17436503 0.16012083 0.18293336;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  9.8785257 61.269482 -1.3322676e-015 
		9.841053 61.195938 -1.3322676e-015 9.7826891 61.137577 -1.3322676e-015 9.7091465 
		61.100105 -1.3322676e-015 9.6276245 61.087193 -1.3322676e-015 9.5460987 61.100105 
		-1.3322676e-015 9.4725599 61.137577 -1.3322676e-015 9.4141932 61.195938 -1.3322676e-015 
		9.3767214 61.269482 -1.3322676e-015 9.3638096 61.351006 -1.3322676e-015 9.3767214 
		61.432529 -1.3322676e-015 9.4141932 61.506069 -1.3322676e-015 9.4725599 61.564434 
		-1.3322676e-015 9.5460987 61.601906 -1.3322676e-015 9.6276245 61.614819 -1.3322676e-015 
		9.7091465 61.601906 -1.3322676e-015 9.7826891 61.564434 -1.3322676e-015 9.841053 
		61.506069 -1.3322676e-015 9.8785257 61.432529 -1.3322676e-015 9.8914366 61.351006 
		-1.3322676e-015;
	setAttr -s 20 ".vt[0:19]"  -14.51338387 -79.96226501 2.1393919 -14.40920067 -79.75779724 2.1393919
		 -14.24693775 -79.59553528 2.1393919 -14.0424757 -79.4913559 2.1393919 -13.81582546 -79.45545959 2.1393919
		 -13.58916855 -79.4913559 2.1393919 -13.38471413 -79.59553528 2.1393919 -13.22244263 -79.75779724 2.1393919
		 -13.11826324 -79.96226501 2.1393919 -13.082364082 -80.18891907 2.1393919 -13.11826324 -80.41556549 2.1393919
		 -13.22244263 -80.62002563 2.1393919 -13.38471413 -80.7822876 2.1393919 -13.58916855 -80.88647461 2.1393919
		 -13.81582546 -80.92237091 2.1393919 -14.0424757 -80.88647461 2.1393919 -14.24693775 -80.7822876 2.1393919
		 -14.40920067 -80.62002563 2.1393919 -14.51338387 -80.41556549 2.1393919 -14.54927826 -80.18891907 2.1393919;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 -19 -18 -17 -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 -20
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "To_Feet_View" -p "FM_Cam_l_hi_crura_";
	setAttr ".v" no;
	setAttr ".rp" -type "double3" 5.8794031143188477 -22.140403747558594 2.1393918991088867 ;
	setAttr ".sp" -type "double3" 5.8794031143188477 -22.140403747558594 2.1393918991088867 ;
createNode mesh -n "To_Feet_ViewShape" -p "|FM_Caml_gui_guides_grp|FM_Cam_BODY_gui_guides_grp|FM_Cam_c_hi_body_|FM_Cam_l_hi_crura_|To_Feet_View";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0:1]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 46 ".uvst[0].uvsp[0:45]" -type "float2" 0.625 0.083988376
		 0 1 1 0.5 0 1 0 0 0.5 0.083988376 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
		 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr -s 46 ".vt[0:45]"  5.86465359 -22.76768494 2.1393919 5.86465359 -21.86595917 2.1393919
		 6.32501125 -21.86595917 2.1393919 6.78840351 -21.86595917 2.1393919 5.40423679 -21.86595917 2.1393919
		 4.94077015 -21.86595917 2.1393919 4.81628704 -21.79497528 2.1393919 4.97506428 -21.48336792 2.1393919
		 5.22236729 -21.23606873 2.1393919 5.53398037 -21.077293396 2.1393919 5.87940311 -21.022583008 2.1393919
		 6.22482586 -21.077293396 2.1393919 6.53644848 -21.23606873 2.1393919 6.78373623 -21.48336792 2.1393919
		 6.94251728 -21.79497528 2.1393919 6.99722576 -22.14041138 2.1393919 6.94251728 -22.48583221 2.1393919
		 6.78373623 -22.7974472 2.1393919 6.53644848 -23.044746399 2.1393919 6.22482586 -23.20352173 2.1393919
		 5.87940311 -23.25823212 2.1393919 5.53398037 -23.20352173 2.1393919 5.22236729 -23.044746399 2.1393919
		 4.97506428 -22.7974472 2.1393919 4.81628704 -22.48583221 2.1393919 4.76157665 -22.14041138 2.1393919
		 4.57317257 -21.71599579 2.1393919 4.76826191 -21.33311462 2.1393919 5.072112083 -21.029266357 2.1393919
		 5.45498753 -20.83418274 2.1393919 5.87940311 -20.76696014 2.1393919 6.30381298 -20.83418274 2.1393919
		 6.68669796 -21.029266357 2.1393919 6.9905405 -21.33311462 2.1393919 7.18562412 -21.71599579 2.1393919
		 7.2528429 -22.14041138 2.1393919 7.18562412 -22.56481934 2.1393919 6.9905405 -22.94769287 2.1393919
		 6.68669796 -23.25154877 2.1393919 6.30381298 -23.44662476 2.1393919 5.87940311 -23.51384735 2.1393919
		 5.45498753 -23.44662476 2.1393919 5.072112083 -23.25154877 2.1393919 4.76826191 -22.94769287 2.1393919
		 4.57318401 -22.56481934 2.1393919 4.50596333 -22.14041138 2.1393919;
	setAttr -s 46 ".ed[0:45]"  2 1 0 2 3 0 0 3 0 4 1 0 0 5 0 4 5 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 20 0 20 21 0 21 22 0 22 23 0 23 24 0 24 25 0 25 6 0 26 27 0 27 28 0 28 29 0
		 29 30 0 30 31 0 31 32 0 32 33 0 33 34 0 34 35 0 35 36 0 36 37 0 37 38 0 38 39 0 39 40 0
		 40 41 0 41 42 0 42 43 0 43 44 0 44 45 0 45 26 0;
	setAttr -s 2 -ch 46 ".fc[0:1]" -type "polyFaces" 
		f 6 5 -5 2 -2 0 -4
		mu 0 6 0 1 2 3 4 5
		f 20 -44 -43 -42 -41 -40 -39 -38 -37 -36 -35 -34 -33 -32 -31 -30 -29 -28 -27 -46 -45
		mu 0 20 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
		h 20 25 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
		mu 0 20 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "FM_Cam_c_hi_life_" -p "FM_Cam_c_hi_body_";
	setAttr ".rp" -type "double3" -2.1876201629638672 -2.9261531829833984 2.3219918012619019 ;
	setAttr ".sp" -type "double3" -2.1876201629638672 -2.9261531829833984 2.3219918012619019 ;
createNode transform -n "root_waist_ikCtrl_guide" -p "FM_Cam_c_hi_life_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -2.1876153945922852 5.2616233825683594 2.5045914649963379 ;
	setAttr ".sp" -type "double3" -2.1876153945922852 5.2616233825683594 2.5045914649963379 ;
createNode mesh -n "root_waist_ikCtrl_guideShape" -p "root_waist_ikCtrl_guide";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 6 ".uvst[0].uvsp[0:5]" -type "float2" 0.26224762 0.11706195
		 0.19908482 0.22638434 0.072875679 0.22638434 0.0097126365 0.11706183 0.072875321
		 0.0077396352 0.19908494 0.0077396948;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 6 ".pt[0:5]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0;
	setAttr -s 6 ".vt[0:5]"  -16.98741913 -54.19951248 2.50459146 -18.88592911 -54.19951248 2.50459146
		 -19.83517838 -55.84366989 2.50459146 -18.88593292 -57.48781204 2.50459146 -16.98742676 -57.48781204 2.50459146
		 -16.038173676 -55.84366989 2.50459146;
	setAttr -s 6 ".ed[0:5]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 0 0;
	setAttr -ch 6 ".fc[0]" -type "polyFaces" 
		f 6 5 0 1 2 3 4
		mu 0 6 0 1 2 3 4 5;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "mid_waist_ikCtrl_guide" -p "FM_Cam_c_hi_life_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -2.1876134872436523 9.8772850036621094 2.504591703414917 ;
	setAttr ".sp" -type "double3" -2.1876134872436523 9.8772850036621094 2.504591703414917 ;
createNode mesh -n "mid_waist_ikCtrl_guideShape" -p "mid_waist_ikCtrl_guide";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 6 ".uvst[0].uvsp[0:5]" -type "float2" 0.26224762 0.11706195
		 0.19908482 0.22638434 0.072875679 0.22638434 0.0097126365 0.11706183 0.072875321
		 0.0077396352 0.19908494 0.0077396948;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 6 ".pt[0:5]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0;
	setAttr -s 6 ".vt[0:5]"  -17.39790344 -50.29483032 2.5045917 -18.47544098 -50.29483032 2.5045917
		 -19.014209747 -51.22800064 2.5045917 -18.47544479 -52.16117096 2.5045917 -17.39790726 -52.16117096 2.5045917
		 -16.85913849 -51.22800064 2.5045917;
	setAttr -s 6 ".ed[0:5]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 0 0;
	setAttr -ch 6 ".fc[0]" -type "polyFaces" 
		f 6 5 0 1 2 3 4
		mu 0 6 0 1 2 3 4 5;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "waist_FK1_ctrl_guide" -p "FM_Cam_c_hi_life_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -2.187617301940918 8.022003173828125 2.5045915842056274 ;
	setAttr ".sp" -type "double3" -2.187617301940918 8.022003173828125 2.5045915842056274 ;
createNode mesh -n "waist_FK1_ctrl_guideShape" -p "waist_FK1_ctrl_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193001 0.61471206 0.80727184 0.7219848 0.7221396 0.80711704 0.61486673 0.86177522
		 0.49595416 0.8806091 0.3770414 0.86177522 0.2697686 0.80711704 0.18463637 0.7219848
		 0.12997819 0.61471206 0.11114423 0.49579921 0.12997819 0.37688643 0.18463637 0.26961371
		 0.26976854 0.1844815 0.37704134 0.12982315 0.49595416 0.11098927 0.61486691 0.12982315
		 0.72213972 0.18448138 0.80727196 0.26961353 0.86193019 0.37688643;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  -17.23911667 -52.85663605 2.5045917 -17.34329987 -52.65216446 2.5045917
		 -17.50556183 -52.4899025 2.5045917 -17.71002579 -52.38572311 2.5045917 -17.93667603 -52.34982681 2.5045917
		 -18.16333008 -52.38572311 2.5045917 -18.36778641 -52.4899025 2.5045917 -18.530056 -52.65216446 2.5045917
		 -18.63423538 -52.85663605 2.50459146 -18.6701355 -53.083282471 2.50459146 -18.63423538 -53.30992889 2.50459146
		 -18.530056 -53.51439285 2.50459146 -18.36778641 -53.67665863 2.50459146 -18.16333008 -53.78084183 2.50459146
		 -17.93667603 -53.81673813 2.50459146 -17.71002579 -53.78084183 2.50459146 -17.50556183 -53.67665863 2.50459146
		 -17.34329987 -53.51439285 2.50459146 -17.23911667 -53.30992889 2.50459146 -17.20322037 -53.083282471 2.50459146;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 19 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "waist_FK2_ctrl_guide" -p "FM_Cam_c_hi_life_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -2.187617301940918 11.823139190673828 2.504591703414917 ;
	setAttr ".sp" -type "double3" -2.187617301940918 11.823139190673828 2.504591703414917 ;
createNode mesh -n "waist_FK2_ctrl_guideShape" -p "waist_FK2_ctrl_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193001 0.61471206 0.80727184 0.7219848 0.7221396 0.80711704 0.61486673 0.86177522
		 0.49595416 0.8806091 0.3770414 0.86177522 0.2697686 0.80711704 0.18463637 0.7219848
		 0.12997819 0.61471206 0.11114423 0.49579921 0.12997819 0.37688643 0.18463637 0.26961371
		 0.26976854 0.1844815 0.37704134 0.12982315 0.49595416 0.11098927 0.61486691 0.12982315
		 0.72213972 0.18448138 0.80727196 0.26961353 0.86193019 0.37688643;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  -17.23911667 -49.055500031 2.5045917 -17.34329987 -48.85102844 2.5045917
		 -17.50556183 -48.68876648 2.5045917 -17.71002579 -48.5845871 2.5045917 -17.93667603 -48.5486908 2.5045917
		 -18.16333008 -48.5845871 2.5045917 -18.36778641 -48.68876648 2.5045917 -18.530056 -48.85102844 2.5045917
		 -18.63423538 -49.055500031 2.5045917 -18.6701355 -49.28214645 2.5045917 -18.63423538 -49.50879288 2.5045917
		 -18.530056 -49.71325684 2.5045917 -18.36778641 -49.87552261 2.5045917 -18.16333008 -49.97970581 2.5045917
		 -17.93667603 -50.015602112 2.5045917 -17.71002579 -49.97970581 2.5045917 -17.50556183 -49.87552261 2.5045917
		 -17.34329987 -49.71325684 2.5045917 -17.23911667 -49.50879288 2.5045917 -17.20322037 -49.28214645 2.5045917;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 19 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "neck_FK_ctrl_guide" -p "FM_Cam_c_hi_life_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -2.187617301940918 15.787181854248047 2.504591703414917 ;
	setAttr ".sp" -type "double3" -2.187617301940918 15.787181854248047 2.504591703414917 ;
createNode mesh -n "neck_FK_ctrl_guideShape" -p "neck_FK_ctrl_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193001 0.61471206 0.80727184 0.7219848 0.7221396 0.80711704 0.61486673 0.86177522
		 0.49595416 0.8806091 0.3770414 0.86177522 0.2697686 0.80711704 0.18463637 0.7219848
		 0.12997819 0.61471206 0.11114423 0.49579921 0.12997819 0.37688643 0.18463637 0.26961371
		 0.26976854 0.1844815 0.37704134 0.12982315 0.49595416 0.11098927 0.61486691 0.12982315
		 0.72213972 0.18448138 0.80727196 0.26961353 0.86193019 0.37688643;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  -17.23911667 -45.091457367 2.5045917 -17.34329987 -44.88698578 2.5045917
		 -17.50556183 -44.72472382 2.5045917 -17.71002579 -44.62054443 2.5045917 -17.93667603 -44.58464813 2.5045917
		 -18.16333008 -44.62054443 2.5045917 -18.36778641 -44.72472382 2.5045917 -18.530056 -44.88698578 2.5045917
		 -18.63423538 -45.091457367 2.5045917 -18.6701355 -45.31810379 2.5045917 -18.63423538 -45.54475021 2.5045917
		 -18.530056 -45.74921417 2.5045917 -18.36778641 -45.91147995 2.5045917 -18.16333008 -46.015663147 2.5045917
		 -17.93667603 -46.051559448 2.5045917 -17.71002579 -46.015663147 2.5045917 -17.50556183 -45.91147995 2.5045917
		 -17.34329987 -45.74921417 2.5045917 -17.23911667 -45.54475021 2.5045917 -17.20322037 -45.31810379 2.5045917;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 19 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "top_waist_ikCtrl_guide" -p "FM_Cam_c_hi_life_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -2.1876134872436523 13.787025451660156 2.504591703414917 ;
	setAttr ".sp" -type "double3" -2.1876134872436523 13.787025451660156 2.504591703414917 ;
createNode mesh -n "top_waist_ikCtrl_guideShape" -p "top_waist_ikCtrl_guide";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 6 ".uvst[0].uvsp[0:5]" -type "float2" 0.26224762 0.11706195
		 0.19908482 0.22638434 0.072875679 0.22638434 0.0097126365 0.11706183 0.072875321
		 0.0077396352 0.19908494 0.0077396948;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 6 ".pt[0:5]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0;
	setAttr -s 6 ".vt[0:5]"  -17.39790344 -46.38508987 2.5045917 -18.47544098 -46.38508987 2.5045917
		 -19.014209747 -47.31826019 2.5045917 -18.47544479 -48.25143051 2.5045917 -17.39790726 -48.25143051 2.5045917
		 -16.85913849 -47.31826019 2.5045917;
	setAttr -s 6 ".ed[0:5]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 0 0;
	setAttr -ch 6 ".fc[0]" -type "polyFaces" 
		f 6 5 0 1 2 3 4
		mu 0 6 0 1 2 3 4 5;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "head_ctrl_guide" -p "FM_Cam_c_hi_life_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -2.1876153945922852 19.718935012817383 2.1393923759460449 ;
	setAttr ".sp" -type "double3" -2.1876153945922852 19.718935012817383 2.1393923759460449 ;
createNode mesh -n "head_ctrl_guideShape" -p "head_ctrl_guide";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.49595405597541053 0.49579916243414279 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.88076389 0.49579921
		 0.86193001 0.61471206 0.80727184 0.7219848 0.7221396 0.80711704 0.61486673 0.86177522
		 0.49595416 0.8806091 0.3770414 0.86177522 0.2697686 0.80711704 0.18463637 0.7219848
		 0.12997819 0.61471206 0.11114423 0.49579921 0.12997819 0.37688643 0.18463637 0.26961371
		 0.26976854 0.1844815 0.37704134 0.12982315 0.49595416 0.11098927 0.61486691 0.12982315
		 0.72213972 0.18448138 0.80727196 0.26961353 0.86193019 0.37688643;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  -16.82162476 -41.024055481 2.13939238 -16.98815918 -40.69721222 2.13939238
		 -17.24753952 -40.43783188 2.13939238 -17.57437515 -40.27130127 2.13939238 -17.93667603 -40.21392441 2.13939238
		 -18.2989769 -40.27130127 2.13939238 -18.6258049 -40.43783188 2.13939238 -18.88518906 -40.69721222 2.13939238
		 -19.051719666 -41.024055481 2.13939238 -19.10910797 -41.38634872 2.13939238 -19.051719666 -41.74864578 2.13939238
		 -18.88518906 -42.075481415 2.13939238 -18.6258049 -42.33486176 2.13939238 -18.2989769 -42.50139618 2.13939238
		 -17.93667603 -42.55877686 2.13939238 -17.57437515 -42.50139618 2.13939238 -17.24753952 -42.33486176 2.13939238
		 -16.98815918 -42.075481415 2.13939238 -16.82162476 -41.74864578 2.13939238 -16.76424408 -41.38634872 2.13939238;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 19 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "waist_Ctrl_guide" -p "FM_Cam_c_hi_life_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -2.1876168251037598 3.4931392669677734 2.1393921375274658 ;
	setAttr ".sp" -type "double3" -2.1876168251037598 3.4931392669677734 2.1393921375274658 ;
createNode mesh -n "waist_Ctrl_guideShape" -p "waist_Ctrl_guide";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.65625 0.84375 0.6486026
		 0.89203393 0.62640893 0.93559146 0.59184146 0.97015893 0.54828387 0.9923526 0.5 1
		 0.4517161 0.9923526 0.40815854 0.97015893 0.37359107 0.93559146 0.3513974 0.89203393
		 0.34374997 0.84375 0.3513974 0.79546607 0.37359107 0.75190854 0.40815851 0.71734107
		 0.45171607 0.69514734 0.5 0.68749994 0.54828393 0.69514734 0.59184152 0.71734101
		 0.62640899 0.75190848 0.64860266 0.79546607;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  -10.76477718 -57.37049103 2.13939214 -11.8358984 -57.15248489 2.13939214
		 -13.50419903 -56.97947311 2.13939214 -15.60638714 -56.86839294 2.13939214 -17.93667603 -56.83012009 2.13939214
		 -20.26696396 -56.86839294 2.13939214 -22.36914825 -56.97947311 2.13939214 -24.037452698 -57.15248489 2.13939214
		 -25.10856247 -57.37049103 2.13939214 -25.47764969 -57.61214828 2.13939214 -25.10856247 -57.85380173 2.13939214
		 -24.037452698 -58.071807861 2.13939214 -22.36914444 -58.24481964 2.13939214 -20.26696396 -58.35590363 2.13939214
		 -17.93667603 -58.39417267 2.13939214 -15.60638714 -58.35590363 2.13939214 -13.50419903 -58.24481964 2.13939214
		 -11.8358984 -58.071807861 2.13939214 -10.76478863 -57.85380173 2.13939214 -10.39570522 -57.61214828 2.13939214;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 19 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "Character_guide" -p "FM_Cam_c_hi_life_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -2.1876130104064941 -24.013534545898438 2.1393918991088867 ;
	setAttr ".sp" -type "double3" -2.1876130104064941 -24.013534545898438 2.1393918991088867 ;
createNode mesh -n "Character_guideShape" -p "Character_guide";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 20 ".uvst[0].uvsp[0:19]" -type "float2" 0.65625 0.84375 0.6486026
		 0.89203393 0.62640893 0.93559146 0.59184146 0.97015893 0.54828387 0.9923526 0.5 1
		 0.4517161 0.9923526 0.40815854 0.97015893 0.37359107 0.93559146 0.3513974 0.89203393
		 0.34374997 0.84375 0.3513974 0.79546607 0.37359107 0.75190854 0.40815851 0.71734107
		 0.45171607 0.69514734 0.5 0.68749994 0.54828393 0.69514734 0.59184152 0.71734101
		 0.62640899 0.75190848 0.64860266 0.79546607;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 20 ".pt[0:19]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0;
	setAttr -s 20 ".vt[0:19]"  -10.78562832 -84.90914917 2.1393919 -11.85363293 -84.71999359 2.1393919
		 -13.51708126 -84.56988525 2.1393919 -15.61315441 -84.47351074 2.1393919 -17.93667221 -84.44029999 2.1393919
		 -20.26018906 -84.47351074 2.1393919 -22.35626221 -84.56988525 2.1393919 -24.019710541 -84.71999359 2.1393919
		 -25.087715149 -84.90914917 2.1393919 -25.45572281 -85.11882019 2.1393919 -25.087715149 -85.32849121 2.1393919
		 -24.019710541 -85.51764679 2.1393919 -22.35626221 -85.66775513 2.1393919 -20.26018906 -85.76412964 2.1393919
		 -17.93667221 -85.79734039 2.1393919 -15.61316204 -85.76412964 2.1393919 -13.51708508 -85.66775513 2.1393919
		 -11.85363293 -85.51764679 2.1393919 -10.78562832 -85.32849121 2.1393919 -10.41762447 -85.11882019 2.1393919;
	setAttr -s 20 ".ed[0:19]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0;
	setAttr -ch 20 ".fc[0]" -type "polyFaces" 
		f 20 19 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		mu 0 20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "Master_guide" -p "FM_Cam_c_hi_life_";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -2.1876201629638672 -26.080612182617187 2.1393918991088867 ;
	setAttr ".sp" -type "double3" -2.1876201629638672 -26.080612182617187 2.1393918991088867 ;
createNode mesh -n "Master_guideShape" -p "Master_guide";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 18 ".uvst[0].uvsp[0:17]" -type "float2" 0.65625 0.84375 0.6486026
		 0.89203393 0.62640893 0.93559146 0.59184146 0.97015893 0.54828387 0.9923526 0.54828393
		 0.69514734 0.59184152 0.71734101 0.62640899 0.75190848 0.64860266 0.79546607 0.4517161
		 0.9923526 0.40815854 0.97015893 0.37359107 0.93559146 0.3513974 0.89203393 0.34374997
		 0.84375 0.3513974 0.79546607 0.37359107 0.75190854 0.40815851 0.71734107 0.45171607
		 0.69514734;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".lev" 0;
	setAttr ".rsl" 0;
	setAttr -s 18 ".pt[0:17]" -type "float3"  15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 61.105286 0 15.749061 
		61.105286 0;
	setAttr -s 18 ".vt[0:17]"  -2.44216061 -86.97045898 2.1393919 -4.75625134 -86.77610779 2.1393919
		 -8.36054134 -86.62187195 2.1393919 -12.90220547 -86.52284241 2.1393919 -22.97115326 -86.52284241 2.1393919
		 -27.51281357 -86.62187195 2.1393919 -31.11710358 -86.77610779 2.1393919 -33.43119431 -86.97045898 2.1393919
		 -34.22858047 -87.18589783 2.1393919 -33.43119431 -87.40133667 2.1393919 -31.11710358 -87.59568787 2.1393919
		 -27.51281357 -87.74992371 2.1393919 -22.97114944 -87.84895325 2.1393919 -12.90220547 -87.84895325 2.1393919
		 -8.36054897 -87.74992371 2.1393919 -4.75625515 -87.59568787 2.1393919 -2.44216442 -87.40133667 2.1393919
		 -1.64478207 -87.18589783 2.1393919;
	setAttr -s 18 ".ed[0:17]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 0 0;
	setAttr -ch 18 ".fc[0]" -type "polyFaces" 
		f 18 12 13 14 15 16 17 0 1 2 3 4 5 6 7 8 9 10 11
		mu 0 18 17 5 6 7 8 0 1 2 3 4 9 10 11 12 13 14 15 16;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dr" 1;
createNode transform -n "FM_BODY_CAM_GRP" -p "FM_Cam_BODY_gui_guides_grp";
	setAttr ".v" no;
	setAttr ".rp" -type "double3" 15.749060374460042 0 -2.1019476964872256e-045 ;
	setAttr ".sp" -type "double3" 15.749060374460042 0 -2.1019476964872256e-045 ;
createNode transform -n "FM_BODY_CAM" -p "FM_BODY_CAM_GRP";
	setAttr ".t" -type "double3" -2.2109562645852794 -0.073235331648283053 13.591253403945958 ;
	setAttr ".s" -type "double3" 1 1.0000000000000007 1.0000000000000007 ;
	setAttr ".rp" -type "double3" -3.5527136788005009e-015 8.8817841970012582e-016 -0.16009716521941908 ;
	setAttr ".sp" -type "double3" -3.5527136788005009e-015 8.8817841970012523e-016 -0.16009716521941897 ;
	setAttr ".spt" -type "double3" 0 5.9164567891575929e-031 -1.1102230246251573e-016 ;
createNode camera -n "FM_BODY_CAMShape" -p "FM_BODY_CAM";
	setAttr -k off ".v";
	setAttr ".rnd" no;
	setAttr ".cap" -type "double2" 1.4173 0.9449 ;
	setAttr -l on ".ff";
	setAttr ".ow" 48.909571885352428;
	setAttr ".imn" -type "string" "camera1";
	setAttr ".den" -type "string" "camera1_depth";
	setAttr ".man" -type "string" "camera1_mask";
	setAttr ".o" yes;
createNode transform -s -n "persp";
	setAttr ".v" no;
	setAttr ".t" -type "double3" -98.029107391681904 1220.9394032791724 253.39314543339938 ;
	setAttr ".r" -type "double3" -42.338352729609227 -4.600000000000648 -1.9942704634686485e-016 ;
createNode camera -s -n "perspShape" -p "persp";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999986;
	setAttr ".coi" 1688.3091288961837;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".tp" -type "double3" 0.016330986022949218 -999.99874770414829 0.029159522691286195 ;
	setAttr ".hc" -type "string" "viewSet -p %camera";
createNode transform -s -n "top";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 1000.1023591184617 0 ;
	setAttr ".r" -type "double3" -89.999999999999986 0 0 ;
createNode camera -s -n "topShape" -p "top";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1023591184617;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "top";
	setAttr ".den" -type "string" "top_depth";
	setAttr ".man" -type "string" "top_mask";
	setAttr ".hc" -type "string" "viewSet -t %camera";
	setAttr ".o" yes;
createNode transform -s -n "front";
	setAttr ".v" no;
	setAttr ".t" -type "double3" -15.530400987960757 -10.601819574830783 1000.2253459868759 ;
createNode camera -s -n "frontShape" -p "front";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1023591184617;
	setAttr ".ow" 29.884887441218464;
	setAttr ".imn" -type "string" "front";
	setAttr ".den" -type "string" "front_depth";
	setAttr ".man" -type "string" "front_mask";
	setAttr ".hc" -type "string" "viewSet -f %camera";
	setAttr ".o" yes;
createNode transform -s -n "side";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1000.1023591184617 0 0 ;
	setAttr ".r" -type "double3" 0 89.999999999999986 0 ;
createNode camera -s -n "sideShape" -p "side";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1023591184617;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
createNode materialInfo -n "materialInfo17";
createNode shadingEngine -n "CJW_selectPannel_backgroundColor_lambertSG";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode lambert -n "CJW_selectPannel_backgroundColor_lambert";
	setAttr ".c" -type "float3" 0.43553999 0.49562985 0.61000001 ;
createNode groupId -n "groupId1482";
	setAttr ".ihi" 0;
createNode shadingEngine -n "CJW_selectPannel_lambert_01SG";
	setAttr ".ihi" 0;
	setAttr -s 7 ".dsm";
	setAttr ".ro" yes;
	setAttr -s 7 ".gn";
createNode materialInfo -n "p002001MiniTiger_backgroundColor_materialInfo";
createNode lambert -n "CJW_selectPannel__lambert_01";
createNode file -n "CJW_selectPannel_lambert_file";
	addAttr -ci true -sn "originalTexture" -ln "originalTexture" -dt "string";
	setAttr ".ftn" -type "string" "Z:/Resource/Support/Maya/extra/Rigging_Simulation/edward/python/RIG/face_BS/TemplateFile/Facial_V1/color001_quarter.jpg";
	setAttr -l on ".originalTexture" -type "string" "color001.jpg";
createNode place2dTexture -n "CJW_selectPannel_place2dTexture";
createNode materialInfo -n "materialInfo18";
createNode shadingEngine -n "CJW_selectPannel_selectDefaultSurfaceShaderSG";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode surfaceShader -n "CJW_selectPannel_selectDefaultSurfaceShader";
	setAttr ".oc" -type "float3" 0.175 0.91100001 0.65799999 ;
createNode materialInfo -n "materialInfo3";
createNode shadingEngine -n "CJW_selectPannel_cover_lambertSG";
	setAttr ".ihi" 0;
	setAttr -s 5 ".dsm";
	setAttr ".ro" yes;
createNode lambert -n "CJW_selectPannel_cover_lambert";
	setAttr ".c" -type "float3" 0.27450982 0.32549021 0.40000001 ;
createNode materialInfo -n "materialInfo4";
createNode shadingEngine -n "CJW_selectPannel_brow_lambert_01SG";
	setAttr ".ihi" 0;
	setAttr -s 28 ".dsm";
	setAttr ".ro" yes;
createNode lambert -n "CJW_selectPannel_brow_lambert_01";
	setAttr ".c" -type "float3" 0.1882353 0.38431373 0.77254903 ;
createNode materialInfo -n "materialInfo5";
createNode shadingEngine -n "CJW_selectPannel_eye_lambertSG";
	setAttr ".ihi" 0;
	setAttr -s 2 ".dsm";
	setAttr ".ro" yes;
createNode lambert -n "CJW_selectPannel_eye_lambert";
	setAttr ".c" -type "float3" 0 0 0 ;
createNode materialInfo -n "materialInfo1";
createNode shadingEngine -n "CJW_selectPannel_cover_lambert_01SG";
	setAttr ".ihi" 0;
	setAttr -s 53 ".dsm";
	setAttr ".ro" yes;
	setAttr -s 2 ".gn";
createNode lambert -n "CJW_selectPannel_cover_lambert_01";
	setAttr ".c" -type "float3" 0.48626605 0.8399902 0.96100003 ;
createNode materialInfo -n "materialInfo2";
createNode shadingEngine -n "CJW_selectPannel_brow_lambertSG";
	setAttr ".ihi" 0;
	setAttr -s 25 ".dsm";
	setAttr ".ro" yes;
createNode lambert -n "CJW_selectPannel_brow_lambert";
	setAttr ".c" -type "float3" 0.52805001 0.6518957 0.89499998 ;
createNode materialInfo -n "materialInfo6";
createNode shadingEngine -n "CJW_selectPannel_brow_lambert_01SG1";
	setAttr ".ihi" 0;
	setAttr -s 24 ".dsm";
	setAttr ".ro" yes;
createNode lambert -n "CJW_selectPannel_brow_lambert_02";
	setAttr ".c" -type "float3" 1 1 1 ;
createNode materialInfo -n "AA_materialInfo16";
createNode shadingEngine -n "CJW_selectPannel_hi_lambert_01SG";
	setAttr ".ihi" 0;
	setAttr -s 8 ".dsm";
	setAttr ".ro" yes;
	setAttr -s 6 ".gn";
createNode lambert -n "CJW_selectPannel_hi_lambert_01";
	setAttr ".c" -type "float3" 0.34117648 0.56078434 0.21176471 ;
createNode materialInfo -n "p002001MiniTiger_hand_materialInfo";
createNode shadingEngine -n "CJW_selectPannel_hand_lambertSG";
	setAttr ".ihi" 0;
	setAttr -s 26 ".dsm";
	setAttr ".ro" yes;
createNode lambert -n "CJW_selectPannel_hand_lambert";
createNode file -n "CJW_selectPannel_hand_lambert_file";
	addAttr -ci true -sn "originalTexture" -ln "originalTexture" -dt "string";
	setAttr ".ftn" -type "string" "Z:/Resource/Support/Maya/GDC/scripts/RIG/face_BS/TemplateFile/Facial_V1/mi_p002001MiniTiger_color_2K_quarter.jpg";
	setAttr -l on ".originalTexture" -type "string" "mi_p002001MiniTiger_color_2K.tga";
createNode place2dTexture -n "CJW_selectPannel_place2dTexture1";
createNode groupId -n "groupId634";
	setAttr ".ihi" 0;
createNode groupId -n "groupId633";
	setAttr ".ihi" 0;
createNode materialInfo -n "materialInfo7";
createNode shadingEngine -n "CJW_selectPannel_body_lambertSG";
	setAttr ".ihi" 0;
	setAttr -s 6 ".dsm";
	setAttr ".ro" yes;
createNode lambert -n "CJW_selectPannel_body_lambert";
	setAttr ".c" -type "float3" 0.3019608 0.39215687 0.56470591 ;
createNode deleteComponent -n "deleteComponent13";
	setAttr ".dc" -type "componentList" 1 "e[8]";
createNode deleteComponent -n "deleteComponent12";
	setAttr ".dc" -type "componentList" 1 "e[7]";
createNode polyTweak -n "polyTweak11";
	setAttr ".uopa" yes;
	setAttr -s 8 ".tk[0:7]" -type "float3"  0.059910424 -0.1694895 0.014545808
		 0 0 0.01454627 0 0 0.01454627 0 -0.10355638 0.014545794 0 0 0.014545794 -0.0023602266
		 0.17139223 0.014545731 0 0 0.01454604 0 -0.14146492 0.014545794;
createNode polySplit -n "polySplit6";
	setAttr -s 2 ".e[0:1]"  0.54976916 1;
	setAttr -s 2 ".d[0:1]"  -2147483642 -2147483647;
createNode polySplit -n "polySplit5";
	setAttr -s 2 ".e[0:1]"  0.27474338 1;
	setAttr -s 2 ".d[0:1]"  -2147483646 -2147483648;
createNode materialInfo -n "materialInfo9";
createNode shadingEngine -n "CJW_selectPannel_tongue_lambertSG";
	setAttr ".ihi" 0;
	setAttr -s 18 ".dsm";
	setAttr ".ro" yes;
	setAttr -s 2 ".gn";
createNode lambert -n "CJW_selectPannel_tongue_lambert";
	setAttr ".c" -type "float3" 0.94117647 0.66274512 0.67843139 ;
createNode deleteComponent -n "deleteComponent11";
	setAttr ".dc" -type "componentList" 2 "e[7]" "e[9]";
createNode polyTweak -n "polyTweak10";
	setAttr ".uopa" yes;
	setAttr -s 8 ".tk[0:7]" -type "float3"  -0.12768817 -0.27227509 0.01454587
		 0 0 0.01454627 0 0 0.01454627 0 0 0.014545794 0 -0.092876337 0.014545794 0.042223807
		 0.15983611 0.014545727 0 0 0.01454627 0 -0.1143753 0.01454604;
createNode polySplit -n "polySplit2";
	setAttr -s 2 ".e[0:1]"  0 0.56005961;
	setAttr -s 2 ".d[0:1]"  -2147483648 -2147483642;
createNode polySplit -n "polySplit1";
	setAttr -s 2 ".e[0:1]"  0 0.26968902;
	setAttr -s 2 ".d[0:1]"  -2147483645 -2147483646;
createNode materialInfo -n "materialInfo8";
createNode shadingEngine -n "CJW_selectPannel_tongue_lambert_01SG";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode lambert -n "CJW_selectPannel_tongue_lambert_01";
	setAttr ".c" -type "float3" 0.86666667 0.54509807 0.56078434 ;
createNode deleteComponent -n "deleteComponent15";
	setAttr ".dc" -type "componentList" 1 "e[10]";
createNode deleteComponent -n "deleteComponent14";
	setAttr ".dc" -type "componentList" 1 "e[8]";
createNode polyTweak -n "polyTweak12";
	setAttr ".uopa" yes;
	setAttr -s 10 ".tk[0:9]" -type "float3"  -0.0023602266 0.17139223 0.014545731
		 0 0.014607918 0.014545794 0 -0.10355638 0.014545794 0 -0.029215816 0.014545794 0
		 0 0.014545794 0 -0.029215818 0.014545794 0 -0.073039539 0.014545794 0 0 0.014545794
		 0 -0.021490123 0.014545794 0 0 0.014545794;
createNode polySplit -n "polySplit14";
	setAttr -s 2 ".e[0:1]"  0.52727485 0.5;
	setAttr -s 2 ".d[0:1]"  -2147483642 -2147483648;
createNode polySplit -n "polySplit13";
	setAttr -s 2 ".e[0:1]"  0.32339799 0.69520289;
	setAttr -s 2 ".d[0:1]"  -2147483645 -2147483648;
createNode deleteComponent -n "deleteComponent22";
	setAttr ".dc" -type "componentList" 1 "e[10]";
createNode deleteComponent -n "deleteComponent21";
	setAttr ".dc" -type "componentList" 1 "e[8]";
createNode polyTweak -n "polyTweak14";
	setAttr ".uopa" yes;
	setAttr -s 10 ".tk[0:9]" -type "float3"  0.042223807 0.15983611 0.014545727
		 0 0.014607918 0.014545794 0 -0.092876337 0.014545794 0 -0.029215816 0.014545794 0
		 0 0.014545794 0 -0.029215818 0.014545794 0 0 0.014545794 0 -0.15852934 0.014545794
		 0 0 0.014545794 0 -0.10671464 0.014545794;
createNode polySplit -n "polySplit8";
	setAttr -s 2 ".e[0:1]"  0.46225041 0.5;
	setAttr -s 2 ".d[0:1]"  -2147483648 -2147483641;
createNode polySplit -n "polySplit7";
	setAttr -s 2 ".e[0:1]"  0.68986672 0.32040253;
	setAttr -s 2 ".d[0:1]"  -2147483648 -2147483645;
createNode groupId -n "groupId1564";
	setAttr ".ihi" 0;
createNode deleteComponent -n "deleteComponent27";
	setAttr ".dc" -type "componentList" 1 "e[15]";
createNode deleteComponent -n "deleteComponent26";
	setAttr ".dc" -type "componentList" 1 "e[14]";
createNode deleteComponent -n "deleteComponent25";
	setAttr ".dc" -type "componentList" 1 "e[3]";
createNode deleteComponent -n "deleteComponent24";
	setAttr ".dc" -type "componentList" 1 "e[14]";
createNode deleteComponent -n "deleteComponent23";
	setAttr ".dc" -type "componentList" 1 "e[12]";
createNode polyTweak -n "polyTweak15";
	setAttr ".uopa" yes;
	setAttr -s 8 ".tk";
	setAttr ".tk[1]" -type "float3" 0.039871845 -0.18189484 0 ;
	setAttr ".tk[6]" -type "float3" 0 -0.029215816 0 ;
	setAttr ".tk[7]" -type "float3" 0 -0.029215818 0 ;
	setAttr ".tk[8]" -type "float3" 0 0.014607918 0 ;
	setAttr ".tk[9]" -type "float3" -0.067074537 0 0 ;
	setAttr ".tk[11]" -type "float3" -0.051607884 0 0 ;
	setAttr ".tk[13]" -type "float3" -0.038920511 0 0 ;
	setAttr ".tk[15]" -type "float3" 0 -0.12311468 0 ;
createNode polySplit -n "polySplit24";
	setAttr -s 2 ".e[0:1]"  0 0.5;
	setAttr -s 2 ".d[0:1]"  -2147483648 -2147483631;
createNode polySplit -n "polySplit21";
	setAttr -s 2 ".e[0:1]"  0.37913051 0.35937098;
	setAttr -s 2 ".d[0:1]"  -2147483647 -2147483643;
createNode polySplit -n "polySplit16";
	setAttr -s 2 ".e[0:1]"  0.38386574 0.5;
	setAttr -s 2 ".d[0:1]"  -2147483642 -2147483637;
createNode polySplit -n "polySplit15";
	setAttr -s 2 ".e[0:1]"  0.59745604 0.34803179;
	setAttr -s 2 ".d[0:1]"  -2147483642 -2147483641;
createNode groupParts -n "groupParts1";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "f[0:1]";
createNode groupId -n "groupId1565";
	setAttr ".ihi" 0;
createNode deleteComponent -n "deleteComponent20";
	setAttr ".dc" -type "componentList" 1 "e[5]";
createNode deleteComponent -n "deleteComponent19";
	setAttr ".dc" -type "componentList" 1 "e[17]";
createNode deleteComponent -n "deleteComponent18";
	setAttr ".dc" -type "componentList" 1 "e[16]";
createNode deleteComponent -n "deleteComponent17";
	setAttr ".dc" -type "componentList" 1 "e[14]";
createNode deleteComponent -n "deleteComponent16";
	setAttr ".dc" -type "componentList" 1 "e[12]";
createNode polyTweak -n "polyTweak13";
	setAttr ".uopa" yes;
	setAttr -s 8 ".tk";
	setAttr ".tk[0]" -type "float3" 0 -0.029215818 0 ;
	setAttr ".tk[1]" -type "float3" 0 -0.029215816 0 ;
	setAttr ".tk[4]" -type "float3" 0 0.014607918 0 ;
	setAttr ".tk[5]" -type "float3" -0.039871845 -0.18189484 0 ;
	setAttr ".tk[10]" -type "float3" 0.067074537 0 0 ;
	setAttr ".tk[12]" -type "float3" 0.051607884 0 0 ;
	setAttr ".tk[14]" -type "float3" 0.038920511 0 0 ;
	setAttr ".tk[15]" -type "float3" 0 -0.12311468 0 ;
createNode polySplit -n "polySplit26";
	setAttr -s 2 ".e[0:1]"  0.47312248 0;
	setAttr -s 2 ".d[0:1]"  -2147483632 -2147483642;
createNode polySplit -n "polySplit23";
	setAttr -s 2 ".e[0:1]"  0.29253137 0.42341217;
	setAttr -s 2 ".d[0:1]"  -2147483639 -2147483641;
createNode polySplit -n "polySplit20";
	setAttr -s 2 ".e[0:1]"  0.4603554 0.39968896;
	setAttr -s 2 ".d[0:1]"  -2147483638 -2147483648;
createNode polySplit -n "polySplit19";
	setAttr -s 2 ".e[0:1]"  0.36838147 0.62146223;
	setAttr -s 2 ".d[0:1]"  -2147483647 -2147483648;
createNode groupParts -n "groupParts2";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "f[0:1]";
createNode groupId -n "groupId1553";
	setAttr ".ihi" 0;
createNode groupId -n "groupId1483";
	setAttr ".ihi" 0;
createNode groupId -n "groupId1552";
	setAttr ".ihi" 0;
createNode groupId -n "groupId1559";
	setAttr ".ihi" 0;
createNode materialInfo -n "p002001MiniTiger_polySurface212_f_0__materialInfo";
createNode shadingEngine -n "CJW_selectPannel__lambertSG";
	setAttr ".ihi" 0;
	setAttr -s 78 ".dsm";
	setAttr ".ro" yes;
	setAttr -s 30 ".gn";
createNode lambert -n "CJW_selectPannel__lambert";
createNode ramp -n "CJW_selectPannel__lambert_ramp";
	addAttr -ci true -sn "resolution" -ln "resolution" -dv 32 -at "long";
	setAttr ".t" 4;
	setAttr ".in" 0;
	setAttr -s 3 ".cel";
	setAttr ".cel[0].ep" 0;
	setAttr ".cel[0].ec" -type "float3" 0.34025377 0.58823532 0.0922722 ;
	setAttr ".cel[1].ep" 0.49500000476837158;
	setAttr ".cel[1].ec" -type "float3" 1 1 1 ;
	setAttr ".cel[2].ep" 0.58499997854232788;
	setAttr ".cel[2].ec" -type "float3" 1 1 1 ;
	setAttr ".resolution" 256;
createNode place2dTexture -n "CJW_selectPannel__place2dTexture";
createNode groupId -n "groupId1532";
	setAttr ".ihi" 0;
createNode groupId -n "groupId1533";
	setAttr ".ihi" 0;
createNode groupId -n "groupId1554";
	setAttr ".ihi" 0;
createNode groupId -n "groupId1534";
	setAttr ".ihi" 0;
createNode groupId -n "groupId1535";
	setAttr ".ihi" 0;
createNode groupId -n "groupId1536";
	setAttr ".ihi" 0;
createNode groupId -n "groupId1539";
	setAttr ".ihi" 0;
createNode groupId -n "groupId1538";
	setAttr ".ihi" 0;
createNode groupId -n "groupId1537";
	setAttr ".ihi" 0;
createNode groupId -n "groupId1540";
	setAttr ".ihi" 0;
createNode groupId -n "groupId1541";
	setAttr ".ihi" 0;
createNode groupId -n "groupId1542";
	setAttr ".ihi" 0;
createNode groupId -n "groupId1545";
	setAttr ".ihi" 0;
createNode groupId -n "groupId1544";
	setAttr ".ihi" 0;
createNode groupId -n "groupId1543";
	setAttr ".ihi" 0;
createNode groupId -n "groupId1551";
	setAttr ".ihi" 0;
createNode groupId -n "groupId1560";
	setAttr ".ihi" 0;
createNode groupId -n "groupId1517";
	setAttr ".ihi" 0;
createNode groupId -n "groupId1518";
	setAttr ".ihi" 0;
createNode groupId -n "groupId1519";
	setAttr ".ihi" 0;
createNode groupId -n "groupId1520";
	setAttr ".ihi" 0;
createNode groupId -n "groupId1521";
	setAttr ".ihi" 0;
createNode groupId -n "groupId1522";
	setAttr ".ihi" 0;
createNode groupId -n "groupId1525";
	setAttr ".ihi" 0;
createNode groupId -n "groupId1524";
	setAttr ".ihi" 0;
createNode groupId -n "groupId1523";
	setAttr ".ihi" 0;
createNode groupId -n "groupId1526";
	setAttr ".ihi" 0;
createNode groupId -n "groupId1527";
	setAttr ".ihi" 0;
createNode groupId -n "groupId1528";
	setAttr ".ihi" 0;
createNode groupId -n "groupId1529";
	setAttr ".ihi" 0;
createNode groupId -n "groupId1530";
	setAttr ".ihi" 0;
createNode groupId -n "groupId1531";
	setAttr ".ihi" 0;
createNode groupId -n "groupId1500";
	setAttr ".ihi" 0;
createNode groupId -n "groupId1503";
	setAttr ".ihi" 0;
createNode shadingEngine -n "CJW_selectPannel_polySurface95_f_0__lambertSG";
	setAttr ".ihi" 0;
	setAttr -s 5 ".dsm";
	setAttr ".ro" yes;
	setAttr -s 5 ".gn";
createNode materialInfo -n "AA_materialInfo11";
createNode lambert -n "CJW_selectPannel_polySurface95_f_0__lambert";
	setAttr ".c" -type "float3" 1 0.99215686 0.28235295 ;
createNode groupId -n "groupId1485";
	setAttr ".ihi" 0;
createNode groupId -n "groupId1488";
	setAttr ".ihi" 0;
createNode groupId -n "groupId1509";
	setAttr ".ihi" 0;
createNode groupId -n "groupId1511";
	setAttr ".ihi" 0;
createNode groupId -n "groupId1492";
	setAttr ".ihi" 0;
createNode groupId -n "groupId1494";
	setAttr ".ihi" 0;
createNode groupId -n "groupId1480";
	setAttr ".ihi" 0;
createNode groupId -n "groupId1481";
	setAttr ".ihi" 0;
createNode groupId -n "groupId1067";
	setAttr ".ihi" 0;
createNode lightLinker -s -n "lightLinker1";
	setAttr -s 18 ".lnk";
	setAttr -s 18 ".slnk";
createNode displayLayerManager -n "layerManager";
createNode displayLayer -n "defaultLayer";
createNode renderLayerManager -n "renderLayerManager";
createNode renderLayer -n "defaultRenderLayer";
	setAttr ".g" yes;
createNode hyperGraphInfo -n "nodeEditorPanel1Info";
createNode hyperView -n "hyperView1";
	setAttr ".dag" no;
createNode hyperLayout -n "hyperLayout1";
	setAttr ".ihi" 0;
	setAttr -s 50 ".hyp";
	setAttr ".hyp[0].nvs" 1920;
	setAttr ".hyp[1].nvs" 1920;
	setAttr ".hyp[2].nvs" 1920;
	setAttr ".hyp[3].nvs" 1920;
	setAttr ".hyp[4].nvs" 1920;
	setAttr ".hyp[5].nvs" 1920;
	setAttr ".hyp[6].nvs" 1920;
	setAttr ".hyp[7].nvs" 1920;
	setAttr ".hyp[8].nvs" 1920;
	setAttr ".hyp[9].nvs" 1920;
	setAttr ".hyp[10].nvs" 1920;
	setAttr ".hyp[11].nvs" 1920;
	setAttr ".hyp[12].nvs" 1920;
	setAttr ".hyp[13].nvs" 1920;
	setAttr ".hyp[14].nvs" 1920;
	setAttr ".hyp[15].nvs" 1920;
	setAttr ".hyp[16].nvs" 1920;
	setAttr ".hyp[17].nvs" 1920;
	setAttr ".hyp[18].nvs" 1920;
	setAttr ".hyp[19].nvs" 1920;
	setAttr ".hyp[20].nvs" 1920;
	setAttr ".hyp[21].nvs" 1920;
	setAttr ".hyp[22].nvs" 1920;
	setAttr ".hyp[23].nvs" 1920;
	setAttr ".hyp[24].nvs" 1920;
	setAttr ".hyp[25].nvs" 1920;
	setAttr ".hyp[26].nvs" 1920;
	setAttr ".hyp[27].nvs" 1920;
	setAttr ".hyp[28].nvs" 1920;
	setAttr ".hyp[29].nvs" 1920;
	setAttr ".hyp[30].nvs" 1920;
	setAttr ".hyp[31].nvs" 1920;
	setAttr ".hyp[32].nvs" 1920;
	setAttr ".hyp[33].nvs" 1920;
	setAttr ".hyp[34].nvs" 1920;
	setAttr ".hyp[35].nvs" 1920;
	setAttr ".hyp[36].nvs" 1920;
	setAttr ".hyp[37].nvs" 1920;
	setAttr ".hyp[38].nvs" 1920;
	setAttr ".hyp[39].nvs" 1920;
	setAttr ".hyp[40].nvs" 1920;
	setAttr ".hyp[41].nvs" 1920;
	setAttr ".hyp[42].nvs" 1920;
	setAttr ".hyp[43].nvs" 1920;
	setAttr ".hyp[44].nvs" 1920;
	setAttr ".hyp[45].nvs" 1920;
	setAttr ".hyp[46].nvs" 1920;
	setAttr ".hyp[47].nvs" 1920;
	setAttr ".hyp[48].nvs" 1920;
	setAttr ".hyp[49].nvs" 1920;
	setAttr ".anf" yes;
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
		+ "            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Front View\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `modelPanel -unParent -l (localizedPanelLabel(\"Front View\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            modelEditor -e \n                -camera \"front\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n"
		+ "                -displayAppearance \"wireframe\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 1\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 8192\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -maxConstantTransparency 1\n                -rendererName \"base_OpenGL_Renderer\" \n"
		+ "                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 256 256 \n                -bumpResolution 512 512 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 1\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n"
		+ "                -imagePlane 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -clipGhosts 1\n                -greasePencils 1\n                -shadows 0\n                $editorName;\n            modelEditor -e -viewSelected 0 $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Front View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"front\" \n            -useInteractiveMode 0\n"
		+ "            -displayLights \"default\" \n            -displayAppearance \"wireframe\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 1\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 8192\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -maxConstantTransparency 1\n            -rendererName \"base_OpenGL_Renderer\" \n            -objectFilterShowInHUD 1\n"
		+ "            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -fluids 1\n"
		+ "            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Persp View\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `modelPanel -unParent -l (localizedPanelLabel(\"Persp View\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            modelEditor -e \n                -camera \"persp\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n"
		+ "                -displayAppearance \"smoothShaded\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 1\n                -headsUpDisplay 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 1\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 1\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 8192\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -maxConstantTransparency 1\n"
		+ "                -rendererName \"base_OpenGL_Renderer\" \n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 256 256 \n                -bumpResolution 512 512 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 1\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n"
		+ "                -hulls 1\n                -grid 1\n                -imagePlane 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -clipGhosts 1\n                -greasePencils 1\n                -shadows 0\n                $editorName;\n            modelEditor -e -viewSelected 0 $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Persp View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n"
		+ "            -camera \"persp\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 1\n            -headsUpDisplay 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 1\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 1\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 8192\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -maxConstantTransparency 1\n            -rendererName \"base_OpenGL_Renderer\" \n"
		+ "            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n"
		+ "            -dynamics 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"Outliner\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `outlinerPanel -unParent -l (localizedPanelLabel(\"Outliner\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            outlinerEditor -e \n                -docTag \"isolOutln_fromSeln\" \n                -showShapes 0\n"
		+ "                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 0\n                -showConnected 0\n                -showAnimCurvesOnly 0\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 0\n                -showDagOnly 1\n                -showAssets 1\n                -showContainedOnly 1\n                -showPublishedAsConnected 0\n                -showContainerContents 1\n                -ignoreDagHierarchy 0\n                -expandConnections 0\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 1\n                -showLeafs 1\n                -showNumericAttrsOnly 0\n                -highlightActive 1\n                -autoSelectNewObjects 0\n                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 0\n                -setFilter \"defaultSetFilter\" \n                -showSetMembers 1\n"
		+ "                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 0\n                -mapMotionTrails 0\n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"Outliner\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -docTag \"isolOutln_fromSeln\" \n            -showShapes 0\n"
		+ "            -showReferenceNodes 0\n            -showReferenceMembers 0\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n"
		+ "            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\tif ($useSceneConfig) {\n\t\toutlinerPanel -e -to $panelName;\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"graphEditor\" (localizedPanelLabel(\"Graph Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"graphEditor\" -l (localizedPanelLabel(\"Graph Editor\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n"
		+ "            outlinerEditor -e \n                -showShapes 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 1\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 0\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 1\n                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 1\n"
		+ "                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 1\n                -mapMotionTrails 1\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"GraphEd\");\n            animCurveEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 1\n"
		+ "                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -showResults \"off\" \n                -showBufferCurves \"off\" \n                -smoothness \"fine\" \n                -resultSamples 1\n                -resultScreenSamples 0\n                -resultUpdate \"delayed\" \n                -showUpstreamCurves 1\n                -stackedCurves 0\n                -stackedCurvesMin -1\n                -stackedCurvesMax 1\n                -stackedCurvesSpace 0.2\n                -displayNormalized 0\n                -preSelectionHighlight 0\n                -constrainDrag 0\n                -classicMode 1\n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Graph Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n"
		+ "                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 1\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 0\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 1\n                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 1\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n"
		+ "                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 1\n                -mapMotionTrails 1\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"GraphEd\");\n            animCurveEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 1\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n"
		+ "                -showResults \"off\" \n                -showBufferCurves \"off\" \n                -smoothness \"fine\" \n                -resultSamples 1\n                -resultScreenSamples 0\n                -resultUpdate \"delayed\" \n                -showUpstreamCurves 1\n                -stackedCurves 0\n                -stackedCurvesMin -1\n                -stackedCurvesMax 1\n                -stackedCurvesSpace 0.2\n                -displayNormalized 0\n                -preSelectionHighlight 0\n                -constrainDrag 0\n                -classicMode 1\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dopeSheetPanel\" (localizedPanelLabel(\"Dope Sheet\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"dopeSheetPanel\" -l (localizedPanelLabel(\"Dope Sheet\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n"
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
		+ "\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Paint Effects\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"scriptEditorPanel\" (localizedPanelLabel(\"Script Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"scriptEditorPanel\" -l (localizedPanelLabel(\"Script Editor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Script Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\tif ($useSceneConfig) {\n        string $configName = `getPanel -cwl (localizedPanelLabel(\"Current Layout\"))`;\n        if (\"\" != $configName) {\n\t\t\tpanelConfiguration -edit -label (localizedPanelLabel(\"Current Layout\")) \n\t\t\t\t-defaultImage \"vacantCell.xP:/\"\n\t\t\t\t-image \"\"\n\t\t\t\t-sc false\n"
		+ "\t\t\t\t-configString \"global string $gMainPane; paneLayout -e -cn \\\"single\\\" -ps 1 100 100 $gMainPane;\"\n\t\t\t\t-removeAllPanels\n\t\t\t\t-ap false\n\t\t\t\t\t(localizedPanelLabel(\"Persp View\")) \n\t\t\t\t\t\"modelPanel\"\n"
		+ "\t\t\t\t\t\"$panelName = `modelPanel -unParent -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels `;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 1\\n    -headsUpDisplay 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 1\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 1\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 8192\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -maxConstantTransparency 1\\n    -rendererName \\\"base_OpenGL_Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName\"\n"
		+ "\t\t\t\t\t\"modelPanel -edit -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels  $panelName;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 1\\n    -headsUpDisplay 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 1\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 1\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 8192\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -maxConstantTransparency 1\\n    -rendererName \\\"base_OpenGL_Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName\"\n"
		+ "\t\t\t\t$configName;\n\n            setNamedPanelLayout (localizedPanelLabel(\"Current Layout\"));\n        }\n\n        panelHistory -e -clear mainPanelHistory;\n        setFocus `paneLayout -q -p1 $gMainPane`;\n        sceneUIReplacement -deleteRemaining;\n        sceneUIReplacement -clear;\n\t}\n\n\ngrid -spacing 5 -size 12 -divisions 5 -displayAxes yes -displayGridLines yes -displayDivisionLines yes -displayPerspectiveLabels no -displayOrthographicLabels no -displayAxesBold yes -perspectiveLabelPosition axis -orthographicLabelPosition edge;\nviewManip -drawCompass 0 -compassAngle 0 -frontParameters \"\" -homeParameters \"\" -selectionLockParameters \"\";\n}\n");
	setAttr ".st" 3;
createNode script -n "sceneConfigurationScriptNode";
	setAttr ".b" -type "string" "playbackOptions -min 1 -max 24 -ast 1 -aet 48 ";
	setAttr ".st" 6;
createNode polySplit -n "polySplit30";
	setAttr ".e[0]"  0.5;
	setAttr ".d[0]"  -2147483648;
select -ne :time1;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr ".o" 1;
	setAttr -av ".unw" 1;
	setAttr -k on ".etw";
	setAttr -k on ".tps";
	setAttr -k on ".tms";
select -ne :renderPartition;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 18 ".st";
	setAttr -cb on ".an";
	setAttr -cb on ".pt";
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
	setAttr ".ro" yes;
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
	setAttr ".ro" yes;
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
select -ne :defaultShaderList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 18 ".s";
select -ne :defaultTextureList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 3 ".tx";
select -ne :postProcessList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".p";
select -ne :defaultRenderUtilityList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 3 ".u";
select -ne :defaultRenderingList1;
select -ne :renderGlobalsList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
select -ne :defaultRenderGlobals;
	setAttr -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -k on ".nds";
	setAttr -k on ".bnm";
	setAttr -k on ".macc";
	setAttr -k on ".macd";
	setAttr -k on ".macq";
	setAttr -k on ".mcfr";
	setAttr -k on ".ifg";
	setAttr -k on ".clip";
	setAttr -k on ".edm";
	setAttr -k on ".edl";
	setAttr -cb on ".ren";
	setAttr -av -k on ".esr";
	setAttr -k on ".ors";
	setAttr -k on ".sdf";
	setAttr -av -k on ".outf";
	setAttr -k on ".imfkey";
	setAttr -k on ".gama";
	setAttr -k on ".ar";
	setAttr -k on ".fs";
	setAttr -k on ".ef";
	setAttr -av -k on ".bfs";
	setAttr -k on ".me";
	setAttr -k on ".se";
	setAttr -av -k on ".be";
	setAttr -cb on ".ep";
	setAttr -k on ".fec";
	setAttr -av -k on ".ofc";
	setAttr -k on ".ofe";
	setAttr -k on ".efe";
	setAttr -k on ".oft";
	setAttr -k on ".umfn";
	setAttr -k on ".ufe";
	setAttr -k on ".peie";
	setAttr -k on ".rv";
	setAttr -k on ".comp";
	setAttr -k on ".cth";
	setAttr -k on ".soll";
	setAttr -cb on ".sosl";
	setAttr -k on ".rd";
	setAttr -k on ".lp";
	setAttr -av -k on ".sp";
	setAttr -k on ".shs";
	setAttr -av -k on ".lpr";
	setAttr -k on ".gv";
	setAttr -k on ".sv";
	setAttr -k on ".mm";
	setAttr -k on ".npu";
	setAttr -k on ".itf";
	setAttr -k on ".shp";
	setAttr -k on ".isp";
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
	setAttr ".pram" -type "string" "";
	setAttr -k on ".poam";
	setAttr -k on ".prlm";
	setAttr -k on ".polm";
	setAttr -cb on ".prm";
	setAttr -cb on ".pom";
	setAttr -k on ".pfrm";
	setAttr -k on ".pfom";
	setAttr -av -k on ".bll";
	setAttr -av -k on ".bls";
	setAttr -av -k on ".smv";
	setAttr -k on ".ubc";
	setAttr -k on ".mbc";
	setAttr -k on ".mbt";
	setAttr -k on ".udbx";
	setAttr -k on ".smc";
	setAttr -k on ".kmv";
	setAttr -k on ".isl";
	setAttr -k on ".ism";
	setAttr -k on ".imb";
	setAttr -av -k on ".rlen";
	setAttr -av -k on ".frts";
	setAttr -k on ".tlwd";
	setAttr -k on ".tlht";
	setAttr -k on ".jfc";
	setAttr -k on ".rsb";
	setAttr -k on ".ope";
	setAttr -k on ".oppf";
	setAttr -k on ".hbl";
select -ne :defaultResolution;
	setAttr -av -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -k on ".bnm";
	setAttr -av ".w";
	setAttr -av ".h";
	setAttr -av ".pa" 1;
	setAttr -av -k on ".al";
	setAttr -av ".dar";
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
	setAttr ".ctrs" 256;
	setAttr -av ".btrs" 512;
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
	setAttr -av -k on ".bcb";
	setAttr -av -k on ".bcg";
	setAttr -av -k on ".bcr";
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
	setAttr ".fn" -type "string" "im";
	setAttr -k on ".if";
	setAttr ".res" -type "string" "ntsc_4d 646 485 1.333";
	setAttr -k on ".as";
	setAttr -k on ".ds";
	setAttr -k on ".lm";
	setAttr -av -k on ".fir";
	setAttr -k on ".aap";
	setAttr -av -k on ".gh";
	setAttr -cb on ".sd";
connectAttr "groupId1482.id" "FM_Cam_characters_FACIAL_backgroundColor_Shape.iog.og[0].gid"
		;
connectAttr "CJW_selectPannel_lambert_01SG.mwc" "FM_Cam_characters_FACIAL_backgroundColor_Shape.iog.og[0].gco"
		;
connectAttr "groupId634.id" "c_Lf_nosewing_CTRL_guideShape.iog.og[0].gid";
connectAttr "CJW_selectPannel_cover_lambert_01SG.mwc" "c_Lf_nosewing_CTRL_guideShape.iog.og[0].gco"
		;
connectAttr "groupId633.id" "c_Rt_nosewing_CTRL_guideShape.iog.og[0].gid";
connectAttr "CJW_selectPannel_cover_lambert_01SG.mwc" "c_Rt_nosewing_CTRL_guideShape.iog.og[0].gco"
		;
connectAttr "deleteComponent13.og" "FM_Cam_c_hi_tongue_1_guideShape.i";
connectAttr "deleteComponent11.og" "FM_Cam_c_hi_tongue_2_guideShape.i";
connectAttr "deleteComponent15.og" "FM_Cam_c_hi_tongue_4_guideShape.i";
connectAttr "deleteComponent22.og" "FM_Cam_c_hi_tongue_5_guideShape.i";
connectAttr "groupId1564.id" "FM_Cam_c_hi_tongue_10_guideShape.iog.og[0].gid";
connectAttr "CJW_selectPannel_tongue_lambertSG.mwc" "FM_Cam_c_hi_tongue_10_guideShape.iog.og[0].gco"
		;
connectAttr "deleteComponent27.og" "FM_Cam_c_hi_tongue_10_guideShape.i";
connectAttr "groupId1565.id" "FM_Cam_c_hi_tongue_11_guideShape.iog.og[0].gid";
connectAttr "CJW_selectPannel_tongue_lambertSG.mwc" "FM_Cam_c_hi_tongue_11_guideShape.iog.og[0].gco"
		;
connectAttr "deleteComponent20.og" "FM_Cam_c_hi_tongue_11_guideShape.i";
connectAttr "polySplit30.out" "c_tongue_joint2_guideShape.i";
connectAttr "groupId1553.id" "FM_Cam_BODY_backgroundColor_Shape.iog.og[0].gid";
connectAttr "CJW_selectPannel_lambert_01SG.mwc" "FM_Cam_BODY_backgroundColor_Shape.iog.og[0].gco"
		;
connectAttr "groupId1483.id" "FM_Cam_characters_BODY_picture_Shape.iog.og[0].gid"
		;
connectAttr "CJW_selectPannel_lambert_01SG.mwc" "FM_Cam_characters_BODY_picture_Shape.iog.og[0].gco"
		;
connectAttr "groupId1552.id" "FM_Cam_HANDS_backgroundColor_Shape.iog.og[0].gid";
connectAttr "CJW_selectPannel_lambert_01SG.mwc" "FM_Cam_HANDS_backgroundColor_Shape.iog.og[0].gco"
		;
connectAttr "groupId1559.id" "FM_Cam_characters_hands_picture_Shape.iog.og[0].gid"
		;
connectAttr "CJW_selectPannel_lambert_01SG.mwc" "FM_Cam_characters_hands_picture_Shape.iog.og[0].gco"
		;
connectAttr "groupId1532.id" "Rt_thumb3_guideShape.iog.og[0].gid";
connectAttr "CJW_selectPannel__lambertSG.mwc" "Rt_thumb3_guideShape.iog.og[0].gco"
		;
connectAttr "groupId1533.id" "Rt_thumb2_guideShape.iog.og[0].gid";
connectAttr "CJW_selectPannel__lambertSG.mwc" "Rt_thumb2_guideShape.iog.og[0].gco"
		;
connectAttr "groupId1554.id" "Rt_thumb1_guideShape.iog.og[0].gid";
connectAttr "CJW_selectPannel__lambertSG.mwc" "Rt_thumb1_guideShape.iog.og[0].gco"
		;
connectAttr "groupId1534.id" "Rt_index3_guideShape.iog.og[0].gid";
connectAttr "CJW_selectPannel__lambertSG.mwc" "Rt_index3_guideShape.iog.og[0].gco"
		;
connectAttr "groupId1535.id" "Rt_index2_guideShape.iog.og[0].gid";
connectAttr "CJW_selectPannel__lambertSG.mwc" "Rt_index2_guideShape.iog.og[0].gco"
		;
connectAttr "groupId1536.id" "Rt_index1_guideShape.iog.og[0].gid";
connectAttr "CJW_selectPannel__lambertSG.mwc" "Rt_index1_guideShape.iog.og[0].gco"
		;
connectAttr "groupId1539.id" "Rt_mid3_guideShape.iog.og[0].gid";
connectAttr "CJW_selectPannel__lambertSG.mwc" "Rt_mid3_guideShape.iog.og[0].gco"
		;
connectAttr "groupId1538.id" "Rt_mid2_guideShape.iog.og[0].gid";
connectAttr "CJW_selectPannel__lambertSG.mwc" "Rt_mid2_guideShape.iog.og[0].gco"
		;
connectAttr "groupId1537.id" "Rt_mid1_guideShape.iog.og[0].gid";
connectAttr "CJW_selectPannel__lambertSG.mwc" "Rt_mid1_guideShape.iog.og[0].gco"
		;
connectAttr "groupId1540.id" "Rt_ring3_guideShape.iog.og[0].gid";
connectAttr "CJW_selectPannel__lambertSG.mwc" "Rt_ring3_guideShape.iog.og[0].gco"
		;
connectAttr "groupId1541.id" "Rt_ring2_guideShape.iog.og[0].gid";
connectAttr "CJW_selectPannel__lambertSG.mwc" "Rt_ring2_guideShape.iog.og[0].gco"
		;
connectAttr "groupId1542.id" "Rt_ring1_guideShape.iog.og[0].gid";
connectAttr "CJW_selectPannel__lambertSG.mwc" "Rt_ring1_guideShape.iog.og[0].gco"
		;
connectAttr "groupId1545.id" "Rt_pinky3_guideShape.iog.og[0].gid";
connectAttr "CJW_selectPannel__lambertSG.mwc" "Rt_pinky3_guideShape.iog.og[0].gco"
		;
connectAttr "groupId1544.id" "Rt_pinky2_guideShape.iog.og[0].gid";
connectAttr "CJW_selectPannel__lambertSG.mwc" "Rt_pinky2_guideShape.iog.og[0].gco"
		;
connectAttr "groupId1543.id" "Rt_pinky1_guideShape.iog.og[0].gid";
connectAttr "CJW_selectPannel__lambertSG.mwc" "Rt_pinky1_guideShape.iog.og[0].gco"
		;
connectAttr "groupId1551.id" "FM_Cam_FEET_backgroundColor_Shape.iog.og[0].gid";
connectAttr "CJW_selectPannel_lambert_01SG.mwc" "FM_Cam_FEET_backgroundColor_Shape.iog.og[0].gco"
		;
connectAttr "groupId1560.id" "FM_Cam_characters_feet_picture_Shape.iog.og[0].gid"
		;
connectAttr "CJW_selectPannel_lambert_01SG.mwc" "FM_Cam_characters_feet_picture_Shape.iog.og[0].gco"
		;
connectAttr "groupId1517.id" "Rt_Toe_thumb3_guideShape.iog.og[0].gid";
connectAttr "CJW_selectPannel__lambertSG.mwc" "Rt_Toe_thumb3_guideShape.iog.og[0].gco"
		;
connectAttr "groupId1518.id" "Rt_Toe_thumb2_guideShape.iog.og[0].gid";
connectAttr "CJW_selectPannel__lambertSG.mwc" "Rt_Toe_thumb2_guideShape.iog.og[0].gco"
		;
connectAttr "groupId1519.id" "Rt_Toe_thumb1_guideShape.iog.og[0].gid";
connectAttr "CJW_selectPannel__lambertSG.mwc" "Rt_Toe_thumb1_guideShape.iog.og[0].gco"
		;
connectAttr "groupId1520.id" "Rt_Toe_index3_guideShape.iog.og[0].gid";
connectAttr "CJW_selectPannel__lambertSG.mwc" "Rt_Toe_index3_guideShape.iog.og[0].gco"
		;
connectAttr "groupId1521.id" "Rt_Toe_index2_guideShape.iog.og[0].gid";
connectAttr "CJW_selectPannel__lambertSG.mwc" "Rt_Toe_index2_guideShape.iog.og[0].gco"
		;
connectAttr "groupId1522.id" "Rt_Toe_index1_guideShape.iog.og[0].gid";
connectAttr "CJW_selectPannel__lambertSG.mwc" "Rt_Toe_index1_guideShape.iog.og[0].gco"
		;
connectAttr "groupId1525.id" "Rt_Toe_mid3_guideShape.iog.og[0].gid";
connectAttr "CJW_selectPannel__lambertSG.mwc" "Rt_Toe_mid3_guideShape.iog.og[0].gco"
		;
connectAttr "groupId1524.id" "Rt_Toe_mid2_guideShape.iog.og[0].gid";
connectAttr "CJW_selectPannel__lambertSG.mwc" "Rt_Toe_mid2_guideShape.iog.og[0].gco"
		;
connectAttr "groupId1523.id" "Rt_Toe_mid1_guideShape.iog.og[0].gid";
connectAttr "CJW_selectPannel__lambertSG.mwc" "Rt_Toe_mid1_guideShape.iog.og[0].gco"
		;
connectAttr "groupId1526.id" "Rt_Toe_ring3_guideShape.iog.og[0].gid";
connectAttr "CJW_selectPannel__lambertSG.mwc" "Rt_Toe_ring3_guideShape.iog.og[0].gco"
		;
connectAttr "groupId1527.id" "Rt_Toe_ring2_guideShape.iog.og[0].gid";
connectAttr "CJW_selectPannel__lambertSG.mwc" "Rt_Toe_ring2_guideShape.iog.og[0].gco"
		;
connectAttr "groupId1528.id" "Rt_Toe_ring1_guideShape.iog.og[0].gid";
connectAttr "CJW_selectPannel__lambertSG.mwc" "Rt_Toe_ring1_guideShape.iog.og[0].gco"
		;
connectAttr "groupId1529.id" "Rt_Toe_pinky3_guideShape.iog.og[0].gid";
connectAttr "CJW_selectPannel__lambertSG.mwc" "Rt_Toe_pinky3_guideShape.iog.og[0].gco"
		;
connectAttr "groupId1530.id" "Rt_Toe_pinky2_guideShape.iog.og[0].gid";
connectAttr "CJW_selectPannel__lambertSG.mwc" "Rt_Toe_pinky2_guideShape.iog.og[0].gco"
		;
connectAttr "groupId1531.id" "Rt_Toe_pinky1_guideShape.iog.og[0].gid";
connectAttr "CJW_selectPannel__lambertSG.mwc" "Rt_Toe_pinky1_guideShape.iog.og[0].gco"
		;
connectAttr "groupId1500.id" "Rt_shoulder_guideShape.iog.og[0].gid";
connectAttr "CJW_selectPannel_hi_lambert_01SG.mwc" "Rt_shoulder_guideShape.iog.og[0].gco"
		;
connectAttr "groupId1503.id" "RtArm_Switch_guideShape.iog.og[0].gid";
connectAttr "CJW_selectPannel_polySurface95_f_0__lambertSG.mwc" "RtArm_Switch_guideShape.iog.og[0].gco"
		;
connectAttr "groupId1485.id" "Lf_shoulder_guideShape.iog.og[0].gid";
connectAttr "CJW_selectPannel_hi_lambert_01SG.mwc" "Lf_shoulder_guideShape.iog.og[0].gco"
		;
connectAttr "groupId1488.id" "LfArm_Switch_guideShape.iog.og[0].gid";
connectAttr "CJW_selectPannel_polySurface95_f_0__lambertSG.mwc" "LfArm_Switch_guideShape.iog.og[0].gco"
		;
connectAttr "groupId1509.id" "RtLeg_hip_ctrl_guideShape.iog.og[0].gid";
connectAttr "CJW_selectPannel_hi_lambert_01SG.mwc" "RtLeg_hip_ctrl_guideShape.iog.og[0].gco"
		;
connectAttr "groupId1511.id" "RtLeg_Switch_guideShape.iog.og[0].gid";
connectAttr "CJW_selectPannel_polySurface95_f_0__lambertSG.mwc" "RtLeg_Switch_guideShape.iog.og[0].gco"
		;
connectAttr "groupId1492.id" "LfLeg_hip_ctrl_guideShape.iog.og[0].gid";
connectAttr "CJW_selectPannel_hi_lambert_01SG.mwc" "LfLeg_hip_ctrl_guideShape.iog.og[0].gco"
		;
connectAttr "groupId1494.id" "LfLeg_Switch_guideShape.iog.og[0].gid";
connectAttr "CJW_selectPannel_polySurface95_f_0__lambertSG.mwc" "LfLeg_Switch_guideShape.iog.og[0].gco"
		;
connectAttr "groupId1480.id" "waist_Ctrl_guideShape.iog.og[0].gid";
connectAttr "CJW_selectPannel_hi_lambert_01SG.mwc" "waist_Ctrl_guideShape.iog.og[0].gco"
		;
connectAttr "groupId1481.id" "Character_guideShape.iog.og[0].gid";
connectAttr "CJW_selectPannel_hi_lambert_01SG.mwc" "Character_guideShape.iog.og[0].gco"
		;
connectAttr "groupId1067.id" "Master_guideShape.iog.og[0].gid";
connectAttr "CJW_selectPannel_polySurface95_f_0__lambertSG.mwc" "Master_guideShape.iog.og[0].gco"
		;
connectAttr "CJW_selectPannel_backgroundColor_lambertSG.msg" "materialInfo17.sg"
		;
connectAttr "CJW_selectPannel_backgroundColor_lambert.msg" "materialInfo17.m";
connectAttr "CJW_selectPannel_backgroundColor_lambert.oc" "CJW_selectPannel_backgroundColor_lambertSG.ss"
		;
connectAttr "FM_Cam_FACIAL_backgroundColor_Shape.iog" "CJW_selectPannel_backgroundColor_lambertSG.dsm"
		 -na;
connectAttr "CJW_selectPannel__lambert_01.oc" "CJW_selectPannel_lambert_01SG.ss"
		;
connectAttr "FM_Cam_characters_FACIAL_backgroundColor_Shape.iog.og[0]" "CJW_selectPannel_lambert_01SG.dsm"
		 -na;
connectAttr "FM_Cam_characters_BODY_picture_Shape.iog.og[0]" "CJW_selectPannel_lambert_01SG.dsm"
		 -na;
connectAttr "FM_Cam_FEET_backgroundColor_Shape.iog.og[0]" "CJW_selectPannel_lambert_01SG.dsm"
		 -na;
connectAttr "FM_Cam_HANDS_backgroundColor_Shape.iog.og[0]" "CJW_selectPannel_lambert_01SG.dsm"
		 -na;
connectAttr "FM_Cam_BODY_backgroundColor_Shape.iog.og[0]" "CJW_selectPannel_lambert_01SG.dsm"
		 -na;
connectAttr "FM_Cam_characters_hands_picture_Shape.iog.og[0]" "CJW_selectPannel_lambert_01SG.dsm"
		 -na;
connectAttr "FM_Cam_characters_feet_picture_Shape.iog.og[0]" "CJW_selectPannel_lambert_01SG.dsm"
		 -na;
connectAttr "groupId1482.msg" "CJW_selectPannel_lambert_01SG.gn" -na;
connectAttr "groupId1483.msg" "CJW_selectPannel_lambert_01SG.gn" -na;
connectAttr "groupId1551.msg" "CJW_selectPannel_lambert_01SG.gn" -na;
connectAttr "groupId1552.msg" "CJW_selectPannel_lambert_01SG.gn" -na;
connectAttr "groupId1553.msg" "CJW_selectPannel_lambert_01SG.gn" -na;
connectAttr "groupId1559.msg" "CJW_selectPannel_lambert_01SG.gn" -na;
connectAttr "groupId1560.msg" "CJW_selectPannel_lambert_01SG.gn" -na;
connectAttr "CJW_selectPannel_lambert_01SG.msg" "p002001MiniTiger_backgroundColor_materialInfo.sg"
		;
connectAttr "CJW_selectPannel__lambert_01.msg" "p002001MiniTiger_backgroundColor_materialInfo.m"
		;
connectAttr "CJW_selectPannel_lambert_file.msg" "p002001MiniTiger_backgroundColor_materialInfo.t"
		 -na;
connectAttr "CJW_selectPannel_lambert_file.oc" "CJW_selectPannel__lambert_01.c";
connectAttr "CJW_selectPannel_place2dTexture.c" "CJW_selectPannel_lambert_file.c"
		;
connectAttr "CJW_selectPannel_place2dTexture.tf" "CJW_selectPannel_lambert_file.tf"
		;
connectAttr "CJW_selectPannel_place2dTexture.rf" "CJW_selectPannel_lambert_file.rf"
		;
connectAttr "CJW_selectPannel_place2dTexture.mu" "CJW_selectPannel_lambert_file.mu"
		;
connectAttr "CJW_selectPannel_place2dTexture.mv" "CJW_selectPannel_lambert_file.mv"
		;
connectAttr "CJW_selectPannel_place2dTexture.s" "CJW_selectPannel_lambert_file.s"
		;
connectAttr "CJW_selectPannel_place2dTexture.wu" "CJW_selectPannel_lambert_file.wu"
		;
connectAttr "CJW_selectPannel_place2dTexture.wv" "CJW_selectPannel_lambert_file.wv"
		;
connectAttr "CJW_selectPannel_place2dTexture.re" "CJW_selectPannel_lambert_file.re"
		;
connectAttr "CJW_selectPannel_place2dTexture.of" "CJW_selectPannel_lambert_file.of"
		;
connectAttr "CJW_selectPannel_place2dTexture.r" "CJW_selectPannel_lambert_file.ro"
		;
connectAttr "CJW_selectPannel_place2dTexture.n" "CJW_selectPannel_lambert_file.n"
		;
connectAttr "CJW_selectPannel_place2dTexture.vt1" "CJW_selectPannel_lambert_file.vt1"
		;
connectAttr "CJW_selectPannel_place2dTexture.vt2" "CJW_selectPannel_lambert_file.vt2"
		;
connectAttr "CJW_selectPannel_place2dTexture.vt3" "CJW_selectPannel_lambert_file.vt3"
		;
connectAttr "CJW_selectPannel_place2dTexture.vc1" "CJW_selectPannel_lambert_file.vc1"
		;
connectAttr "CJW_selectPannel_place2dTexture.o" "CJW_selectPannel_lambert_file.uv"
		;
connectAttr "CJW_selectPannel_place2dTexture.ofs" "CJW_selectPannel_lambert_file.fs"
		;
connectAttr "CJW_selectPannel_selectDefaultSurfaceShaderSG.msg" "materialInfo18.sg"
		;
connectAttr "CJW_selectPannel_selectDefaultSurfaceShader.msg" "materialInfo18.m"
		;
connectAttr "CJW_selectPannel_selectDefaultSurfaceShader.msg" "materialInfo18.t"
		 -na;
connectAttr "CJW_selectPannel_selectDefaultSurfaceShader.oc" "CJW_selectPannel_selectDefaultSurfaceShaderSG.ss"
		;
connectAttr "FM_Cam_characters_FACIAL_backgroundColor_pPlaneShape.iog" "CJW_selectPannel_selectDefaultSurfaceShaderSG.dsm"
		 -na;
connectAttr "CJW_selectPannel_cover_lambertSG.msg" "materialInfo3.sg";
connectAttr "CJW_selectPannel_cover_lambert.msg" "materialInfo3.m";
connectAttr "CJW_selectPannel_cover_lambert.oc" "CJW_selectPannel_cover_lambertSG.ss"
		;
connectAttr "c_Lf_eyebrows_CTRL_backgroundColor_Shape.iog" "CJW_selectPannel_cover_lambertSG.dsm"
		 -na;
connectAttr "c_Rt_eyebrows_CTRL_backgroundColor_Shape.iog" "CJW_selectPannel_cover_lambertSG.dsm"
		 -na;
connectAttr "FM_Cam_r_hi_eye_1_guideShape.iog" "CJW_selectPannel_cover_lambertSG.dsm"
		 -na;
connectAttr "c_Lf_eye_CTRL_backgroundColor_Shape.iog" "CJW_selectPannel_cover_lambertSG.dsm"
		 -na;
connectAttr "FM_Cam_c_hi_mouth_backgroundColor_Shape.iog" "CJW_selectPannel_cover_lambertSG.dsm"
		 -na;
connectAttr "CJW_selectPannel_brow_lambert_01SG.msg" "materialInfo4.sg";
connectAttr "CJW_selectPannel_brow_lambert_01.msg" "materialInfo4.m";
connectAttr "CJW_selectPannel_brow_lambert_01.oc" "CJW_selectPannel_brow_lambert_01SG.ss"
		;
connectAttr "head_stretch_bottom_Ctrl2_guideShape.iog" "CJW_selectPannel_brow_lambert_01SG.dsm"
		 -na;
connectAttr "head_stretch_Ctrl_guideShape.iog" "CJW_selectPannel_brow_lambert_01SG.dsm"
		 -na;
connectAttr "c_nose_fold_CTRL_guideShape.iog" "CJW_selectPannel_brow_lambert_01SG.dsm"
		 -na;
connectAttr "c_Rt_nostril_CTRL_guideShape.iog" "CJW_selectPannel_brow_lambert_01SG.dsm"
		 -na;
connectAttr "c_Lf_nostril_CTRL_guideShape.iog" "CJW_selectPannel_brow_lambert_01SG.dsm"
		 -na;
connectAttr "FM_Cam_c_hi_cover_40_guideShape.iog" "CJW_selectPannel_brow_lambert_01SG.dsm"
		 -na;
connectAttr "FM_Cam_c_hi_cover_29_guideShape.iog" "CJW_selectPannel_brow_lambert_01SG.dsm"
		 -na;
connectAttr "FM_Cam_c_hi_cover_28_guideShape.iog" "CJW_selectPannel_brow_lambert_01SG.dsm"
		 -na;
connectAttr "FM_Cam_c_hi_cover_27_guideShape.iog" "CJW_selectPannel_brow_lambert_01SG.dsm"
		 -na;
connectAttr "FM_Cam_c_hi_cover_32_guideShape.iog" "CJW_selectPannel_brow_lambert_01SG.dsm"
		 -na;
connectAttr "FM_Cam_c_hi_cover_31_guideShape.iog" "CJW_selectPannel_brow_lambert_01SG.dsm"
		 -na;
connectAttr "FM_Cam_c_hi_cover_30_guideShape.iog" "CJW_selectPannel_brow_lambert_01SG.dsm"
		 -na;
connectAttr "c_Rt_eyebrows_02_CTRL_guideShape.iog" "CJW_selectPannel_brow_lambert_01SG.dsm"
		 -na;
connectAttr "c_Rt_eyebrows_01_CTRL_guideShape.iog" "CJW_selectPannel_brow_lambert_01SG.dsm"
		 -na;
connectAttr "c_Lf_eyebrows_01_CTRL_guideShape.iog" "CJW_selectPannel_brow_lambert_01SG.dsm"
		 -na;
connectAttr "c_Lf_eyebrows_02_CTRL_guideShape.iog" "CJW_selectPannel_brow_lambert_01SG.dsm"
		 -na;
connectAttr "FM_Cam_r_hi_eye_3_guideShape.iog" "CJW_selectPannel_brow_lambert_01SG.dsm"
		 -na;
connectAttr "FM_Cam_r_hi_eye_4_guideShape.iog" "CJW_selectPannel_brow_lambert_01SG.dsm"
		 -na;
connectAttr "FM_Cam_r_hi_eye_2_guideShape.iog" "CJW_selectPannel_brow_lambert_01SG.dsm"
		 -na;
connectAttr "FM_Cam_r_hi_eye_5_guideShape.iog" "CJW_selectPannel_brow_lambert_01SG.dsm"
		 -na;
connectAttr "FM_Cam_r_hi_eye_6_guideShape.iog" "CJW_selectPannel_brow_lambert_01SG.dsm"
		 -na;
connectAttr "FM_Cam_r_hi_eye_7_guideShape.iog" "CJW_selectPannel_brow_lambert_01SG.dsm"
		 -na;
connectAttr "FM_Cam_l_hi_eye_7_guideShape.iog" "CJW_selectPannel_brow_lambert_01SG.dsm"
		 -na;
connectAttr "FM_Cam_l_hi_eye_6_guideShape.iog" "CJW_selectPannel_brow_lambert_01SG.dsm"
		 -na;
connectAttr "FM_Cam_l_hi_eye_5_guideShape.iog" "CJW_selectPannel_brow_lambert_01SG.dsm"
		 -na;
connectAttr "FM_Cam_l_hi_eye_4_guideShape.iog" "CJW_selectPannel_brow_lambert_01SG.dsm"
		 -na;
connectAttr "FM_Cam_l_hi_eye_2_guideShape.iog" "CJW_selectPannel_brow_lambert_01SG.dsm"
		 -na;
connectAttr "FM_Cam_l_hi_eye_3_guideShape.iog" "CJW_selectPannel_brow_lambert_01SG.dsm"
		 -na;
connectAttr "CJW_selectPannel_eye_lambertSG.msg" "materialInfo5.sg";
connectAttr "CJW_selectPannel_eye_lambert.msg" "materialInfo5.m";
connectAttr "CJW_selectPannel_eye_lambert.oc" "CJW_selectPannel_eye_lambertSG.ss"
		;
connectAttr "c_Rt_pupil_M_guideShape.iog" "CJW_selectPannel_eye_lambertSG.dsm" -na
		;
connectAttr "c_Lf_pupil_M_guideShape.iog" "CJW_selectPannel_eye_lambertSG.dsm" -na
		;
connectAttr "CJW_selectPannel_cover_lambert_01SG.msg" "materialInfo1.sg";
connectAttr "CJW_selectPannel_cover_lambert_01.msg" "materialInfo1.m";
connectAttr "CJW_selectPannel_cover_lambert_01.oc" "CJW_selectPannel_cover_lambert_01SG.ss"
		;
connectAttr "c_nose_CTRL_guideShape.iog" "CJW_selectPannel_cover_lambert_01SG.dsm"
		 -na;
connectAttr "c_Rt_eyebrows_03_CTRL_guideShape.iog" "CJW_selectPannel_cover_lambert_01SG.dsm"
		 -na;
connectAttr "c_Lf_eyebrows_03_CTRL_guideShape.iog" "CJW_selectPannel_cover_lambert_01SG.dsm"
		 -na;
connectAttr "FM_Cam_l_hi_eye_19_guideShape.iog" "CJW_selectPannel_cover_lambert_01SG.dsm"
		 -na;
connectAttr "FM_Cam_l_hi_eye_17_guideShape.iog" "CJW_selectPannel_cover_lambert_01SG.dsm"
		 -na;
connectAttr "FM_Cam_l_hi_eye_18_guideShape.iog" "CJW_selectPannel_cover_lambert_01SG.dsm"
		 -na;
connectAttr "FM_Cam_r_hi_eye_18_guideShape.iog" "CJW_selectPannel_cover_lambert_01SG.dsm"
		 -na;
connectAttr "FM_Cam_r_hi_eye_17_guideShape.iog" "CJW_selectPannel_cover_lambert_01SG.dsm"
		 -na;
connectAttr "FM_Cam_r_hi_eye_19_guideShape.iog" "CJW_selectPannel_cover_lambert_01SG.dsm"
		 -na;
connectAttr "FM_Cam_r_hi_eye_14_guideShape.iog" "CJW_selectPannel_cover_lambert_01SG.dsm"
		 -na;
connectAttr "FM_Cam_r_hi_eye_15_guideShape.iog" "CJW_selectPannel_cover_lambert_01SG.dsm"
		 -na;
connectAttr "FM_Cam_r_hi_eye_16_guideShape.iog" "CJW_selectPannel_cover_lambert_01SG.dsm"
		 -na;
connectAttr "FM_Cam_l_hi_eye_16_guideShape.iog" "CJW_selectPannel_cover_lambert_01SG.dsm"
		 -na;
connectAttr "FM_Cam_l_hi_eye_15_guideShape.iog" "CJW_selectPannel_cover_lambert_01SG.dsm"
		 -na;
connectAttr "FM_Cam_l_hi_eye_14_guideShape.iog" "CJW_selectPannel_cover_lambert_01SG.dsm"
		 -na;
connectAttr "c_tongue_CTRL_guideShape.iog" "CJW_selectPannel_cover_lambert_01SG.dsm"
		 -na;
connectAttr "head_stretch_top_Ctrl_guideShape.iog" "CJW_selectPannel_cover_lambert_01SG.dsm"
		 -na;
connectAttr "head_stretch_bottom_Ctrl_guideShape.iog" "CJW_selectPannel_cover_lambert_01SG.dsm"
		 -na;
connectAttr "c_muothLip_04_second_CTRL_guideShape.iog" "CJW_selectPannel_cover_lambert_01SG.dsm"
		 -na;
connectAttr "c_muothLip_03_second_CTRL_guideShape.iog" "CJW_selectPannel_cover_lambert_01SG.dsm"
		 -na;
connectAttr "c_muothLip_02_second_CTRL_guideShape.iog" "CJW_selectPannel_cover_lambert_01SG.dsm"
		 -na;
connectAttr "c_muothLip_01_second_CTRL_guideShape.iog" "CJW_selectPannel_cover_lambert_01SG.dsm"
		 -na;
connectAttr "c_muothLip_14_second_CTRL_guideShape.iog" "CJW_selectPannel_cover_lambert_01SG.dsm"
		 -na;
connectAttr "c_muothLip_13_second_CTRL_guideShape.iog" "CJW_selectPannel_cover_lambert_01SG.dsm"
		 -na;
connectAttr "c_muothLip_12_second_CTRL_guideShape.iog" "CJW_selectPannel_cover_lambert_01SG.dsm"
		 -na;
connectAttr "c_muothLip_11_second_CTRL_guideShape.iog" "CJW_selectPannel_cover_lambert_01SG.dsm"
		 -na;
connectAttr "c_muothLip_10_second_CTRL_guideShape.iog" "CJW_selectPannel_cover_lambert_01SG.dsm"
		 -na;
connectAttr "c_muothLip_09_second_CTRL_guideShape.iog" "CJW_selectPannel_cover_lambert_01SG.dsm"
		 -na;
connectAttr "c_muothLip_08_second_CTRL_guideShape.iog" "CJW_selectPannel_cover_lambert_01SG.dsm"
		 -na;
connectAttr "c_muothLip_07_second_CTRL_guideShape.iog" "CJW_selectPannel_cover_lambert_01SG.dsm"
		 -na;
connectAttr "c_muothLip_05_second_CTRL_guideShape.iog" "CJW_selectPannel_cover_lambert_01SG.dsm"
		 -na;
connectAttr "c_muothLip_06_second_CTRL_guideShape.iog" "CJW_selectPannel_cover_lambert_01SG.dsm"
		 -na;
connectAttr "c_jaw_dn_CTRL_guideShape.iog" "CJW_selectPannel_cover_lambert_01SG.dsm"
		 -na;
connectAttr "FM_Cam_r_hi_eye_9_guideShape.iog" "CJW_selectPannel_cover_lambert_01SG.dsm"
		 -na;
connectAttr "FM_Cam_r_hi_eye_10_guideShape.iog" "CJW_selectPannel_cover_lambert_01SG.dsm"
		 -na;
connectAttr "FM_Cam_l_hi_eye_9_guideShape.iog" "CJW_selectPannel_cover_lambert_01SG.dsm"
		 -na;
connectAttr "FM_Cam_l_hi_eye_10_guideShape.iog" "CJW_selectPannel_cover_lambert_01SG.dsm"
		 -na;
connectAttr "c_Rt_eyeStretch_CTRL_guideShape.iog" "CJW_selectPannel_cover_lambert_01SG.dsm"
		 -na;
connectAttr "c_Lf_eyeStretch_CTRL_guideShape.iog" "CJW_selectPannel_cover_lambert_01SG.dsm"
		 -na;
connectAttr "c_Lf_nosewing_CTRL_guide1Shape.iog" "CJW_selectPannel_cover_lambert_01SG.dsm"
		 -na;
connectAttr "c_Rt_spec_M_guideShape.iog" "CJW_selectPannel_cover_lambert_01SG.dsm"
		 -na;
connectAttr "c_Lf_spec_M_guideShape.iog" "CJW_selectPannel_cover_lambert_01SG.dsm"
		 -na;
connectAttr "c_Rt_nosewing_CTRL_guide1Shape.iog" "CJW_selectPannel_cover_lambert_01SG.dsm"
		 -na;
connectAttr "c_Rt_nosewing_CTRL_guideShape.iog.og[0]" "CJW_selectPannel_cover_lambert_01SG.dsm"
		 -na;
connectAttr "c_Lf_nosewing_CTRL_guideShape.iog.og[0]" "CJW_selectPannel_cover_lambert_01SG.dsm"
		 -na;
connectAttr "Lfknee1_bend_guideShape.iog" "CJW_selectPannel_cover_lambert_01SG.dsm"
		 -na;
connectAttr "Lfleg1_bend_guideShape.iog" "CJW_selectPannel_cover_lambert_01SG.dsm"
		 -na;
connectAttr "Rtknee1_bend_guideShape.iog" "CJW_selectPannel_cover_lambert_01SG.dsm"
		 -na;
connectAttr "Rtleg1_bend_guideShape.iog" "CJW_selectPannel_cover_lambert_01SG.dsm"
		 -na;
connectAttr "LfupArm1_bend_guideShape.iog" "CJW_selectPannel_cover_lambert_01SG.dsm"
		 -na;
connectAttr "Lfelbow1_bend_guideShape.iog" "CJW_selectPannel_cover_lambert_01SG.dsm"
		 -na;
connectAttr "RtupArm1_bend_guideShape.iog" "CJW_selectPannel_cover_lambert_01SG.dsm"
		 -na;
connectAttr "Rtelbow1_bend_guideShape.iog" "CJW_selectPannel_cover_lambert_01SG.dsm"
		 -na;
connectAttr "groupId633.msg" "CJW_selectPannel_cover_lambert_01SG.gn" -na;
connectAttr "groupId634.msg" "CJW_selectPannel_cover_lambert_01SG.gn" -na;
connectAttr "CJW_selectPannel_brow_lambertSG.msg" "materialInfo2.sg";
connectAttr "CJW_selectPannel_brow_lambert.msg" "materialInfo2.m";
connectAttr "CJW_selectPannel_brow_lambert.oc" "CJW_selectPannel_brow_lambertSG.ss"
		;
connectAttr "UpperTooth_Ctrl_guideShape.iog" "CJW_selectPannel_brow_lambertSG.dsm"
		 -na;
connectAttr "LowerTooth_Ctrl_guideShape.iog" "CJW_selectPannel_brow_lambertSG.dsm"
		 -na;
connectAttr "c_up_mouthLip_CTRL_guideShape.iog" "CJW_selectPannel_brow_lambertSG.dsm"
		 -na;
connectAttr "c_dn_mouthLip_CTRL_guideShape.iog" "CJW_selectPannel_brow_lambertSG.dsm"
		 -na;
connectAttr "c_mouthLip_CTRL_guideShape.iog" "CJW_selectPannel_brow_lambertSG.dsm"
		 -na;
connectAttr "c_Rt_mouthLip_CTRL_guideShape.iog" "CJW_selectPannel_brow_lambertSG.dsm"
		 -na;
connectAttr "c_Lf_mouthLip_CTRL_guideShape.iog" "CJW_selectPannel_brow_lambertSG.dsm"
		 -na;
connectAttr "c_Rt_cheek_CTRL_guideShape.iog" "CJW_selectPannel_brow_lambertSG.dsm"
		 -na;
connectAttr "c_Lf_cheek_CTRL_guideShape.iog" "CJW_selectPannel_brow_lambertSG.dsm"
		 -na;
connectAttr "FM_Cam_c_hi_cover_38_guideShape.iog" "CJW_selectPannel_brow_lambertSG.dsm"
		 -na;
connectAttr "FM_Cam_c_hi_cover_42_guideShape.iog" "CJW_selectPannel_brow_lambertSG.dsm"
		 -na;
connectAttr "FM_Cam_c_hi_cover_44_guideShape.iog" "CJW_selectPannel_brow_lambertSG.dsm"
		 -na;
connectAttr "FM_Cam_r_hi_eye_11_guideShape.iog" "CJW_selectPannel_brow_lambertSG.dsm"
		 -na;
connectAttr "FM_Cam_l_hi_eye_11_guideShape.iog" "CJW_selectPannel_brow_lambertSG.dsm"
		 -na;
connectAttr "c_Rt_brows_05_CTRL_guideShape.iog" "CJW_selectPannel_brow_lambertSG.dsm"
		 -na;
connectAttr "c_Rt_brows_04_CTRL_guideShape.iog" "CJW_selectPannel_brow_lambertSG.dsm"
		 -na;
connectAttr "c_Rt_brows_03_CTRL_guideShape.iog" "CJW_selectPannel_brow_lambertSG.dsm"
		 -na;
connectAttr "c_Rt_brows_02_CTRL_guideShape.iog" "CJW_selectPannel_brow_lambertSG.dsm"
		 -na;
connectAttr "c_Rt_brows_01_CTRL_guideShape.iog" "CJW_selectPannel_brow_lambertSG.dsm"
		 -na;
connectAttr "c_Lf_brows_01_CTRL_guideShape.iog" "CJW_selectPannel_brow_lambertSG.dsm"
		 -na;
connectAttr "c_Lf_brows_02_CTRL_guideShape.iog" "CJW_selectPannel_brow_lambertSG.dsm"
		 -na;
connectAttr "c_Lf_brows_03_CTRL_guideShape.iog" "CJW_selectPannel_brow_lambertSG.dsm"
		 -na;
connectAttr "c_Lf_brows_04_CTRL_guideShape.iog" "CJW_selectPannel_brow_lambertSG.dsm"
		 -na;
connectAttr "c_Lf_brows_05_CTRL_guideShape.iog" "CJW_selectPannel_brow_lambertSG.dsm"
		 -na;
connectAttr "FM_Cam_c_hi_cover_36_guideShape.iog" "CJW_selectPannel_brow_lambertSG.dsm"
		 -na;
connectAttr "CJW_selectPannel_brow_lambert_01SG1.msg" "materialInfo6.sg";
connectAttr "CJW_selectPannel_brow_lambert_02.msg" "materialInfo6.m";
connectAttr "CJW_selectPannel_brow_lambert_02.oc" "CJW_selectPannel_brow_lambert_01SG1.ss"
		;
connectAttr "LowerTooth_second01_Ctrl_guideShape.iog" "CJW_selectPannel_brow_lambert_01SG1.dsm"
		 -na;
connectAttr "c_Rt_eyebrows_CTRL_guideShape.iog" "CJW_selectPannel_brow_lambert_01SG1.dsm"
		 -na;
connectAttr "c_Lf_eyebrows_CTRL_guideShape.iog" "CJW_selectPannel_brow_lambert_01SG1.dsm"
		 -na;
connectAttr "c_Rt_up_eyelids_CTRL_guideShape.iog" "CJW_selectPannel_brow_lambert_01SG1.dsm"
		 -na;
connectAttr "c_Rt_dn_eyelids_CTRL_guideShape.iog" "CJW_selectPannel_brow_lambert_01SG1.dsm"
		 -na;
connectAttr "c_Lf_dn_eyelids_CTRL_guideShape.iog" "CJW_selectPannel_brow_lambert_01SG1.dsm"
		 -na;
connectAttr "c_Lf_up_eyelids_CTRL_guideShape.iog" "CJW_selectPannel_brow_lambert_01SG1.dsm"
		 -na;
connectAttr "c_Lf_eye_M_guideShape.iog" "CJW_selectPannel_brow_lambert_01SG1.dsm"
		 -na;
connectAttr "c_Rt_eye_M_guideShape.iog" "CJW_selectPannel_brow_lambert_01SG1.dsm"
		 -na;
connectAttr "UpperTooth_second01_Ctrl_guideShape.iog" "CJW_selectPannel_brow_lambert_01SG1.dsm"
		 -na;
connectAttr "UpperTooth_second02_Ctrl_guideShape.iog" "CJW_selectPannel_brow_lambert_01SG1.dsm"
		 -na;
connectAttr "UpperTooth_second04_Ctrl_guideShape.iog" "CJW_selectPannel_brow_lambert_01SG1.dsm"
		 -na;
connectAttr "UpperTooth_second05_Ctrl_guideShape.iog" "CJW_selectPannel_brow_lambert_01SG1.dsm"
		 -na;
connectAttr "UpperTooth_second03_Ctrl_guideShape.iog" "CJW_selectPannel_brow_lambert_01SG1.dsm"
		 -na;
connectAttr "FM_Cam_l_feet_letter_Shape.iog" "CJW_selectPannel_brow_lambert_01SG1.dsm"
		 -na;
connectAttr "FM_Cam_r_feet_letter_Shape.iog" "CJW_selectPannel_brow_lambert_01SG1.dsm"
		 -na;
connectAttr "FM_Cam_l_hands_letter_Shape.iog" "CJW_selectPannel_brow_lambert_01SG1.dsm"
		 -na;
connectAttr "FM_Cam_r_hands_letter_Shape.iog" "CJW_selectPannel_brow_lambert_01SG1.dsm"
		 -na;
connectAttr "FM_Cam_l_body_letter_Shape.iog" "CJW_selectPannel_brow_lambert_01SG1.dsm"
		 -na;
connectAttr "FM_Cam_r_body_letter_Shape.iog" "CJW_selectPannel_brow_lambert_01SG1.dsm"
		 -na;
connectAttr "LowerTooth_second02_Ctrl_guideShape.iog" "CJW_selectPannel_brow_lambert_01SG1.dsm"
		 -na;
connectAttr "LowerTooth_second04_CtrlguideShape.iog" "CJW_selectPannel_brow_lambert_01SG1.dsm"
		 -na;
connectAttr "LowerTooth_second05_Ctrl_guideShape.iog" "CJW_selectPannel_brow_lambert_01SG1.dsm"
		 -na;
connectAttr "LowerTooth_second03_Ctrl_guideShape.iog" "CJW_selectPannel_brow_lambert_01SG1.dsm"
		 -na;
connectAttr "CJW_selectPannel_hi_lambert_01SG.msg" "AA_materialInfo16.sg";
connectAttr "CJW_selectPannel_hi_lambert_01.msg" "AA_materialInfo16.m";
connectAttr "CJW_selectPannel_hi_lambert_01.oc" "CJW_selectPannel_hi_lambert_01SG.ss"
		;
connectAttr "waist_Ctrl_guideShape.iog.og[0]" "CJW_selectPannel_hi_lambert_01SG.dsm"
		 -na;
connectAttr "Character_guideShape.iog.og[0]" "CJW_selectPannel_hi_lambert_01SG.dsm"
		 -na;
connectAttr "Lf_shoulder_guideShape.iog.og[0]" "CJW_selectPannel_hi_lambert_01SG.dsm"
		 -na;
connectAttr "LfLeg_hip_ctrl_guideShape.iog.og[0]" "CJW_selectPannel_hi_lambert_01SG.dsm"
		 -na;
connectAttr "Rt_shoulder_guideShape.iog.og[0]" "CJW_selectPannel_hi_lambert_01SG.dsm"
		 -na;
connectAttr "RtLeg_hip_ctrl_guideShape.iog.og[0]" "CJW_selectPannel_hi_lambert_01SG.dsm"
		 -na;
connectAttr "c_Rt_eyelids_CTRL_guideShape.iog" "CJW_selectPannel_hi_lambert_01SG.dsm"
		 -na;
connectAttr "c_Lf_eyelids_CTRL_guideShape.iog" "CJW_selectPannel_hi_lambert_01SG.dsm"
		 -na;
connectAttr "groupId1480.msg" "CJW_selectPannel_hi_lambert_01SG.gn" -na;
connectAttr "groupId1481.msg" "CJW_selectPannel_hi_lambert_01SG.gn" -na;
connectAttr "groupId1485.msg" "CJW_selectPannel_hi_lambert_01SG.gn" -na;
connectAttr "groupId1492.msg" "CJW_selectPannel_hi_lambert_01SG.gn" -na;
connectAttr "groupId1500.msg" "CJW_selectPannel_hi_lambert_01SG.gn" -na;
connectAttr "groupId1509.msg" "CJW_selectPannel_hi_lambert_01SG.gn" -na;
connectAttr "CJW_selectPannel_hand_lambertSG.msg" "p002001MiniTiger_hand_materialInfo.sg"
		;
connectAttr "CJW_selectPannel_hand_lambert.msg" "p002001MiniTiger_hand_materialInfo.m"
		;
connectAttr "CJW_selectPannel_hand_lambert_file.msg" "p002001MiniTiger_hand_materialInfo.t"
		 -na;
connectAttr "CJW_selectPannel_hand_lambert.oc" "CJW_selectPannel_hand_lambertSG.ss"
		;
connectAttr "c_Rt_ear_CTRL_guideShape.iog" "CJW_selectPannel_hand_lambertSG.dsm"
		 -na;
connectAttr "c_Lf_ear_CTRL_guideShape.iog" "CJW_selectPannel_hand_lambertSG.dsm"
		 -na;
connectAttr "FM_Cam_c_hi_hand_9_guideShape.iog" "CJW_selectPannel_hand_lambertSG.dsm"
		 -na;
connectAttr "FM_Cam_c_hi_hand_8_guideShape.iog" "CJW_selectPannel_hand_lambertSG.dsm"
		 -na;
connectAttr "FM_Cam_c_hi_hand_7_guideShape.iog" "CJW_selectPannel_hand_lambertSG.dsm"
		 -na;
connectAttr "FM_Cam_c_hi_hand_6_guideShape.iog" "CJW_selectPannel_hand_lambertSG.dsm"
		 -na;
connectAttr "FM_Cam_c_hi_hand_5_guideShape.iog" "CJW_selectPannel_hand_lambertSG.dsm"
		 -na;
connectAttr "FM_Cam_c_hi_hand_4_guideShape.iog" "CJW_selectPannel_hand_lambertSG.dsm"
		 -na;
connectAttr "FM_Cam_c_hi_hand_3_guideShape.iog" "CJW_selectPannel_hand_lambertSG.dsm"
		 -na;
connectAttr "FM_Cam_c_hi_hand_2_guideShape.iog" "CJW_selectPannel_hand_lambertSG.dsm"
		 -na;
connectAttr "FM_Cam_c_hi_hand_1_guideShape.iog" "CJW_selectPannel_hand_lambertSG.dsm"
		 -na;
connectAttr "top_waist_ikCtrl_guideShape.iog" "CJW_selectPannel_hand_lambertSG.dsm"
		 -na;
connectAttr "mid_waist_ikCtrl_guideShape.iog" "CJW_selectPannel_hand_lambertSG.dsm"
		 -na;
connectAttr "root_waist_ikCtrl_guideShape.iog" "CJW_selectPannel_hand_lambertSG.dsm"
		 -na;
connectAttr "RtLeg_foot_guideShape.iog" "CJW_selectPannel_hand_lambertSG.dsm" -na
		;
connectAttr "LfLeg_foot_guideShape.iog" "CJW_selectPannel_hand_lambertSG.dsm" -na
		;
connectAttr "LfLeg_Leg_IK_guideShape.iog" "CJW_selectPannel_hand_lambertSG.dsm" 
		-na;
connectAttr "LfLeg_Pole_ctrl_guideShape.iog" "CJW_selectPannel_hand_lambertSG.dsm"
		 -na;
connectAttr "RtLeg_Leg_IK_guideShape.iog" "CJW_selectPannel_hand_lambertSG.dsm" 
		-na;
connectAttr "RtLeg_Pole_ctrl_guideShape.iog" "CJW_selectPannel_hand_lambertSG.dsm"
		 -na;
connectAttr "LfArm_Pole_ctrl_guideShape.iog" "CJW_selectPannel_hand_lambertSG.dsm"
		 -na;
connectAttr "LfArm_Wrist_IK_guideShape.iog" "CJW_selectPannel_hand_lambertSG.dsm"
		 -na;
connectAttr "RtArm_Pole_ctrl_guideShape.iog" "CJW_selectPannel_hand_lambertSG.dsm"
		 -na;
connectAttr "RtArm_Wrist_IK_guideShape.iog" "CJW_selectPannel_hand_lambertSG.dsm"
		 -na;
connectAttr "FM_Cam_l_hi_arm1_Shape.iog" "CJW_selectPannel_hand_lambertSG.dsm" -na
		;
connectAttr "c_eye_M_guideShape.iog" "CJW_selectPannel_hand_lambertSG.dsm" -na;
connectAttr "CJW_selectPannel_hand_lambert_file.oc" "CJW_selectPannel_hand_lambert.c"
		;
connectAttr "CJW_selectPannel_place2dTexture1.c" "CJW_selectPannel_hand_lambert_file.c"
		;
connectAttr "CJW_selectPannel_place2dTexture1.tf" "CJW_selectPannel_hand_lambert_file.tf"
		;
connectAttr "CJW_selectPannel_place2dTexture1.rf" "CJW_selectPannel_hand_lambert_file.rf"
		;
connectAttr "CJW_selectPannel_place2dTexture1.mu" "CJW_selectPannel_hand_lambert_file.mu"
		;
connectAttr "CJW_selectPannel_place2dTexture1.mv" "CJW_selectPannel_hand_lambert_file.mv"
		;
connectAttr "CJW_selectPannel_place2dTexture1.s" "CJW_selectPannel_hand_lambert_file.s"
		;
connectAttr "CJW_selectPannel_place2dTexture1.wu" "CJW_selectPannel_hand_lambert_file.wu"
		;
connectAttr "CJW_selectPannel_place2dTexture1.wv" "CJW_selectPannel_hand_lambert_file.wv"
		;
connectAttr "CJW_selectPannel_place2dTexture1.re" "CJW_selectPannel_hand_lambert_file.re"
		;
connectAttr "CJW_selectPannel_place2dTexture1.of" "CJW_selectPannel_hand_lambert_file.of"
		;
connectAttr "CJW_selectPannel_place2dTexture1.r" "CJW_selectPannel_hand_lambert_file.ro"
		;
connectAttr "CJW_selectPannel_place2dTexture1.n" "CJW_selectPannel_hand_lambert_file.n"
		;
connectAttr "CJW_selectPannel_place2dTexture1.vt1" "CJW_selectPannel_hand_lambert_file.vt1"
		;
connectAttr "CJW_selectPannel_place2dTexture1.vt2" "CJW_selectPannel_hand_lambert_file.vt2"
		;
connectAttr "CJW_selectPannel_place2dTexture1.vt3" "CJW_selectPannel_hand_lambert_file.vt3"
		;
connectAttr "CJW_selectPannel_place2dTexture1.vc1" "CJW_selectPannel_hand_lambert_file.vc1"
		;
connectAttr "CJW_selectPannel_place2dTexture1.o" "CJW_selectPannel_hand_lambert_file.uv"
		;
connectAttr "CJW_selectPannel_place2dTexture1.ofs" "CJW_selectPannel_hand_lambert_file.fs"
		;
connectAttr "CJW_selectPannel_body_lambertSG.msg" "materialInfo7.sg";
connectAttr "CJW_selectPannel_body_lambert.msg" "materialInfo7.m";
connectAttr "CJW_selectPannel_body_lambert.oc" "CJW_selectPannel_body_lambertSG.ss"
		;
connectAttr "FM_Cam_c_hi_cover_39_guideShape.iog" "CJW_selectPannel_body_lambertSG.dsm"
		 -na;
connectAttr "FM_Cam_c_hi_cover_37_guideShape.iog" "CJW_selectPannel_body_lambertSG.dsm"
		 -na;
connectAttr "|FM_Caml_gui_guides_grp|FM_Cam_BODY_gui_guides_grp|FM_Cam_c_hi_body_|FM_Cam_l_hi_crura_|To_Feet_View|To_Feet_ViewShape.iog" "CJW_selectPannel_body_lambertSG.dsm"
		 -na;
connectAttr "|FM_Caml_gui_guides_grp|FM_Cam_BODY_gui_guides_grp|FM_Cam_c_hi_body_|FM_Cam_r_hi_crura_|To_Feet_View|To_Feet_ViewShape.iog" "CJW_selectPannel_body_lambertSG.dsm"
		 -na;
connectAttr "|FM_Caml_gui_guides_grp|FM_Cam_BODY_gui_guides_grp|FM_Cam_c_hi_body_|FM_Cam_l_hi_arm_|To_Hands_View|To_Hands_ViewShape.iog" "CJW_selectPannel_body_lambertSG.dsm"
		 -na;
connectAttr "|FM_Caml_gui_guides_grp|FM_Cam_BODY_gui_guides_grp|FM_Cam_c_hi_body_|FM_Cam_r_hi_arm_|To_Hands_View|To_Hands_ViewShape.iog" "CJW_selectPannel_body_lambertSG.dsm"
		 -na;
connectAttr "deleteComponent12.og" "deleteComponent13.ig";
connectAttr "polyTweak11.out" "deleteComponent12.ig";
connectAttr "polySplit6.out" "polyTweak11.ip";
connectAttr "polySplit5.out" "polySplit6.ip";
connectAttr "polySurfaceShape3.o" "polySplit5.ip";
connectAttr "CJW_selectPannel_tongue_lambertSG.msg" "materialInfo9.sg";
connectAttr "CJW_selectPannel_tongue_lambert.msg" "materialInfo9.m";
connectAttr "CJW_selectPannel_tongue_lambert.oc" "CJW_selectPannel_tongue_lambertSG.ss"
		;
connectAttr "FM_Cam_c_hi_tongue_5_guideShape.iog" "CJW_selectPannel_tongue_lambertSG.dsm"
		 -na;
connectAttr "FM_Cam_c_hi_tongue_2_guideShape.iog" "CJW_selectPannel_tongue_lambertSG.dsm"
		 -na;
connectAttr "FM_Cam_c_hi_tongue_4_guideShape.iog" "CJW_selectPannel_tongue_lambertSG.dsm"
		 -na;
connectAttr "FM_Cam_c_hi_tongue_1_guideShape.iog" "CJW_selectPannel_tongue_lambertSG.dsm"
		 -na;
connectAttr "FM_Cam_c_hi_tongue_10_guideShape.iog.og[0]" "CJW_selectPannel_tongue_lambertSG.dsm"
		 -na;
connectAttr "FM_Cam_c_hi_tongue_11_guideShape.iog.og[0]" "CJW_selectPannel_tongue_lambertSG.dsm"
		 -na;
connectAttr "c_tongue_joint8_guideShape.iog" "CJW_selectPannel_tongue_lambertSG.dsm"
		 -na;
connectAttr "c_tongue_joint10_guideShape.iog" "CJW_selectPannel_tongue_lambertSG.dsm"
		 -na;
connectAttr "c_tongue_joint7_guideShape.iog" "CJW_selectPannel_tongue_lambertSG.dsm"
		 -na;
connectAttr "c_tongue_joint11_guideShape.iog" "CJW_selectPannel_tongue_lambertSG.dsm"
		 -na;
connectAttr "c_tongue_joint6_guideShape.iog" "CJW_selectPannel_tongue_lambertSG.dsm"
		 -na;
connectAttr "c_tongue_joint1_guideShape.iog" "CJW_selectPannel_tongue_lambertSG.dsm"
		 -na;
connectAttr "c_tongue_joint9_guideShape.iog" "CJW_selectPannel_tongue_lambertSG.dsm"
		 -na;
connectAttr "c_tongue_joint12_guideShape.iog" "CJW_selectPannel_tongue_lambertSG.dsm"
		 -na;
connectAttr "c_tongue_joint4_guideShape.iog" "CJW_selectPannel_tongue_lambertSG.dsm"
		 -na;
connectAttr "c_tongue_joint3_guideShape.iog" "CJW_selectPannel_tongue_lambertSG.dsm"
		 -na;
connectAttr "c_tongue_joint5_guideShape.iog" "CJW_selectPannel_tongue_lambertSG.dsm"
		 -na;
connectAttr "c_tongue_joint2_guideShape.iog" "CJW_selectPannel_tongue_lambertSG.dsm"
		 -na;
connectAttr "groupId1564.msg" "CJW_selectPannel_tongue_lambertSG.gn" -na;
connectAttr "groupId1565.msg" "CJW_selectPannel_tongue_lambertSG.gn" -na;
connectAttr "polyTweak10.out" "deleteComponent11.ig";
connectAttr "polySplit2.out" "polyTweak10.ip";
connectAttr "polySplit1.out" "polySplit2.ip";
connectAttr "polySurfaceShape1.o" "polySplit1.ip";
connectAttr "CJW_selectPannel_tongue_lambert_01SG.msg" "materialInfo8.sg";
connectAttr "CJW_selectPannel_tongue_lambert_01.msg" "materialInfo8.m";
connectAttr "CJW_selectPannel_tongue_lambert_01.oc" "CJW_selectPannel_tongue_lambert_01SG.ss"
		;
connectAttr "deleteComponent14.og" "deleteComponent15.ig";
connectAttr "polyTweak12.out" "deleteComponent14.ig";
connectAttr "polySplit14.out" "polyTweak12.ip";
connectAttr "polySplit13.out" "polySplit14.ip";
connectAttr "polySurfaceShape6.o" "polySplit13.ip";
connectAttr "deleteComponent21.og" "deleteComponent22.ig";
connectAttr "polyTweak14.out" "deleteComponent21.ig";
connectAttr "polySplit8.out" "polyTweak14.ip";
connectAttr "polySplit7.out" "polySplit8.ip";
connectAttr "polySurfaceShape4.o" "polySplit7.ip";
connectAttr "deleteComponent26.og" "deleteComponent27.ig";
connectAttr "deleteComponent25.og" "deleteComponent26.ig";
connectAttr "deleteComponent24.og" "deleteComponent25.ig";
connectAttr "deleteComponent23.og" "deleteComponent24.ig";
connectAttr "polyTweak15.out" "deleteComponent23.ig";
connectAttr "polySplit24.out" "polyTweak15.ip";
connectAttr "polySplit21.out" "polySplit24.ip";
connectAttr "polySplit16.out" "polySplit21.ip";
connectAttr "polySplit15.out" "polySplit16.ip";
connectAttr "groupParts1.og" "polySplit15.ip";
connectAttr "polySurfaceShape7.o" "groupParts1.ig";
connectAttr "groupId1564.id" "groupParts1.gi";
connectAttr "deleteComponent19.og" "deleteComponent20.ig";
connectAttr "deleteComponent18.og" "deleteComponent19.ig";
connectAttr "deleteComponent17.og" "deleteComponent18.ig";
connectAttr "deleteComponent16.og" "deleteComponent17.ig";
connectAttr "polyTweak13.out" "deleteComponent16.ig";
connectAttr "polySplit26.out" "polyTweak13.ip";
connectAttr "polySplit23.out" "polySplit26.ip";
connectAttr "polySplit20.out" "polySplit23.ip";
connectAttr "polySplit19.out" "polySplit20.ip";
connectAttr "groupParts2.og" "polySplit19.ip";
connectAttr "polySurfaceShape9.o" "groupParts2.ig";
connectAttr "groupId1565.id" "groupParts2.gi";
connectAttr "CJW_selectPannel__lambertSG.msg" "p002001MiniTiger_polySurface212_f_0__materialInfo.sg"
		;
connectAttr "CJW_selectPannel__lambert.msg" "p002001MiniTiger_polySurface212_f_0__materialInfo.m"
		;
connectAttr "CJW_selectPannel__lambert_ramp.msg" "p002001MiniTiger_polySurface212_f_0__materialInfo.t"
		 -na;
connectAttr "CJW_selectPannel__lambert.oc" "CJW_selectPannel__lambertSG.ss";
connectAttr "head_ctrl_guideShape.iog" "CJW_selectPannel__lambertSG.dsm" -na;
connectAttr "neck_FK_ctrl_guideShape.iog" "CJW_selectPannel__lambertSG.dsm" -na;
connectAttr "RtArm_UpArm_FK_guideShape.iog" "CJW_selectPannel__lambertSG.dsm" -na
		;
connectAttr "LfArm_UpArm_FK_guideShape.iog" "CJW_selectPannel__lambertSG.dsm" -na
		;
connectAttr "RtArm_Elbow_FK_guideShape.iog" "CJW_selectPannel__lambertSG.dsm" -na
		;
connectAttr "RtArm_Wrist_FK_guideShape.iog" "CJW_selectPannel__lambertSG.dsm" -na
		;
connectAttr "LfArm_Elbow_FK_guideShape.iog" "CJW_selectPannel__lambertSG.dsm" -na
		;
connectAttr "LfArm_Wrist_FK_guideShape.iog" "CJW_selectPannel__lambertSG.dsm" -na
		;
connectAttr "waist_FK2_ctrl_guideShape.iog" "CJW_selectPannel__lambertSG.dsm" -na
		;
connectAttr "waist_FK1_ctrl_guideShape.iog" "CJW_selectPannel__lambertSG.dsm" -na
		;
connectAttr "RtLeg_Leg_FK_guideShape.iog" "CJW_selectPannel__lambertSG.dsm" -na;
connectAttr "LfLeg_Leg_FK_guideShape.iog" "CJW_selectPannel__lambertSG.dsm" -na;
connectAttr "RtLeg_Knee_FK_guideShape.iog" "CJW_selectPannel__lambertSG.dsm" -na
		;
connectAttr "LfLeg_Knee_FK_guideShape.iog" "CJW_selectPannel__lambertSG.dsm" -na
		;
connectAttr "LfLeg_Ankle_FK_guideShape.iog" "CJW_selectPannel__lambertSG.dsm" -na
		;
connectAttr "RtLeg_Ankle_FK_guideShape.iog" "CJW_selectPannel__lambertSG.dsm" -na
		;
connectAttr "LfLegLeg_ball_FK_guideShape.iog" "CJW_selectPannel__lambertSG.dsm" 
		-na;
connectAttr "RtLegLeg_ball_FK_guideShape.iog" "CJW_selectPannel__lambertSG.dsm" 
		-na;
connectAttr "Lf_Toe_pinky3_guideShape.iog" "CJW_selectPannel__lambertSG.dsm" -na
		;
connectAttr "Lf_Toe_pinky2_guideShape.iog" "CJW_selectPannel__lambertSG.dsm" -na
		;
connectAttr "Lf_Toe_pinky1_guideShape.iog" "CJW_selectPannel__lambertSG.dsm" -na
		;
connectAttr "Lf_Toe_ring1_guideShape.iog" "CJW_selectPannel__lambertSG.dsm" -na;
connectAttr "Lf_Toe_ring2_guideShape.iog" "CJW_selectPannel__lambertSG.dsm" -na;
connectAttr "Lf_Toe_ring3_guideShape.iog" "CJW_selectPannel__lambertSG.dsm" -na;
connectAttr "Lf_Toe_mid3_guideShape.iog" "CJW_selectPannel__lambertSG.dsm" -na;
connectAttr "Lf_Toe_mid2_guideShape.iog" "CJW_selectPannel__lambertSG.dsm" -na;
connectAttr "Lf_Toe_mid1_guideShape.iog" "CJW_selectPannel__lambertSG.dsm" -na;
connectAttr "Lf_Toe_index1_guideShape.iog" "CJW_selectPannel__lambertSG.dsm" -na
		;
connectAttr "Lf_Toe_index2_guideShape.iog" "CJW_selectPannel__lambertSG.dsm" -na
		;
connectAttr "Lf_Toe_index3_guideShape.iog" "CJW_selectPannel__lambertSG.dsm" -na
		;
connectAttr "Lf_Toe_thumb1_guideShape.iog" "CJW_selectPannel__lambertSG.dsm" -na
		;
connectAttr "Lf_Toe_thumb2_guideShape.iog" "CJW_selectPannel__lambertSG.dsm" -na
		;
connectAttr "Lf_Toe_thumb3_guideShape.iog" "CJW_selectPannel__lambertSG.dsm" -na
		;
connectAttr "Lf_thumb2_guideShape.iog" "CJW_selectPannel__lambertSG.dsm" -na;
connectAttr "Lf_thumb3_guideShape.iog" "CJW_selectPannel__lambertSG.dsm" -na;
connectAttr "Lf_index1_guideShape.iog" "CJW_selectPannel__lambertSG.dsm" -na;
connectAttr "Lf_index2_guideShape.iog" "CJW_selectPannel__lambertSG.dsm" -na;
connectAttr "Lf_index3_guideShape.iog" "CJW_selectPannel__lambertSG.dsm" -na;
connectAttr "Lf_mid2_guideShape.iog" "CJW_selectPannel__lambertSG.dsm" -na;
connectAttr "Lf_mid1_guideShape.iog" "CJW_selectPannel__lambertSG.dsm" -na;
connectAttr "Lf_mid3_guideShape.iog" "CJW_selectPannel__lambertSG.dsm" -na;
connectAttr "Lf_ring3_guideShape.iog" "CJW_selectPannel__lambertSG.dsm" -na;
connectAttr "Lf_ring2_guideShape.iog" "CJW_selectPannel__lambertSG.dsm" -na;
connectAttr "Lf_ring1_guideShape.iog" "CJW_selectPannel__lambertSG.dsm" -na;
connectAttr "Lf_pinky1_guideShape.iog" "CJW_selectPannel__lambertSG.dsm" -na;
connectAttr "Lf_pinky2_guideShape.iog" "CJW_selectPannel__lambertSG.dsm" -na;
connectAttr "Lf_pinky3_guideShape.iog" "CJW_selectPannel__lambertSG.dsm" -na;
connectAttr "Rt_Toe_thumb3_guideShape.iog.og[0]" "CJW_selectPannel__lambertSG.dsm"
		 -na;
connectAttr "Rt_Toe_thumb2_guideShape.iog.og[0]" "CJW_selectPannel__lambertSG.dsm"
		 -na;
connectAttr "Rt_Toe_thumb1_guideShape.iog.og[0]" "CJW_selectPannel__lambertSG.dsm"
		 -na;
connectAttr "Rt_Toe_index3_guideShape.iog.og[0]" "CJW_selectPannel__lambertSG.dsm"
		 -na;
connectAttr "Rt_Toe_index2_guideShape.iog.og[0]" "CJW_selectPannel__lambertSG.dsm"
		 -na;
connectAttr "Rt_Toe_index1_guideShape.iog.og[0]" "CJW_selectPannel__lambertSG.dsm"
		 -na;
connectAttr "Rt_Toe_mid1_guideShape.iog.og[0]" "CJW_selectPannel__lambertSG.dsm"
		 -na;
connectAttr "Rt_Toe_mid2_guideShape.iog.og[0]" "CJW_selectPannel__lambertSG.dsm"
		 -na;
connectAttr "Rt_Toe_mid3_guideShape.iog.og[0]" "CJW_selectPannel__lambertSG.dsm"
		 -na;
connectAttr "Rt_Toe_ring3_guideShape.iog.og[0]" "CJW_selectPannel__lambertSG.dsm"
		 -na;
connectAttr "Rt_Toe_ring2_guideShape.iog.og[0]" "CJW_selectPannel__lambertSG.dsm"
		 -na;
connectAttr "Rt_Toe_ring1_guideShape.iog.og[0]" "CJW_selectPannel__lambertSG.dsm"
		 -na;
connectAttr "Rt_Toe_pinky3_guideShape.iog.og[0]" "CJW_selectPannel__lambertSG.dsm"
		 -na;
connectAttr "Rt_Toe_pinky2_guideShape.iog.og[0]" "CJW_selectPannel__lambertSG.dsm"
		 -na;
connectAttr "Rt_Toe_pinky1_guideShape.iog.og[0]" "CJW_selectPannel__lambertSG.dsm"
		 -na;
connectAttr "Rt_thumb3_guideShape.iog.og[0]" "CJW_selectPannel__lambertSG.dsm" -na
		;
connectAttr "Rt_thumb2_guideShape.iog.og[0]" "CJW_selectPannel__lambertSG.dsm" -na
		;
connectAttr "Rt_index3_guideShape.iog.og[0]" "CJW_selectPannel__lambertSG.dsm" -na
		;
connectAttr "Rt_index2_guideShape.iog.og[0]" "CJW_selectPannel__lambertSG.dsm" -na
		;
connectAttr "Rt_index1_guideShape.iog.og[0]" "CJW_selectPannel__lambertSG.dsm" -na
		;
connectAttr "Rt_mid1_guideShape.iog.og[0]" "CJW_selectPannel__lambertSG.dsm" -na
		;
connectAttr "Rt_mid2_guideShape.iog.og[0]" "CJW_selectPannel__lambertSG.dsm" -na
		;
connectAttr "Rt_mid3_guideShape.iog.og[0]" "CJW_selectPannel__lambertSG.dsm" -na
		;
connectAttr "Rt_ring3_guideShape.iog.og[0]" "CJW_selectPannel__lambertSG.dsm" -na
		;
connectAttr "Rt_ring2_guideShape.iog.og[0]" "CJW_selectPannel__lambertSG.dsm" -na
		;
connectAttr "Rt_ring1_guideShape.iog.og[0]" "CJW_selectPannel__lambertSG.dsm" -na
		;
connectAttr "Rt_pinky1_guideShape.iog.og[0]" "CJW_selectPannel__lambertSG.dsm" -na
		;
connectAttr "Rt_pinky2_guideShape.iog.og[0]" "CJW_selectPannel__lambertSG.dsm" -na
		;
connectAttr "Rt_pinky3_guideShape.iog.og[0]" "CJW_selectPannel__lambertSG.dsm" -na
		;
connectAttr "Lf_thumb1_guideShape.iog" "CJW_selectPannel__lambertSG.dsm" -na;
connectAttr "Rt_thumb1_guideShape.iog.og[0]" "CJW_selectPannel__lambertSG.dsm" -na
		;
connectAttr "groupId1517.msg" "CJW_selectPannel__lambertSG.gn" -na;
connectAttr "groupId1518.msg" "CJW_selectPannel__lambertSG.gn" -na;
connectAttr "groupId1519.msg" "CJW_selectPannel__lambertSG.gn" -na;
connectAttr "groupId1520.msg" "CJW_selectPannel__lambertSG.gn" -na;
connectAttr "groupId1521.msg" "CJW_selectPannel__lambertSG.gn" -na;
connectAttr "groupId1522.msg" "CJW_selectPannel__lambertSG.gn" -na;
connectAttr "groupId1523.msg" "CJW_selectPannel__lambertSG.gn" -na;
connectAttr "groupId1524.msg" "CJW_selectPannel__lambertSG.gn" -na;
connectAttr "groupId1525.msg" "CJW_selectPannel__lambertSG.gn" -na;
connectAttr "groupId1526.msg" "CJW_selectPannel__lambertSG.gn" -na;
connectAttr "groupId1527.msg" "CJW_selectPannel__lambertSG.gn" -na;
connectAttr "groupId1528.msg" "CJW_selectPannel__lambertSG.gn" -na;
connectAttr "groupId1529.msg" "CJW_selectPannel__lambertSG.gn" -na;
connectAttr "groupId1530.msg" "CJW_selectPannel__lambertSG.gn" -na;
connectAttr "groupId1531.msg" "CJW_selectPannel__lambertSG.gn" -na;
connectAttr "groupId1532.msg" "CJW_selectPannel__lambertSG.gn" -na;
connectAttr "groupId1533.msg" "CJW_selectPannel__lambertSG.gn" -na;
connectAttr "groupId1534.msg" "CJW_selectPannel__lambertSG.gn" -na;
connectAttr "groupId1535.msg" "CJW_selectPannel__lambertSG.gn" -na;
connectAttr "groupId1536.msg" "CJW_selectPannel__lambertSG.gn" -na;
connectAttr "groupId1537.msg" "CJW_selectPannel__lambertSG.gn" -na;
connectAttr "groupId1538.msg" "CJW_selectPannel__lambertSG.gn" -na;
connectAttr "groupId1539.msg" "CJW_selectPannel__lambertSG.gn" -na;
connectAttr "groupId1540.msg" "CJW_selectPannel__lambertSG.gn" -na;
connectAttr "groupId1541.msg" "CJW_selectPannel__lambertSG.gn" -na;
connectAttr "groupId1542.msg" "CJW_selectPannel__lambertSG.gn" -na;
connectAttr "groupId1543.msg" "CJW_selectPannel__lambertSG.gn" -na;
connectAttr "groupId1544.msg" "CJW_selectPannel__lambertSG.gn" -na;
connectAttr "groupId1545.msg" "CJW_selectPannel__lambertSG.gn" -na;
connectAttr "groupId1554.msg" "CJW_selectPannel__lambertSG.gn" -na;
connectAttr "CJW_selectPannel__lambert_ramp.oc" "CJW_selectPannel__lambert.c";
connectAttr "CJW_selectPannel__place2dTexture.o" "CJW_selectPannel__lambert_ramp.uv"
		;
connectAttr "CJW_selectPannel__place2dTexture.ofs" "CJW_selectPannel__lambert_ramp.fs"
		;
connectAttr "CJW_selectPannel_polySurface95_f_0__lambert.oc" "CJW_selectPannel_polySurface95_f_0__lambertSG.ss"
		;
connectAttr "Master_guideShape.iog.og[0]" "CJW_selectPannel_polySurface95_f_0__lambertSG.dsm"
		 -na;
connectAttr "LfArm_Switch_guideShape.iog.og[0]" "CJW_selectPannel_polySurface95_f_0__lambertSG.dsm"
		 -na;
connectAttr "LfLeg_Switch_guideShape.iog.og[0]" "CJW_selectPannel_polySurface95_f_0__lambertSG.dsm"
		 -na;
connectAttr "RtArm_Switch_guideShape.iog.og[0]" "CJW_selectPannel_polySurface95_f_0__lambertSG.dsm"
		 -na;
connectAttr "RtLeg_Switch_guideShape.iog.og[0]" "CJW_selectPannel_polySurface95_f_0__lambertSG.dsm"
		 -na;
connectAttr "groupId1067.msg" "CJW_selectPannel_polySurface95_f_0__lambertSG.gn"
		 -na;
connectAttr "groupId1488.msg" "CJW_selectPannel_polySurface95_f_0__lambertSG.gn"
		 -na;
connectAttr "groupId1494.msg" "CJW_selectPannel_polySurface95_f_0__lambertSG.gn"
		 -na;
connectAttr "groupId1503.msg" "CJW_selectPannel_polySurface95_f_0__lambertSG.gn"
		 -na;
connectAttr "groupId1511.msg" "CJW_selectPannel_polySurface95_f_0__lambertSG.gn"
		 -na;
connectAttr "CJW_selectPannel_polySurface95_f_0__lambertSG.msg" "AA_materialInfo11.sg"
		;
connectAttr "CJW_selectPannel_polySurface95_f_0__lambert.msg" "AA_materialInfo11.m"
		;
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "CJW_selectPannel_cover_lambert_01SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "CJW_selectPannel_brow_lambertSG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "CJW_selectPannel_cover_lambertSG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "CJW_selectPannel_brow_lambert_01SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "CJW_selectPannel_eye_lambertSG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "CJW_selectPannel_brow_lambert_01SG1.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "CJW_selectPannel_body_lambertSG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "CJW_selectPannel_tongue_lambert_01SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "CJW_selectPannel_tongue_lambertSG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "CJW_selectPannel_hand_lambertSG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "CJW_selectPannel_backgroundColor_lambertSG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "CJW_selectPannel_selectDefaultSurfaceShaderSG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "CJW_selectPannel_polySurface95_f_0__lambertSG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "CJW_selectPannel_hi_lambert_01SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "CJW_selectPannel_lambert_01SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "CJW_selectPannel__lambertSG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "CJW_selectPannel_cover_lambert_01SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "CJW_selectPannel_brow_lambertSG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "CJW_selectPannel_cover_lambertSG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "CJW_selectPannel_brow_lambert_01SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "CJW_selectPannel_eye_lambertSG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "CJW_selectPannel_brow_lambert_01SG1.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "CJW_selectPannel_body_lambertSG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "CJW_selectPannel_tongue_lambert_01SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "CJW_selectPannel_tongue_lambertSG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "CJW_selectPannel_hand_lambertSG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "CJW_selectPannel_backgroundColor_lambertSG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "CJW_selectPannel_selectDefaultSurfaceShaderSG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "CJW_selectPannel_polySurface95_f_0__lambertSG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "CJW_selectPannel_hi_lambert_01SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "CJW_selectPannel_lambert_01SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "CJW_selectPannel__lambertSG.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "hyperView1.msg" "nodeEditorPanel1Info.b[0]";
connectAttr "hyperLayout1.msg" "hyperView1.hl";
connectAttr ":persp.msg" "hyperLayout1.hyp[0].dn";
connectAttr ":perspShape.msg" "hyperLayout1.hyp[1].dn";
connectAttr ":top.msg" "hyperLayout1.hyp[2].dn";
connectAttr ":topShape.msg" "hyperLayout1.hyp[3].dn";
connectAttr ":front.msg" "hyperLayout1.hyp[4].dn";
connectAttr ":frontShape.msg" "hyperLayout1.hyp[5].dn";
connectAttr ":side.msg" "hyperLayout1.hyp[6].dn";
connectAttr ":sideShape.msg" "hyperLayout1.hyp[7].dn";
connectAttr "layerManager.msg" "hyperLayout1.hyp[8].dn";
connectAttr "defaultLayer.msg" "hyperLayout1.hyp[9].dn";
connectAttr "defaultRenderLayer.msg" "hyperLayout1.hyp[10].dn";
connectAttr "c_tongue_joint2_guide.msg" "hyperLayout1.hyp[11].dn";
connectAttr "c_tongue_joint2_guideShape.msg" "hyperLayout1.hyp[12].dn";
connectAttr "c_tongue_joint3_guide.msg" "hyperLayout1.hyp[13].dn";
connectAttr "c_tongue_joint3_guideShape.msg" "hyperLayout1.hyp[14].dn";
connectAttr "|FM_Caml_gui_guides_grp|FM_Cam_FACIAL_gui_guides_grp|FM_Cam_c_hi_face|FM_Cam_c_hi_tongue|c_tongue_joint3_guide|polySurfaceShape11.msg" "hyperLayout1.hyp[15].dn"
		;
connectAttr "c_tongue_joint4_guide.msg" "hyperLayout1.hyp[16].dn";
connectAttr "c_tongue_joint4_guideShape.msg" "hyperLayout1.hyp[17].dn";
connectAttr "|FM_Caml_gui_guides_grp|FM_Cam_FACIAL_gui_guides_grp|FM_Cam_c_hi_face|FM_Cam_c_hi_tongue|c_tongue_joint4_guide|polySurfaceShape11.msg" "hyperLayout1.hyp[18].dn"
		;
connectAttr "uiConfigurationScriptNode.msg" "hyperLayout1.hyp[19].dn";
connectAttr "sceneConfigurationScriptNode.msg" "hyperLayout1.hyp[20].dn";
connectAttr "c_tongue_joint5_guide.msg" "hyperLayout1.hyp[21].dn";
connectAttr "c_tongue_joint5_guideShape.msg" "hyperLayout1.hyp[22].dn";
connectAttr "|FM_Caml_gui_guides_grp|FM_Cam_FACIAL_gui_guides_grp|FM_Cam_c_hi_face|FM_Cam_c_hi_tongue|c_tongue_joint5_guide|polySurfaceShape11.msg" "hyperLayout1.hyp[23].dn"
		;
connectAttr "c_tongue_joint6_guide.msg" "hyperLayout1.hyp[24].dn";
connectAttr "c_tongue_joint6_guideShape.msg" "hyperLayout1.hyp[25].dn";
connectAttr "|FM_Caml_gui_guides_grp|FM_Cam_FACIAL_gui_guides_grp|FM_Cam_c_hi_face|FM_Cam_c_hi_tongue|c_tongue_joint6_guide|polySurfaceShape11.msg" "hyperLayout1.hyp[26].dn"
		;
connectAttr "c_tongue_joint7_guide.msg" "hyperLayout1.hyp[27].dn";
connectAttr "c_tongue_joint7_guideShape.msg" "hyperLayout1.hyp[28].dn";
connectAttr "|FM_Caml_gui_guides_grp|FM_Cam_FACIAL_gui_guides_grp|FM_Cam_c_hi_face|FM_Cam_c_hi_tongue|c_tongue_joint7_guide|polySurfaceShape11.msg" "hyperLayout1.hyp[29].dn"
		;
connectAttr "c_tongue_joint8_guide.msg" "hyperLayout1.hyp[30].dn";
connectAttr "c_tongue_joint8_guideShape.msg" "hyperLayout1.hyp[31].dn";
connectAttr "|FM_Caml_gui_guides_grp|FM_Cam_FACIAL_gui_guides_grp|FM_Cam_c_hi_face|FM_Cam_c_hi_tongue|c_tongue_joint8_guide|polySurfaceShape11.msg" "hyperLayout1.hyp[32].dn"
		;
connectAttr "|FM_Caml_gui_guides_grp|FM_Cam_FACIAL_gui_guides_grp|FM_Cam_c_hi_face|FM_Cam_c_hi_tongue|c_tongue_joint2_guide|polySurfaceShape11.msg" "hyperLayout1.hyp[33].dn"
		;
connectAttr "polySplit30.msg" "hyperLayout1.hyp[34].dn";
connectAttr "c_tongue_joint9_guide.msg" "hyperLayout1.hyp[35].dn";
connectAttr "c_tongue_joint9_guideShape.msg" "hyperLayout1.hyp[36].dn";
connectAttr "|FM_Caml_gui_guides_grp|FM_Cam_FACIAL_gui_guides_grp|FM_Cam_c_hi_face|FM_Cam_c_hi_tongue|c_tongue_joint9_guide|polySurfaceShape11.msg" "hyperLayout1.hyp[37].dn"
		;
connectAttr "c_tongue_joint10_guide.msg" "hyperLayout1.hyp[38].dn";
connectAttr "c_tongue_joint10_guideShape.msg" "hyperLayout1.hyp[39].dn";
connectAttr "|FM_Caml_gui_guides_grp|FM_Cam_FACIAL_gui_guides_grp|FM_Cam_c_hi_face|FM_Cam_c_hi_tongue|c_tongue_joint10_guide|polySurfaceShape11.msg" "hyperLayout1.hyp[40].dn"
		;
connectAttr "c_tongue_joint11_guide.msg" "hyperLayout1.hyp[41].dn";
connectAttr "c_tongue_joint11_guideShape.msg" "hyperLayout1.hyp[42].dn";
connectAttr "|FM_Caml_gui_guides_grp|FM_Cam_FACIAL_gui_guides_grp|FM_Cam_c_hi_face|FM_Cam_c_hi_tongue|c_tongue_joint11_guide|polySurfaceShape11.msg" "hyperLayout1.hyp[43].dn"
		;
connectAttr "c_tongue_joint12_guide.msg" "hyperLayout1.hyp[44].dn";
connectAttr "c_tongue_joint12_guideShape.msg" "hyperLayout1.hyp[45].dn";
connectAttr "|FM_Caml_gui_guides_grp|FM_Cam_FACIAL_gui_guides_grp|FM_Cam_c_hi_face|FM_Cam_c_hi_tongue|c_tongue_joint12_guide|polySurfaceShape11.msg" "hyperLayout1.hyp[46].dn"
		;
connectAttr "c_tongue_joint1_guide.msg" "hyperLayout1.hyp[47].dn";
connectAttr "c_tongue_joint1_guideShape.msg" "hyperLayout1.hyp[48].dn";
connectAttr "|FM_Caml_gui_guides_grp|FM_Cam_FACIAL_gui_guides_grp|FM_Cam_c_hi_face|FM_Cam_c_hi_tongue|c_tongue_joint1_guide|polySurfaceShape11.msg" "hyperLayout1.hyp[49].dn"
		;
connectAttr "|FM_Caml_gui_guides_grp|FM_Cam_FACIAL_gui_guides_grp|FM_Cam_c_hi_face|FM_Cam_c_hi_tongue|c_tongue_joint2_guide|polySurfaceShape11.o" "polySplit30.ip"
		;
connectAttr "CJW_selectPannel_cover_lambert_01SG.pa" ":renderPartition.st" -na;
connectAttr "CJW_selectPannel_brow_lambertSG.pa" ":renderPartition.st" -na;
connectAttr "CJW_selectPannel_cover_lambertSG.pa" ":renderPartition.st" -na;
connectAttr "CJW_selectPannel_brow_lambert_01SG.pa" ":renderPartition.st" -na;
connectAttr "CJW_selectPannel_eye_lambertSG.pa" ":renderPartition.st" -na;
connectAttr "CJW_selectPannel_brow_lambert_01SG1.pa" ":renderPartition.st" -na;
connectAttr "CJW_selectPannel_body_lambertSG.pa" ":renderPartition.st" -na;
connectAttr "CJW_selectPannel_tongue_lambert_01SG.pa" ":renderPartition.st" -na;
connectAttr "CJW_selectPannel_tongue_lambertSG.pa" ":renderPartition.st" -na;
connectAttr "CJW_selectPannel_hand_lambertSG.pa" ":renderPartition.st" -na;
connectAttr "CJW_selectPannel_backgroundColor_lambertSG.pa" ":renderPartition.st"
		 -na;
connectAttr "CJW_selectPannel_selectDefaultSurfaceShaderSG.pa" ":renderPartition.st"
		 -na;
connectAttr "CJW_selectPannel_polySurface95_f_0__lambertSG.pa" ":renderPartition.st"
		 -na;
connectAttr "CJW_selectPannel_hi_lambert_01SG.pa" ":renderPartition.st" -na;
connectAttr "CJW_selectPannel_lambert_01SG.pa" ":renderPartition.st" -na;
connectAttr "CJW_selectPannel__lambertSG.pa" ":renderPartition.st" -na;
connectAttr "CJW_selectPannel_cover_lambert_01.msg" ":defaultShaderList1.s" -na;
connectAttr "CJW_selectPannel_brow_lambert.msg" ":defaultShaderList1.s" -na;
connectAttr "CJW_selectPannel_cover_lambert.msg" ":defaultShaderList1.s" -na;
connectAttr "CJW_selectPannel_brow_lambert_01.msg" ":defaultShaderList1.s" -na;
connectAttr "CJW_selectPannel_eye_lambert.msg" ":defaultShaderList1.s" -na;
connectAttr "CJW_selectPannel_brow_lambert_02.msg" ":defaultShaderList1.s" -na;
connectAttr "CJW_selectPannel_body_lambert.msg" ":defaultShaderList1.s" -na;
connectAttr "CJW_selectPannel_tongue_lambert_01.msg" ":defaultShaderList1.s" -na
		;
connectAttr "CJW_selectPannel_tongue_lambert.msg" ":defaultShaderList1.s" -na;
connectAttr "CJW_selectPannel_hand_lambert.msg" ":defaultShaderList1.s" -na;
connectAttr "CJW_selectPannel_backgroundColor_lambert.msg" ":defaultShaderList1.s"
		 -na;
connectAttr "CJW_selectPannel_selectDefaultSurfaceShader.msg" ":defaultShaderList1.s"
		 -na;
connectAttr "CJW_selectPannel_polySurface95_f_0__lambert.msg" ":defaultShaderList1.s"
		 -na;
connectAttr "CJW_selectPannel_hi_lambert_01.msg" ":defaultShaderList1.s" -na;
connectAttr "CJW_selectPannel__lambert_01.msg" ":defaultShaderList1.s" -na;
connectAttr "CJW_selectPannel__lambert.msg" ":defaultShaderList1.s" -na;
connectAttr "CJW_selectPannel_hand_lambert_file.msg" ":defaultTextureList1.tx" -na
		;
connectAttr "CJW_selectPannel_lambert_file.msg" ":defaultTextureList1.tx" -na;
connectAttr "CJW_selectPannel__lambert_ramp.msg" ":defaultTextureList1.tx" -na;
connectAttr "CJW_selectPannel_place2dTexture1.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "CJW_selectPannel_place2dTexture.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "CJW_selectPannel__place2dTexture.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
connectAttr ":perspShape.msg" ":defaultRenderGlobals.sc";
// End of High_selectPannel_rig.ma

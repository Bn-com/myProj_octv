# Auto batch process for Agisoft Metashape
# @ H.GONG 2017/02/22

import Metashape
import os,re,sys
import datetime
# get the photo (.JPG) list in specified folder
def getPhotoList(root_path, photoList):
	pattern = '.JPG$'
	for root, dirs, files in os.walk(root_path):
		for name in files:
			if re.search(pattern,name):
				cur_path = os.path.join(root, name)
				#print (cur_path)
				photoList.append(cur_path)
			
def MetashapeProcess(root_path):
	data_record = {}
	data_record['1_startTime'] = datetime.datetime.now()
	#Metashape.app.messageBox('hello world! \n')
	Metashape.app.console.clear()

	## construct the document class
	doc = Metashape.app.document

	## save project
	#doc.open("M:/Metashape/practise.psx")
	psxfile = root_path + 'practise.psx'
	doc.save( psxfile )
	print ('>> Saved to: ' + psxfile)

	## point to current chunk
	#chunk = doc.chunk

	## add a new chunk
	chunk = doc.addChunk()

	## set coordinate system
	# - Metashape.CoordinateSystem("EPSG::4612") -->  JGD2000
	chunk.crs = Metashape.CoordinateSystem("EPSG::4612")

	################################################################################################
	### get photo list ###
	photoList = []
	getPhotoList(root_path, photoList)
	#print (photoList)
	
	################################################################################################
	### add photos ###
	# addPhotos(filenames[, progress])
	# - filenames(list of string) – A list of file paths.
	chunk.addPhotos(photoList)
	data_record['2_start_alignPhoto'] = datetime.datetime.now()
	################################################################################################
	### align photos ###
	## Perform image matching for the chunk frame.
	# matchPhotos(accuracy=HighAccuracy, preselection=NoPreselection, filter_mask=False, keypoint_limit=40000, tiepoint_limit=4000[, progress])
	# - Alignment accuracy in [HighestAccuracy, HighAccuracy, MediumAccuracy, LowAccuracy, LowestAccuracy]
	# - Image pair preselection in [ReferencePreselection, GenericPreselection, NoPreselection]
	# chunk.matchPhotos(accuracy=Metashape.LowAccuracy, preselection=Metashape.ReferencePreselection, filter_mask=False, keypoint_limit=0, tiepoint_limit=0)
	chunk.matchPhotos(downscale=5, generic_preselection=1,reference_preselection=0,filter_mask=False, keypoint_limit=0, tiepoint_limit=0)
	chunk.alignCameras()

	################################################################################################
	### build dense cloud ###
	data_record['3_start_cloud'] = datetime.datetime.now()
	## Generate depth maps for the chunk.
	# buildDenseCloud(quality=MediumQuality, filter=AggressiveFiltering[, cameras], keep_depth=False, reuse_depth=False[, progress])
	# - Dense point cloud quality in [UltraQuality, HighQuality, MediumQuality, LowQuality, LowestQuality]
	# - Depth filtering mode in [AggressiveFiltering, ModerateFiltering, MildFiltering, NoFiltering]
	# chunk.buildDenseCloud(quality=Metashape.LowQuality, filter=Metashape.AggressiveFiltering)
	# chunk.buildDenseCloud(quality=Metashape.LowestQuality, filter=Metashape.NoFiltering)
	chunk.buildDepthMaps(downscale=5,filter_mode=Metashape.NoFiltering)
	chunk.buildDenseCloud()

	################################################################################################
	### build mesh ###
	data_record['4_start_mesh'] = datetime.datetime.now()
	## Generate model for the chunk frame.
	# buildModel(surface=Arbitrary, interpolation=EnabledInterpolation, face_count=MediumFaceCount[, source ][, classes][, progress])
	# - Surface type in [Arbitrary, HeightField]
	# - Interpolation mode in [EnabledInterpolation, DisabledInterpolation, Extrapolated]
	# - Face count in [HighFaceCount, MediumFaceCount, LowFaceCount]
	# - Data source in [PointCloudData, DenseCloudData, ModelData, ElevationData]
	# chunk.buildModel(surface=Metashape.HeightField, interpolation=Metashape.EnabledInterpolation, face_count=Metashape.HighFaceCount)
	chunk.buildModel(surface_type=Metashape.Arbitrary, interpolation=Metashape.DisabledInterpolation, face_count=Metashape.LowFaceCount)

	################################################################################################
	### build texture (optional) ###
	data_record['5_start_textrue'] = datetime.datetime.now()
	## Generate uv mapping for the model.
	# buildUV(mapping=GenericMapping, count=1[, camera ][, progress])
	# - UV mapping mode in [GenericMapping, OrthophotoMapping, AdaptiveOrthophotoMapping, SphericalMapping, CameraMapping]
	# chunk.buildUV(mapping=Metashape.AdaptiveOrthophotoMapping)
	# chunk.buildUV(mapping=Metashape.SphericalMapping)
	chunk.buildUV(mapping_mode=Metashape.OrthophotoMapping)
	## Generate texture for the chunk.
	# buildTexture(blending=MosaicBlending, color_correction=False, size=2048[, cameras][, progress])
	# - Blending mode in [AverageBlending, MosaicBlending, MinBlending, MaxBlending, DisabledBlending]
	# chunk.buildTexture(blending=Metashape.MosaicBlending, color_correction=True, size=30000)
	# chunk.buildTexture(blending=Metashape.MosaicBlending, color_correction=True, texture_size=1024)
	chunk.buildTexture(blending_mode=Metashape.MosaicBlending, texture_size=1024)

	################################################################################################
	## save the project before build the DEM and Ortho images
	doc.save()
	data_record['6_ENDING...'] = datetime.datetime.now()
	################################################################################################
	### build DEM (before build dem, you need to save the project into psx) ###
	## Build elevation model for the chunk.
	# buildDem(source=DenseCloudData, interpolation=EnabledInterpolation[, projection ][, region ][, classes][, progress])
	# - Data source in [PointCloudData, DenseCloudData, ModelData, ElevationData]
	# chunk.buildDem(source=Metashape.DenseCloudData, interpolation=Metashape.EnabledInterpolation, projection=chunk.crs)

	################################################################################################
	## Build orthomosaic for the chunk.
	# buildOrthomosaic(surface=ElevationData, blending=MosaicBlending, color_correction=False[, projection ][, region ][, dx ][, dy ][, progress])
	# - Data source in [PointCloudData, DenseCloudData, ModelData, ElevationData]
	# - Blending mode in [AverageBlending, MosaicBlending, MinBlending, MaxBlending, DisabledBlending]
	# chunk.buildOrthomosaic(surface=Metashape.ModelData, blending=Metashape.MosaicBlending, color_correction=True, projection=chunk.crs)
	
	################################################################################################
	## auto classify ground points (optional)
	#chunk.dense_cloud.classifyGroundPoints()
	#chunk.buildDem(source=Metashape.DenseCloudData, classes=[2])
	
	################################################################################################
	doc.save()
	labs = list(data_record.keys())
	labs.sort()
	start_time, end_time = 0, 0
	for n in range(len(labs)):
		if n == 0 :start_time = data_record[labs[n]]
		elif n == len(labs)-1:end_time = data_record[labs[n]]
		print("{}{}   : {}".format(labs[n],os.linesep,data_record[labs[n]]))
	print(">>>Total Consume TIme: {}".format(end_time-start_time))
# main
if __name__ == "__main__":
	Path = sys.argv[1]
	#folder = "J:/projs/Photos/"
	# MetashapeProcess(folder)
	MetashapeProcess(Path)









"""
buildDenseCloud


2020-05-11 10:52:46 BuildDenseCloud: quality = Lowest, depth filtering = Mild, point colors = 1
2020-05-11 10:52:46 Error: Operation not applicable
2020-05-11 10:52:46 BuildDenseCloud: quality = Lowest, depth filtering = Mild, point colors = 1
2020-05-11 10:52:46 Error: Operation not applicable
2020-05-11 10:52:46 BuildDenseCloud: quality = Lowest, depth filtering = Mild, point colors = 1
2020-05-11 10:52:46 Generating depth maps...
2020-05-11 10:52:46 Initializing...
"""
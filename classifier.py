#!/usr/bin/env python
# coding: utf-8

import numpy as np
from django.contrib.gis.gdal import GDALRaster
import subprocess
from PIL import Image
import os
from joblib import dump, load
import sys
from progress.bar import Bar
from postprocessor import get_adjacent_indices

Image.MAX_IMAGE_PIXELS = None

def path_maker(path):
	if not os.path.exists(path):
		os.makedirs(path)


def l1c_classifier(inputDir, outputDir, modelDir):

	file_name = inputDir + '.png'

	for root, dirs, files in os.walk(inputDir, topdown = False):
		for name in dirs:
			if name == 'IMG_DATA':
				inpath = os.path.abspath(os.path.join(root, name)) + '/'

	model_path = os.path.join(modelDir,'Model.joblib')

	path_maker(outputDir)

# reading 13 bands
	inpath = os.path.join(inpath,'*_B*.jp2')

	# storing vrt file
	outPath = os.path.join(outputDir,'resampled_stack.vrt')

	# getting band value
	command = "gdalbuildvrt -resolution user -tr 20 20 -separate -overwrite {0} {1}".format(outPath,inpath)
	subprocess.run(command, shell=True)

	rast = GDALRaster(outPath)
	rastersBands = []
	index_arr = []
	for band in rast.bands:
		b = band.data()
		rastersBands.append(b)

	# indexs = cal_index(rastersBands[0],rastersBands[1],rastersBands[2],rastersBands[3],rastersBands[4],rastersBands[5],rastersBands[6],rastersBands[7],
	# 				rastersBands[8],rastersBands[9],rastersBands[10],rastersBands[11],rastersBands[12])

	# for index in indexs:
	# 	rastersBands.append(index)

	print('reading 13 bands')
	#print('15 indexs done')
	rasterStack = np.dstack(rastersBands)
	#rasterStack = np.dstack(index_arr)

	X_test = np.expand_dims(rasterStack,axis=0)

	#scaler = load('scaler.gz')
	loaded_model = load(model_path)
	rgbArray = np.zeros((X_test.shape[1],X_test.shape[2],3), 'uint8')
	post_processingArray = np.zeros((X_test.shape[1],X_test.shape[2]),dtype='object')

	bar = Bar('Classifying Image', max = X_test.shape[1])

	def color(row,col,r,g,b):
		rgbArray[row,col, 0] = r * 255
		rgbArray[row,col, 1] = g * 255
		rgbArray[row,col, 2] = b * 255

	ci = cl = ot = sh = sn = wa = 0

	for row in range(X_test.shape[1]):
		#in_arr = scaler.transform(X_test[0][row])
		in_arr = X_test[0][row]
		y_pred = loaded_model.predict(in_arr)
		for class_v,col in zip (y_pred,range(in_arr.shape[0])):
			post_processingArray[row][col] = class_v
			if class_v == 'cirrus':
				ci = ci + 1
				color(row,col,0.733, 0.773, 0.925) # red
			elif class_v == 'cloud':
				cl = cl + 1
				color(row,col,0.949, 0.949, 0.949) # white
			elif class_v == 'other':
				ot = ot + 1
				color(row,col,0, 1, 0) # yellow
			elif class_v == 'shadow':
				sh = sh + 1
				color(row,col,0.467, 0.298, 0.043) # black
			elif class_v == 'snow':
				sn = sn + 1
				color(row,col,0.325, 1, 0.980) # green
			elif class_v == 'water':
				wa = wa + 1
				color(row,col,0, 0, 1) # blue
		bar.next()

	total = ci + cl + ot + sh + sn + wa

	print("\nci-{0}, cl-{1}, ot-{2}, sh-{3}, sn-{4}, wa-{5}, total-{6}\n".format(ci,cl,ot,sh,sn,wa,total))

	img = Image.fromarray(rgbArray,'RGB')
	# storing RGB file
	file_name = 'classified_' + file_name.split('/')[-1]
	RGB_file_path = os.path.join(outputDir,file_name)
	img.save(RGB_file_path)

	print('image saved at',RGB_file_path)


	command = "rm {0}".format(outPath)
	subprocess.run(command, shell=True)

	#np.save('classifying_image.npy',post_processingArray)

	bar.finish()

	bar = Bar('Post Processing', max = X_test.shape[1])

	rgbArray = np.zeros((X_test.shape[1],X_test.shape[2],3), 'uint8')
	m = post_processingArray.shape[0]
	n = post_processingArray.shape[1]

	ci = cl = ot = sh = sn = wa = 0

	for row in range(m):
		for col in range(n):
			class_v = get_adjacent_indices(row,col,m,n,post_processingArray)
			if class_v == 'cirrus':
				ci = ci + 1
				color(row,col,0.733, 0.773, 0.925) # red
			elif class_v == 'cloud':
				cl = cl + 1
				color(row,col,0.949, 0.949, 0.949) # white
			elif class_v == 'other':
				ot = ot + 1
				color(row,col,0, 1, 0) # yellow
			elif class_v == 'shadow':
				sh = sh + 1
				color(row,col,0.467, 0.298, 0.043) # black
			elif class_v == 'snow':
				sn = sn + 1
				color(row,col,0.325, 1, 0.980) # green
			elif class_v == 'water':
				wa = wa + 1
				color(row,col,0, 0, 1) # blue
		bar.next()

	total = ci + cl + ot + sh + sn + wa

	print("\nci-{0}, cl-{1}, ot-{2}, sh-{3}, sn-{4}, wa-{5}, total-{6}\n".format(ci,cl,ot,sh,sn,wa,total))

	img = Image.fromarray(rgbArray,'RGB')
	# storing RGB file
	file_name = 'post_processed_' + file_name.split('/')[-1]
	RGB_file_path = os.path.join(outputDir,file_name)
	img.save(RGB_file_path)

	bar.finish()

	print('image saved at',RGB_file_path)
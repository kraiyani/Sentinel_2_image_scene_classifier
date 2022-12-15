#!/usr/bin/env python
# coding: utf-8

import sys
import getopt
from classifier import l1c_classifier
import os
import warnings
warnings.filterwarnings('ignore')

def error():
	print( 'main.py -i <inputdirectory> -o <outputdirectory>')
	sys.exit()

def getRelevantDirectories(argv):
	inputDir = ''
	outputDir = ''
	modelDir = ''
	
	try:
		opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
	except getopt.GetoptError:
		error()

	for opt, arg in opts:
		if opt == '-h' or len(arg) == 0:
			error()
		if opt in ("-i", "--ifile"):
			inputDir = arg
		if opt in ("-o", "--ofile"):
			outputDir = arg

	if len(opts) == 0 or inputDir == '' or outputDir == '':
		print( 'main.py -i <inputdirectory> -o <outputdirectory>')
		#print( 'The input directory should contain all the training files. \nThe output directory will be where the models are stored.')
		sys.exit()

	modelDir = os.path.abspath(modelDir)
	inputDir = os.path.abspath(inputDir)
	outputDir = os.path.abspath(outputDir)
	return inputDir, outputDir, modelDir

def main():
	inputDir, outputDir, modelDir = getRelevantDirectories(sys.argv[1:])
	l1c_classifier(inputDir, outputDir, modelDir)

if __name__ == '__main__':
	main()
#!/usr/bin/env python
# coding: utf-8

import numpy as np

def cal_index(b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b8a):

	brightness = wetness = avi = bsi = si = ndvi = ndwi = ndsi = ndgi = ndmi = nbri = npcri = ashburn = gvi = sci = 0

	brightness = 0.3037 * b2 + 0.2793 * b3 + 0.4743 * b4 + 0.5585 * b8 + 0.5082 * b10 + 0.1863 * b12

	brightness = np.round(brightness,4)

	wetness = 	0.1509 * b2 + 0.1973 * b3 + 0.3279 * b4 + 0.3406 * b8 - 0.7112 * b11 - 0.4572 * b12

	wetness = np.round(wetness,4)

	temp = (b8 * (1 - b4) * (b8 - b4))

	avi = np.cbrt(temp)
	avi = np.round(avi,4)

	temp = ((1 - b2) * (1 - b3) * (1 - b4))

	si = np.cbrt(temp)
	si = np.round(si,4)

	a = (b3 - b8)
	b = (b3 + b8)
	ndwi = np.divide(a, b, out=np.zeros_like(a), where=b!=0)
	ndwi = np.round(ndwi,4)
	
	a = (b8 - b4)
	b = (b8 + b4)
	ndvi = np.divide(a, b, out=np.zeros_like(a), where=b!=0)
	ndvi = np.round(ndvi,4)

	a = (b3 - b11)
	b = (b3 + b11)
	ndsi = np.divide(a, b, out=np.zeros_like(a), where=b!=0)
	ndsi = np.round(ndsi,4)
	
	a = (b3 - b4)
	b = (b3 + b4)
	ndgi = np.divide(a, b, out=np.zeros_like(a), where=b!=0)
	ndgi = np.round(ndgi,4)

	a = (b8 - b11)
	b = (b8 + b11)
	ndmi = np.divide(a, b, out=np.zeros_like(a), where=b!=0)
	ndmi = np.round(ndmi,4)

	a = (b8 - b12)
	b = (b8 + b12)
	nbri = np.divide(a, b, out=np.zeros_like(a), where=b!=0)
	nbri = np.round(nbri,4)

	a = (b4 - b2)
	b = (b4 + b2)
	npcri = np.divide(a, b, out=np.zeros_like(a), where=b!=0)
	npcri = np.round(npcri,4)

	a = ((b11 + b4) - (b8 + b2))
	b = ((b11 + b4) + (b8 + b2))
	bsi = np.divide(a, b, out=np.zeros_like(a), where=b!=0)
	bsi = np.round(bsi,4)

	ashburn = 2 * (b9 - b4)
	ashburn = np.round(ashburn,4)

	gvi = 0.7243 * b8 + 0.0840 * b11 - 0.1800 * b12 - 0.2848 * b2 - 0.2435 * b3 - 0.5436 * b4
	gvi = np.round(gvi,4)

	a = (b11 - b8)
	b = (b11 + b8)
	sci = np.divide(a, b, out=np.zeros_like(a), where=b!=0)
	sci = np.round(sci,4)

	indexs = [brightness, wetness , avi , bsi , si , ndvi , ndwi , ndsi , ndgi , ndmi , nbri , npcri, ashburn , gvi , sci]

	return indexs

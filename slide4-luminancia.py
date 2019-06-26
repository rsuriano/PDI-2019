# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 21:32:52 2019

@author: Suriano, Ramiro & Armanasco, Matias
"""

import imageio
import numpy as np
import matplotlib.pyplot as plt
import tools

columnQty = 10
escalar = 1
filtro = 3
Ymin = 0.1
Ymax = 1
"""
1 - Raiz
2 - Cuadrado
3 - Lineal a trozos
"""
#Loading image
imgpath = "images\slides4 - Histogram\{}.png"
imgName = input("Select image name: ")
img = imageio.imread(imgpath.format(imgName))
img = img[:,:,:3]/255.


"""Extracts Y layer"""
img_YIQ = tools.convert_to("YIQ", img)
img_Y = img_YIQ[:,:,0]

#Plots original image and luminance histogram
plt.figure(1)
plt.imshow(img)
plt.figure(2)
tools.histogramaY(img_Y, columnQty)


"""Applies luminance change to a copy of img
img2_YIQ = img_YIQ
img2_YIQ[:,:,0] *= escalar
img2_Y = np.clip(img2_YIQ[:,:,0],0.,1.)

img2_YIQ[:,:,0] = img2_Y
img2_RGB = tools.convert_to("RGB", img2_YIQ)

#Plots altered image
plt.figure(3)
plt.imshow(img2_RGB)
plt.figure(4)
tools.histogramaY(img2_YIQ[:,:,0], columnQty)"""


"""Filters the image"""
filteredImg_YIQ = img_YIQ

if filtro == 1:
    filteredImg_YIQ[:,:,0] = np.sqrt(filteredImg_YIQ[:,:,0])
if filtro == 2:
    filteredImg_YIQ[:,:,0] = np.square(filteredImg_YIQ[:,:,0])
if filtro == 3:
    for i in np.ndenumerate(filteredImg_YIQ[:,:,0]):
        if i[1] < Ymin:
            filteredImg_YIQ[i[0][0], i[0][1], 0] = 0
        if i[1] > Ymax:
            filteredImg_YIQ[i[0][0], i[0][1], 0] = 1
        else:
            filteredImg_YIQ[i[0][0], i[0][1], 0] *= 1/(Ymax-Ymin)
    filteredImg_YIQ[:,:,0] = np.clip(filteredImg_YIQ[:,:,0],0.,1.)

filteredImg_RGB = tools.convert_to("RGB", filteredImg_YIQ)

#Plots filtered image
plt.figure(5)
plt.imshow(filteredImg_RGB)
plt.figure(6)
tools.histogramaY(filteredImg_YIQ[:,:,0], columnQty)
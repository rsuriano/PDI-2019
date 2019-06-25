# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 21:32:52 2019

@author: Suriano, Ramiro & Armanasco, Matias
"""

import imageio
import numpy as np
import matplotlib.pyplot as plt
import tools

columnQty = 100
escalar = 1.5
filtro = 1
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

#Extracts Y layer
img_YIQ = tools.convert_to('YIQ', img)
img_Y = img_YIQ[:,:,0]


#Applies luminance change to a copy of img
img2_YIQ = img_YIQ
img2_YIQ[:,:,0] *= escalar
img2_Y = np.clip(img2_YIQ[:,:,0],0.,1.)

img2_YIQ[:,:,0] = img2_Y
img2_RGB = tools.convert_to("RGB", img2_YIQ)


#Filters the image
filteredImg_YIQ = img_YIQ

if filtro == 1:
    filteredImg_YIQ[:,:,0] = np.sqrt(filteredImg_YIQ[:,:,0])
if filtro == 2:
    filteredImg_YIQ[:,:,0] = np.square(filteredImg_YIQ[:,:,0])

filteredImg_RGB = tools.convert_to("RGB", filteredImg_YIQ)


### PLOTS ###

"""Plots original image and luminance histogram"""
plt.figure(1)
plt.imshow(img)
plt.figure(2)
tools.histogramaY(img_Y, columnQty)

"""Plots altered image"""
plt.figure(3)
plt.imshow(img2_RGB)
plt.figure(4)
tools.histogramaY(img2_YIQ[:,:,0], columnQty)

"""Plots filtered image"""
plt.figure(5)
plt.imshow(filteredImg_RGB)
plt.figure(6)
#tools.histogramaY(filteredImg_YIQ[:,:,0], columnQty)
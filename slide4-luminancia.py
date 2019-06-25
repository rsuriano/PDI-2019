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
escalar = 1.5

#Loading image
imgpath = "images\slides4 - Histogram\{}.png"
imgName = input("Select image name: ")
#columnQty = int(input("Number of bars: "))
#advanced = input("Advanced input? Y/N: ")
#advanced = advanced.upper()
#if advanced != "N":
    #escalar = input("Factor de luminancia: ")
    #Takes selection for the filter
    #print("1 - Filtro raiz\n2 - Filtro cuadrado\n3 - Lineal a trozos")
    #chosenFilter = input("Select filter: ")

img = imageio.imread(imgpath.format(imgName))
img = img[:,:,:3]/255.

#Extracts Y layer
img_YIQ = tools.convert_to('YIQ', img)
img_Y = img_YIQ[:,:,0]

#if advanced != "N":
#Applies luminance change to a copy of img
imgAfectada = img_YIQ
imgAfectada[:,:,0] *= escalar
imgAfectada[:,:,0] = np.clip(imgAfectada[:,:,0],0.,1.)
imgAfectada = tools.convert_to("RGB",imgAfectada)

for i in range(3):
    imgAfectada[:,:,i] = np.clip(imgAfectada[:,:,i], 0., 1.)
        
print(img.shape)
print(imgAfectada.shape)

### PLOTS ###

#Plots original image and luminance histogram
plt.figure(1)
#plt.subplot(121)
plt.imshow(img)
#plt.subplot(122)
plt.figure(2)
tools.histogramaY(img_Y, columnQty)
#plt.figure(3)
#plt.hist(img_Y)


#if advanced != "N":
#Plots altered image
plt.figure(3)
#plt.subplot(121)
plt.imshow(imgAfectada)
plt.figure(4)
#plt.subplot(122)
tools.histogramaY(imgAfectada[:,:,0], columnQty)
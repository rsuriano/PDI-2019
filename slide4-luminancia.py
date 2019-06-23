# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 21:32:52 2019

@author: Suriano, Ramiro & Armanasco, Matias
"""

import imageio
import numpy as np
import matplotlib.pyplot as plt
import tools

columnQty = 200
#Loading image
imgpath = "images\slides4 - Histogram\{}.png"
imgName = input("Select image name: ")
columnQty = int(input("Number of bars: "))
escalar = input("Factor de luminancia: ")

img = imageio.imread(imgpath.format(imgName))
img = img[:,:,:3]/255.

#Extract Y layer
img_YIQ = tools.convert_to('YIQ', img)
img_Y = img_YIQ[:,:,0]

#Applies luminance change to a copy of img
imgAfectada = img_YIQ
imgAfectada[:,:,0] *= float(escalar)
imgAfectada[:,:,0] = np.clip(imgAfectada[:,:,0],0.,1.)
imgAfectada = tools.convert_to("RGB",imgAfectada)

#Plots original image and luminance histogram
plt.figure(1)
plt.imshow(img)
plt.figure(2)
tools.histogramaY(img, columnQty)

#Plots altered image
plt.figure(3)
plt.imshow(imgAfectada)
plt.figure(4)
tools.histogramaY(imgAfectada, columnQty)

#Takes selection for the filter
#print("1 - Filtro raiz\n2 - Filtro cuadrado\n3 - Lineal a trozos")
#chosenFilter = input("Select filter: ")
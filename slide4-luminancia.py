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
#Loading image
imgpath = "images\slides4 - Histogram\{}.png"
imgName = input("Select image name: ")

escalar = input("Factor de escala: ")

img = imageio.imread(imgpath.format(imgName))
img = img[:,:,:3]/255.

#Extract Y layer
img_YIQ = tools.convert_to('YIQ', img)
img_Y = img_YIQ[:,:,0]

#Applies luminance change to a copy of img
imgAfectada = img_YIQ
imgAfectada[:,:,0] *= float(escalar)
new_im[:,:,0] = np.clip(new_im[:,:,0],0.,1.)
new_im[:,:,1] = np.clip(new_im[:,:,1],-0.59,0.59)
new_im[:,:,2] = np.clip(new_im[:,:,2],-0.52,0.52)
imgAfectada = tools.convert_to("RGB",imgAfectada)

#Plots original image and luminance histogram
plt.figure(1)
plt.imshow(img)
tools.histogramaY(img, columnQty)

#Plots altered image
plt.figure(3)
plt.imshow(imgAfectada)
plt.figure()
tools.histogramaY(imgAfectada, columnQty)

#Takes selection for the filter
#print("1 - Filtro raiz\n2 - Filtro cuadrado\n3 - Lineal a trozos")
#chosenFilter = input("Select filter: ")
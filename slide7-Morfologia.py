# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 15:29:20 2019

@author: Ramiro
"""

import imageio
from scipy import fftpack
import numpy as np
import matplotlib.pyplot as plt
import tools

#Loading image
imgpath = "images\slides7 - Morphology\{}.png"
imgName = input("Select image name: ")
imagen = imageio.imread(imgpath.format(imgName))
imagen = imagen/255. #lo divido por 255 para cambiarlo de unit8
imagen = np.clip(imagen,0.,1.)

plt.figure(0)
plt.imshow(imagen,'gray')

imagenErosionada = np.zeros(imagen.shape)
squaredCircle = np.zeros((3,3))

for i in np.ndenumerate(imagen):
    minValue = 1.
    coordImg = i[0]
    if coordImg[0]<len(imagen[0])-2 and coordImg[1]<len(imagen[0])-2:  
        for j in np.ndenumerate(squaredCircle):
            coordKernel = j[0]
            print(coordImg[0]+coordKernel[0], coordImg[1]+coordKernel[1])
            aux = imagen[coordImg[0]+coordKernel[0], coordImg[1]+coordKernel[1]]
            if (aux<minValue):
                minValue = aux
        for k in np.ndenumerate(squaredCircle):
            cordKernel = k[0]
            imagenErosionada[coordImg[0]+coordKernel[0], coordImg[1]+coordKernel[1]] = minValue
    
plt.figure(1)
plt.imshow(imagenErosionada, 'gray')
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 01:42:05 2019

@author: Usuario
"""

import imageio
from scipy import fftpack
import numpy as np
import matplotlib.pyplot as plt
import tools

#Loading image
imgpath = "images\slides6 - Convolution\{}.png"
imgName = input("Select image name: ")
imagen = imageio.imread(imgpath.format(imgName))
imagen = imagen/255. #lo divido por 255 para cambiarlo de unit8
imagen = np.clip(imagen,0.,1.)

plt.figure(0)
plt.imshow(imagen,'gray')

#Filtro pasabajos plano 3x3
pasaBajos = np.ones((3,3))/9
barlett = [[-1, 2, -1], [-2, 4, -2], [1, -2, 1]]

imagenFiltrada = imagen

for i in np.ndenumerate(imagenFiltrada):
    convolucion = 0.
    coordImg = i[0]
    if coordImg[0]<len(imagenFiltrada[0])-2 and coordImg[1]<len(imagenFiltrada[0])-2:  
        for j in np.ndenumerate(pasaBajos):
            coordKernel = j[0]
            #print(coordImg[0]+coordKernel[0], coordImg[1]+coordKernel[1])
            convolucion += imagenFiltrada[coordImg[0]+coordKernel[0], coordImg[1]+coordKernel[1]] * j[1]
    
        imagenFiltrada[coordImg[0]+1, coordImg[1]+1] = convolucion
    
plt.figure(1)
plt.imshow(imagenFiltrada, 'gray')
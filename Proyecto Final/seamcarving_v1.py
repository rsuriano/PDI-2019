# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 20:27:47 2020

@author: Ramiro
"""

import imageio
import numpy as np
import matplotlib.pyplot as plt
import tools

#Carga de la imagen
imgName = input("Select image name: ")
imagen = imageio.imread(imgName)

#Normalizacion
if len(imagen.shape)>2:
    imagen = imagen[:,:,0]/255. 
else:
    imagen = imagen/255. 
imagen = np.clip(imagen,0.,1.)

plt.figure(0)
plt.imshow(imagen,'gray')


#Kernels filtros detectores de bordes
sobelXleft = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])   #Eje X hacia la izquierda
sobelXright = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])  #Eje X hacia la derecha
sobelYup = np.array([[2, 1, 2], [0, 0, 0], [-2, -1, -2]])     #Eje Y hacia arriba
sobelYdown = np.array([[-2, -1, -2], [0, 0, 0], [2, 1, 2]])   #Eje Y hacia abajo


#Filtro sobel X e Y
imgSobelX = tools.convolucionar(imagen, sobelXright)
imgSobelY = tools.convolucionar(imagen, sobelYdown)

#Calculos de magnitud y fase
magnitudSobel = np.zeros(imagen.shape)
faseSobel = np.zeros(imagen.shape)
for i in np.ndenumerate(imgSobelX):
    magnitudSobel[i[0]] = np.sqrt(np.square(imgSobelX[i[0]]) + np.square(imgSobelY[i[0]]))
        
magnitudSobel = tools.clipImg(magnitudSobel)
faseSobel = tools.clipImg(faseSobel)

plt.figure()
plt.imshow(magnitudSobel)

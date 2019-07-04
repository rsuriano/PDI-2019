# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 01:42:05 2019

@author: Usuario
"""

import imageio
import numpy as np
import matplotlib.pyplot as plt
import tools

#Loading image
imgpath = "images\slides6 - Convolution\{}.png"
imgName = input("Select image name: ")
imagen = imageio.imread(imgpath.format(imgName))
#Normalization
if len(imagen.shape)>2:
    imagen = imagen[:,:,0]/255. 
else:
    imagen = imagen/255. 
imagen = np.clip(imagen,0.,1.)

plt.figure(0)
plt.imshow(imagen,'gray')


#Kernels de filtros pasabajos:
identidad5 = np.zeros((5,5))
identidad5[2, 2] = 1
plano3 = np.ones((3,3))/9
bartlett3 = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]])/16
bartlett5 = np.array([  [1, 2, 3, 2, 1],
                        [2, 4, 6, 4, 2],
                        [3, 6, 9, 6, 3],
                        [2, 4, 6, 4, 2],
                        [1, 2, 3, 2, 1]])/81
bartlett7 = np.array([  [1, 2,  3,  4,  3,  2,  1],
                        [2, 4,  6,  8,  6,  4,  2],
                        [3, 6,  9,  12, 9,  6,  3],
                        [4, 8,  12, 16, 12, 8,  4],
                        [3, 6,  9,  12, 9,  6,  3],
                        [2,	4,  6,	8,	6,	4,  2],
                        [1,	2,	3,	4,	3,	2,  1]])/256
gaussiano3 = np.array([ [0, 0, 0, 0, 0],
                        [0, 1, 2, 1, 0],
                        [0, 2, 4, 2, 0],
                        [0, 1, 2, 1, 0],
                        [0, 0, 0, 0, 0]])/16
gaussiano5 = np.array([ [1, 4,  6,  4,  1],
                        [4, 16, 24, 16, 4],
                        [6, 24, 36, 24, 6],
                        [4, 16, 24, 16, 4],
                        [1, 4,  6,  4,  1]])/256
gaussiano7 = np.array([ [1,     6,     15,     20,     5,     6,     1],
                        [6,     36,	   90,	   120,    90,    36,    6],
                        [15,    90,    225,    300,    225,   90,   15],
                        [20,	120,   300,    400,    300,   120,  20],
                        [15,	90,    225,	   300,    225,   90,   15],
                        [6,     36,    90,     120,    90,    36,    6],
                        [1,	    6,     15,     20,     15,    6,     1]])/4096

#Kernel de filtros detectores de bordes
laplacianoV4 = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
laplacianoV8 = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
sobelXleft = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])   #Eje X hacia la izquierda
sobelXright = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])  #Eje X hacia la derecha
sobelYup = np.array([[2, 1, 2], [0, 0, 0], [-2, -1, -2]])     #Eje Y hacia arriba
sobelYdown = np.array([[-2, -1, -2], [0, 0, 0], [2, 1, 2]])   #Eje Y hacia abajo
sobelD1 = np.array([[-2, -1, 0], [-1, 0, 1], [0, 1, 2]]) #Diagonal topLeft->bottomRight
sobelD2 = np.array([[0, -1, -2], [1, 0, -1], [2, 1, 0]]) #Diagonal topRight->bottomLeft
sobelD3 = np.array([[0, 1, 2], [-1, 0, 1], [-2, -1, 0]]) #Diagonal bottomLeft->topRight
sobelD4 = np.array([[2, 1, 0], [1, 0, -1], [0, -1, -2]]) #Diagonal bottomRight->topLeft

pasaBanda = gaussiano3 - gaussiano5
pasaAltos02 = identidad5 - gaussiano5
pasaAltos04 = identidad5 - gaussiano3

"""Main program"""
filtro = laplacianoV8
imagenFiltrada = tools.convolucionar(imagen, filtro)
imagenFiltrada = tools.clipImg(imagenFiltrada)

plt.figure(1)
plt.imshow(imagenFiltrada, 'gray')



#Sobel filters
imgSobelX = tools.convolucionar(imagen, sobelXright)
imgSobelY = tools.convolucionar(imagen, sobelYup)

magnitudSobel = np.zeros(imagen.shape)
faseSobel = np.zeros(imagen.shape)

for i in np.ndenumerate(imgSobelX):
    magnitudSobel[i[0]] = np.sqrt(np.square(imgSobelX[i[0]]) + np.square(imgSobelY[i[0]]))
    if (imgSobelX[i[0]] != 0):
        faseSobel[i[0]] = np.arctan(imgSobelY[i[0]]/imgSobelX[i[0]])

magnitudSobel = tools.clipImg(magnitudSobel)
faseSobel = tools.clipImg(faseSobel)
    
imgSobel = np.zeros(imagen.shape+(3,))
imgSobel[:,:,0] = magnitudSobel
imgSobel[:,:,1] = faseSobel

imgSobelRGB = tools.convert_to('RGB', imgSobel)

plt.figure(2)
plt.imshow(magnitudSobel, 'gray')

plt.figure(3)
plt.imshow(imgSobelRGB)
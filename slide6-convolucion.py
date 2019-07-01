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

print("0 - Identidad")
print("1 - Pasa Bajos Plano 3x3")
print("2 - Pasa Bajos Bartlett 3x3")
print("3 - Pasa Bajos Bartlett 5x5")
print("4 - Pasa Bajos Bartlett 7x7")
print("5 - Pasa Bajos Gaussiano 5x5")
print("6 - Pasa Bajos Gaussiano 7x7")
print("7 - Laplaciano v4")
print("8 - Laplaciano v8")

opcion = input('Elija operación (de 0 a 8): ')

plt.figure(0)
plt.imshow(imagen,'gray')


#Index de Filtros
identidad = np.matrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) #FUNCIONA
pasaBajos3 = np.ones((3,3))/9
#bartlett3 = np.array([[1., -2., 1.], [-2., 4., -2.], [1., -2., 1.]])
bartlett3 = np.matrix([[-1., -1., -1.], [-1., 8, -1.], [-1., -1., -1.]]) 

bartlett5 = [[-1, 2, -1], [-2, 4, -2], [1, -2, 1], [], []]

if opcion=='0':
    margen = 2
    filtro = identidad
elif opcion=='1':
    margen = 2
    filtro = pasaBajos3
elif opcion =='2':
    margen = 2
    filtro = bartlett3
    

imagenFiltrada = imagen

for i in np.ndenumerate(imagenFiltrada):
    convolucion = 0.
    coordImg = i[0]
    if coordImg[0]<len(imagenFiltrada[0])-margen and coordImg[1]<len(imagenFiltrada[0])-margen:  
        for j in np.ndenumerate(filtro):
            coordKernel = j[0]
            #print(coordImg[0]+coordKernel[0], coordImg[1]+coordKernel[1])
            convolucion += imagenFiltrada[coordImg[0]+coordKernel[0], coordImg[1]+coordKernel[1]] * j[1]
    
        imagenFiltrada[coordImg[0]+1, coordImg[1]+1] = convolucion #/255 normalizandolo tmp funciona
    
plt.figure(1)
plt.imshow(imagenFiltrada, 'gray')
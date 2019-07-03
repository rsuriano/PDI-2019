# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 01:42:05 2019

@author: Usuario
"""


"""
     si un kernel es mas grande el filtro es de menor frecuencia
     
     traslacion: 
         0 0 1
         0 0 0
         0 0 0
    
    canny edge detection 

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
print("9 - Sobel")

opcion = input('Elija operación (de 0 a 9): ')

plt.figure(0)
plt.imshow(imagen,'gray')


#Index de Kernels
identidad = np.matrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
pasaBajos3 = np.ones((3,3))/9
bartlett3 = [[1, 2, 1], [2, 4, 2], [1, 2, 1]]/16
bartlett5 = [   [1, 2, 3, 2, 1]
                [2, 4, 6, 4, 2]
                [3, 6, 9, 6, 3]
                [2, 4, 6, 4, 2]
                [1, 2, 3, 2, 1]]/81
gaussiano3 = [[1, 2, 1], [2, 4, 2], [1, 2, 1]]/16
gaussiano5 = [  [1, 4,  6,  4,  1]
                [4, 16, 24, 16, 4]
                [6, 24, 36, 24, 6]
                [4, 16, 24, 16, 4]
                [1, 4,  6,  4,  1]]/256
sobelX = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]] #derivada en x
sobelY = [[-2, -1, -2], [0, 0, 0], [2, 1, 2]] #derivada en y

if opcion=='0':
    margen = 2
    filtro = identidad
elif opcion=='1':
    margen = 2
    filtro = pasaBajos3
elif opcion =='2':
    margen = 2
    filtro = bartlett3
if opcion=='9':
    filtro = sobelX
if opcion=='10':
    filtro = sobelY
    
imagenFiltrada = tools.convolucionar()

plt.figure(1)
plt.imshow(imagenFiltrada, 'gray')
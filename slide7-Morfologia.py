# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 15:29:20 2019

@author: Ramiro
"""

import imageio
import numpy as np
import matplotlib.pyplot as plt
import tools

#Loading image
imgpath = "images\slides7 - Morphology\{}.png"
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

#Input sequence
print("1 - Erosion")
print("2 - Dilatacion")
print("3 - Apertura")
print("4 - Cierre")
print("5 - Borde")
print("6 - Mediana")
print("7 - Tophat")
sequence = input("Seleccione secuencia de filtros: ")
sequence = sequence.split(' ')

for i in sequence:
    filtro = int(i)
    if filtro == 1:
        img2 = tools.erosionar(imagen, 1)
        
    if filtro == 2:
        img2 = tools.dilatar(imagen, 1)
        
    if filtro == 3:
        img2 = tools.apertura(imagen)
    
    if filtro == 4:
        img2 = tools.cierre(imagen)
    
    if filtro == 5:
        img2 = tools.borde(imagen)
        
    if filtro == 6:
        img2 = tools.mediana(imagen, 1)
    
    if filtro == 7:
        img2 = tools.topHat(imagen)
        
    plt.figure(i)
    plt.imshow(img2, 'gray')

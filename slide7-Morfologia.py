# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 15:29:20 2019

@author: Suriano, Ramiro & Armanasco, Matias
"""

import imageio
import numpy as np
import matplotlib.pyplot as plt
import tools

#Carga de la imagen
imgpath = "images\slides7 - Morphology\{}.png"
imgName = input("Select image name: ")
imagen = imageio.imread(imgpath.format(imgName))
#Normalizacion
if len(imagen.shape)>2:
    imagen = imagen[:,:,0]/255. 
else:
    imagen = imagen/255. 
imagen = np.clip(imagen,0.,1.)

plt.figure(0)
plt.imshow(imagen,'gray')

#Secuencia de input
print("1 - Erosion")
print("2 - Dilatacion")
print("3 - Apertura")
print("4 - Cierre")
print("5 - Borde")
print("6 - Mediana")
print("7 - Tophat")
sequence = input("Seleccione secuencia de filtros: (ej: '1 2 1') ")
sequence = sequence.split(' ')
elementoEstructurante = np.ones((3,3))

#Cálculo de las operaciones seleccionadas
for i in sequence:
    filtro = int(i)
    if filtro == 1:
        img2 = tools.erosionar(imagen, elementoEstructurante)
        
    if filtro == 2:
        img2 = tools.dilatar(imagen, elementoEstructurante)
        
    if filtro == 3:
        img2 = tools.apertura(imagen, elementoEstructurante)
    
    if filtro == 4:
        img2 = tools.cierre(imagen, elementoEstructurante)
    
    if filtro == 5:
        img2 = tools.borde(imagen, elementoEstructurante)
        
    if filtro == 6:
        img2 = tools.mediana(imagen, elementoEstructurante)
    
    if filtro == 7:
        img2 = tools.topHat(imagen, elementoEstructurante)
   
    plt.figure(i)
    plt.imshow(img2, 'gray')
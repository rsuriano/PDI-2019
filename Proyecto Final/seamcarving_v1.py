# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 20:27:47 2020

@author: Ramiro
"""

import imageio
import numpy as np
#import matplotlib.pyplot as plt
import tools
import seamTools as st
from scipy import ndimage

#Carga de la imagen
imgName = input("Select image name: ")
imagen = imageio.imread(imgName)

#Normalizacion
if len(imagen.shape)>2:
    imagen = imagen[:,:,:3]/255. 
else:
    imagen = imagen/255. 


tools.pltImg(imagen, 'Imagen ingresada')


#Conversion a YIQ para extraer luminancia
imagYIQ = tools.convert_to("YIQ",imagen)
imagY = imagYIQ[:,:,0]


#Kernels filtros detectores de bordes
sobelX = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])  #Eje X hacia la derecha
sobelY = np.array([[-2, -1, -2], [0, 0, 0], [2, 1, 2]])  #Eje Y hacia abajo

#Filtro sobel X e Y
imgSobelX = ndimage.convolve(imagY,sobelX)
imgSobelY = ndimage.convolve(imagY,sobelY)
    
#Calculo de magnitud
magnitudSobel = np.sqrt(np.square(imgSobelX) + np.square(imgSobelY))
tools.plotImg(tools.clipImg(magnitudSobel), 'Energia de la imagen')



###### EMPIEZA EL SEAM CARVING ######
colsToDelete = 1
deletedCols = 0
procImg = imagen
while deletedCols<colsToDelete:
    
    #Conversion a YIQ para extraer luminancia
    imagYIQ = tools.convert_to("YIQ",procImg)
    imagY = imagYIQ[:,:,0]
    
    #Filtro sobel X e Y
    imgSobelX = ndimage.convolve(imagY,sobelX)
    imgSobelY = ndimage.convolve(imagY,sobelY)
    
    #Calculo de magnitud
    magnitudSobel = np.sqrt(np.square(imgSobelX) + np.square(imgSobelY))
    
    #buscador de seam con energia minima a eliminar
    startPoint, seamMap = st.seamFinder(imagY, magnitudSobel)
    
    #removedor de seam
    removed, seam = st.seamremover_revisited(int(startPoint), seamMap, procImg)
    done = tools.clipImg(procImg+seam)
    deletedCols +=1

    procImg = removed

tools.pltImg(removed, 'Imagen procesada')



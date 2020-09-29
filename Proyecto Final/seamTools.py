# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 21:05:40 2020

@author: Ramiro
"""

import numpy as np

def seamFinder(luminance, energyMap):    
    
    seamMap = np.zeros(luminance.shape, dtype=int)
    #primer loop de seam finder, recorre fila por fila
    previousRow = energyMap[1]
    for row in range(energyMap.shape[0]-1):
        currentRow = np.zeros(energyMap.shape[1])   
        #print(seamMap)
        
        #segundo loop, recorre elementos de cada fila para calcular energias
        for col in range(energyMap.shape[1]):
            
            #x_range define si se trata de un caso borde o no
            x_left = max(col - 1, 0)
            x_right = min(col + 1, energyMap.shape[1])
            
            #calculo de seam minimo encima de cada pixel
            prevPath = previousRow[x_left : x_right]
            minSeam = min(prevPath)
            #guardado de energias acumuladas en la nueva fila, y coordenadas en el mapa
            seamMap[row+1,col] = int(np.where(prevPath == min(prevPath))[0][0] + 1 * (x_left - max(x_left, col)))
            currentRow[col] = energyMap[row+1,col]+minSeam
            #print(row+1,col)
            #print(seamMap)
            
        previousRow = currentRow
        
    startPoint = np.where(currentRow == min(currentRow))[0][0]

    return startPoint, seamMap



def seamremover(N,roads,imagenOriginal):
    #método para remover un camino de mínima energía almacenado en roads
    alto, ancho, _ = imagenOriginal.shape
    imagenAuxiliar = np.zeros(alto,ancho-1)
    ult_fila = alto-1
    pixel = N
    
    while (ult_fila>-1):
        fila = imagenOriginal[ult_fila,:]   #bottom-up salgo de la ultima fila y voy subiendo
        pixel = N + fila[N]                 #pixel es el que voy a eliminar
        del fila[N]                         #elimino 'pixel'
        imagenAuxiliar[ult_fila,:] = fila   #la fila sin 'pixel' la guardo en la nueva imagen
        N = pixel                           #actualizo N para cuando vuelvo a pasar el loop
        ult_fila = (ult_fila - 1)           #actualizo la ultima fila para cunaod vuelvo a pasar el loop
    
    return imagenAuxiliar #esta imagen entra de nuevo en seamcarver()



def seamremover_revisited(N,roads,imagenOriginal):
    #método para remover un camino de mínima energía almacenado en roads
    alto, ancho = imagenOriginal.shape[0:2]
    imagenAuxiliar = np.zeros([alto,ancho-1])
    ult_fila = alto-1
    pixel = N
    seam = np.zeros(imagenOriginal.shape)
    
    while (ult_fila>-1):
        fila = imagenOriginal[ult_fila,:]   #bottom-up salgo de la ultima fila y voy subiendo
        filaMapa = roads[ult_fila,:]
        
        pixel = N + filaMapa[N]                 #pixel es el que voy a eliminar   
        fila = np.delete(fila, N)               #elimino 'pixel'
        print(fila.shape)
        seam[ult_fila,N-2:N+2,0] = 1.
        imagenAuxiliar[ult_fila,:] = fila   #la fila sin 'pixel' la guardo en la nueva imagen
        N = int(pixel)                           #actualizo N para cuando vuelvo a pasar el loop
        ult_fila = (ult_fila - 1)           #actualizo la ultima fila para cunaod vuelvo a pasar el loop
          
    return imagenAuxiliar, seam #esta imagen entra de nuevo en seamcarver()
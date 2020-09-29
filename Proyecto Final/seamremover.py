# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 01:10:48 2020

@author: Usuario
"""

import numpy as np


def seamreamover(N,roads,imagenOriginal):
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
    alto, ancho = imagenOriginal.shape
    imagenAuxiliar = np.zeros([alto,ancho-1])
    ult_fila = alto-1
    pixel = N
    
    while (ult_fila>-1):
        #fila = imagenOriginal[ult_fila,:]   #bottom-up salgo de la ultima fila y voy subiendo
        filaMapa = roads[ult_fila,:]
        
        pixel = N + filaMapa[N]                 #pixel es el que voy a eliminar
        #del fila[N]                         #elimino 'pixel'
        imagenOriginal[ult_fila,N] = 1.
        #imagenAuxiliar[ult_fila,:] = fila   #la fila sin 'pixel' la guardo en la nueva imagen
        N = int(pixel)                           #actualizo N para cuando vuelvo a pasar el loop
        ult_fila = (ult_fila - 1)           #actualizo la ultima fila para cunaod vuelvo a pasar el loop
       
    return imagenAuxiliar #esta imagen entra de nuevo en seamcarver()
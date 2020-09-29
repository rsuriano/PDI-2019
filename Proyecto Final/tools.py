# -*- coding: utf-8 -*-
"""
Created on Fri May 17 17:40:09 2019

@author: Suriano, Ramiro & Armanasco, Matias
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack


#Clipping images - Misc:
def clipImg(image):
    if (np.amin(image)<0 or np.amax(image)>1):
        clippedImg = np.clip(image, 0., 1.)
        return clippedImg
    else:
        return image
        

#Conversión RGB/YIQ - Slides 2:
#Convierte una matriz 'image' al espacio cromático indicado en 'space'
def convert_to(space,image): 
    
    imageRet = np.zeros(image.shape)
    toYIQ = np.array([[0.299,0.587,0.114] , [0.595716,-0.274453,-0.321263] , [0.211456,-0.522591,0.311135]])
    toRGB = np.array([[1,0.9663,0.621] , [1,-0.2721,-0.6474] , [1,-1.107,1.7046]])
    
    if (space == 'RGB'):
        for i in range(3):
            imageRet[:,:,i] = toRGB[i,0]*image[:,:,0] + toRGB[i,1]*image[:,:,1] + toRGB[i,2]*image[:,:,2]
        return imageRet
    
    if (space == 'YIQ'):
        for i in range(3):
            imageRet[:,:,i] = toYIQ[i,0]*image[:,:,0] + toYIQ[i,1]*image[:,:,1] + toYIQ[i,2]*image[:,:,2]
        return imageRet
    
    else:
        return image



#Luminancia - Slides 4 - Histograma de luminancias:
def histogramaY(image, bars):
    
    histogram = np.zeros(bars+1)

    for i in np.ndenumerate(image):
        # Desnormaliza el valor de luminancia, lo trunca y lo asigna a su 
        # barra correspondiente en el histograma
        histogram[int(np.trunc(i[1]*bars))] +=1
    
    return histogram



#Fourier - Slides 5:
#Recibe una imagen y devuelve la magnitud y fase de la transformada
def fourier(imagen):
    
    transformada = np.zeros(imagen.shape)
    transformada = fftpack.fft2(imagen)
    #Centrar la frecuencia cero en el centro
    transformada = fftpack.fftshift(transformada)
    #Obtener la magnitud
    magnitud = np.abs(transformada)
    #Obtener la fase
    fase = np.angle(transformada)
    tuple_return = (magnitud,fase)
    return tuple_return

#Recibe magnitud y fase de una transformada y calcula su inversa
def fourier_undo(mag,fase):
    
    transformada = mag * (np.cos(fase)+np.sin(fase)*1j)
    transformada = fftpack.ifftshift(transformada)
    inversa = fftpack.ifft2(transformada)   
    inversa = np.abs(inversa)
    return inversa



#Convolucion - Slides 6:
#Realiza la convolucion entre la imagen y un kernel
def convolucionar(img, kernel):
    
    #Copia los bordes de la imagen alrededor de la imagen original
    borde = int(kernel.shape[1]/2)
    imagen = expandirLimites(img, borde)
    
    #Calcula la convolucion de la imagen con el kernel
    imagenConv = np.zeros(imagen.shape)
    margen = kernel.shape[0] - 1
    for i in np.ndenumerate(imagen):
        convolucion = 0.
        coordImg = i[0]
        if (coordImg[0]<imagen.shape[0]-margen) and (coordImg[1]<imagen.shape[1]-margen): 
            for j in np.ndenumerate(kernel):
                coordKernel = j[0]
                convolucion += imagen[coordImg[0]+coordKernel[0], coordImg[1]+coordKernel[1]] * j[1]
        
            imagenConv[coordImg[0]+int(kernel.shape[0]/2), coordImg[1]+int(kernel.shape[0]/2)] = convolucion
    
    #Elimina los bordes agregados anteriormente, y devuelve la imagen convolucionada
    imagenSalida = quitarLimites(imagenConv, borde)
    return imagenSalida



#Agregar contorno a imagen - Slide 6
def expandirLimites(img, margin):
    newImg = np.zeros((img.shape[0]+2*margin, img.shape[1]+2*margin))
    
    #Copy img at the center of newImg
    for i in np.ndenumerate(newImg):
        nImgCoord = i[0]
        if (nImgCoord[0]<newImg.shape[0]-2*margin and nImgCoord[1]<newImg.shape[1]-2*margin):
            newImg[(nImgCoord[0]+margin, nImgCoord[1]+margin)] = img[nImgCoord] 
    
    #Agregado de contorno
    for a in range(0, margin):
        newImg[a,:] = newImg[margin,:]
        newImg[:,a] = newImg[:,margin]
        newImg[newImg.shape[0]-(margin-a), :] = newImg[newImg.shape[0]-margin-1, :]
        newImg[:, newImg.shape[0]-(margin-a)] = newImg[:, newImg.shape[0]-margin-1]
    return newImg

#Eliminar contorno de la imagen - Slide 6
def quitarLimites(img, margin):
    #Get original img
    origImg = np.zeros((img.shape[0]-2*margin, img.shape[1]-2*margin))
    
    for i in np.ndenumerate(img):
        nImgCoord = i[0]
        
        if (0 < nImgCoord[0]<img.shape[0]-margin) and  (0 < nImgCoord[1]<img.shape[1]-margin):
            origImg[(nImgCoord[0]-margin, nImgCoord[1]-margin)] = img[nImgCoord] 
    return origImg


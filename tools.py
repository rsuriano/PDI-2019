# -*- coding: utf-8 -*-
"""
Created on Fri May 17 17:40:09 2019

@author: Suriano, Ramiro & Armanasco, Matias
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack
import imageio

#Conversión RGB/YIQ
def convert_to(space,image): 
    #esta funcion convierte una matriz 'image' al espacio cromático indicado en 'space'
    imageRet = np.zeros(image.shape)
    toYIQ = np.array([[0.299,0.587,0.114] , [0.595716,-0.274453,-0.321263] , [0.211456,-0.522591,0.311135]])
    toRGB = np.array([[1,0.9663,0.621] , [1,-0.2721,-0.6474] , [1,-1.107,1.7046]])
    
    #np matmul para hacerlo mas corto
    if (space == 'RGB'):
        for i in range(3):
            imageRet[:,:,i] = toRGB[i,0]*image[:,:,0] + toRGB[i,1]*image[:,:,1] + toRGB[i,2]*image[:,:,2]
        return imageRet
    
    if (space == 'YIQ'):
        for i in range(3):
            imageRet[:,:,i] = toYIQ[i,0]*image[:,:,0] + toYIQ[i,1]*image[:,:,1] + toYIQ[i,2]*image[:,:,2]
        return imageRet


#Colormaps Slide 2
def showColormaps (image):
    plt.imshow(image)
    plt.show()

    plt.imshow(image, 'jet')
    plt.show()
    
    plt.imshow(image, 'ocean')
    plt.show()
    
    plt.imshow(image, 'gray')
    plt.show()
    
    plt.imshow(image, 'rainbow')
    plt.show()
    
    plt.imshow(image, 'nipy_spectral')
    plt.show()
    return 0    
    

##  Aritmetica de pixels
def sumaClampeadaRGB(image1,image2):
    image3 = image1 + image2
    image3 = np.clip(image3,0.,1.)
    return image3

def restaClampeadaRGB(image1,image2):
    image3 = image1 - image2
    image3 = np.clip(image3,0.,1.)
    return image3

def sumaPromRGB(image1,image2):
    image3 = (image1 + image2)/2
    image3 = np.clip(image3,0.,1.)
    return image3

def restaPromRGB(image1,image2):
    image3 = (image1 - image2)/2 + np.ones(image1.shape)*0.5
    image3 = np.clip(image3,0.,1.)
    return image3

def sumaClampeadaYIQ(image1,image2):
    image3 = np.zeros(image1.shape)
    image1 = convert_to('YIQ',image1)    
    image2 = convert_to('YIQ',image2)
    
    image3[:,:,0] = (image1[:,:,0] + image2[:,:,0])
    image3[:,:,1] = [image1[:,:,0]*image1[:,:,1] + image2[:,:,0]*image2[:,:,1]]/(image1[:,:,0]+image2[:,:,0])
    image3[:,:,2] = [image1[:,:,0]*image1[:,:,2] + image2[:,:,0]*image2[:,:,2]]/(image1[:,:,0]+image2[:,:,0])

    image3[:,:,0] = np.clip(image3[:,:,0],0.,1.)
    image3 = convert_to('RGB',image3)
    return image3

def sumaPromYIQ(image1,image2):
    image3 = np.zeros(image1.shape)
    image1 = convert_to('YIQ',image1)    
    image2 = convert_to('YIQ',image2)

    image3[:,:,0] = (image1[:,:,0] + image2[:,:,0])/2
    image3[:,:,1] = [image1[:,:,0]*image1[:,:,1] + image2[:,:,0]*image2[:,:,1]]/(image1[:,:,0]+image2[:,:,0])
    image3[:,:,2] = [image1[:,:,0]*image1[:,:,2] + image2[:,:,0]*image2[:,:,2]]/(image1[:,:,0]+image2[:,:,0])

    image3[:,:,0] = np.clip(image3[:,:,0],0.,1.)
    image3 = convert_to('RGB',image3)
    return image3

def ifDarker(image1,image2):
    image3 = np.zeros(image1.shape)
    image1 = convert_to('YIQ',image1)    
    image2 = convert_to('YIQ',image2)

    darker = image1[:,:,0]<image2[:,:,0]
    brighter = 1 - darker
    for i in range(3):
        image3[:,:,i] = image1[:,:,i]*darker + image2[:,:,i]*brighter
    
    image3 = convert_to('RGB',image3)
    
    return image3


#Histograma de luminancias
#Recibe la capa Y de una imagen, y plotea el histograma
def histogramaY(image, bars):
    
    histogram = np.zeros(bars+1)
    names = np.arange(0,len(histogram))
    
    for i in np.ndenumerate(image):
        # desnormalizo el valor de luminancia, lo trunco y lo asigno a su 
        # barra correspondiente en el histograma
        histogram[int(np.trunc(i[1]*bars))] +=1/np.prod(image.shape)#puede estar no normalizado
    
    plt.bar(names,histogram, width=bars/20)#devolver array y plotear en el programa principal
    return histogramaY


#Fourier Slides-5
def fourier(imagen):
    #recibe una imagen y devuelve la magnitud y fase de la transformada
    transformada = np.zeros(imagen.shape)
    transformada = fftpack.fft2(imagen)
    #centrar la frecuencia cero en el centro
    transformada = fftpack.fftshift(transformada)
    #obtener la magnitud
    magnitud = np.abs(transformada)
    #obtener la fase
    fase = np.angle(transformada)
    tuple_return = (magnitud,fase)
    
    return tuple_return

def fourier_undo(mag,fase):
    #recibe mag y fase de una transformada y la invierte
    transformada = mag * (np.cos(fase)+np.sin(fase)*1j)
    transformada = fftpack.ifftshift(transformada)
    inversa = fftpack.ifft2(transformada)   
    inversa = np.abs(inversa)
    
    return inversa

    

#Erosion - Slide 7
def erode(imagen):
    print(imagen.shape)
    imagenErosionada = np.zeros(imagen.shape)
    squaredCircle = np.zeros((3,3))
    """
    prog25 = (np.trunc(imagen.shape[0]/4), imagen.shape[1])
    prog50 = (np.trunc(imagen.shape[0]/2), imagen.shape[1])
    prog75 = (np.trunc(imagen.shape[0]*(3/4)), imagen.shape[1])
    """ 
    for i in np.ndenumerate(imagen):
        minValue = 1.
        coordImg = i[0]
        if (coordImg[0]<imagen.shape[0]-2) and (coordImg[1]<imagen.shape[1]-2):  
            for j in np.ndenumerate(squaredCircle):
                coordKernel = j[0]
                #print(coordImg[0]+coordKernel[0], coordImg[1]+coordKernel[1])
                aux = imagen[coordImg[0]+coordKernel[0], coordImg[1]+coordKernel[1]]
                if (aux<minValue):
                    minValue = aux
            for k in np.ndenumerate(squaredCircle):
                coordKernel = k[0]
                imagenErosionada[coordImg[0]+coordKernel[0], coordImg[1]+coordKernel[1]] = minValue
        """
        if (coordImg == prog25):
            print("25% completado")
        if coordImg[0] == prog50:
            print("50% completado")
        if coordImg[0] == prog75:
            print("75% completado")"""
            
    return imagenErosionada

def dilate(imagen):
    print(imagen.shape)
    imagenDilatada = np.zeros(imagen.shape)
    squaredCircle = np.zeros((3,3))
    for i in np.ndenumerate(imagen):
        maxValue = 0.
        coordImg = i[0]
        if (coordImg[0]<imagen.shape[0]-2) and (coordImg[1]<imagen.shape[1]-2):  
            for j in np.ndenumerate(squaredCircle):
                coordKernel = j[0]
                #print(coordImg[0]+coordKernel[0], coordImg[1]+coordKernel[1])
                aux = imagen[coordImg[0]+coordKernel[0], coordImg[1]+coordKernel[1]]
                if (aux>maxValue):
                    maxValue = aux
            for k in np.ndenumerate(squaredCircle):
                coordKernel = k[0]
                imagenDilatada[coordImg[0]+coordKernel[0], coordImg[1]+coordKernel[1]] = maxValue
                
            
    return imagenDilatada
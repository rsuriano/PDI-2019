# -*- coding: utf-8 -*-
"""
Created on Fri May 17 17:40:09 2019

@author: Suriano, Ramiro & Armanasco, Matias
"""

import numpy as np
import matplotlib.pyplot as plt

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
        histogram[int(np.trunc(i[1]*bars))] +=1/np.prod(image.shape)
    
    plt.bar(names,histogram, width=bars/20)
    return histogramaY
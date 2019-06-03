# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 18:37:36 2019

@author: Usuario
"""

import imageio
import numpy as np
import matplotlib.pyplot as plt
import tools

def sumaCampleadaRGB(image1,image2):
    image3 = np.zeros(image1.shape)
    image3[:,:,0] = image1[:,:,0] + image2[:,:,0]
    image3[:,:,1] = image1[:,:,1] + image2[:,:,1]
    image3[:,:,2] = image1[:,:,2] + image2[:,:,2]
    
    image3 = np.clip(image3,0.,1.)
    
    return image3

def restaCampleadaRGB(image1,image2):
    image3 = np.zeros(image1.shape)
    image3[:,:,0] = image1[:,:,0] - image2[:,:,0] + 0.5
    image3[:,:,1] = image1[:,:,1] - image2[:,:,1] + 0.5
    image3[:,:,2] = image1[:,:,2] - image2[:,:,2] + 0.5
    
    image3 = np.clip(image3,0.,1.)
    
    return image3

def sumaPromRGB(image1,image2):
    image3 = np.zeros(image1.shape)
    image3[:,:,0] = (image1[:,:,0] + image2[:,:,0])/2
    image3[:,:,1] = (image1[:,:,1] + image2[:,:,1])/2
    image3[:,:,2] = (image1[:,:,2] + image2[:,:,2])/2
    
    image3 = np.clip(image3,0.,1.)
    
    return image3

def restaPromRGB(image1,image2):
    image3 = np.zeros(image1.shape)
    image3[:,:,0] = (image1[:,:,0] - image2[:,:,0])/2 + 0.5
    image3[:,:,1] = (image1[:,:,1] - image2[:,:,1])/2 + 0.5
    image3[:,:,2] = (image1[:,:,2] - image2[:,:,2])/2 + 0.5
    
    image3 = np.clip(image3,0.,1.)
    
    return image3

def sumaCampleadaYIQ(image1,image2):
    image3 = np.zeros(image1.shape)
    image1 = tools.convert_to('YIQ',image1)    
    image2 = tools.convert_to('YIQ',image2)

    image3[:,:,0] = (image1[:,:,0] + image2[:,:,0])
    image3[:,:,1] = [image1[:,:,0]*image1[:,:,1] + image2[:,:,0]*image2[:,:,1]]/(image1[:,:,0]+image2[:,:,0])
    image3[:,:,2] = [image1[:,:,0]*image1[:,:,2] + image2[:,:,0]*image2[:,:,2]]/(image1[:,:,0]+image2[:,:,0])

    image3[:,:,0] = np.clip(image3[:,:,0],0.,1.)
    
    image3 = tools.convert_to('RGB',image3)
    
    return image3

def sumaPromYIQ(image1,image2):
    image3 = np.zeros(image1.shape)
    image1 = tools.convert_to('YIQ',image1)    
    image2 = tools.convert_to('YIQ',image2)

    image3[:,:,0] = (image1[:,:,0] + image2[:,:,0])/2
    image3[:,:,1] = [image1[:,:,0]*image1[:,:,1] + image2[:,:,0]*image2[:,:,1]]/(image1[:,:,0]+image2[:,:,0])
    image3[:,:,2] = [image1[:,:,0]*image1[:,:,2] + image2[:,:,0]*image2[:,:,2]]/(image1[:,:,0]+image2[:,:,0])

    image3[:,:,0] = np.clip(image3[:,:,0],0.,1.)
    
    image3 = tools.convert_to('RGB',image3)
    
    return image3

paisaje = imageio.imread("images\slides3 - Pixel Arithmetic\image1.png")
paisaje = paisaje[:,:,:3]/255. #dejo las dos primeras bandas, y de la tercer banda borro una (alpha)
                           #lo divido por 255 para cambiarlo de unit8
plaza = imageio.imread("images\slides3 - Pixel Arithmetic\image2.png")
plaza = plaza[:,:,:3]/255.

resultado = np.zeros(paisaje.shape)

suma = input('Elija operación (de 1 a 6): ')

if suma=='1':
    resultado = sumaCampleadaRGB(paisaje,plaza)
    plt.imshow(resultado)
elif suma=='2':
    resultado = restaCampleadaRGB(paisaje,plaza)
    plt.imshow(resultado)
elif suma=='3':
    resultado = sumaPromRGB(paisaje,plaza)
    plt.imshow(resultado)
elif suma=='4':
    resultado = restaPromRGB(paisaje,plaza)
    plt.imshow(resultado)
elif suma=='5':
    resultado = sumaCampleadaYIQ(paisaje,plaza)
    plt.imshow(resultado)
elif suma=='6':
    resultado = sumaPromYIQ(paisaje,plaza)
    plt.imshow(resultado)
else: 
    print(suma,'no es una operación definida')

 

# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 18:37:36 2019

@author: Usuario
"""

import imageio
import numpy as np
import matplotlib.pyplot as plt
import tools

def sumaClampeadaRGB(image1,image2):
    image3 = image1 + image2 #np.zeros(image1.shape)
    
    #image3[:,:,0] = image1[:,:,0] + image2[:,:,0]
    #image3[:,:,1] = image1[:,:,1] + image2[:,:,1]
    #image3[:,:,2] = image1[:,:,2] + image2[:,:,2]
    
    image3 = np.clip(image3,0.,1.)
    
    return image3

def restaClampeadaRGB(image1,image2):
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

def sumaClampeadaYIQ(image1,image2):
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

def ifDarker(image1,image2):
    image3 = np.zeros(image1.shape)
    #darker = np.array(image1.size)
    image1 = tools.convert_to('YIQ',image1)    
    image2 = tools.convert_to('YIQ',image2)

    darker = image1[:,:,0]<image2[:,:,0]
    brighter = 1 - darker
    for i in range(3):
        image3[:,:,i] = image1[:,:,i]*darker + image2[:,:,i]*brighter
    
    image3 = tools.convert_to('RGB',image3)
    
    return image3
        

fig=plt.figure()
paisaje = imageio.imread("images\slides3 - Pixel Arithmetic\image1.png")
paisaje = paisaje[:,:,:3]/255. #dejo las dos primeras bandas, y de la tercer banda borro una (alpha)
                           #lo divido por 255 para cambiarlo de unit8
plaza = imageio.imread("images\slides3 - Pixel Arithmetic\image2.png")
plaza = plaza[:,:,:3]/255.

resultado = np.zeros(paisaje.shape)

print("1 - Suma RGB Clampeada")
print("2 - Resta RGB Clampeada")
print("3 - Suma RGB Promediada")
print("4 - Resta RGB Promediada")
print("5 - Suma YIQ Clampeada")
print("6 - Suma YIQ Promediada")
print("7 - ifDarker")


suma = input('Elija operación (de 1 a 7): ')

if suma=='1':
    resultado = sumaClampeadaRGB(paisaje,plaza)
    print("1 - Suma RGB Clampeada")
    plt.imshow(resultado)
elif suma=='2':
    resultado = restaClampeadaRGB(paisaje,plaza)
    print("2 - Resta RGB Clampeada")
    plt.imshow(resultado)
elif suma=='3':
    resultado = sumaPromRGB(paisaje,plaza)
    print("3 - Suma RGB Promediada")
    plt.imshow(resultado)
elif suma=='4':
    resultado = restaPromRGB(paisaje,plaza)
    print("4 - Resta RGB Promediada")
    plt.imshow(resultado)
elif suma=='5':
    resultado = sumaClampeadaYIQ(paisaje,plaza)
    print("5 - Suma YIQ Clampeada")
    plt.imshow(resultado)
elif suma=='6':
    resultado = sumaPromYIQ(paisaje,plaza)
    print("6 - Suma YIQ Promediada")
    plt.imshow(resultado)
elif suma=='7':
    resultado = ifDarker(paisaje,plaza)
    print(" - ifDarker")
    plt.imshow(resultado)
else: 
    print(suma,' no es una operación definida')


 

# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 18:37:36 2019

@author: Suriano, Ramiro & Armanasco, Matias
"""

import imageio
import matplotlib.pyplot as plt
import tools

#Carga y normalización de imagenes
fig=plt.figure()
paisaje = imageio.imread("images\slides3 - Pixel Arithmetic\image1.png")
paisaje = paisaje[:,:,:3]/255. 
plaza = imageio.imread("images\slides3 - Pixel Arithmetic\image2.png")
plaza = plaza[:,:,:3]/255.

#User input de la operacion a realizar
print("1 - Suma RGB Clampeada")
print("2 - Resta RGB Clampeada")
print("3 - Suma RGB Promediada")
print("4 - Resta RGB Promediada")
print("5 - Suma YIQ Clampeada")
print("6 - Suma YIQ Promediada")
print("7 - ifDarker")
suma = input('Elija operación (de 1 a 7): ')


if suma=='1':
    resultado = tools.sumaClampeadaRGB(paisaje,plaza)
    print("1 - Suma RGB Clampeada")
    plt.imshow(resultado)
elif suma=='2':
    resultado = tools.restaClampeadaRGB(paisaje,plaza)
    print("2 - Resta RGB Clampeada")
    plt.imshow(resultado)
elif suma=='3':
    resultado = tools.sumaPromRGB(paisaje,plaza)
    print("3 - Suma RGB Promediada")
    plt.imshow(resultado)
elif suma=='4':
    resultado = tools.restaPromRGB(paisaje,plaza)
    print("4 - Resta RGB Promediada")
    plt.imshow(resultado)
elif suma=='5':
    resultado = tools.sumaClampeadaYIQ(paisaje,plaza)
    print("5 - Suma YIQ Clampeada")
    plt.imshow(resultado)
elif suma=='6':
    resultado = tools.sumaPromYIQ(paisaje,plaza)
    print("6 - Suma YIQ Promediada")
    plt.imshow(resultado)
elif suma=='7':
    resultado = tools.ifDarker(paisaje,plaza)
    print(" - ifDarker")
    plt.imshow(resultado)
else: 
    print(suma,' no es una operación definida')
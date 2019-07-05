# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 16:42:18 2019

@author: Usuario
"""

import imageio
import numpy as np
import matplotlib.pyplot as plt
import tools

#Loading image
imgpath = "images\slides8 - Remuestro\{}.png"
imgName = input("Select image name: ")
imagen = imageio.imread(imgpath.format(imgName))
print(" ")
print("Indique el color de la imagen...")
imgColor = input("0 si es B&N, o 1 si es RGB: ")
print(" ")

if imgColor == '0':
    imagen = imagen/255.
else:
    imagen = imagen[:,:,:3]/255.
imagen = np.clip(imagen,0.,1.)

plt.figure(0)
plt.imshow(imagen,'gray')

print("0 - Downsampling constante x2")
print("1 - Downsampling bilineal x2")
print("2 - Downsampling bicubico x2")
print("3 - Upsampling constante x2")
print("4 - Upsampling bilineal x2")
print("5 - Upsampling bicubico x2")
print("6 - Cuantización uniforme en B&N")

opcion = input('Elija opción de 0 a 6: ')

largo = imagen.shape[0]
alto = imagen.shape[1]

if imgColor == '0':     #matriz para B&N
    downSampledImg = np.zeros([int(largo/2),int(alto/2)])
    upSampledImg = np.zeros([int(largo*2),int(alto*2)])
    quantum = np.zeros(imagen.shape)
else:                   #matriz para Color
    downSampledImg = np.zeros([int(largo/2),int(alto/2),3])
    upSampledImg = np.zeros([int(largo*2),int(alto*2),3])

coordenadaX = 0 
coordenadaY = 0 
normal_y = 0 
normal_x = 0
prom = 0

#Solo estan desarrolladas la opcion 0, 1, 3, 4 y 6

if opcion == '0':
    #Downsampling constante x2
    while normal_y <= alto-1:
        while normal_x <= largo-1:
            if imgColor == '0':
                downSampledImg[coordenadaX,coordenadaY] = imagen[normal_x,normal_y]
            else :
                downSampledImg[coordenadaX,coordenadaY,:] = imagen[normal_x,normal_y,:]
            #de un kernel de 2x2 copiamos el pixel superior izquiero a la nueva imagen
            normal_x = normal_x+2
            coordenadaX = coordenadaX + 1
        normal_y = normal_y+2
        normal_x = 0
        coordenadaX = 0
        coordenadaY = coordenadaY + 1
    
    plt.figure(1)
    plt.figure(figsize=(2,3))
    plt.imshow(downSampledImg,'gray')
        
elif opcion == '1':
    #Downsampling bilineal x2
    while normal_y <= alto-1:
        while normal_x <= largo-1:
            if imgColor == '0':
                prom = (imagen[normal_x,normal_y]+imagen[normal_x+1,normal_y]+imagen[normal_x,normal_y+1]+imagen[normal_x+1,normal_y+1])/4
                downSampledImg[coordenadaX,coordenadaY] = prom 
            else :
                prom = (imagen[normal_x,normal_y,:]+imagen[normal_x+1,normal_y,:]+imagen[normal_x,normal_y+1,:]+imagen[normal_x+1,normal_y+1,:])/4
                downSampledImg[coordenadaX,coordenadaY,:] = prom
            #de un kernel de 2x2 copiamos un promedio de los 4pixeles a la nueva imagen
            normal_x = normal_x+2
            coordenadaX = coordenadaX + 1
        normal_y = normal_y+2
        normal_x = 0
        coordenadaX = 0
        coordenadaY = coordenadaY + 1
    plt.figure(1)
    plt.figure(figsize=(2,3))
    plt.imshow(downSampledImg,'gray')
    
elif opcion == '2':
    print("No implementado")

elif opcion == '3':
    #Upsampling constante x2
    while normal_y <= alto-1:
        while normal_x <= largo-1:
            if imgColor == '0':
                upSampledImg[coordenadaX,coordenadaY]     = imagen[normal_x,normal_y]
                upSampledImg[coordenadaX+1,coordenadaY]   = imagen[normal_x,normal_y]
                upSampledImg[coordenadaX,coordenadaY+1]   = imagen[normal_x,normal_y]
                upSampledImg[coordenadaX+1,coordenadaY+1] = imagen[normal_x,normal_y]
            else :
                upSampledImg[coordenadaX,coordenadaY,:]     = imagen[normal_x,normal_y,:]
                upSampledImg[coordenadaX+1,coordenadaY,:]   = imagen[normal_x,normal_y,:]
                upSampledImg[coordenadaX,coordenadaY+1,:]   = imagen[normal_x,normal_y,:]
                upSampledImg[coordenadaX+1,coordenadaY+1,:] = imagen[normal_x,normal_y,:]
            #de un pixel de la imagen original copiamos el valor a los 4pixeles de la imagen aumentada
            normal_x = normal_x+1
            coordenadaX = coordenadaX + 2
        normal_y = normal_y+1
        normal_x = 0
        coordenadaX = 0
        coordenadaY = coordenadaY + 2
    
    plt.figure(1)
    plt.figure(figsize=(7.5,10))
    plt.imshow(upSampledImg,'gray')
    
elif opcion == '4':
    #Upsampling bilineal x2
    #tuvimos problemas con los bordes la imagen por eso hay 'if' para evitarlo, creemos que eso no funciona del todo bien.
    while normal_y <= alto-1:
        while normal_x <= largo-1:
            if normal_x == 63:
                normal_x = 62
            if normal_y == 63:
                normal_y = 62
            if imgColor == '0':
                upSampledImg[coordenadaX,coordenadaY]     = imagen[normal_x,normal_y]
            
                promX = imagen[normal_x,normal_y]+imagen[normal_x+1,normal_y]/2
                upSampledImg[coordenadaX+1,coordenadaY]   = promX
            
                promY = imagen[normal_x,normal_y]+imagen[normal_x,normal_y+1]/2
                upSampledImg[coordenadaX,coordenadaY+1]   = promY
            
                prom = (imagen[normal_x,normal_y]+imagen[normal_x+1,normal_y]+imagen[normal_x,normal_y+1]+imagen[normal_x+1,normal_y+1])
                prom = prom/4
                upSampledImg[coordenadaX+1,coordenadaY+1] = prom
            else : #en RGB no funciona.
                upSampledImg[coordenadaX,coordenadaY,:]     = imagen[normal_x,normal_y,:]
            
                promX = imagen[normal_x,normal_y,:]+imagen[normal_x+1,normal_y,:]/2
                upSampledImg[coordenadaX+1,coordenadaY,:]   = promX
            
                promY = imagen[normal_x,normal_y,:]+imagen[normal_x,normal_y+1,:]/2
                upSampledImg[coordenadaX,coordenadaY+1,:]   = promY
            
                prom = (imagen[normal_x,normal_y,:]+imagen[normal_x+1,normal_y,:]+imagen[normal_x,normal_y+1,:]+imagen[normal_x+1,normal_y+1,:])
                prom = prom/4
                upSampledImg[coordenadaX+1,coordenadaY+1,:] = prom
            #a la imagen aumentada se copian el promedio horizontal, vertical, y total para los 4nuevos pixeles
            normal_x = normal_x+1
            
            coordenadaX = coordenadaX + 2
            if coordenadaX >= 127:
                break
        normal_y = normal_y+1
        normal_x = 0
        coordenadaX = 0
        coordenadaY = coordenadaY + 2
        if coordenadaY >= 127:
            break
    
    plt.figure(1)
    plt.figure(figsize=(7.5,10))
    plt.imshow(upSampledImg,'gray') 
    
elif opcion == '5':
    print("No implementado")

elif opcion == '6':
    #Cuantizaión unforme
    while normal_y <= alto-1:
        while normal_x <= largo-1:
            if imagen[normal_x,normal_y] <= 0.25:
                quantum[normal_x,normal_y] = 0.25
            elif imagen[normal_x,normal_y] <= 0.5:
                quantum[normal_x,normal_y] = 0.5
            elif imagen[normal_x,normal_y] <= 0.75:
                quantum[normal_x,normal_y] = 0.75
            elif imagen[normal_x,normal_y] <= 1:
                quantum[normal_x,normal_y] = 1
            #establecemos 4 nieveles discretos para la escala de grises    
            normal_x = normal_x + 1
        normal_x = 0
        normal_y = normal_y + 1
    plt.figure(1)
    plt.imshow(quantum,'gray')
    
    
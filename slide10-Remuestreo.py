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

imgColor = input("Indique 0 si la imagen es B&N, o 1 si es RGB: ")
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


opcion = input('Elija opción de 0 a 3: ')
lado = [imagen.shape[0]]

#downsizing = np.zeros[int(imagen.shape[0]/2),int(imagen.shape[0]/2)]
#upsizing = np.zeros(int(imagen.shape[0]*2),int(imagen.shape[1]*2))
largo = imagen.shape[0]
alto = imagen.shape[1]

downsizing = np.zeros([int(largo/2),int(alto/2)])
upsizing = np.zeros([int(largo*2),int(alto*2)])


coordenadaX = 0 
coordenadaY = 0 
normal_y = 0 
normal_x = 0
prom = 0

if opcion == '0':
    #Downsampling constante x2
    while normal_y <= alto-1:
        while normal_x <= largo-1:
            downsizing[coordenadaX,coordenadaY] = imagen[normal_x,normal_y]
            
            normal_x = normal_x+2
            coordenadaX = coordenadaX + 1
        normal_y = normal_y+2
        normal_x = 0
        coordenadaX = 0
        coordenadaY = coordenadaY + 1
    
    plt.figure(1)
    plt.imshow(downsizing,'gray')
        
elif opcion == '1':
    #Downsampling bilineal x2
    while normal_y <= alto-1:
        while normal_x <= largo-1:
            prom = (imagen[normal_x,normal_y]+imagen[normal_x+1,normal_y]+imagen[normal_x,normal_y+1]+imagen[normal_x+1,normal_y+1])/4
            downsizing[coordenadaX,coordenadaY] = prom 
            
            normal_x = normal_x+2
            coordenadaX = coordenadaX + 1
        normal_y = normal_y+2
        normal_x = 0
        coordenadaX = 0
        coordenadaY = coordenadaY + 1
    #downsizing = downsizing*100
    plt.figure(1)
    plt.imshow(downsizing,'gray')
    
elif opcion == '3':
    #Upsampling constante x2
    while normal_y <= alto-1:
        while normal_x <= largo-1:
            upsizing[coordenadaX,coordenadaY]     = imagen[normal_x,normal_y]
            upsizing[coordenadaX+1,coordenadaY]   = imagen[normal_x,normal_y]
            upsizing[coordenadaX,coordenadaY+1]   = imagen[normal_x,normal_y]
            upsizing[coordenadaX+1,coordenadaY+1] = imagen[normal_x,normal_y]
            
            normal_x = normal_x+1
            coordenadaX = coordenadaX + 2
        normal_y = normal_y+1
        normal_x = 0
        coordenadaX = 0
        coordenadaY = coordenadaY + 2
    #downsizing = downsizing*100
    plt.figure(1)
    plt.imshow(upsizing,'gray')
    
elif opcion == '4':
    #Upsampling bilineal x2
    #np.insert(imagen,largo,imagen[largo-1],axis=0)
    #np.insert(imagen,alto,imagen[alto-1],axis=1)
    #plt.figure(0)
    #plt.imshow(imagen,'gray')
    #print (largo)
    #print (alto)
    while normal_y <= alto-1:
        while normal_x <= largo-1:
            if normal_x == 63:
                normal_x = 62
            if normal_y == 63:
                normal_y = 62
            
            upsizing[coordenadaX,coordenadaY]     = imagen[normal_x,normal_y]
            
            promX = imagen[normal_x,normal_y]+imagen[normal_x+1,normal_y]/2
            upsizing[coordenadaX+1,coordenadaY]   = promX
            
            promY = imagen[normal_x,normal_y]+imagen[normal_x,normal_y+1]/2
            upsizing[coordenadaX,coordenadaY+1]   = promY
            
            prom = (imagen[normal_x,normal_y]+imagen[normal_x+1,normal_y]+imagen[normal_x,normal_y+1]+imagen[normal_x+1,normal_y+1])
            prom = prom/4
            upsizing[coordenadaX+1,coordenadaY+1] = prom
            
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
    #downsizing = downsizing*100
    plt.figure(1)
    plt.imshow(upsizing,'gray')
    
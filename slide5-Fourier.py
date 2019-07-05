# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 23:24:14 2019

@author: Suriano, Ramiro & Armanasco, Matias
"""

import imageio
import numpy as np
import matplotlib.pyplot as plt
import tools
from PIL import Image

#Carga de la imagen
img = "images\slides5 - Fourier\{}.png"
imgName = input("Select image name: ")
imagen = imageio.imread(img.format(imgName))
imagen = imagen/255.
imagen = np.clip(imagen,0.,1.)

#Calculo y plot de la magnitud y fase de la transformada de Fourier
imagen_fourier = tools.fourier(imagen)
plt.figure(0)
plt.imshow(imagen,'gray')
plt.figure(1)
plt.imshow(np.log10(imagen_fourier[0]+1),'gray')
plt.figure(2)
plt.imshow(imagen_fourier[1],'jet')
plt.show()

#Guardado de la imagen en un archivo
mag = imagen_fourier[0]
phase = imagen_fourier[1]
fourier = Image.fromarray(np.log10(imagen_fourier[0]+1))
fourier.convert("L").save("fourier_image.bmp")

#Calculo y plot de la transformada inversa de la imagen transformada
im_inversa = tools.fourier_undo(mag,phase)
plt.figure(3)
plt.imshow(im_inversa,'gray')
plt.show()



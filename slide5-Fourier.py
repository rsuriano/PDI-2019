# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 23:24:14 2019

@author: Usuario
"""

import imageio
from scipy import fftpack
import numpy as np
import matplotlib.pyplot as plt
import tools

imagen = imageio.imread("images\slides5 - Fourier\circle.png")
imagen = imagen/255. #lo divido por 255 para cambiarlo de unit8
imagen = np.clip(imagen,0.,1.)


#transformada de fourier
transformada = np.zeros(imagen.shape)
transformada = fftpack.fft2(imagen)
#centrar la frecuencia cero en el centro
transformada = fftpack.fftshift(transformada)
#obtener la magnitud
magnitud = np.abs(transformada)
#obtener la fase
fase = np.angle(transformada)

plt.figure(0)
plt.imshow(imagen,'gray')
plt.figure(1)
plt.imshow(np.log(magnitud+1),'gray')
plt.figure(2)
plt.imshow(fase,'jet')
plt.show()

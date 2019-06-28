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
from PIL import Image

img = "images\slides5 - Fourier\{}.png"
#imagen = imagen/255. #lo divido por 255 para cambiarlo de unit8

imgName = input("Select image name: ")
imagen = imageio.imread(img.format(imgName))
imagen = imagen/255.
imagen = np.clip(imagen,0.,1.)

imagen_fourier = tools.fourier(imagen)

plt.figure(0)
plt.imshow(imagen,'gray')
plt.figure(1)
plt.imshow(np.log10(imagen_fourier[0]+1),'gray') #creo que se ve un poco mas lindo con log10
plt.figure(2)
plt.imshow(imagen_fourier[1],'jet')
plt.show()

mag = imagen_fourier[0]
phase = imagen_fourier[1]

fourier = Image.fromarray(np.log10(imagen_fourier[0]+1))
fourier.convert("L").save("fourier_image.bmp")

im_inversa = tools.fourier_undo(mag,phase)

plt.figure(3)
plt.imshow(im_inversa,'gray')
plt.show()



"""


PRUEBAS PREVIAS, SI DESCOMENTAS FUNCIONA. BORRAR ANTES DE ENVIARLO!!!


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
plt.imshow(np.log10(magnitud+1),'gray') #creo que se ve un poco mas lindo con log10
plt.figure(2)
plt.imshow(fase,'jet')
plt.show()


#transformada inversa de fourier
new_magnitud = np.zeros(imagen.shape)

centro = np.array(imagen.shape)//2

offset = (0.2 * centro[0]).astype(np.int)
new_magnitud[centro[0]-offset:centro[0]+offset,centro[1]-offset:centro[1]+offset] = 1
new_magnitud *= magnitud
#felix hizo todo esto para modificar la magnitud y usarla en la antitransformada, no se para que. Queda mejor sin esto

# retransform
transformada = magnitud * (np.cos(fase)+np.sin(fase)*1j)
imBack = np.abs(fftpack.ifft2(fftpack.ifftshift(transformada)))

plt.figure(1)
epsilon= 0.00001
plt.imshow(np.log(new_magnitud+epsilon),'gray')

plt.figure(2)
plt.imshow(imBack,'gray')
plt.show()
"""





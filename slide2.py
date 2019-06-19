# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 17:21:03 2019

@author: Suriano, Ramiro & Armanasco, Matias
"""
import imageio
import numpy as np
import matplotlib.pyplot as plt
import tools 


im_in = imageio.imread("images\slides2 - Luminance\Lena128C.png")
im_in = im_in[:,:,:3]/255. #dejo las dos primeras bandas, y de la tercer banda borro una (alpha)
                           #lo divido por 255 para cambiarlo de unit8


new_im = np.zeros(im_in.shape)
new_im = tools.convert_to('YIQ',im_in)

factor_luminancia = 1.2
factor_saturacion = 1

new_im[:,:,0] *= factor_luminancia
new_im[:,:,1] *= factor_saturacion
new_im[:,:,2] *= 1 - factor_saturacion

new_im[:,:,0] = np.clip(new_im[:,:,0],0.,1.)
new_im[:,:,1] = np.clip(new_im[:,:,1],-0.59,0.59)
new_im[:,:,2] = np.clip(new_im[:,:,2],-0.52,0.52)

img_procesada = np.zeros(im_in.shape)
img_procesada = tools.convert_to('RGB',new_im)

img_procesada = np.clip(img_procesada,0.,1.)
plt.imshow(img_procesada)
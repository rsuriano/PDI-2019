# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 17:21:03 2019

@author: Usuario
"""
import imageio
import numpy as np
import matplotlib.pyplot as plt
import tools 


im_in = imageio.imread("images\slides2 - Luminance\Lena128C.png")
im_in = im_in[:,:,:3]/255.  #dejo las dos primeras bandas, y de la tercer banda borro una (alpha)
                            #lo divido por 255 para cambiarlo de unit8
print(im_in.shape)
plt.imshow(im_in)

new_im = np.zeros(im_in.shape)
new_im = tools.convert_to('YIQ',im_in)

print(new_im.shape)
#new_im[:,:,0] *= 1.5 

luminancia = np.zeros(im_in.shape)
luminancia = tools.convert_to('RGB',new_im)

luminancia = np.clip(luminancia,0.,1.)
#plt.imshow(luminancia)


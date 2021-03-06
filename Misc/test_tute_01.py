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
"""
new_im[:,:,0] = 0.299000*im_in[:,:,0] + 0.587000*im_in[:,:,1] + 0.114000*im_in[:,:,2]
new_im[:,:,1] = 0.595716*im_in[:,:,0] - 0.274453*im_in[:,:,1] - 0.321263*im_in[:,:,2]
new_im[:,:,2] = 0.211456*im_in[:,:,0] - 0.522591*im_in[:,:,1] + 0.311135*im_in[:,:,2]

#plt.imshow(new_im)
"""
new_im[:,:,0] *= 1.5 

luminancia = np.zeros(im_in.shape)
luminancia = tools.convert_to('RGB',new_im)
"""
luminancia[:,:,0] = 1*new_im[:,:,0] + 0.9663*new_im[:,:,1] + 0.6210*new_im[:,:,2]
luminancia[:,:,1] = 1*new_im[:,:,0] - 0.2721*new_im[:,:,1] - 0.6474*new_im[:,:,2]
luminancia[:,:,2] = 1*new_im[:,:,0] - 1.1070*new_im[:,:,1] + 1.7046*new_im[:,:,2]
"""
luminancia = np.clip(luminancia,0.,1.)
plt.imshow(luminancia)


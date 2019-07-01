# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 15:29:20 2019

@author: Ramiro
"""

import imageio
import numpy as np
import matplotlib.pyplot as plt
import tools

#Loading image
imgpath = "images\slides7 - Morphology\{}.png"
imgName = input("Select image name: ")
imagen = imageio.imread(imgpath.format(imgName))
#normalizacion
if len(imagen.shape)>2:
    imagen = imagen[:,:,0]/255. 
else:
    imagen = imagen/255. 
imagen = np.clip(imagen,0.,1.)

plt.figure(0)
plt.imshow(imagen,'gray')

#img2 = tools.erosionar(imagen,5)
#img2 = tools.dilatar(img2,1)
#img2 = tools.apertura(imagen)
img2 = tools.topHat(imagen)

plt.figure(1)
plt.imshow(img2, 'gray')
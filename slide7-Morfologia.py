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
imagen = imagen/255. #lo divido por 255 para cambiarlo de unit8
imagen = np.clip(imagen,0.,1.)

plt.figure(0)
plt.imshow(imagen,'gray')

img2 = tools.erode(imagen,5)
#img2 = tools.dilate(img2,1)

plt.figure(1)
plt.imshow(img2, 'gray')
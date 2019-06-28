# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 01:42:05 2019

@author: Usuario
"""

import imageio
from scipy import fftpack
import numpy as np
import matplotlib.pyplot as plt
import tools
from PIL import Image

imagen = imageio.imread("images/fourier_image.bmp")
imagen = imagen/255. #lo divido por 255 para cambiarlo de unit8
imagen = np.clip(imagen,0.,1.)

plt.figure(0)
plt.imshow(imagen,'gray')
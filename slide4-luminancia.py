# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 21:32:52 2019

@author: Suriano, Ramiro & Armanasco, Matias
"""

import imageio
import numpy as np
import matplotlib.pyplot as plt
import tools
import tkinter as tk

columnQty = 100
imgpath = "images\slides4 - Histogram\{}.png"
imgName = input("Select image name: ")

img = imageio.imread(imgpath.format(imgName))
img = img[:,:,:3]/255.

img_YIQ = tools.convert_to('YIQ', img)
img_Y = img_YIQ[:,:,0]
histogram = np.zeros((1,columnQty))

for i in np.ndenumerate(img_YIQ[:,:,0]):
    #print(int(np.trunc(i[1]*columnQty)))
    histogram[0,int(np.trunc(i[1]*columnQty))] +=1/np.prod(img_Y.shape)

histogram = histogram[0]
names = np.arange(0,len(histogram))


plt.figure(1)
plt.imshow(img)
plt.figure(2)
plt.bar(names,histogram)
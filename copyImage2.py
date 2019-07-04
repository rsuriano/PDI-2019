# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 23:57:22 2019

@author: Ramiro
"""

import numpy as np

img = np.arange(1, 10)
img = np.reshape(img, (3,3))

print(img)

margin = 4
newImg = np.zeros((img.shape[0]+2*margin, img.shape[1]+2*margin))

for i in np.ndenumerate(newImg):
    nImgCoord = i[0]
    
    #Copy img at the center of newImg
    if (nImgCoord[0]<newImg.shape[0]-2*margin and nImgCoord[1]<newImg.shape[1]-2*margin):
        newImg[(nImgCoord[0]+margin, nImgCoord[1]+margin)] = img[nImgCoord] 

for a in range(0, margin):
    newImg[a,:] = newImg[margin,:]
    newImg[:,a] = newImg[:,margin]
    newImg[newImg.shape[0]-(margin-a), :] = newImg[newImg.shape[0]-margin-1, :]
    newImg[:, newImg.shape[0]-(margin-a)] = newImg[:, newImg.shape[0]-margin-1]

print(newImg)

#Get original img
origImg = np.zeros((newImg.shape[0]-2*margin, newImg.shape[1]-2*margin))
for i in np.ndenumerate(newImg):
    nImgCoord = i[0]
    
    if (0 < nImgCoord[0]<newImg.shape[0]-margin) and  (0 < nImgCoord[1]<newImg.shape[1]-margin):
        origImg[(nImgCoord[0]-margin, nImgCoord[1]-margin)] = newImg[nImgCoord] 
    
print(origImg)

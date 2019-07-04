# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 23:57:22 2019

@author: Ramiro
"""

import numpy as np

img = np.arange(1, 10)
img = np.reshape(img, (3,3))

print(img)

margin = 6
newImg = np.zeros((img.shape[0]+margin, img.shape[1]+margin))

for i in np.ndenumerate(newImg):
    nImgCoord = i[0]
    
    #Copy img at the center of newImg
    if (nImgCoord[0]<newImg.shape[0]-margin and nImgCoord[1]<newImg.shape[1]-margin):
        newImg[(nImgCoord[0]+int(margin/2), nImgCoord[1]+int(margin/2))] = img[nImgCoord] 
    
for a in range(0, int(margin/2)):
    newImg[a,:] = newImg[int(margin/2),:]
    newImg[:,a] = newImg[:,int(margin/2)]
    newImg[newImg.shape[0]-(int(margin/2)-a), :] = newImg[newImg.shape[0]-int((margin/2))-1, :]
    newImg[:, newImg.shape[0]-(int(margin/2)-a)] = newImg[:, newImg.shape[0]-int((margin/2))-1]

print(newImg)

#Get original img
origImg = np.zeros((newImg.shape[0]-margin, newImg.shape[1]-margin))
for i in np.ndenumerate(newImg):
    nImgCoord = i[0]
    
    if (0 < nImgCoord[0]<newImg.shape[0]-int(margin/2)) and  (0 < nImgCoord[1]<newImg.shape[1]-int(margin/2)):
        origImg[(nImgCoord[0]-int(margin/2), nImgCoord[1]-int(margin/2))] = newImg[nImgCoord] 
    
print(origImg)
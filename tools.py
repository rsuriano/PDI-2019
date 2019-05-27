# -*- coding: utf-8 -*-
"""
Created on Fri May 17 17:40:09 2019

@author: Suriano, Ramiro & Armanasco, Matias
"""

import imageio
import numpy as np
import matplotlib.pyplot as plt

def convert_to(space,image): 
    #esta funcion convierte una matriz 'image' al espacio cromático indicado en 'space'
    imageRet = np.zeros(image.shape)
    toYIQ = np.array([[0.299,0.587,0.114] , [0.595716,-0.274453,-0.321263] , [0.211456,-0.522591,0.311135]])
    toRGB = np.array([[1,0.9663,0.621] , [1,-0.2721,-0.6474] , [1,-1.107,1.7046]])
    imgAux = np.array([image[:,:,0],image[:,:,1],image[:,:,2]])
    
    if (space == 'RGB'):
        imageRet[:,:,0] = toRGB[0,0]*image[:,:,0] + toRGB[0,1]*image[:,:,1] + toRGB[0,2]*image[:,:,2]
        imageRet[:,:,1] = toRGB[1,0]*image[:,:,0] + toRGB[1,1]*image[:,:,1] + toRGB[1,2]*image[:,:,2]
        imageRet[:,:,2] = toRGB[2,0]*image[:,:,0] + toRGB[2,1]*image[:,:,1] + toRGB[2,2]*image[:,:,2]
        return imageRet
    
    if (space == 'YIQ'):
        imageRet[:,:,0] = toYIQ[0,0]*image[:,:,0] + toYIQ[0,1]*image[:,:,1] + toYIQ[0,2]*image[:,:,2]
        imageRet[:,:,1] = toYIQ[1,0]*image[:,:,0] + toYIQ[1,1]*image[:,:,1] + toYIQ[1,2]*image[:,:,2]
        imageRet[:,:,2] = toYIQ[2,0]*image[:,:,0] + toYIQ[2,1]*image[:,:,1] + toYIQ[2,2]*image[:,:,2]
        
        return imageRet
    
    
    
    
    
 
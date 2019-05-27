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
    toYIQ = toRGB = np.zeros((3,3))
    imageRet = np.zeros(image.shape)
    toYIQ = [[0.299,0.587,0.114] , [0.595716,-0.274453,-0.321263] , [0.211456,-0.522591,0.311135]] 
    toRGB = [[1,0.9663,0.621] , [1,-0.2721,-0.6474] , [1,-1.107,1.7046]]
    
    
    if (space == 'RGB'):
        imageRet[:,:,0] = [image[:,:,0]*[toRGB[0,:]]
        imageRet[:,:,1] = [image[:,:,1]*[toRGB[1,:]]
        imageRet[:,:,2] = [image[:,:,2]*[toRGB[2,:]]
    
        return imageRet
    if (space == 'YIQ'):
        imageRet[:,:,0] = [image[:,:,0]*[toYIQ[0,:]]
        imageRet[:,:,1] = [image[:,:,1]*[toYIQ[1,:]]
        imageRet[:,:,2] = [image[:,:,2]*[toYIQ[2,:]]
        
        return imageRet
    
    
    
    
    
 
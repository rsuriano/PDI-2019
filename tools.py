# -*- coding: utf-8 -*-
"""
Created on Fri May 17 17:40:09 2019

@author: Usuario
"""

import imageio
import numpy as np
import matplotlib.pyplot as plt

def convert_to(space,image):
    
    toYIQ = toRGB = np.zeros((3,3))
    toYIQ = [[0.299, 0.587, 0.114] , [0.595716, -0.274453, -0.321263] , [0.211456, -0.522591, 0.311135]] 
    toRGB = [[1, 0.9663, 0.621] , [1, -0.2721, -0.6474] , [1, -1.107, 1.7046]]
    
    if (space == 'YIQ'):
        return np.dot(toRGB, image)
            
            
    if (space == 'RGB'):
        return 0
    
    
    
 
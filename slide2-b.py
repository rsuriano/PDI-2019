# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 17:21:03 2019

@author: Suriano, Ramiro & Armanasco, Matias
"""
import imageio
import matplotlib.pyplot as plt
import tools

fig=plt.figure()

im_lena = imageio.imread("images\slides2 - Colormaps\Lena128G.png")
im_particles = imageio.imread("images\slides2 - Colormaps\ParticlesG.png")
im_retina = imageio.imread("images\slides2 - Colormaps\RetinaG.png")

showColormaps(im_lena)
showColormaps(im_particles)
showColormaps(im_retina)



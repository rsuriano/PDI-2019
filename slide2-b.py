# -*- coding: utf-8 -*-
"""
Created on Fry May 24 23:37:16 2019

@author: Suriano, Ramiro & Armanasco, Matias
"""
import imageio
import matplotlib.pyplot as plt
import tools

fig=plt.figure()

im_lena = imageio.imread("images\slides2 - Colormaps\Lena128G.png")
im_particles = imageio.imread("images\slides2 - Colormaps\ParticlesG.png")
im_retina = imageio.imread("images\slides2 - Colormaps\RetinaG.png")

tools.showColormaps(im_lena)
tools.showColormaps(im_particles)
tools.showColormaps(im_retina)
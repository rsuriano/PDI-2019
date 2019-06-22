# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 16:14:22 2019

@author: Ramiro
"""

from tkinter import *      
root = Tk()      
canvas = Canvas(root, width = 300, height = 300)      
canvas.pack()      
img = PhotoImage(file="color maps.png")      
canvas.create_image(20,20, anchor=NW, image=img)      
mainloop()    
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 02:33:20 2019

@author: Ramiro
"""

import imageio
import numpy as np
import matplotlib.pyplot as plt
import tools
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.load = tk.Button(self)
        self.load["text"] = "Cargar Imagen"
        self.load["command"] = self.printImage
        self.load.pack(side="bottom")

    def printImage(self):
        imgRGB = imageio.imread("images\slides4 - Histogram\Lena512.png")
        imagen = tk.PhotoImage(file='images\slides4 - Histogram\Lena512.png')
        cv = tk.Canvas(root, width = 300, height = 300)
        cv.create_image((20,20),image=imagen,anchor='nw')
        print("Image loaded successfully")
    

root = tk.Tk()
app = Application(master=root)
app.mainloop()
'''
This file main Job is creating the 3-D meshes
'''

import numpy as np
import pyvista as vista


def Generation3(shape):
    if shape == 2:
        cube()
    elif shape == 1:
        sphere()
    else:
        print("Can't create this mesh yet.")

def cube():
    c = vista.Box()
    p = vista.Plotter(shape=(1,1))
    p.subplot(0,0)
    p.add_mesh(c, color='lightblue', show_edges=True)
    p.show()

def sphere():
    s = vista.Sphere()
    p = vista.Plotter(shape=(1,1))
    p.subplot(0,0)
    p.add_mesh(s, color='lightblue', show_edges=True)
    p.show()
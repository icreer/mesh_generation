'''
This file main Job is creating the 3-D meshes
'''

import numpy as np
import pyvista as vista


def Generation3(shape):

    if shape == 2:
        mesh = cube()
    elif shape == 1:
        mesh = sphere()
    else:
        mesh = 0
        print("Can't create this mesh yet.")
    return mesh

def cube():
    c = vista.Box()
    p = vista.Plotter(shape=(1,1))
    p.subplot(0,0)
    p.add_mesh(c, color='lightblue', show_edges=True)

    points = [[1,1,1],[1,-1,1],[-1,1,1],[1,1,-1],[-1,-1,1],[-1,-1,-1],[1,-1,-1],[-1,1,-1]]

    cells = [len(points)] + list(range(len(points)))

    box = vista.UnstructuredGrid(cells, [vista.CellType.VOXEL], points)
    
    return box

def sphere():
    s = vista.Sphere()
    p = vista.Plotter(shape=(1,1))
    p.subplot(0,0)
    p.add_mesh(s, color='lightblue', show_edges=True)
    return p
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
    '''
    Create a 2x2x2 cube as of right now can't edit that
    '''
    points = [[1,1,1],[1,-1,1],
              [-1,1,1],[-1,-1,1],
              [1,1,-1],[1,-1,-1],
              [-1,1,-1],[-1,-1,-1]]

    cells = [len(points)] + list(range(len(points)))

    box = vista.UnstructuredGrid(cells, [vista.CellType.VOXEL], points)
    
    return box

def sphere():
    '''
    This creates two sphere in each of each other. Next step is figuring out how to not make it just one cell
    '''

    number_of_points = 100
    outer_factor = 1
    inter_facotr = 0.95
    outer_points = []
    inter_points = []
    for i in range(number_of_points):
        outer_points.append([outer_factor*np.cos((i*2*np.pi)/number_of_points),outer_factor*np.sin((i*2*np.pi)/number_of_points), outer_factor*np.cos((i*np.pi)/(number_of_points))])
        inter_points.append([inter_facotr*np.cos((i*2*np.pi)/number_of_points),inter_facotr*np.sin((i*2*np.pi)/number_of_points), inter_facotr*np.cos((i*np.pi)/(number_of_points))])
        
    print(outer_points)
    print(inter_points)

    return 0
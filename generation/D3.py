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
    Remember that cell is a factor of points to faces
    '''
    # mesh points
    number_of_points = 100
    outer_factor = 1
    inter_facotr = 0.95
    outer_points = []
    inter_points = []
    m = 2*np.pi / number_of_points # multiplication factor 

    for i in range(number_of_points):
        for k in range(number_of_points):
            outer_points.append([outer_factor*np.cos(k*m)*np.sin(i*m), outer_factor*np.sin(k*m)*np.sin(i*m), outer_factor*np.cos(i*m)])
            inter_points.append([inter_facotr*np.cos(k*m)*np.sin(i*m), inter_facotr*np.sin(k*m)*np.sin(i*m), inter_facotr*np.cos(i*m)])

    # mesh faces
    # the number of faces will depend on what the cell shape that exist 
    square = 6/8
    number_of_faces = int(number_of_points * square)
    top_faces = []
    bottom_faces = []
    sides_1 = []
    sides_2 = []

    vista.PolyData

    #faces = np.hstack([])


    return outer_points
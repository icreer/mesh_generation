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
    number_of_points = 10
    outer_factor = 1
    inter_facotr = 0.95
    outer_points = []
    inter_points = []
    m = 2*np.pi / number_of_points # multiplication factor 

    for i in range(number_of_points):
        for k in range(number_of_points):
            x = np.cos(k*m)*np.sin(i*m)
            y = np.sin(k*m)*np.sin(i*m)
            z = np.cos(i*m)

            outer_points.append([outer_factor * x, outer_factor * y, outer_factor * z])
            inter_points.append([inter_facotr * x, inter_facotr * y, inter_facotr * z])

    
    points = outer_points + inter_points

    print(len(outer_points))
    print(len(inter_points))

    print(len(points))

    # mesh faces
    # the number of faces will depend on what the cell shape that exist 
    square = 6/8
    number_of_faces = int(number_of_points * square)
    top_faces = []
    bottom_faces = []
    sides_1 = []
    sides_2 = []

    for i in range(number_of_points**2):
        top_faces.append([4,i,i+1,i+number_of_points+1,i+number_of_points])
        bottom_faces.append([4,i+len(outer_points),i+1+len(outer_points),i+number_of_points+1+len(outer_points),i+number_of_points+len(outer_points)])
        sides_2.append([4, i, i+len(outer_points), i+len(outer_points)+number_of_points, i+number_of_points])

    f = 0
    while f < number_of_points**2:
        sides_1.append([4,f,f+1,f+len(outer_points)+1,f+len(outer_points)])
        f+=2



    faces = np.hstack(sides_1 + top_faces + bottom_faces + sides_2)

    cells = [8] + list(range(len(points)))

    surf = vista.PolyData(points,faces)


    return surf
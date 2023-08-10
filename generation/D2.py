'''
This File is the main location for creating 2-D shapes
'''

import numpy as np
import pyvista as vista 


def Generation2(shape):
    if shape == 1:
        Square()
    elif shape == 2:
        circle()
    elif shape == 3:
        Octagon()
    elif shape == 4:
        Equlatral_trinalge()
    else:
        print("This is not a shape that can be generated right now.")

def Square():
    pass

def circle():
    pass

def Octagon():
    pass

def Equlatral_trinalge():
    pass

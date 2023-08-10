'''
This file main Job is creating the 3-D meshes
'''

import numpy as np
import pyvista as vista
from mesh import Mesh

class Generation3():
    def __init__(self, option):
        super().__init__(option)
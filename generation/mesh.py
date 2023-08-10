'''
This file is for holding the class called mesh witch is were all the simulares between 2-D and 3-D meshes 
'''

import numpy as np
import pyvista as vista 
from generation.D2 import Generation2
from generation.D3 import Generation3

class Mesh():
    def __init__(self, dimention, shape, mesh_number):
        self.dimention = dimention
        self.shape = shape
        self.number = mesh_number

    def generate(self):
        print("works")
        if self.dimention == 2:
            Generation2(self.shape)
        elif self.dimention == 3:
            Generation3(self.shape)
        else:
            print(f"Can't develp a {self.dimention}-D Mesh ")
        
    def show(self):
        pass


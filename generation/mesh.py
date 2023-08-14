'''
This file is for holding the class called mesh witch is were all the simulares between 2-D and 3-D meshes 
'''

import pyvista as vista
from generation.D2 import Generation2
from generation.D3 import Generation3

class Mesh():
    def __init__(self, dimention, shape, mesh_number):
        self.dimention = dimention
        self.shape = shape
        self.number = mesh_number
        self.mesh = 0

    def generate(self):
        if self.dimention == 2:
            Generation2(self.shape)
        elif self.dimention == 3:
            self.mesh = Generation3(self.shape)
        else:
            print(f"Can't develp a {self.dimention}-D Mesh ")
        
    def show(self):
        print(self.mesh)
        if self.mesh != 0:
            plotter = vista.Plotter()
            plotter.add_mesh(self.mesh)
            plotter.show()
        else:
            print(f"Was not able to generate mesh number {self.number}")


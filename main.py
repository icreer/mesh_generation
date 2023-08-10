'''

'''
import numpy as np
import pyvista as vista 
import threading 

from generation.mesh import Mesh


def option():
    
    creation = []
    number_to_make = int(input("Please enter the number of meshes you wish to create:"))
    n = 0
    while n < number_to_make:
        dementions = int(input("Please select the type of mesh you want generated: \n\t1.2-D \n\t2.3-D \nSelection:")) + 1
        if ( dementions == 2):
            shape = int(input("Please select a 2-D shape: \n\t1.Square\n\t2.Circle\n\t3.Octagon\n\t4.Equlatral Triangle \nSelection:"))
        elif (dementions == 3):
            shape = int(input("Please select a shape: \n\t1.Sphere \n\t2.Cube \nSelection:"))
        else:
            shape = 0
        creation.append((dementions,shape))
        n+=1

    return (creation , number_to_make)

def main():
    create = option()
    print(create)
    meshes = []
    for x in range(create[1]):
        meshes.append(Mesh(create[0][0],create[0][1], x))
    
    for m in meshes:
        m.generate()


if __name__ == '__main__':
    main()
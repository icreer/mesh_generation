'''

'''
import numpy as np
import pyvista as vista 

from generation.mesh import Mesh


def option():
    print("Works")
    dementions = int(input("Please select the type of mesh you want generated: \n\t1.2-D \n\t2.3-D \nSelection:")) + 1
    if ( dementions == 2):
        shape = int(input("Please select a 2-D shape: \n\t1.Square\n\t2.Circle\n\t3.Octagon\n\t4.Equlatral Triangle \nSelection:"))
    elif (dementions == 3):
        shape = int(input("Please select a shape: \n\t1.Sphere \n\t2.Cube \nSelection:"))
    else:
        shape = 0
    return (dementions, shape)

def main():
    create = option()
    print(create)
    m = Mesh(create)


if __name__ == '__main__':
    main()
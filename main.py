'''
This file is the is the main file that cotrals all the action the the mesh files do. 
'''

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

    return creation

def main():
    create = option()
    
    meshes = []
    for x in range(len(create)):
        
        meshes.append(Mesh(create[x][0], create[x][1],x+1))
    
    for m in meshes:
        m.generate()
    
    for m in meshes:
        m.show()


if __name__ == '__main__':
    main()
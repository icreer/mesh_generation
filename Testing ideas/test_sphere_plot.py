import numpy as np
import matplotlib.pyplot as plt

ax = plt.figure().add_subplot(projection='3d')

number_of_points = 100
outer_factor = 1
inter_facotr = 0.95
outer_points = []
inter_points = []
x = []
y = []
z = []
for i in range(number_of_points):
    outer_points.append([outer_factor*np.cos((i*2*np.pi)/number_of_points),outer_factor*np.sin((i*2*np.pi)/number_of_points), outer_factor*np.cos((i*np.pi)/(number_of_points))])
    inter_points.append([inter_facotr*np.cos((i*2*np.pi)/number_of_points),inter_facotr*np.sin((i*2*np.pi)/number_of_points), inter_facotr*np.cos((i*np.pi)/(number_of_points))])
    for k in range(number_of_points):
        x.append(outer_factor*np.cos((k*2*np.pi)/number_of_points))
        y.append(outer_factor*np.sin((k*2*np.pi)/number_of_points))
        #z.append(outer_factor*np.tan((k*2*np.pi)/(number_of_points)))
        z.append(outer_factor*np.sqrt((outer_factor*np.cos((k*2*np.pi)/number_of_points))**2 + (outer_factor*np.sin((k*2*np.pi)/number_of_points))**2 ))

ax.scatter(x,y,z)
plt.show()

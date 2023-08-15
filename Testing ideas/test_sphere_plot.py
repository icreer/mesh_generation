import numpy as np
import matplotlib.pyplot as plt

ax = plt.figure().add_subplot(projection='3d')

number_of_points = 100
outer_factor = 10
inter_facotr = 0.95
outer_points = []
inter_points = []
x = []
y = []
z = []
m = 2*np.pi / number_of_points
for i in range(number_of_points):
    for k in range(number_of_points):
        x.append(outer_factor*np.cos(k*m)*np.sin(i*m))
        y.append(outer_factor*np.sin(k*m)*np.sin(i*m))
        z.append(outer_factor*np.cos(i*m))
        outer_points.append([outer_factor*np.cos(k*m)*np.sin(i*m), outer_factor*np.sin(k*m)*np.sin(i*m), outer_factor*np.cos(i*m)])
        inter_points.append([inter_facotr*np.cos(k*m)*np.sin(i*m), inter_facotr*np.sin(k*m)*np.sin(i*m), inter_facotr*np.cos(i*m)])

ax.scatter(x,y,z)
plt.show()

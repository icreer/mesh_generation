import numpy as np

number_of_points = 10
outer_factor = 1
inter_facotr = 0.95
outer_points = []
inter_points = []
m = 2*np.pi / number_of_points # multiplication factor 

for i in range(number_of_points):
    for k in range(number_of_points):
        outer_points.append([outer_factor*np.cos(k*m)*np.sin(i*m), outer_factor*np.sin(k*m)*np.sin(i*m), outer_factor*np.cos(i*m)])
        inter_points.append([inter_facotr*np.cos(k*m)*np.sin(i*m), inter_facotr*np.sin(k*m)*np.sin(i*m), inter_facotr*np.cos(i*m)])

points = outer_points + inter_points

for i in range(len(points)):
    print(points[i])
    if points[i] == [0.0,0.0,0.0]:
        points.pop(i)
        print("worked")

print(len(outer_points))
print(len(inter_points))

print(len(points))
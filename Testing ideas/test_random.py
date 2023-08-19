import numpy as np

number_of_points = 10
outer_factor = 1
inter_facotr = 0.95
outer_points = []
inter_points = []
m = 2*np.pi / number_of_points # multiplication factor 

for i in range(number_of_points):
    for k in range(number_of_points):
        x = np.cos(k*m)*np.sin(i*m)
        y = np.sin(k*m)*np.sin(i*m)
        z = np.cos(i*m)

        outer_points.append([outer_factor * x, outer_factor * y, outer_factor * z])
        inter_points.append([inter_facotr * x, inter_facotr * y, inter_facotr * z])

 
# Check if there is duplicates



points = outer_points + inter_points

for i in range(len(points)):
    print(points[i])
    if points[i] == [0.0,0.0,0.0]:
        points.pop(i)
        print("worked")

print(len(outer_points))
print(len(inter_points))

print(len(points))
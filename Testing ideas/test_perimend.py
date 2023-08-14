'''
This file is here for testing ideas and consepts without easier
'''
import numpy as np

import pyvista as pv

# mesh points
vertices = np.array([[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0], [0.5, 0.5, -1]])

# mesh faces
faces = np.hstack(
    [
        [4, 0, 1, 2, 3],  # square
        [3, 0, 1, 4],  # triangle
        [3, 1, 2, 4],  # triangle
        [3, 2, 3, 4],
        [3, 3, 0, 4],
    ]
)

surf = pv.PolyData(vertices, faces)

# plot each face with a different color
surf.plot(
    scalars=np.arange(5),
    cpos=[-1, 1, 0.5],
    show_scalar_bar=False,
    show_edges=True,
    line_width=5,
)
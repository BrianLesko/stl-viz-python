import numpy as np
from stl import mesh
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load the mesh from the STL file
your_mesh = mesh.Mesh.from_file('my_stl.stl')

# Extract the vertices
vertices = np.array(your_mesh.vectors).reshape(-1, 3)
x, y, z = vertices.T

# Use the I, J, K indices directly
I, J, K = np.arange(vertices.shape[0]).reshape(-1, 3).T

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')



ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
import numpy as np
import plotly.graph_objects as go
from stl import mesh #! pip install numpy-stl

# Load the mesh from the STL file
your_mesh = mesh.Mesh.from_file('my_stl.stl')

# Extract the vertices and reshape
vertices = np.array(your_mesh.vectors).reshape(-1, 3)
x, y, z = vertices.T

# Generate the list of indices for the triangles
indices = np.arange(vertices.shape[0]).reshape(-1, 3)
I, J, K = indices.T

fig = go.Figure(data=[go.Mesh3d(
    x=x, y=y, z=z,
    i=I, j=J, k=K,
    color='#E8E9ED',
    opacity=1,
    flatshading=False,
    lighting=dict(ambient=0.3, diffuse=1, specular=0.5, roughness=0.3),
    lightposition=dict(x=100, y=100, z=200)
)])

# Update layout
fig.update_layout(
    title='3D Model Visualization',
    scene=dict(
        xaxis=dict(showbackground=False, title='X-axis'),
        yaxis=dict(showbackground=False, title='Y-axis'),
        zaxis=dict(showbackground=False, title='Z-axis'),
        camera=dict(
            eye=dict(x=1.5, y=1.5, z=1.5)  # Adjust the camera position
        )
    ),
    annotations=[{
        "showarrow": False, 
        "text": "Detailed View",
        "x": 0.5,
        "y": 0,
        "xref": "paper",
        "yref": "paper",
        "align": "center"
    }]
)

fig.show()
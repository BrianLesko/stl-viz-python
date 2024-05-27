import pyvista as pv

def view_stl(file_path):
    # Load mesh
    mesh = pv.read(file_path)

    # Plot mesh
    plotter = pv.Plotter()
    plotter.add_mesh(mesh, color='white', show_edges=False)
    plotter.show()

# Replace 'path_to_your_file.stl' with the path to your STL file
view_stl('my_stl.stl')

from projectionViewer import ProjectionViewer 
import wireframe
import numpy as np
from obj_loader import OBJ_loader

# cube = wireframe.Wireframe()
# cube2 = wireframe.Wireframe()
# cube3 = wireframe.Wireframe()

cube_nodes = [(x, y, z) for x in (50, 250) for y in (50, 250) for z in (50, 250)]
# cube_nodes2 = [(x, y, z) for x in (250, 400) for y in (250, 400) for z in (250, 400)]
# cube_nodes3 = [(x, y, z) for x in (1, 800) for y in (400, 401) for z in (1, 800)]

print(cube_nodes)

# cube.addNodes(np.array(cube_nodes))
# cube.addEdges([(n, n + 4) for n in range(0, 4)])
# cube.addEdges([(n, n + 1) for n in range(0, 8, 2)])
# cube.addEdges([(n, n + 2) for n in (0, 1, 4, 5)])
# cube2.addNodes(np.array(cube_nodes2))
# cube2.addEdges([(n, n + 4) for n in range(0, 4)])
# cube2.addEdges([(n, n + 1) for n in range(0, 8, 2)])
# cube2.addEdges([(n, n + 2) for n in (0, 1, 4, 5)])
# cube3.addNodes(np.array(cube_nodes3))
# cube3.addEdges([(n, n + 4) for n in range(0, 4)])
# cube3.addEdges([(n, n + 1) for n in range(0, 8, 2)])
# cube3.addEdges([(n, n + 2) for n in (0, 1, 4, 5)])

loader = OBJ_loader("./teapot.obj")

Object = loader.create_wireframe()

pv = ProjectionViewer(1200, 1000)
pv.addWireframe('object', Object)
# pv.addWireframe('cube', cube)
# pv.addWireframe('cube2', cube2)
# pv.addWireframe('cube3', cube3)


pv.run()
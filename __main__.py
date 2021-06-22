from projectionViewer import ProjectionViewer 
import wireframe
import numpy as np
from obj_loader import OBJ_loader
import random
from mesh_floor import *

# cube = wireframe.Wireframe()
# cube2 = wireframe.Wireframe()
# cube3 = wireframe.Wireframe()

# cube_nodes = [(x, y, z) for x in (50, 250) for y in (50, 500) for z in (50, 250)]
# cube_nodes2 = [(x, y, z) for x in (250, 400) for y in (250, 500) for z in (250, 5000)]
# #cube_nodes3 = [(x, y, z) for x in (1, 800) for y in (400, 401) for z in (1, 800)]

# print(cube_nodes)

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

# loader = OBJ_loader("./teapot.obj")

# Object = loader.create_wireframe()


cube = wireframe.Wireframe()

axes = wireframe.Wireframe()

a = np.array([[0,0,0],[1000,0,0], [0,1000,0], [0,0,1000]])

axes.addNodes(a)
axes.addEdges([(0,1), (0,2), (0,3)])

cube_nodes = grid_generation(10000,10000,False)

print(len(cube_nodes))

a = np.array(cube_nodes)

for i in a:
	i[1] = random.randint(1,1000)

cube.addNodes(a)
cube.addEdges([(n, n + 1) for n in range(0, 9, 1)])
cube.addEdges([(n, n + 1) for n in range(10, 19, 1)])
cube.addEdges([(n, n + 1) for n in range(20, 29, 1)])
cube.addEdges([(n, n + 1) for n in range(30, 39, 1)])
cube.addEdges([(n, n + 1) for n in range(40, 49, 1)])
cube.addEdges([(n, n + 1) for n in range(50, 59, 1)])
cube.addEdges([(n, n + 1) for n in range(60, 69, 1)])
cube.addEdges([(n, n + 1) for n in range(70, 79, 1)])
cube.addEdges([(n, n + 1) for n in range(80, 89, 1)])
cube.addEdges([(n, n + 1) for n in range(90, 99, 1)])

for i in range(0,10):
	cube.addEdges([(0+i,10+i),(10+i,20+i),(20+i,30+i),(30+i,40+i),(40+i,50+i),(50+i,60+i),(60+i,70+i),(70+i,80+i),(80+i,90+i)])
		



pv = ProjectionViewer(1200, 1000, axes)
# pv.addWireframe('object', Object)

	
pv.addWireframe('floormesh', cube)
pv.addWireframe('axes', axes)

# pv.addWireframe('cube', cube)
# pv.addWireframe('cube2', cube2)
# pv.addWireframe('cube3', cube3)


pv.run()
#Floor Mesh Generator

cubes = []

for i in range(0,40):
	for j in range(0, 40):

		cube = wireframe.Wireframe()

		cube_nodes = [(x, y, z) for x in (((i*200)+50, (i*200)+250) for y in (0,1) for z in ((j*200)+50, (j*200)+250))]

		cube.addNodes(np.array(cube_nodes))
		cube.addEdges([(n, n + 4) for n in range(0, 4)])
		cube.addEdges([(n, n + 1) for n in range(0, 8, 2)])
		cube.addEdges([(n, n + 2) for n in (0, 1, 4, 5)])

		cubes.append(cube)

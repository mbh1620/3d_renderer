from wireframe import *
import pygame
import numpy as np

class ProjectionViewer:

	''' Displays 3D Objects on a Pygame Screen '''

	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.screen = pygame.display.set_mode((width, height))
		pygame.display.set_caption('Wireframe Display')
		self.background = (10,10,50)


		self.wireframes = {}
		self.displayNodes = True
		self.displayEdges = True
		self.nodeColour = (255,255,255)
		self.edgeColour = (200,200,200)
		self.nodeRadius = 4

	def run(self):

		key_to_function = {
		pygame.K_LEFT: (lambda x: x.translateAll([-10, 0, 0])),
 		pygame.K_RIGHT:(lambda x: x.translateAll([ 10, 0, 0])),
 		pygame.K_DOWN: (lambda x: x.translateAll([0,  10, 0])),
 		pygame.K_UP:   (lambda x: x.translateAll([0, -10, 0])),

 		# pygame.K_LEFT: (lambda x: x.moveCameraX(0,0.005)),
 		# pygame.K_RIGHT:(lambda x: x.moveCameraX(0,-0.005)),
 		# pygame.K_DOWN: (lambda x: x.moveCameraX(0.005,0)),
 		# pygame.K_UP:   (lambda x: x.moveCameraX(-0.005,0)),

 		pygame.K_a: (lambda x: x.rotate_about_Center('Y', -0.08)),
 		pygame.K_d: (lambda x: x.rotate_about_Center('Y', 0.08)),
 		pygame.K_w: (lambda x: x.rotate_about_Center('X', -0.08)),
 		pygame.K_s: (lambda x: x.rotate_about_Center('X', 0.08)),


		pygame.K_EQUALS: (lambda x: x.scale_centre([1.25,1.25,1.25])),
		pygame.K_MINUS: (lambda x: x.scale_centre([0.8,0.8,0.8])),

		pygame.K_q: (lambda x: x.rotateAll('X', 0.1)),
		#pygame.K_w: (lambda x: x.rotateAll('X', -0.1)),
		# pygame.K_a: (lambda x: x.rotateAll('Y', 0.1)),
		#pygame.K_s: (lambda x: x.rotateAll('Y', -0.1)),
		pygame.K_z: (lambda x: x.rotateAll('Z', 0.1)),
		pygame.K_x: (lambda x: x.rotateAll('Z', -0.1)),
		pygame.K_p: (lambda x: x.perspectiveMode()),
		pygame.K_t: (lambda x: x.translate_Camera())
		
		}


		running = True
		flag = False

		while running:

			keys = pygame.key.get_pressed()

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False

				
				
			if keys[pygame.K_LEFT]:
				key_to_function[pygame.K_LEFT](self)
			if keys[pygame.K_RIGHT]:
				key_to_function[pygame.K_RIGHT](self)
			if keys[pygame.K_DOWN]:
				key_to_function[pygame.K_DOWN](self)
			if keys[pygame.K_UP]:
				key_to_function[pygame.K_UP](self)
			if keys[pygame.K_EQUALS]:
				key_to_function[pygame.K_EQUALS](self)
			if keys[pygame.K_MINUS]:
				key_to_function[pygame.K_MINUS](self)
			if keys[pygame.K_LEFT]:
				key_to_function[pygame.K_LEFT](self)
			if keys[pygame.K_q]:
				key_to_function[pygame.K_q](self)
			if keys[pygame.K_w]:
				key_to_function[pygame.K_w](self)
			if keys[pygame.K_a]:
				key_to_function[pygame.K_a](self)
			if keys[pygame.K_s]:
				key_to_function[pygame.K_s](self)
			if keys[pygame.K_z]:
				key_to_function[pygame.K_z](self)
			if keys[pygame.K_x]:
				key_to_function[pygame.K_x](self)
			if keys[pygame.K_p]:
				key_to_function[pygame.K_p](self)
			if keys[pygame.K_t]:
				key_to_function[pygame.K_t](self)
			if keys[pygame.K_d]:
				key_to_function[pygame.K_d](self)

			self.display()
			pygame.display.flip()

	def addWireframe(self, name, wireframe):
		self.wireframes[name] = wireframe
		#translate to center
		wf = Wireframe()
		matrix = wf.translationMatrix(-self.width/2,-self.height/2,0)

		for wireframe in self.wireframes.values():
			wireframe.transform(matrix)

		

		wf = Wireframe()
		matrix = wf.translationMatrix(self.width,self.height,0)

		for wireframe in self.wireframes.values():
			wireframe.transform(matrix)


		

	def display(self):

		self.screen.fill(self.background)

		for wireframe in self.wireframes.values():
			wireframe.transform_for_perspective((self.width/2, self.height/2))	

			if self.displayNodes:
				for node in wireframe.perspective_nodes:

					pygame.draw.circle(self.screen, self.nodeColour, (int(node[0]), int(node[1])), self.nodeRadius, 0)

			if self.displayEdges:
				for n1, n2 in wireframe.edges:

					pygame.draw.aaline(self.screen, self.edgeColour, wireframe.perspective_nodes[n1][:2], wireframe.perspective_nodes[n2][:2], 1)



	def translateAll(self, vector):
		''' Translate all wireframes along a given axis by d units '''
		wf = Wireframe()
		matrix = wf.translationMatrix(*vector)
		for wireframe in self.wireframes.values():
			wireframe.transform(matrix)

	def scaleAll(self, vector):
		wf = Wireframe()
		matrix = wf.scaleMatrix(*vector)

		for wireframe in self.wireframes.values():
			wireframe.transform(matrix)

	def rotateAll(self, axis, theta):

		wf = Wireframe()
		if axis == 'X':
			matrix = wf.rotateXMatrix(theta)
		elif axis == 'Y':
			matrix = wf.rotateYMatrix(theta)
		elif axis == 'Z':
			matrix = wf.rotateZMatrix(theta)

		for wireframe in self.wireframes.values():
			wireframe.transform(matrix)
			#wireframe.transform_for_perspective()

	def moveCameraX(self,x,y):

		wf = Wireframe()

		matrix = wf.movCamera(x,y)
		print("test")

		for wireframe in self.wireframes.values():
			wireframe.transform(matrix)

	def moveCameraZ(self,x,y):

		wf = Wireframe()

		matrix = wf.testMat((0,0,val))

		for wireframe in self.wireframes.values():
			wireframe.transform(matrix)

	def perspectiveMode(self):

		#First translate the centre of screen to 0,0

		wf = Wireframe()
		matrix = wf.translationMatrix(-self.width/2,-self.height/2,0)

		for wireframe in self.wireframes.values():
			wireframe.transform(matrix)

		#perform the perspectivecorrection

		wf = Wireframe()
		matrix = wf.translationMatrix(-self.width/2,-self.height/2,0)

		for wireframe in self.wireframes.values():
			matrix = wf.perspectiveCorrection(1.2)
			wireframe.transform(matrix)

		wf = Wireframe()
		matrix = wf.translationMatrix(self.width/2,self.height/2,0)

		for wireframe in self.wireframes.values():
			wireframe.transform(matrix)


	def rotate_about_Center(self, Axis, theta):

		#First translate Centre of screen to 0,0

		wf = Wireframe()
		matrix = wf.translationMatrix(-self.width/2,-self.height/2,0)

		for wireframe in self.wireframes.values():
			wireframe.transform(matrix)

		#Do Rotation
		wf = Wireframe()
		if Axis == 'X':
			matrix = wf.rotateXMatrix(theta)
		elif Axis == 'Y':
			matrix = wf.rotateYMatrix(theta)
		elif Axis == 'Z':
			matrix = wf.rotateZMatrix(theta)

		for wireframe in self.wireframes.values():
			wireframe.transform(matrix)
			

		
		

		#Translate back to centre of screen

		wf = Wireframe()
		matrix = wf.translationMatrix(self.width/2,self.height/2,0)

		for wireframe in self.wireframes.values():
			wireframe.transform(matrix)



		

		#Do perspective if needed

	def scale_centre(self, vector):

		#Transform center of screen to origin

		wf = Wireframe()
		matrix = wf.translationMatrix(-self.width/2,-self.height/2,0)

		for wireframe in self.wireframes.values():
			wireframe.transform(matrix)

		#Scale the origin by vector

		wf = Wireframe()
		matrix = wf.scaleMatrix(*vector)

		for wireframe in self.wireframes.values():
			wireframe.transform(matrix)

		wf = Wireframe()
		matrix = wf.translationMatrix(self.width/2,self.height/2,0)

		for wireframe in self.wireframes.values():
			wireframe.transform(matrix)



	def add_perspective(self):

		for wireframe in self.wireframes.values():
			for node in wireframe.nodes:
				if node[2] != 0:


					print("Point ----------")
					print("x node", node[0])
					print("y node", node[1])
					print("z node", node[2])

					node[0] = node[0] + (10/node[2])
					node[1] = node[1] + (10/node[2])

					









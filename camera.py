
'''
Camera class

position
FOV
zoom 

'''


class Camera:

	def __init__(self, pos, fov=250, zoom=500):
		self.pos = pos
		self.fov = fov
		self.zoom = self.pos[2]
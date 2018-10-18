import readproducts as rp
import sys

class node:
	def __init__(self,x,y, nodeId):
		self.x = x
		self.y = y
		self.id = nodeId
		self.neigh = []
		self.distance = sys.maxsize #set a huge number to the distances
		self.visited = False


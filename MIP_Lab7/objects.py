import math
from numpy import random
import numpy as np

class Location():
	coords = np.array([0,0,0]) # x,y,z
	def __init__(self,x,y,z):
		self.coords[0] = x
		self.coords[1] = y
		self.coords[2] = z
		
	def add(self,loc):
		self.add(loc)

	def add(self,x,y,z):
		self.coords[0] += x
		self.coords[1] += y
		self.coords[2] += z

	def set(self,x,y,z):
		self.coords[0] = x
		self.coords[1] = y
		self.coords[2] = z

	def distance(self, loc):
		dx = self.coords[0] - loc.coords[0];
		dy = self.coords[1] - loc.coords[1];
		dz = self.coords[2] - loc.coords[2];
		return math.sqrt(dx*dx + dy*dy + dz*dz)

	def __repr__(self)->str:
		return f"x={self.coords[0]},y={self.coords[1]},z={self.coords[2]}"

class Player():
	PLAYER_COUNT = 0
	_id = 0
	name = "player"
	loc = Location(0,0,0) # Location
	ticks = 0

	def __init__(self, name, loc):
		self._id = ++Player.PLAYER_COUNT
		self.name = name
		self.loc = loc
		print(f"Created {self.name} {self.loc}")

	def tick(self):
		++self.ticks
		print(f"Ticked {self.name} {self.loc}")

	def move(self,x,y,z):
		self.loc.set(x,y,z)

	def __repr__(self)->str:
		return f"id={self._id},name={self.name}"

class World():
	players = np.array([Player]);
	ticks = 0

	def addPlayer(self,name):
		player = Player(name, random.randint(100), random.randint(100), random.randint(100))
		if self.players.__contains__(player):
			return
		np.append(self.players, player)

	def removePlayer(self,players):
		if self.players.__contains__(players) == False:
			return
		np.remove(self.players, players)

	def tick(self):
		self.ticks = self.ticks + 1
		print(f"Tick {self.ticks}")
		for player in self.players:
			player.tick()





import math
class Point(object):
# Type def of a point object
	def init(self, x, y):
		self.x = x
		self.y = y

	def fromData(self, data):
		split = data.split(',')
		self.x = int(split[0])
		self.y = int(split[1])
	
	def __repr__(self)->str:
		return f"{self.x},{self.y}"

	def distance(self, p):
		return math.sqrt(pow(self.x - p.x, 2) + pow(self.y - p.y, 2))

class Circle(Point):
# Type def of a circle object extending a point object

	def init(self, x, y, r):
		super().init(x,y)
		self.r = r;

	def fromData(self, data):
		split = data.split(',')
		self.x = int(split[0])
		self.y = int(split[1])
		self.r = float(split[2])

	def __repr__(self)->str:
		return f"{self.x},{self.y},{self.r}"

	def distance(self, c):
		d = math.sqrt(pow(self.x - c.x, 2) + pow(self.y - c.y, 2))
		if d < (self.r + c.r):
			return 0
		return d - self.r - c.r

	def area(self):
		return math.pi * self.r * self.r





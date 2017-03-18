import math
import graphics

class Polygon:
	def __init__(self, sides, angle, color, x_offset, y_offset, offset_rotation, length=69):
		self.sides = sides
		self.angle = (360/self.sides)			# creates an attribute representing the angle rotated between drawing sides
		self.color = color						# creates an attribute for the color of the polygon
		self.length = length					# creates an attribute for sidelength
		self.value = 0							# creates an attribute representing whether the polygon is dead or alive
		self.neighbors = 0						# creates an attribute representing how many neighbors the polygon has
		radian_offset_rotation = math.radians(offset_rotation)		# converts the offset rotation to radians
		x = x_offset	# dummy variables to help calculate the coordinates of the polygon relative to the unit cell
		y = y_offset	#
		x_offset = x * math.cos(radian_offset_rotation) + y * math.sin(radian_offset_rotation) 		    #
		y_offset = -1 * x * math.sin(radian_offset_rotation) + y * math.cos(radian_offset_rotation)		#
		self.x_offset = x_offset						# x offset relative to the unit cell
		self.y_offset = y_offset						# y offset relative to the unit cell
		self.life_threshold = .75*self.sides 			# sets a threshold for a new polygon being "born"
		self.lower_death_threshold = .25*self.sides		# sets a threshold past which the polygon will "die" due to underpopulation
		self.upper_death_threshold = self.sides 		# sets a threshold past which the polygon will "die" of overcrowding
		self.offset_rotation = offset_rotation

	def __repr__(self):
		return "<%d sides at x:%f, y:%f>" % (self.sides, self.x_offset, self.y_offset)


class Square(Polygon):
	def __init__(self, angle, x_offset, y_offset, offset_rotation):
		sides = 4
		color = "red"
		angle = 0
		super().__init__(sides, angle, color, x_offset, y_offset, offset_rotation)

class S1(Square):
	def __init__(self):
		super().__init__(0, 0, 0, -90)

class S2(Square):
	def __init__(self):
		super().__init__(0, 0, 1+ 3**.5 + .5, 60)

class S3(Square):
	def __init__(self):
		super().__init__(0, 0, 1+ 3**.5 + .5, 120)

class S4(Square):
	def __init__(self):
		super().__init__(0, 0, 1+ 3**.5 + .5, 180)

class S5(Square):
	def __init__(self):
		super().__init__(0, 0, 1+ 3**.5 + .5, 240)

class S6(Square):
	def __init__(self):
		super().__init__(0, 0, 1+ 3**.5 + .5, 300)

class Triangle(Polygon):
	def __init__(self, angle, x_offset, y_offset, offset_rotation):
		sides = 3
		color = "gold"
		angle=0
		super().__init__(sides, angle, color, x_offset, y_offset, offset_rotation)

class T1(Triangle):
	def __init__(self):
		super().__init__(0, 0,1 + (3 ** .5) + (3 ** .5) / 2, 0)

class T2(Triangle):
	def __init__(self):
		super().__init__(0, 0,1 + (3 ** .5) + (3 ** .5) / 2, 180)

class Hexagon(Polygon):
	def __init__(self, angle, x_offset, y_offset, offset_rotation):
		sides = 6
		color = "green"
		angle=0
		super().__init__(sides, angle, color, x_offset, y_offset, offset_rotation)

class H1(Hexagon):
	def __init__(self):
		super().__init__(0, 0,  1 + (3 ** .5) + (3 ** .5), 30)

class H2(Hexagon):
	def __init__(self):
		super().__init__(0, 0,  1 + (3 ** .5) + (3 ** .5), 150)

class H3(Hexagon):
	def __init__(self):
		super().__init__(0, 0,  1 + (3 ** .5) + (3 ** .5), 270)

class Dodecagon(Polygon):
	"""Note radius from center to edge is (1 + sqrt(3)) * length of side / sqrt(2)"""
	def __init__(self, angle, x_offset, y_offset, offset_rotation):
		sides = 12
		color = "blue"
		angle=0
		super().__init__(sides, angle, color, x_offset, y_offset, offset_rotation)

class UnitCell:
	def __init__(self, x,y):
		self.x = x
		self.y = y
		self.d1 = Dodecagon(0, 0, 0, 0)
		self.s1 = S1()
		self.s2 = S2()
		self.s3 = S3()
		self.s4 = S4()
		self.s5 = S5()
		self.s6 = S6()
		self.h1 = H1()
		self.h2 = H2()
		self.h3 = H3()
		self.t1 = T1()
		self.t2 = T2()

	def __repr__(self):
		return str(self.d1) + str(self.s2) + str(self.h3) + str(self.t2)

class UnitGrid:
	def __init__(self, height, width):
		self.height = height
		self.width = width
		self.grid = []
		for x in range(self.width):
			column = []
			for y in range(self.height):
				column.append(UnitCell(x,y))
			self.grid.append(column)


u = UnitGrid(1,1)
graphics.drawUnitGrid(u)
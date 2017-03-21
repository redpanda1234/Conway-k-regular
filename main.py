import math
import graphics
import random
import time

class Polygon:
    def __init__(self, sides, color, x_offset, y_offset, offset_rotation, length=50):
        self.sides = sides
        self.angle = (360/self.sides)           # creates an attribute representing the angle rotated between drawing sides
        self.color = color                      # creates an attribute for the color of the polygon
        self.length = length                    # creates an attribute for sidelength
        self.value = 0                          # creates an attribute representing whether the polygon is dead or alive
        self.neighbors = 0                      # creates an attribute representing how many neighbors the polygon has
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.x_offset = x_offset                        # x offset relative to the unit cell
        self.y_offset = y_offset                        # y offset relative to the unit cell
        self.life_threshold = .75*self.sides            # sets a threshold for a new polygon being "born"
        self.lower_death_threshold = .25*self.sides     # sets a threshold past which the polygon will "die" due to underpopulation
        self.upper_death_threshold = self.sides         # sets a threshold past which the polygon will "die" of overcrowding
        self.offset_rotation = offset_rotation

    def __repr__(self):
        return "<%d sides at x:%f, y:%f>" % (self.sides, self.x_offset, self.y_offset)

    def get_neighbor_cell(self, x,y):
        try:
            return u.grid[x][y]
        except IndexError:
            return UnitCell(0,0,0,0)

    def count_neighbors(self, cell, cell_x, cell_y): # Abstract Method
        pass

    def update(self, cell, cell_x, cell_y):
        neighbor_count = self.count_neighbors(cell, cell_x, cell_y)
        if self.value == 0:
            if neighbor_count >= self.life_threshold:
                self.value = 1
        else:
            if neighbor_count <= self.lower_death_threshold or neighbor_count >= self.upper_death_threshold:
                self.value = 0



class Square(Polygon):
    def __init__(self, x_offset, y_offset, offset_rotation):
        sides = 4
        color = "red"
        angle = 0
        super().__init__(sides, color, x_offset, y_offset, offset_rotation)

class S1(Square):
    def __init__(self):
        super().__init__(0, 0, -90)
    def count_neighbors(self, cell, cell_x, cell_y):
        count = 0
        count += cell.t1.value
        count += cell.h1.value
        count += self.get_neighbor_cell(cell_x - ((cell_y + 1) % 2), cell_y + 1).h3.value
        count += cell.d1.value
        return count

class S2(Square):
    def __init__(self):
        super().__init__(1 + math.sqrt(3), 0, 60)

    def count_neighbors(self, cell, cell_x, cell_y):
        count = 0
        count += cell.h1.value
        count += cell.h2.value
        count += cell.d1.value
        count += cell.t2.value
        return count

class S3(Square):
    def __init__(self):
        super().__init__(1.5+math.sqrt(3)/2,-1.5-math.sqrt(3)/2, 30)

    def count_neighbors(self, cell, cell_x, cell_y):
        count = 0
        count += cell.h2.value
        count += cell.h3.value
        count += self.get_neighbor_cell(cell_x + ((cell_y) % 2), cell_y - 1).t1.value
        count += cell.d1.value
        return count

class S4(Square):
    def __init__(self):
        super().__init__(0, -2-math.sqrt(3), 0)

    def count_neighbors(self, cell, cell_x, cell_y):
        count = 0
        count += cell.h3.value
        count += self.get_neighbor_cell(cell_x - ((cell_y + 1) % 2), cell_y - 1).t2.value
        count += self.get_neighbor_cell(cell_x - ((cell_y + 1) % 2), cell_y - 1).h1.value
        count += cell.d1.value
        return count

class S5(Square):
    def __init__(self):
        super().__init__(-math.sqrt(3)/2, -1.5-math.sqrt(3), 150)

    def count_neighbors(self, cell, cell_x, cell_y):
        count = 0
        count += self.get_neighbor_cell(cell_x - 1, cell_y).h2.value
        count += self.get_neighbor_cell(cell_x - ((cell_y + 1) % 2), cell_y - 1).t1.value
        count += self.get_neighbor_cell(cell_x - ((cell_y + 1) % 2), cell_y - 1).h1.value
        count += cell.d1.value
        return count    

class S6(Square):
    def __init__(self):
        super().__init__(-.5-math.sqrt(3)/2, -.5-math.sqrt(3)/2, 210)

    def count_neighbors(self, cell, cell_x, cell_y):
        count = 0
        count += self.get_neighbor_cell(cell_x - 1, cell_y).h2.value
        count += self.get_neighbor_cell(cell_x - 1, cell_y).t2.value
        count += self.get_neighbor_cell(cell_x - ((cell_y + 1) % 2), cell_y + 1).h3.value
        count += cell.d1.value
        return count

class Triangle(Polygon):
    def __init__(self, x_offset, y_offset, offset_rotation):
        sides = 3
        color = "gold"
        angle=0
        super().__init__(sides, color, x_offset, y_offset, offset_rotation)

class T1(Triangle):
    def __init__(self):
        super().__init__(0, 1, 300)

    def count_neighbors(self, cell, cell_x, cell_y):
        count = 0
        count += self.get_neighbor_cell(cell_x + (cell_y % 2), cell_y + 1).s5.value
        count += self.get_neighbor_cell(cell_x - ((cell_y + 1) % 2), cell_y + 1).s3.value
        count += cell.s1.value
        return count

class T2(Triangle):
    def __init__(self):
        super().__init__(1+math.sqrt(3), 0, 0)

    def count_neighbors(self, cell, cell_x, cell_y):
        count = 0
        count += self.get_neighbor_cell(cell_x + (cell_y % 2), cell_y + 1).s4.value
        count += self.get_neighbor_cell(cell_x + 1, cell_y).s6.value
        count += cell.s2.value
        return count

class Hexagon(Polygon):
    def __init__(self, x_offset, y_offset, offset_rotation):
        sides = 6
        color = "green"
        angle=0
        super().__init__(sides, color, x_offset, y_offset, offset_rotation)

class H1(Hexagon):
    def __init__(self):
        super().__init__(1+math.sqrt(3)/2,  1.5, 30)

    def count_neighbors(self, cell, cell_x, cell_y):
        count = 0
        count += self.get_neighbor_cell(cell_x + (cell_y % 2), cell_y + 1).s4.value
        count += self.get_neighbor_cell(cell_x + (cell_y % 2), cell_y + 1).s5.value
        count += self.get_neighbor_cell(cell_x + (cell_y % 2), cell_y + 1).d1.value
        count += cell.s1.value
        count += cell.s2.value
        count += cell.d1.value
        return count

class H2(Hexagon):
    def __init__(self):
        super().__init__(1.5 + math.sqrt(3),  -math.sqrt(3)/2, 30)

    def count_neighbors(self, cell, cell_x, cell_y):
        count = 0
        count += self.get_neighbor_cell(cell_x + 1, cell_y).s6.value
        count += self.get_neighbor_cell(cell_x + 1, cell_y).s5.value
        count += self.get_neighbor_cell(cell_x + 1, cell_y).d1.value
        count += cell.s2.value
        count += cell.s3.value
        count += cell.d1.value
        return count

class H3(Hexagon):
    def __init__(self):
        super().__init__(1+math.sqrt(3)/2,  -1.5-math.sqrt(3), 30)

    def count_neighbors(self, cell, cell_x, cell_y):
        count = 0
        count += self.get_neighbor_cell(cell_x + (cell_y % 2), cell_y - 1).s1.value
        count += self.get_neighbor_cell(cell_x + (cell_y % 2), cell_y - 1).s6.value
        count += self.get_neighbor_cell(cell_x + (cell_y % 2), cell_y - 1).d1.value
        count += cell.s3.value
        count += cell.s4.value
        count += cell.d1.value
        return count


class Dodecagon(Polygon):
    """Note radius from center to edge is (1 + sqrt(3)) * length of side / sqrt(2)"""
    def __init__(self, x_offset, y_offset, offset_rotation):
        sides = 12
        color = "blue"
        angle=0
        super().__init__(sides, color, x_offset, y_offset, offset_rotation)

    def count_neighbors(self, cell, cell_x, cell_y):
        count = 0
        count += cell.s1.value
        count += cell.s2.value
        count += cell.s3.value
        count += cell.s4.value
        count += cell.s5.value
        count += cell.s6.value
        count += cell.h1.value
        count += cell.h2.value
        count += cell.h3.value
        count += self.get_neighbor_cell(cell_x - ((cell_y + 1) % 2), cell_y - 1).h1.value
        count += self.get_neighbor_cell(cell_x - 1, cell_y).h2.value
        count += self.get_neighbor_cell(cell_x - ((cell_y + 1) % 2), cell_y + 1).h3.value
        return count

class UnitCell:
    def __init__(self, x,y, height, width):
        self.x = x
        self.y = y
        if y % 2 == 0:
            self.draw_x = x * (2 + 2 * (3**.5))
        else:
            self.draw_x = x * (2 + 2 * (3**.5)) + ((3**.5) + 1)
        self.draw_y = y * (3 + (3**.5))
        self.draw_x -= width * (2 + 2 * (3**.5))/2
        self.draw_y -= height * (3 + (3**.5))/2
        self.d1 = Dodecagon(0, 0, 0)
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

    def update_unit_cell(self):
        self.d1.update(self, self.x, self.y)
        self.s1.update(self, self.x, self.y)
        self.s2.update(self, self.x, self.y)
        self.s3.update(self, self.x, self.y)
        self.s4.update(self, self.x, self.y)
        self.s5.update(self, self.x, self.y)
        self.s6.update(self, self.x, self.y)
        self.t1.update(self, self.x, self.y)
        self.t2.update(self, self.x, self.y)
        self.h1.update(self, self.x, self.y)
        self.h2.update(self, self.x, self.y)
        self.h3.update(self, self.x, self.y)

    def pick_random(self):
        self.d1.value = random.choice([True,False])
        self.s1.value = random.choice([True,False])
        self.s2.value = random.choice([True,False])
        self.s3.value = random.choice([True,False])
        self.s4.value = random.choice([True,False])
        self.s5.value = random.choice([True,False])
        self.s6.value = random.choice([True,False])
        self.h1.value = random.choice([True,False])
        self.h2.value = random.choice([True,False])
        self.h3.value = random.choice([True,False])
        self.t1.value = random.choice([True,False])
        self.t2.value = random.choice([True,False])
            


class UnitGrid:
    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.grid = []
        for x in range(self.width):
            column = []
            for y in range(self.height):
                if y % 2 == 0:
                    column.append(UnitCell(x,y, self.height, self.width))
                else:
                    column.append(UnitCell(x,y, self.height, self.width))
            self.grid.append(column)

    def update_unit_grid(self):
        for x in range(self.width):
            for y in range(self.height):
                self.grid[x][y].update_unit_cell()

    def randomize_unit_grid(self):
        for x in range(self.width):
            for y in range(self.height):
                self.grid[x][y].pick_random()


u = UnitGrid(3,3)
u.randomize_unit_grid()
while True:
    u.update_unit_grid()
    graphics.drawUnitGrid(u)
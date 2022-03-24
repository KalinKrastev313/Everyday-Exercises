class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.initial_x = x
        self.initial_y = y

    def set_x(self, new_x):
        self.x = new_x

    def set_y(self, new_y):
        self.y = new_y

    def distance(self, coord_x, coord_y):
        if self.x and self.y > 0:
            return ((self.x - coord_x)**2 + (self.y - coord_y)**2)**(1/2)
        elif self.x < 0 < self.y:
            return ((self.x + coord_x) ** 2 + (self.y - coord_y) ** 2) ** (1 / 2)
        elif self.x > 0 > self.y:
            return ((self.x - coord_x) ** 2 + (self.y - coord_y) ** 2) ** (1 / 2)


p = Point(2, 4)
p.set_x(3)
p.set_y(5)
print(p.distance(10, 2))
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sum(self, p):
        return Vector(self.x + p.x, self.y + p.y)

    def print_point(self):
        print(f"X is {self.x} & Y is {self.y}")

    def __add__(self, p):
        return Vector(self.x + p.x, self.y + p.y)


p1 = Vector(6, 3)
p2 = Vector(8, 5)


# p = p1.sum(p2)   # Returns a new point which is a sum of new point
p = p1 + p2   # we overloaded the + function by writing __add__ function
p.print_point()

import math

class Shape():
    def __init__(self):
        area, perimeter = 0, 0

    def get_area():
        pass

    def get_perimeter():
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        self.area = math.pi * math.pow(self.radius, 2)
        return self.area

    def get_perimeter(self):
        self.perimeter = 2 * math.pi * self.radius
        return self.perimeter

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def get_area(self):
        self.area = self.side * self.side
        return self.area

    def get_perimeter(self):
        self.perimeter = math.pow(self.side, 2)
        return self.perimeter

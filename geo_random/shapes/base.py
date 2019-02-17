import math
from geo_random import exceptions

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def point_coordinates (self):
        point = [self.x, self.y]
        x = self.x
        y = self.y
        #print(f"point coordinate x({x})y({y})")
        return point

class Line():
    def __init__(self, point_1, point_2):
        self.point_1 = point_1
        self.point_2 = point_2
        self.x = str(point_1[0])
        self.y = str(point_1[1])
        self.x1 = str(point_2[0])
        self.y2 = str(point_2[1])

    #def printer (self):
        #result = (f"A x({self.x})y({self.y})  B x({self.x1}),y({self.y2})")
        #return print(result)

    def is_valid(self):
        """Метод 'is_valid' проверяет то что две заданные точки находяться в рвзных местах"""
        if self.point_1[0] == self.point_2[0] and self.point_1[1] == self.point_2[1]:
            print("Unf ortunately you put two or more points in one place, try again, do not make this error again")
        else:
            return Line(self.point_1, self.point_2).line_len()

    def line_len (self):
        line_len = math.sqrt((self.point_1[1] - self.point_2[1])**2 + (self.point_1[0] - self.point_2[0])**2)

        return line_len #print(f"A x ({x}) y ({y})  B ({x1}) y ({y2})")
# a = Point(3,4).point_coordinates()
# b = Point (5,6).point_coordinates()
# c = Line(a,b).is_valid()
# d = Line(a,b).printer()
# print(a)

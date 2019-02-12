import math
from geo_random import exceptions

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def point_coordinates (self):
        point = [self.x, self.y]
        #print(type(point))
        return point

class Line():
    def __init__(self, point_1, point_2):
        self.point_1 = point_1
        self.point_2 = point_2
        #print(point_1)
        #print(point_2)

    def is_valid(self):
        """Метод 'is_valid' проверяет то что две заданные точки находяться в рвзных местах"""
        if self.point_1[0] == self.point_2[0] and self.point_1[1] == self.point_2[1]:
            print("Unfortunately you put two or more points in one place, try again, do not make this error again")
        else:
            return Line(self.point_1, self.point_2).line_len()

    def line_len (self):
        line_len = math.sqrt((self.point_1[1] - self.point_2[1])**2 + (self.point_1[0] - self.point_2[0])**2)
        return line_len

# a = Point(3,4).point_coordinates()
# b = Point (5,6).point_coordinates()
# c = Line(a,b).is_valid()
# print(c)





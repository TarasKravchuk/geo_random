import math
from geo_random.shapes.base import *

class CircleShape ():
    def __init__(self, point_1_x, point_1_y, point_2_x, point_2_y):
        self.point_1_x = point_1_x
        self.point_1_y = point_1_y
        self.point_2_x = point_2_x
        self.point_2_y = point_2_y
        self.p1 = Point(point_1_x, point_1_y).point_coordinates()
        self.p2 = Point(point_2_x, point_2_y).point_coordinates()
        self.l1 = Line(self.p1, self.p2).is_valid()

    def is_valid(self):
        """Я добавил функцию 'is_valid' поскольку она есть в задании, условие валидности круга это - две точки находящиеся
        не в одном месте, наличие двух точек не в одном месте проверяет 'Line(self.p1, self.p2).is_valid()'"""
        CircleShape(self.point_1_x, self.point_1_y, self.point_2_x, self.point_2_y).get_square()

    def get_square(self):
        """Расчет площади круга по двум точкам - центр круга и точка на окружности"""
        circle_square = self.l1**2 * math.pi
        return print("Square of Circle with coordinates given by you  ==  ", circle_square)

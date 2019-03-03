import math
from geo_random.shapes.base import *

class TriangleShape():
    """Класс триугольник - принимает координаты 3-х вершин триугольника, провиряет возможность существования такого
    триугольника методом 'is_valid' и методом 'get_square' расчитывает площадь триугольника по формуле Герона"""
    def __init__(self, point_1_x, point_1_y, point_2_x, point_2_y, point_3_x, point_3_y):
        self.point_1_x = point_1_x
        self.point_1_y = point_1_y
        self.point_2_x = point_2_x
        self.point_2_y = point_2_y
        self.point_3_x = point_3_x
        self.point_3_y = point_3_y
        self.p1 = Point(point_1_x, point_1_y).point_coordinates()
        self.p2 = Point(point_2_x, point_2_y).point_coordinates()
        self.p3 = Point(point_3_x, point_3_y).point_coordinates()
        self.l1 = Line(self.p1, self.p2).is_valid()
        self.l2 = Line(self.p1, self.p3).is_valid()
        self.l3 = Line(self.p2, self.p3).is_valid()

    def is_valid(self):
        """Проверка валидности триугольника, триугольник можно начертить меж 3-мя точепми, при условии, что они не
        лежат на одной прямой. Функция 'is_valid' проверяет не лежат ли три вершины триугольника на одной линии
        по Х и по Y."""
        if self.p1[0] == self.p2[0] == self.p3[0] or self.p1[1] == self.p2[1] == self.p3[1]:
            print("unfortunately such a triangle cannot exist, try again")
            return False
        else:
            TriangleShape(self.point_1_x, self.point_1_y, self.point_2_x, self.point_2_y, self.point_3_x,
                          self.point_3_y).get_square()
            return True

    def get_square(self):
        """Расчет площади триугольника по формуле Герона"""
        p = (self.l1 + self.l2 + self.l3) / 2
        triangle_square = math.sqrt((p * (p - self.l1) * (p - self.l2) * (p - self.l3)))
        return triangle_square

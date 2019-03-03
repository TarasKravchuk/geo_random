import math
from geo_random.shapes.base import *

class SquareShape:
    def __init__(self,point_1_x, point_1_y, point_2_x, point_2_y, point_3_x, point_3_y, point_4_x, point_4_y):
        self.point_1_x = point_1_x
        self.point_1_y = point_1_y
        self.point_2_x = point_2_x
        self.point_2_y = point_2_y
        self.point_3_x = point_3_x
        self.point_3_y = point_3_y
        self.point_4_y = point_4_y
        self.point_4_x = point_4_x
        self.p1 = Point(self.point_1_x, self.point_1_y).point_coordinates()
        self.p2 = Point(self.point_2_x, self.point_2_y).point_coordinates()
        self.p3 = Point(self.point_3_x, self.point_3_y).point_coordinates()
        self.p4 = Point(self.point_4_x, self.point_4_y).point_coordinates()
        self.l1 = Line(self.p1, self.p2).is_valid()
        self.l2 = Line(self.p2, self.p3).is_valid()
        self.l3 = Line(self.p3, self.p4).is_valid()
        self.l4 = Line(self.p4, self.p1).is_valid()

    def is_valid(self):
        """В проверку валидности прямоугольника включено 2 провeрки:
        1 - противоположные стороны прямоугольника равны по длине
        2 - все четыре угла в прямоуолтнике == 90°"""
        if self.l1 == self.l3 and self.l4 == self.l2:
            if SquareShape(self.point_1_x, self.point_1_y, self.point_2_x, self.point_2_y,
            self.point_3_x, self.point_3_y, self.point_4_x, self.point_4_y).ninety_degree_angle() is True:
                return True

    def ninety_degree_angle (self):
        if (self.p1[0] * self.p2[0] + self.p1[1] * self.p2[1]) / (math.sqrt((self.p1[0])**2 + self.p1[1]**2) *
            math.sqrt((self.p2[0])**2 + self.p2[1]**2)) == 0 and (self.p2[0] * self.p3[0] + self.p2[1] * self.p3[1]) / (math.sqrt((self.p2[0]) ** 2 + self.p2[1] ** 2) *
            math.sqrt((self.p3[0]) ** 2 + self.p3[1] ** 2)) == 0 and (self.p3[0] * self.p4[0] + self.p3[1] * self.p4[1]) / (math.sqrt((self.p3[0])**2 + self.p4[1]**2) *
            math.sqrt((self.p4[0])**2 + self.p4[1]**2)) == 0 and (self.p4[0] * self.p1[0] + self.p4[1] * self.p1[1]) / (math.sqrt((self.p4[0])**2 + self.p4[1]**2) *
            math.sqrt((self.p1[0])**2 + self.p1[1]**2)) == 0:
            SquareShape(self.point_1_x, self.point_1_y, self.point_2_x, self.point_2_y,self.point_3_x, self.point_3_y,
                               self.point_4_x, self.point_4_y).get_square()
            return True

    def get_square(self):
        """Площадь прямоугольника равна произведению его сторон (: """
        square_square = self.l1 * self.l2
        return square_square

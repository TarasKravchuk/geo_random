#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import datetime
import random
from geo_random.shapes.circle import *
from geo_random.shapes.square import *
from geo_random.shapes.triangle import *
from geo_random.serializer import *
import time
from pprint import pprint

def convertation (elements):
    elements = str(elements)
    elements = elements.split(",")
    float_elements = [float(i) for i in elements]
    return float_elements

def convertation_random (elements):
    list_elements = ""
    dot = ","
    for i in elements:
        list_elements = list_elements + str(i) + dot
    list_elements = list_elements[:-1]
    elements = list_elements
    elements = str(elements)
    elements = elements.split(",")
    elements = list(elements)
    float_elements = [float(i) for i in elements]
    return float_elements

def triangle_runner (elements):
    if len(convertation(elements)) == 6:
        point_1_x = convertation(elements)[0]
        point_1_y = convertation(elements)[1]
        point_2_x = convertation(elements)[2]
        point_2_y = convertation(elements)[3]
        point_3_x = convertation(elements)[4]
        point_3_y = convertation(elements)[5]
        if TriangleShape(point_1_x, point_1_y, point_2_x, point_2_y, point_3_x, point_3_y).is_valid() is True:
            return True
    else: print("Тriangle should to contain 6 coordinates, 3 points with coordinates X and Y each.\n Please try again")

def circle_runner (elements):
    if len(convertation(elements)) == 4:
        point_1_x = convertation(elements)[0]
        point_1_y = convertation(elements)[1]
        point_2_x = convertation(elements)[2]
        point_2_y = convertation(elements)[3]
        if CircleShape(point_1_x, point_1_y, point_2_x, point_2_y).is_valid() is True:
            return True
    else:
        print("Circle should to contain 4 coordinates, 2 points with coordinates X and Y each.\n Please try again")

def square_runner (elements):
    if len(convertation(elements)) == 8:
        point_1_x = convertation(elements)[0]
        point_1_y = convertation(elements)[1]
        point_2_x = convertation(elements)[2]
        point_2_y = convertation(elements)[3]
        point_3_x = convertation(elements)[4]
        point_3_y = convertation(elements)[5]
        point_4_x = convertation(elements)[6]
        point_4_y = convertation(elements)[7]
        if SquareShape(point_1_x, point_1_y, point_2_x, point_2_y, point_3_x, point_3_y, point_4_x, point_4_y).is_valid() is True:
            return True
    else:
        print("Square should to contain 8 coordinates, 4 points with coordinates X and Y each.\n Please try again")

def random_triangle_runner (elements, triangles_result, result_list):
    if len(elements) == 6:
        point_1_x = elements[0]
        point_1_y = elements[1]
        point_2_x = elements[2]
        point_2_y = elements[3]
        point_3_x = elements[4]
        point_3_y = elements[5]
        tri_sq = TriangleShape(point_1_x, point_1_y, point_2_x, point_2_y, point_3_x, point_3_y)
        if tri_sq.is_valid() is True:
            triangles_result.append(tri_sq.get_square())
        else: triangles_result.append("incorrect triangle data")
        result_list.append(["triangles_result", triangles_result])
        return True
    else: print("Тriangle should to contain 6 coordinates, 3 points with coordinates X and Y each.\n Please try again")
    return False

def random_square_runner (elements,result_list, squares_result):
    if len(elements) == 8:
        point_1_x = elements[0]
        point_1_y = elements[1]
        point_2_x = elements[2]
        point_2_y = elements[3]
        point_3_x = elements[4]
        point_3_y = elements[5]
        point_4_x = elements[6]
        point_4_y = elements[7]
        sq_sq = SquareShape(point_1_x, point_1_y, point_2_x, point_2_y, point_3_x, point_3_y, point_4_x, point_4_y)
        if sq_sq.is_valid() is True:
            squares_result.append(sq_sq.get_square())
        else:squares_result.append("incorrect square data")
        result_list.append(["squares_result", squares_result])
        return True
    else: return False

def random_circle_runner (elements, result_list, circles_result):
    if len(elements) == 4:
        point_1_x = elements[0]
        point_1_y = elements[1]
        point_2_x = elements[2]
        point_2_y = elements[3]
        circ = CircleShape(point_1_x, point_1_y, point_2_x, point_2_y)
        if circ.is_valid() is True:
            circles_result.append(circ.get_square())
        else:circles_result.append("incorrect circle data")
        result_list.append(["circles_result", circles_result])
        return True
    else: print("Circle should to contain 4 random_coordinatescoordinates, 2 points with coordinates X and Y each.\n Please try again")
    return False

def generate_figures(elements):
    """Генератор заданного количества случайных фигур """
    result_list = []
    NUMBER_OF_SHAPES = elements.split(",")
    start_time = time.time()
    start_time_prt = datetime.datetime.now()
    result_list.append(["start_time", start_time_prt])
    triangles_result = []
    squares_result = []
    circles_result = []

    for i in NUMBER_OF_SHAPES:
        calc = 0
        quantity_triangle = 0
        quantity_square = 0
        quantity_circle = 0
        correct_triangle = 0
        correct_circle = 0
        correct_square = 0
        while int(i) > calc:
            random_figure = random.choice(["triangle", "square", "circle"])

            if random_figure == "triangle":
                quantity_triangle +=1
                random_coordinates = [x + random.random() + random.randint(-100, 100) for x in range(0, 6)]
                calc += 1
                if random_triangle_runner(random_coordinates, triangles_result, result_list) is True:
                    correct_triangle += 1
                result_list.append(["correct triangle", correct_triangle])
                result_list.append(["quantity_triangle", quantity_triangle])

            elif random_figure == "square":
                random_coordinates = [x + random.random() + random.randint(-100, 100) for x in range(0, 8)]
                calc += 1
                quantity_square += 1
                if random_square_runner(random_coordinates, result_list, squares_result) is True:
                    correct_square +=1
                result_list.append(["correct_square", correct_square])
                result_list.append(["quantity_square", quantity_square])

            elif random_figure == "circle":
                random_coordinates = [x + random.random() + random.randint(-100, 100) for x in range(0, 4)]
                calc += 1
                quantity_circle += 1
                if random_circle_runner(random_coordinates, result_list, circles_result) is True:
                    correct_circle +=1
                result_list.append(["correct_circle", correct_circle])
                result_list.append(["quantity_circle", quantity_circle])

        end_time = time.time()
        completion_time = end_time - start_time
        result_list.append(["completion_time", completion_time])
        end_time_prt = datetime.datetime.now()
        result_list.append(["end_time_prt", end_time_prt])
        total_figures = quantity_triangle + quantity_circle + quantity_square
        result_list.append(["total_figures", total_figures])
        try:
            percent_circle = 100*(correct_circle / quantity_circle)
        except ZeroDivisionError: percent_circle =0
        result_list.append(["percent_circle", percent_circle])
        try:
            percent_square = 100* (correct_square / quantity_square)
        except ZeroDivisionError: percent_square = 0
        result_list.append(["percent_square", percent_square])
        try:
            percent_triangle = 100*(correct_triangle / quantity_triangle)
        except ZeroDivisionError: percent_triangle = 0
        result_list.append(["percent_triangle", percent_triangle])

        result_dict = {k:v for k,v in result_list}
        pprint(result_dict)

        pickling(path, file_name, result_dict)

if __name__ == "__main__":
    """Запуск программы через консоль, используя sys.argv"""
    operation_name = sys.argv[1]
    elements = sys.argv[2]
    path = sys.argv[3]
    file_name = sys.argv[4]

    if operation_name.lower() == "triangle":
        triangle_runner(elements)

    elif operation_name.lower() == "random":
        generate_figures(elements)

    elif operation_name.lower() == "circle":
        circle_runner(elements)

    elif  operation_name.lower() == "square":
        square_runner(elements)

    else: print("This program accepts only the following commands: 'square' (8 elements)  'circle' (4 elements)"
                " 'triangle' (6 elements) and 'random' 1 element")

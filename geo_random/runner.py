#!/usr/bin/env python

import sys
sys.path.insert(0, '/home/taras/PycharmProjects/untitled15/geo_random_1')
import datetime
import random
from geo_random.shapes.circle import *
from geo_random.shapes.square import *
from geo_random.shapes.triangle import *
import time

def convertation (elements):
    elements = str(elements)
    elements = elements.split(",")
    elements = list(elements)
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
    if len(convertation(elements)) is 6:
        point_1_x = convertation(elements)[0]
        point_1_y = convertation(elements)[1]
        point_2_x = convertation(elements)[2]
        point_2_y = convertation(elements)[3]
        point_3_x = convertation(elements)[4]
        point_3_y = convertation(elements)[5]
        TriangleShape(point_1_x, point_1_y, point_2_x, point_2_y, point_3_x, point_3_y).is_valid()
    else: print("Тriangle should to contain 6 coordinates, 3 points with coordinates X and Y each.\n Please try again")

def circle_runner (elements):
    if len(convertation(elements)) is 4:
        point_1_x = convertation(elements)[0]
        point_1_y = convertation(elements)[1]
        point_2_x = convertation(elements)[2]
        point_2_y = convertation(elements)[3]
        CircleShape(point_1_x, point_1_y, point_2_x, point_2_y).is_valid()
    else:
        print("Circle should to contain 4 coordinates, 2 points with coordinates X and Y each.\n Please try again")

def square_runner (elements):
    print("Important! The order of specifying points in a rectangle must be specified by clockwise, otherwise the "
          "program may produce an error.")
    if len(convertation(elements)) is 8:
        point_1_x = convertation(elements)[0]
        point_1_y = convertation(elements)[1]
        point_2_x = convertation(elements)[2]
        point_2_y = convertation(elements)[3]
        point_3_x = convertation(elements)[4]
        point_3_y = convertation(elements)[5]
        point_4_x = convertation(elements)[6]
        point_4_y = convertation(elements)[7]
        SquareShape(point_1_x, point_1_y, point_2_x, point_2_y, point_3_x, point_3_y, point_4_x, point_4_y).is_valid()
    else:
        print("Square should to contain 8 coordinates, 4 points with coordinates X and Y each.\n Please try again")

def random_triangle_runner (elements):
    if len(elements) is 6:
        point_1_x = elements[0]
        point_1_y = elements[1]
        point_2_x = elements[2]
        point_2_y = elements[3]
        point_3_x = elements[4]
        point_3_y = elements[5]
        #TriangleShape(point_1_x, point_1_y, point_2_x, point_2_y, point_3_x, point_3_y).is_valid()
        if TriangleShape(point_1_x, point_1_y, point_2_x, point_2_y, point_3_x, point_3_y).is_valid() is True:
            return True
    else: print("Тriangle should to contain 6 coordinates, 3 points with coordinates X and Y each.\n Please try again")
    return False

def random_square_runner (elements):
    if len(elements) is 8:
        point_1_x = elements[0]
        point_1_y = elements[1]
        point_2_x = elements[2]
        point_2_y = elements[3]
        point_3_x = elements[4]
        point_3_y = elements[5]
        point_4_x = elements[6]
        point_4_y = elements[7]
        if SquareShape(point_1_x, point_1_y, point_2_x, point_2_y, point_3_x, point_3_y, point_4_x, point_4_y).is_valid() is True:
            return True
    else: print("Square should to contain 8 coordinates, 4 points with coordinates X and Y each.\n Please try again")
    return False

def random_circle_runner (elements):
    if len(elements) is 4:
        point_1_x = elements[0]
        point_1_y = elements[1]
        point_2_x = elements[2]
        point_2_y = elements[3]
        if CircleShape(point_1_x, point_1_y, point_2_x, point_2_y).is_valid() is True:
            return True
    else: print("Circle should to contain 4 random_coordinatescoordinates, 2 points with coordinates X and Y each.\n Please try again")
    return False

"""Генератор заданного количества случайных фигур """
def generate_figures(elements):
    NUMBER_OF_SHAPES = list(elements.split(","))
    start_time  = time.time()
    start_time_prt = datetime.datetime.now()
    calc = 0; quantity_triangle = 0; quantity_square = 0; quantity_circle = 0; correct_triangle = 0; correct_circle =0; correct_square =0

    for i in NUMBER_OF_SHAPES:
        while int(i) > calc:
            random_figure = random.choice(["triangle", "circle", "square"])
            if random_figure is "triangle":
                random_coordinates = [x + random.random() + random.randint(-100, 100) for x in range(0, 6)]
                calc += 1
                quantity_triangle += 1
                if random_triangle_runner(random_coordinates) is True:
                    correct_triangle += 1

            elif random_figure is "square":
                random_coordinates = [x + random.random() + random.randint(-100, 100) for x in range(0, 8)]
                calc += 1
                quantity_square += 1
                if random_square_runner(random_coordinates) is True:
                    correct_square +=1

            elif random_figure is "circle":
                random_coordinates = [x + random.random() + random.randint(-100, 100) for x in range(0, 4)]
                calc += 1
                quantity_circle += 1
                if random_circle_runner(random_coordinates) is True:
                    correct_circle +=1
            else:
                print("Houston, we have a problem")

        end_time = time.time()
        completion_time = end_time - start_time
        end_time_prt = datetime.datetime.now()
        total_figures = quantity_triangle + quantity_circle +quantity_square
        try:
            percent_circle = 100*(correct_circle / quantity_circle)
        except ZeroDivisionError: percent_circle =0
        try:
            percent_square = 100* (correct_square / quantity_square)
        except ZeroDivisionError: percent_square = 0
        try:
            percent_triangle = 100*(correct_triangle / quantity_triangle)
        except ZeroDivisionError: percent_triangle = 0
        print(f"Program execution statistics: \nTotal figures = {total_figures} \nTotal triangles == {quantity_triangle}"
              f" Correct triangles == {correct_triangle} % of correct triangles == {percent_triangle}"
              f"\nTotal circles == {quantity_circle} Correct circles == {correct_circle} % of correct circles == {percent_circle} "
              f"\nTotal squares == {quantity_square} Correct squares == {correct_square} % of correct squares == {percent_square}"
              f"\nStart of execution == {start_time_prt} \nEnd of execution == {end_time_prt}\nEexecution time == {completion_time} sec")


"""Запуск программы через консоль"""
if __name__ == "__main__":
    operation_name = sys.argv[1]; elements = sys.argv[2]

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

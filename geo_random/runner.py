#!/usr/bin/env python
import sys
import random
sys.path.insert(0, '/home/taras/PycharmProjects/untitled15')
from geo_random.shapes.circle import *
from geo_random.shapes.square import *
from geo_random.shapes.triangle import *


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
        TriangleShape(point_1_x, point_1_y, point_2_x, point_2_y, point_3_x, point_3_y).is_valid()
    else: print("Тriangle should to contain 6 coordinates, 3 points with coordinates X and Y each.\n Please try again")

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
        SquareShape(point_1_x, point_1_y, point_2_x, point_2_y, point_3_x, point_3_y, point_4_x, point_4_y).is_valid()
    else: print("Square should to contain 8 coordinates, 4 points with coordinates X and Y each.\n Please try again")

def random_circle_runner (elements):
    if len(elements) is 4:
        point_1_x = elements[0]
        point_1_y = elements[1]
        point_2_x = elements[2]
        point_2_y = elements[3]
        CircleShape(point_1_x, point_1_y, point_2_x, point_2_y).is_valid()
    else: print("Circle should to contain 4 coordinates, 2 points with coordinates X and Y each.\n Please try again")

if __name__ == "__main__":
    operation_name = sys.argv[1]; elements = sys.argv[2]

    if operation_name.lower() == "triangle":
        triangle_runner(elements)

    elif operation_name.lower() == "random":
        calc = 0
        while int(elements) > calc:
            random_figure = random.randint(1, 3)
            if random_figure is 1:
                random_coordinates = [x + random.randint(-100, 100) for x in range(0, 6)]
                #print ("Sides of your random triangle are 1-st ==" )
                random_triangle_runner(random_coordinates)
                calc +=1
            elif random_figure is 2:
                random_coordinates = [x + random.randint(-100, 100) for x in range(0, 8)]
                random_square_runner(random_coordinates)
                calc += 1
            elif random_figure is 3:
                random_coordinates = [x + random.randint(-100, 100) for x in range(0, 4)]
                random_circle_runner(random_coordinates)
                calc += 1
            else: print("Houston, we have a problem")

    elif operation_name.lower() == "circle":
        circle_runner(elements)

    elif  operation_name.lower() == "square":
        square_runner(elements)

    else: print("This program accepts only the following commands: 'square' (8 elements)  'circle' (4 elements)"
                " 'triangle' (6 elements) and 'random' 1 element")

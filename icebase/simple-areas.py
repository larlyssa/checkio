"""
You should write a function to calculate the area of simple figures: circles, rectangles and triangles. You are give an arbitrary number of arguments and depending on this, the function calculates area for the different figures.
One argument -- The diameter of a circle and you need calculate the area of the circle.
Two arguments -- The side lengths of a rectangle and you need calculate the area of the rectangle.
Three arguments -- The lengths of each side on a triangle and you need calculate the area of the triangle.

Input: One, two or three arguments as floats or as integers.
Output: The area of the circle, the rectangle or the triangle as a float.
Precondition:
0 < len(args) ≤ 3
all(0 < x ≤ 1000 for x in args)
For "triangle" cases the sum of the lengths of any two sides always exceeds the length of the third side.
"""

import math
def simple_areas(*args):
    if len(args) == 1:
        return ((args[0] / 2) ** 2) * math.pi
    elif len(args) == 2:
        return args[0] * args[1]
    elif len(args) == 3:
        perimeter = (args[0] + args[1] + args[2]) / 2
        return math.sqrt(perimeter * (perimeter - args[0]) * (perimeter - args[1]) * (perimeter - args[2]))

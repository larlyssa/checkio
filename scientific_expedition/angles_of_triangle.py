"""

DIFFICULTY: ELEMENTARY

You are given the lengths for each side on a triangle. You need to find all three angles for this triangle. If the given side lengths cannot form a triangle (or form a degenerated triangle), then you must return all angles as 0 (zero). The angles should be represented as a list of integers in ascending order. Each angle is measured in degrees and rounded to the nearest integer number (Standard mathematical rounding).
triangle-angles
Input: The lengths of the sides of a triangle as integers.
Output: Angles of a triangle in degrees as sorted list of integers.
Precondition: 
0 < a,b,c ≤ 1000
"""
import math

def checkio(a, b, c):
    angles = []

    if (a + b) <= c or (b + c) <= a or (a + c) <= b:
        angles = [0, 0, 0]
    
    else:
        angle_A = math.degrees(math.acos(((b ** 2) + (c ** 2) - (a ** 2)) / (2 * b * c)))
        angle_B = math.degrees(math.acos(((a ** 2) + (c ** 2) - (b ** 2)) / (2 * a * c)))
        angle_C = 180 - angle_A - angle_B
        
        angles = [round(angle_A), round(angle_B), round(angle_C)]
        angles.sort()
    
    return angles

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"

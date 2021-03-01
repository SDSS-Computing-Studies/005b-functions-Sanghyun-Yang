#!python3

"""
Create a function called distance()
Input is 2 tuples, that each contain an (x,y) coordinate.
Return value is the distance between the (x,y) coordinates.
Note that the coordinates should be signed (positive or negative) floats
(2 points)
"""
import math

def distance(a, b):
    side1 = a[0] - b[0]
    side2 = a[1] - b[1]
    answer = math.sqrt(( side1 ** 2 + side2 ** 2))
    return answer
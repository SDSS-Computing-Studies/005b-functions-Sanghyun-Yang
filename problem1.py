#!python3
""" 
Create a function called hypotenuse()
Input is 2 float numbers and a boolean
If the boolean is True, then find the hypotenuse
If the boolean is False, then the larger number is the hypotenuse
Return the missing side
(2 points)
"""
def hypotenuse(a, b, c):
    if c == True:
        formula = ( a ** 2 + b ** 2 ) ** (0.5)
    elif c == False:
        if a > b:
            formula = (a ** 2 - b ** 2) ** (1/2)
        elif b > a:
            formula = (b ** 2 - a ** 2) ** (1/2)
    if formula % 1 == 0:
        formula = int(formula)
    return formula
     

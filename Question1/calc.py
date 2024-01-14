# Import math Library required for finding the log10
import math


# function for factorial of a number
def factorial(number):
    factorial = 1
    if number < 0:
        return -1
    elif number == 0:
        return 0
    else:
        for i in range(1, number + 1):
            factorial = factorial * i

    return factorial


# function for finding log10 of a given number
def logFunction(number):
    return math.log10(number)


# function to convert degrees to radians
def degreeToRadians(number):
    return math.radians(number)


# function to find sine, cosine and tangent of an angle
def calc_trig(number):
    sine = math.sin(math.radians(number))
    cos = math.cos(math.radians(number))
    tan = math.tan(math.radians(number))

    return [sine, cos, tan]

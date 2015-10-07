"""
    Assignment: Spirograph
    Author: Ari Sanders
    Date: 09/08/2014
"""

from turtle import *
import math

def inRange(min, max):
    """
        If used, this function would prompt for a number,
        until one within range is given,
        at which point the input would be returned to the user.
        min = minimum bound of range
        max = maximum bound of range
    """
    emet = False
    while not emet:#emet is Hebrew for true
        out = int(input("Input a value between " +
                        str(min) + " and " + str(max) + ":"))
        if out >= min and out <= max:
            emet = True
    return out

def computeX(R, r, t, p):
    """
        Computes the value of the point's x coordinate based on the formula
        R = Radius of fixed circle
        r = Radius of moving circle
        t = Iteration between 0 and 2Pi
        p = Pen offset
    """
    return (R - r) * math.cos(t) - (r + p) * math.cos((R - r) / r * t)

def computeY(R, r, t, p):
    """
        Computes the value of the point's y coordinate based on the formula
        R = Radius of fixed circle
        r = Radius of moving circle
        t = Iteration between 0 and 2Pi
        p = Pen offset
    """
    return (R - r) * math.sin(t) - (r + p) * math.sin((R - r) / r * t)

def colorize(x, y):
    """
        Calculates the appropriate RGB color values for color mode 255
            based on the location of the turtle
        x = x coordinate
        y = y coordinate
    """
    x = (x * 2 if x > 0 else abs(x))
    y = (y * 2 if y > 0 else abs(y))

    z = 1.0 - x - y
    Y = 1.0
    X = (Y / y) * x
    Z = (Y / y) * z

    r = X * 1.612 - Y * 0.203 - Z * 0.302
    g = -X * 0.509 + Y * 1.412 + Z * 0.066
    b = X * 0.026 - Y * 0.072 + Z * 0.962
    r = abs(r)
    g = abs(g)
    b = abs(b)
    r = int(255 * (r if r < 1.0 else 1.0 / r))
    g = int(255 * (g if g < 1.0 else 1.0 / g))
    b = int(255 * (b if b < 1.0 else 1.0 / b))

    return (r, g, b)

def main():
    """
        Main program
    """
    #p = inRange(10, 100)
    p = input("Input a value between 10 and 100: ")
    if p.isnumeric():
        p = int(p)
    else:
        p = 0
    if p < 10 or p > 100:
        print("Incorrect value for p!")
        return

    mode("logo")
    shape("turtle")
    color("Blue")
    speed(0)
    colormode(255)

    R = 100
    r = 4
    t = 2 * math.pi

    pu()
    goto(computeX(R, r, 0, p), computeY(R, r, 0, p))
    pd()

    while t >= 0:
        x = computeX(R, r, t, p)
        y = computeY(R, r, t, p)
        pencolor(colorize(x, y))
        goto(x, y)
        t -= 0.01

    pu()
    goto(0, 0)
    ht()

    input("Hit enter to close...")
    bye()

main()

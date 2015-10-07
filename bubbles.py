"""
    Author: Ari Sanders
    Assignment: Bubble maker
    Date: 9/12/14
"""

from turtle import *
import math, random

def randColor():
    """
        Returns tuple for random color
        Pre-Conditions:
            colormode = 1.0
    """
    return (random.random(), random.random(), random.random())

"""
    What follows are poor imitations of constants in the form of functions
    Constants are inherently non-Pythonic
"""

def MAX_BUBBLES():
    """Returns the maximum value for the number of bubbles"""
    return 500

def BOUNDING_BOX():
    """Returns the value of the side length for the bounding box"""
    return 200

def MAX_DISTANCE():
    """Returns the maximum value for the distance between bubbles"""
    return 20

def MAX_RADIUS():
    """Returns the maximum value for the radius of each bubble"""
    return 20

def MAX_ANGLE():
    """Returns the maximum value for the angle turned after each bubble"""
    return 30

def fr():
    """fd() with a randomized input"""
    fd(random.randint(1,MAX_DISTANCE()))

def cir():
    """Creates a circle with random fill"""
    color(randColor())
    begin_fill()
    r = random.randint(1, MAX_RADIUS())
    circle(r)
    end_fill()
    return r

def lr(r):
    """
        Rotates the next bubble a random amount within bounds
        Bounces off box
    """
    x, y = position()
    if x + r * 2 > BOUNDING_BOX():
        seth(270)
    elif x - r * 2 < -BOUNDING_BOX():
        seth(90)
    elif y + r * 2 > BOUNDING_BOX():
        seth(180)
    elif y - r * 2 < -BOUNDING_BOX():
        seth(0)
    else:
        lt(random.randint(-MAX_ANGLE(), MAX_ANGLE()))

def recursive(n):
    """
        Recursively generates the bubble chain.
        Post-Conditions:
            Turtle is at random location within box
    """
    pd()
    if n <= 0:
        return 0
    else:
        r = cir()
        pu()
        fr()
        lr(r)
        return abs(r) + abs(recursive(n - 1))

def iterative(n):
    """
        Iteratively generates the bubble chain.
        Post-Conditions:
            Turtle is at random location within box
    """
    s = 0
    while n > 0:
        pd()
        r = cir()
        pu()
        fr()
        lr(r)
        s += abs(r)
        n -= 1
    return s

def initialize():
    """
        Sets up turtle and draws boundary box
        Pre-conditions:
            Turtle is at center of bounding box
        Post-Conditions:
            Mode is logo
            Speed is 0
            Turtle is invisible
    """
    mode("logo")
    speed(0)
    ht()
    pu()
    fd(BOUNDING_BOX())
    pd()
    lt(90)
    fd(BOUNDING_BOX())
    lt(90)
    fd(BOUNDING_BOX() * 2)
    lt(90)
    fd(BOUNDING_BOX() * 2)
    lt(90)
    fd(BOUNDING_BOX() * 2)
    lt(90)
    fd(BOUNDING_BOX())
    pu()
    rt(90)
    bk(BOUNDING_BOX())

def main():
    """Runs main program"""
    random.random()
    n = input("How many bubbles?: ")
    if n.isnumeric():
        n = int(n)
    else:
        print("Input must be numeric.")
        return False
    if n < 0 or n > MAX_BUBBLES():
        print("Bubbles must be between 0 and " + str(MAX_BUBBLES()) + " inclusive.")
        return False

    initialize()
    print("Sum of the radii: " + str(recursive(n)))
    input("Hit enter to continue")

    reset()
    initialize()
    print("Sum of the radii: " + str(iterative(n)))
    input("Hit enter to close...")
    bye()

main()

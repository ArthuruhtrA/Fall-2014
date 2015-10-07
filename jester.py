"""
    Author: Ari Sanders
    Assignment: Recursively draw boxes with circles on the last ones
    Date: 09/05/2014
"""

from turtle import *

def recolor(depth):
    """
        Determines and implements proper pen color
        Pre-conditions:
            All turtle functions have been imported
        Post-conditions:
            IF depth % 2 == 1: Pen color is blue
            ELSE: Pen color is red
    """
    pencolor("blue") if depth % 2 == 1 else pencolor("red")
    #Conditional Expression, known in other languages as a Ternary Operator

def jester(depth, size):
    """
        Recursively draw the shapes specified in the lab
        Pre-conditions:
        All turtle functions have been imported
            Turtle has been moved to starting position AND
            Pen is down AND
            IF depth % 2 == 0: turtle is facing north
            ELSEIF depth % 2 == 1:
                IF this is first recursive call: turtle is facing northeast
                ELIF this is second recursive call: turtle is facing northwest
        Post-conditions:
            Turtle is in original position AND
            Turtle is facing original direction AND
            Pen is still down AND
            IF depth % 2 == 1: Pen color is blue
            ELSE: Pen color is red
    """
    recolor(depth)
    if depth > 1:
        #Pre-ultimate layers are squares
        rt(90)
        fd(size / 2)
        lt(90)
        fd(size)
        rt(45)
        jester(depth - 1, size / 2)
        #At corner, go to next layer
        recolor(depth)
        lt(135)
        fd(size)
        rt(45)
        jester(depth - 1, size / 2)
        #At corner, go to next layer
        recolor(depth)
        lt(135)
        fd(size)
        lt(90)
        fd(size / 2)
        lt(90)
    elif depth == 1:
        #Ultimate layer is circles
        rt(90)
        circle(size / 2)
        lt(90)
    else:
        #Base case
        return

def main():
    """
        Set up, draw, and clean up
        Basically do everything
        Pre-conditions:
            All turtle functions have been imported
            Turtle is at 0,0 AND facing north OR
            This is the first call to turtle
        Post-conditions:
            Turtle has been exited
    """
    mode("logo")
    setup(600, 600)
    title("Jester")
    shape("turtle")
    color("blue")
    #speed(0)
    pu()
    depth = 1 + int(input("How deep should we go?"))
    size = 185 / (1 - (1 / 2 ** depth))
    #Calculate size to fit on screen at given depth
    fd(-(size - (size / 2 ** depth)))
    #Move starting position so drawing is roughly vertically centered
    pd()
    jester(depth, size)
    input("Press enter to close")
    bye()

main()

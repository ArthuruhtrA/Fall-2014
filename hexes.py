"""
   Author:
      Ari Sanders
   Assignment:
      Use Turtle library to draw a ring of hexagons in Python
   Date:
      08/24/2014
"""

import turtle
import math

def initialize():
    """Initialize the turtle so that it is facing North with the pen up."""
    turtle.mode("logo")
    turtle.pu()
    turtle.shape("turtle")

def drawSide():
    """
        Draw one side of the hexagon.
    """
    turtle.fd(100)
    turtle.rt(60)

def drawHex():
    """
        Draw a Hexagon.
    """
    turtle.pd()
    drawSide()#1
    drawSide()#2
    drawSide()#3
    drawSide()#4
    drawSide()#5
    drawSide()#6
    turtle.pu()

def move():
    turtle.rt(120)
    turtle.fd(100)
    turtle.lt(60)

def drawRing():
    """Draw a ring of hexagons."""
    turtle.pu()
    r = math.sqrt(7500)
    turtle.fd(r)
    turtle.lt(90)
    turtle.fd(50)
    turtle.rt(60)
    drawHex()
    move()
    drawHex()
    move()
    drawHex()
    move()
    drawHex()
    move()
    drawHex()
    move()
    drawHex()
    turtle.rt(180)
    turtle.fd(100)
    turtle.lt(90)

def main():
    """
        The program creates draws a ring of hexagons and
        waits for the user to respond before terminating.
    """
    initialize()
    drawRing()
    input("Hit ENTER to finish the program.")
    turtle.bye()

main()

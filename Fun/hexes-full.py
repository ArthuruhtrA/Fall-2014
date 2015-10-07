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

def drawSide(l):
    """
        Draw one side of the hexagon.
        l is side length
    """
    turtle.fd(l)
    turtle.rt(60)

def drawHex(x,y,l):
    """
        Draw a Hexagon.
        x,y are coordinates
        l is side length
    """

    turtle.pu()
    turtle.rt(90)
    turtle.fd(x)
    turtle.rt(90)
    turtle.fd(y)
    turtle.lt(90)
    turtle.pd()

    #Draw Hexagon
    drawSide(l)#1
    turtle.shape("classic")
    drawSide(l)#2
    turtle.shape("arrow")
    drawSide(l)#3
    turtle.shape("square")
    drawSide(l)#4
    turtle.shape("circle")
    drawSide(l)#5
    turtle.shape("triangle")
    drawSide(l)#6
    turtle.shape("turtle")

    #Return to Original Position
    turtle.pu()
    turtle.lt(90)
    turtle.fd(y)
    turtle.lt(90)
    turtle.fd(x)
    turtle.rt(90)

def pythagorean(a,c):
    """
        Calculate length of third side of triangle given a leg and the hypoteneuse
        a is leg length
        c is hypoteneuse length
    """
    return math.sqrt(c*c-a*a)

def drawRing(l):
    """Draw a ring of hexagons."""
    turtle.pu()
    turtle.fd(3*l)
    turtle.lt(90)
    turtle.fd(3*l)
    turtle.rt(90)
    r = pythagorean(l/2,l)
    drawHex(2*l,0,l)
    drawHex(3.5*l,r,l)
    drawHex(3.5*l,3*r,l)
    drawHex(2*l,4*r,l)
    drawHex(l/2,3*r,l)
    drawHex(l/2,r,l)

def main():
    """
        The program creates draws a ring of hexagons and
        waits for the user to respond before terminating.
    """
    initialize()
    drawRing(100)
    input("Hit ENTER to finish the program.")
    turtle.bye()

main()

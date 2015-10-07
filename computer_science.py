"""
    Author: Ari Sanders
    Assignment: Draw the words Computer Science using the basic Turtle functions in Python using my group's design conventions
    Date: 07/29/2014
"""

from turtle import *
import math

def initialize():
    """Initialize Turtle/Canvas"""
    mode("logo")
    shape("turtle")#Because it's far more appropriate
    screensize(2250)
    #Because my group had poor design conventions and the words don't fit on the default canvas with our starting point and letter widths.
    rt(90)#Yes, I'm using shorthand functions. Less typing.
    pu()

def c():
    """Draw the letter C"""
    pd()
    lt(180)
    fd(50)#1_
    rt(90)
    fd(25)#2|
    rt(90)
    fd(50)#3‾
    pu()
    rt(90)
    fd(25)#Move
    lt(90)
    fd(75)

def o():
    """Draw the letter O"""
    pd()
    lt(90)
    fd(25)#1|
    lt(90)
    fd(50)#2‾
    lt(90)
    fd(25)#3|
    lt(90)
    fd(50)#4_
    pu()
    fd(75)#Move

def m():
    """Draw the letter M"""
    pd()
    lt(90)
    fd(25)#1|
    lt(135)
    r = math.hypot(25,25)#Same as math.sqrt(25*25+25*25), but better.
    fd(r)#2/
    rt(90)
    fd(r)#3\
    lt(135)
    fd(25)#4|
    pu()
    lt(90)
    fd(125)#Move

def p():
    """Draw the letter P"""
    lt(180)
    fd(50)
    pd()
    rt(90)
    fd(25)#1|
    rt(90)
    fd(50)#2‾
    rt(90)
    fd(12.5)#3|
    rt(90)
    fd(50)#4-
    pu()
    lt(90)
    fd(12.5)
    lt(90)
    fd(125)#Move

def u():
    """Draw the letter U"""
    pd()
    lt(90)
    fd(25)#1|
    pu()
    lt(90)
    fd(50)
    pd()
    lt(90)
    fd(25)#2|
    lt(90)
    fd(50)#3_
    pu()
    fd(75)#Move

def t():
    """Draw the letter T"""
    lt(90)
    fd(25)
    pd()
    lt(90)
    fd(50)#1‾
    pu()
    rt(180)
    fd(25)
    pd()
    rt(90)
    fd(25)#2|
    pu()
    lt(90)
    fd(100)#Move

def e():
    """Draw the letter E"""
    pd()
    lt(180)
    fd(50)#1_
    rt(90)
    fd(25)#2|
    rt(90)
    fd(50)#3‾
    pu()
    rt(90)
    fd(12.5)
    pd()
    rt(90)
    fd(50)#4-
    pu()
    lt(90)
    fd(12.5)
    lt(90)
    fd(125)#Move

def r():
    """Draw the letter R"""
    pd()
    a = math.degrees(math.atan2(12.5,-50))
    #I know I shouldn't be doing stuff like ^this here, but if I did it on a calculator and plugged it in it would be inaccurate.
    lt(a)
    fd(math.hypot(12.5,50))#1\
    rt(a)
    fd(50)#2-
    lt(90)
    fd(12.5)#3|
    lt(90)
    fd(50)#4‾
    lt(90)
    fd(25)#5|
    pu()
    lt(90)
    fd(125)#Move

def space():
    """Draw a space"""
    fd(25)#Move

def newLine():
    """
        Draw a newline
        Not necessary with the initial resize of the canvas
    """
    lt(180)
    fd(600)
    lt(90)
    fd(50)
    lt(90)

def s():
    """Draw the letter S"""
    pd()
    lt(90)
    fd(12.5)#1|
    lt(90)
    fd(50)#2-
    rt(90)
    fd(12.5)#3|
    rt(90)
    fd(50)#4‾
    pu()
    rt(90)
    fd(25)
    pd()
    rt(90)
    fd(50)#5_
    pu()
    rt(180)
    fd(125)#Move

def i():
    """Draw the letter I"""
    pd()
    lt(180)
    fd(50)#1_
    pu()
    rt(90)
    fd(25)
    pd()
    rt(90)
    fd(50)#2‾
    pu()
    lt(180)
    fd(25)
    pd()
    lt(90)
    fd(25)#3|
    pu()
    lt(90)
    fd(100)#Move

def n():
    """Draw the letter N"""
    lt(90)
    fd(25)
    pd()
    rt(180)
    fd(25)#1|
    a = 90+math.degrees(math.atan2(25,-50))
    lt(a)
    fd(math.hypot(50,25))#2\
    rt(a)
    fd(25)#3|
    pu()
    lt(90)
    fd(125)#Move

def main():
    """Draw the phrase 'COMPUTER SCIENCE'"""
    initialize()
    c()
    o()
    m()
    p()
    u()
    t()
    e()
    r()
    space()#Replace this function with newLine() to better view the output
    s()
    c()
    i()
    e()
    n()
    c()
    e()
    input("Press ENTER to kill")
    bye()

main()

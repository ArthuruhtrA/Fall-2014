"""
    Draw a tree
"""

from turtle import *
import time

def initialize():
    title("Tree Grower")
    mode("logo")
    setworldcoordinates(-1000, 0, 1000, 2500)
    seth(90)
    shape("turtle")
    #ht()

def kill():
    pu()
    goto(0,-20)
    input("Press enter to kill.")
    bye()

def main():
    initialize()
    size = int(input("How big is the tree?"))
    pd()
    mult = 100
    if size == 0:
        circle(5)
    elif size == 1:
        fd(size * mult)
    else:
        fd(size * mult)
        left = [clone()]
        right = [clone()]
        for i in range(2, size + 1):
            """
                Use two turtles, split the turtles every iteration
            """
            if size > 2:
                right2 = []
                for l in range(len(left)):
                    right2.append(left[l].clone())
                    left[l].color("red")
                for r in range(len(right)):
                    left.append(right[r].clone())
                    right[r].color("blue")
                for t in range(len(right2)):
                    right.append(right2[t])
                    right2[t].color("green")
                del right2
            length = size * mult / i
            for l in range(len(left)):
                left[l].lt(60)
                left[l].fd(length)
                left[l].color("purple")
            for r in range(len(right)):
                right[l].rt(60)
                right[r].fd(length)
                right[r].color("brown")
    kill()

main()

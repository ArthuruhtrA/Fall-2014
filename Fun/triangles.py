from turtle import *
import math

def t(n, s):
    if n <= 0:
        return
    elif n == 1:
        pd()
        fd(s/2)
        lt(120)
        fd(s)
        lt(120)
        fd(s)
        lt(120)
        fd(s/2)
        pu()
    else:
        pd()
        fd(s/2)
        lt(120)
        fd(s)
        lt(120)
        fd(s)
        lt(120)
        fd(s/2)
        pu()
        fd(s/4)
        t(n - 1, s / 2)
        lt(180)
        fd(2 * s / 4)
        lt(180)
        t(n - 1, s / 2)
        fd(s / 4)
        lt(90)
        fd(math.sqrt(s / 2 * s / 2 - s / 4 * s / 4))
        rt(90)
        t(n - 1, s / 2)
        rt(90)
        fd(math.sqrt(s / 2 * s / 2 - s / 4 * s / 4))
        lt(90)

t(3, 100)
input("Press enter to exit")

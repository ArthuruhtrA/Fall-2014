"""
    Spiral
"""

from turtle import *

def maze(num):
    for i in range(num, 0, -1):
        fd(i)
        rt(90)

def main():
    mode("logo")
    shape("turtle")
    speed(0)
    pu()
    num = int(input("Input how many turns to make your maze:"))
    goto(-num / 2, -num / 2)
    pd()
    ht()
    maze(num)
    st()
    input("Press enter to kill.")
    bye()

main()

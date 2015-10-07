"""
    Name: letterHist
    Author: Ari Sanders
    Assignment: Unigram Project
    Date: 11/7/2014

    Draws histogram of relative letter frequencies using turtle
"""

from turtle import *
from string import ascii_uppercase

def gt(x, y=False):
    """
        goto() without drawing
        x = float, x coordinate to go to
        y = float, y coordinate to go to, defaults to False
    """
    pu()
    goto(x, y)
    pd()

def letterFreqPlot(freqList):
    """
        Plots a histogram of letter frequencies in turtle
        freqList = list, floats from 0.0 to 1.0 for each letter of the alphabet
        returns: None, draws histogram
        Note to coder: width is always 26 bars,
            height/scale depend on max value in list
            title, x-axis letter labels, y-axis frequency labels
    """
    """Set up turtle"""
    title("Histogram of Letter Frequencies")
    mode("logo")
    #speed(0)
    ht()
    bar_width = 15#How wide should each bar be?
    width = 26 * bar_width
    height = 250
    max_freq = max(freqList)
    unit_height = height / max_freq#Make sizes relative
    halfW = -(width / 2)
    halfH = -(height / 2)
    tenthH = int(height / 10)

    """Label axes"""
    """Y"""
    gt(halfW - 100)
    write("Frequency")
    gt(halfW - 30, halfH - 7)
    for i in range(0, height + tenthH, tenthH):
        write(str(i / unit_height)[:5])
        gt(xcor(), ycor() + tenthH)
    """X"""
    gt(0, halfH - 40)
    write("Letter")
    gt(halfW + (bar_width / 3), halfH - 15)
    for i in ascii_uppercase:
        write(i)
        gt(xcor() + bar_width, ycor())

    """Draw Border"""
    gt(halfW, -halfH)
    rt(180)
    fd(height)
    lt(90)
    fd(width)
    gt(halfW, halfH)
    
    """Iterate through alphabet, draw bars as rectangles with fill"""
    fillcolor("blue")
    for i in freqList:
        if i > 0:
            bar_height = unit_height * i
            begin_fill()
            fd(bar_width)
            lt(90)
            fd(bar_height)
            lt(90)
            fd(bar_width)
            lt(90)
            fd(bar_height)
            end_fill()
            lt(90)
        pu()
        fd(bar_width)
        pd()
    input("Press enter to exit.")

def main():
    """Main function of the program"""
    pass

if __name__ == "__main__":
        main()

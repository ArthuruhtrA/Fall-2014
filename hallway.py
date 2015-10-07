"""
File: hallway.py

Draw shrinking squares with multiple recursion.
This turtle program prompts for the recursion depth and draws the
depth number of concentric squares, connected at the corners.

language: python3
author: bks@cs.rit.edu, ben k steele
author: rwd@cs.rit.edu, Rob Duncan
author: axs3546@rit.edu, Ari Sanders
"""

# # imports

import math
import turtle


# # function definitions

def initWorld( depth, size ):
    """
    initWorld : Number -> None
    initWorld initializes the drawing canvas, pen and drawing state.
    depth -- depth of recursion to be drawn
    size -- size of the figure to be drawn (centered)
    pre-conditions: not applicable.
    post-conditions: turtle is at origin, pen up, facing North.
                     The world coordinates are size X size with
                     the origin at the bottom middle of the canvas.
    """
    # dimension is the extent of width and height of the coordinate system

    dimension = 2 * size ## ( depth + 1 ) * size
    max = dimension / 2
    turtle.setworldcoordinates( -max-1, -1, max, dimension )
    turtle.up()        # pen
    if depth > 0:
        turtle.left( 180 )
        turtle.forward( max )
        turtle.write( "depth:" + str(depth), False, font=("Helvetica", 18, "bold") )
        turtle.home()
    turtle.left( 90 )  # North

def drawSquare( size, hall ):
    """
    drawSquare : Number -> None
    drawSquare draws a square, clockwise.
    size -- length of a side of the square
    hall -- setting hall = 1 will cause the "hall" lines to write
    pre-conditions: turtle is pen up, facing North, in some start location.
    post-conditions: turtle is pen up, facing North, in same, start location.
    """
    turtle.pendown()
    turtle.right( 90 )
    turtle.forward( size / 2 )
    turtle.left( 90 )
    hallSegment( hall )
    turtle.forward( size )
    turtle.left( 90 )
    hallSegment( hall )
    turtle.forward( size )
    turtle.left( 90 )
    hallSegment( hall )
    turtle.forward( size )
    turtle.left( 90 )
    hallSegment( hall )
    turtle.forward( size / 2)
    turtle.left( 90 )
    turtle.penup()

def hallSegment( hall ):
    """
    hallSegment : Number -> None
    hallSegment draws the segment to connect two concentric square corners
    hall -- value of 1 causes the segment to be drawn
    pre-conditions: turtle is pen down, pointing in some direction, at some location
    post-conditions: turtle is pen down, pointing in the same direction, same location
    """
    if hall != 1:
        return
    else:
        turtle.left( 45 )
        distance = math.sqrt( 2 )
        turtle.forward( distance )
        turtle.forward( -distance )
        turtle.right( 45 )

def drawShrinkingSquares( depth, size, hall ):
    """
    drawShrinkingSquares : Number Number -> None
    drawShrinkingSquares draws a series shrinking squares recursively.
    depth -- depth of recursion
    size -- length of a side of the square
    hall -- setting hall = 1 will cause the "hall" lines to write
    pre-conditions: turtle pen up, facing North, in some start location.
    post-conditions: turtle pen up, facing North, in same, start location.
    """
    if depth <= 0:
        return
    elif depth == 1:
        drawSquare( size, 0 )
    else:
        drawSquare( size, hall )
        turtle.forward( 1 )
        drawShrinkingSquares( depth - 1, size - 2, hall)
        turtle.forward( -1 )

# # script execution/run

def makePicture():
    """
    makePicture : None -> None
    makePicture prompts for recursion depth.
    Next makePicture sets up the canvas window and draws shrinking squares.
    Finally makePicture waits for the user to click in the window
    to end the program.
    pre-conditions: program has an input capability.
    post-conditions: canvas window is closed.
    """
    depth = int( input( "enter depth: " ) )
    if depth < 1:
        depth = 1
    size = 3 * depth
    initWorld( depth, size )
    drawShrinkingSquares( depth, size, 1 )
    turtle.home()
    turtle.left( 90 )

    #pause when finished for input
    input("Hit enter to close...")
    turtle.bye()

if __name__ == "__main__":
    makePicture()

# # # # # # #
# $Id$
# Revision History:
# $Log$
#

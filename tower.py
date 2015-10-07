#2^n - 1
"""
    Author: Ari Sanders
    Assignment: Solve Tower of Hanoi
    Date: 10/15/2014
"""

from tower_animate import *
from myStack import *

def moveDisk(fromPile, toPile, list):
    """
        Moves a disk from one pile to another
        Pre-conditions: fromPile contains at least one ring
        Post-conditions: one ring has been moved from fromPile to toPile
        fromPile: stack to move from
        toPile: stack to move to
        list: list of stacks
    """
    list[toPile] = push(list[toPile], top(list[fromPile]))
    list[fromPile] = pop(list[fromPile])
    animate_move(list, fromPile, toPile)

#Alternate which stack we send to: using fromPile and toPile
def solve(disks, list, fromPile, toPile):
    """
        Solves the puzzle
        Pre-conditions:
            On first run: list contains three elements, a stack of rings disks to 1, and two Nones
            On consecutive runs: there are rings on at least one stack
        Post-conditions: all rings have been moved from first pile to third
        disks: total number of disks
        list: list containing the three stacks
        fromPile: pile to move from
        toPile: pile to move to
    """
    if disks == 0:
        return 0
    other = 3 - fromPile - toPile
    total = solve(disks - 1, list, fromPile, other)
    moveDisk(fromPile, toPile, list)
    total += solve(disks - 1, list, other, toPile) + 1
    return total

def main():
    """
        Main function, does everything
        Pre-conditions: none
        Post-conditions: shit's been done
    """
    disks = int(input("How high a tower to start with: "))
    list = [None, None, None]
    for i in range(disks, 0, -1):
        list[0] = push(list[0], i)
    animate_init(disks)
    moves = solve(disks, list, 0, 2)
    print("The tower of Hanoi puzzle with", disks, "disks", end='')
    print(" is solved in", moves, "moves")
    input("Press enter to quit")
    animate_finish()

main()

"""
    Author: Ari Sanders
    Assignment: States
    Date: 11/01/2014
"""

from rit_object import *
import random

class State(rit_object):
    __slots__ = ("name", "max")
    _types = (str, int)

def findState(states, number):
    """
        Determines which state the ID is in
        states = list of max IDs for each state
        number = which ID to check
    """
    for state in states:
        if state.max > number:
            return state.name

def test(states, total):
    """
        Runs one test of how many people it takes
            to have two people in the same room from the same state
        states = list of max IDs for each state
        total = total number of people
    """
    #Keep running until there are two of the same state or 50
    sample = set()
    for i in range(1, 51):
        number = random.randint(1, total)
        state = findState(states, number)
        if state in sample:
            return i
        else:
            sample.add(state)
    return 51

def main():
    """
        Main code
    """
        total = 0
        states = []
        for line in open(input("Where is your states file?: ")):
            line = line.strip().split()
            line[1] = int(line[1])
            states.append(State(line[0], total + line[1]))
            total += line[1]
        tests = int(input("How many tests should we run? (1-1000): "))
        if tests < 1 or tests > 1000:
            raise IndexError("Incorrect value for tests")
        sum = 0
        for i in range(1, tests):
            sum += test(states, total)
        print("The average is", sum / tests)

main()

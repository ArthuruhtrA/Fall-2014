"""
    Author: Ari Sanders
    Assignment: AirExpress
    Date: 10/28/2014
"""

from testPriorityQueue import *

def main():
    queue = createPriorityQueue()
    file = open(input("What is the name of the simulation file: "))
    for line in file:
        line = line.split()
        if line[0] == "checkin":
            print("Checking in", line[1], "for seat", line[2])
            insert(queue, Passenger(line[1], int(line[2])))
        else:
            line[1] = int(line[1])
            print("Boarding seats down to", line[1])
            while line[1] <= front(queue).priority:
                passenger = remove(queue).data
                print("Boarding", passenger.name, "for seat", passenger.priority)

main()

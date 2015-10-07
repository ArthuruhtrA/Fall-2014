"""
    Author: Ari Sanders
    Assignment: Bieber Hash
    Date: 11/11/2014
"""

from hashtable import *

def create_bills(file, size):
    """
        Creates hashtable, reads file, then tracks total bill for each person
        file = str, file to parse
        size = int, how many seats at the concert
        returns: prints name, seat, and total bill for each person in file
            OR exits if person isn't seated
    """
    hTable = createHashTable(capacity=size)
    for line in open(file):
        line = line.strip().split(" $")
        if has(hTable, line[0]):
            hTable.table[indexOf(hTable, line[0])].value += int(line[1])
        else:
            put(hTable, line[0], int(line[1]))
    for key in keys(hTable):
        print(key, indexOf(hTable, key), get(hTable, key))

def main():
    size = int(input("How big should the hashtable be?: "))
    file = input("Where is the file to read from?: ")
    create_bills(file, size)

main()

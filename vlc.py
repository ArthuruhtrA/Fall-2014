"""
    Author: Ari Sanders
    Assignment: VLC
    Date: 11/25/2014
"""

from rit_object import *
from array_heap import *
from math import *

class Symbol(rit_object):
    __slots__ = ("name", "freq", "code")
    _types = (str, int, str)

class Node(rit_object):
    __slots__ = ("total", "objects")
    _types = (int, list)

def compareFunc(node1, node2):
    """
        Compares two nodes
        node1 = first node to compare
        node2 = other node to compare
        Returns whether or not the second node is bigger
    """
    return node1.total < node2.total

def main():
    """
        Reads file into dictionary
        Converts it to a heap
        Generates codewords
        Prints them, along with average variable and fixed code lengths
    """
    """Read file and turn it into a dictionary"""
    dict = {}
    for line in open(input("Where is the symbol file?: ")):
        line = line.strip()
        for char in line:
            if char in dict:
                dict[char] += 1
            else:
                dict[char] = 1

    """Turn dictionary into heap of Symbols"""
    max = len(dict)
    heap = createEmptyHeap(max, compareFunc)
    for symbol in dict:
        add(heap, Node(dict[symbol], [Symbol(symbol, dict[symbol], "")]))
    
    """Create codewords"""
    while heap.size > 1:
        one = removeMin(heap)
        for symbol in one.objects:
            symbol.code = "0" + symbol.code
        two = removeMin(heap)
        for symbol in two.objects:
            symbol.code = "1" + symbol.code
        add(heap, Node(one.total + two.total, one.objects + two.objects))

    """Print results"""
    total = 0
    for symbol in heap.array[0].objects:
        print("Symbol: %2s " % symbol.name, end="")
        print("Codeword: %8s " % symbol.code, end="")
        print("Frequency: %5d" % symbol.freq)
        total += len(symbol.code) * symbol.freq#Keep track of total bits

    print("Average VLC codeword length: ", total / heap.array[0].total,
          "bits per symbol")
    print("Average fixed-length codeword length: ", ceil(log(max)),
          "bits per symbol")

main()

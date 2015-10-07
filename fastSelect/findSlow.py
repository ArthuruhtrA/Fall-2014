"""
    Author: Ari Sanders
    Assignment: Sorting Lab
    Date: 10/3/14
    Sort written by the people in the next comment block:
"""
import time

"""
Demonstrate sorting a list of unsorted data
using the insertion sort algorithm.
Problem: Insertion Sort
Author: Sean Strout (sps@cs.rit.edu)
Contributor: ben k steele bk
Contributor: Arthur Nunes-Harwitt anh
"""

def swap( lst, i, j ):
    """
    swap: List NatNum NatNum -> None
    swap the contents of list at pos i and j.
    Parameters:
        lst - the list of data
        i   - index of one datum
        j   - index of the other datum
    """
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp

def insert( lst, mark ):
    """
    insert: List(Orderable) NatNum -> None
    Move the value at index mark+1 so that it is in its proper place.
    Parameters:
        lst - the list of data
        mark - represents cutting the list between
               index mark and index mark+1
    pre-conditions:
      lst[0:mark+1] is sorted.
    post-conditions:
      lst[0:mark+2] is sorted.
    """
    index = mark
    while index > -1 and lst[index] > lst[index+1]:
        swap( lst, index, index+1 )
        index = index - 1

def insertion_sort( lst ):
    """
    insertion_sort : List(Orderable) -> None
    Perform an in-place insertion sort on a list of orderable data.
    Parameters:
        lst - the list of data to sort
    post-conditions:
        The data list has been sorted.
    """
    for mark in range( len( lst ) - 1 ):
        insert( lst, mark )

def fileToList(file):
    file = open(file)
    list = []
    for line in file:
        line = line.split()
        list.append(int(line[1]))
    return list

def median(list):
    length = len(list)
    if length % 2 == 1:
        return list[length // 2 + 1]
    else:
        return (list[length // 2] + list[length // 2 + 1]) / 2

def main():
    list = fileToList("testDataSet10k.txt")
    time1 = time.clock()
    insertion_sort(list)
    med = median(list)
    time1 = time.clock() - time1
    print("The median is: " + str(med))
    print("The total time was: " + str(time1))
main()

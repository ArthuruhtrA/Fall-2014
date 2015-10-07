"""
file: heapSort.py
version: python3
author: Sean Strout
author: Ari Sanders
purpose: Implementation of the heapsort algorithm, not
    in-place, (lst is unmodified and a new sorted one is returned)
"""

from heapq import *    # mkHeap (for adding/removing from heap)
import testSorts    # run (for individual test run)

def heapSort(lst):
    """
    heapSort(List(Orderable)) -> List(Ordered)
        performs a heapsort on 'lst' returning a new sorted list
    Postcondition: the argument lst is not modified
    """
    heap = []
    for i in lst:
        heappush(heap, i)# use heapPush to push the item onto heap
    output = []
    while heap != []:
        output.insert(0, heappop(heap))# use heapPop to pop the items off one by one into a new list (which is sorted)
    return output

if __name__ == "__main__":
    testSorts.run('heapSort')

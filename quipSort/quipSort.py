"""
file: quipSort.py
version: python3
author: Sean Strout
author: Ari Sanders
purpose: Implementation of the quicheSort algorithm (not in place),
    It first uses quickSort, using the median-of-3 pivot, until it
    reaches a recursion limit bounded by int(math.log(N,2)).
    Here, N is the length of the initial list to sort.
    Once it reaches that depth limit, it switches to using heapSort instead of
    quicksort.
"""

import heapSort             # heapSort
from math import log2                 # log2 (for quicksort depth limit)
import testSorts            # run (for individual test run)
from statistics import median

def quipSortRec(lst, limit):
    """
    A non in-place, depth limited quickSort, using median-of-3 pivot.
    Once the limit drops to 0, it uses heapSort instead.
    """
    if len(lst) == 1 or lst == []:
        return lst
    if limit <= 0:
        return heapSort.heapSort(lst)
    pivot = [median([lst[0], lst[len(lst) // 2], lst[len(lst) - 1]])]
    lst2 = []
    lst3 = []
    for i in lst:
        if i < pivot[0]:
            lst2.append(i)
        elif i > pivot[0]:
            lst3.append(i)
        else:
            pivot.append(i)
    return quipSortRec(lst2, limit - 1) + pivot + quipSortRec(lst3, limit - 1)

def quipSort(lst):
    """
    The main routine called to do the sort.  It should call the
    recursive routine with the correct values in order to perform
    the sort
    """
    quipSortRec(lst, log2(len(lst)))

if __name__ == "__main__":
    testSorts.run('quipSort')

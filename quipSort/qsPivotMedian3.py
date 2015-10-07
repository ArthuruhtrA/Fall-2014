"""
file: qsPivotMedian3.py
version: python3
author: Sean Strout
author: Ari Sanders
purpose: Implementation of the quick-sort algorithm (not in-place).  The 
    pivot is chosen always to be the median-of-3 (the median of
    the first, middle and last values)
"""

import testSorts        # run (for individual test run)
from statistics import median

def medianOf3(lst):
    """
    From a lst of unordered data, find and return the the median value from
    the first, middle and last values.
    """
    return median([lst[0], lst[len(lst) // 2], lst[len(lst) - 1]])
    
def quickSort(lst):
    """
    quickSort: List(lst) -> List(result)
        Where the return 'result' is a totally ordered 'lst'.
        It uses the median-of-3 to select the pivot

    e.g.  quickSort([1,8,5,3,4]) == [1,3,4,5,8]
    """
    if len(lst) == 1 or lst == []:
        return lst
    pivot = [medianOf3(lst)]
    lst2 = []
    lst3 = []
    for i in lst:
        if i < pivot[0]:
            lst2.append(i)
        elif i > pivot[0]:
            lst3.append(i)
        else:
            pivot.append(i)
    return quickSort(lst2) + pivot + quickSort(lst3)
   
if __name__ == "__main__":
    testSorts.run('qsPivotMedian3')

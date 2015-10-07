"""
    Author: Ari Sanders
    Assignment: Sorting Lab
    Date: 10/3/14
"""
import time

def fastSelect(list, k):
    while list != []:
        pivot = list[len(list) // 2]
        smaller = []
        larger = []
        count = 0
        for i in list:
            if i < pivot:
                smaller.append(i)
            elif i == pivot:
                count += 1
            elif i > pivot:
                larger.append(i)
            else:
                print("Something went wrong. It should be impossible to get here.")
        m = len(smaller)
        if k >= m and k < m + count:
            return pivot
        if m > k:
            list = smaller
        else:
            k = k - m - count
            list = larger

def fileToList(file):
    file = open(file)
    list = []
    for line in file:
        line = line.split()
        list.append(int(line[1]))
    return list

def main():
    list = fileToList("testDataSet10k.txt")
    time1 = time.clock()
    length = len(list)
    if length % 2 == 1:
        median = fastSelect(list, length // 2)
    else:
        med1 = fastSelect(list, length // 2)
        med2 = fastSelect(list, (length // 2) + 1)
        med = (med1 + med2) / 2
    time1 = time.clock() - time1
    print("The median is: " + str(med))
    print("The total time was: " + str(time1))

main()

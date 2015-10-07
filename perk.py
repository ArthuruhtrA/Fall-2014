"""
    Author: Ari Sanders
    Assignment: Perk Sort
    Date: 10/04/14
"""

def fileToList(file):
    """
        Converts a file to a list
        Returns a list in the format of one line per element
        file = Location of file to open
    """
    handle = open(file)
    list = []
    for l in handle:
        list.append(int(l.strip()))
    return list

def perkSort(list):
    """
        Perculatively sorts through a list
        Assumes list contains only numeric variable types
        Returns sorted list from least to greatest
        list = List to sort
    """
    sorted = False
    while sorted == False:
        for i in range(0, len(list) - 1):
            t1 = 0
            t2 = 0#Temporary variables for pre-swap storage
            if list[i] > list[i + 1]:
                t1 = list[i]
                t2 = list[i + 1]
                list[i] = t2
                list[i + 1] = t1
                true = True
        if true == False:
            sorted = True
        else:
            true = False
    return list

def main():
    """
        Takes a file from user input
        Converts it to a list
        Outputs the list
        Sorts it
        Outputs the sorted list
    """
    list = fileToList(input("Type the name of a file to sort: "))
    print(list)
    print(perkSort(list))

main()

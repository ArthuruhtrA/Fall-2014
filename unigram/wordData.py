"""
    Name: wordData
    Author: Ari Sanders
    Assignment: Unigram Project
    Date: 11/7/2014

    Utility program
"""

from rit_object import *

class YearCount(rit_object):
    """Appearances per year"""
    __slots__ = ("count", "year")
    _types = (int, int)

class WordCount(rit_object):
    """Appearances per word"""
    __slots__ = ("word", "count")
    _types = (str, int)

def readWordFile(filename):
    """
        Reads word data files
        filename = string, name of data file
        returns: dict, maps words to lists of YearCounts
    """
    dict = {}
    with open("data/" + filename) as file:
        for line in file:
            line = line.strip().split(", ")
            if line[0] in dict:
                dict[line[0]].append(YearCount(int(line[2]), int(line[1])))
            else:
                dict[line[0]] = [YearCount(int(line[2]), int(line[1]))]
    return dict

def totalOccurrences(word, words):
    """
        Counts how many total occurences of word are in the data
        word = str, word to count occurences of
        words = dict, all data (from readWordFile())
    """
    count = 0
    for yearCount in words[word]:
        count += yearCount.count
    return count


def main():
    """Test function"""
    words = readWordFile("very_short.csv")
    print(words)
    count = totalOccurrences("airport", words)
    print(count)
    print(count == 175702 + 173294)

if __name__ == "__main__":
        main()

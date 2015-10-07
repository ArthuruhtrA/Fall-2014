"""
    Name: wordFreq
    Author: Ari Sanders
    Assignment: Unigram Project
    Date: 11/7/2014

    Aggregate word counts and distribution of word frequencies
"""

from wordData import *
from simplePlot import wordFreqPlot
from heapq import heappop, heappush#Priority Queue via heap

def wordFrequencies(words):
    """
        Sorts words from most to least frequent
        words = dict, maps words to lists of YearCounts
        returns: list, sorted list of WordCounts
    """
    h = []
    for word in words:
        total = 0
        for yearCount in words[word]:
            total += yearCount.count#Sum count for all years
        heappush(h, (total, word))#Add word to heap using total count
    output = []
    while h != []:
        item = heappop(h)#Remove the least-frequent word
        output.insert(0, WordCount(item[1], item[0]))#Prepend it as a WordCount
    return output

def main():
    """Plots wordFrequencies"""
    freqs = wordFrequencies(
        readWordFile(input("Which file should we use?: ")))
    rank = int(input("Select a rank: "))
    print("Rank", str(rank), ": WordCount( word: ", freqs[rank - 1].word, ", count: ", int(freqs[rank - 1].count), ")")
    wordFreqPlot(freqs)

if __name__ == "__main__":
        main()

"""
    Name: letterFreq
    Author: Ari Sanders
    Assignment: Unigram Project
    Date: 11/7/2014

    Relative letter frequencies of words in the English language
"""

from wordData import *
from letterHist import *
from string import ascii_lowercase

def letterFreq(words):
    """
        Creates a list of letter frequencies
        words = dict, maps words to lists of YearCounts
        returns: list, letter frequencies
    """
    dict = {}
    total = 0
    for word in words:#Iterate through words
        for letter in word:#Increment by letter
            count = 0
            for yearCount in words[word]:
                count += yearCount.count#Increment total instances of word
            total += count#Count total letters
            if letter in dict:
                dict[letter] += count#Add to existing entry
            else:
                dict[letter] = count#Create new entry
    """CODE FOR THE WHOLE ALPHABET"""
    list = []
    for letter in ascii_lowercase:
        if letter in dict and dict[letter] != 0:
            list.append(dict[letter] / total)#Convert to relative
        else:
            list.append(0.0)#Fill alphabet
    return list

def main():
    """Draws histogram of letterFreq"""
    letterFreqPlot(letterFreq(
        readWordFile(input("Which file should we use?: "))))

if __name__ == "__main__":
        main()

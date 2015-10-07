"""
    Name: wordLength
    Author: Ari Sanders
    Assignment: Unigram Project
    Date: 11/7/2014

    Length of average written word throughout data set
"""

from wordData import *
from simplePlot import averageWordLengthPlot

def occurrencesInYear(word, year, words):
    """
        Counts occurences of a given word in a given year
        word = str, word to count for
        year = int, year to count in
        words = dict, maps from words to lists of YearCounts
        returns: int, number of occurences of word in year
    """
    if word in words:
        for yearCount in words[word]:
            if yearCount.year == year:
                return yearCount.count
    return 0

def averageWordLength(year, words):
    """
        Counts average word length for a given year
        year = int, which year to count for
        words = dict, maps words to lists of YearCounts
        returns: float, average word length
        Note: based on previous function
    """
    totalWords = 0
    totalLetters = 0
    for word in words:
        value = occurrencesInYear(word, year, words)
        totalWords += value
        totalLetters += len(word) * value
    if totalWords == 0:
        return 0
    return totalLetters / totalWords

def averageWordLengthYears(startYear, endYear, words):
    """
        Creates list of averages for all years in range
        startYear = int, which year to start from
        endYear = int, which year to end with
        words = dict, maps words to lists of YearCounts
        returns: list, floats of all averages in range
        Note: startYear and endYear are inclusive
            based on previous function
    """
    list = []
    for year in range(startYear, endYear + 1):
        list.append(averageWordLength(year, words))
    return list

def main():
    """Draws average length of words in a span"""
    words = readWordFile(input("Which file should we use?: "))

    """occurrencesInYear"""
    word = input("Select a word: ")
    year = input("Select a year: ")
    print("The word '", word, "' appeared ", occurrencesInYear(word, int(year), words), "times in the year", year)

    """averageWordLength"""
    year = input("Select a year: ")
    print("The average word length for the year", year, "is", averageWordLength(int(year), words), "letters")

    """averageWordLengthYears"""
    start = int(input("Which year should we start with?: "))
    end = int(input("Which year should we end with?: "))
    averageWordLengthPlot(
        start, end, averageWordLengthYears(
            start, end, words))

if __name__ == "__main__":
        main()

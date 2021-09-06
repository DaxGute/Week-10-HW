"""
Description: For this lab, you will analyze data extracted from Rotten Tomatoes, 
a website that aggregates movie reviews from film critics. Your goal is to read
a file containing movie reviews and use sorting to determine which words are
most associated with positive reviews and which words are most associated with 
negative reviews.
Name: Daxton Gutekunst
Date: Sep. 5 2021
"""

import math


def binarySearch(x, L):
    """
    Purpose: This function searches through a sorted list using binary search and 
    finds the index where a value is located.
    Parameters: desired value, list to sift through
    Return Val: Returns the index where the desired value was found
    """
    low = 0
    high = len(L) - 1
    while True:
        mid = (high + low)//2
        listItem = L[mid]
        if x == listItem:
            return mid
        elif x > listItem:
            low = mid + 1
        elif x < listItem:
            high = mid - 1
        if low > high:
            return -1


def getStopWordsAsList(file):
    """
    Purpose: This function takes in a string that contains the name of a file. After parsing 
    that file, it puts each line into an array which it returns. This is used for stop words.
    Parameters: A string of the file name
    Return Val: Returns a list of lines for the file passed in
    """
    f = open(file, "r")
    listOfLines = []
    for x in f:
        listOfLines.append(x.lower().replace("\n","").replace("\t",""))

    return listOfLines


def proccessLinesAsListOfWords(file):
    """
    Purpose: This code is passed in a file name and searches the immediate folder
    for that file. When this file is found, it parses in its data line by line.
    Each line is separated by with its rating and blurb in two separate lists. Which
    are then returned in an encompassing list.
    Parameters: A string of the file name
    Return Val: A parrellel list of ratings and blurbs
    """
    f = open(file, "r")
    reviews = []
    reviews.append([]) #ratings
    reviews.append([]) #blurb
    for line in f:
        reviews[0].append(int(line[:1])-2)
        proccessedLine = line.lower().replace("\n","").replace("\t","")
        reviews[1].append(getWordsOfBlurb(proccessedLine))

    return reviews


def getWordsOfBlurb(blurbText):
    """
    Purpose: This method is passed in a blurb of the of a review. Using this blurb,
    it then splits up the blurb into the words and puts those split up words into an
    list in an overarching list that is passed out.
    Parameters: A list containing all the blurbs 
    Return Val: A list of lists containing the words of each blurb
    """ 
    bannedWords = getStopWordsAsList("stopWords.txt")
    words = []
    lastSpaceIndex = 0
    for i in range(len(blurbText)):
        if blurbText[i] == " ":
            word = blurbText[lastSpaceIndex:i]
            if binarySearch(word,bannedWords) == -1 and word.isalpha():
                words.append(word)
            lastSpaceIndex = i + 1

    return words


def getUniqueWordsRating(reviews): 
    """
    Purpose: This function tallys up the scores of all of the words. Words that appear
    more in more highly rated movies will correspondingly receive higher scores. It
    then outputs this list of scores as an unsorted list of words and their
    associated scores.
    Parameters: A parrellel list of reviews and blurbs 
    Return Val: A parrellel list of unique words and their ratings
    """
    listOfUniqueWords = getUniqueWords(reviews[1])
    sortedUniqueWords = wordSelectionSort(listOfUniqueWords)
    parrellelWordSum = []
    parrellelWordNum = []

    for i in range(len(sortedUniqueWords)):
        parrellelWordSum.append(0)
        parrellelWordNum.append(0)

    for i in range(len(reviews[0])):
        for word in reviews[1][i]:
            listIndex = binarySearch(word, sortedUniqueWords)
            parrellelWordSum[listIndex] += reviews[0][i]
            parrellelWordNum[listIndex] += 1

    wordRatings = [sortedUniqueWords,[]]
    for i in range(len(sortedUniqueWords)):
        wordRatings[1].append((parrellelWordSum[i]/parrellelWordNum[i])*math.log(parrellelWordNum[i]))

    return wordRatings


def getUniqueWords(blurbs):
    """
    Purpose: This function gets all the unique words in a list of blurbs. If a word is already
    in the list, it is skipped. However, if it is not already in the list, it is then added. 
    This list is then returned.
    Parameters: A list of blurbs 
    Return Val: A list of unique words
    """
    uniqueWords = []
    for blurb in blurbs:
        for word in blurb:
            if word not in uniqueWords: # TODO: ask if allowed to do?
                uniqueWords.append(word)
    return uniqueWords


def wordSelectionSort(uniqueWords):
    """
    Purpose: This function sorts a list of unique words alphbetically. This makes it so that 
    binary search can later be used on this list. This sorted list is automatically updated.
    Parameters: A list of unique words 
    Return Val: NA
    """
    for i in range(len(uniqueWords)):
        smallest = i
        for j in range(i, len(uniqueWords)):
            if (uniqueWords[j] < uniqueWords[smallest]):
                smallest = j
        uniqueWords[i], uniqueWords[smallest] = uniqueWords[smallest], uniqueWords[i]
        smallest = i


def rankWordSelectionSort(uniqueWords):
    """
    Purpose: This function sorts a parrellel list of unique words and their corresponding 
    ratings by their ratings from best to worst rating with bubble sort. This sorted list 
    is automatically updated.
    Parameters: Parrellel list of unique words and their corresponding ratings 
    Return Val: NA
    """
    for i in range(len(uniqueWords[1])):
        smallest = i
        for j in range(i, len(uniqueWords[1])):
            if (uniqueWords[1][j] < uniqueWords[1][smallest]):
                smallest = j
        uniqueWords[0][i], uniqueWords[0][smallest] = uniqueWords[0][smallest], uniqueWords[0][i]
        uniqueWords[1][i], uniqueWords[1][smallest] = uniqueWords[1][smallest], uniqueWords[1][i]
        smallest = i


def displayScores(uniqueWordsRatings):
    """
    Purpose: This function receives a list of words and their associated ratings.
    Using the built in sort method, the function sorts the list by the the value
    that is associated with the word. Words with the highest values are sent to the top.
    Words are then displayed by the top twenty and bottom twenty.
    Parameters: A parrellel list of the unique words and their ratings
    Return Val: NA
    """
    rankWordSelectionSort(uniqueWordsRatings)
    print("Top 20")
    for i in range(-1, -21, -1):
        print(f'{uniqueWordsRatings[1][i]:.2f} {uniqueWordsRatings[0][i]}')
    print("\nBottom 20")
    for i in range(21):
        print(f'{uniqueWordsRatings[1][i]:.2f} {uniqueWordsRatings[0][i]}')


def main():
    reviews = proccessLinesAsListOfWords("movieReviews.txt")
    uniqueWordsRatings = getUniqueWordsRating(reviews)
    displayScores(uniqueWordsRatings)

main()

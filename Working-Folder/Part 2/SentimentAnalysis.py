# TODO REIMPORT FILES AND DOUBLE CHECK STANDARDS AND COMMENTS
import math

def binarySearch(x, L):
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

def getIndividualLinesAsList(file):
    f = open(file, "r")
    listOfLines = []
    for x in f:
        listOfLines.append(x.lower().replace("\n","").replace("\t",""))

    return listOfLines
"""
Purpose: This code is passed in a file name and searches the immediate folder
for that file. When this file is found, it parses in its data line by line.
Each one of these lines are stored in an array for later use and passed out.
"""
def proccessLinesAsListOfWords(file):
    f = open(file, "r")
    reviews = []
    reviews.append([]) #ratings
    reviews.append([]) #blurb
    for line in f:
        reviews[0].append(int(line[:1])-2)
        proccessedLine = line.lower().replace("\n","").replace("\t","")
        reviews[1].append(getWordsOfBlurb(proccessedLine))

    return reviews

"""
Purpose: This method is passed in a blurb of the of a review. Using this blurb,
it then splits up the blurb into the words and puts those split up words into an
array that is passed out.
"""
def getWordsOfBlurb(blurbText):
    bannedWords = getIndividualLinesAsList("stopWords.txt")
    words = []
    lastSpaceIndex = 0
    for i in range(len(blurbText)):
        if blurbText[i] == " ":
            word = blurbText[lastSpaceIndex:i]
            if binarySearch(word,bannedWords) == -1 and word.isalpha():
                words.append(word)
            lastSpaceIndex = i + 1

    return words


"""
Purpose: This function tallys up the scores of all of the words. Words that appear
more in more highly rated movies will correspondingly receive higher scores. It
then outputs this list of scores as an unsorted list of words and their
associated scores.
"""
def getUniqueWordsRating(reviewsAndBlurbs): #[[number, number ...],[[word, word ...],[word, word ...]...]]
    listOfUniqueWords = wordBubbleSort(getUniqueWords(reviewsAndBlurbs[1]))
    parrellelWordSum = []
    parrellelWordNum = []

    for i in range(len(listOfUniqueWords)):
        parrellelWordSum.append(0)
        parrellelWordNum.append(0)

    for i in range(len(reviewsAndBlurbs[0])):
        for word in reviewsAndBlurbs[1][i]:
            listIndex = binarySearch(word, listOfUniqueWords)
            parrellelWordSum[listIndex] += reviewsAndBlurbs[0][i]
            parrellelWordNum[listIndex] += 1

    wordRatings = [listOfUniqueWords,[]]
    for i in range(len(listOfUniqueWords)):
        wordRatings[1].append((parrellelWordSum[i]/parrellelWordNum[i])*math.log(parrellelWordNum[i]))

    return wordRatings


def getUniqueWords(reviews):
    uniqueWords = []
    for blurb in reviews:
        for word in blurb:
            if word not in uniqueWords: # TODO: ask if allowed to do?
                uniqueWords.append(word)
    return uniqueWords

def wordBubbleSort(uniqueWords):
    for i in range(len(uniqueWords)):
        for j in range(len(uniqueWords)-1 - i):
            if uniqueWords[j] > uniqueWords[j+1]:
                uniqueWords[j], uniqueWords[j+1] = uniqueWords[j+1], uniqueWords[j]

    return uniqueWords

def rankWordBubbleSort(uniqueWords):
    for i in range(len(uniqueWords[1])):
        for j in range(len(uniqueWords[1])-1 - i):
            if uniqueWords[1][j] > uniqueWords[1][j+1]:
                uniqueWords[0][j], uniqueWords[0][j+1] = uniqueWords[0][j+1], uniqueWords[0][j]
                uniqueWords[1][j], uniqueWords[1][j+1] = uniqueWords[1][j+1], uniqueWords[1][j]
"""
Purpose: This function receives a list of words and their associated ratings.
Using the built in sort method, the function sorts the list by the the value
that is associated with the word. Words with the highest values are sent to the top.
Words are then displayed by the top twenty and bottom twenty.
"""
def displayScores(uniqueWordsRatings):
    rankWordBubbleSort(uniqueWordsRatings)
    print("Top 20")
    for i in range(-1, -21, -1):
        print(f'{uniqueWordsRatings[1][i]:.2f} {uniqueWordsRatings[0][i]}')
    print("\nBottom 20")
    for i in range(21):
        print(f'{uniqueWordsRatings[1][i]:.2f} {uniqueWordsRatings[0][i]}')


#TODO: make sure to filter out all of the bad apostrophes and stuff
def main():
    reviewsAndBlurbs = proccessLinesAsListOfWords("movieReviews.txt")
    uniqueWordsRatings = getUniqueWordsRating(reviewsAndBlurbs)
    displayScores(uniqueWordsRatings)

main()

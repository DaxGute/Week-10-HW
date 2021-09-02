# TODO REIMPORT FILES AND DOUBLE CHECK STANDARDS AND COMMENTS
import math
"""
Purpose: This code is passed in a file name and searches the immediate folder
for that file. When this file is found, it parses in its data line by line.
Each one of these lines are stored in an array for later use and passed out.
"""
def getIndividualLinesAsList(file):
    f = open(file, "r")
    listOfLines = []
    for x in f:
        listOfLines.append(x.lower().replace("\n","").replace("\t",""))

    return listOfLines

"""
Purpose: This method eliminates all the words that are unlikely to provide clarity
on whether or not a given film is good or bad based on the ratings. These words
are stored in a file that is read in. If any of the words in a line match these
banned words, they are removed. The words are kept as individual indexs on an
array of blurbs and then returned.
"""
def purgeUnecessaryCharacters(reviewBlurbs):
    bannedWords = getIndividualLinesAsList("stopWords.txt")
    additionalBannedWords = [",",".",":",";","a"]
    newTrimmedReviews = []
    for review in reviewBlurbs:
        words = getWordsOfBlurb(review)
        newBlurb = []
        for word in words:
            if word not in bannedWords and word not in additionalBannedWords:
                newBlurb.append(word)
        newTrimmedReviews.append(newBlurb)

    return newTrimmedReviews

"""
Purpose: This method is passed in a blurb of the of a review. Using this blurb,
it then splits up the blurb into the words and puts those split up words into an
array that is passed out.
"""
def getWordsOfBlurb(blurbText):
    words = []
    lastSpaceIndex = 0
    for i in range(len(blurbText)):
        if blurbText[i] == " ":
            words.append(blurbText[lastSpaceIndex:i])
            lastSpaceIndex = i + 1

    return words


"""
Purpose: This method separates the Blurbs and the Ratings from the list. The ratings
are appropriately shifted and then both of them are returned as items of a lists.
"""
def separateRatingBlurbFromList(listOfReviews):
    reviews = []
    reviews.append([]) #ratings
    reviews.append([]) #blurb
    for review in listOfReviews:
        reviews[0].append(int(review[:1])-2)
        reviews[1].append(review[1:])

    reviews[1] = purgeUnecessaryCharacters(reviews[1])

    return reviews


"""
Purpose: This function tallys up the scores of all of the words. Words that appear
more in more highly rated movies will correspondingly receive higher scores. It
then outputs this list of scores as an unsorted list of words and their
associated scores.
"""
def getUniqueWordsRating(reviewsAndBlurbs): #[[number, number ...],[[word, word ...],[word, word ...]...]]
    listOfUniqueWords = getUniqueWords(reviewsAndBlurbs[1])
    parrellelWordSum = []
    parrellelWordNum = []

    for i in range(len(listOfUniqueWords)):
        parrellelWordSum.append(0)
        parrellelWordNum.append(0)

    for i in range(len(reviewsAndBlurbs[0])):
        for word in reviewsAndBlurbs[1][i]:
            listIndex = listOfUniqueWords.index(word) #TODO: ask is this allowed
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


def uniqueWordBubbleSort(uniqueWords):
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
    uniqueWordBubbleSort(uniqueWordsRatings)
    print("Top 20")
    for i in range(-20, 0):
        print(f'{uniqueWordsRatings[1][i]:.2f} {uniqueWordsRatings[0][i]}')
    print("\nBottom 20")
    for i in range(21):
        print(f'{uniqueWordsRatings[1][i]:.2f} {uniqueWordsRatings[0][i]}')


#TODO: make sure to filter out all of the bad apostrophes and stuff
def main():
    listOfReviews = getIndividualLinesAsList("movieReviews.txt")
    reviewsAndBlurbs = separateRatingBlurbFromList(listOfReviews)
    uniqueWordsRatings = getUniqueWordsRating(reviewsAndBlurbs)
    displayScores(uniqueWordsRatings)

main()

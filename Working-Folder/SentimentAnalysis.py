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
    newTrimmedReviews = []
    for review in reviewBlurbs:
        words = getWordsOfBlurb(review)
        newBlurb = []
        for word in words:
            if word not in bannedWords:
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
are appropriately shifted and then both of them are returned as items of a dictionary.
"""
def separateRatingBlurbFromList(listOfReviews):
    reviews = {}
    reviews["ratings"] = []
    reviews["blurb"] = []
    for review in listOfReviews:
        reviews["ratings"].append(int(review[:1])-2)
        reviews["blurb"].append(review[1:])

    reviews["blurb"] = purgeUnecessaryCharacters(reviews["blurb"])

    return reviews


"""
Purpose: This function tallys up the scores of all of the words. Words that appear
more in more highly rated movies will correspondingly receive higher scores. It
then outputs this list of scores as an unsorted dictionary of words and their
associated scores.
"""
def getUniqueWordsRating(reviewsAndBlurbs):
    wordRatings = {}
    wordSum = {}
    wordNum = {}
    for i in range(len(reviewsAndBlurbs['ratings'])):
        for word in reviewsAndBlurbs['blurb'][i]:
            try:
                wordSum[word] += reviewsAndBlurbs['ratings'][i]
            except:
                wordSum[word] = reviewsAndBlurbs['ratings'][i] # creates a key if there isn't already one
            try:
                wordNum[word] += 1
            except:
                wordNum[word] = 1
    for word in wordSum:
        wordRatings[word] = (wordSum[word]/wordNum[word])*math.log(wordNum[word])

    return wordRatings


"""
Purpose: This function receives a dictionary of words and their associated ratings.
Using the built in sort method, the function sorts the dictionary by the the value
that is associated with the word. Words with the highest values are sent to the top.
Words are then displayed by the top twenty and bottom twenty.
"""
def displayScores(uniqueWordsRatings):
    uniqueWordsRatings = sorted(uniqueWordsRatings.items(), key=lambda x:x[1], reverse=True) #yucky but efficient lambdas
    print("Top 20")
    for i in range(21):
        print(f'{uniqueWordsRatings[i][1]:.2f} {uniqueWordsRatings[i][0]}')
    print("\nBottom 20")
    for i in range(-20, 0):
        print(f'{uniqueWordsRatings[i][1]:.2f} {uniqueWordsRatings[i][0]}')


def main():
    listOfReviews = getIndividualLinesAsList("movieReviews.txt")
    reviewsAndBlurbs = separateRatingBlurbFromList(listOfReviews)
    uniqueWordsRatings = getUniqueWordsRating(reviewsAndBlurbs)
    displayScores(uniqueWordsRatings)

main()

def getIndividualLinesAsList(file):
    f = open(file, "r")
    listOfLines = []
    for x in f:
        listOfLines.append(x.lower().replace("\n","").replace("\t",""))

    return listOfLines

def getWords(review):
    words = []
    lastSpaceIndex = 0
    for i in range(len(review)):
        if review[i] == " ":
            words.append(review[lastSpaceIndex:i])
            lastSpaceIndex = i + 1

    return words

def purgeUnecessaryCharacters(reviewBlurbs):
    bannedWords = getIndividualLinesAsList("stopWords.txt")
    newTrimmedReviews = []
    for review in reviewBlurbs:
        words = getWords(review)
        newReview = []
        for word in words:
            if word not in bannedWords:
                newReview.append(word)
        newTrimmedReviews.append(newReview)

    return newTrimmedReviews


def separateRatingBlurbFromList(listOfReviews):
    reviews = {}
    reviews["ratings"] = []
    reviews["blurb"] = []
    for review in listOfReviews:
        reviews["ratings"].append(review[:1])
        reviews["blurb"].append(review[1:])

    reviews["blurb"] = purgeUnecessaryCharacters(reviews["blurb"])

    return reviews

def adjustRatings(ratings):
    allRatings = []
    for rating in ratings:
        allRatings.append(int(rating) - 2)

    return allRatings

def getUniqueWords(blurbs):
    allWordList = []
    for rating in blurbs:
        for word in rating:
            if not word in allWordList:
                allWordList.append(word)

    return allWordList

def getUniqueWordsRating(uniqueWords, reviewsAndBlurbs):
    wordRatings = {}
    for word in uniqueWords:
        wordRatings[word] = 0

    for i in range(len(reviewsAndBlurbs['ratings'])):
        for word in reviewsAndBlurbs['blurb'][i]:
            wordRatings[word] += reviewsAndBlurbs['ratings'][i]

    return wordRatings


def main():
    listOfReviews = getIndividualLinesAsList("smallReviews.txt")
    reviewsAndBlurbs = separateRatingBlurbFromList(listOfReviews)
    reviewsAndBlurbs['ratings'] = adjustRatings(reviewsAndBlurbs['ratings'])
    uniqueWords = getUniqueWords(reviewsAndBlurbs['blurb'])
    uniqueWordsRating = getUniqueWordsRating(uniqueWords, reviewsAndBlurbs)
    displayScores(uniqueWordsRatings)
    print(uniqueWordsRating)

main()

def getIndividualLinesAsList(file):
    f = open(file, "r")
    listOfLines = []
    for x in f:
        listOfLines.append(''.join(filter(str.isalnum, x)) )

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
                print(bannedWords)
        newTrimmedReviews.append(newReview)

    return newTrimmedReviews


def getReviewRatingFromList(listOfReviews):
    reviews = {}
    reviews["ratings"] = []
    reviews["blurb"] = []
    for review in listOfReviews:
        reviews["ratings"].append(review[:1])
        reviews["blurb"].append(review[1:])

    reviews["blurb"] = purgeUnecessaryCharacters(reviews["blurb"])

    return reviews


def main():
    listOfReviews = getIndividualLinesAsList("smallReviews.txt")
    reviews = getReviewRatingFromList(listOfReviews)
    print(reviews)


main()

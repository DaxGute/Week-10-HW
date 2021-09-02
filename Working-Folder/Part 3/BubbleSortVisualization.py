from graphics import *
from random import shuffle
from time import *

def bubbleSortCompareIndexes(windowBars, L, win, j):
    if L[j] > L[j+1]:
        L[j], L[j+1] = L[j+1], L[j]

    displaySwitched(j, j+1, windowBars, L, win)


def displaySwitched(i, j, windowBars, L, win):
    windowBars[i][1].setFill('blue')
    windowBars[j][1].setFill('blue')
    windowBars[i][1].undraw()
    windowBars[j][1].undraw()
    tuple = [0, 0]
    for bar in windowBars:
        if bar[0] == L[i]: #checking the value against current value position
            barBottomX = 2 + (i*11)
            barTopX = 9 + (i*11)
            tuple[0] = (bar[0], Rectangle(Point(barBottomX,0), Point(barTopX,bar[0]*10)))
        if bar[0] == L[j]:
            barBottomX = 2 + (j*11)
            barTopX = 9 + (j*11)
            tuple[1] = (bar[0], Rectangle(Point(barBottomX,0), Point(barTopX,bar[0]*10)))
    windowBars[i] = tuple[0]
    windowBars[j] = tuple[1]

    windowBars[i][1].setFill('red')
    windowBars[j][1].setFill('red')
    windowBars[i][1].draw(win)
    windowBars[j][1].draw(win)


def bubbleSort(windowBars, L, lSorted, win):
    for i in range(len(L)):
        for j in range(len(L)-1-i):
            bubbleSortCompareIndexes(windowBars, L, win, j)
        if L == lSorted:
            break


def updateRectanglesWithRandom(windowBars, L, win):
    shuffle(L)
    for item in win.items[:]:
        item.undraw()
    newBars = []
    for i in L:
        newBars.append(0)
    for i in range(len(L)):
        for bar in windowBars:
            if bar[0] == L[i]:
                barBottomX = 2 + (i*11)
                barTopX = 9 + (i*11)
                newBars[i] = (bar[0], Rectangle(Point(barBottomX, 0), Point(barTopX,bar[0]*10)))
                newBars[i][1].setFill('red')
    for rect in newBars:
        rect[1].draw(win)

    return newBars


def main():
    N = 50
    L = []
    lSorted = []
    windowBars = []
    for i in range(N):
        L.append(i) # in case I want to make it with different values in the future
        lSorted.append(i)
        barBottomX = 2 + (i*11)
        barTopX = 9 + (i*11)
        tuple = (i, Rectangle(Point(barBottomX,0), Point(barTopX,i*10)))
        windowBars.append(tuple)

    win = GraphWin("Bubble Sort", N*11, N*10)
    win.setCoords(0, 0, N*11, N*10)

    for rect in windowBars:
        rect[1].setFill('red')
        rect[1].draw(win)

    windowBars = updateRectanglesWithRandom(windowBars, L, win)

    bubbleSort(windowBars, L, lSorted, win)

    win.getMouse() # pause for click in window

    win.close()
main()

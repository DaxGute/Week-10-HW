"""
Description: Your task is to write a program, visual-sort.py, that displays a visualization 
of how one particular sorting algorithm works.  This visualization can work by printing strings
to the terminal, or — for an extra challenge — by creating an animation using Zelle graphics. 
Your program should allow its users to see how a particular sorting algorithm changes a list 
from unsorted to sorted, one swap at a time.
Name: Daxton Gutekunst
Date: Sep. 5 2021
"""

from graphics import *
from random import shuffle
from time import *

def bubbleSortCompareIndexes(windowBars, L, win, j):
    """
    Purpose: This function runs one comparison of bubble sort. This comparison is then sent to the 
    displaySwitched function to be displayed.
    Parameters: the window bars, parrellel list of values, the window, the current index being compared
    Return Val: NA
    """
    if L[j] > L[j+1]:
        L[j], L[j+1] = L[j+1], L[j]

    displaySwitched(j, j+1, windowBars, L, win)


def displaySwitched(i, j, windowBars, L, win):
    """
    Purpose: Switches the rectangles and displays that switch on the window 
    Parameters: first index, second index, list of rectangles, parrellel list, window
    Return Val: NA
    """
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


def bubbleSort(windowBars, L, win):
    """
    Purpose: This is a modified version of bubble sort. Each comparison is sent to another method to 
    be compared and displayed. When it is sorted, is is stopped and the program is over.
    Parameters: the window bars, a parrellel list of values, the window 
    Return Val: NA
    """
    for i in range(len(L)):
        for j in range(len(L)-1-i):
            bubbleSortCompareIndexes(windowBars, L, win, j)
        if isSorted(L):
            break


def isSorted(L):
    """
    Purpose: Checks if a list is sorted from lowest to highest 
    Parameters: a list 
    Return Val: a boolean based on if the list is sorted or not 
    """
    for i in range(len(L)-1):
        if L[i]>L[i+1]:
            return False
    return True


def updateRectanglesWithRandom(windowBars, L, win):
    """
    Purpose: Randomly shuffles and display rectangles on the window. After it shuffles and recalculates
    the rectangle positions, a list of new rectangles is returned.
    Parameters: list of rectangles, the parrellel list, window
    Return Val: a new list of rectangles
    """
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


def setUpRectangles(N):
    """
    Purpose: Sets up the initial set of rectangles and parrellel list
    Parameters: number of rectangles
    Return Val: the list of rectangles, the parrellel list
    """
    L = []
    lSorted = []
    windowBars = []
    for i in range(N):
        L.append(i) 
        lSorted.append(i)
        barBottomX = 2 + (i*11)
        barTopX = 9 + (i*11)
        rect = (i, Rectangle(Point(barBottomX,0), Point(barTopX,i*10)))
        rect[1].setFill('red')
        windowBars.append(rect)
    
    return windowBars, L


def main():
    numRect = int(input("How large is the list: "))
    windowBars, L = setUpRectangles(numRect)

    win = GraphWin("Bubble Sort", numRect*11, numRect*10)
    win.setCoords(0, 0, numRect*11, numRect*10)

    for rect in windowBars:
        rect[1].draw(win)

    windowBars = updateRectanglesWithRandom(windowBars, L, win)

    bubbleSort(windowBars, L, win)

    win.getMouse()

    win.close()
main()

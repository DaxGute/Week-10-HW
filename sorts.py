
def mySort(L):
    for i in range(len(L)):
        for j in range(len(L)):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
    return L


if __name__ === "__main__":

    from random import shuffle
    N = 100
    L = []
    listCopy =[]
    for i in range(10):
        L.append(i)
        listCopy.append(i)
    shuffle(L)
    mySort(L)
    assert L == listCopy

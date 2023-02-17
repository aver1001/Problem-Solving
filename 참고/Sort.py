import sys
import heapq
Array = [6, 5, 2, 1, 4, 7, 9, 8, 3]
N = len(Array)


def bubbleSort():
    for i in range(N):
        for j in range(N-i-1):
            if Array[j] > Array[j+1]:
                Array[j], Array[j+1] = Array[j+1], Array[j]


def selectSort():
    for i in range(N):
        Min = sys.maxsize
        MinIdx = -1
        for j in range(i, N):
            if Array[j] < Min:
                Min = Array[j]
                MinIdx = j

        if MinIdx != -1:
            Array[i], Array[MinIdx] = Array[MinIdx], Array[i]


def insertSort():
    for i in range(N):
        for j in range(i):
            if Array[j] > Array[i]:
                # insert
                Array.insert(j, Array.pop(i))


def mergeSort(Array):

    def merge(Arr):
        if len(Arr) <= 1:
            return Arr
        else:
            mid = len(Arr)//2
            A = merge(Arr[:mid])
            B = merge(Arr[mid:])

            NA = len(A)
            NB = len(B)

            aPt = 0
            bPt = 0
            result = []
            while True:
                if aPt >= NA and bPt >= NB:
                    break
                elif aPt == NA:
                    result.append(B[bPt])
                    bPt += 1
                    continue
                elif bPt == NB:
                    result.append(A[aPt])
                    aPt += 1
                    continue
                if A[aPt] <= B[bPt]:
                    result.append(A[aPt])
                    aPt += 1
                else:
                    result.append(B[bPt])
                    bPt += 1

            return result

    return merge(Array)


def heapSort():
    heapq.heapify(Array)
    result = []
    while Array:
        result.append(heapq.heappop(Array))

    return result


def quickSort(Arr):
    if len(Arr) <= 1:
        return Arr

    lower = []
    higher = []
    same = []
    for idx in range(len(Arr)):
        if Arr[idx] < Arr[0]:
            lower.append(Arr[idx])
        elif Arr[idx] == Arr[0]:
            same.append(Arr[idx])
        else:
            higher.append(Arr[idx])

    return quickSort(lower) + same + quickSort(higher)


Array = quickSort(Array)
print(Array)

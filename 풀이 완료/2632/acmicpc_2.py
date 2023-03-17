import sys
sys.stdin = open('input.txt', "r")

targetSize = int(sys.stdin.readline().rstrip())

sizeA, sizeB = map(int, sys.stdin.readline().rstrip().split())
listA = []
for _ in range (sizeA):
    listA.append(int(sys.stdin.readline().rstrip()))

listB = []
for _ in range (sizeB):
    listB.append(int(sys.stdin.readline().rstrip()))

print(targetSize)
print(listA)
print(listB)

answer = 0

sumA = sum(listA)
sumB = sum(listB)
ltA = 0
rtA = 0
ltB = -1
ltB = -1
hapA = listA[0]
##A Pt
while ltA < len(listA):
    
    if hapA >= targetSize:
        if hapA == targetSize:
            answer += 1
            print(ltA,rtA,hapA,'||',ltB,rtB)
        ltA += 1
        rtA = ltA
        if ltA == len(listA):
            break
        hapA=listA[ltA]
    else:
        rtA += 1
        if rtA == len(listA):
            rtA = 0
        hapA += listA[rtA]
    ##B Pt
    ltB = 0
    rtB = 0
    hapB = listB[0]
    
    while ltB < len(listB):
        if sumB < hapB:
            break
        if hapA + hapB >= targetSize:
            
            if hapA + hapB == targetSize:
                print(ltA,rtA,hapA,'||',ltB,rtB,hapB)
                answer += 1
            if ltB == rtB:
                ltB += 1
                rtB += 1
                if rtB == len(listB):
                    rtB = 0

                hapB = listB[rtB]
            else:
                hapB -= listB[ltB]
                ltB += 1
        else:
            rtB += 1
            if rtB == len(listB):
                rtB = 0
            hapB += listB[rtB]
    ltB = -1
    rtB = -1
print(answer)
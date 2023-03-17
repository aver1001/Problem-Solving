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

# print(listA)
# print(listB)

def calCase(List):
    case = {0:1}
    for i in range (len(List)):
        hap = 0
        for j in range (i,len(List)):
            hap += List[j]
            if hap in case:
                case[hap] += 1
            else:
                case[hap] = 1

        for j in range (i-1):
            hap += List[j]
            if hap in case:
                case[hap] += 1
            else:
                case[hap] = 1
                
    return case
        
caseA = calCase(listA)
caseB = calCase(listB)

#print(caseA)
#print(caseB)

answer = 0
for costA,timesA in sorted(caseA.items()):
    if targetSize-costA in caseB:
        answer += timesA*caseB[targetSize-costA]
print(answer)
import sys
sys.stdin = open('input.txt', "r")

N,M = map(int, sys.stdin.readline().rstrip().split())

table = {i:{'in':set(),'out':set()} for i in range (1,N+1)}

for _ in range (M):
    A,B = map(int, sys.stdin.readline().rstrip().split())
    table[A]['in'].add(B)
    table[B]['out'].add(A)

def moveIn(x):
    isVisited[x] = True

    hap = 0
    for i in table[x]['in']:
        if isVisited[i] == False:
            hap += moveIn(i)
    
    return hap + 1

def moveOut(x):
    isVisited[x] = True
    hap = 0
    for i in table[x]['out']:
        if isVisited[i] == False:
            hap += moveOut(i)
    return hap+1
answer = 0
for idx in range (1,N+1):
    isVisited=[False]*(N+1)
    if (N == moveIn(idx) + moveOut(idx)-1):
        answer += 1
print(answer)
        
        
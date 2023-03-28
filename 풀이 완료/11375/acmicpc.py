import sys
sys.stdin = open('input.txt', "r")

def bimatch(x):
    #방문했다면
    if visited[x]:
        return False
    visited[x] = True
    
    for num in doItList[x]:
        if choose[num] == -1 or bimatch(choose[num]):
            choose[num] = x
            return True
    return False

N,M = map(int, sys.stdin.readline().rstrip().split())
doItList = []
for _ in range (N):
    doItList.append(list(map(int, sys.stdin.readline().rstrip().split()))[1:])

choose = [-1]*(M+1)
for i in range (N):
    visited = [False]*(N+1)
    bimatch(i)
    
for i in range (N):
    visited = [False]*(N+1)
    bimatch(i)

answer = 0
for i in choose:
    if i != -1:
        answer += 1
print(answer)
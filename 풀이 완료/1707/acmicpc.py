import sys
from collections import deque

sys.stdin = open('input.txt', "r")

def bfsA(queue:deque):
    
    nextQueue = deque([])
    
    while queue:
        loc = queue.popleft()
        groupA.add(loc)
        for nextLoc in table[loc]:
            if nextLoc not in groupA and nextLoc not in groupB:
                nextQueue.append(nextLoc)
    
    if len(nextQueue) != 0:
        bfsB(nextQueue)

def bfsB(queue:deque):
    nextQueue = deque([])
    
    while queue:
        loc = queue.popleft()
        groupB.add(loc)
        for nextLoc in table[loc]:
            if nextLoc not in groupA and nextLoc not in groupB:
                nextQueue.append(nextLoc)
    
    if len(nextQueue) != 0:
        bfsA(nextQueue)


def solution()->int:
    cnt = 0
    for idx in range (1,V+1):
        #이미 그룹에 들어가 있을경우
        if idx in groupA or idx in groupB:
            #다음거 진행
            pass
        #그룹에 없는것일경우
        else:
            #bfs돌면서 확인
            bfsA(deque([idx]))
            cnt += 1
    return cnt

K = int (sys.stdin.readline().rstrip())
for _ in range (K):
    #정점V(1~V) 간선
    V,E = map(int, sys.stdin.readline().rstrip().split())
    table = {i:set() for i in range (1,V+1)}
    #이분그래프를 만들기 위해서 그룹 두개를 만든다
    groupA = set()
    groupB = set()
    
    for _ in range (E):
        u,v = map(int, sys.stdin.readline().rstrip().split())
        table[u].add(v)
        table[v].add(u)

    solution()
    if len(groupA) + len(groupB) == V:
        print("YES")
    else:
        print("NO")

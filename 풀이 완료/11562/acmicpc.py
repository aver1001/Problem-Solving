import sys
from collections import deque
from copy import deepcopy
sys.stdin = open('input.txt', "r")

n, m = map(int, sys.stdin.readline().rstrip().split())

table = { i:set() for i in range (n)}
reverse = { i:set() for i in range (n)}
for _ in range (m):
    u,v,b = map(int, sys.stdin.readline().rstrip().split())
    u -= 1
    v -= 1
    table[u].add(v)
    if b == 1:
        table[v].add(u)
    else:
        reverse[v].add(u)

allAnswer = []

for i in range (n):
    
    #i번에서 출발했을떄 어디까지 도착할수 있는지를 미리 파악
    
    check = {i}
    root = [i for i in range (n)]
    if root[i] == i:
        queue = deque([i])
        
        while queue:
            nowLoc = queue.popleft()
            
            for nextLoc in table[nowLoc]:
                if root[nextLoc] != i:
                    check.add(nextLoc)
                    root[nextLoc] = i
                    queue.append(nextLoc)
    
    answer = [0]*n
    #print(root)
    cnt = 1
    while (len(check) != 0):
        
        queue = deque([])
        tempCheck = set()
        #역방향 확인해야되는 친구들을 순회하면서
        for Loc in check:
            #그친구의 역방향들을 확인해서
            for nextLoc in reverse[Loc]:
                #역방향이 아직 도착하지 않았다면
                if root[nextLoc] != i:
                    #역방향의 도착지에 도착했다고 표시하고
                    root[nextLoc] = i
                    #몇번만에 도착했는지 적어준다
                    answer[nextLoc] = cnt
                    #새로 방문한곳에 넣어준다
                    tempCheck.add(nextLoc)
                    #큐에 넣어준다
                    queue.append(nextLoc)
        
        #역방향으로 도착한 애들의 순방향으로 어디까지 갈수있나 확인
        while queue:
            #역방향 도착한 위치 뽑아줘서
            Loc = queue.popleft()
            #도착한 친구의 순방향 순회를 한다
            for nextLoc in table[Loc]:
                if root[nextLoc] == i:
                    continue
                root[nextLoc] = i
                answer[nextLoc] = cnt
                tempCheck.add(nextLoc)
                queue.append(nextLoc)
        
        check = tempCheck
        cnt += 1
    allAnswer.append(answer)

#print(allAnswer)


k = int(sys.stdin.readline().rstrip())
for _ in range (k):
    s,e = map(int, sys.stdin.readline().rstrip().split())
    print(allAnswer[s-1][e-1])
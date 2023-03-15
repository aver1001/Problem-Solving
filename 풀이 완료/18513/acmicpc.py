import sys
from collections import deque
sys.stdin = open('input.txt', "r")

N,K = map(int, sys.stdin.readline().rstrip().split())
water = list(map(int,sys.stdin.readline().rstrip().split()))
isBlock = set(water)

queue = deque([])
cnt = 0

for w in water:
    if w-1 not in isBlock:
        queue.append((w-1,1,True))# isLeft
    if w+1 not in isBlock:
        queue.append((w+1,1,False))

answer = 0
while queue:
    Loc,cost,isLeft = queue.popleft()
    if Loc not in isBlock:  #집을 짓지 않았다면
        isBlock.add(Loc)    #집을 지었다고 적어주고
        cnt += 1            #집의 개수를 더해준다
        answer += cost

        if cnt == K:        #목표치만큼 집을 지었다면
            break           #멈춘다
        
    if isLeft :
        if Loc-1 not in isBlock:
            queue.append((Loc-1,cost+1,isLeft))
    else:
        if Loc+1 not in isBlock:
            queue.append((Loc+1,cost+1,isLeft))
print(answer)
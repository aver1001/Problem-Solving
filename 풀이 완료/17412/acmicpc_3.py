import sys
from collections import deque
sys.stdin = open('input.txt', "r")

N,P = map(int, sys.stdin.readline().rstrip().split())

def MaxFlow(start,end):
    answer = 0
    isVisited = [False]*N
    while True:
        #부모값 초기화
        root = [-1]*N
        queue = deque([start])
        
        #경로탐색
        while queue:
            now = queue.popleft()
            for next in route[now]:
                if (flow[now][next] - currentFlow[now][next] > 0 and root[next] == -1 and isVisited[next] == False):
                    queue.append(next)
                    root[next] = now
                    
            if root[end] != -1:
                break
        if root[end] == -1:
            break
        
        now = end
        minFlow = sys.maxsize
        
        while True:
            next = root[now]
            if now == start:
                break
            minFlow = min(minFlow,flow[next][now] - currentFlow[next][now])
            now = next
        now = end
        while True:
            next = root[now]
            if now == start:
                break
            currentFlow[now][next] -= minFlow
            currentFlow[next][now] += minFlow
            now = next
        answer += minFlow
    return answer
    

flow = [[0]*N for _ in range (N)]
route = [set() for _ in range (N)]
currentFlow = [[0]*N for _ in range (N)]
for _ in range (P):
    A,B = map(int, sys.stdin.readline().rstrip().split())
    A -= 1
    B -= 1
    
    flow[A][B] = 1
    flow[A][B] = 1
    route[A].add(B)
    route[B].add(A)

print(MaxFlow(0,1))
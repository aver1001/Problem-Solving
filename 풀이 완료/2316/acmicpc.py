import sys
from collections import deque
sys.stdin = open('input.txt', "r")

N ,P= map(int, sys.stdin.readline().rstrip().split())
flow = [[0]*(2*N) for _ in range (2*N)]
route = [[] for _ in range (2*N)]

def maxFlow(start,end):
    currentFlow = [[0]*(2*N) for _ in range (2*N)]
    answer = 0
    
    while True:
        root = [-1]*(2*N)
        queue = deque([start])
        
        # BFS로 경로를 탐색한다.
        while queue:
            loc = queue.popleft()
            #print(loc,':',route[loc])
            for nextLoc in route[loc]:
                #print(flow[loc][nextLoc],currentFlow[loc][nextLoc])
                if (flow[loc][nextLoc] - currentFlow[loc][nextLoc] > 0 and root[nextLoc] == -1):
                    queue.append(nextLoc)
                    root[nextLoc] = loc
            
                    #end까지 도착했을경우 경로를 찾은것.
                    if root[end] != -1:
                        break
        #print(root)
        # end까지 도착하지 못했을경우 경로가 더이상 없으므로, break
        if root[end] == -1:
            break
        
        #도착지까지 도착한것이므로, 정답에 1을 더해준다
        answer += 1
        
        #경로를 뒤집어가면서 역방향, 순방향 값을 변경해준다
        #최소 플로우는 무조건 1임.
        now = end
        while True:
            next = root[now]
            currentFlow[now][next] -= 1
            currentFlow[next][now] += 1
            now = next
            
            if now == start:
                break
        
    return answer



    
## flow 설정
for _ in range (P):
    A ,B= map(int, sys.stdin.readline().rstrip().split())
    A -= 1
    B -= 1
    ## in A
    ## out A + N
    
    flow[A+N][B] = 1
    flow[B+N][A] = 1
    
    route[A+N].append(B)
    route[B+N].append(A)
    
    route[B].append(A+N)
    route[A].append(B+N)
# in -> out 연결
for i in range (N):
    flow[i][i+N] = 1
    route[i+N].append(i)
    route[i].append(i+N)

# 시작점은 0의 out임을 주의하자.
print(maxFlow(0+N,1))
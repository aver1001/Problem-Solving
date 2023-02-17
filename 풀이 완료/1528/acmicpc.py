import sys
from collections import deque
sys.stdin = open('input.txt', "r")
N = int(sys.stdin.readline().rstrip())

queue= deque([''])

answer = []
while queue:
    temp = queue.popleft()
    
    t1 = int('4'+temp)
    t2 = int('7'+temp)
    
    if t1 <= N:
        queue.append(str(t1))
        answer.append(t1)
    if t2 <= N:
        queue.append(str(t2))
        answer.append(t2)

#print(answer)
answer.sort(reverse=True)
DP = [sys.maxsize]*(N+1)
for a in answer:
    DP[a] = 1
    for idx in range (a+1,N+1):
        DP[idx] = min(DP[idx],DP[idx-a]+1)
#print(DP)
        

# def DFS(x):
    
#     if x == 0:
#         return 0
    
#     if DP[x] != 0:
#         return DP[x]
#     ret = sys.maxsize
    
#     for a in answer:
#         if x-a >= 0: 
#             ret = min(DFS(x-a)+1,ret)
    
#     DP[x] = ret
#     return DP[x]
# DP = [0]*(N+1)
# DFS(N)
def findAnswer(x):
    
    for a in answer[::-1]:
        
        if DP[x]-DP[x-a] == 1 or x-a == 0:
            print(a,end=' ')
            findAnswer(x-a)
            return

if DP[N] == sys.maxsize:
    print(-1)
else:
    findAnswer(N)
import sys
import time
sys.stdin = open('input.txt', "r")

N,M = map(int, sys.stdin.readline().rstrip().split())
table = []
for _ in range (N):
    table.append(int(sys.stdin.readline().rstrip()))
    
    


lt,rt = 0, sys.maxsize
answer = sys.maxsize
while lt <= rt:    
    mid = (lt+rt) // 2
    temp = 0
    
    for t in table:
        temp += mid//t
        
    if temp >= M:
        rt = mid - 1
        answer = min(mid,answer)
    else:
        lt = mid + 1
    
print(answer)

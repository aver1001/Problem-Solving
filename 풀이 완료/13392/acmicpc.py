import sys
from collections import deque

sys.stdin = open('input.txt', "r")

N = int(sys.stdin.readline().rstrip())
start = int(sys.stdin.readline().rstrip())
target = int(sys.stdin.readline().rstrip())




def bfs(start):
    queue = deque([[start,0]])
    DP = [sys.maxsize]*(10**(N))
    
    while queue:
        num,cnt = queue.popleft()
        
        #바꾸는 idx
        for idx in range (N):
            #left
            change = turnLeft(num,idx)
            if change == target:
                print(cnt+1)
                exit()
            if DP[change] > cnt+1:
                DP[change] = cnt +1
                queue.append([change,cnt+1])
            
            #right
            change = turnRight(num,idx)
            if change == target:
                print(cnt+1)
                exit()
            if DP[change] > cnt+1:
                DP[change] = cnt +1
                queue.append([change,cnt+1])

def turnLeft(num:int,start:int):
    #다같이 움직이기(증가)
    for idx in range (start,N):
        
        location = 10**(N-1-idx)
        
        if num // location == 9:
            num -= location*9
        else:
            num += location
    return num


def turnRight(num:int,start:int):
    #하나만 움직이기 (감소)
    location = 10**(N-1-start)
    
    if num // location == 0:
        num += location*9
    else:
        num -= location
    return num

bfs(start)
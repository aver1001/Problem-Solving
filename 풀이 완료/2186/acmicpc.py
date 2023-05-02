import sys
from collections import deque
sys.stdin = open('input.txt', "r")

Y,X,K = map(int, sys.stdin.readline().rstrip().split())
board = []
for _ in range (Y):
    board.append(list(sys.stdin.readline().rstrip()))
target = sys.stdin.readline().rstrip()

def printBoard(board):
    for i in board:
        print(i)
    print()

def isRange(y:int, x:int):
    if (0<= y < Y and 0<= x <X):
        return True

def move(y,x):
    return dfs(y,x,1)

def dfs(y,x,cnt):
    global answer
    
    if cnt == len(target):
        return 1
    
    if DP[y][x][cnt] != -1:
        return DP[y][x][cnt]
    
    hap = 0
    
    for idx in range (4):
        for k in range (1,K+1):
            ty = y + k*dy[idx]
            tx = x + k*dx[idx]
            if isRange(ty,tx) and board[ty][tx] == target[cnt] :
                hap += dfs(ty,tx,cnt+1)
                
    DP[y][x][cnt] = hap
    return hap

dy = (0,0,1,-1)
dx = (1,-1,0,0)
answer = 0
DP = [[[-1]*(len(target)+1) for _ in range (Y)] for _ in range(X)]

for y in range (Y):
    for x in range (X):
        if board[y][x] == target[0]:
            answer += move(y,x)
print(answer)
import sys
from collections import deque
sys.stdin = open('input.txt', "r")

dy = (0,0,1,-1)
dx = (1,-1,0,0)

def isRange(y:int, x:int) -> bool:
    if 0<= y < Y and 0<= x < X:
        return True
    return False

def printBoard(board:list)-> None:
    for i in board:
        print(i)
    print()

Y,X,K = map(int, sys.stdin.readline().rstrip().split())
board = []
for _ in range (Y):
    board.append(list(map(int, list(sys.stdin.readline().rstrip()))))
#print(K)
#printBoard(board)

DP = [[[False]*(K+1) for _ in range (X)]for _ in range (Y)]

queue = deque([[0,0,0,1]])

while queue:
    y,x,k,cnt = queue.popleft()
    #print(y,x,k,cnt)
    if y == Y-1 and x == X-1:
        print(cnt)
        exit(0)
    
    for idx in range (4):
        ty = y + dy[idx]
        tx = x + dx[idx]
        
        if isRange(ty,tx):
            if board[ty][tx] == 1 and k < K and DP[ty][tx][k+1] == False:
                DP[ty][tx][k+1] = True
                queue.append([ty,tx,k+1,cnt+1])
            elif board[ty][tx] == 0 and DP[ty][tx][k] == False:
                DP[ty][tx][k] = True
                queue.append([ty,tx,k,cnt+1])
print(-1)
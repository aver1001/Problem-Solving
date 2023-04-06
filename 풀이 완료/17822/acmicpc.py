import sys
from collections import deque

dy = (0,0,1,-1)
dx = (1,-1,0,0)

def move(x,d,k):
    for y in range (x,N+1,x):
        #시계방향
        if d ==0:
            for _ in range (k):
                board[y].appendleft(board[y].pop())
        #반시계방향
        elif d == 1:
            for _ in range (k):
                board[y].append(board[y].popleft())

def isRange(y:int, x:int) -> bool:
    if (0<= x < M and 0<= y < N+1):
        return True
    return False

def bfs(Y:int, X:int, isVisted:list) ->bool:
    
    loc = {(Y,X)}
    queue = deque([[Y,X]])
    
    while queue:
        y,x = queue.popleft()
        
        for idx in range (4):
            ty = y+dy[idx]
            tx = x+dx[idx]
            
            if tx == M:
                tx = 0
            if tx == -1:
                tx = M-1

            if(isRange(ty,tx) and isVisted[ty][tx] == False and board[Y][X] == board[ty][tx]):
                queue.append([ty,tx])
                isVisted[ty][tx] = True
                loc.add((ty,tx))
    
    
    if len(loc) >= 2:
        for y,x in loc:
            board[y][x] = 0
        return True
    else:
        return False


def delete() -> bool:
    state = False
    isVisted = [[False]*M for _ in range (N+1)]
    for y in range (1,N+1):
        for x in range (M):
            if (isVisted[y][x] == False and board[y][x] != 0):
                state |= bfs(y,x,isVisted)
    return state

def setAvg():
    cnt = 0
    hap = 0
    for y in range (1,N+1):
        for x in range (M):
            if board[y][x] != 0:
                cnt += 1
                hap += board[y][x]
    if cnt == 0:
        return
    aveage = hap/cnt
    for y in range (1,N+1):
        for x in range (M):
            if board[y][x] != 0:
                if board[y][x] > aveage:
                    board[y][x] -= 1
                elif board[y][x] < aveage:
                    board[y][x] += 1

def printAnswer():
    hap = 0
    for y in range (1,N+1):
        for x in range (M):
            hap += board[y][x]
    print(hap)

def printBoard():
    for i in board:
        print(i)
    print()

sys.stdin = open('input.txt', "r")

N,M,T = map(int, sys.stdin.readline().rstrip().split())
board = [deque([0]*M)]
for _ in range (N):
    board.append(deque(map(int,sys.stdin.readline().rstrip().split(' '))))
    
printBoard()
for _ in range (T):
    x,d,k = map(int, sys.stdin.readline().rstrip().split())
    move(x,d,k)
    printBoard()
    if delete() == False:
        setAvg()
    printBoard()
printAnswer()
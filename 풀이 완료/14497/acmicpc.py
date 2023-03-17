import sys
from collections import deque
sys.stdin = open('input.txt', "r")

dy = (0,0,1,-1)
dx = (1,-1,0,0)

def isRange(y:int,x:int) -> bool:
    if 0<= y < Y and 0<= x < X:
        return True
    else:
        return False
    
def printBoard():
    for i in board:
        print(i)
    print()

def solution()-> bool:
    queue = deque([[startY,startX]])
    
    isVisted = set()
    isVisted.add((startY,startX))
    while queue:
        y,x = queue.popleft()
        for idx in range (4):
            ty = y+dy[idx]
            tx = x+dx[idx]
            if isRange(ty,tx) and (board[ty][tx] != '1') and (ty,tx) not in isVisted:
                queue.append([ty,tx])
                isVisted.add((ty,tx))
    for y,x in isVisted:
        for idx in range (4):
            ty = y+dy[idx]
            tx = x+dx[idx]
            if isRange(ty,tx):
                board[ty][tx] = '0'
                if ty == endY and tx == endX:
                    return True
    
    return False
            
        


Y, X = map(int, sys.stdin.readline().rstrip().split())
startY, startX,endY,endX = map(int, sys.stdin.readline().rstrip().split())
startY-= 1
startX-= 1
endY-=1
endX-=1

board = []
for _ in range (Y):
    board.append(list(sys.stdin.readline().rstrip()))

cnt = 0
while True:
    
    state = solution()
    cnt += 1
    if state:
        break
print(cnt)




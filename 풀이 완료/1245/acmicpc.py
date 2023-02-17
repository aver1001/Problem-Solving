import sys
from collections import deque
sys.stdin = open('input.txt', "r")

Y,X = map(int, sys.stdin.readline().rstrip().split())

board = []
for _ in range (Y):
    board.append(list(map(int,sys.stdin.readline().rstrip().split())))
    
def printBoard(board):
    for i in board:
        print(i)
    print()

check = [[0]*X for _ in range (Y)]

dy = (-1,-1,-1,0,0,1,1,1)
dx = (-1,0,1,-1,1,-1,0,1)
def BFS(y,x,height):
    queue = deque([(y,x)])
    isSanbong = True
    
    while queue:
        y,x = queue.popleft()
        check[y][x] = answer
        for idx in range (8):
            ty = y+dy[idx]
            tx = x+dx[idx]
            
            
            
            if 0<= ty < Y and 0<= tx < X  and check[ty][tx] == 0:
                if board[y][x] == board[ty][tx]:
                    if board[ty][tx] == 0:
                        continue
                    queue.append((ty,tx))
                elif board[y][x] < board[ty][tx]:
                    isSanbong = False
    return isSanbong
                    

answer = 0

for y in range (Y):
    for x in range (X):
        if check[y][x] == 0 and board[y][x] != 0:
            
            if BFS(y,x,board[y][x]):
                answer += 1
            
printBoard(check)


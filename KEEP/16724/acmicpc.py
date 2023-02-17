import sys
from collections import deque
sys.stdin = open('input.txt', "r")

direction = {
    'U':(-1,0),
    'L':(0,-1),
    'D':(1,0),
    'R':(0,1)
}

Y, X = map(int, sys.stdin.readline().rstrip().split())
board = []
for _ in range (Y):
    board.append(list(sys.stdin.readline().rstrip()))
    
def printBoard(board):
    for i in board:
        print(i)
    print()
    

check = [[0]*X for _ in range (Y)]

cnt = 0
answer = 0
for y in range (Y):
    for x in range (X):
        if check[y][x] == 0:
            cnt += 1
            ty = y
            tx = x
            while True:
                check[ty][tx] = cnt
                #printBoard(check)
                dy,dx = direction[board[ty][tx]]
                
                ty += dy
                tx += dx
                if 0<= ty < Y and 0<= tx < X:
                    if check[ty][tx] == 0:
                        continue
                    elif check[ty][tx] == cnt:
                        answer += 1
                        break
                    else:
                        break
                else:
                    break
                
                        
print(answer)
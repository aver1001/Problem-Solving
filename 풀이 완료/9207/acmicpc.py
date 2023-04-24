import sys
from copy import deepcopy
sys.stdin = open('input.txt', "r")



dy = (0,0,1,-1)
dx = (1,-1,0,0)

def printBoard(board):
    for i in board:
        print(i)
    print()

def isRange(y,x):
    if 0<= y < 5 and 0<= x < 9:
        return True
    
def calPin(board):
    cnt = 0
    for y in range (5):
        for x in range (9):
            if board[y][x] == 'o':
                cnt += 1
    return cnt

def dfs(board,cnt):
    temp = cnt
    for y in range (5):
        for x in range (9):
            if board[y][x] == 'o':
                for idx in range (4):
                    ty = y+dy[idx]
                    tx = x+dx[idx]
                    tty = ty+dy[idx]
                    ttx = tx+dx[idx]
                    if isRange(tty,ttx) and board[ty][tx] == 'o' and board[tty][ttx] == '.':
                        tempBoard = deepcopy(board)
                        tempBoard[y][x] = '.'
                        tempBoard[ty][tx] = '.'
                        tempBoard[tty][ttx] = 'o'
                        temp = max(dfs(tempBoard,cnt+1),temp)
    return temp


N = int(sys.stdin.readline().rstrip())

for _ in range (N):
    board = []
    for _ in range (5):
        board.append(list(sys.stdin.readline().rstrip()))
    sys.stdin.readline()
    v = dfs(board,0)
    print(calPin(board)-v,v)
    

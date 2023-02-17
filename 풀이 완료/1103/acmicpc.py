import sys
sys.setrecursionlimit(1000000)
sys.stdin = open('input.txt', "r")

Y,X  = map(int, sys.stdin.readline().rstrip().split())
board = []
for _ in range (Y):
    board.append(list(sys.stdin.readline().rstrip()))

def printBoard(board):
    for i in board:
        print(i)
    print()
    
dy = (0,0,1,-1)
dx = (1,-1,0,0)

costs = [[0]*X for _ in range (Y)]
isVisited = [[False]*X for _ in range (Y)]
answer = 1

def DFS(y,x,cost):
    global answer
    
    for idx in range (4):
        ty = y+dy[idx]*int(board[y][x])
        tx = x+dx[idx]*int(board[y][x])
        
        if 0<= ty < Y and 0<= tx < X and board[ty][tx] != 'H' and cost+1 > costs[ty][tx]:
            
            if isVisited[ty][tx] == True:
                print(-1)
                exit()
            
            costs[ty][tx] = cost + 1
            isVisited[ty][tx] = True
            answer =  max(cost+1,answer)
            DFS(ty,tx,cost+1)
            isVisited[ty][tx] = False
            
DFS(0,0,1)
print(answer)
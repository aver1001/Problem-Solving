import sys
sys.setrecursionlimit(100000)
sys.stdin = open('input.txt', "r")

def printBoard(board):
    for i in board:
        print(i)
    print()

def isRange(y:int,x:int):
    if (0<= y < Y and 0 <= x < X):
        return True
    else:
        return False
    
dy = (0,-1,-1,0)
dx = (-1,-1,0,0)
def DFS(y:int,x:int,cnt:int):
    if y == Y-1 and x == X-1:
        global answer
        answer = max(answer,cnt)
    
    isBlock = False
    
    if y-1 >= 0 and x-1 >= 0: 
        
        for idx in range (4):
            if not isRange(y+dy[idx],x+dx[idx]):
                isBlock = True
                break
            
            if isRange(y+dy[idx],x+dx[idx]) and (board[y+dy[idx]][x+dx[idx]] == 1 or (isCheckd[y+dy[idx]][x+dx[idx]] == True)):
                isBlock = True
                break
        
        ##설치를 하거나
        if isBlock == False:
            for idx in range (4):
                isCheckd[y+dy[idx]][x+dx[idx]] = True
                
            if (x+1 >= X):
                DFS(y+1,0,cnt+1)
            else:
                DFS(y,x+1,cnt+1)
                
            for idx in range (4):
                isCheckd[y+dy[idx]][x+dx[idx]] = False
    
    #설치를 안하거나
    if (x+1 >= X):
        DFS(y+1,0,cnt)
    else:
        DFS(y,x+1,cnt)
            

T = int(sys.stdin.readline())
for test_case in range (1,T+1):
    Y,X = map(int,sys.stdin.readline().rstrip().split())
    board = []
    isCheckd = [[False]*X for _ in range (Y)]
    
    for _ in range (Y):
        board.append(list(map(int,sys.stdin.readline().rstrip().split())))
        
    answer = 0
    DFS(0,0,0)
    print(answer)
    
    

            

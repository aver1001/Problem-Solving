import sys
from collections import deque
sys.stdin = open('input.txt', "r")
N = int(sys.stdin.readline().rstrip())

turnY = (-1,-1,-1,0,0,1,1,1)
turnX = (-1,0,1,-1,1,-1,0,1)

dy = (0,0,1,-1)
dx = (1,-1,0,0)

wy = (0,0,0)
wx = (-1,0,1)

hy = (-1,0,1)
hx = (0,0,0)

def printBoard(board):
    for i in board:
        print(i)
    print()

# 0 => 가로
# 1 => 세로

def findAll(board):
    Bloc = []
    Eloc = []
    for y in range (N):
        for x in range(N):
            if board[y][x] == 'B':
                Bloc.append([y,x])
                continue
            if board[y][x] == 'E':
                Eloc.append([y,x])
                continue
    if Bloc[0][0] == Bloc[1][0] == Bloc[2][0]:
        bResult = [*Bloc[1],0]
    else:
        bResult = [*Bloc[1],1]
        
    if Eloc[0][0] == Eloc[1][0] == Eloc[2][0]:
        eResult = [*Eloc[1],0]
    else:
        eResult = [*Eloc[1],1]
    
    return bResult,eResult

def isRange(y:int,x:int) -> bool:
    if(0<= y < N and 0<= x < N and board[y][x] != '1'):
        return True
    return False

board = []
for _ in range (N):
    board.append(list(sys.stdin.readline().rstrip()))
    
DP = [[[False]*2 for _ in range(N)] for _ in range (N)]

Start,End = findAll(board)

queue = deque([[*Start,0]])
while queue:
    y,x,d,cnt = queue.popleft()
    if y == End[0] and x == End[1] and d == End[2]:
        print(cnt)
        exit()
    
    #가로라면s
    if d == 0:
        for i in range (4):
            #가로 다 확인해보고
            for j in range(3):
                ty = y+wy[j]+dy[i]
                tx = x+wx[j]+dx[i]
                #못가면 break
                if not isRange(ty,tx):
                    break
            #for 문 다 돌았다면 움직일수 있는것임
            else:
                if DP[y+dy[i]][x+dx[i]][0] == False:
                    DP[y+dy[i]][x+dx[i]][0] = True
                    queue.append([y+dy[i],x+dx[i],0,cnt+1])

        #회전 처리
        for i in range (8):
            ty = y + turnY[i]
            tx = x + turnX[i]
            
            if not isRange(ty,tx):
                break
        else:
            if DP[y][x][1] == False:
                DP[y][x][1] = True
                queue.append([y,x,1,cnt+1])
    else:
        for i in range (4):
            for j in range (3):
                ty = y+hy[j] + dy[i]
                tx = x+hx[j] + dx[i]
                #못가면 break
                if not isRange(ty,tx):
                    break
            else:
                if DP[y+dy[i]][x+dx[i]][1] == False:
                    DP[y+dy[i]][x+dx[i]][1] = True
                    queue.append([y+dy[i],x+dx[i],1,cnt+1])
        
        for i in range (8):
            ty = y + turnY[i]
            tx = x + turnX[i]
            
            if not isRange(ty,tx):
                break
        else:
            if DP[y][x][0] == False:
                DP[y][x][0] = True
                queue.append([y,x,0,cnt+1])
print(0)
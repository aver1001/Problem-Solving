import sys
from itertools import permutations
from copy import deepcopy
sys.stdin = open('input.txt', "r")

Y,X,K = map(int, sys.stdin.readline().rstrip().split())

board = []
for _ in range (Y):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))

#두개씩 바꿀거면 회전은 반시계로 해야 시계방향으로 돌릴수 있다.
dy = (1,0,-1,0)
dx = (0,1,0,-1)

def isRange(y:int,x:int)->bool:
    if 0<= y < Y and 0 <= x < X:
        return True
    return False

def rotate(startY:int, startX:int,c:int,board:list):
    
    add = 0
    while True:
        direction = 0
        
        #시작점을 왼쪽 맨위에서 한칸씩 오른쪽 아래로 내려가준다
        y = startY-c+add
        x = startX-c+add
        
        
        #기저조건
        if y == startY and x == startX:
            break
        
        y+=1
        #4방향 돌기
        while direction != 4:
            '''
            회전 로직
            1. 자신의 좌표 +1 을 확인해서 범위를 벗어나는지 확인한다
                => 벗어난다면 방향+1 해준다
            2. 벗어나지 않는다면 두개를 바꿔주고 좌표+1 해준다
            '''
            while True:
                #다음좌표 확인
                ty = y+dy[direction]
                tx = x+dx[direction]

                #만약 다음 좌표가 범위안에 들어가고, 범위를 벗어나지 않는다면
                if isRange(ty,tx) and startY-c+add <= ty <= startY+c-add and startX-c+add <= tx <= startX+c-add:
                    #값 두개를 치환해준다
                    board[ty][tx],board[y][x] = board[y][x], board[ty][tx]
                    #다음좌표를 지금좌표로 변경해준다
                    y,x = ty,tx
                # 더이상 움직일수 없을경우
                else:
                    #멈춰준다
                    break
            #방향을 바꿔준다
            direction += 1
        add += 1

def boardPrint(board:list): 
    for i in board:
        print(i)
    print()

def calHap(board:list)->int:
    answer = sys.maxsize
    for y in range (Y):
        hap = 0
        for x in range (X):
            hap += board[y][x]
        answer = min(answer,hap)
    return answer
    
commend = []

for _ in range (K):
    #y-c, x-c 왼쪽위
    #y+c, x+c 오른쪽 아래
    #정사각형 모양으로 시계방향으로 한칸씩 돌리기
    y,x,c = map(int, sys.stdin.readline().rstrip().split())
    commend.append((y-1,x-1,c))

answer = sys.maxsize
for p in permutations(range(K),K):
    tempBoard = deepcopy(board)
    for pp in p:
        rotate(*commend[pp],tempBoard)
    answer = min(answer,calHap(tempBoard))
print(answer)
import sys
sys.stdin = open('input.txt', "r")

Y,X = map(int, sys.stdin.readline().rstrip().split())
y,x,d = map(int, sys.stdin.readline().rstrip().split())

frontDirection = {
    0:(-1,0),
    1:(0,1),
    2:(1,0),
    3:(0,-1)
}

backDirection = {
    0:(1,0),
    1:(0,-1),
    2:(-1,0),
    3:(0,1)
}

dy = (0,0,1,-1)
dx = (1,-1,0,0)

board = []
for _ in range(Y):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))

'''
0의경우 청소가 아직 안된 빈칸,
1의경우 벽

0인 경우 북쪽, 
1인 경우 동쪽, 
2인 경우 남쪽, 
3인 경우 서쪽을 바라보고 있는 것이다.

1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.

2.현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
    1.바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
    2.바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.

3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
    1.반시계 방향으로 90∘회전한다.
    2.바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
    3.1번으로 돌아간다.

'''

def printBoard(board):
    for i in board:
        print(i)
    print()
    
def isRange(y:int,x:int)->bool:
    if 0<= y < Y and 0<= x < X :
        return True

def canNearClear(y:int,x:int)->bool:
    for idx in range (4):
        ty = y+dy[idx]
        tx = x+dx[idx]
        
        if isRange(ty,tx) and board[ty][tx] == 0:
            return True
    return False
answer = 0

while True:
    # 현재 칸이 아직 청소되지 않은 경우
    if board[y][x] == 0 :
        #현재 칸을 청소한다.
        board[y][x] = 2
        answer += 1
        continue
    # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
    elif not canNearClear(y,x):
        #1.바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면
        ty = y+backDirection[d][0]
        tx = x+backDirection[d][1]
        if isRange(ty,tx) and board[ty][tx] != 1:
            #한 칸 후진하고 1번으로 돌아간다.
            y = ty
            x = tx
            continue
        else:
            #벽이라 후진할 수 없다면 작동을 멈춘다.
            break
    #현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
    else:
        #반시계 방향으로 90∘회전한다.
        d -= 1
        if d == -1:
            d = 3
        # 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
        ty = y+frontDirection[d][0]
        tx = x+frontDirection[d][1]
        
        if isRange(ty,tx) and board[ty][tx] == 0:
            y = ty
            x = tx
        continue
    
print(answer)
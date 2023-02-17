import sys
sys.stdin = open('input.txt', "r")

'''

가희는 고구마를 정말 좋아합니다.
이번에도 어김 없이 고구마 냄새가 났는데, 고구마가 보이지 않습니다. 오빠가 방 안에 고구마를 숨겨 놓았기 때문입니다.

오빠는 가희에게 하나의 게임을 제안하고, 게임의 규칙을 설명해 주었습니다. 게임 규칙은 아래와 같습니다.

가희는 1초마다 상하좌우 방향 중 한 방향으로 1번 이동하거나, 이동하지 않고 그 자리에 머무를 수 있습니다.
가희가 이동한 지점에 고구마가 있는 경우에는, 고구마를 먹습니다. 고구마를 먹는 데 걸리는 시간은 없다고 가정합니다.
가희가 고구마를 먹으면, 고구마가 다시 그 자리에 생기지 않습니다.

가희는 현재 위치에서 T초만큼 이동했을 때 고구마를 최대한 많이 먹고 싶습니다. 가희가 최대 몇 개의 고구마를 먹을 수 있는지 알려주세요.

G = 가희
S = 고구마
. = 빈칸
# = 장애물

T 최대값이 10이기 때문에
그냥 다 돌려보면 될거같음.

'''
Y,X,T = map(int, sys.stdin.readline().rstrip().split())

board = []
for _ in range (Y):
    board.append(list(sys.stdin.readline().rstrip()))
    
def findGahi():
    for y in range (Y):
        for x in range (X):
            if board[y][x] == 'G':
                return (y,x)

Gahi = findGahi()

dy = (0,0,1,-1)
dx = (1,-1,0,0)

EatGuma = [[False]*X for _ in range (Y)]

answer = 0
def DFS(y,x,Guma,cnt):
    global answer
    if cnt > T:
        return
    
    answer = max(answer, Guma)
    
    DFS(y,x,Guma,cnt+1)
    
    for idx in range (4):
        ty = y+dy[idx]
        tx = x+dx[idx]
        
        if 0<= ty < Y and 0<= tx < X and board[ty][tx] != '#':
            if board[ty][tx] == 'S' and EatGuma[ty][tx] == False:
                EatGuma[ty][tx] = True
                DFS(ty,tx,Guma+1,cnt+1)
                EatGuma[ty][tx] = False
            else:
                DFS(ty,tx,Guma,cnt+1)
            

DFS(*Gahi,0,0)
print(answer)
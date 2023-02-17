import sys
from copy import deepcopy
sys.stdin = open('input.txt', "r")
'''
욱제는 학교 숙제로 크기가 8×8인 체스판에서 탈출하는 게임을 만들었다.
체스판의 모든 칸은 빈 칸 또는 벽 중 하나이다.
욱제의 캐릭터는 가장 왼쪽 아랫 칸에 있고,
이 캐릭터는 가장 오른쪽 윗 칸으로 이동해야 한다.

이 게임의 특징은 벽이 움직인다는 점이다.
1초마다 모든 벽이 아래에 있는 행으로 한 칸씩 내려가고, 가장 아래에 있어서 아래에 행이 없다면 벽이 사라지게 된다.
욱제의 캐릭터는 1초에 인접한 한 칸 또는 대각선 방향으로 인접한 한 칸으로 이동하거나, 현재 위치에 서 있을 수 있다.
이동할 때는 빈 칸으로만 이동할 수 있다.

1초 동안 욱제의 캐릭터가 먼저 이동하고, 그 다음 벽이 이동한다.
벽이 캐릭터가 있는 칸으로 이동하면 더 이상 캐릭터는 이동할 수 없다.

욱제의 캐릭터가 가장 오른쪽 윗 칸으로 이동할 수 있는지 없는지 구해보자.

'''

dy = (-1,-1,-1,0,0,1,1,1,0)
dx = (-1,0,1,-1,1,-1,0,1,0)

def printBoard():
    for i in board:
        print(i)
    print()
    
def findTimeWall():
    wall = set()
    timeToWall = {}
    # 초기 벽의 위치를 찾는다
    for y in range (8):
        for x in range (8):
            if board[y][x] =='#':
                wall.add((y,x))
                
    # 0초~ 7초 까지의 벽 상태를 저장하고, 8초 이후는 벽이 없다.
    for time in range (8):
        timeToWall[time] = deepcopy(wall)
        
        tempWall = set()
        while wall:
            ty,tx = wall.pop()
            if (ty-1) >= 6:
                continue
            tempWall.add((ty+1,tx))
        wall = tempWall
                
    return timeToWall

def canMove(y,x,time):
    if time >= 8:
        return True
    else:
        if (y,x) in timeToWall[time]:
            return False
        else:
            return True


def DFS(y,x,time):
    '''
    1초일떄 y <= 0 이면 가능
    2초일때 y <= 1 이면 가능
    3초일때 y <= 2 이면 가능
    4초일때 y <= 3 이면 가능
        ..........
    time일때 y <= time-1 이면 가능
    '''
    if y <= time-1:
        print(1)
        exit()
    
    for idx in range (9):
        ty = y+dy[idx]
        tx = x+dx[idx]
        if (0<= ty < 8 and 0<= tx < 8 and canMove(ty,tx,time) and canMove(ty,tx,time+1)):
            DFS(ty,tx,time+1)
    
    
    
                

board = []
for _ in range (8):
    board.append(list(sys.stdin.readline().rstrip()))
timeToWall = findTimeWall()

DFS(7,0,0)
print(0)
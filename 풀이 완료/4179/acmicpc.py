import sys
from collections import deque
from copy import deepcopy
sys.stdin = open('input.txt', "r")

def printBoard(board : list)->None:
    '''
    2중배열 board를 출력하는 메서드
    '''
    for i in board:
        print(i)
    print()

def findStart():
    '''
    J의 위치(시작점)을 찾는 메서드
    '''
    for y in range (Y):
        for x in range (X):
            if board[y][x] == 'J':
                return y,x

def findFire():
    '''
    초기 불의 위치를 찾는 매서드
    '''
    fire = set()
    for y in range (Y):
        for x in range (X):
            if board[y][x] == 'F':
                fire.add((y,x))
    return fire

def isRange(y:int, x:int)->bool:
    '''
    y,x가 주어진 범위를
    벗어나는지 확인하는 메서드
    '''
    if 0 <= y < Y and 0 <= x < X:
        return True
    
#4방탐색 방향
dy = (0,0,1,-1)
dx = (1,-1,0,0)

#입력받기
Y, X = map(int, sys.stdin.readline().rstrip().split())
board = []
for _ in range (Y):
    board.append(list(sys.stdin.readline().rstrip()))

#방문체크
isVisited = [[False]*X for _ in range (Y)]
#시작위치 찾기
startY,startX = findStart()
#불 위치 찾기
newFire = findFire()
#불이 있던 장소 저장
fireCheck = deepcopy(newFire)

#시작점 큐에넣고 시작
queue = deque([[startY,startX]])
time = 0



while True:
    tempQueue = deque([])
    tempFire = set()
    
    # 불 확산시키기
    for y,x in newFire:
        
        for idx in range (4):
            ty = y + dy[idx]
            tx = x + dx[idx]
            #범위를 벗어나지 않고, 벽이 아니고, 아직 불이 가지 못했을경우
            if isRange(ty,tx) and board[ty][tx] != '#' and (ty,tx) not in fireCheck:
                board[ty][tx] = 'F'
                fireCheck.add((ty,tx))
                tempFire.add((ty,tx))
    
    #이제 움직여준다
    while queue:
        y,x = queue.popleft()
        
        #만약 도착지일경우 끝낸다
        if y == 0 or y == Y-1 or x == 0 or x == X-1:
            print(time+1)
            exit(0)
        
        for idx in range (4):
            ty = y+dy[idx]
            tx = x+dx[idx]
            #범위안에 들어가고, 벽이 아니고, 불이 아니고, 방문 안했으면 고고
            if isRange(ty,tx) and board[ty][tx] != '#' and board[ty][tx] != 'F' and isVisited[ty][tx] == False: 
                isVisited[ty][tx] = True
                tempQueue.append([ty,tx])
    #큐랑 불위치 바꿔줌
    queue = tempQueue
    newFire = tempFire
    time += 1
    
    
    if len(tempFire) == 0 and len(queue) == 0:
        break
print('IMPOSSIBLE')

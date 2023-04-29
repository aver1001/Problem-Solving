import sys
from collections import deque
sys.stdin = open('input.txt', "r")
'''
S 위치에서 BFS를 진행한다. 이떄, DP를 사용해서 시간복잡도를 줄여준다.
C는 항상 2개 존재하므로, 1,2나눠서 비트연산으로 갖고있음을 확인한다.
각 방은 4방향으로 들어올수있으므로, 4방향을 확인한다.
그러므로 DP table은 Y * X * 4 * 4로 만든다.
'''
Y,X = map(int, sys.stdin.readline().rstrip().split())

DP = [[[[False]*4 for _ in range (4)]for _ in range (X)]for _ in range (Y)]
board = []
for _ in range (Y):
    board.append(list(sys.stdin.readline().rstrip()))

cnt = 1
for y in range (Y):
    for x in range (X):
        if board[y][x] == 'S':
            startLoc = (y,x)
            continue
        if board[y][x] == 'C':
            board[y][x] = cnt
            cnt += 1

def printBoard(board):
    for i in board:
        print(i)
    print()

def isGo(y,x):
    if 0<= y < Y and 0<= x < X and board[y][x] != '#':
        return True

dy = (0,0,1,-1)
dx = (1,-1,0,0)

queue = deque([[*startLoc,0,0,4]])# y,x,key,time,direction

while queue:
    y,x,key,time,direction = queue.popleft()
    
    if type(board[y][x]) == int:
        key = key|board[y][x]
    if key == 3:
        print(time)
        exit(0)

    for idx in range (4):
        #이전 움직임과 방향이 같을경우 실행하지 않는다.
        if direction == idx:
            continue
        ty = y+dy[idx]
        tx = x+dx[idx]
        
        if isGo(ty,tx):
            if DP[ty][tx][key][idx] == False:
                DP[ty][tx][key][idx] = True
                queue.append([ty,tx,key,time+1,idx])
print(-1)
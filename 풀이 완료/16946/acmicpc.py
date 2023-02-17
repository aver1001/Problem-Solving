import sys
from collections import deque
sys.stdin = open('input.txt', "r")

input = sys.stdin.readline

n,m = map(int,input().split())
board = [[-1]*(m+2)]+[[-1]+list(map(int,list(input().rstrip())))+[-1] for _ in range(n)]+[[-1]*(m+2)]
move = [(0,1),(1,0),(0,-1),(-1,0)]

for i in range(1,n+1):
    for j in range(1,m+1):
        if not board[i][j]:
            board[i][j] = -1
            q = deque([(i,j)])
            r = 1; area = set()
            while q:
                x,y = q.popleft()
                for a,b in move:
                    dx = x+a; dy = y+b
                    if not board[dx][dy]:
                        board[dx][dy] = -1
                        q.append((dx,dy))
                        r += 1
                    # 근처의 벽을 중복을 제거하여 좌표를 구한다.
                    elif board[dx][dy] > 0:
                        area.add((dx,dy))
            
            while area:
                x,y = area.pop()
                board[x][y] += r

for i in board:
    print(i)

for i in range(1,n+1):
    for j in range(1,m+1):
        if board[i][j] == -1:
            print(0,end="")
        else:
            print(board[i][j]%10,end="")
    print()
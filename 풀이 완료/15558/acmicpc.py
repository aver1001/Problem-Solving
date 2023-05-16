import sys
from collections import deque
sys.stdin = open('input.txt', "r")

N,K = map(int, sys.stdin.readline().rstrip().split())
board = []
board.append(sys.stdin.readline().rstrip())
board.append(sys.stdin.readline().rstrip())

isVisited = [[False]*N for _ in range (2)]

queue = deque([[0,0,-1]])

while queue:
    y,x,time = queue.popleft()
    if x+1 >= N or x+K >= N:
        print(1)
        exit(0)
    
    # 한 칸 앞으로 이동한다. 예를 들어, 현재 있는 칸이 i번 칸이면, i+1번 칸으로 이동한다.
    if isVisited[y][x+1] == False and board[y][x+1] == '1':
        isVisited[y][x+1] = True
        queue.append([y,x+1,time+1])
    
    # 한 칸 뒤로 이동한다. 예를 들어, 현재 있는 칸이 i번 칸이면, i-1번 칸으로 이동한다.
    if isVisited[y][x-1] == False and board[y][x-1] == '1' and x-1 > time+1:
        isVisited[y][x-1] = True
        queue.append([y,x-1,time+1])
    
    # 반대편 줄로 점프한다. 이때, 원래 있던 칸보다 k칸 앞의 칸으로 이동해야 한다. 예를 들어, 현재 있는 칸이 왼쪽 줄의 i번 칸이면, 오른쪽 줄의 i+k번 칸으로 이동해야 한다.
    if isVisited[not y][x+K] == False and board[not y][x+K] == '1':
        isVisited[not y][x+K] = True
        queue.append([not y, x+K,time+1])

print(0)

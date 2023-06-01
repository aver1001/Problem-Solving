import sys
from copy import deepcopy
sys.stdin = open('input.txt', "r")

board = []
Y,X = map(int, sys.stdin.readline().rstrip().split())
for _ in range (Y):
    board.append(sys.stdin.readline().rstrip())
K = int(sys.stdin.readline().rstrip())

'''
dfs + backTracking?

최대 경우의수
2^열의개수 => 2^50 불가능

bruteForce 진행 불가
backTracking 할수있는 부분?
모든행이 다 켜져있을때 -> 불이켜져있다
그렇다면 한 열씩 진행하면서, 지금까지 다 켜져있던것들의 개수가 탐색했던 최대보다는 커야만 진행.

'''
check = [False]*Y
answer = 0
for y in range (Y):
    
    if check[y]:
        continue
    
    cnt = 0
    
    for x in range (X):
        if board[y][x] == '0':
            cnt += 1
    
    
    if cnt <= K and cnt % 2 == K % 2:
        hap = 0
        for yy in range (Y):
            if board[y] == board[yy]:
                check[yy] = True
                hap += 1
        answer = max(hap,answer)
print(answer)
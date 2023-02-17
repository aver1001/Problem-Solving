import sys
from collections import deque
sys.stdin = open('input.txt', "r")

Y,X = map(int, sys.stdin.readline().rstrip().split())
board = []
for _ in range (Y):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))
    

def printBoard(board):
    for i in board:
        print(i)
    print()
        

dy = (0,0,1,-1)
dx = (1,-1,0,0)

def MeltCheese():
    check = [[0]*X for _ in range (Y)]
    isMelt = False
    
    queue = deque([(0,0)])
    
    while queue:
        y,x = queue.popleft()
        for idx in range (4):
            ty = dy[idx] + y
            tx = dx[idx] + x
            
            if 0<= ty < Y and 0<= tx < X:
                
                #아직 방문하지 못했을 경우
                if check[ty][tx] == 0:
                    #치즈일경우
                    if board[ty][tx] == 1:
                        check[ty][tx] += 1
                    #빈칸일경우
                    elif board[ty][tx] == 0:
                        check[ty][tx] = -1
                        queue.append((ty,tx))
                #이미 방문한 빈칸일경우
                elif check[ty][tx] == -1:
                    continue
                #공기와 맞닿은 치즈 일 경우
                else:
                    check[ty][tx] += 1
                    #공기와 2면 이상 닿았을경우
                    if check[ty][tx] >= 2:
                        board[ty][tx] = 0
                        isMelt = True
                    
    return isMelt
                
        
answer = 0
while MeltCheese():
    answer += 1
print(answer)
import sys
sys.stdin = open('input.txt', "r")
N = int(sys.stdin.readline().rstrip())

def makeDragonCurve():
    DragonCurve = [0]
    for i in range (10):
        lenArr = len(DragonCurve)
        for idx in range (lenArr-1,-1,-1):
            DragonCurve.append((DragonCurve[idx]+1) % 4)

    return DragonCurve

def drawDragonCurve(x,y,d,g):
    Y = y
    X = x
    # print(1<<(g-1))
    board[Y][X] = 1
    for idx in range(1<<(g)):
        Y += dy[(DragonCurve[idx] + d) %4]
        X += dx[(DragonCurve[idx] + d) %4]
        board[Y][X] = 1
        
def calAnswer():
    answer = 0
    for y in range (100):
        for x in range (100):
            if (board[y][x] == board[y+1][x] == board[y][x+1] == board[y+1][x+1] == 1):
                answer += 1
    return answer

def printBoard():
    for i in board:
        print(i)
    print()
DragonCurve = makeDragonCurve()
board = [[0]*(101) for _ in range (101)]
dy = (0,-1,0,1)
dx = (1,0,-1,0)

for _ in range (N):
    # x와 y는 드래곤 커브의 시작 점, d는 시작 방향, g는 세대이다.
    x,y,d,g = map(int, sys.stdin.readline().rstrip().split())
    drawDragonCurve(x,y,d,g)
    #printBoard()
print(calAnswer())

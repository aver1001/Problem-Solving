import sys
sys.stdin = open('input.txt', "r")

def printBoard(board):
    for i in board:
        print(i)
    print()

def isBuild(x:int ,y:int):
    if (x + 1 >= X or y + 1 >= Y):
        return False
    if (board[y][x] or board[y + 1][x] or board[y][x + 1] or board[y + 1][x + 1]):
        return False
    return True    

def DFS(y:int,x:int,cnt:int):
    if (x >= X - 1) :
        x = 0
        y+= 1

    if (y == Y - 1) :
        if (ans < cnt):
            ans = cnt
        return
    
    if (x == 0) :
        bit = 0
        for y in range (Y):
            bit |= (board[y][x] << y)
        if (DP[y][x] >= cnt):
            return
        DP[y][bit] = cnt

    if (isBuild(y,x)) :
        board[y][x] = board[y + 1][x] = board[y][x + 1] = board[y + 1][x + 1] = 1
        DFS(x + 2, y, cnt + 1)
        board[y][x] = board[y + 1][x] = board[y][x + 1] = board[y + 1][x + 1] = 0

    DFS(y,x+1, cnt)

T = int(sys.stdin.readline())
for test_case in range (1,T+1):
    Y,X = map(int,sys.stdin.readline().rstrip().split())
    board = []
    DP = [[-1]*X for _ in range (Y)]
    
    for _ in range (Y):
        board.append(list(map(int,sys.stdin.readline().rstrip().split())))
        
    answer = 0
    DFS(0,0,0)
    print(f"#{test_case} {answer}")
    printBoard(DP)
    
    

            

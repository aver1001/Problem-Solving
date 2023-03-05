import sys
from collections import deque
sys.stdin = open('input.txt', "r")

def printBoard(board):
    for i in board:
        print(i)
    print()
    
def isRange(y,x):
    if (0<= y < N and 0<= x < N):
        return True
    return False
stright = {1,2}
turn = {3,4,5,6}

T = int(sys.stdin.readline().rstrip())
for test_case in range (1,T+1):
    N = int(sys.stdin.readline().rstrip())
    
    board = []
    MAX_COST = N*N
    DP = [[[MAX_COST]*4 for _ in range(N+1)]for _ in range (N+1)]
    for y in range (N):
        board.append(list(map(int,sys.stdin.readline().rstrip().split())))
        board[y].append(0)
    board.append([0]*(N))
    for y in range (N):
        for x in range (N):
            if board[y][x] in stright:
                board[y][x] = 1
            elif board[y][x] in turn:
                board[y][x] = 2
                
    queue = deque([(0,0,0,2)])    #y,x,cnt,d
    DP[0][0][2] = 0
    # 0 : D
    # 1 : U
    # 2 : L
    # 3 : R
    
    while queue:
        y,x,cnt,d = queue.popleft()
        
        if board[y][x] == 1:    #직선파이프일경우   
            if d == 0:  #D  아래에서 왔다면
                if isRange(y-1,x) and DP[y-1][x][0] > cnt+1:    #나는 위로 올라가주고
                    DP[y-1][x][0] = cnt+1
                    queue.append((y-1,x,cnt+1,0))               #윗 친구 입장에서는 나는 아래에서 왔을것
            elif d == 1: #U 위에서 왔다면
                if isRange(y+1,x) and DP[y+1][x][1] > cnt+1:    #나는 밑으로 내려주고
                    DP[y+1][x][1] = cnt+1
                    queue.append((y+1,x,cnt+1,1))               #밑 친구 입장에선 난 위에서 왔을것임
            elif d == 2: #L 왼쪽에서 왔다면
                if isRange(y,x+1) and DP[y][x+1][2] > cnt+1:    #나는 오른쪽으로 이동하고
                    DP[y][x+1][2] = cnt+1
                    queue.append((y,x+1,cnt+1,2))               #오른쪽 친구 입장에서 나는 왼쪽에서 왔을것
            elif d == 3: #R 오른쪽에서 왔다면
                if isRange(y,x-1) and DP[y][x-1][3] > cnt+1:    #나는 왼쪽으로 이동하고
                    DP[y][x-1][3] = cnt+1
                    queue.append((y,x-1,cnt+1,3))               #왼쪽 친구 입장에서 나는 오른쪽에서 왔을것
                    
        elif board[y][x] == 2:  #곡선파이프일경우
            if d == 2 or d == 3:      #좌우에서 왔을경우
                #나는 위아래로 움직여줘야함.
                if isRange(y-1,x) and DP[y-1][x][0] > cnt +1:      #위로 이동할경우 윗친구 입장에선 아래에서 왔을것
                    DP[y-1][x][0] = cnt+1
                    queue.append((y-1,x,cnt+1,0))
                if isRange(y+1,x) and DP[y+1][x][1] > cnt + 1:      #아래로 이동할경우 아랫친구 입장에선 위에서 왔을것
                    DP[y+1][x][1] = cnt+1
                    queue.append((y+1,x,cnt+1,1))
            if d == 0 or d == 1:      #상하 에서 올경우 좌우로 내보낸다
                if isRange(y,x-1) and DP[y][x-1][3] > cnt + 1: #왼쪽으로 이동할경우 왼쪽친구 입장에서는 오른쪽에서 왔을것
                    DP[y][x-1][3] = cnt+1
                    queue.append((y,x-1,cnt+1,3))
                if isRange(y,x+1) and DP[y][x+1][2] > cnt + 1:
                    DP[y][x+1][2] = cnt + 1
                    queue.append((y,x+1,cnt+1,2))
        else:                   #빈곳일경우
            continue
    printBoard(board)
    printBoard(DP)
    print(f"#{test_case} {min(DP[N-1][N])}")
   



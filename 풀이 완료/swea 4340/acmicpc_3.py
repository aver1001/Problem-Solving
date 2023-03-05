
def printBoard(board):
    for i in board:
        print(i)
    print()
    
def isRange(y,x):
    if (0<= y < N+1 and 0<= x < N+1):
        return True
    return False

def DFS(y,x,cnt,d):
    isVistied[y][x] = True
    if board[y][x] == 1:    #직선파이프일경우   
        if d == 0:  #D  아래에서 왔다면
            if isRange(y-1,x) and DP[y-1][x][0] > cnt+1 and isVistied[y-1][x] == False:    #나는 위로 올라가주고
                DP[y-1][x][0] = cnt+1
                DFS(y-1,x,cnt+1,0)
        elif d == 1: #U 위에서 왔다면
            if isRange(y+1,x) and DP[y+1][x][1] > cnt+1 and isVistied[y+1][x] == False:    #나는 밑으로 내려주고
                DP[y+1][x][1] = cnt+1
                DFS(y+1,x,cnt+1,1)               #밑 친구 입장에선 난 위에서 왔을것임
        elif d == 2: #L 왼쪽에서 왔다면
            if isRange(y,x+1) and DP[y][x+1][2] > cnt+1 and isVistied[y][x+1] == False:    #나는 오른쪽으로 이동하고
                DP[y][x+1][2] = cnt+1
                DFS(y,x+1,cnt+1,2)               #오른쪽 친구 입장에서 나는 왼쪽에서 왔을것
        elif d == 3: #R 오른쪽에서 왔다면
            if isRange(y,x-1) and DP[y][x-1][3] > cnt+1 and isVistied[y][x-1] == False:    #나는 왼쪽으로 이동하고
                DP[y][x-1][3] = cnt+1
                DFS(y,x-1,cnt+1,3)               #왼쪽 친구 입장에서 나는 오른쪽에서 왔을것
                    
    elif board[y][x] == 2:  #곡선파이프일경우
        if d == 2 or d == 3:      #좌우에서 왔을경우
            #나는 위아래로 움직여줘야함.
            if isRange(y-1,x) and DP[y-1][x][0] > cnt +1 and isVistied[y-1][x] == False:      #위로 이동할경우 윗친구 입장에선 아래에서 왔을것
                DP[y-1][x][0] = cnt+1
                DFS(y-1,x,cnt+1,0)
            if isRange(y+1,x) and DP[y+1][x][1] > cnt + 1 and isVistied[y+1][x] == False:      #아래로 이동할경우 아랫친구 입장에선 위에서 왔을것
                DP[y+1][x][1] = cnt+1
                DFS(y+1,x,cnt+1,1)
        if d == 0 or d == 1:      #상하 에서 올경우 좌우로 내보낸다
            if isRange(y,x-1) and DP[y][x-1][3] > cnt + 1 and isVistied[y][x-1] == False: #왼쪽으로 이동할경우 왼쪽친구 입장에서는 오른쪽에서 왔을것
                DP[y][x-1][3] = cnt+1
                DFS(y,x-1,cnt+1,3)
            if isRange(y,x+1) and DP[y][x+1][2] > cnt + 1 and isVistied[y][x+1] == False:
                DP[y][x+1][2] = cnt + 1
                DFS(y,x+1,cnt+1,2)
    isVistied[y][x] = False

stright = {1,2}
turn = {3,4,5,6}

T = int(input().rstrip())
for test_case in range (1,T+1):
    N = int(input().rstrip())
    
    tempBoard = []
    MAX_COST = N*N
    
    for y in range (N):
        tempBoard.append(list(map(int,input().rstrip().split())))
    for y in range (N):
        for x in range (N):
            if tempBoard[y][x] in stright:
                tempBoard[y][x] = 1
            elif tempBoard[y][x] in turn:
                tempBoard[y][x] = 2
    # 0 : D
    # 1 : U
    # 2 : L
    # 3 : R
    DP = [[[MAX_COST]*4 for _ in range(N+1)]for _ in range (N+1)]
    isVistied = [[False]*(N+1) for _ in range(N+1)]
    board = [[0]*(N+1) for _ in range (N+1)]
    for y in range (N):
        for x in range (N):
            board[y][x] = tempBoard[y][x]
    DP[0][0][2] = 0
    DFS(0,0,0,2)
    A1 = min(DP[N-1][N])
    
    DP = [[[MAX_COST]*4 for _ in range(N+1)]for _ in range (N+1)]
    board = [[0]*(N+1) for _ in range (N+1)]
    isVistied = [[False]*(N+1) for _ in range(N+1)]
    for y in range (N):
        for x in range (N):
            board[y+1][x+1] = tempBoard[y][x]
    DP[N][N][3] = 0
    DFS(N,N,0,3)
    A2 = min(DP[1][0])
    
    print(f"#{test_case} {min(A1,A2)}")
    
    
   



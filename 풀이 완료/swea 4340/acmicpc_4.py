import time

def printBoard(board):
    for i in board:
        print(i)
    print()
    
def isRange(y,x):
    if (0<= y < N and 0<= x < N+1):
        return True
    return False

def DFS(y,x,cnt,d):
    global answer
    if (y == x == 0):
        answer = min(answer,cnt)
        return 
    
    if (x+y+cnt >= answer):
        return
    
    isVistied[y][x] = True
    if board[y][x] == 1:    #직선파이프일경우   
        if d == 0:  #D  아래에서 왔다면
            if isRange(y-1,x) and isVistied[y-1][x] == False:    #나는 위로 올라가주고
                DFS(y-1,x,cnt+1,0)
        elif d == 1: #U 위에서 왔다면
            if isRange(y+1,x) and isVistied[y+1][x] == False:    #나는 밑으로 내려주고
                DFS(y+1,x,cnt+1,1)               #밑 친구 입장에선 난 위에서 왔을것임
        elif d == 2: #L 왼쪽에서 왔다면
            if isRange(y,x+1) and isVistied[y][x+1] == False:    #나는 오른쪽으로 이동하고
                DFS(y,x+1,cnt+1,2)               #오른쪽 친구 입장에서 나는 왼쪽에서 왔을것
        elif d == 3: #R 오른쪽에서 왔다면
            if isRange(y,x-1) and isVistied[y][x-1] == False:    #나는 왼쪽으로 이동하고
                DFS(y,x-1,cnt+1,3)               #왼쪽 친구 입장에서 나는 오른쪽에서 왔을것
                    
    elif board[y][x] == 2:  #곡선파이프일경우
        if d == 2 or d == 3:      #좌우에서 왔을경우
            #나는 위아래로 움직여줘야함.
            if isRange(y-1,x) and isVistied[y-1][x] == False:      #위로 이동할경우 윗친구 입장에선 아래에서 왔을것
                DFS(y-1,x,cnt+1,0)
            if isRange(y+1,x) and isVistied[y+1][x] == False:      #아래로 이동할경우 아랫친구 입장에선 위에서 왔을것
                DFS(y+1,x,cnt+1,1)
        if d == 0 or d == 1:      #상하 에서 올경우 좌우로 내보낸다
            if isRange(y,x-1) and isVistied[y][x-1] == False: #왼쪽으로 이동할경우 왼쪽친구 입장에서는 오른쪽에서 왔을것
                DFS(y,x-1,cnt+1,3)
            if isRange(y,x+1) and isVistied[y][x+1] == False:
                DFS(y,x+1,cnt+1,2)
    isVistied[y][x] = False
    
start = time.time()

stright = {1,2}
turn = {3,4,5,6}

T = int(input().rstrip())
for test_case in range (1,T+1):
    N = int(input().rstrip())
    
    board = []
    MAX_COST = N*N
    for y in range (N):
        board.append([0]+list(map(int,input().rstrip().split())))
    for y in range (N):
        for x in range (1,N+1):
            if board[y][x] in stright:
                board[y][x] = 1
            elif board[y][x] in turn:
                board[y][x] = 2
                
    answer = MAX_COST
    
    # 0 : D
    # 1 : U
    # 2 : L
    # 3 : R
    
    isVistied = [[False]*(N+1) for _ in range(N)]
    DFS(N-1,N,0,3)
    print(f"#{test_case} {answer}")
    
   


print(time.time()-start)
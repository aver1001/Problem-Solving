import sys
sys.stdin = open('input.txt', "r")
sys.setrecursionlimit(1000000)
N = int(sys.stdin.readline().rstrip())
board = []
for _ in range (N):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))
    
'''
0,0 을 기준으로 잡고 오른쪽으로 이동
더이상 오른쪽으로 갈 수 없으면 아래로 이동
'''

def divide():
    white = []
    black = []
    x,y = 0,0
    isWhite = True
    while True:
        sub = 0
        temp = set()
        while True:
            tx = x-sub
            ty = y+sub
            
            if 0<= ty < N and 0<= tx < N:
                temp.add((ty,tx))
                sub += 1
            else:
                if isWhite:
                    white.append(temp)
                else:
                    black.append(temp)
                break
        
        
        
        if x+1 < N:
            x += 1
        elif y+1 < N:
            y += 1
        else:
            break
        
        
        isWhite = not isWhite
        
    return white,black

def numberling1():
    board = [[0]*N for _ in range (N)]
    y = 0
    x = 0
    cnt = 0
    while True:
        sub = 0
        while True:
            tx = x-sub
            ty = y+sub
            
            if 0<= ty < N and 0<= tx < N:
                board[ty][tx] = cnt
                sub += 1
            else:
                break
        cnt += 1
        
        if x+1 < N:
            x += 1
        elif y+1 < N:
            y += 1
        else:
            break
        
    # for i in board:
    #     print(i)
    # print()
    
    return board
    
def numberling2():
    board = [[0]*N for _ in range (N)]
    y = 0
    x = N-1
    cnt = 0
    while True:
        sub = 0
        while True:
            tx = x+sub
            ty = y+sub
            
            if 0<= ty < N and 0<= tx < N:
                board[ty][tx] = cnt
                sub += 1
            else:
                break
        cnt += 1
        
        if 0<= x-1 < N:
            x -= 1
        elif 0<= y+1 < N:
            y += 1
        else:
            break
        
    # for i in board:
    #     print(i)
    # print()
    
    return board
    
b1 = numberling1()
b2 = numberling2()


boardN = N*2 -1
b1Arr = [set() for _ in range (boardN)]
b2Arr = [set() for _ in range (boardN)]

for y in range (N):
    for x in range (N):
        if board[y][x] == 1:
            b1Arr[b1[y][x]].add(b2[y][x])
            b2Arr[b2[y][x]].add(b1[y][x])

def DFS(idx):
    global visited
    if visited[idx] == True:
        return False
    
    visited[idx] = True
    
    for choose in b1Arr[idx]:
        #반대편이 매칭되지 않았거나. || 다른점을 움직여서 매칭이 가능하다면 매칭성공
        if answer[choose] == -1 or DFS(answer[choose]):
            answer[choose] = idx
            return True
        
    return False
    
answer = [-1] * boardN
a = 0
for i in range (boardN):
    visited = [False]*boardN
    if DFS(i):
        a += 1
print(a)
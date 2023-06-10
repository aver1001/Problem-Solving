import sys
sys.setrecursionlimit(9999)
sys.stdin = open('input.txt', "r")

direction = {
    'U':(-1,0),
    'R':(0,1),
    'D':(1,0),
    'L':(0,-1),
}

def calAnswer() -> int :
    answer = 0
    for y in range (Y):
        for x in range (X):
            if boardState[y][x] == 1:
                answer += 1
    return answer 

def isRange(y:int, x:int) -> bool:
    
    if 0<= y < Y and 0<= x <X:
        return True
    return False

def BoardPrint(board):
    for i in board:
        print(i)
    print()

def DFS(y:int,x:int) -> int:
    #벗어나면 탈출성공
    if isRange(y,x) == False:
        return 1
    
    #이미 방문한곳이면 원래 적어놨던거로 적용한다
    if isVisted[y][x]:
        if boardState[y][x] == 0 :
            boardState[y][x] = -1
            return -1
        else:
            return boardState[y][x]
    
    isVisted[y][x] = True
    
    #방문 안했을경우
    if boardState[y][x] == 0:
        boardState[y][x] = DFS(direction[board[y][x]][0]+y, direction[board[y][x]][1]+x)
        return boardState[y][x]
    #True일경우
    elif boardState[y][x] == 1:
        return 1
    #False일경우
    elif boardState[y][x] == -1:
        return -1
    
    

Y,X = map(int, sys.stdin.readline().rstrip().split())

board = []
for _ in range (Y):
    board.append(list(sys.stdin.readline().rstrip()))
    
boardState = [[0]*X for _ in range (Y)]
isVisted = [[False]*X for _ in range (Y)]

for y in range (Y):
    for x in range (X):
        DFS(y,x)
        
print(calAnswer())
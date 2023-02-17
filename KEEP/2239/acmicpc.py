import sys
sys.stdin = open('input.txt', "r")

board = []
for _ in range (9):
    board.append(list(map(int, list(sys.stdin.readline().rstrip()))))
    
def printBoard():
    for i in board:
        print(i)
    print()
    
def findSection(y,x):
    
    if 0<= y <= 2:
        if 0<= x<= 2:
            return 1
        elif 3<=x<=5:
            return 2
        elif 6<=x<=8:
            return 3
        
    elif 3<=y<=5:
        if 0<= x<= 2:
            return 4
        elif 3<=x<=5:
            return 5
        elif 6<=x<=8:
            return 6

    elif 6<=y<=8:
        if 0<= x<= 2:
            return 7
        elif 3<=x<=5:
            return 8
        elif 6<=x<=8:
            return 9
        
section = {
    1:[(0,0),(0,1),(0,2),
       (1,0),(1,1),(1,2),
       (2,0),(2,1),(2,2)],
    2:[(0,3),(0,4),(0,5),
       (1,3),(1,4),(1,5),
       (2,3),(2,4),(2,5)],
    3:[(0,6),(0,7),(0,8),
       (1,6),(1,7),(1,8),
       (2,6),(2,7),(2,8)],
    
    4:[(3,0),(3,1),(3,2),
       (4,0),(4,1),(4,2),
       (5,0),(5,1),(5,2)],
    5:[(3,3),(3,4),(3,5),
       (4,3),(4,4),(4,5),
       (5,3),(5,4),(5,5)],
    6:[(3,6),(3,7),(3,8),
       (4,6),(4,7),(4,8),
       (5,6),(5,7),(5,8)],
    
    7:[(6,0),(6,1),(6,2),
       (7,0),(7,1),(7,2),
       (8,0),(8,1),(8,2)],
    8:[(6,3),(6,4),(6,5),
       (7,3),(7,4),(7,5),
       (8,3),(8,4),(8,5)],
    9:[(6,6),(6,7),(6,8),
       (7,6),(7,7),(7,8),
       (8,6),(8,7),(8,8)],
    
}

def DFS():
    printBoard()
    
    for y in range (9):
        for x in range (9):
            if board[y][x] == 0:
                #구역확인
                #set으로 가능한것들 적어놓기
                temp = set()
                
                for tx in range (9):
                    temp.add(board[y][tx])
                for ty in range (9):
                    temp.add(board[ty][x])
                
                for ty,tx in section[findSection(y,x)]:
                    temp.add(board[ty][tx])
                    
                for idx in range (1,10):
                    if idx in temp:
                        continue
                    board[y][x] = idx
                    DFS()
                    board[y][x] = 0
                
                return
            if y == 8 and x == 8:
                printBoard()    
                exit()
    
    
    
DFS()
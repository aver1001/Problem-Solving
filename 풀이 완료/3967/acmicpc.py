import sys
sys.stdin = open('input.txt', "r")

visited = [False]*13
star=[]
for _ in range (5):
    star.append(list(sys.stdin.readline().rstrip()))

cnt = 0
for y in range (5):
    for x in range(9):
        if star[y][x] == 'x':
            cnt += 1

def check():
    if ((ord(star[0][4]) - ord('A') + 1) + (ord(star[1][3]) - ord('A') + 1) + (ord(star[2][2]) - ord('A') + 1) + (ord(star[3][1]) - ord('A') + 1) != 26): return False
    if ((ord(star[0][4]) - ord('A') + 1) + (ord(star[1][5]) - ord('A') + 1) + (ord(star[2][6]) - ord('A') + 1) + (ord(star[3][7]) - ord('A') + 1) != 26): return False
    if ((ord(star[1][1]) - ord('A') + 1) + (ord(star[1][3]) - ord('A') + 1) + (ord(star[1][5]) - ord('A') + 1) + (ord(star[1][7]) - ord('A') + 1) != 26): return False
    if ((ord(star[3][1]) - ord('A') + 1) + (ord(star[3][3]) - ord('A') + 1) + (ord(star[3][5]) - ord('A') + 1) + (ord(star[3][7]) - ord('A') + 1) != 26): return False
    if ((ord(star[4][4]) - ord('A') + 1) + (ord(star[3][3]) - ord('A') + 1) + (ord(star[2][2]) - ord('A') + 1) + (ord(star[1][1]) - ord('A') + 1) != 26): return False
    if ((ord(star[4][4]) - ord('A') + 1) + (ord(star[3][5]) - ord('A') + 1) + (ord(star[2][6]) - ord('A') + 1) + (ord(star[1][7]) - ord('A') + 1) != 26): return False

    return True



def DFS(y:int,x:int,n:int):
    
    if(n == cnt):
        if(check() == True): # x의 개수와 방문한 수가 같으면 종료
            for s in star:
                print(''.join(s))
            exit(0)
        return
    
    if x == 8:
        nextX = 0
        nextY = y+1
    else:
        nextX = x+1
        nextY = y
        
    if star[y][x] != 'x':
        DFS(nextY,nextX,n)
        
    for i in range (12):
        if(visited[i] == True):
            continue
        visited[i] = True
        star[y][x] = chr(i + ord('A'))
        DFS(nextY,nextX, n+1)
        star[y][x] = 'x'
        visited[i] = False

DFS(0,0,0)
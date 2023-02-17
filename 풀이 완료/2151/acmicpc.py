import sys
from collections import deque
sys.stdin = open('input.txt', "r")
'''
채영이는 거울을 들여다 보는것을 참 좋아한다.
그래서 집 곳곳에 거울을 설치해두고 집 안을 돌아다닐 때 마다 거울을 보곤 한다.

채영이는 새 해를 맞이하여 이사를 하게 되었는데,
거울을 좋아하는 그녀의 성격 때문에 새 집에도 거울을 매달만한 위치가 여러 곳 있다.
또한 채영이네 새 집에는 문이 두개가 있는데,
채영이는 거울을 잘 설치하여 장난을 치고 싶어졌다.
즉, 한쪽 문에서 다른 쪽 문을 볼 수 있도록 거울을 설치하고 싶어졌다.
채영이네 집에 대한  정보가 주어졌을때, 한 쪽 문에서 다른 쪽 문을 볼 수 있도록 하기 위해 설치해야 하는 거울의 최소 개수를 구하는 프로그램을 구하시오

거울을 설치할 때에는 45도 기울어진 대각선 방향으로 설치해야 한다.
또한 모든 거울은 양면 거울이기 때문에 양 쪽 모두에서 반사가 일어날 수 있다.
채영이는 거울을 매우 많이 가지고 있어서 거울이 부족한 경우는 없다고 하자.

거울을 어떻게 설치헤도 한쪽 문에서 다른 쪽 문을 볼 수 없는 경우는 주어지지 않는다.

첫째 줄에 집의 크기 N이 주어진다 (2~50)다음 N개의 줄에는 N개의 문자로 집에 대한 정보가 주어진다.
# 은 문이 설치된 곳으로 항상 두 곳이며.
. 은 아무 것도 없는 것으로 빛은 이 곳을 통과한다.
! 은 거울을 설치할 수 있는 위치를 나타내고
*은 빛이 통과할 수 없는 벽을 나타낸다.
'''
N = int(sys.stdin.readline().rstrip())
board = []
for _ in range (N):
    board.append(list(sys.stdin.readline().rstrip()))

def printBoard(board):
    for i in board:
        print(i)
    print()
    
def findDoor() -> tuple:
    for y in range (N):
        for x in range (N):
            if board[y][x] == '#':
                return (y,x)
            
direction = {
    0: (0,1),
    1: (0,-1),
    2: (1,0),
    3: (-1,0)
}
dy = (-1,-1,1,1)
dx = (-1,1,-1,1)
check = [[[N*N]*4 for _ in range (N)]for _ in range (N)]
y,x = findDoor()
board[y][x] = '!'
queue = deque([(y,x,0,0),(y,x,0,1),(y,x,0,2),(y,x,0,3)])
while queue:
    y,x,cnt,d= queue.popleft()
    
    if check[y][x][d] < cnt:
        continue
    
    check[y][x][d] = cnt
        
    #문일경우
    if board[y][x] == '#':
        continue
    #빈곳일경우
    if board[y][x] == '.':
        ty = y+direction[d][0]
        tx = x+direction[d][1]
        if 0<= ty < N and 0<= tx < N:
            queue.append((ty,tx,cnt,d))
    #거울설치가능할경우
    if board[y][x] == '!':
        for idx in range (4):
            ty = y+direction[idx][0]
            tx = x+direction[idx][1]
            
            
            
            if 0<= ty < N and 0<= tx < N:
                if d == idx:
                    queue.append((ty,tx,cnt,idx))
                else:
                    queue.append((ty,tx,cnt+1,idx))
    #빛이 통과하지 못하는 벽일경우
    if board[y][x] == '*':
        continue
y,x = findDoor()
printBoard(check)
print(min(check[y][x]))
            


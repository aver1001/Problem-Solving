import sys
from collections import deque
sys.stdin = open('input.txt', "r")

X, Y = map(int, sys.stdin.readline().rstrip().split())
K = int(sys.stdin.readline().rstrip())

XInfo = {}
YInfo = {}
for _ in range (K):
    b ,sx, sy, dx, dy= map(int, sys.stdin.readline().rstrip().split())
    
    if sx == dx:
        if sx in XInfo :
            XInfo[sx].append((sx,min(sy,dy),dx,max(sy,dy)))
        else:
            XInfo[sx] = [(sx,min(sy,dy),dx,max(sy,dy))]
    
    if sy == dy :
        if sy in YInfo :
            YInfo[sy].append((min(sx,dx),sy,max(sx,dx),dy))
        else:
            YInfo[sy] = [(min(sx,dx),sy,max(sx,dx),dy)]

startX, startY, endX, endY =  map(int, sys.stdin.readline().rstrip().split())

DP = set()
DP.add((startX,startY))

queue = deque([(startX,startY,0)]) # x, y, cnt

while queue:
    nowX, nowY, cnt = queue.popleft()
    
    
    if nowX in XInfo:
        for sx,sy,dx,dy in XInfo[nowX]:
            for y in range(sy,dy+1):
                if (nowX,y) not in DP:
                    if nowX == endX and y == endY:
                        print(cnt+1)
                        exit(0)
                    DP.add((nowX,y))
                    queue.append((nowX,y,cnt+1))
    
    if nowY in YInfo:
        for sx,sy,dx,dy in YInfo[nowY]:
            for x in range(sx,dx+1):
                if (x,nowY) not in DP:
                    if x == endX and nowY == endY:
                        print(cnt+1)
                        exit(0)
                    DP.add((x,nowY))
                    queue.append((x,nowY,cnt+1))
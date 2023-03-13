import sys
from collections import deque
sys.stdin = open('input.txt', "r")

X, Y = map(int, sys.stdin.readline().rstrip().split())
K = int(sys.stdin.readline().rstrip())

def isCross(x1,y1,x2,y2,x3,y3,x4,y4):
    if ccw(x1,y1,x2,y2,x3,y3) * ccw(x1,y1,x2,y2,x4,y4) <= 0:
        return True
    else:
        return False
    

def ccw(x1,y1,x2,y2,x3,y3) :
	a = x1 * y2 + x2 * y3 + x3 * y1
	b = y1 * x2 + y2 * x3 + y3 * x1
	return a - b


table = {i :{'loc':None,'next':set()} for i in range (1,K+1)}

start = set()
end = set()

inputs = []
for _ in range (K):
    b ,sx, sy, dx, dy = map(int, sys.stdin.readline().rstrip().split())
    table[b]['loc'] = (min(sx,dx), min(sy,dy), max(sx,dx), max(sy,dy))

startX, startY, endX, endY =  map(int, sys.stdin.readline().rstrip().split())


for Ikey,Ivalue in table.items():
    #TODO start, end 찾아줘야함
    for Jkey,Jvalue in table.items():
        if Ikey == Jkey:
            continue
        if isCross(*Ivalue['loc'],*Jvalue['loc']):
            table[Ikey]['next'].add(Jkey)
            table[Jkey]['next'].add(Ikey)
            
print(table)

queue = deque([(startX,startY)])

while queue:
    x,y = queue.popleft()
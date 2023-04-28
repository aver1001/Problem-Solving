import sys
sys.stdin = open('input.txt', "r")

X, Y = map(int, sys.stdin.readline().rstrip().split())
N = int(sys.stdin.readline().rstrip())

NO = set()
DP = [[0]*(X+1) for _ in range(Y+1)]
for _ in range(N):
    x1,y1,x2,y2 = map(int, sys.stdin.readline().rstrip().split())
    NO.add((y1,x1,y2,x2))
    NO.add((y2,x2,y1,x1))

DP[0][0]= 1

for y in range(1,Y+1):
    if (y-1,0,y,0) not in NO:
        DP[y][0] = DP[y-1][0]

for x in range (1,X+1):
    if (0,x-1,0,x) not in NO:
        DP[0][x] = DP[0][x-1]

for y in range(1,Y+1):
    for x in range (1,X+1):
        if (y,x-1,y,x) not in NO:
            DP[y][x] += DP[y][x-1]
        if (y-1,x,y,x) not in NO:
            DP[y][x] += DP[y-1][x]
            
print(DP[-1][-1])

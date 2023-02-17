import sys
import heapq

sys.stdin = open('input.txt', "r")

N = int(sys.stdin.readline().rstrip())
X = []
Y = []
Z = []

for idx in range (N):
    x, y, z = map(int, sys.stdin.readline().rstrip().split())
    X.append((x,idx))
    Y.append((y,idx))
    Z.append((z,idx))

X.sort()
Y.sort()
Z.sort()
dis = []
for arr in [X,Y,Z]:
    
    for idx in range (N-1):
        dis.append((abs(arr[idx][0]-arr[idx+1][0]),arr[idx][1],arr[idx+1][1]))

dis.sort()
root = [i for i in range (N)]

answer = 0

def find(x):
    if x != root[x]:
        root[x] = find(root[x])
    return root[x]

def union(x,y):
    x = find(x)
    y = find(y)
    root[y] = x

answer = 0
cnt = N-1
for cost,a,b in dis:
    if find(a) == find(b):
        continue
    union(a,b)
    cnt -= 1
    answer += cost
    
    if cnt == 0:
        break
print(answer)
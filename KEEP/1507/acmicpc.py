import sys
sys.stdin = open('input.txt', "r")

N = int(sys.stdin.readline().rstrip())
dis = []
root = [i for i in range (N)]
route = []

def union(a,b):
    a = find(a)
    b = find(b)
    
    if a > b:
        root[a] = b
    else:
        root[b] = a

def find(x):
    if root[x] != x:
        root[x] = find(root[x])
        
    return root[x]

for _ in range (N):
    dis.append(list(map(int,sys.stdin.readline().rstrip().split())))

cal = [[9999]*N for _ in range (N)]
for a in range (N):
    for b in range (N):
        if a>b:
            route.append((dis[a][b],a,b))
            
route.sort()
answer = 0
for cost,a,b in route:
    if find(a) == find(b):
        continue
    union(a,b)
    cal[a][b] = cost
    cal[b][a] = cost
    answer += cost


'''
6 9 2 16 4 18
2 4 6 9 16 18

3 4 1 2
0 3 0 1
'''
    
for y in range (N):
    for x in range (N):
        if y == x:
            cal[y][x] = 0
            continue
        for k in range (N):
            cal[y][x] = min(cal[y][x],cal[y][k] + cal[k][x])
        
for y in range (N):
    for x in range (N):
        if y<x:
            continue
        if dis[y][x] < cal[y][x]:
            answer += dis[y][x]
        elif dis[y][x] == cal[y][x]:
            continue
        else:
            print(-1)
            exit()
            
            
            

print(answer)
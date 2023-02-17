import sys
sys.stdin = open('input.txt', "r")

N = int(sys.stdin.readline().rstrip())
table = {}
for _ in range (N):
    path = sys.stdin.readline().rstrip().split('\\')
    temp = table
    for dir in path:
        if dir not in temp:
            temp[dir] = {}
        temp = temp[dir]
        


def DFS(d,v):
    temp = list(d.keys())
    temp.sort()
    
    for t in temp:
        print((' '*v)+t)
        DFS(d[t],v+1)

DFS(table,0)
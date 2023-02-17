import sys
sys.stdin = open('input.txt', "r")

N,M = map(int, sys.stdin.readline().rstrip().split())
Root = [i for i in range (N)]


def findRoot(x):
    if x != Root[x]:
        Root[x] = findRoot(Root[x])
        
    return Root[x]

def union(a,b):
    a = findRoot(a)
    b = findRoot(b)
    
    if a > b:
        Root[a] = b
    else:
        Root[b] = a
        
cnt = 0
for _ in range (M):
    A,B = map(int, sys.stdin.readline().rstrip().split())
    cnt += 1
    if findRoot(A) == findRoot(B):
        print(cnt)
        exit()
    else:
        union(A,B)
print(0)
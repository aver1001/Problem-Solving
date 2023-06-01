import sys
sys.stdin = open('input.txt', "r")

def union(a:int,b:int):
    a = find(a)
    b = find(b)
    
    if a < b:
        root[b] = a
        size[a] += size[b]
        size[b] = 0
    elif a > b:
        root[a] = b
        size[b] += size[a]
        size[a] = 0

def find(x:int):
    if root[x] != x:
        root[x] = find(root[x])
        return root[x]
    else:
        return x
    
N = int(sys.stdin.readline().rstrip())
root = [i for i in range (1000001)]
size = [1 for _ in range (1000001)]
for _ in range (N):
    commend = sys.stdin.readline().rstrip().split()
    
    if commend[0] == 'I':
        union(int(commend[1]),int(commend[2]))
    elif commend[0] == 'Q':
        print(size[find(int(commend[1]))])
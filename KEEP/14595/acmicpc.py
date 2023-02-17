import sys
sys.setrecursionlimit(10000000)
sys.stdin = open('input.txt', "r")

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())

table = [i for i in range (N)]

def union(a,b):
    a = find(a)
    b = find(b)
    
    if a > b:
        table[a] = b
        return b
    else:
        table[b] = a
        return a


def find(x):
    if table[x] != x:
        table[x] = find(table[x])
    return table[x]

for _ in range (M):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    x -= 1
    y -= 1
    temp = y
    while True:
        temp = union(temp-1,temp)
        if temp <= x:
            break

answer = set()
for idx in range (N):
    answer.add(find(idx))
print(len(answer))

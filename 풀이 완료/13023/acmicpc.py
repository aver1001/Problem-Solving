import sys
sys.stdin = open('input.txt', "r")

N, M = map(int, sys.stdin.readline().rstrip().split(' '))

table = [[] for _ in range(N)]
visited = [False]*N

for _ in range(M):
    A, B = map(int, sys.stdin.readline().rstrip().split(' '))

    table[A].append(B)
    table[B].append(A)


def DFS(now, cnt):
    if cnt == 4:
        print(1)
        exit()

    for Next in table[now]:
        if visited[Next] == False:
            visited[Next] = True
            DFS(Next, cnt+1)
            visited[Next] = False


for i in range(N):

    visited[i] = True
    DFS(i, 0)
    visited[i] = False

print(0)

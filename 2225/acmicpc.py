import sys
sys.stdin = open('input.txt', "r")

N, K = map(int, sys.stdin.readline().rstrip().split())

global answer

answer = 0


def DFS(num, cnt):
    global answer
    #num = 0
    #cnt = 0

    for i in range(N+1):

        if num + i > N:
            continue
        if cnt+1 == K:
            if num + i == N:
                answer += 1
                answer 
            continue
        DFS(num+i, cnt+1)


DFS(0, 0)
print(answer)

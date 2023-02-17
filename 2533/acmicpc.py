import sys
sys.stdin = open('input.txt', "r")

N = int(sys.stdin.readline().rstrip())


# 먼져 방향 그래프를 이어준다 (트리)
direct = [[]for _ in range(N+1)]
for _ in range(N-1):
    A, B = map(int, sys.stdin.readline().rstrip().split(' '))
    direct[A].append(B)
    direct[B].append(A)


DP = [[0, 0] for _ in range(N+1)]  # 켜졌을경우, 꺼졌을경우
# 켜졌을경우 하위노드들의 최솟값을 가져온다.
# 꺼졌을경우 하위노드들이 켜졌을 경우를 가져온다.
check = [False]*(N+1)
# 정점 아무거나 하나를 선택한뒤 내려간다.


def DFS(now):
    check[now] = True
    DP[now][0] = 1
    for next in direct[now]:
        if check[next] == True:
            continue
        # 켜졌을경우
        DFS(next)
        DP[now][0] += min(DP[next])
        # 꺼졌을경우
        DP[now][1] += DP[next][0]


DFS(1)
print(min(DP[1]))
